# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request_bracket_order.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='request_bracket_order.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1brequest_bracket_order.proto\x12\x03rti\"\xcd\x10\n\x13RequestBracketOrder\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12\x12\n\x08user_tag\x18\x87\xb4\t \x01(\t\x12\x10\n\x06\x66\x63m_id\x18\x9d\xb3\t \x01(\t\x12\x0f\n\x05ib_id\x18\x9e\xb3\t \x01(\t\x12\x14\n\naccount_id\x18\x98\xb3\t \x01(\t\x12\x10\n\x06symbol\x18\x94\xdc\x06 \x01(\t\x12\x12\n\x08\x65xchange\x18\x95\xdc\x06 \x01(\t\x12\x12\n\x08quantity\x18\x84\xeb\x06 \x01(\x05\x12\x0f\n\x05price\x18\xe2\xdd\x06 \x01(\x01\x12\x17\n\rtrigger_price\x18\xff\x8d\t \x01(\x01\x12\x44\n\x10transaction_type\x18\x83\xeb\x06 \x01(\x0e\x32(.rti.RequestBracketOrder.TransactionType\x12\x35\n\x08\x64uration\x18\x85\xeb\x06 \x01(\x0e\x32!.rti.RequestBracketOrder.Duration\x12\x38\n\nprice_type\x18\x88\xeb\x06 \x01(\x0e\x32\".rti.RequestBracketOrder.PriceType\x12\x15\n\x0btrade_route\x18\x90\xeb\x06 \x01(\t\x12\x41\n\x0emanual_or_auto\x18\xd6\xb8\t \x01(\x0e\x32\'.rti.RequestBracketOrder.OrderPlacement\x12\x36\n\tuser_type\x18\xb4\xb3\t \x01(\x0e\x32!.rti.RequestBracketOrder.UserType\x12<\n\x0c\x62racket_type\x18\x9f\xcb\t \x01(\x0e\x32$.rti.RequestBracketOrder.BracketType\x12\x1a\n\x10\x62reak_even_ticks\x18\xf2\xcb\t \x01(\x05\x12\"\n\x18\x62reak_even_trigger_ticks\x18\xf4\xcb\t \x01(\x05\x12\x19\n\x0ftarget_quantity\x18\xd9\xb6\t \x01(\x05\x12\x16\n\x0ctarget_ticks\x18\xd8\xb6\t \x01(\x05\x12\x17\n\rstop_quantity\x18\xdb\xb6\t \x01(\x05\x12\x14\n\nstop_ticks\x18\xda\xb6\t \x01(\x05\x12%\n\x1btrailing_stop_trigger_ticks\x18\xc4\xcb\t \x01(\x05\x12+\n!trailing_stop_by_last_trade_price\x18\x86\xcb\t \x01(\x08\x12(\n\x1etarget_market_order_if_touched\x18\xdf\xcb\t \x01(\x08\x12\x1f\n\x15stop_market_on_reject\x18\xe9\xb9\t \x01(\x08\x12 \n\x16target_market_at_ssboe\x18\xd9\xcb\t \x01(\x05\x12 \n\x16target_market_at_usecs\x18\xda\xcb\t \x01(\x05\x12\x1e\n\x14stop_market_at_ssboe\x18\xdb\xcb\t \x01(\x05\x12\x1e\n\x14stop_market_at_usecs\x18\xdc\xcb\t \x01(\x05\x12(\n\x1etarget_market_order_after_secs\x18\xdd\xcb\t \x01(\x05\x12\x19\n\x0f\x63\x61ncel_at_ssboe\x18\x9d\xcb\t \x01(\x05\x12\x19\n\x0f\x63\x61ncel_at_usecs\x18\x9e\xcb\t \x01(\x05\x12\x1b\n\x11\x63\x61ncel_after_secs\x18\xf8\xb6\t \x01(\x05\x12\x1b\n\x11if_touched_symbol\x18\xd3\xb6\t \x01(\t\x12\x1d\n\x13if_touched_exchange\x18\xd4\xb6\t \x01(\t\x12\x42\n\x14if_touched_condition\x18\xd5\xb6\t \x01(\x0e\x32\".rti.RequestBracketOrder.Condition\x12\x45\n\x16if_touched_price_field\x18\xd6\xb6\t \x01(\x0e\x32#.rti.RequestBracketOrder.PriceField\x12\x1a\n\x10if_touched_price\x18\xa0\xb0\t \x01(\x01\"Z\n\x08UserType\x12\x13\n\x0fUSER_TYPE_ADMIN\x10\x00\x12\x11\n\rUSER_TYPE_FCM\x10\x01\x12\x10\n\x0cUSER_TYPE_IB\x10\x02\x12\x14\n\x10USER_TYPE_TRADER\x10\x03\"\x8c\x01\n\x0b\x42racketType\x12\r\n\tSTOP_ONLY\x10\x01\x12\x0f\n\x0bTARGET_ONLY\x10\x02\x12\x13\n\x0fTARGET_AND_STOP\x10\x03\x12\x14\n\x10STOP_ONLY_STATIC\x10\x04\x12\x16\n\x12TARGET_ONLY_STATIC\x10\x05\x12\x1a\n\x16TARGET_AND_STOP_STATIC\x10\x06\"$\n\x0fTransactionType\x12\x07\n\x03\x42UY\x10\x01\x12\x08\n\x04SELL\x10\x02\".\n\x08\x44uration\x12\x07\n\x03\x44\x41Y\x10\x01\x12\x07\n\x03GTC\x10\x02\x12\x07\n\x03IOC\x10\x03\x12\x07\n\x03\x46OK\x10\x04\"p\n\tPriceType\x12\t\n\x05LIMIT\x10\x01\x12\n\n\x06MARKET\x10\x02\x12\x0e\n\nSTOP_LIMIT\x10\x03\x12\x0f\n\x0bSTOP_MARKET\x10\x04\x12\x15\n\x11MARKET_IF_TOUCHED\x10\x05\x12\x14\n\x10LIMIT_IF_TOUCHED\x10\x06\"&\n\x0eOrderPlacement\x12\n\n\x06MANUAL\x10\x01\x12\x08\n\x04\x41UTO\x10\x02\"M\n\nPriceField\x12\r\n\tBID_PRICE\x10\x01\x12\x0f\n\x0bOFFER_PRICE\x10\x02\x12\x0f\n\x0bTRADE_PRICE\x10\x03\x12\x0e\n\nLEAN_PRICE\x10\x04\"\x83\x01\n\tCondition\x12\x0c\n\x08\x45QUAL_TO\x10\x01\x12\x10\n\x0cNOT_EQUAL_TO\x10\x02\x12\x10\n\x0cGREATER_THAN\x10\x03\x12\x19\n\x15GREATER_THAN_EQUAL_TO\x10\x04\x12\x0f\n\x0bLESSER_THAN\x10\x05\x12\x18\n\x14LESSER_THAN_EQUAL_TO\x10\x06')
)



_REQUESTBRACKETORDER_USERTYPE = _descriptor.EnumDescriptor(
  name='UserType',
  full_name='rti.RequestBracketOrder.UserType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER_TYPE_ADMIN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_TYPE_FCM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_TYPE_IB', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_TYPE_TRADER', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1476,
  serialized_end=1566,
)
_sym_db.RegisterEnumDescriptor(_REQUESTBRACKETORDER_USERTYPE)

_REQUESTBRACKETORDER_BRACKETTYPE = _descriptor.EnumDescriptor(
  name='BracketType',
  full_name='rti.RequestBracketOrder.BracketType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STOP_ONLY', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_ONLY', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_AND_STOP', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP_ONLY_STATIC', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_ONLY_STATIC', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_AND_STOP_STATIC', index=5, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1569,
  serialized_end=1709,
)
_sym_db.RegisterEnumDescriptor(_REQUESTBRACKETORDER_BRACKETTYPE)

_REQUESTBRACKETORDER_TRANSACTIONTYPE = _descriptor.EnumDescriptor(
  name='TransactionType',
  full_name='rti.RequestBracketOrder.TransactionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUY', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SELL', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1711,
  serialized_end=1747,
)
_sym_db.RegisterEnumDescriptor(_REQUESTBRACKETORDER_TRANSACTIONTYPE)

_REQUESTBRACKETORDER_DURATION = _descriptor.EnumDescriptor(
  name='Duration',
  full_name='rti.RequestBracketOrder.Duration',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DAY', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GTC', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IOC', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOK', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1749,
  serialized_end=1795,
)
_sym_db.RegisterEnumDescriptor(_REQUESTBRACKETORDER_DURATION)

_REQUESTBRACKETORDER_PRICETYPE = _descriptor.EnumDescriptor(
  name='PriceType',
  full_name='rti.RequestBracketOrder.PriceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LIMIT', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARKET', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP_LIMIT', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STOP_MARKET', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARKET_IF_TOUCHED', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIMIT_IF_TOUCHED', index=5, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1797,
  serialized_end=1909,
)
_sym_db.RegisterEnumDescriptor(_REQUESTBRACKETORDER_PRICETYPE)

_REQUESTBRACKETORDER_ORDERPLACEMENT = _descriptor.EnumDescriptor(
  name='OrderPlacement',
  full_name='rti.RequestBracketOrder.OrderPlacement',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MANUAL', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTO', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1911,
  serialized_end=1949,
)
_sym_db.RegisterEnumDescriptor(_REQUESTBRACKETORDER_ORDERPLACEMENT)

_REQUESTBRACKETORDER_PRICEFIELD = _descriptor.EnumDescriptor(
  name='PriceField',
  full_name='rti.RequestBracketOrder.PriceField',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BID_PRICE', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFFER_PRICE', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRADE_PRICE', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEAN_PRICE', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1951,
  serialized_end=2028,
)
_sym_db.RegisterEnumDescriptor(_REQUESTBRACKETORDER_PRICEFIELD)

_REQUESTBRACKETORDER_CONDITION = _descriptor.EnumDescriptor(
  name='Condition',
  full_name='rti.RequestBracketOrder.Condition',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EQUAL_TO', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_EQUAL_TO', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREATER_THAN', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GREATER_THAN_EQUAL_TO', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LESSER_THAN', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LESSER_THAN_EQUAL_TO', index=5, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2031,
  serialized_end=2162,
)
_sym_db.RegisterEnumDescriptor(_REQUESTBRACKETORDER_CONDITION)


_REQUESTBRACKETORDER = _descriptor.Descriptor(
  name='RequestBracketOrder',
  full_name='rti.RequestBracketOrder',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.RequestBracketOrder.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.RequestBracketOrder.user_msg', index=1,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_tag', full_name='rti.RequestBracketOrder.user_tag', index=2,
      number=154119, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fcm_id', full_name='rti.RequestBracketOrder.fcm_id', index=3,
      number=154013, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ib_id', full_name='rti.RequestBracketOrder.ib_id', index=4,
      number=154014, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='rti.RequestBracketOrder.account_id', index=5,
      number=154008, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='rti.RequestBracketOrder.symbol', index=6,
      number=110100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='rti.RequestBracketOrder.exchange', index=7,
      number=110101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='rti.RequestBracketOrder.quantity', index=8,
      number=112004, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='rti.RequestBracketOrder.price', index=9,
      number=110306, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trigger_price', full_name='rti.RequestBracketOrder.trigger_price', index=10,
      number=149247, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_type', full_name='rti.RequestBracketOrder.transaction_type', index=11,
      number=112003, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='rti.RequestBracketOrder.duration', index=12,
      number=112005, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_type', full_name='rti.RequestBracketOrder.price_type', index=13,
      number=112008, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trade_route', full_name='rti.RequestBracketOrder.trade_route', index=14,
      number=112016, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manual_or_auto', full_name='rti.RequestBracketOrder.manual_or_auto', index=15,
      number=154710, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_type', full_name='rti.RequestBracketOrder.user_type', index=16,
      number=154036, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bracket_type', full_name='rti.RequestBracketOrder.bracket_type', index=17,
      number=157087, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='break_even_ticks', full_name='rti.RequestBracketOrder.break_even_ticks', index=18,
      number=157170, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='break_even_trigger_ticks', full_name='rti.RequestBracketOrder.break_even_trigger_ticks', index=19,
      number=157172, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_quantity', full_name='rti.RequestBracketOrder.target_quantity', index=20,
      number=154457, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_ticks', full_name='rti.RequestBracketOrder.target_ticks', index=21,
      number=154456, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_quantity', full_name='rti.RequestBracketOrder.stop_quantity', index=22,
      number=154459, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_ticks', full_name='rti.RequestBracketOrder.stop_ticks', index=23,
      number=154458, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trailing_stop_trigger_ticks', full_name='rti.RequestBracketOrder.trailing_stop_trigger_ticks', index=24,
      number=157124, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trailing_stop_by_last_trade_price', full_name='rti.RequestBracketOrder.trailing_stop_by_last_trade_price', index=25,
      number=157062, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_market_order_if_touched', full_name='rti.RequestBracketOrder.target_market_order_if_touched', index=26,
      number=157151, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_market_on_reject', full_name='rti.RequestBracketOrder.stop_market_on_reject', index=27,
      number=154857, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_market_at_ssboe', full_name='rti.RequestBracketOrder.target_market_at_ssboe', index=28,
      number=157145, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_market_at_usecs', full_name='rti.RequestBracketOrder.target_market_at_usecs', index=29,
      number=157146, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_market_at_ssboe', full_name='rti.RequestBracketOrder.stop_market_at_ssboe', index=30,
      number=157147, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop_market_at_usecs', full_name='rti.RequestBracketOrder.stop_market_at_usecs', index=31,
      number=157148, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_market_order_after_secs', full_name='rti.RequestBracketOrder.target_market_order_after_secs', index=32,
      number=157149, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cancel_at_ssboe', full_name='rti.RequestBracketOrder.cancel_at_ssboe', index=33,
      number=157085, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cancel_at_usecs', full_name='rti.RequestBracketOrder.cancel_at_usecs', index=34,
      number=157086, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cancel_after_secs', full_name='rti.RequestBracketOrder.cancel_after_secs', index=35,
      number=154488, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='if_touched_symbol', full_name='rti.RequestBracketOrder.if_touched_symbol', index=36,
      number=154451, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='if_touched_exchange', full_name='rti.RequestBracketOrder.if_touched_exchange', index=37,
      number=154452, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='if_touched_condition', full_name='rti.RequestBracketOrder.if_touched_condition', index=38,
      number=154453, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='if_touched_price_field', full_name='rti.RequestBracketOrder.if_touched_price_field', index=39,
      number=154454, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='if_touched_price', full_name='rti.RequestBracketOrder.if_touched_price', index=40,
      number=153632, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTBRACKETORDER_USERTYPE,
    _REQUESTBRACKETORDER_BRACKETTYPE,
    _REQUESTBRACKETORDER_TRANSACTIONTYPE,
    _REQUESTBRACKETORDER_DURATION,
    _REQUESTBRACKETORDER_PRICETYPE,
    _REQUESTBRACKETORDER_ORDERPLACEMENT,
    _REQUESTBRACKETORDER_PRICEFIELD,
    _REQUESTBRACKETORDER_CONDITION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=2162,
)

_REQUESTBRACKETORDER.fields_by_name['transaction_type'].enum_type = _REQUESTBRACKETORDER_TRANSACTIONTYPE
_REQUESTBRACKETORDER.fields_by_name['duration'].enum_type = _REQUESTBRACKETORDER_DURATION
_REQUESTBRACKETORDER.fields_by_name['price_type'].enum_type = _REQUESTBRACKETORDER_PRICETYPE
_REQUESTBRACKETORDER.fields_by_name['manual_or_auto'].enum_type = _REQUESTBRACKETORDER_ORDERPLACEMENT
_REQUESTBRACKETORDER.fields_by_name['user_type'].enum_type = _REQUESTBRACKETORDER_USERTYPE
_REQUESTBRACKETORDER.fields_by_name['bracket_type'].enum_type = _REQUESTBRACKETORDER_BRACKETTYPE
_REQUESTBRACKETORDER.fields_by_name['if_touched_condition'].enum_type = _REQUESTBRACKETORDER_CONDITION
_REQUESTBRACKETORDER.fields_by_name['if_touched_price_field'].enum_type = _REQUESTBRACKETORDER_PRICEFIELD
_REQUESTBRACKETORDER_USERTYPE.containing_type = _REQUESTBRACKETORDER
_REQUESTBRACKETORDER_BRACKETTYPE.containing_type = _REQUESTBRACKETORDER
_REQUESTBRACKETORDER_TRANSACTIONTYPE.containing_type = _REQUESTBRACKETORDER
_REQUESTBRACKETORDER_DURATION.containing_type = _REQUESTBRACKETORDER
_REQUESTBRACKETORDER_PRICETYPE.containing_type = _REQUESTBRACKETORDER
_REQUESTBRACKETORDER_ORDERPLACEMENT.containing_type = _REQUESTBRACKETORDER
_REQUESTBRACKETORDER_PRICEFIELD.containing_type = _REQUESTBRACKETORDER
_REQUESTBRACKETORDER_CONDITION.containing_type = _REQUESTBRACKETORDER
DESCRIPTOR.message_types_by_name['RequestBracketOrder'] = _REQUESTBRACKETORDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestBracketOrder = _reflection.GeneratedProtocolMessageType('RequestBracketOrder', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTBRACKETORDER,
  __module__ = 'request_bracket_order_pb2'
  # @@protoc_insertion_point(class_scope:rti.RequestBracketOrder)
  ))
_sym_db.RegisterMessage(RequestBracketOrder)


# @@protoc_insertion_point(module_scope)
