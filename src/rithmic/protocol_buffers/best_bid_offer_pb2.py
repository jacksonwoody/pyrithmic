# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: best_bid_offer.proto

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
  name='best_bid_offer.proto',
  package='rti',
  serialized_pb=_b('\n\x14\x62\x65st_bid_offer.proto\x12\x03rti\"\xdb\x03\n\x0c\x42\x65stBidOffer\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x10\n\x06symbol\x18\x94\xdc\x06 \x01(\t\x12\x12\n\x08\x65xchange\x18\x95\xdc\x06 \x01(\t\x12\x17\n\rpresence_bits\x18\x92\x8d\t \x01(\r\x12\x14\n\nclear_bits\x18\xcb\xb7\t \x01(\r\x12\x15\n\x0bis_snapshot\x18\xa9\xdc\x06 \x01(\x08\x12\x13\n\tbid_price\x18\xb6\x8d\x06 \x01(\x01\x12\x12\n\x08\x62id_size\x18\xbe\x8d\x06 \x01(\x05\x12\x14\n\nbid_orders\x18\xa3\xb6\t \x01(\x05\x12\x1b\n\x11\x62id_implicit_size\x18\xf3\xb9\t \x01(\x05\x12\x12\n\x08\x62id_time\x18\xaa\x8f\x06 \x01(\t\x12\x13\n\task_price\x18\xb9\x8d\x06 \x01(\x01\x12\x12\n\x08\x61sk_size\x18\xbf\x8d\x06 \x01(\x05\x12\x14\n\nask_orders\x18\xa4\xb6\t \x01(\x05\x12\x1b\n\x11\x61sk_implicit_size\x18\xf4\xb9\t \x01(\x05\x12\x12\n\x08\x61sk_time\x18\xab\x8f\x06 \x01(\t\x12\x14\n\nlean_price\x18\x9d\xba\t \x01(\x01\x12\x0f\n\x05ssboe\x18\xd4\x94\t \x01(\x05\x12\x0f\n\x05usecs\x18\xd5\x94\t \x01(\x05\"0\n\x0cPresenceBits\x12\x07\n\x03\x42ID\x10\x01\x12\x07\n\x03\x41SK\x10\x02\x12\x0e\n\nLEAN_PRICE\x10\x04')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_BESTBIDOFFER_PRESENCEBITS = _descriptor.EnumDescriptor(
  name='PresenceBits',
  full_name='rti.BestBidOffer.PresenceBits',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BID', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASK', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEAN_PRICE', index=2, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=457,
  serialized_end=505,
)
_sym_db.RegisterEnumDescriptor(_BESTBIDOFFER_PRESENCEBITS)


_BESTBIDOFFER = _descriptor.Descriptor(
  name='BestBidOffer',
  full_name='rti.BestBidOffer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.BestBidOffer.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='rti.BestBidOffer.symbol', index=1,
      number=110100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='rti.BestBidOffer.exchange', index=2,
      number=110101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='presence_bits', full_name='rti.BestBidOffer.presence_bits', index=3,
      number=149138, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clear_bits', full_name='rti.BestBidOffer.clear_bits', index=4,
      number=154571, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_snapshot', full_name='rti.BestBidOffer.is_snapshot', index=5,
      number=110121, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_price', full_name='rti.BestBidOffer.bid_price', index=6,
      number=100022, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_size', full_name='rti.BestBidOffer.bid_size', index=7,
      number=100030, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_orders', full_name='rti.BestBidOffer.bid_orders', index=8,
      number=154403, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_implicit_size', full_name='rti.BestBidOffer.bid_implicit_size', index=9,
      number=154867, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_time', full_name='rti.BestBidOffer.bid_time', index=10,
      number=100266, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask_price', full_name='rti.BestBidOffer.ask_price', index=11,
      number=100025, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask_size', full_name='rti.BestBidOffer.ask_size', index=12,
      number=100031, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask_orders', full_name='rti.BestBidOffer.ask_orders', index=13,
      number=154404, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask_implicit_size', full_name='rti.BestBidOffer.ask_implicit_size', index=14,
      number=154868, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask_time', full_name='rti.BestBidOffer.ask_time', index=15,
      number=100267, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lean_price', full_name='rti.BestBidOffer.lean_price', index=16,
      number=154909, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ssboe', full_name='rti.BestBidOffer.ssboe', index=17,
      number=150100, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='usecs', full_name='rti.BestBidOffer.usecs', index=18,
      number=150101, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BESTBIDOFFER_PRESENCEBITS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=505,
)

_BESTBIDOFFER_PRESENCEBITS.containing_type = _BESTBIDOFFER
DESCRIPTOR.message_types_by_name['BestBidOffer'] = _BESTBIDOFFER

BestBidOffer = _reflection.GeneratedProtocolMessageType('BestBidOffer', (_message.Message,), dict(
  DESCRIPTOR = _BESTBIDOFFER,
  __module__ = 'best_bid_offer_pb2'
  # @@protoc_insertion_point(class_scope:rti.BestBidOffer)
  ))
_sym_db.RegisterMessage(BestBidOffer)


# @@protoc_insertion_point(module_scope)
