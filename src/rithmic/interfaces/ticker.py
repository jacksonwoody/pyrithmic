import asyncio

import pandas as pd

from rithmic.config.credentials import RithmicEnvironment
from rithmic.interfaces.base import RithmicBaseApi
from rithmic.callbacks.callbacks import CallbackManager, CallbackId
from rithmic.protocol_buffers import request_login_pb2, last_trade_pb2, request_market_data_update_pb2
from rithmic.tools.pyrithmic_exceptions import WebsocketClosedException, MissingCustomCallback
from rithmic.tools.pyrithmic_logger import logger, configure_logging


CONSUMPTION_RESPONSE_MAP = {
    150: dict(proto=last_trade_pb2.LastTrade, fn='process_last_trade'),
}


class RithmicTickerApi(RithmicBaseApi):
    infra_type = request_login_pb2.RequestLogin.SysInfraType.TICKER_PLANT

    def __init__(self, env: RithmicEnvironment = None, auto_connect: bool = True,
                 callback_manager: CallbackManager = None, loop=None, periodic_sync_interval_seconds: float = 0.1):
        RithmicBaseApi.__init__(self, env, callback_manager, auto_connect, loop)
        self.consuming_subscription = False
        self.streamed_data = []
        self.periodic_sync_interval_seconds = periodic_sync_interval_seconds
        self._register_periodic_sync()

    def _register_periodic_sync(self):
        has_sync_callback = self.callback_manager.get_callback_by_callback_id(CallbackId.PERIODIC_TICK_DATA_SYNCING)
        if has_sync_callback:
            asyncio.run_coroutine_threadsafe(self.periodic_syncing(), loop=self.loop)

    async def consume_subscription(self):
        """
        Consumes new messages as data is streamed, sends a heartbeat if no data received after 5 seconds and
        the websocket is still open.

        :return: None
        """
        self.consuming_subscription = True
        await self.send_heartbeat()
        while True:
            msg_buf = bytearray()
            waiting_for_msg = True
            while waiting_for_msg:
                try:
                    logger.debug('Waiting for msg...')
                    msg_buf = await asyncio.wait_for(self.ws.recv(), timeout=5)
                    waiting_for_msg = False
                except asyncio.TimeoutError:
                    if self.ws.open:
                        await self.send_heartbeat()
                    else:
                        logger.info("connection appears to be closed.  exiting consume()")
                        raise WebsocketClosedException('Websocket has closed')
            template_id = self.get_template_id_from_message_buffer(msg_buf)
            if template_id == 19:
                logger.debug('Heartbeat received')
            else:
                self.process_new_message(template_id, msg_buf)

    def process_new_message(self, template_id: int, msg_buf):
        if template_id in CONSUMPTION_RESPONSE_MAP:
            meta = CONSUMPTION_RESPONSE_MAP[template_id]
            msg = meta['proto']()
            msg.ParseFromString(msg_buf[4:])
            fn = getattr(self, meta['fn'])
            result = fn(template_id, msg)
            callback_fn = self.callback_manager.get_callback_by_template_id(template_id)
            if callback_fn is not None:
                callback_fn(result)
        else:
            print(template_id)

    def process_last_trade(self, template_id: int, msg):
        """
        Processes new tick data message as it streams in. Will add new data to the streamed_data and perform
        callback if custom callback provided

        :param template_id: int, template id of the message received over the websocket
        :param msg:
        :return:
        """
        data = self._get_row_information(template_id, msg)
        if msg.trade_size == 0:
            return
        if data['aggressor'] == 1:
            bid_volume, ask_volume = 0, data['trade_size']
        else:
            ask_volume, bid_volume = 0, data['trade_size']
        result = dict(
            timestamp=data['update_time'],
            security_code=data['symbol'],
            exchange_code=data['exchange'],
            close=data['trade_price'],
            volume=data['trade_size'],
            bid_volume=bid_volume,
            ask_volume=ask_volume,
        )
        self.process_new_tick_data(result)
        return result

    async def periodic_syncing(self):
        """
        Subscribe to periodic syncing if a custom callback is provided to handle new data every n seconds.
        Can be used to periodically process chunks of tick data, eg save new records to database in a group
        every 0.1 seconds

        :return: None
        """
        callback_fn = self.callback_manager.get_callback_by_callback_id(CallbackId.PERIODIC_TICK_DATA_SYNCING)
        if callback_fn is None:
            msg = 'Custom callback for period syncing required, use attach_periodic_sync_callback to set first'
            raise MissingCustomCallback(msg)
        complete = False
        last_row_processed = -1
        while not complete:
            df_current = self.tick_dataframe
            df = df_current.iloc[last_row_processed:]
            if len(df) > 0:
                callback_fn(df)
                last_row_processed = len(df_current)
            await asyncio.sleep(self.periodic_sync_interval_seconds)

    def process_new_tick_data(self, data):
        """
        New tick row is appended to streamed_data
        :param data: dict of tick data
        :return: None
        """
        self.streamed_data.append(data)

    def _create_subscribe_unsubscribe_request(self, security_code, exchange_code, subscribe: bool = True):
        rq = request_market_data_update_pb2.RequestMarketDataUpdate()
        rq.template_id = 100
        msg = 'subscribing' if subscribe else 'unsubscribing'
        request_type = 'SUBSCRIBE' if subscribe else 'UNSUBSCRIBE'
        rq.user_msg.append(msg)
        rq.symbol = security_code
        rq.exchange = exchange_code
        rq.request = getattr(request_market_data_update_pb2.RequestMarketDataUpdate.Request, request_type)
        last_trade = request_market_data_update_pb2.RequestMarketDataUpdate.UpdateBits.LAST_TRADE
        rq.update_bits = last_trade
        buf = self._convert_request_to_buffer(rq)
        return buf

    async def subscribe_to_market_data_stream(self, security_code: str, exchange_code: str):
        buffer = self._create_subscribe_unsubscribe_request(security_code, exchange_code, subscribe=True)
        await self.ws.send(buffer)
        logger.info(f'Subscribed to Market Data for {security_code} on {exchange_code}')

    async def unsubscribe_from_market_data_stream(self, security_code, exchange_code):
        buffer = self._create_subscribe_unsubscribe_request(security_code, exchange_code, subscribe=False)
        await self.ws.send(buffer)
        logger.info(f'Unsubscribed to Market Data for {security_code} on {exchange_code}')

    def stream_market_data(self, security_code: str, exchange_code: str):
        """
        Subscribe to a tick data streaming for a security_code and exchange_code combination, eg ESU3 and CME
        :param security_code: str security code
        :param exchange_code: str exchange code
        :return: None
        """
        if self.consuming_subscription is False:
            asyncio.run_coroutine_threadsafe(self.consume_subscription(), loop=self.loop)
        asyncio.run_coroutine_threadsafe(
            self.subscribe_to_market_data_stream(security_code, exchange_code), loop=self.loop
        )

    def stop_market_data_stream(self, security_code: str, exchange_code: str):
        """
               Unsubscribe to a tick data streaming for a security_code and exchange_code combination, eg ESU3 and CME
               :param security_code: str security code
               :param exchange_code: str exchange code
               :return: None
               """
        if self.consuming_subscription is False:
            return
        asyncio.run_coroutine_threadsafe(
            self.unsubscribe_from_market_data_stream(security_code, exchange_code), loop=self.loop
        )

    @property
    def tick_dataframe(self):
        data = self.streamed_data[:]
        return pd.DataFrame(data)


if __name__ == '__main__':
    configure_logging(logger)
    callbacks = CallbackManager()
    callbacks.register_callback(CallbackId.PERIODIC_TICK_DATA_SYNCING, lambda x: print(x.tail()))
    callbacks.register_callback(CallbackId.LAST_TRADE, lambda x: print('New Tick data received'))
    r = RithmicTickerApi(RithmicEnvironment.RITHMIC_PAPER_TRADING, callback_manager=callbacks, auto_connect=True)
    r.stream_market_data('ESU3', 'CME')
    r.stream_market_data('NQU3', 'CME')
    x =1

