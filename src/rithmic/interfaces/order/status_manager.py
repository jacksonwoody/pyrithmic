from typing import Union

from rithmic import CallbackManager, CallbackId
from rithmic.interfaces.order.order_types import ChildOrderType, CHILD_TYPE_MAP, MarketOrder, LimitOrder, \
    TakeProfitOrder, StopLossOrder, BracketOrder, VALID_ORDER_TYPES
from rithmic.tools.general import dict_destructure
from rithmic.tools.pyrithmic_exceptions import DuplicateOrderIdException
from rithmic.tools.pyrithmic_logger import logger


class StatusManager:
    """
    Status Manager is used internally only by the Order API to map orders and update order status as messages flow
    from the Exchange and Rithmic
    """
    def __init__(self, callback_manager: CallbackManager = None):
        """
        Init constructor callback manager from Order API passed through for callbacks on status changes
        """
        self.child_parent_map = dict()
        self.cancelled_orders = []
        self.orders = dict()
        self.fill_data = []
        self.callback_manager = None
        self.add_callback_manager(callback_manager)

    def __getstate__(self):
        state_map = self.__dict__.copy()
        del state_map['callback_manager']
        return state_map

    def add_callback_manager(self, callback_manager: Union[CallbackManager, None]):
        self.callback_manager = callback_manager if callback_manager is not None else CallbackManager()

    def _add_new_order(self, order: VALID_ORDER_TYPES) -> None:
        """Checks uniqueness of order id across session and internally maps the order"""
        order_id = order.order_id
        if order_id in self.orders.keys():
            raise DuplicateOrderIdException('Order ID {0} already used, must be unique'.format(order_id))
        self.orders[order_id] = order

    def _get_order_by_order_id(self, order_id: str) -> VALID_ORDER_TYPES:
        """Gets a VALID_ORDER_TYPE already mapped by the system using user Order ID"""
        return self.orders.get(order_id)

    def _get_order_by_basket_id(self, basket_id: str) -> VALID_ORDER_TYPES:
        """Gets a VALID_ORDER_TYPE already mapped by the system using Rithmic Basket ID"""
        order_id = self.basket_id_order_id_map[basket_id]
        return self._get_order_by_order_id(order_id)

    def _add_market_order(self, order_id: str, security_code: str, exchange_code: str, quantity: int,
                          is_buy: bool) -> MarketOrder:
        """
        Internally creates and maps a new market order

        :param order_id: (str) Unique string per order
        :param security_code: (str) Valid Security Code
        :param exchange_code: (str) Valid Exchange Code
        :param quantity: (int) Quantity in lots of the Order
        :param is_buy: (bool) True for a Buy, False for a Sell
        :return: (MarketOrder) the created market order
        """
        order = MarketOrder(order_id, security_code, exchange_code, quantity, is_buy)
        self._add_new_order(order)
        return order

    def _add_limit_order(self, order_id: str, security_code: str, exchange_code: str, quantity: int, is_buy: bool,
                         limit_price: float) -> LimitOrder:
        """
        Internally creates and maps a new limit order

        :param order_id: (str) Unique string per order
        :param security_code: (str) Valid Security Code
        :param exchange_code: (str) Valid Exchange Code
        :param quantity: (int) Quantity in lots of the Order
        :param is_buy: (bool) True for a Buy, False for a Sell
        :param limit_price: (float) Upper/Lower limit for a Buy/Sell to fill at
        :return: (LimitOrder) the created Limit Order
        """
        order = LimitOrder(order_id, security_code, exchange_code, quantity, is_buy, limit_price)
        self._add_new_order(order)
        return order

    def _add_bracket_order(self, order_id: str, security_code: str, exchange_code: str, quantity: int, is_buy: bool,
                           limit_price: float, take_profit_ticks: int, stop_loss_ticks: int,
                           tick_multiplier: float) -> BracketOrder:
        """
        Internally creates and maps a new bracket order

        :param order_id: (str) Unique string per order
        :param security_code: (str) Valid Security Code
        :param exchange_code: (str) Valid Exchange Code
        :param quantity: (int) Quantity in lots of the Order
        :param is_buy: (bool) True for a Buy, False for a Sell
        :param limit_price: (float) Upper/Lower limit for a Buy/Sell to fill the parent at
        :param take_profit_ticks: (int) Number of ticks from limit price to set Take Profit Limit Price
        :param stop_loss_ticks: (int) Number of ticks from limit price to set Stop Loss Trigger Price
        :param tick_multiplier: (float) minimum move for this security
        :return: (BracketOrder) the created Bracket Order
        """
        order = BracketOrder(
            order_id, security_code, exchange_code, quantity, is_buy, limit_price, take_profit_ticks, stop_loss_ticks,
            tick_multiplier,
        )
        self._add_new_order(order)
        return order

    def _add_take_profit_order(self, data: dict, parent_order: BracketOrder) -> TakeProfitOrder:
        """
        Internally creates and maps a new take profit order as message arrives from Exchange

        :param data: (dict) message from the Exchange
        :param parent_order: (BracketOrder) parent order of new child
        :return: (TakeProfitOrder) the created Take Profit Order
        """
        order_id = parent_order.generate_new_take_profit_order_id
        cols = ['symbol', 'exchange', 'confirmed_size', 'transaction_type', 'price']
        security_code, exchange_code, quantity, transaction_type, limit_price = dict_destructure(data, cols)
        is_buy = transaction_type == 1
        order = TakeProfitOrder(
            order_id, security_code, exchange_code, quantity, is_buy, limit_price, parent_order.order_id
        )
        self._add_new_order(order)
        return order

    def add_stop_loss_order(self, data: dict, parent_order: BracketOrder) -> StopLossOrder:
        """
        Internally creates and maps a new stop loss order as message arrives from Exchange

        :param data: (dict) message from the Exchange
        :param parent_order: (BracketOrder) parent order of new child
        :return: (StopLossOrder) the created Stop Loss Order
        """
        order_id = parent_order.generate_new_stop_loss_order_id
        cols = ['symbol', 'exchange', 'confirmed_size', 'transaction_type', 'trigger_price']
        security_code, exchange_code, quantity, transaction_type, trigger_price = dict_destructure(data, cols)
        is_buy = transaction_type == 1
        order = StopLossOrder(
            order_id, security_code, exchange_code, quantity, is_buy, trigger_price, parent_order.order_id
        )
        self._add_new_order(order)
        return order

    def _process_exchange_update(self, data: dict) -> None:
        """
        Routing function for new messages arriving from the Exchange
        :param data: (dict) message from the Exchange
        :return: None
        """
        try:
            report_type = data['report_type']
            if report_type == 'status':
                self._process_order_status_report(data)
            elif report_type == 'fill':
                self._process_order_fill_report(data)
            elif report_type == 'cancel':
                self._process_order_cancel_report(data)
            elif report_type == 'modify':
                self._process_order_modify_report(data)
            else:
                logger.info('Unprocessed Report Type: {0}\n\r{1}'.format(report_type, data))
        except Exception as e:
            raise (e)

    def _process_rithmic_update(self, data: dict) -> None:
        """
        Routing function for new messages arriving from Rithmic
        :param data: (dict) message from Rithmic
        :return: None
        """
        if data.get('completion_reason') == 'FA':
            self._process_order_complete_rejected(data)

    def _process_order_complete_rejected(self, data: dict) -> None:
        """Handles a rejected order notification"""
        order = self._get_order_by_order_id(data['order_id'])
        timestamp, reason = data['update_time'], data['report_text']
        order._mark_order_rejected(timestamp, reason)

    def _process_order_status_report(self, data: dict) -> None:
        """Handles an order that is valid and recognised by the Exchange"""
        order_id = data.get('order_id')
        if order_id is not None:
            order = self._get_order_by_order_id(order_id)
            basket_id = data.get('basket_id')
            order._add_basket_id(basket_id)
        else:
            self._process_bracket_order_child(data)

    def _map_child_order(self, parent_order: BracketOrder, child_order: Union[TakeProfitOrder, StopLossOrder],
                         child_order_type: ChildOrderType, basket_id: str) -> None:
        """Maps a child order, adds Rithmic ID and maps to Parent Order"""
        child_order._add_basket_id(basket_id)
        self.child_parent_map[child_order.order_id] = child_order.parent_order_id
        parent_order._add_child_order(child_order, child_order_type)

    def _get_child_type_from_price_type(self, price_type: int) -> ChildOrderType:
        """Gets the Child Order Type from the exchange metadata"""
        return CHILD_TYPE_MAP.get(price_type, ChildOrderType.UNKNOWN)

    def _process_bracket_order_child(self, data: dict) -> None:
        """Handles new children of parent Bracket Order when notified by the Exchange"""
        if 'original_basket_id' in data:
            parent_basket_id = data['original_basket_id']
            parent_order_id = self.basket_id_order_id_map[parent_basket_id]
            assert parent_order_id in self.orders.keys()
            parent_order = self._get_order_by_order_id(parent_order_id)
            price_type = data['orig_price_type']
            basket_id = data.get('basket_id')
            order = None
            child_type = self._get_child_type_from_price_type(price_type)
            if child_type == ChildOrderType.TAKE_PROFIT:
                order = self._add_take_profit_order(data, parent_order)
            elif child_type == ChildOrderType.STOP_LOSS:
                order = self.add_stop_loss_order(data, parent_order)
            if order is not None:
                self._map_child_order(parent_order, order, child_type, basket_id)

    def _process_order_fill_report(self, data: dict) -> None:
        """Handles new fill messages, adds to status manager and the relevant order, callback run if provided"""
        is_buy = data['transaction_type'] == 1
        basket_id = data['basket_id']
        order = self._get_order_by_basket_id(basket_id)
        parent_order_id = None
        if isinstance(order, (TakeProfitOrder, StopLossOrder)):
            parent_order_id = order.parent_order_id
        if isinstance(order, BracketOrder):
            parent_order_id = order.order_id
        fill = dict(
            timestamp=data['update_time'], order_id=order.order_id, parent_order_id=parent_order_id,
            security_code=data['symbol'], exchange_code=data['exchange'],
            is_buy=is_buy, quantity=data['fill_size'], price=data['fill_price'], fill_id=data['fill_id']
        )
        self.fill_data.append(fill)
        order._add_fill(fill)
        callback = self.callback_manager.get_callback_by_callback_id(CallbackId.ORDER_NEW_FILL_NOTIFICATION)
        if callback is not None:
            callback(fill)

    def _process_order_cancel_report(self, data: dict) -> None:
        """Handles cancellation messages from the Exchange"""
        basket_id = data['basket_id']
        order = self._get_order_by_basket_id(basket_id)
        cancelled_id = data['cancelled_id']
        timestamp = data['update_time']
        cancelled_qty = order.unfilled_quantity
        order._cancel_order(timestamp, cancelled_id, cancelled_qty)
        self.cancelled_orders.append(order.order_id)

    def _process_order_modify_report(self, data: dict) -> None:
        """Handles modification messages from the Exchange"""
        cols = ['update_time', 'basket_id', 'price_type', 'modify_id']
        timestamp, basket_id, price_type, modify_id = dict_destructure(data, cols)
        order = self._get_order_by_basket_id(basket_id)
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
    def basket_id_order_id_map(self) -> dict:
        """Returns dict mapping of Rithmic Basket ID to User Order ID"""
        return {order.basket_id: order_id for order_id, order in self.orders.items() if order.basket_id is not None}

    @property
    def order_id_basket_id_map(self) -> dict:
        """Returns dict mapping of User Order ID to Rithmic Basket ID"""
        return {order_id: order.basket_id for order_id, order in self.orders.items() if order.basket_id is not None}

    def __eq__(self, other):
        assert self.child_parent_map == other.child_parent_map
        assert self.cancelled_orders == other.cancelled_orders
        for k, order in self.orders.items():
            try:
                other_order = other.orders[k]
                assert order == other_order
            except AssertionError as e:
                x = 1
        assert self.fill_data == other.fill_data
        return True
