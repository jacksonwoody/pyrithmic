import time

import pandas as pd

from rithmic import RithmicOrderApi
from tests.unit.fixtures.api_fixtures import mocked_order_api_ws_mock as order_api_ws_mock, set_ws_messages
from tests.unit.fixtures.mocked_messages import ORDER_BASE_SEND, ORDER_BASE_RECV, MKT_ORDER_SEND, MKT_ORDER_RECV


def test_order_api_login(order_api_ws_mock):
    order_api, ws_mock = order_api_ws_mock
    assert isinstance(order_api, RithmicOrderApi)
    set_ws_messages(ws_mock, ORDER_BASE_SEND, ORDER_BASE_RECV)
    assert order_api.have_trading_config is False
    order_api.connect_and_login()
    assert isinstance(order_api.trade_routes, pd.DataFrame)
    assert len(order_api.trade_routes) == 4
    assert isinstance(order_api.accounts, pd.DataFrame)
    assert order_api.primary_account_id == 'du20000'
    assert order_api.have_trading_config is True
    assert order_api.subscribed_for_updates is True


def test_order_api_market_order(order_api_ws_mock):
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 100)
    pd.set_option('display.width', 1000)
    order_api, ws_mock = order_api_ws_mock
    set_ws_messages(ws_mock, MKT_ORDER_SEND, MKT_ORDER_RECV)
    security_code = 'ESZ3'
    exchange_code = 'CME'
    order_id = '20231004_151407'
    order_api.connect_and_login()
    order_api.submit_market_order(
        order_id=order_id, security_code=security_code, exchange_code=exchange_code, quantity=1, is_buy=True,
    )
    while len(order_api.exchange_updates) < 2:
        time.sleep(0.01)
    df_ex = order_api.exchange_updates
    assert len(df_ex) == 2
    ex_msg1, ex_msg2 = df_ex.iloc[0], df_ex.iloc[1]
    assert ex_msg1.report_type == 'status'
    assert ex_msg1.order_id == order_id

    assert ex_msg2.report_type == 'fill'
    assert ex_msg2.order_id == order_id
    assert ex_msg2.fill_price == 4267.
    assert ex_msg2.fill_size == 1.

