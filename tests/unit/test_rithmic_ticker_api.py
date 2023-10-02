from rithmic.interfaces.ticker import RithmicTickerApi
from tests.unit.fixtures.api_fixtures import mocked_ticker_api_ws_mock as ticker_api_ws_mock, set_ws_messages
from tests.unit.fixtures.mocked_messages import BASE_SEND, BASE_RECV


def test_order_api_login(ticker_api_ws_mock):
    ticker_api, ws_mock = ticker_api_ws_mock
    assert isinstance(ticker_api, RithmicTickerApi)
    set_ws_messages(ws_mock, BASE_SEND, BASE_RECV)
    ticker_api.connect_and_login()
    assert len(ticker_api.streamed_data) == 0
    assert ticker_api.consuming_subscription is False
