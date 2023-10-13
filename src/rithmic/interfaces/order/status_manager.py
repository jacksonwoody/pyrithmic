from typing import Union

from rithmic.interfaces.order.order_types import ChildOrderType, CHILD_TYPE_MAP, MarketOrder, LimitOrder, \
    TakeProfitOrder, StopLossOrder, BracketOrder, VALID_ORDER_TYPES
from rithmic.tools.general import dict_destructure
from rithmic.tools.pyrithmic_exceptions import DuplicateOrderIdException
from rithmic.tools.pyrithmic_logger import logger


class StatusManager:
    def __init__(self):
        self.child_parent_map = dict()
        self.cancelled_orders = []
        self.orders = dict()
        self.fill_data = []

    def add_new_order(self, order: VALID_ORDER_TYPES):
        order_id = order.order_id
        if order_id in self.orders.keys():
            raise DuplicateOrderIdException('Order ID {0} already used, must be unique'.format(order_id))
        self.orders[order_id] = order

    def get_order_by_order_id(self, order_id: str) -> VALID_ORDER_TYPES:
        return self.orders.get(order_id)

    def get_order_by_basket_id(self, basket_id: str) -> VALID_ORDER_TYPES:
        order_id = self.basket_id_order_id_map[basket_id]
        return self.get_order_by_order_id(order_id)

    def get_child_orders_from_parent_order_id(self, order_id: str) -> tuple:
        parent_order = self.get_order_by_order_id(order_id)
        return parent_order.child_orders

    def get_parent_order_from_child_order_id(self, order_id: str) -> BracketOrder:
        child_order = self.get_order_by_order_id(order_id)
        bracket_order = self.get_order_by_order_id(child_order.parent_order_id)
        return bracket_order

    def add_market_order(self, order_id: str, security_code: str, exchange_code: str, quantity: int,
                         is_buy: bool) -> MarketOrder:
        order = MarketOrder(order_id, security_code, exchange_code, quantity, is_buy)
        self.add_new_order(order)
        return order

    def add_limit_order(self, order_id: str, security_code: str, exchange_code: str, quantity: int, is_buy: bool,
                        limit_price: float) -> LimitOrder:
        order = LimitOrder(order_id, security_code, exchange_code, quantity, is_buy, limit_price)
        self.add_new_order(order)
        return order

    def add_bracket_order(self, order_id: str, security_code: str, exchange_code: str, quantity: int, is_buy: bool,
                          limit_price: float, stop_loss_ticks: int, take_profit_ticks: int) -> BracketOrder:
        order = BracketOrder(
            order_id, security_code, exchange_code, quantity, is_buy, limit_price, stop_loss_ticks, take_profit_ticks
        )
        self.add_new_order(order)
        return order

    def add_take_profit_order(self, data: dict, parent_order: BracketOrder) -> TakeProfitOrder:
        order_id = parent_order.generate_new_take_profit_order_id
        cols = ['symbol', 'exchange', 'confirmed_size', 'transaction_type', 'price']
        security_code, exchange_code, quantity, transaction_type, limit_price = dict_destructure(data, cols)
        is_buy = transaction_type == 1
        order = TakeProfitOrder(
            order_id, security_code, exchange_code, quantity, is_buy, limit_price, parent_order.order_id
        )
        self.add_new_order(order)
        return order

    def add_stop_loss_order(self, data: dict, parent_order: BracketOrder) -> StopLossOrder:
        order_id = parent_order.generate_new_stop_loss_order_id
        cols = ['symbol', 'exchange', 'confirmed_size', 'transaction_type', 'trigger_price']
        security_code, exchange_code, quantity, transaction_type, trigger_price = dict_destructure(data, cols)
        is_buy = transaction_type == 1
        order = StopLossOrder(
            order_id, security_code, exchange_code, quantity, is_buy, trigger_price, parent_order.order_id
        )
        self.add_new_order(order)
        return order

    def process_exchange_update(self, data: dict):
        try:
            report_type = data['report_type']
            if report_type == 'status':
                self.process_order_status_report(data)
            elif report_type == 'fill':
                self.process_order_fill_report(data)
            elif report_type == 'cancel':
                self.process_order_cancel_report(data)
            elif report_type == 'modify':
                self.process_order_modify_report(data)
            else:
                logger.info('Unprocessed Report Type: {0}\n\r{1}'.format(report_type, data))
        except Exception as e:
            raise(e)

    def process_order_status_report(self, data: dict):
        order_id = data.get('order_id')
        if order_id is not None:
            order = self.get_order_by_order_id(order_id)
            basket_id = data.get('basket_id')
            order._add_basket_id(basket_id)
        else:
            self.process_bracket_order_child(data)

    def map_child_order(self, parent_order: BracketOrder, child_order: Union[TakeProfitOrder, StopLossOrder],
                        child_order_type: ChildOrderType, basket_id: str):
        child_order._add_basket_id(basket_id)
        self.child_parent_map[child_order.order_id] = child_order.parent_order_id
        parent_order._add_child_order(child_order, child_order_type)

    def _get_child_type_from_price_type(self, price_type: int):
        return CHILD_TYPE_MAP.get(price_type, ChildOrderType.UNKNOWN)

    def process_bracket_order_child(self, data: dict):
        if 'original_basket_id' in data:
            parent_basket_id = data['original_basket_id']
            parent_order_id = self.basket_id_order_id_map[parent_basket_id]
            assert parent_order_id in self.orders.keys()
            parent_order = self.get_order_by_order_id(parent_order_id)
            price_type = data['orig_price_type']
            basket_id = data.get('basket_id')
            order = None
            child_type = self._get_child_type_from_price_type(price_type)
            if child_type == ChildOrderType.TAKE_PROFIT:
                order = self.add_take_profit_order(data, parent_order)
            elif child_type == ChildOrderType.STOP_LOSS:
                order = self.add_stop_loss_order(data, parent_order)
            if order is not None:
                self.map_child_order(parent_order, order, child_type, basket_id)

    def process_order_fill_report(self, data: dict):
        is_buy = data['transaction_type'] == 1
        basket_id = data['basket_id']
        order = self.get_order_by_basket_id(basket_id)
        fill = dict(
            timestamp=data['update_time'], order_id=order.order_id,
            security_code=data['symbol'], exchange_code=data['exchange'],
            is_buy=is_buy, quantity=data['fill_size'], price=data['fill_price'], fill_id=data['fill_id']
        )
        self.fill_data.append(fill)
        order._add_fill(fill)

    def process_order_cancel_report(self, data: dict):
        basket_id = data['basket_id']
        order = self.get_order_by_basket_id(basket_id)
        cancelled_id = data['cancelled_id']
        timestamp = data['update_time']
        order._cancel_order(timestamp, cancelled_id)
        self.cancelled_orders.append(order.order_id)

    def process_order_modify_report(self, data: dict):
        cols = ['update_time', 'basket_id', 'price_type', 'modify_id']
        timestamp, basket_id, price_type, modify_id = dict_destructure(data, cols)
        order = self.get_order_by_basket_id(basket_id)
        if isinstance(order, BracketOrder):
            pass
        else:
            child_type = self._get_child_type_from_price_type(price_type)
            new_level = None
            if child_type == ChildOrderType.STOP_LOSS:
                new_level = data['trigger_price']
            elif child_type == ChildOrderType.TAKE_PROFIT:
                new_level = data['price']
            if child_type != ChildOrderType.UNKNOWN:
                order._modify_order(timestamp, modify_id, new_level)

    @property
    def basket_id_order_id_map(self):
        return {order.basket_id: order_id for order_id, order in self.orders.items() if order.basket_id is not None}

    @property
    def order_id_basket_id_map(self):
        return {order_id: order.basket_id for order_id, order in self.orders.items() if order.basket_id is not None}
