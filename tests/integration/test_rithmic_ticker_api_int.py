import time

import numpy as np
import pandas as pd

from rithmic.callbacks.callbacks import CallbackManager, CallbackId
from rithmic.interfaces.ticker import RithmicTickerApi


def test_ticker_api_initialise():
    api = RithmicTickerApi(env=None, callback_manager=None, loop=None, auto_connect=False)
    api.connect_and_login()
    assert api.ws.open is True
    assert api.consuming_subscription is False


def test_ticker_api_streaming_tick_data():
    api = RithmicTickerApi(env=None, callback_manager=None, loop=None, auto_connect=True)
    security_code = 'ESZ3'
    exchange_code = 'CME'
    assert isinstance(api.tick_dataframe, pd.DataFrame)
    assert len(api.tick_dataframe) == 0
    api.stream_market_data(security_code, exchange_code)
    while len(api.tick_dataframe) == 0:
        time.sleep(0.1)
    assert api.consuming_subscription is True
    df = api.tick_dataframe
    data = df.iloc[0]
    assert isinstance(data.timestamp, pd.Timestamp)
    assert data.security_code == security_code
    assert data.exchange_code == exchange_code
    assert isinstance(data.volume, np.int64)
    assert isinstance(data.close, np.float64)


def test_ticker_api_streaming_tick_data_custom_callbacks():
    callback_manager = CallbackManager()

    class Stream:
        def __init__(self):
            self.tick_count = 0
            self.data = []

        def periodic_sync(self, df: pd.DataFrame):
            self.tick_count += len(df)

        def last_tick_callback(self, data):
            self.data.append(data)


    s = Stream()
    callback_manager.register_callback(CallbackId.PERIODIC_TICK_DATA_SYNCING, s.periodic_sync)
    callback_manager.register_callback(CallbackId.LAST_TRADE, s.last_tick_callback)

    api = RithmicTickerApi(env=None, callback_manager=callback_manager, loop=None, auto_connect=True,
                           periodic_sync_interval_seconds=0.0001)
    security_code = 'ESZ3'
    exchange_code = 'CME'
    assert isinstance(api.tick_dataframe, pd.DataFrame)
    assert len(api.tick_dataframe) == 0
    api.stream_market_data(security_code, exchange_code)
    while len(api.tick_dataframe) == 0:
        time.sleep(0.1)
    tick_count = len(api.tick_dataframe)
    assert s.tick_count == tick_count
    assert len(api.streamed_data) == len(s.data)
    assert api.streamed_data[-1] == s.data[-1]

