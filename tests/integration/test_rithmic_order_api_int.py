from datetime import datetime as dt
import time

import pandas as pd

from rithmic.interfaces.order.order_types import FillStatus, ChildOrderType
from rithmic.tools.general import dict_destructure, get_utc_now


ES = 'ES'
NQ = 'NQ'
EXCHANGE_CODE = 'CME'


def test_order_api_buy_limit_order_and_cancel(order_api, ticker_api):
    order_api.clear_existing_updates()
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    es = ticker_api.stream_market_data(security_code, EXCHANGE_CODE)
    while len(es.tick_dataframe) == 0:
        time.sleep(0.1)
    last_px = es.tick_dataframe.iloc[-1].close
    ticker_api.stop_market_data_stream(security_code, EXCHANGE_CODE)
    order_id = '{0}_buy_limit_cancel_order_test'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
    limit_price = last_px - (0.25 * 20)
    order = order_api.submit_limit_order(
        order_id=order_id, security_code=security_code, exchange_code=EXCHANGE_CODE, quantity=1, is_buy=True,
        limit_price=limit_price,
    )
    while order.in_market is False:
        time.sleep(0.01)

    avg_px, avg_qty = order.average_fill_price_qty
    assert order.in_market is True
    assert isinstance(order.basket_id, str)
    assert order.has_fills is False
    assert order.filled_quantity == 0
    assert pd.isna(avg_px)
    assert avg_qty == 0
    assert order.fill_status == FillStatus.UNFILLED

    assert order.cancelled is False
    assert order.cancelled_id is None
    order_api.submit_cancel_order(order.order_id)
    now = get_utc_now()
    while order.cancelled is False:
        time.sleep(0.01)
    assert order.cancelled is True
    assert order.cancelled_id is not None
    assert order.order_id in order_api.status_manager.cancelled_orders
    time_diff = order.cancelled_at - now
    assert time_diff.seconds < 2


def test_order_api_sell_limit_order_and_cancel(order_api, ticker_api):
    order_api.clear_existing_updates()
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    es = ticker_api.stream_market_data(security_code, EXCHANGE_CODE)
    while len(es.tick_dataframe) == 0:
        time.sleep(0.1)
    last_px = es.tick_dataframe.iloc[-1].close
    ticker_api.stop_market_data_stream(security_code, EXCHANGE_CODE)
    order_id = '{0}_sell_limit_cancel_order_test'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
    order = order_api.submit_limit_order(
        order_id=order_id, security_code=security_code, exchange_code=EXCHANGE_CODE, quantity=1, is_buy=False,
        limit_price=last_px + (0.25 * 10)
    )
    while order.in_market is False:
        time.sleep(0.1)

    avg_px, avg_qty = order.average_fill_price_qty
    assert order.in_market is True
    assert isinstance(order.basket_id, str)
    assert order.has_fills is False
    assert order.filled_quantity == 0
    assert pd.isna(avg_px)
    assert avg_qty == 0
    assert order.fill_status == FillStatus.UNFILLED

    assert order.cancelled is False
    assert order.cancelled_id is None
    order_api.submit_cancel_order(order.order_id)
    now = get_utc_now()
    while order.cancelled is False:
        time.sleep(0.01)
    assert order.cancelled is True
    assert order.cancelled_id is not None
    assert order.order_id in order_api.status_manager.cancelled_orders
    time_diff = order.cancelled_at - now
    assert time_diff.seconds < 2


def test_order_api_sell_limit_filled(order_api, ticker_api):
    order_api.clear_existing_updates()
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    es = ticker_api.stream_market_data(security_code, EXCHANGE_CODE)
    while len(es.tick_dataframe) == 0:
        time.sleep(0.1)
    last_px = es.tick_dataframe.iloc[-1].close
    limit_px = last_px - (0.25 * 3)
    ticker_api.stop_market_data_stream(security_code, EXCHANGE_CODE)
    order_id = '{0}_sell_limit_filled_order_test'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
    order = order_api.submit_limit_order(
        order_id=order_id, security_code=security_code, exchange_code=EXCHANGE_CODE, quantity=1, is_buy=False,
        limit_price=limit_px,
    )
    while order.in_market is False:
        time.sleep(0.1)

    avg_px, avg_qty = order.average_fill_price_qty
    assert order.in_market is True
    assert isinstance(order.basket_id, str)
    assert order.has_fills is True
    assert order.filled_quantity == 1
    assert avg_px >= limit_px
    assert avg_qty == 1
    assert order.fill_status == FillStatus.FILLED


def test_order_api_buy_market_order(order_api, ticker_api):
    order_api.clear_existing_updates()
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    order_id = '{0}_mkt_order_test'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
    order = order_api.submit_market_order(
        order_id=order_id, security_code=security_code, exchange_code=EXCHANGE_CODE, quantity=1, is_buy=True,
    )
    while len(order_api.exchange_updates_data) < 2:
        time.sleep(0.1)

    # order = order_api.get_order_by_order_id(order_id)
    avg_px, avg_qty = order.average_fill_price_qty

    assert order.in_market is True
    assert isinstance(order.basket_id, str)
    assert order.has_fills is True
    assert order.filled_quantity == 1
    assert isinstance(avg_px, float)
    assert avg_qty == 1
    assert order.fill_status == FillStatus.FILLED


def test_order_api_buy_bracket_order_and_cancel(order_api, ticker_api):
    order_api.clear_existing_updates()
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    es = ticker_api.stream_market_data(security_code, EXCHANGE_CODE)
    while len(es.tick_dataframe) < 5:
        time.sleep(0.1)
    last_px = es.tick_dataframe.iloc[-1].close
    ticker_api.stop_market_data_stream(security_code, EXCHANGE_CODE)
    order_id = '{0}_bracket_order_and_cancel_test'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
    order = order_api.submit_bracket_order(
        order_id=order_id, security_code=security_code, exchange_code=EXCHANGE_CODE, quantity=1, is_buy=True,
        limit_price=last_px - (0.25 * 20), stop_loss_ticks=10, take_profit_ticks=10,
    )
    while order.in_market is False:
        time.sleep(0.01)

    assert order.basket_id is not None
    assert order.fill_status == FillStatus.UNFILLED
    assert order.children_in_market is False

    now = get_utc_now()
    order_api.submit_cancel_order(order.order_id)
    while order.cancelled is False:
        time.sleep(0.01)
    assert order.cancelled is True
    assert order.cancelled_id is not None
    assert order.order_id in order_api.status_manager.cancelled_orders
    time_diff = order.cancelled_at - now
    assert time_diff.seconds < 2


def test_fill_bracket_order_children_created_and_cancelled(order_api, ticker_api):
    order_api.clear_existing_updates()
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    exchange_code = 'CME'
    es = ticker_api.stream_market_data(security_code, exchange_code)
    while len(es.tick_dataframe) < 5:
        time.sleep(0.1)
    last_px = es.tick_dataframe.iloc[-1].close
    limit_px = last_px + (0.25 * 1)
    stop_loss_ticks = 10
    take_profit_ticks = 10
    ticker_api.stop_market_data_stream(security_code, exchange_code)
    order_id = '{0}_bracket_order_legs_created_cancelled'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
    bracket_order = order_api.submit_bracket_order(
        order_id=order_id, security_code=security_code, exchange_code=exchange_code, quantity=1, is_buy=True,
        limit_price=limit_px, stop_loss_ticks=stop_loss_ticks, take_profit_ticks=take_profit_ticks,
    )
    while bracket_order.children_in_market is False:
        time.sleep(0.01)

    assert bracket_order.fill_status == FillStatus.FILLED
    tp_orders, sl_orders = bracket_order.child_orders

    for order in tp_orders + sl_orders:
        assert order.fill_status == FillStatus.UNFILLED
        assert order.in_market is True

    now = get_utc_now()
    order_api.submit_cancel_bracket_order_all_children(order_id)
    while bracket_order.all_children_cancelled is False:
        time.sleep(0.01)

    for order in tp_orders + sl_orders:
        time_diff = order.cancelled_at - now
        assert time_diff.seconds < 2


def test_fill_bracket_order_children_created_one_filled_one_cancelled(order_api, ticker_api):
    order_api.clear_existing_updates()
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    es = ticker_api.stream_market_data(security_code, EXCHANGE_CODE)
    while len(es.tick_dataframe) < 5:
        time.sleep(0.1)
    last_px = es.tick_dataframe.iloc[-1].close
    limit_px = last_px + (0.25 * 1)
    stop_loss_ticks = 2
    take_profit_ticks = 1
    ticker_api.stop_market_data_stream(security_code, EXCHANGE_CODE)
    order_id = '{0}_bracket_order_one_leg_filled'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
    bracket_order = order_api.submit_bracket_order(
        order_id=order_id, security_code=security_code, exchange_code=EXCHANGE_CODE, quantity=1, is_buy=True,
        limit_price=limit_px, stop_loss_ticks=stop_loss_ticks, take_profit_ticks=take_profit_ticks,
    )
    while bracket_order.children_in_market is False:
        time.sleep(0.01)

    assert bracket_order.fill_status == FillStatus.FILLED

    child_type = ChildOrderType.UNKNOWN
    while not bracket_order.filled_children_complete:
        time.sleep(0.01)
        child_filled, child_type = bracket_order.child_side_filled

    if child_type == ChildOrderType.TAKE_PROFIT:
        assert bracket_order.all_stop_loss_orders_cancelled is True
    elif child_type == ChildOrderType.STOP_LOSS:
        assert bracket_order.all_take_profit_orders_cancelled


def test_fill_bracket_order_children_created_stops_amended(order_api, ticker_api):
    order_api.clear_existing_updates()
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    es = ticker_api.stream_market_data(security_code, EXCHANGE_CODE)
    while len(es.tick_dataframe) < 5:
        time.sleep(0.1)
    last_px = es.tick_dataframe.iloc[-1].close
    limit_px = last_px + (0.25 * 3)
    stop_loss_ticks = 20
    take_profit_ticks = 50
    ticker_api.stop_market_data_stream(security_code, EXCHANGE_CODE)
    order_id = '{0}_bracket_order_stop_amend'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
    bracket_order = order_api.submit_bracket_order(
        order_id=order_id, security_code=security_code, exchange_code=EXCHANGE_CODE, quantity=1, is_buy=True,
        limit_price=limit_px, stop_loss_ticks=stop_loss_ticks, take_profit_ticks=take_profit_ticks,
    )
    while bracket_order.children_in_market is False:
        time.sleep(0.01)

    assert bracket_order.fill_status == FillStatus.FILLED
    assert bracket_order.all_stop_loss_orders_unfilled is True
    assert bracket_order.all_take_profit_orders_unfilled is True

    now = get_utc_now()

    new_stop_ticks = 10
    new_stop = limit_px - (0.25 * new_stop_ticks)
    order_api.submit_amend_bracket_order_all_stop_loss_orders(bracket_order.order_id, new_stop)

    amended = False
    while not amended:
        time.sleep(0.01)
        amended = all(o.modify_count == 1 for o in bracket_order.stop_loss_orders)

    assert all(o.trigger_price == new_stop for o in bracket_order.stop_loss_orders)


def test_fill_bracket_order_children_created_take_profit_amended(order_api, ticker_api):
    order_api.clear_existing_updates()
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    es = ticker_api.stream_market_data(security_code, EXCHANGE_CODE)
    while len(es.tick_dataframe) < 5:
        time.sleep(0.1)
    last_px = es.tick_dataframe.iloc[-1].close
    limit_px = last_px + (0.25 * 3)
    stop_loss_ticks = 20
    take_profit_ticks = 15
    ticker_api.stop_market_data_stream(security_code, EXCHANGE_CODE)
    order_id = '{0}_bracket_order_take_profit_amend'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
    bracket_order = order_api.submit_bracket_order(
        order_id=order_id, security_code=security_code, exchange_code=EXCHANGE_CODE, quantity=1, is_buy=True,
        limit_price=limit_px, stop_loss_ticks=stop_loss_ticks, take_profit_ticks=take_profit_ticks,
    )
    while bracket_order.children_in_market is False:
        time.sleep(0.01)

    assert bracket_order.fill_status == FillStatus.FILLED
    assert bracket_order.all_stop_loss_orders_unfilled is True
    assert bracket_order.all_take_profit_orders_unfilled is True

    now = get_utc_now()

    new_take_ticks = 10
    new_limit = limit_px + (0.25 * new_take_ticks)
    order_api.submit_amend_bracket_order_all_take_profit_orders(bracket_order.order_id, new_limit)

    amended = False
    while not amended:
        time.sleep(0.01)
        amended = all(o.modify_count == 1 for o in bracket_order.take_profit_orders)

    assert all(o.limit_price == new_limit for o in bracket_order.take_profit_orders)
    modify_history = [o.modify_history for o in bracket_order.take_profit_orders]
    for history in modify_history:
        record = history[1]
        assert record['new_limit_price'] == new_limit
        assert record['old_limit_price'] == limit_px + (take_profit_ticks * 0.25)
        assert isinstance(record['modify_id'], str)


def test_bracket_order_rejected(order_api, ticker_api):
    order_api.clear_existing_updates()
    security_code = ticker_api.get_front_month_contract(ES, EXCHANGE_CODE)
    es = ticker_api.stream_market_data(security_code, EXCHANGE_CODE)
    while len(es.tick_dataframe) < 5:
        time.sleep(0.1)
    last_px = es.tick_dataframe.iloc[-1].close
    limit_px = last_px + (0.25 * 3)
    quantity = 150 # Large quantity above margin limit
    stop_loss_ticks = 20
    take_profit_ticks = 15
    ticker_api.stop_market_data_stream(security_code, EXCHANGE_CODE)
    order_id = '{0}_bracket_order_rejected'.format(dt.now().strftime('%Y%m%d_%H%M%S'))
    bracket_order = order_api.submit_bracket_order(
        order_id=order_id, security_code=security_code, exchange_code=EXCHANGE_CODE, quantity=quantity, is_buy=True,
        limit_price=limit_px, stop_loss_ticks=stop_loss_ticks, take_profit_ticks=take_profit_ticks,
    )
    while bracket_order.rejected is False:
        time.sleep(0.01)

    assert bracket_order.rejected_reason == 'Rejected at RMS - Available margin exhausted'

