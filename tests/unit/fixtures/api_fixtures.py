from unittest import mock
from unittest.mock import AsyncMock

import pytest

from rithmic.interfaces.base import RithmicBaseApi
from rithmic.interfaces.order import RithmicOrderApi
from rithmic.interfaces.ticker import RithmicTickerApi


def set_ws_messages(ws_mock, send_msgs, recv_msgs):
    ws_mock.send.side_effect = send_msgs
    ws_mock.recv.side_effect = recv_msgs


@pytest.fixture()
def mocked_order_api_ws_mock():
    with mock.patch.object(RithmicBaseApi, '_get_websocket_connection') as mock_get_ws:
        ws_mock = AsyncMock()
        mock_get_ws.return_value = ws_mock
        order_api = RithmicOrderApi(env=None, callback_manager=None, loop=None, auto_connect=False)
        yield [order_api, ws_mock]


@pytest.fixture()
def mocked_ticker_api_ws_mock():
    with mock.patch.object(RithmicBaseApi, '_get_websocket_connection') as mock_get_ws:
        ws_mock = AsyncMock()
        mock_get_ws.return_value = ws_mock
        order_api = RithmicTickerApi(env=None, callback_manager=None, loop=None, auto_connect=False)
        yield [order_api, ws_mock]
