import time
from datetime import datetime as dt

import pytest
import pytz
from pandas import DataFrame

from rithmic import CallbackManager, CallbackId
from rithmic.interfaces.history.history_api import DownloadRequest
from rithmic.tools.general import get_utc_now


def test_history_api_download_tick_data(history_api):
    security_code = 'ESZ3'
    security_code2 = 'NQZ3'
    exchange_code = 'CME'
    assert history_api.downloads_in_progress is False
    start_time = dt(2023, 10, 11, 1, tzinfo=pytz.utc)
    end_time = dt(2023, 10, 11, 5, tzinfo=pytz.utc)
    es = history_api.download_historical_tick_data(security_code, exchange_code, start_time, end_time)
    assert history_api.downloads_in_progress is True
    nq = history_api.download_historical_tick_data(security_code2, exchange_code, start_time, end_time)
    while history_api.downloads_in_progress:
        time.sleep(0.1)

    assert len(history_api.current_downloads) == 2
    assert es.complete
    assert nq.complete
    assert isinstance(es.tick_dataframe, DataFrame)
    assert isinstance(nq.tick_dataframe, DataFrame)

    assert len(es.tick_dataframe) > 10000
    assert len(nq.tick_dataframe) > 10000


def test_history_api_download_tick_data_callbacks(history_api):
    security_code = 'ESZ3'
    security_code2 = 'NQZ3'
    exchange_code = 'CME'
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
    start_time = dt(2023, 10, 11, 1, tzinfo=pytz.utc)
    end_time = dt(2023, 10, 11, 5, tzinfo=pytz.utc)
    es = history_api.download_historical_tick_data(security_code, exchange_code, start_time, end_time)
    assert history_api.downloads_in_progress is True
    nq = history_api.download_historical_tick_data(security_code2, exchange_code, start_time, end_time)
    while history_api.downloads_in_progress:
        time.sleep(0.1)

    history_api.detach_callback_manager()
    assert res.history_complete is True
    assert res.history_intermittent_count == 4

    assert res.tick_count == (es.download_row_count + nq.download_row_count)


def test_download_request_raises():
    security_code, exchange_code = 'ESZ3', 'CME'
    start_time = get_utc_now()
    start_time_bad = dt.now()
    end_time = get_utc_now()
    end_time_bad = dt.now(tz=pytz.timezone('America/New_York'))
    dr = DownloadRequest(security_code, exchange_code, start_time, end_time)
    with pytest.raises(ValueError) as e:
        dr = DownloadRequest(security_code, exchange_code, start_time_bad, end_time)
    with pytest.raises(ValueError) as e:
        dr = DownloadRequest(security_code, exchange_code, start_time, end_time_bad)
