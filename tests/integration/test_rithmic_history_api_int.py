import time as timemod
from datetime import datetime as dt, date, time

import pytest
import pytz
from pandas import DataFrame

from rithmic import CallbackManager, CallbackId
from rithmic.interfaces.history.history_api import DownloadRequest
from rithmic.tools.general import get_utc_now, find_nearest_day_of_week, DayOfWeek
from rithmic.tools.pyrithmic_exceptions import DownloadErrorException


ES = 'ES'
NQ = 'NQ'
EXCHANGE_CODE = 'CME'


def test_history_api_download_tick_data(history_api, ticker_api):
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    security_code2 = ticker_api.get_front_month_contract(NQ, EXCHANGE_CODE)
    assert history_api.downloads_in_progress is False
    prev_thurs = find_nearest_day_of_week(date.today(), DayOfWeek.THURSDAY)
    start_time = dt.combine(prev_thurs, time(1, 0), tzinfo=pytz.utc)
    end_time = dt.combine(prev_thurs, time(5, 0), tzinfo=pytz.utc)
    es = history_api.download_historical_tick_data(security_code, EXCHANGE_CODE, start_time, end_time)
    assert history_api.downloads_in_progress is True
    nq = history_api.download_historical_tick_data(security_code2, EXCHANGE_CODE, start_time, end_time)
    while history_api.downloads_in_progress:
        timemod.sleep(0.1)

    assert len(history_api.current_downloads) == 2
    assert es.complete
    assert nq.complete
    assert isinstance(es.tick_dataframe, DataFrame)
    assert isinstance(nq.tick_dataframe, DataFrame)

    assert len(es.tick_dataframe) > 10000
    assert len(nq.tick_dataframe) > 10000


def test_history_api_download_tick_data_callbacks(history_api, ticker_api):
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    security_code2 = ticker_api.get_front_month_contract(NQ, EXCHANGE_CODE)
    assert history_api.downloads_in_progress is False

    class Callbacks:
        def __init__(self):
            self.tick_count = 0
            self.history_intermittent_count = 0
            self.history_complete = False

        def cb_history_intermittent(self, df: DataFrame, download_request: DownloadRequest):
            assert isinstance(df, DataFrame)
            assert isinstance(download_request, DownloadRequest)
            self.history_intermittent_count += 1
            self.tick_count += len(df)

        def history_complete_data(self, df: DataFrame, download_request: DownloadRequest):
            df_r = download_request.tick_dataframe
            assert df.equals(df_r)
            self.history_complete = True

    res = Callbacks()
    cbm = CallbackManager()
    cbm.register_callback(CallbackId.HISTORY_DOWNLOAD_INTERMITTENT_PROCESSING, res.cb_history_intermittent)
    cbm.register_callback(CallbackId.HISTORY_DOWNLOAD_COMPLETE_PROCESSING, res.history_complete_data)
    history_api.add_callback_manager(cbm)
    prev_thurs = find_nearest_day_of_week(date.today(), DayOfWeek.THURSDAY)
    start_time = dt.combine(prev_thurs, time(1, 0), tzinfo=pytz.utc)
    end_time = dt.combine(prev_thurs, time(5, 0), tzinfo=pytz.utc)
    es = history_api.download_historical_tick_data(security_code, EXCHANGE_CODE, start_time, end_time)
    assert history_api.downloads_in_progress is True
    nq = history_api.download_historical_tick_data(security_code2, EXCHANGE_CODE, start_time, end_time)
    while history_api.downloads_in_progress:
        timemod.sleep(0.1)

    history_api.detach_callback_manager()
    assert res.history_complete is True
    assert res.history_intermittent_count > 1

    assert res.tick_count == (es.download_row_count + nq.download_row_count)


def test_download_request_raises():
    security_code = 'SOMETICKER'
    start_time = get_utc_now()
    start_time_bad = dt.now()
    end_time = get_utc_now()
    end_time_bad = dt.now(tz=pytz.timezone('America/New_York'))
    dr = DownloadRequest(security_code, EXCHANGE_CODE, start_time, end_time)
    with pytest.raises(ValueError) as e:
        dr = DownloadRequest(security_code, EXCHANGE_CODE, start_time_bad, end_time)
    with pytest.raises(ValueError) as e:
        dr = DownloadRequest(security_code, EXCHANGE_CODE, start_time, end_time_bad)


def test_history_api_download_tick_data_reference_data_error_raises(history_api):
    # Old contract will not download
    security_code = 'ESU2'
    exchange_code = 'CME'
    assert history_api.downloads_in_progress is False
    start_time = dt(2022, 1, 20, 22, tzinfo=pytz.utc)
    end_time = dt(2022, 1, 20, 23, tzinfo=pytz.utc)
    with pytest.raises(DownloadErrorException) as e:
        history_api.download_historical_tick_data(security_code, exchange_code, start_time, end_time)


def test_history_api_download_tick_data_old_dates_no_data(history_api):
    # Old contract will not download
    security_code = 'ESU2'
    exchange_code = 'CME'
    start_time = dt(2022, 1, 20, 22, tzinfo=pytz.utc)
    end_time = dt(2022, 1, 20, 23, tzinfo=pytz.utc)
    with pytest.raises(DownloadErrorException) as e:
        history_api.download_historical_tick_data(security_code, exchange_code, start_time, end_time)


def test_history_api_download_tick_data_callback_async(history_api, ticker_api):
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)

    class Callbacks:
        def __init__(self):
            self.tick_count = 0
            self.history_intermittent_count = 0

        async def cb_history_intermittent(self, df: DataFrame, download_request: DownloadRequest):
            assert isinstance(df, DataFrame)
            assert isinstance(download_request, DownloadRequest)
            self.history_intermittent_count += 1
            self.tick_count += len(df)


    res = Callbacks()
    cbm = CallbackManager()
    cbm.register_callback(CallbackId.HISTORY_DOWNLOAD_INTERMITTENT_PROCESSING, res.cb_history_intermittent)
    history_api.add_callback_manager(cbm)
    prev_thurs = find_nearest_day_of_week(date.today(), DayOfWeek.THURSDAY)
    start_time = dt.combine(prev_thurs, time(1, 0), tzinfo=pytz.utc)
    end_time = dt.combine(prev_thurs, time(5, 0), tzinfo=pytz.utc)
    es = history_api.download_historical_tick_data(security_code, EXCHANGE_CODE, start_time, end_time)
    assert history_api.downloads_in_progress is True
    while history_api.downloads_in_progress:
        timemod.sleep(0.1)

    history_api.detach_callback_manager()
    assert res.history_intermittent_count > 1

    assert res.tick_count == es.download_row_count
