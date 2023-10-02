import asyncio

import pandas as pd

from rithmic.callbacks.callbacks import CallbackManager
from rithmic.config.credentials import RithmicEnvironment
from rithmic.interfaces.base import RithmicBaseApi
from rithmic.protocol_buffers import (
    request_login_pb2, request_login_info_pb2, response_login_info_pb2, request_account_list_pb2,
    response_account_list_pb2, request_trade_routes_pb2, response_trade_routes_pb2,
    request_subscribe_for_order_updates_pb2, request_subscribe_to_bracket_updates_pb2, rithmic_order_notification_pb2,
    exchange_order_notification_pb2, response_bracket_order_pb2, response_new_order_pb2, request_new_order_pb2,
    request_bracket_order_pb2, request_cancel_order_pb2, request_update_stop_bracket_level_pb2,
    request_modify_order_pb2, request_update_target_bracket_level_pb2,
)
from rithmic.tools.general import dict_destructure
from rithmic.tools.pyrithmic_exceptions import (
    NoValidTradingAccountException, NoValidTradeRouteException, NoTradingConfigException, WebsocketClosedException,
)
from rithmic.tools.pyrithmic_logger import logger

ORDER_UPDATE_RESPONSE_MAP = {
    351: dict(proto=rithmic_order_notification_pb2.RithmicOrderNotification, fn='process_rithmic_order_notification'),
    352: dict(proto=exchange_order_notification_pb2.ExchangeOrderNotification,
              fn='process_exchange_order_notification'),
    331: dict(proto=response_bracket_order_pb2.ResponseBracketOrder, fn='process_response_bracket_order'),
    313: dict(proto=response_new_order_pb2.ResponseNewOrder, fn='process_response_new_order'),
}

SIDE_MAP = {
    True: request_new_order_pb2.RequestNewOrder.TransactionType.BUY,
    False: request_new_order_pb2.RequestNewOrder.TransactionType.SELL,
}

BRACKET_SIDE_MAP = {
    True: request_bracket_order_pb2.RequestBracketOrder.TransactionType.BUY,
    False: request_bracket_order_pb2.RequestBracketOrder.TransactionType.SELL,
}


class RithmicOrderApi(RithmicBaseApi):
    infra_type = request_login_pb2.RequestLogin.SysInfraType.ORDER_PLANT

    def __init__(self, env: RithmicEnvironment = None, callback_manager: CallbackManager = None, loop=None,
                 auto_connect: bool = True):
        self.have_trading_config = False
        self.subscribed_for_updates = False
        self.fcm_id = None
        self.ib_id = None
        self.user_type = None
        self.accounts = None
        self.trade_routes = None
        RithmicBaseApi.__init__(self, env=env, callback_manager=callback_manager, loop=loop, auto_connect=auto_connect)
        self.rithmic_updates_data = []
        self.exchange_updates_data = []
        self.processed_fill_ids = []
        self.exchange_update_callback = None
        self.rithmic_update_callback = None

    def attach_exchange_update_callback(self, fn):
        self.exchange_update_callback = fn

    def _set_log_in_details(self, details):
        keys = ['fcm_id', 'ib_id', 'user_type', 'accounts', 'trade_routes']
        fcm_id, ib_id, user_type, accounts, trade_routes = dict_destructure(details, keys)
        self.fcm_id = fcm_id
        self.ib_id = ib_id
        self.user_type = user_type
        self.accounts = pd.DataFrame(accounts)
        self.trade_routes = pd.DataFrame(trade_routes)
        self.have_trading_config = True

    def connect_and_login(self):
        logged_in = super(RithmicOrderApi, self).connect_and_login()
        future = asyncio.run_coroutine_threadsafe(self.get_login_info(), loop=self.loop)
        log_in_details = future.result()
        self._set_log_in_details(log_in_details)
        self.run_update_subscription()

    async def get_login_info(self):
        rq = request_login_info_pb2.RequestLoginInfo()
        rq.template_id = 300
        rq.user_msg.append("request_login_info")
        buffer = self._convert_request_to_buffer(rq)
        await self.ws.send(buffer)

        rp_buf = bytearray()
        rp_buf = await self.ws.recv()

        rp_length = int.from_bytes(rp_buf[0:3], byteorder='big', signed=True)

        rp = response_login_info_pb2.ResponseLoginInfo()
        rp.ParseFromString(rp_buf[4:])

        user_type_to_string = {0: 'ADMIN', 1: 'FCM', 2: 'IB', 3: 'TRADER'}

        if rp.rp_code[0] == '0':
            accounts = await self.list_accounts(rp.fcm_id, rp.ib_id, rp.user_type)
            trade_routes = await self.list_trade_routes()
            details = dict(
                template_id=rp.template_id, user_msg=rp.user_msg, rp_code=rp.rp_code,
                fcm_id=rp.fcm_id, ib_id=rp.ib_id, user_type=user_type_to_string[rp.user_type],
                accounts=accounts, trade_routes=trade_routes,
            )
            return details
        raise ConnectionError('Error Getting Details from Rithmic')

    async def list_accounts(self, fcm_id, ib_id, user_type):
        rq = request_account_list_pb2.RequestAccountList()
        rq.template_id = 302
        rq.user_msg.append("hello")
        rq.fcm_id = fcm_id
        rq.ib_id = ib_id
        rq.user_type = user_type

        buffer = self._convert_request_to_buffer(rq)
        rp_is_done = False
        await self.ws.send(buffer)

        rp_buf = bytearray()

        accounts = []
        while rp_is_done == False:
            rp_buf = await self.ws.recv()
            # get length from first four bytes from rp_buf
            rp_length = int.from_bytes(rp_buf[0:3], byteorder='big', signed=True)
            rp = response_account_list_pb2.ResponseAccountList()
            rp.ParseFromString(rp_buf[4:])

            record = dict(
                template_id=rp.template_id, rq_handler_rp_code=rp.rq_handler_rp_code,
                rp_code=rp.rp_code, fcm_id=rp.fcm_id, ib_id=rp.ib_id, account_id=rp.account_id,
                account_name=rp.account_name,
            )
            if len(rp.rp_code) > 0:
                rp_is_done = True
            else:
                accounts.append(record)
        return accounts

    async def list_trade_routes(self):
        rq = request_trade_routes_pb2.RequestTradeRoutes()
        rq.template_id = 310
        rq.user_msg.append("request_trade_routes")
        rq.subscribe_for_updates = False

        buffer = self._convert_request_to_buffer(rq)
        rp_is_done = False
        await self.ws.send(buffer)

        rp_buf = bytearray()
        trade_routes = []
        while rp_is_done == False:
            rp_buf = await self.ws.recv()
            rp_length = int.from_bytes(rp_buf[0:3], byteorder='big', signed=True)
            rp = response_trade_routes_pb2.ResponseTradeRoutes()
            rp.ParseFromString(rp_buf[4:])
            record = dict(
                template_id=rp.template_id, rp_handler_code=rp.rq_handler_rp_code, rp_code=rp.rp_code,
                fcm_id=rp.fcm_id, ib_id=rp.ib_id, exchange=rp.exchange, trade_route=rp.trade_route,
                status=rp.status, is_default=rp.is_default,
            )
            if len(rp.rp_code) > 0:
                rp_is_done = True
            else:
                trade_routes.append(record)
        return trade_routes

    @property
    def primary_account_id(self):
        if len(self.accounts) == 0:
            raise NoValidTradingAccountException('No Valid Trading Accounts Found')
        return self.accounts.iloc[0].account_id

    def get_trade_route(self, exchange_code: str):
        df = self.trade_routes
        df = df[df.exchange == exchange_code]
        if len(df) == 0:
            raise NoValidTradeRouteException('No Valid Trade Route Exists for {0}'.format(exchange_code))
        return df.iloc[0].trade_route

    async def subscribe_for_order_updates(self, fcm_id, ib_id, account_id):
        rq = request_subscribe_for_order_updates_pb2.RequestSubscribeForOrderUpdates()
        rq.template_id = 308
        rq.user_msg.append("order_updates_subscription")
        rq.fcm_id = fcm_id
        rq.ib_id = ib_id
        rq.account_id = account_id
        buffer = self._convert_request_to_buffer(rq)
        await self.ws.send(buffer)

    async def subscribe_for_bracket_updates(self, fcm_id, ib_id, account_id):
        rq = request_subscribe_to_bracket_updates_pb2.RequestSubscribeToBracketUpdates()
        rq.template_id = 336
        rq.user_msg.append('bracket_updates_subscription')
        rq.fcm_id = fcm_id
        rq.ib_id = ib_id
        rq.account_id = account_id
        buffer = self._convert_request_to_buffer(rq)
        await self.ws.send(buffer)

    def check_update_status(self):
        if self.have_trading_config:
            if self.subscribed_for_updates is False:
                primary_account = self.primary_account_id
                asyncio.run_coroutine_threadsafe(
                    self.subscribe_for_order_updates(self.fcm_id, self.ib_id, primary_account), loop=self.loop
                )
                asyncio.run_coroutine_threadsafe(
                    self.subscribe_for_bracket_updates(self.fcm_id, self.ib_id, primary_account), loop=self.loop,
                )
                self.subscribed_for_updates = True
        else:
            raise NoTradingConfigException('Have not received Trading Config from Rithmic')

    async def consume_order_updates(self):
        await self.send_heartbeat()
        while True:
            try:
                msg_buf = bytearray()
                waiting_for_msg = True
                while waiting_for_msg:
                    try:
                        msg_buf = await asyncio.wait_for(self.ws.recv(), timeout=5)
                        waiting_for_msg = False
                    except asyncio.TimeoutError:
                        if self.ws.open:
                            await self.send_heartbeat()
                        else:
                            logger.info("connection appears to be closed.  exiting consume()")
                            raise WebsocketClosedException('Websocket has closed')
                template_id = self.get_template_id_from_message_buffer(msg_buf)
                if template_id != 19:
                    result = self.process_order_update(template_id, msg_buf)
            except Exception as e:
                print(e)

    def process_order_update(self, template_id: int, msg_buf):
        if template_id in ORDER_UPDATE_RESPONSE_MAP:
            meta = ORDER_UPDATE_RESPONSE_MAP[template_id]
            msg = meta['proto']()
            msg.ParseFromString(msg_buf[4:])
            fn = getattr(self, meta['fn'])
            result = fn(template_id, msg)
            callback_fn = self.callback_manager.get_callback_by_template_id(template_id)
            if callback_fn is not None:
                callback_fn(result)
            return result

    def process_response_bracket_order(self, template_id, msg):
        row = self._get_row_information(template_id, msg)
        order_id = row.get('user_tag')
        basket_id = row.get('basket_id')
        return row

    def process_rithmic_order_notification(self, template_id, msg):
        row = self._get_row_information(template_id, msg)
        row['order_id'] = row.get('user_tag')
        self.rithmic_updates_data.append(row)
        return row

    def process_exchange_order_notification(self, template_id, msg):
        row = self._get_row_information(template_id, msg)
        row['order_id'] = row.get('user_tag')
        self.exchange_updates_data.append(row)
        return row

    def process_response_new_order(self, template_id, msg):
        row = self._get_row_information(template_id, msg)
        order_id = row.get('user_tag')
        basket_id = row.get('basket_id')
        return row

    def process_response_stop_update(self, template_id, msg):
        row = self._get_row_information(template_id, msg)
        return row

    def run_update_subscription(self):
        self.check_update_status()
        asyncio.run_coroutine_threadsafe(self.consume_order_updates(), self.loop)

    @property
    def rithmic_updates(self):
        data = self.rithmic_updates_data[:]
        return pd.DataFrame(data)

    @property
    def exchange_updates(self):
        data = self.exchange_updates_data[:]
        return pd.DataFrame(data)

    async def send_market_order(self, order_id: str, security_code: str, exchange_code: str, quantity: int,
                                is_buy: bool):
        rq = request_new_order_pb2.RequestNewOrder()
        rq.template_id = 312
        rq.user_tag = order_id
        rq.fcm_id = self.fcm_id
        rq.ib_id = self.ib_id
        rq.account_id = self.primary_account_id
        rq.exchange = exchange_code
        rq.symbol = security_code
        rq.quantity = quantity
        rq.transaction_type = SIDE_MAP[is_buy]
        rq.duration = request_new_order_pb2.RequestNewOrder.Duration.DAY
        rq.price_type = request_new_order_pb2.RequestNewOrder.PriceType.MARKET
        rq.manual_or_auto = request_new_order_pb2.RequestNewOrder.OrderPlacement.MANUAL
        rq.trade_route = self.get_trade_route(exchange_code)
        buffer = self._convert_request_to_buffer(rq)
        await self.ws.send(buffer)

    async def send_limit_order(self, order_id: str, security_code: str, exchange_code: str, quantity: int, is_buy: bool,
                               limit_price: float):
        rq = request_new_order_pb2.RequestNewOrder()
        rq.template_id = 312
        rq.user_tag = order_id
        rq.fcm_id = self.fcm_id
        rq.ib_id = self.ib_id
        rq.account_id = self.primary_account_id
        rq.exchange = exchange_code
        rq.symbol = security_code
        rq.quantity = quantity
        rq.transaction_type = SIDE_MAP[is_buy]
        rq.duration = request_new_order_pb2.RequestNewOrder.Duration.DAY
        rq.price_type = request_new_order_pb2.RequestNewOrder.PriceType.LIMIT
        rq.manual_or_auto = request_new_order_pb2.RequestNewOrder.OrderPlacement.MANUAL
        rq.trade_route = self.get_trade_route(exchange_code)
        rq.price = limit_price
        buffer = self._convert_request_to_buffer(rq)
        await self.ws.send(buffer)

    async def send_bracket_order(self, order_id: str, security_code: str, exchange_code: str, quantity: int,
                                 is_buy: bool, limit_price: float, stop_loss_ticks: int, take_profit_ticks: int):
        rq = request_bracket_order_pb2.RequestBracketOrder()
        rq.template_id = 330
        rq.user_tag = order_id
        rq.fcm_id = self.fcm_id
        rq.ib_id = self.ib_id
        rq.account_id = self.primary_account_id
        rq.exchange = exchange_code
        rq.symbol = security_code
        rq.quantity = quantity
        rq.transaction_type = BRACKET_SIDE_MAP[is_buy]
        rq.duration = request_bracket_order_pb2.RequestBracketOrder.Duration.DAY
        rq.bracket_type = request_bracket_order_pb2.RequestBracketOrder.BracketType.TARGET_AND_STOP
        rq.price_type = request_bracket_order_pb2.RequestBracketOrder.PriceType.LIMIT
        rq.price = limit_price
        rq.trade_route = self.get_trade_route(exchange_code)
        rq.manual_or_auto = request_bracket_order_pb2.RequestBracketOrder.OrderPlacement.MANUAL
        rq.target_quantity = quantity
        rq.target_ticks = take_profit_ticks
        rq.stop_quantity = quantity
        rq.stop_ticks = stop_loss_ticks
        rq.user_type = request_bracket_order_pb2.RequestBracketOrder.UserType.USER_TYPE_TRADER
        buffer = self._convert_request_to_buffer(rq)
        await self.ws.send(buffer)

    def submit_market_order(self, order_id: str, security_code: str, exchange_code: str, quantity: int,
                            is_buy: bool):
        asyncio.run_coroutine_threadsafe(
            self.send_market_order(order_id, security_code, exchange_code, quantity, is_buy), loop=self.loop
        )

    def submit_bracket_order(self, order_id: str, security_code: str, exchange_code: str, quantity: int,
                             is_buy: bool, limit_price: float, stop_loss_ticks: int, take_profit_ticks: int):
        asyncio.run_coroutine_threadsafe(self.send_bracket_order(
            order_id, security_code, exchange_code, quantity, is_buy, limit_price, stop_loss_ticks, take_profit_ticks
        ), loop=self.loop)

    def submit_limit_order(self, order_id: str, security_code: str, exchange_code: str, quantity: int,
                             is_buy: bool, limit_price: float):
        asyncio.run_coroutine_threadsafe(self.send_limit_order(
            order_id, security_code, exchange_code, quantity, is_buy, limit_price,
        ), loop=self.loop)

    async def send_cancel_order(self, basket_id: str):
        rq = request_cancel_order_pb2.RequestCancelOrder()
        rq.template_id = 316
        rq.user_msg.append('cancel_order')
        rq.fcm_id = self.fcm_id
        rq.ib_id = self.ib_id
        rq.account_id = self.primary_account_id
        rq.basket_id = basket_id
        rq.manual_or_auto = request_cancel_order_pb2.RequestCancelOrder.OrderPlacement.MANUAL
        buffer = self._convert_request_to_buffer(rq)
        await self.ws.send(buffer)

    def _add_account_info_to_request(self, rq):
        rq.fcm_id = self.fcm_id
        rq.ib_id = self.ib_id
        rq.account_id = self.primary_account_id
        return rq

    def submit_cancel_order(self, basket_id):
        asyncio.run_coroutine_threadsafe(self.send_cancel_order(basket_id), loop=self.loop)

    async def send_bracket_order_stop_amendment(self, basket_id: str, old_stop_ticks: int, new_stop_ticks: int):
        rq = request_update_stop_bracket_level_pb2.RequestUpdateStopBracketLevel()
        rq.template_id = 334
        rq = self._add_account_info_to_request(rq)
        rq.basket_id = basket_id
        rq.level = old_stop_ticks
        rq.stop_ticks = new_stop_ticks
        buffer = self._convert_request_to_buffer(rq)
        await self.ws.send(buffer)

    async def send_stop_loss_order_amendment(self, basket_id: str, symbol: str, exchange: str, quantity: int,
                                             stop_loss: float):
        rq = request_modify_order_pb2.RequestModifyOrder()
        rq.template_id = 314
        rq = self._add_account_info_to_request(rq)
        rq.basket_id = basket_id
        rq.symbol = symbol
        rq.exchange = exchange
        rq.quantity = quantity
        rq.trigger_price = stop_loss
        rq.price_type = request_modify_order_pb2.RequestModifyOrder.PriceType.STOP_MARKET
        rq.manual_or_auto = request_modify_order_pb2.RequestModifyOrder.OrderPlacement.MANUAL

        buffer = self._convert_request_to_buffer(rq)
        await self.ws.send(buffer)

    async def send_bracket_order_target_amendment(self, basket_id: str, old_target_ticks: int, new_target_ticks: int):
        rq = request_update_target_bracket_level_pb2.RequestUpdateTargetBracketLevel()
        rq.template_id = 332
        rq = self._add_account_info_to_request(rq)
        rq.basket_id = basket_id
        rq.level = old_target_ticks
        rq.target_ticks = new_target_ticks
        buffer = self._convert_request_to_buffer(rq)
        await self.ws.send(buffer)

    def submit_amend_bracket_order_stop_loss(self, basket_id: str, old_stop_ticks: int, new_stop_ticks: int):
        asyncio.run_coroutine_threadsafe(
            self.send_bracket_order_stop_amendment(basket_id, old_stop_ticks, new_stop_ticks), loop=self.loop,
        )

    def submit_amend_bracket_order_take_profit(self, basket_id: str, old_target_ticks: int, new_target_ticks: int):
        asyncio.run_coroutine_threadsafe(
            self.send_bracket_order_target_amendment(basket_id, old_target_ticks, new_target_ticks),
            loop=self.loop,
        )

    def submit_amend_stop_loss_order(self, basket_id: str, symbol: str, exchange: str, quantity: int, stop_loss: float):
        asyncio.run_coroutine_threadsafe(
            self.send_stop_loss_order_amendment(basket_id, symbol, exchange, quantity, stop_loss),
            loop=self.loop,
        )

