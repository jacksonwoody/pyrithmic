from abc import ABCMeta
import asyncio
from datetime import datetime as dt
from pathlib import Path
import pytz
import ssl
import threading
import websockets

from rithmic.callbacks.callbacks import CallbackManager
from rithmic.config.credentials import RithmicEnvironment, get_rithmic_credentials
from rithmic.protocol_buffers import base_pb2, request_login_pb2, response_login_pb2, request_heartbeat_pb2
from rithmic.tools.pyrithmic_logger import logger


INFRA_MAP = {
    1: 'TICKER', 2: 'ORDER', 3: 'HISTORY'
}


def _setup_ssl_context():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    localhost_pem = Path(__file__).parent.parent / 'certificates' / 'rithmic_ssl_cert_auth_params'
    ssl_context.load_verify_locations(localhost_pem)
    return ssl_context


class RithmicBaseApi(metaclass=ABCMeta):
    infra_type = None

    def __init__(self, env: RithmicEnvironment = None, callback_manager: CallbackManager = None,
                 auto_connect: bool = True, loop = None):
        self.ws = None
        credentials = get_rithmic_credentials(env)
        self.uri = credentials['uri']
        self.user = credentials['user']
        self.pw = credentials['pw']
        self.app_name = credentials['app_name']
        self.app_version = credentials['app_version']
        self.system_name = credentials['system_name']
        self.ssl_context = self.setup_ssl_context()
        self.callback_manager = callback_manager if callback_manager is not None else CallbackManager()
        self.loop = None
        if loop is not None:
            self.loop = loop
        else:
            self.start_loop()
        if auto_connect:
            self.connect_and_login()

    async def consume_subscription(self):
        raise NotImplementedError('Must be implemented in non abstract class')

    def start_loop(self):
        self.loop = asyncio.new_event_loop()
        thr = threading.Thread(target=self.loop.run_forever, daemon=True)
        thr.start()

    def get_template_id_from_message_buffer(self, msg_buf) -> int:
        msg_length = int.from_bytes(msg_buf[0:3], byteorder='big', signed=True)
        base = base_pb2.Base()
        base.ParseFromString(msg_buf[4:])
        return base.template_id

    def _convert_request_to_buffer(self, request):
        serialized = request.SerializeToString()
        length = len(serialized)
        buffer = bytearray()
        buffer = length.to_bytes(4, byteorder='big', signed=True)
        buffer += serialized
        return buffer

    def setup_ssl_context(self):
        return _setup_ssl_context()

    def connect_and_login(self):
        ws = self._get_websocket_connection()
        self.ws = ws
        return self._log_into_rithmic()

    def _get_websocket_connection(self):
        future = asyncio.run_coroutine_threadsafe(self.get_websocket_connection(), self.loop)
        return future.result()

    def _log_into_rithmic(self):
        future = asyncio.run_coroutine_threadsafe(self.rithmic_login(), loop=self.loop)
        return future.result()

    async def get_websocket_connection(self):
        ws = await websockets.connect(self.uri, ssl=self.ssl_context, ping_interval=3)
        logger.info('Connected to {0}'.format(self.uri))
        return ws

    async def rithmic_login(self):
        rq = request_login_pb2.RequestLogin()
        rq.template_id = 10
        rq.template_version = "3.9"
        rq.user = self.user
        rq.password = self.pw
        rq.app_name = self.app_name
        rq.app_version = self.app_version
        rq.system_name = self.system_name
        rq.infra_type = self.infra_type
        buffer = self._convert_request_to_buffer(rq)
        await self.ws.send(buffer)

        rp_buf = bytearray()
        rp_buf = await self.ws.recv()
        rp_length = int.from_bytes(rp_buf[0:3], byteorder='big', signed=True)
        rp = response_login_pb2.ResponseLogin()
        rp.ParseFromString(rp_buf[4:])
        logger.info('Logged into Rithmic => unique user id={0}; Plant=>{1}'.format(
            rp.unique_user_id, INFRA_MAP[self.infra_type])
        )
        return rp

    async def send_heartbeat(self):
        rq = request_heartbeat_pb2.RequestHeartbeat()
        rq.template_id = 18
        buffer = self._convert_request_to_buffer(rq)
        await self.ws.send(buffer)
        logger.debug('Sent Heartbeat Request')

    def _get_row_information(self, template_id, msg):
        ts = '{0}.{1}'.format(msg.ssboe, msg.usecs)
        update_time = dt.fromtimestamp(float(ts), tz=pytz.utc)
        msg = self._convert_msg_to_dict(msg)
        row = dict(template_id=template_id, update_time=update_time)
        row.update(msg)
        return row

    def _convert_msg_to_dict(self, msg):
        result = dict()
        keys = [x.split(':')[0] for x in str(msg).strip().split('\n')]
        for k in keys:
            result[k] = getattr(msg, k)
        return result
