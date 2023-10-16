from datetime import datetime as dt

import pytz

from rithmic.interfaces.order.order_types import BracketOrder, FillStatus, ChildOrderType
from rithmic.interfaces.order.status_manager import StatusManager

TEST_SEC = 'ESZ3'
TEST_EXCH = 'CME'


def simulate_exchange_updates_to_status_manager(status_manager: StatusManager, exchange_updates: list):
    for exchange_update in exchange_updates:
        status_manager._process_exchange_update(exchange_update)


def test_status_manager_bracket_order_filled_child_filled():
    sm = StatusManager()
    exchange_updates = [
        {'template_id': 352, 'update_time': dt(2023, 10, 9, 13, 27, 48, 739370, tzinfo=pytz.utc), 'symbol': TEST_SEC,
         'exchange': TEST_EXCH, 'basket_id': '1687449781', 'price': 4323.5, 'transaction_type': 1, 'duration': 1,
         'price_type': 1, 'trade_route': 'simulator', 'trade_exchange': TEST_EXCH, 'report_type': 'status',
         'ssboe': 1696858068, 'usecs': 739370, 'notify_type': 1,
         'user_tag': '20231009_142748_bracket_order_one_leg_filled', 'currency': 'USD', 'manual_or_auto': 1,
         'orig_price_type': 1, 'bracket_type': 6, 'order_id': '20231009_142748_bracket_order_one_leg_filled'},
        {'template_id': 352, 'update_time': dt(2023, 10, 9, 13, 27, 48, 739382,
                                               tzinfo=pytz.utc), 'symbol': TEST_SEC, 'exchange': TEST_EXCH,
         'price': 4323.5, 'fill_price': 4323.25, 'fill_size': 1,
         'fill_time': '13:27:48', 'fill_date': '20231009', 'fill_id': '1004589', 'avg_fill_price': 4323.25,
         'sequence_number': 'Q8U70', 'transaction_type': 1, 'duration': 1, 'price_type': 1, 'trade_route': 'simulator',
         'trade_exchange': TEST_EXCH, 'report_type': 'fill', 'basket_id': '1687449781',
         'ssboe': 1696858068, 'usecs': 739382, 'notify_type': 5,
         'ib_id': 'Rithmic', 'total_fill_size': 1, 'total_unfilled_size': 0,
         'user_tag': '20231009_142748_bracket_order_one_leg_filled', 'currency': 'USD', 'manual_or_auto': 1,
         'orig_price_type': 1, 'bracket_type': 6, 'order_id': '20231009_142748_bracket_order_one_leg_filled'},
        {'template_id': 352, 'update_time': dt(2023, 10, 9, 13, 27, 48, 741067,
                                               tzinfo=pytz.utc), 'symbol': TEST_SEC, 'exchange': TEST_EXCH,
         'instrument_type': 'Future', 'basket_id': '1687449782', 'price': 4323.75, 'confirmed_time': '13:27:48',
         'confirmed_date': '20231009', 'confirmed_size': 1, 'confirmed_id': '1004590',
         'linked_basket_ids': '1687449782,1687449783', 'sequence_number': 'Q8U71', 'transaction_type': 2, 'duration': 1,
         'price_type': 1, 'trade_route': 'simulator', 'trade_exchange': TEST_EXCH, 'report_type': 'status',
         'usecs': 741067, 'notify_type': 1, 'account_id': '486559',
         'original_basket_id': '1687449781', 'manual_or_auto': 2, 'orig_price_type': 1, 'bracket_type': 6,
         'order_id': None},
        {'template_id': 352, 'update_time': dt(2023, 10, 9, 13, 27, 48, 741130,
                                               tzinfo=pytz.utc), 'symbol': TEST_SEC, 'exchange': TEST_EXCH,
         'instrument_type': 'Future', 'basket_id': '1687449783', 'confirmed_time': '13:27:48',
         'confirmed_date': '20231009', 'confirmed_size': 1, 'confirmed_id': '1004591',
         'linked_basket_ids': '1687449782,1687449783', 'sequence_number': 'Q8U72', 'transaction_type': 2, 'duration': 1,
         'price_type': 4, 'trade_route': 'simulator', 'trade_exchange': TEST_EXCH, 'report_type': 'status',
         'trigger_price': 4323.0,
         'orig_sequence_number': 'Q8U72', 'cor_sequence_number': 'Q8U72', 'ssboe': 1696858068, 'usecs': 741130,
         'notify_type': 1, 'total_fill_size': 0,
         'total_unfilled_size': 1, 'currency': 'USD', 'original_basket_id': '1687449781', 'manual_or_auto': 2,
         'orig_price_type': 4, 'bracket_type': 6, 'order_id': None},
        {'template_id': 352, 'update_time': dt(2023, 10, 9, 13, 27, 50, 765834,
                                               tzinfo=pytz.utc), 'symbol': TEST_SEC, 'exchange': TEST_EXCH,
         'instrument_type': 'Future', 'basket_id': '1687449783', 'confirmed_time': '13:27:50',
         'confirmed_date': '20231009', 'confirmed_size': 1, 'linked_basket_ids': '1687449782,1687449783',
         'sequence_number': 'Q8U72', 'transaction_type': 2, 'duration': 1, 'price_type': 2, 'trade_route': 'simulator',
         'trade_exchange': TEST_EXCH, 'report_type': 'trigger',
         'exchange_order_id': '1687449783', 'trigger_price': 4323.0, 'orig_sequence_number': 'Q8U72',
         'cor_sequence_number': 'Q8U72', 'trigger_id': '1004592', 'ssboe': 1696858070, 'usecs': 765834,
         'notify_type': 4, 'total_fill_size': 0,
         'total_unfilled_size': 1, 'currency': 'USD', 'original_basket_id': '1687449781', 'manual_or_auto': 2,
         'orig_price_type': 4, 'bracket_type': 6, 'order_id': None},
        {'template_id': 352, 'update_time': dt(2023, 10, 9, 13, 27, 50, 765976,
                                               tzinfo=pytz.utc), 'symbol': TEST_SEC, 'exchange': TEST_EXCH,
         'instrument_type': 'Future', 'basket_id': '1687449783', 'fill_price': 4323.0, 'fill_size': 1,
         'fill_time': '13:27:50', 'fill_date': '20231009', 'fill_id': '1004593', 'avg_fill_price': 4323.0,
         'linked_basket_ids': '1687449782,1687449783', 'sequence_number': 'Q8U72', 'transaction_type': 2, 'duration': 1,
         'price_type': 2, 'trade_route': 'simulator', 'trade_exchange': TEST_EXCH, 'report_type': 'fill',
         'trigger_price': 4323.0,
         'orig_sequence_number': 'Q8U72', 'cor_sequence_number': 'Q8U72', 'ssboe': 1696858070, 'usecs': 765976,
         'notify_type': 5, 'account_id': '486559', 'fcm_id': 'Rithmic', 'ib_id': 'Rithmic', 'total_fill_size': 1,
         'total_unfilled_size': 0, 'currency': 'USD', 'original_basket_id': '1687449781', 'manual_or_auto': 2,
         'orig_price_type': 4, 'bracket_type': 6, 'order_id': None},
        {'template_id': 352, 'update_time': dt(2023, 10, 9, 13, 27, 50, 767370,
                                               tzinfo=pytz.utc), 'symbol': TEST_SEC, 'exchange': TEST_EXCH,
         'instrument_type': 'Future', 'basket_id': '1687449782', 'price': 4323.75, 'cancelled_size': 1,
         'cancelled_time': '13:27:50', 'cancelled_date': '20231009', 'cancelled_id': '1004594',
         'linked_basket_ids': '1687449782,1687449783', 'sequence_number': 'Q8U88', 'transaction_type': 2, 'duration': 1,
         'price_type': 1, 'trade_route': 'simulator', 'trade_exchange': TEST_EXCH, 'report_type': 'cancel',
         'orig_sequence_number': 'Q8U71',
         'cor_sequence_number': 'Q8U71', 'ssboe': 1696858070, 'usecs': 767370, 'notify_type': 3,
         'total_fill_size': 0, 'total_unfilled_size': 1, 'currency': 'USD',
         'original_basket_id': '1687449781', 'manual_or_auto': 2, 'orig_price_type': 1, 'bracket_type': 6,
         'order_id': None},
    ]
    order = sm._add_bracket_order('20231009_142748_bracket_order_one_leg_filled', TEST_SEC, TEST_EXCH, 1, True, 4323.5, 2, 1)
    simulate_exchange_updates_to_status_manager(sm, exchange_updates)
    assert order.fill_status == FillStatus.FILLED

    filled, side = order.child_side_filled
    assert filled is True
    assert side == ChildOrderType.STOP_LOSS
    assert order.all_stop_loss_orders_filled
    assert order.all_take_profit_orders_cancelled
    assert order.all_take_profit_orders_unfilled
