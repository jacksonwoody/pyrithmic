import asyncio
import logging
import time
from datetime import datetime as dt
from typing import Union, Tuple, Callable, Dict

import pandas as pd
import pytz
from pandas import NaT

from rithmic import RithmicEnvironment, CallbackManager, CallbackId
from rithmic.interfaces.base import RithmicBaseApi
from rithmic.protocol_buffers import request_login_pb2, request_tick_bar_replay_pb2, response_tick_bar_replay_pb2
from rithmic.tools.general import set_index_no_name, is_datetime_utc
from rithmic.tools.pyrithmic_exceptions import ReferenceDataUnavailableException, DownloadErrorException
from rithmic.tools.pyrithmic_logger import logger, configure_logging


class DownloadRequest:
    """
    Download Request keeps track of the replay of historical tick data.

    It is fully finished when the complete attribute is True

    """
    def __init__(self, security_code: str, exchange_code: str, start_time: dt, end_time: dt):
        """
        Download Request init method

        :param security_code: (str) valid security code
        :param exchange_code: (str) valid exchange code
        :param start_time: (dt) start datetime in utc
        :param end_time: (dt) end datetime in utc
        """
        if is_datetime_utc(start_time) is False or is_datetime_utc(end_time) is False:
            raise ValueError('Both Start Time and End Time must be TZ Aware and in UTC')
        self.security_code = security_code
        self.exchange_code = exchange_code
        self._downloading_row_count = 0
        self.start_time = start_time
        self.end_time = end_time
        self.download_results = []
        self.complete = False
        self.tick_dataframe = pd.DataFrame([])
        self._temp_data = []
        self._last_bar_returned = False
        self.error_downloading = False

    @property
    def has_response(self):
        return len(self._temp_data) > 0 or len(
            self.download_results) > 0 or self.error_downloading or self._last_bar_returned

    def _clear_temp_data(self) -> None:
        """Clear existing temp data before new data arrives"""
        self._temp_data = []

    @property
    def download_row_count(self) -> int:
        """Get row count of ticks downloaded"""
        if self.complete:
            return len(self.tick_dataframe)
        return self._downloading_row_count

    @property
    def download_in_progress(self) -> bool:
        """Returns bool of whether download is still in progress"""
        return not self.complete

    @property
    def request_id(self) -> str:
        """Generate a request id for the download"""
        return '{0}_{1}'.format(self.security_code, self.exchange_code)

    def _mark_download_complete(self) -> None:
        """Marks download as complete"""
        self.complete = True

    def _create_tick_dataframe(self) -> None:
        """Creates Tick Dataframe once download has completed"""
        df = pd.concat(self.download_results)
        df = set_index_no_name(df, 'timestamp')
        self.tick_dataframe = df

    def _clear_interim_status(self) -> None:
        """As last bar returned on interim request and data consumed, clear the temp status of the download"""
        self._last_bar_returned = False
        self._clear_temp_data()

    @property
    def download_key(self) -> tuple:
        """Returns a tuple of security code and exchange code for mapping purposes"""
        return self.security_code, self.exchange_code

    def mark_error_downloading(self):
        self.error_downloading = True


class RithmicHistoryApi(RithmicBaseApi):
    """
    Rithmic History API For the HISTORY PLANT to download historical tick data for security/exchange combinations
    """
    infra_type = request_login_pb2.RequestLogin.SysInfraType.HISTORY_PLANT

    def __init__(self, env: RithmicEnvironment = None, callback_manager: CallbackManager = None,
                 auto_connect: bool = True, loop=None):
        """
        Rithmic History API to download historical tick data

        :param env: (RithmicEnvironment) provide a rithmic environment to connect to, if omitted, tries to get the
                    default environment from the Environment Variable RITHMIC_ENVIRONMENT_NAME
        :param auto_connect: (bool) automatically connect and log into Rithmic, defaults to True
        :param callback_manager: (CallbackManager) provide a configured manager with callbacks registered
        :param loop: (AbstractEventLoop) asyncio event loop can be provided to share/use existing loop
        """
        RithmicBaseApi.__init__(self, env, callback_manager, auto_connect, loop)
        self.current_downloads: Dict[tuple, DownloadRequest] = dict()
        self.consuming_subscription = False

    def _add_download(self, download: DownloadRequest) -> None:
        """Adds a new Download Request for tracking and use"""
        self.current_downloads[download.download_key] = download

    def get_download_by_request_id(self, request_id) -> DownloadRequest:
        """Retrieves DownloadRequest object by the request id"""
        security_code, exchange_code = request_id.split('_')
        return self.current_downloads[(security_code, exchange_code)]

    @property
    def downloads_in_progress(self) -> bool:
        """Returns True if any downloads have not completed"""
        return any(download.download_in_progress for download in self.current_downloads.values())

    @property
    def downloads_are_complete(self) -> bool:
        """Returns True if all downloads have completed"""
        return all(download.complete for download in self.current_downloads.values())

    async def _consume_subscription(self) -> None:
        """
        Consumes new messages as data is streamed, sends a heartbeat if no data received after 5 seconds and
        the websocket is still open. Starts once a historical download is requested.

        :return: None
        """
        await self.send_heartbeat()

        connected = True
        while connected:
            msg_buf = bytearray()
            waiting_for_msg = True

            while waiting_for_msg:
                try:
                    msg_buf = await asyncio.wait_for(self.recv_buffer(), timeout=5)
                    waiting_for_msg = False
                except asyncio.TimeoutError as e:
                    if self.ws.open:
                        await self.send_heartbeat()
                    else:
                        raise Exception('Connection is Closed')

                try:
                    template_id = self.get_template_id_from_message_buffer(msg_buf)
                    if template_id == 207:
                        try:
                            row, is_last_bar, request_id = self._handle_tick_data(msg_buf)
                        except ReferenceDataUnavailableException as e:
                            download = self.get_download_by_request_id(e.request_id)
                            download._last_bar_returned = True
                            download.mark_error_downloading()
                            continue
                        download = self.get_download_by_request_id(request_id)
                        if is_last_bar:
                            download._last_bar_returned = True
                        else:
                            download._temp_data.append(row)
                    elif template_id == 13:
                        connected = False
                        continue
                except Exception as e:
                    raise (e)

    def _handle_tick_data(self, msg_buf) -> Tuple[dict, bool, str]:
        """
        Processes new bytes message of tick data downloaded

        :param msg_buf: (bytes) response from rithmic
        :return: (tuple) (dict of tick data, bool if last row in sub download, request_id str)
        """
        msg = response_tick_bar_replay_pb2.ResponseTickBarReplay()
        msg.ParseFromString(msg_buf[4:])
        if msg.rp_code == ['7', 'reference data not available']:
            request_id = msg.user_msg[0]
            raise ReferenceDataUnavailableException(
                'Reference Data is Not Available for the Security requested', request_id
            )
        is_last_bar = msg.rp_code == ['0'] or msg.rq_handler_rp_code == []
        ssboe = msg.data_bar_ssboe
        usecs = msg.data_bar_usecs

        row = None
        request_id = msg.user_msg[0]
        if not is_last_bar:
            ts = '{0}.{1:06}'.format(max(ssboe), max(usecs))
            timestamp = dt.fromtimestamp(float(ts), tz=pytz.utc)
            row = dict(
                timestamp=timestamp,
                close=msg.close_price,
                security_code=msg.symbol,
                volume=msg.volume,
                bid_volume=msg.bid_volume,
                ask_volume=msg.ask_volume,
            )
        return row, is_last_bar, request_id

    async def _replay_tick_data(self, request_id: str, security_code: str, exchange_code: str, start_time: dt,
                                end_time: dt) -> None:
        """
        Creates and sends request for download of tick data for security/exchange over time period

        :param request_id: (str) generated request id used for processing as messages come in
        :param security_code: (str) valid security code
        :param exchange_code: (str) valid exchange code
        :param start_time: (dt) start time as datetime in utc
        :param end_time: (dt) end time as datetime in utc
        :return: None
        """
        rq = request_tick_bar_replay_pb2.RequestTickBarReplay()
        rq.template_id = 206
        rq.user_msg.append(request_id)
        rq.symbol = security_code
        rq.exchange = exchange_code
        rq.bar_type = request_tick_bar_replay_pb2.RequestTickBarReplay.BarType.TICK_BAR
        rq.bar_type_specifier = "1"
        rq.bar_sub_type = request_tick_bar_replay_pb2.RequestTickBarReplay.BarSubType.REGULAR
        rq.start_index = int(start_time.timestamp())
        rq.finish_index = int(end_time.timestamp())
        buf = self._convert_request_to_bytes(rq)
        await self.send_buffer(buf)
        logger.info('Requested Tick Data Replay for {0}|{1} from {2} to {3}'.format(
            security_code, exchange_code, start_time, end_time
        ))

    def _request_historical_tick_data(self, request_id: str, security_code: str, exchange_code: str, start_time: dt,
                                      end_time: dt) -> None:
        """
        Convenience method to call request to rithmic asynchronously

        :param request_id: (str) generated request id used for processing as messages come in
        :param security_code: (str) valid security code
        :param exchange_code: (str) valid exchange code
        :param start_time: (dt) start time as datetime in utc
        :param end_time: (dt) end time as datetime in utc
        :return: None
        """
        asyncio.run_coroutine_threadsafe(
            self._replay_tick_data(request_id, security_code, exchange_code, start_time, end_time), loop=self.loop
        )

    def _check_subscription(self) -> None:
        """Starts consumption routine if not already active"""
        if self.consuming_subscription is False:
            asyncio.run_coroutine_threadsafe(self._consume_subscription(), loop=self.loop)

    async def _fetch_historical_tick_data(self, download: DownloadRequest) -> None:
        """
        This method runs asynchronously per download, sending new requests as the download limits are hit.

        Sends an initial request for the full time span, each request is limited to 10000 rows. If it is not the last
        bar for the full download, it truncates to the penultimate second (to prevent ticks on same millisecond being
        missed/duplicated, then adjusts the start time and sends a new sub request. It continues until the last tick row
        for the download is finally returned.

        Can attach a callback for both the sub download results and/or the final download results, arguments for both
        callbacks is the DataFrame of results, the security code and exchange code.

        :param download: (DownloadRequest) to process
        :return: None
        """
        intermittent_cb = self.callback_manager.get_callback_by_callback_id(
            CallbackId.HISTORY_DOWNLOAD_INTERMITTENT_PROCESSING
        )
        final_cb = self.callback_manager.get_callback_by_callback_id(
            CallbackId.HISTORY_DOWNLOAD_COMPLETE_PROCESSING
        )
        self._check_subscription()
        complete = False
        request_id = download.request_id
        start_time, end_time = download.start_time, download.end_time
        while not complete:
            self._request_historical_tick_data(
                request_id, download.security_code, download.exchange_code, start_time, end_time)
            while download._last_bar_returned is False:
                await asyncio.sleep(0.5)
            if download.error_downloading:
                download._mark_download_complete()
                return
            complete, start_time = self._process_last_bar_returned(download, intermittent_cb, end_time)
        if final_cb is not None:
            df = download.tick_dataframe
            self.perform_callback(final_cb, [df, download])
        download._mark_download_complete()

    def _process_last_bar_returned(self, download: DownloadRequest, intermittent_cb: Callable,
                                   end_time: dt) -> Tuple[bool, Union[dt, None]]:
        """
        Process interim result after last bar has been returned. Returns a bool if download has fully completed
        and a start time update if not fully complete for the next request

        :param download: (DownloadRequest) The download in progress
        :param intermittent_cb: (Callbable) any callback attached for intermittent processing
        :param end_time: (dt) timestamp of original end_time requested
        :return: (tuple) boolean if download fully completed and start time adjusted for next request
        """
        complete = False
        start_time = NaT
        df = pd.DataFrame(download._temp_data)
        if len(df) == 0:
            return True, None
        download._clear_interim_status()
        last_timestamp = df.timestamp.max()
        last_timestamp_second = last_timestamp.floor('1s')
        if (last_timestamp < end_time) and (len(df) == 10000):
            df_final = df[df.timestamp < last_timestamp_second]
            start_time = last_timestamp_second
        else:
            df_final = df[:]
            complete = True
        download.download_results.append(df_final)
        download._downloading_row_count += len(df_final)
        if complete:
            download._create_tick_dataframe()
        if intermittent_cb is not None:
            self.perform_callback(intermittent_cb, [df_final, download])
        return complete, start_time

    def download_historical_tick_data(self, security_code: str, exchange_code: str, start_time: dt, end_time: dt):
        """
        Download historical tick data for a security & exchange over a time period

        Each download runs asynchronously and several can be triggered at once

        Use downloads_in_progress attribute to know when all downloads are complete

        :param security_code: security code str eg ESZ3
        :param exchange_code: exchange code str eg CME
        :param start_time: datetime to start download from in utc
        :param end_time: datetime to download up until in utc
        :return: Download request object
        """
        download = DownloadRequest(security_code, exchange_code, start_time, end_time)
        self._add_download(download)
        coro = self._fetch_historical_tick_data(download)
        asyncio.run_coroutine_threadsafe(coro, loop=self.loop)
        while download.has_response is False:
            time.sleep(0.01)
        if download.error_downloading:
            raise DownloadErrorException(
                'Error encountered on download for {0}-{1}'.format(download.security_code, download.exchange_code)
            )
        return download
