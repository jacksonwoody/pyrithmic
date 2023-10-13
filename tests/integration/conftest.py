import pandas as pd
import pytest

from rithmic import RithmicEnvironment, RithmicTickerApi, RithmicOrderApi, RithmicHistoryApi

TEST_ENVIRONMENT = RithmicEnvironment.RITHMIC_PAPER_TRADING


class RithmicOrderApiTesting(RithmicOrderApi):
    def clear_existing_updates(self):
        self.exchange_updates_data = []
        self.rithmic_updates_data = []


class RithmicTickerApiTesting(RithmicTickerApi):
    def clear_streamed_data(self):
        self.streamed_data = []

    def reset_streams(self):
        self.tick_data_streams = dict()


@pytest.fixture(scope='session', autouse=True)
def order_api() -> RithmicOrderApiTesting:
    print('Setting up order API')
    api = RithmicOrderApiTesting(env=TEST_ENVIRONMENT, auto_connect=False)
    assert api.have_trading_config is False
    api.connect_and_login()
    assert api.is_connected is True
    assert isinstance(api.trade_routes, pd.DataFrame)
    assert len(api.trade_routes) > 4
    assert isinstance(api.accounts, pd.DataFrame)
    assert isinstance(api.primary_account_id, str)
    assert api.have_trading_config is True
    assert api.subscribed_for_updates is True

    yield api

    print('tearing down order api')
    api.disconnect_and_logout()
    assert api.is_connected is False


@pytest.fixture(scope='session', autouse=True)
def ticker_api() -> RithmicTickerApiTesting:
    print('Setting up ticker API')
    api = RithmicTickerApiTesting(env=TEST_ENVIRONMENT, auto_connect=False)
    api.connect_and_login()
    assert api.is_connected is True
    assert api.consuming_subscription is False

    yield api

    print('tearing down ticker api')
    api.disconnect_and_logout()
    assert api.is_connected is False


@pytest.fixture(scope='session', autouse=True)
def history_api() -> RithmicHistoryApi:
    print('Setting up History API')
    api = RithmicHistoryApi(env=TEST_ENVIRONMENT, auto_connect=False)
    api.connect_and_login()
    assert api.is_connected is True
    assert api.consuming_subscription is False

    yield api

    print('tearing down History api')
    api.disconnect_and_logout()
    assert api.is_connected is False
