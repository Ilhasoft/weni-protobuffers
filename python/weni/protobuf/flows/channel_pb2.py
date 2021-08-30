# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weni/protobuf/flows/channel.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='weni/protobuf/flows/channel.proto',
  package='weni.flows.channel',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!weni/protobuf/flows/channel.proto\x12\x12weni.flows.channel\"H\n\x18WeniWebChatCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x10\n\x08\x62\x61se_url\x18\x03 \x01(\t\"\x1b\n\x0bWeniWebChat\x12\x0c\n\x04name\x18\x01 \x01(\t2r\n\x15WeniWebChatController\x12Y\n\x06\x43reate\x12,.weni.flows.channel.WeniWebChatCreateRequest\x1a\x1f.weni.flows.channel.WeniWebChat\"\x00\x62\x06proto3'
)




_WENIWEBCHATCREATEREQUEST = _descriptor.Descriptor(
  name='WeniWebChatCreateRequest',
  full_name='weni.flows.channel.WeniWebChatCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.flows.channel.WeniWebChatCreateRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='weni.flows.channel.WeniWebChatCreateRequest.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_url', full_name='weni.flows.channel.WeniWebChatCreateRequest.base_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=129,
)


_WENIWEBCHAT = _descriptor.Descriptor(
  name='WeniWebChat',
  full_name='weni.flows.channel.WeniWebChat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.flows.channel.WeniWebChat.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=158,
)

DESCRIPTOR.message_types_by_name['WeniWebChatCreateRequest'] = _WENIWEBCHATCREATEREQUEST
DESCRIPTOR.message_types_by_name['WeniWebChat'] = _WENIWEBCHAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WeniWebChatCreateRequest = _reflection.GeneratedProtocolMessageType('WeniWebChatCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _WENIWEBCHATCREATEREQUEST,
  '__module__' : 'weni.protobuf.flows.channel_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.channel.WeniWebChatCreateRequest)
  })
_sym_db.RegisterMessage(WeniWebChatCreateRequest)

WeniWebChat = _reflection.GeneratedProtocolMessageType('WeniWebChat', (_message.Message,), {
  'DESCRIPTOR' : _WENIWEBCHAT,
  '__module__' : 'weni.protobuf.flows.channel_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.channel.WeniWebChat)
  })
_sym_db.RegisterMessage(WeniWebChat)



_WENIWEBCHATCONTROLLER = _descriptor.ServiceDescriptor(
  name='WeniWebChatController',
  full_name='weni.flows.channel.WeniWebChatController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=160,
  serialized_end=274,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='weni.flows.channel.WeniWebChatController.Create',
    index=0,
    containing_service=None,
    input_type=_WENIWEBCHATCREATEREQUEST,
    output_type=_WENIWEBCHAT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WENIWEBCHATCONTROLLER)

DESCRIPTOR.services_by_name['WeniWebChatController'] = _WENIWEBCHATCONTROLLER

# @@protoc_insertion_point(module_scope)
