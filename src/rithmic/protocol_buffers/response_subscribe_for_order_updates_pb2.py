# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_subscribe_for_order_updates.proto

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
  name='response_subscribe_for_order_updates.proto',
  package='rti',
  serialized_pb=_b('\n*response_subscribe_for_order_updates.proto\x12\x03rti\"`\n ResponseSubscribeForOrderUpdates\x12\x15\n\x0btemplate_id\x18\xe3\xb6\t \x02(\x05\x12\x12\n\x08user_msg\x18\x98\x8d\x08 \x03(\t\x12\x11\n\x07rp_code\x18\x9e\x8d\x08 \x03(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RESPONSESUBSCRIBEFORORDERUPDATES = _descriptor.Descriptor(
  name='ResponseSubscribeForOrderUpdates',
  full_name='rti.ResponseSubscribeForOrderUpdates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='rti.ResponseSubscribeForOrderUpdates.template_id', index=0,
      number=154467, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_msg', full_name='rti.ResponseSubscribeForOrderUpdates.user_msg', index=1,
      number=132760, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rp_code', full_name='rti.ResponseSubscribeForOrderUpdates.rp_code', index=2,
      number=132766, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=147,
)

DESCRIPTOR.message_types_by_name['ResponseSubscribeForOrderUpdates'] = _RESPONSESUBSCRIBEFORORDERUPDATES

ResponseSubscribeForOrderUpdates = _reflection.GeneratedProtocolMessageType('ResponseSubscribeForOrderUpdates', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSESUBSCRIBEFORORDERUPDATES,
  __module__ = 'response_subscribe_for_order_updates_pb2'
  # @@protoc_insertion_point(class_scope:rti.ResponseSubscribeForOrderUpdates)
  ))
_sym_db.RegisterMessage(ResponseSubscribeForOrderUpdates)


# @@protoc_insertion_point(module_scope)
