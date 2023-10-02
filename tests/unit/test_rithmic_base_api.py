from datetime import datetime
from ssl import SSLContext

import pytz

from rithmic.interfaces.base import _setup_ssl_context, RithmicBaseApi
from rithmic.protocol_buffers.last_trade_pb2 import LastTrade
from rithmic.protocol_buffers.request_login_pb2 import RequestLogin


def test__setup_ssl_context():
    ssl_context = _setup_ssl_context()
    assert isinstance(ssl_context, SSLContext)


def test__convert_request_to_buffer():
    rq = RequestLogin()
    rq.template_id = 10
    rq.template_version = "3.9"
    rq.user = 'my_username'
    rq.password = 'my_password'
    rq.app_name = 'my_app'
    rq.app_version = 'my_version'
    rq.system_name = 'RITHMIC TEST'
    rq.infra_type = 2

    api = RithmicBaseApi(env=None, auto_connect=False, loop=None)
    result = api._convert_request_to_buffer(rq)
    expected = b'\x00\x00\x00U\x92\xbd?\x06my_app\xa2\xbd?\x0bmy_password\xda\xfb?\x0bmy_username\xda\xad@\nmy_version\xa8\x81K\x02\xe2\x81K\x0cRITHMIC TEST\x92\x82K\x033.9\x98\xb6K\n'
    assert result == expected
    assert isinstance(result, bytes)


def test_get_template_id_from_message_buffer():
    api = RithmicBaseApi(env=None, auto_connect=False, loop=None)
    msg_buf = b'\x00\x00\x00\x17\x98\xb6K\x13\xa0\xa5I\xa5\xa0\xeb\xa8\x06\xa8\xa5I\x8c\xd9.\xf2\xe9@\x010'
    result = api.get_template_id_from_message_buffer(msg_buf)
    assert result == 19


def test_get_row_information():
    api= RithmicBaseApi(env=None, auto_connect=False, loop=None)
    msg = LastTrade()
    key_values = dict(
        trade_price=4303.75, volume=24405, trade_size=1, symbol='ESZ3', exchange='CME', is_snapshot=True,
        aggressor=LastTrade.TransactionType.SELL, ssboe=1696256037, template_id=150,
    )
    for k, v in key_values.items():
        setattr(msg, k, v)

    result = api._get_row_information(150, msg)
    expected = {'template_id': 150, 'update_time': datetime(2023, 10, 2, 14, 13, 57, tzinfo=pytz.UTC),
                'trade_price': 4303.75, 'volume': 24405, 'trade_size': 1, 'symbol': 'ESZ3', 'exchange': 'CME',
                'is_snapshot': True, 'aggressor': 2, 'ssboe': 1696256037}

    assert result == expected
