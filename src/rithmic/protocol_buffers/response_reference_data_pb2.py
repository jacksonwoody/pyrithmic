# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_reference_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_reference_data.proto',
  package='rti',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1dresponse_reference_data.proto\x12\x03rti\"\xa2\t\n\x15ResponseReferenceData\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12\x11\n\x07rp_code\x18\x9e\x8d\x08 \x03(\t\x12\x17\n\rpresence_bits\x18\x92\x8d\t \x01(\r\x12\x14\n\nclear_bits\x18\xcb\xb7\t \x01(\r\x12\x10\n\x06symbol\x18\x94\xdc\x06 \x01(\t\x12\x12\n\x08\x65xchange\x18\x95\xdc\x06 \x01(\t\x12\x19\n\x0f\x65xchange_symbol\x18\xa2\xdc\x06 \x01(\t\x12\x15\n\x0bsymbol_name\x18\xa3\x8d\x06 \x01(\t\x12\x18\n\x0etrading_symbol\x18\xa7\xcb\t \x01(\t\x12\x1a\n\x10trading_exchange\x18\xa8\xcb\t \x01(\t\x12\x16\n\x0cproduct_code\x18\x8d\x93\x06 \x01(\t\x12\x19\n\x0finstrument_type\x18\xa4\xdc\x06 \x01(\t\x12\x1b\n\x11underlying_symbol\x18\xa2\x95\x06 \x01(\t\x12\x19\n\x0f\x65xpiration_date\x18\xe3\x8d\x06 \x01(\t\x12\x12\n\x08\x63urrency\x18\x8e\xb6\t \x01(\t\x12\x1c\n\x12put_call_indicator\x18\x8d\x8e\x06 \x01(\t\x12\x18\n\x0etick_size_type\x18\xb7\xb4\t \x01(\t\x12\x1e\n\x14price_display_format\x18\x96\xb6\t \x01(\t\x12\x15\n\x0bis_tradable\x18\xdc\xb9\t \x01(\t\x12+\n!is_underlying_for_binary_contrats\x18\xc8\xba\t \x01(\t\x12\x16\n\x0cstrike_price\x18\xe2\x8d\x06 \x01(\x01\x12\x14\n\nftoq_price\x18\x90\xb6\t \x01(\x01\x12\x14\n\nqtof_price\x18\x91\xb6\t \x01(\x01\x12\x1b\n\x11min_qprice_change\x18\x92\xb6\t \x01(\x01\x12\x1b\n\x11min_fprice_change\x18\x93\xb6\t \x01(\x01\x12\x1c\n\x12single_point_value\x18\x95\xb6\t \x01(\x01\"\xd6\x03\n\x0cPresenceBits\x12\x13\n\x0f\x45XCHANGE_SYMBOL\x10\x01\x12\x0f\n\x0bSYMBOL_NAME\x10\x02\x12\x10\n\x0cPRODUCT_CODE\x10\x04\x12\x13\n\x0fINSTRUMENT_TYPE\x10\x08\x12\x15\n\x11UNDERLYING_SYMBOL\x10\x10\x12\x13\n\x0f\x45XPIRATION_DATE\x10 \x12\x0c\n\x08\x43URRENCY\x10@\x12\x17\n\x12PUT_CALL_INDICATOR\x10\x80\x01\x12\x11\n\x0cSTRIKE_PRICE\x10\x80\x02\x12\x15\n\x10\x46PRICE_TO_QPRICE\x10\x80\x04\x12\x15\n\x10QPRICE_TO_FPRICE\x10\x80\x08\x12\x16\n\x11MIN_QPRICE_CHANGE\x10\x80\x10\x12\x16\n\x11MIN_FRPICE_CHANGE\x10\x80 \x12\x17\n\x12SINGLE_POINT_VALUE\x10\x80@\x12\x14\n\x0eTICK_SIZE_TYPE\x10\x80\x80\x01\x12\x1a\n\x14PRICE_DISPLAY_FORMAT\x10\x80\x80\x02\x12\x11\n\x0bIS_TRADABLE\x10\x80\x80\x04\x12\x14\n\x0eTRADING_SYMBOL\x10\x80\x80\x08\x12\x16\n\x10TRADING_EXCHANGE\x10\x80\x80\x10\x12)\n\"IS_UNDERLYING_FOR_BINARY_CONTRACTS\x10\x80\x80\x80\x04')
)



_RESPONSEREFERENCEDATA_PRESENCEBITS = _descriptor.EnumDescriptor(
  name='PresenceBits',
  full_name='rti.ResponseReferenceData.PresenceBits',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXCHANGE_SYMBOL', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYMBOL_NAME', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_CODE', index=2, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTRUMENT_TYPE', index=3, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDERLYING_SYMBOL', index=4, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPIRATION_DATE', index=5, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CURRENCY', index=6, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUT_CALL_INDICATOR', index=7, number=128,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRIKE_PRICE', index=8, number=256,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FPRICE_TO_QPRICE', index=9, number=512,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QPRICE_TO_FPRICE', index=10, number=1024,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIN_QPRICE_CHANGE', index=11, number=2048,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIN_FRPICE_CHANGE', index=12, number=4096,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SINGLE_POINT_VALUE', index=13, number=8192,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TICK_SIZE_TYPE', index=14, number=16384,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE_DISPLAY_FORMAT', index=15, number=32768,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_TRADABLE', index=16, number=65536,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRADING_SYMBOL', index=17, number=131072,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRADING_EXCHANGE', index=18, number=262144,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_UNDERLYING_FOR_BINARY_CONTRACTS', index=19, number=8388608,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=755,
  serialized_end=1225,
)
_sym_db.RegisterEnumDescriptor(_RESPONSEREFERENCEDATA_PRESENCEBITS)


_RESPONSEREFERENCEDATA = _descriptor.Descriptor(
  name='ResponseReferenceData',
  full_name='rti.ResponseReferenceData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.ResponseReferenceData.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.ResponseReferenceData.user_msg', index=1,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rp_code', full_name='rti.ResponseReferenceData.rp_code', index=2,
      number=132766, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='presence_bits', full_name='rti.ResponseReferenceData.presence_bits', index=3,
      number=149138, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clear_bits', full_name='rti.ResponseReferenceData.clear_bits', index=4,
      number=154571, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='rti.ResponseReferenceData.symbol', index=5,
      number=110100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='rti.ResponseReferenceData.exchange', index=6,
      number=110101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange_symbol', full_name='rti.ResponseReferenceData.exchange_symbol', index=7,
      number=110114, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol_name', full_name='rti.ResponseReferenceData.symbol_name', index=8,
      number=100003, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trading_symbol', full_name='rti.ResponseReferenceData.trading_symbol', index=9,
      number=157095, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trading_exchange', full_name='rti.ResponseReferenceData.trading_exchange', index=10,
      number=157096, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product_code', full_name='rti.ResponseReferenceData.product_code', index=11,
      number=100749, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instrument_type', full_name='rti.ResponseReferenceData.instrument_type', index=12,
      number=110116, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='underlying_symbol', full_name='rti.ResponseReferenceData.underlying_symbol', index=13,
      number=101026, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration_date', full_name='rti.ResponseReferenceData.expiration_date', index=14,
      number=100067, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency', full_name='rti.ResponseReferenceData.currency', index=15,
      number=154382, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='put_call_indicator', full_name='rti.ResponseReferenceData.put_call_indicator', index=16,
      number=100109, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tick_size_type', full_name='rti.ResponseReferenceData.tick_size_type', index=17,
      number=154167, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_display_format', full_name='rti.ResponseReferenceData.price_display_format', index=18,
      number=154390, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_tradable', full_name='rti.ResponseReferenceData.is_tradable', index=19,
      number=154844, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_underlying_for_binary_contrats', full_name='rti.ResponseReferenceData.is_underlying_for_binary_contrats', index=20,
      number=154952, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strike_price', full_name='rti.ResponseReferenceData.strike_price', index=21,
      number=100066, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ftoq_price', full_name='rti.ResponseReferenceData.ftoq_price', index=22,
      number=154384, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qtof_price', full_name='rti.ResponseReferenceData.qtof_price', index=23,
      number=154385, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_qprice_change', full_name='rti.ResponseReferenceData.min_qprice_change', index=24,
      number=154386, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_fprice_change', full_name='rti.ResponseReferenceData.min_fprice_change', index=25,
      number=154387, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='single_point_value', full_name='rti.ResponseReferenceData.single_point_value', index=26,
      number=154389, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSEREFERENCEDATA_PRESENCEBITS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=1225,
)

_RESPONSEREFERENCEDATA_PRESENCEBITS.containing_type = _RESPONSEREFERENCEDATA
DESCRIPTOR.message_types_by_name['ResponseReferenceData'] = _RESPONSEREFERENCEDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseReferenceData = _reflection.GeneratedProtocolMessageType('ResponseReferenceData', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEREFERENCEDATA,
  __module__ = 'response_reference_data_pb2'
  # @@protoc_insertion_point(class_scope:rti.ResponseReferenceData)
  ))
_sym_db.RegisterMessage(ResponseReferenceData)


# @@protoc_insertion_point(module_scope)
