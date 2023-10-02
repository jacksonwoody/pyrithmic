from datetime import datetime as dt
import time

import pandas as pd

from rithmic.interfaces.order import RithmicOrderApi
from rithmic.interfaces.ticker import RithmicTickerApi


def test_order_api_initialise():
    order_api = RithmicOrderApi(env=None, callback_manager=None, loop=None, auto_connect=False)
    assert order_api.have_trading_config is False
    order_api.connect_and_login()
    assert isinstance(order_api.trade_routes, pd.DataFrame)
    assert len(order_api.trade_routes) > 4
    assert isinstance(order_api.accounts, pd.DataFrame)
    assert order_api.primary_account_id == 'JW21720'
    assert order_api.have_trading_config is True
    assert order_api.subscribed_for_updates is True


def test_order_api_buy_limit_order():
    order_api = RithmicOrderApi(env=None, callback_manager=None, loop=None, auto_connect=True)
    ticker_api = RithmicTickerApi(env=None, callback_manager=None, loop=None, auto_connect=True)
    security_code = 'ESZ3'
    exchange_code = 'CME'
    ticker_api.stream_market_data(security_code, exchange_code)
    while len(ticker_api.tick_dataframe) == 0:
        time.sleep(0.1)
    last_px = ticker_api.tick_dataframe.iloc[-1].close
    ticker_api.stop_market_data_stream(security_code, exchange_code)
    now_str = dt.now().strftime('%Y%m%d_%H%M%S')
    order_api.submit_limit_order(
        order_id=now_str, security_code=security_code, exchange_code=exchange_code, quantity=1, is_buy=True,
        limit_price=last_px - (0.25 * 10)
    )
    while len(order_api.rithmic_updates_data) == 0:
        time.sleep(0.1)
    first_msg = order_api.rithmic_updates_data[0]
    assert first_msg['status'] == 'Order received from client'
    assert first_msg['order_id'] == now_str


def test_order_api_sell_limit_order():
    order_api = RithmicOrderApi(env=None, callback_manager=None, loop=None, auto_connect=True)
    ticker_api = RithmicTickerApi(env=None, callback_manager=None, loop=None, auto_connect=True)
    security_code = 'ESZ3'
    exchange_code = 'CME'
    ticker_api.stream_market_data(security_code, exchange_code)
    while len(ticker_api.tick_dataframe) == 0:
        time.sleep(0.1)
    last_px = ticker_api.tick_dataframe.iloc[-1].close
    ticker_api.stop_market_data_stream(security_code, exchange_code)
    now_str = dt.now().strftime('%Y%m%d_%H%M%S')
    order_api.submit_limit_order(
        order_id=now_str, security_code=security_code, exchange_code=exchange_code, quantity=1, is_buy=False,
        limit_price=last_px + (0.25 * 10)
    )
    while len(order_api.rithmic_updates_data) == 0:
        time.sleep(0.1)
    first_msg = order_api.rithmic_updates_data[0]
    assert first_msg['status'] == 'Order received from client'
    assert first_msg['order_id'] == now_str


def test_order_api_buy_market_order():
    order_api = RithmicOrderApi(env=None, callback_manager=None, loop=None, auto_connect=True)
    security_code = 'ESZ3'
    exchange_code = 'CME'
    now_str = dt.now().strftime('%Y%m%d_%H%M%S')
    order_api.submit_market_order(
        order_id=now_str, security_code=security_code, exchange_code=exchange_code, quantity=1, is_buy=True,
    )
    while len(order_api.rithmic_updates_data) == 0:
        time.sleep(0.1)
    first_msg = order_api.rithmic_updates_data[0]
    assert first_msg['status'] == 'Order received from client'
    assert first_msg['order_id'] == now_str


def test_order_api_buy_bracket_order():
    order_api = RithmicOrderApi(env=None, callback_manager=None, loop=None, auto_connect=True)
    ticker_api = RithmicTickerApi(env=None, callback_manager=None, loop=None, auto_connect=True)
    security_code = 'ESZ3'
    exchange_code = 'CME'
    ticker_api.stream_market_data(security_code, exchange_code)
    while len(ticker_api.tick_dataframe) == 0:
        time.sleep(0.1)
    last_px = ticker_api.tick_dataframe.iloc[-1].close
    ticker_api.stop_market_data_stream(security_code, exchange_code)
    now_str = dt.now().strftime('%Y%m%d_%H%M%S')
    order_api.submit_bracket_order(
        order_id=now_str, security_code=security_code, exchange_code=exchange_code, quantity=1, is_buy=True,
        limit_price=last_px - (0.25 * 10), stop_loss_ticks=10, take_profit_ticks=10,
    )
    while len(order_api.rithmic_updates_data) == 0:
        time.sleep(0.1)
    first_msg = order_api.rithmic_updates_data[0]
    assert first_msg['status'] == 'Order received from client'
    assert first_msg['order_id'] == now_str
