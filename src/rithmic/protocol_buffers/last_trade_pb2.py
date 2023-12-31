# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: last_trade.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='last_trade.proto',
  package='rti',
  serialized_pb=_b('\n\x10last_trade.proto\x12\x03rti\"\xb0\x05\n\tLastTrade\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x10\n\x06symbol\x18\x94\xdc\x06 \x01(\t\x12\x12\n\x08\x65xchange\x18\x95\xdc\x06 \x01(\t\x12\x17\n\rpresence_bits\x18\x92\x8d\t \x01(\r\x12\x14\n\nclear_bits\x18\xcb\xb7\t \x01(\r\x12\x15\n\x0bis_snapshot\x18\xa9\xdc\x06 \x01(\x08\x12\x15\n\x0btrade_price\x18\xa6\x8d\x06 \x01(\x01\x12\x14\n\ntrade_size\x18\xd2\x8e\x06 \x01(\x05\x12\x33\n\taggressor\x18\x83\xeb\x06 \x01(\x0e\x32\x1e.rti.LastTrade.TransactionType\x12\x1b\n\x11\x65xchange_order_id\x18\xf6\x8d\t \x01(\t\x12%\n\x1b\x61ggressor_exchange_order_id\x18\x91\xb8\t \x01(\t\x12\x14\n\nnet_change\x18\xab\x8d\x06 \x01(\x01\x12\x18\n\x0epercent_change\x18\xd8\x8d\x06 \x01(\x01\x12\x10\n\x06volume\x18\xc0\x8d\x06 \x01(\x04\x12\x0e\n\x04vwap\x18\x83\x98\x06 \x01(\x01\x12\x14\n\ntrade_time\x18\x9b\x90\x06 \x01(\t\x12\x0f\n\x05ssboe\x18\xd4\x94\t \x01(\x05\x12\x0f\n\x05usecs\x18\xd5\x94\t \x01(\x05\x12\x16\n\x0csource_ssboe\x18\x80\x97\t \x01(\x05\x12\x16\n\x0csource_usecs\x18\x81\x97\t \x01(\x05\x12\x16\n\x0csource_nsecs\x18\x84\x97\t \x01(\x05\x12\x13\n\tjop_ssboe\x18\xc8\x98\t \x01(\x05\x12\x13\n\tjop_nsecs\x18\xcc\x98\t \x01(\x05\"X\n\x0cPresenceBits\x12\x0e\n\nLAST_TRADE\x10\x01\x12\x0e\n\nNET_CHANGE\x10\x02\x12\x12\n\x0ePRECENT_CHANGE\x10\x04\x12\n\n\x06VOLUME\x10\x08\x12\x08\n\x04VWAP\x10\x10\"$\n\x0fTransactionType\x12\x07\n\x03\x42UY\x10\x01\x12\x08\n\x04SELL\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_LASTTRADE_PRESENCEBITS = _descriptor.EnumDescriptor(
  name='PresenceBits',
  full_name='rti.LastTrade.PresenceBits',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LAST_TRADE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NET_CHANGE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRECENT_CHANGE', index=2, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUME', index=3, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VWAP', index=4, number=16,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=588,
  serialized_end=676,
)
_sym_db.RegisterEnumDescriptor(_LASTTRADE_PRESENCEBITS)

_LASTTRADE_TRANSACTIONTYPE = _descriptor.EnumDescriptor(
  name='TransactionType',
  full_name='rti.LastTrade.TransactionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUY', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SELL', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=678,
  serialized_end=714,
)
_sym_db.RegisterEnumDescriptor(_LASTTRADE_TRANSACTIONTYPE)


_LASTTRADE = _descriptor.Descriptor(
  name='LastTrade',
  full_name='rti.LastTrade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.LastTrade.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='rti.LastTrade.symbol', index=1,
      number=110100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='rti.LastTrade.exchange', index=2,
      number=110101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='presence_bits', full_name='rti.LastTrade.presence_bits', index=3,
      number=149138, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clear_bits', full_name='rti.LastTrade.clear_bits', index=4,
      number=154571, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_snapshot', full_name='rti.LastTrade.is_snapshot', index=5,
      number=110121, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trade_price', full_name='rti.LastTrade.trade_price', index=6,
      number=100006, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trade_size', full_name='rti.LastTrade.trade_size', index=7,
      number=100178, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aggressor', full_name='rti.LastTrade.aggressor', index=8,
      number=112003, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange_order_id', full_name='rti.LastTrade.exchange_order_id', index=9,
      number=149238, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aggressor_exchange_order_id', full_name='rti.LastTrade.aggressor_exchange_order_id', index=10,
      number=154641, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='net_change', full_name='rti.LastTrade.net_change', index=11,
      number=100011, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='percent_change', full_name='rti.LastTrade.percent_change', index=12,
      number=100056, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volume', full_name='rti.LastTrade.volume', index=13,
      number=100032, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vwap', full_name='rti.LastTrade.vwap', index=14,
      number=101379, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trade_time', full_name='rti.LastTrade.trade_time', index=15,
      number=100379, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ssboe', full_name='rti.LastTrade.ssboe', index=16,
      number=150100, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usecs', full_name='rti.LastTrade.usecs', index=17,
      number=150101, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_ssboe', full_name='rti.LastTrade.source_ssboe', index=18,
      number=150400, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_usecs', full_name='rti.LastTrade.source_usecs', index=19,
      number=150401, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_nsecs', full_name='rti.LastTrade.source_nsecs', index=20,
      number=150404, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jop_ssboe', full_name='rti.LastTrade.jop_ssboe', index=21,
      number=150600, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='jop_nsecs', full_name='rti.LastTrade.jop_nsecs', index=22,
      number=150604, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LASTTRADE_PRESENCEBITS,
    _LASTTRADE_TRANSACTIONTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=714,
)

_LASTTRADE.fields_by_name['aggressor'].enum_type = _LASTTRADE_TRANSACTIONTYPE
_LASTTRADE_PRESENCEBITS.containing_type = _LASTTRADE
_LASTTRADE_TRANSACTIONTYPE.containing_type = _LASTTRADE
DESCRIPTOR.message_types_by_name['LastTrade'] = _LASTTRADE

LastTrade = _reflection.GeneratedProtocolMessageType('LastTrade', (_message.Message,), dict(
  DESCRIPTOR = _LASTTRADE,
  __module__ = 'last_trade_pb2'
  # @@protoc_insertion_point(class_scope:rti.LastTrade)
  ))
_sym_db.RegisterMessage(LastTrade)


# @@protoc_insertion_point(module_scope)
