import time

import numpy as np
import pandas as pd
from pandas import DataFrame

from rithmic.callbacks.callbacks import CallbackManager, CallbackId
from rithmic.interfaces.ticker.ticker_api import TickDataStream


ES = 'ES'
NQ = 'NQ'
EXCHANGE_CODE = 'CME'


def test_ticker_api_streaming_tick_data(ticker_api):
    ticker_api.reset_streams()
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    assert ticker_api.streams_consuming_count == 0
    es = ticker_api.stream_market_data(security_code, EXCHANGE_CODE)
    assert isinstance(es, TickDataStream)
    assert es.is_streaming is True
    while ticker_api.total_tick_count == 0:
        time.sleep(0.1)
    assert ticker_api.consuming_subscription is True
    df = es.tick_dataframe
    data = df.iloc[0]
    assert isinstance(data.timestamp, pd.Timestamp)
    assert data.security_code == security_code
    assert data.exchange_code == EXCHANGE_CODE
    assert isinstance(data.volume, np.int64)
    assert isinstance(data.close, np.float64)
    ticker_api.stop_market_data_stream(security_code, EXCHANGE_CODE)
    assert es.is_streaming is False


def test_ticker_api_streaming_tick_data_custom_callbacks(ticker_api):
    ticker_api.reset_streams()
    callback_manager = CallbackManager()

    assert ticker_api.total_tick_count == 0

    class Result:
        def __init__(self):
            self.tick_count = 0
            self.data = []

        def periodic_sync(self, df: pd.DataFrame, security_code: str, exchange_code: str):
            self.tick_count += len(df)

        def last_tick_callback(self, data):
            self.data.append(data)


    res = Result()
    callback_manager.register_callback(CallbackId.TICKER_PERIODIC_LIVE_TICK_DATA_SYNCING, res.periodic_sync)
    callback_manager.register_callback(CallbackId.TICKER_LAST_TRADE, res.last_tick_callback)

    ticker_api.add_callback_manager(callback_manager)
    ticker_api._set_periodic_sync_interval(0.0001)

    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    es = ticker_api.stream_market_data(security_code, EXCHANGE_CODE)
    while ticker_api.total_tick_count == 0:
        time.sleep(0.1)
    ticker_api.stop_market_data_stream(security_code, EXCHANGE_CODE)
    time.sleep(0.5)
    tick_count = es.tick_count
    assert res.tick_count == tick_count

    len_data = len(res.data)
    assert tick_count == len_data
    assert es.streamed_data[-1] == res.data[-1]


def test_ticker_api_streaming_tick_data_multiple_securities(ticker_api):
    ticker_api.reset_streams()
    security_code1 = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    security_code2 = ticker_api.get_front_month_contract(NQ, EXCHANGE_CODE)
    assert ticker_api.total_tick_count == 0
    es = ticker_api.stream_market_data(security_code1, EXCHANGE_CODE)
    nq = ticker_api.stream_market_data(security_code2, EXCHANGE_CODE)
    while ticker_api.total_tick_count < 50:
        time.sleep(0.1)
    assert ticker_api.consuming_subscription is True
    assert es.is_streaming is True
    assert nq.is_streaming is True
    ticker_api.stop_market_data_stream(security_code1, EXCHANGE_CODE)
    ticker_api.stop_market_data_stream(security_code2, EXCHANGE_CODE)

    df_es = es.tick_dataframe
    df_nq = es.tick_dataframe

    assert isinstance(df_es, DataFrame)
    assert isinstance(df_nq, DataFrame)

    assert len(df_es) > 0
    assert len(df_nq) > 0


def test_ticker_api_streaming_tick_data_custom_callbacks_multiple_securities(ticker_api):
    ticker_api.reset_streams()
    callback_manager = CallbackManager()

    assert ticker_api.total_tick_count == 0

    class Result:
        def __init__(self):
            self.sec_exchange_counter = dict()

        def periodic_sync(self, df: pd.DataFrame, security_code: str, exchange_code: str):
            key = (security_code, exchange_code)
            count = self.sec_exchange_counter.get(key, 0)
            self.sec_exchange_counter[key] = count + 1


    res = Result()
    callback_manager.register_callback(CallbackId.TICKER_PERIODIC_LIVE_TICK_DATA_SYNCING, res.periodic_sync)

    ticker_api.add_callback_manager(callback_manager)
    ticker_api._set_periodic_sync_interval(0.1)

    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    security_code2 = ticker_api.get_front_month_contract(NQ, EXCHANGE_CODE)
    es = ticker_api.stream_market_data(security_code, EXCHANGE_CODE)
    nq = ticker_api.stream_market_data(security_code2, EXCHANGE_CODE)
    while ticker_api.total_tick_count < 50:
        time.sleep(0.1)
    ticker_api.stop_market_data_stream(security_code, EXCHANGE_CODE)
    ticker_api.stop_market_data_stream(security_code2, EXCHANGE_CODE)
    time.sleep(0.5)

    assert res.sec_exchange_counter[es.stream_key] > 0
    assert res.sec_exchange_counter[nq.stream_key] > 0
