# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_time_bar_replay.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_time_bar_replay.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1eresponse_time_bar_replay.proto\x12\x03rti\"\xe1\x04\n\x15ResponseTimeBarReplay\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x15\n\x0brequest_key\x18\x96\x8d\x08 \x01(\t\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12\x1c\n\x12rq_handler_rp_code\x18\x9c\x8d\x08 \x03(\t\x12\x11\n\x07rp_code\x18\x9e\x8d\x08 \x03(\t\x12\x10\n\x06symbol\x18\x94\xdc\x06 \x01(\t\x12\x12\n\x08\x65xchange\x18\x95\xdc\x06 \x01(\t\x12\x32\n\x04type\x18\xa0\xa3\x07 \x01(\x0e\x32\".rti.ResponseTimeBarReplay.BarType\x12\x10\n\x06period\x18\xc8\xa2\x07 \x01(\t\x12\x10\n\x06marker\x18\xbc\xa2\x07 \x01(\x05\x12\x14\n\nnum_trades\x18\xc5\xa2\x07 \x01(\x04\x12\x10\n\x06volume\x18\xc6\xa2\x07 \x01(\x04\x12\x14\n\nbid_volume\x18\xcd\xa2\x07 \x01(\x04\x12\x14\n\nask_volume\x18\xce\xa2\x07 \x01(\x04\x12\x14\n\nopen_price\x18\xb3\x8d\x06 \x01(\x01\x12\x15\n\x0b\x63lose_price\x18\xb5\x8d\x06 \x01(\x01\x12\x14\n\nhigh_price\x18\xac\x8d\x06 \x01(\x01\x12\x13\n\tlow_price\x18\xad\x8d\x06 \x01(\x01\x12\x1a\n\x10settlement_price\x18\xe6\x8d\x06 \x01(\x01\x12\x1e\n\x14has_settlement_price\x18\x92\x8d\t \x01(\x08\x12%\n\x1bmust_clear_settlement_price\x18\xcb\xb7\t \x01(\x08\"H\n\x07\x42\x61rType\x12\x0e\n\nSECOND_BAR\x10\x01\x12\x0e\n\nMINUTE_BAR\x10\x02\x12\r\n\tDAILY_BAR\x10\x03\x12\x0e\n\nWEEKLY_BAR\x10\x04')
)



_RESPONSETIMEBARREPLAY_BARTYPE = _descriptor.EnumDescriptor(
  name='BarType',
  full_name='rti.ResponseTimeBarReplay.BarType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SECOND_BAR', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINUTE_BAR', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DAILY_BAR', index=2, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEEKLY_BAR', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=577,
  serialized_end=649,
)
_sym_db.RegisterEnumDescriptor(_RESPONSETIMEBARREPLAY_BARTYPE)


_RESPONSETIMEBARREPLAY = _descriptor.Descriptor(
  name='ResponseTimeBarReplay',
  full_name='rti.ResponseTimeBarReplay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.ResponseTimeBarReplay.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_key', full_name='rti.ResponseTimeBarReplay.request_key', index=1,
      number=132758, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.ResponseTimeBarReplay.user_msg', index=2,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rq_handler_rp_code', full_name='rti.ResponseTimeBarReplay.rq_handler_rp_code', index=3,
      number=132764, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rp_code', full_name='rti.ResponseTimeBarReplay.rp_code', index=4,
      number=132766, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='rti.ResponseTimeBarReplay.symbol', index=5,
      number=110100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='rti.ResponseTimeBarReplay.exchange', index=6,
      number=110101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='rti.ResponseTimeBarReplay.type', index=7,
      number=119200, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='rti.ResponseTimeBarReplay.period', index=8,
      number=119112, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='marker', full_name='rti.ResponseTimeBarReplay.marker', index=9,
      number=119100, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_trades', full_name='rti.ResponseTimeBarReplay.num_trades', index=10,
      number=119109, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='rti.ResponseTimeBarReplay.volume', index=11,
      number=119110, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bid_volume', full_name='rti.ResponseTimeBarReplay.bid_volume', index=12,
      number=119117, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ask_volume', full_name='rti.ResponseTimeBarReplay.ask_volume', index=13,
      number=119118, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open_price', full_name='rti.ResponseTimeBarReplay.open_price', index=14,
      number=100019, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_price', full_name='rti.ResponseTimeBarReplay.close_price', index=15,
      number=100021, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high_price', full_name='rti.ResponseTimeBarReplay.high_price', index=16,
      number=100012, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low_price', full_name='rti.ResponseTimeBarReplay.low_price', index=17,
      number=100013, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settlement_price', full_name='rti.ResponseTimeBarReplay.settlement_price', index=18,
      number=100070, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_settlement_price', full_name='rti.ResponseTimeBarReplay.has_settlement_price', index=19,
      number=149138, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='must_clear_settlement_price', full_name='rti.ResponseTimeBarReplay.must_clear_settlement_price', index=20,
      number=154571, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSETIMEBARREPLAY_BARTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=649,
)

_RESPONSETIMEBARREPLAY.fields_by_name['type'].enum_type = _RESPONSETIMEBARREPLAY_BARTYPE
_RESPONSETIMEBARREPLAY_BARTYPE.containing_type = _RESPONSETIMEBARREPLAY
DESCRIPTOR.message_types_by_name['ResponseTimeBarReplay'] = _RESPONSETIMEBARREPLAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseTimeBarReplay = _reflection.GeneratedProtocolMessageType('ResponseTimeBarReplay', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSETIMEBARREPLAY,
  __module__ = 'response_time_bar_replay_pb2'
  # @@protoc_insertion_point(class_scope:rti.ResponseTimeBarReplay)
  ))
_sym_db.RegisterMessage(ResponseTimeBarReplay)


# @@protoc_insertion_point(module_scope)
