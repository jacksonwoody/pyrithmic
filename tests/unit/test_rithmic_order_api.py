import pandas as pd

from rithmic.interfaces.order import RithmicOrderApi
from tests.unit.fixtures.api_fixtures import mocked_order_api_ws_mock as order_api_ws_mock, set_ws_messages
from tests.unit.fixtures.mocked_messages import ORDER_BASE_SEND, ORDER_BASE_RECV


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


