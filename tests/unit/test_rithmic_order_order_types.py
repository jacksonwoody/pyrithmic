import numpy as np
import pytest

from rithmic.interfaces.order.order_types import MarketOrder, FillStatus, LimitOrder, TakeProfitOrder, StopLossOrder, \
    BracketOrder, ChildOrderType
from rithmic.tools.general import get_utc_now
from rithmic.tools.pyrithmic_exceptions import UncancellableOrderException, UnmodifiableOrderException

TEST_SEC = 'ESZ3'
TEST_EXCH = 'CME'
TICK_MULT = 0.25


def test_market_order():
    is_buy = True
    qty = 10
    o = MarketOrder(order_id='123', security_code=TEST_SEC, exchange_code=TEST_EXCH, quantity=qty, is_buy=is_buy)

    assert o.fill_status == FillStatus.UNFILLED
    avg_px, avg_qty = o.average_fill_price_qty
    assert np.isnan(avg_px)
    assert avg_qty == 0

    now = get_utc_now()
    assert o.basket_id is None
    o._add_basket_id('abc', now)

    assert o.basket_id == 'abc'
    assert o.in_market is True
    assert o.in_market_at == now
    assert o.has_fills is False
    assert o.last_modification is None

    with pytest.raises(UncancellableOrderException):
        o._cancel_order(get_utc_now(), 'cancel_123', o.unfilled_quantity)

    with pytest.raises(UnmodifiableOrderException):
        o._modify_order(get_utc_now(), 'mod_123', 4000.)

    fill_data = {
        'timestamp': get_utc_now(), 'order_id': 'mkt_order_test', 'security_code': TEST_SEC, 'exchange_code': TEST_EXCH,
        'is_buy': is_buy, 'quantity': 5, 'price': 4312.25, 'fill_id': 'fill_id_123'}
    o._add_fill(fill_data)
    assert o.fill_status == FillStatus.PARTIAL

    fill_data = {
        'timestamp': get_utc_now(), 'order_id': 'mkt_order_test', 'security_code': TEST_SEC, 'exchange_code': TEST_EXCH,
        'is_buy': is_buy, 'quantity': 5, 'price': 4312.75, 'fill_id': 'fill_id_234'}
    o._add_fill(fill_data)
    assert o.fill_status == FillStatus.FILLED

    df = o.fill_dataframe
    assert len(df) == 2

    avg_px, fill_qty = o.average_fill_price_qty
    assert avg_px == 4312.5
    assert fill_qty == 10 == o.filled_quantity


def test_limit_order():
    is_buy = True
    qty = 10
    o = LimitOrder(order_id='123', security_code=TEST_SEC, exchange_code=TEST_EXCH, quantity=qty, is_buy=is_buy,
                   limit_price=4000.)

    assert o.fill_status == FillStatus.UNFILLED
    avg_px, avg_qty = o.average_fill_price_qty
    assert np.isnan(avg_px)
    assert avg_qty == 0

    now = get_utc_now()
    assert o.basket_id is None
    o._add_basket_id('abc', now)

    assert o.basket_id == 'abc'
    assert o.in_market is True
    assert o.in_market_at == now
    assert o.has_fills is False
    assert o.last_modification is None

    o._modify_order(get_utc_now(), 'mod_123', 4010.)
    assert o.modified is True
    assert o.modify_count == 1
    assert o.modify_field == 'limit_price'

    fill_data = {
        'timestamp': get_utc_now(), 'order_id': 'mkt_order_test', 'security_code': TEST_SEC, 'exchange_code': TEST_EXCH,
        'is_buy': is_buy, 'quantity': 5, 'price': 4009.5, 'fill_id': 'fill_id_123'}
    o._add_fill(fill_data)
    assert o.fill_status == FillStatus.PARTIAL

    fill_data = {
        'timestamp': get_utc_now(), 'order_id': 'mkt_order_test', 'security_code': TEST_SEC, 'exchange_code': TEST_EXCH,
        'is_buy': is_buy, 'quantity': 5, 'price': 4010., 'fill_id': 'fill_id_234'}
    o._add_fill(fill_data)
    assert o.fill_status == FillStatus.FILLED

    df = o.fill_dataframe
    assert len(df) == 2

    avg_px, fill_qty = o.average_fill_price_qty
    assert avg_px == 4009.75
    assert fill_qty == 10 == o.filled_quantity


def test_take_profit_order():
    is_buy = True
    qty = 10
    o = TakeProfitOrder(order_id='123', security_code=TEST_SEC, exchange_code=TEST_EXCH, quantity=qty, is_buy=is_buy,
                   limit_price=4000., parent_order_id='p1')

    assert o.fill_status == FillStatus.UNFILLED
    avg_px, avg_qty = o.average_fill_price_qty
    assert np.isnan(avg_px)
    assert avg_qty == 0

    now = get_utc_now()
    assert o.basket_id is None
    o._add_basket_id('abc', now)

    assert o.basket_id == 'abc'
    assert o.in_market is True
    assert o.in_market_at == now
    assert o.has_fills is False
    assert o.last_modification is None

    o._modify_order(get_utc_now(), 'mod_123', 4010.)
    assert o.modified is True
    assert o.modify_count == 1
    assert o.modify_field == 'limit_price'

    assert o.cancelled is False
    o._cancel_order(get_utc_now(), 'cancel_1', o.unfilled_quantity)
    assert o.cancelled is True


def test_stop_loss_order():
    is_buy = False
    qty = 10
    o = StopLossOrder(order_id='123', security_code=TEST_SEC, exchange_code=TEST_EXCH, quantity=qty, is_buy=is_buy,
                      trigger_price=4000., parent_order_id='p1')

    assert o.fill_status == FillStatus.UNFILLED
    avg_px, avg_qty = o.average_fill_price_qty
    assert np.isnan(avg_px)
    assert avg_qty == 0

    now = get_utc_now()
    assert o.basket_id is None
    o._add_basket_id('abc', now)

    assert o.basket_id == 'abc'
    assert o.in_market is True
    assert o.in_market_at == now
    assert o.has_fills is False
    assert o.last_modification is None

    o._modify_order(get_utc_now(), 'mod_123', 4010.)
    assert o.modified is True
    assert o.modify_count == 1
    assert o.modify_field == 'trigger_price'
    assert o.trigger_price == 4010.

    assert o.cancelled is False
    o._cancel_order(get_utc_now(), 'cancel_1', o.unfilled_quantity)
    assert o.cancelled is True


def test_bracket_order():
    order_id = 'bracket1'
    qty = 10
    is_buy = True
    limit_px = 4000
    stop_ticks = 8
    take_ticks = 8
    o = BracketOrder(order_id=order_id, security_code=TEST_SEC, exchange_code=TEST_EXCH, quantity=qty, is_buy=is_buy,
                     limit_price=limit_px, take_profit_ticks=take_ticks, stop_loss_ticks=stop_ticks,
                     tick_multiplier=TICK_MULT,
                   )

    fill_data = {
        'timestamp': get_utc_now(), 'order_id': order_id, 'security_code': TEST_SEC, 'exchange_code': TEST_EXCH,
        'is_buy': is_buy, 'quantity': qty, 'price': 4000., 'fill_id': 'fill_1'}
    o._add_fill(fill_data)
    assert o.fill_status == FillStatus.FILLED

    assert o.children_in_market is False
    o._add_stop_loss_order(
        StopLossOrder(o.generate_new_stop_loss_order_id, TEST_SEC, TEST_EXCH, qty, False, 3998, o.order_id)
    )
    assert o.children_in_market is False
    o._add_take_profit_order(
        TakeProfitOrder(o.generate_new_take_profit_order_id, TEST_SEC, TEST_EXCH, qty, False, 4002., o.order_id)
    )
    assert o.children_in_market is True

    tp, sl = o.child_orders
    assert len(tp) == 1
    assert len(sl) == 1

    assert o.all_children_cancelled is False
    assert o.all_stop_loss_orders_filled is False
    assert o.all_take_profit_orders_filled is False
    assert o.all_stop_loss_orders_cancelled is False
    assert o.all_take_profit_orders_cancelled is False

    stop_loss = sl[0]
    fill_data = {
        'timestamp': get_utc_now(), 'order_id': stop_loss.order_id, 'security_code': TEST_SEC,
        'exchange_code': TEST_EXCH,
        'is_buy': is_buy, 'quantity': qty, 'price': 3998., 'fill_id': 'fill_1'}
    stop_loss._add_fill(fill_data)

    filled, side = o.child_side_filled
    assert filled is True
    assert side == ChildOrderType.STOP_LOSS




