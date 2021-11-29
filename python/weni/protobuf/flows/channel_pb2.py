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


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='weni/protobuf/flows/channel.proto',
  package='weni.flows.channel',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!weni/protobuf/flows/channel.proto\x12\x12weni.flows.channel\x1a\x1bgoogle/protobuf/empty.proto\"Y\n\x14\x43hannelCreateRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0b\n\x03org\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\x12\x18\n\x10\x63hanneltype_code\x18\x04 \x01(\t\"&\n\x16\x43hannelRetrieveRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"7\n\x12\x43hannelListRequest\x12\x0b\n\x03org\x18\x01 \x01(\t\x12\x14\n\x0c\x63hannel_type\x18\x02 \x01(\t\"F\n\x07\x43hannel\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\"3\n\x15\x43hannelDestroyRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"U\n\x18WeniWebChatCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x10\n\x08\x62\x61se_url\x18\x03 \x01(\t\x12\x0b\n\x03org\x18\x04 \x01(\t\"\x1b\n\x0bWeniWebChat\x12\x0c\n\x04uuid\x18\x01 \x01(\t2\xd8\x02\n\x11\x43hannelController\x12O\n\x06\x43reate\x12(.weni.flows.channel.ChannelCreateRequest\x1a\x1b.weni.flows.channel.Channel\x12S\n\x08Retrieve\x12*.weni.flows.channel.ChannelRetrieveRequest\x1a\x1b.weni.flows.channel.Channel\x12M\n\x04List\x12&.weni.flows.channel.ChannelListRequest\x1a\x1b.weni.flows.channel.Channel0\x01\x12N\n\x07\x44\x65stroy\x12).weni.flows.channel.ChannelDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x32r\n\x15WeniWebChatController\x12Y\n\x06\x43reate\x12,.weni.flows.channel.WeniWebChatCreateRequest\x1a\x1f.weni.flows.channel.WeniWebChat\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_CHANNELCREATEREQUEST = _descriptor.Descriptor(
  name='ChannelCreateRequest',
  full_name='weni.flows.channel.ChannelCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='weni.flows.channel.ChannelCreateRequest.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='org', full_name='weni.flows.channel.ChannelCreateRequest.org', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='weni.flows.channel.ChannelCreateRequest.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channeltype_code', full_name='weni.flows.channel.ChannelCreateRequest.channeltype_code', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=86,
  serialized_end=175,
)


_CHANNELRETRIEVEREQUEST = _descriptor.Descriptor(
  name='ChannelRetrieveRequest',
  full_name='weni.flows.channel.ChannelRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.flows.channel.ChannelRetrieveRequest.uuid', index=0,
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
  serialized_start=177,
  serialized_end=215,
)


_CHANNELLISTREQUEST = _descriptor.Descriptor(
  name='ChannelListRequest',
  full_name='weni.flows.channel.ChannelListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org', full_name='weni.flows.channel.ChannelListRequest.org', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_type', full_name='weni.flows.channel.ChannelListRequest.channel_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=217,
  serialized_end=272,
)


_CHANNEL = _descriptor.Descriptor(
  name='Channel',
  full_name='weni.flows.channel.Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.flows.channel.Channel.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.flows.channel.Channel.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='weni.flows.channel.Channel.config', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='weni.flows.channel.Channel.address', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=274,
  serialized_end=344,
)


_CHANNELDESTROYREQUEST = _descriptor.Descriptor(
  name='ChannelDestroyRequest',
  full_name='weni.flows.channel.ChannelDestroyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='weni.flows.channel.ChannelDestroyRequest.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.flows.channel.ChannelDestroyRequest.uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=346,
  serialized_end=397,
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
    _descriptor.FieldDescriptor(
      name='org', full_name='weni.flows.channel.WeniWebChatCreateRequest.org', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=399,
  serialized_end=484,
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
      name='uuid', full_name='weni.flows.channel.WeniWebChat.uuid', index=0,
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
  serialized_start=486,
  serialized_end=513,
)

DESCRIPTOR.message_types_by_name['ChannelCreateRequest'] = _CHANNELCREATEREQUEST
DESCRIPTOR.message_types_by_name['ChannelRetrieveRequest'] = _CHANNELRETRIEVEREQUEST
DESCRIPTOR.message_types_by_name['ChannelListRequest'] = _CHANNELLISTREQUEST
DESCRIPTOR.message_types_by_name['Channel'] = _CHANNEL
DESCRIPTOR.message_types_by_name['ChannelDestroyRequest'] = _CHANNELDESTROYREQUEST
DESCRIPTOR.message_types_by_name['WeniWebChatCreateRequest'] = _WENIWEBCHATCREATEREQUEST
DESCRIPTOR.message_types_by_name['WeniWebChat'] = _WENIWEBCHAT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChannelCreateRequest = _reflection.GeneratedProtocolMessageType('ChannelCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELCREATEREQUEST,
  '__module__' : 'weni.protobuf.flows.channel_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.channel.ChannelCreateRequest)
  })
_sym_db.RegisterMessage(ChannelCreateRequest)

ChannelRetrieveRequest = _reflection.GeneratedProtocolMessageType('ChannelRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELRETRIEVEREQUEST,
  '__module__' : 'weni.protobuf.flows.channel_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.channel.ChannelRetrieveRequest)
  })
_sym_db.RegisterMessage(ChannelRetrieveRequest)

ChannelListRequest = _reflection.GeneratedProtocolMessageType('ChannelListRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELLISTREQUEST,
  '__module__' : 'weni.protobuf.flows.channel_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.channel.ChannelListRequest)
  })
_sym_db.RegisterMessage(ChannelListRequest)

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), {
  'DESCRIPTOR' : _CHANNEL,
  '__module__' : 'weni.protobuf.flows.channel_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.channel.Channel)
  })
_sym_db.RegisterMessage(Channel)

ChannelDestroyRequest = _reflection.GeneratedProtocolMessageType('ChannelDestroyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELDESTROYREQUEST,
  '__module__' : 'weni.protobuf.flows.channel_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.channel.ChannelDestroyRequest)
  })
_sym_db.RegisterMessage(ChannelDestroyRequest)

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



_CHANNELCONTROLLER = _descriptor.ServiceDescriptor(
  name='ChannelController',
  full_name='weni.flows.channel.ChannelController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=516,
  serialized_end=860,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='weni.flows.channel.ChannelController.Create',
    index=0,
    containing_service=None,
    input_type=_CHANNELCREATEREQUEST,
    output_type=_CHANNEL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='weni.flows.channel.ChannelController.Retrieve',
    index=1,
    containing_service=None,
    input_type=_CHANNELRETRIEVEREQUEST,
    output_type=_CHANNEL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='weni.flows.channel.ChannelController.List',
    index=2,
    containing_service=None,
    input_type=_CHANNELLISTREQUEST,
    output_type=_CHANNEL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='weni.flows.channel.ChannelController.Destroy',
    index=3,
    containing_service=None,
    input_type=_CHANNELDESTROYREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHANNELCONTROLLER)

DESCRIPTOR.services_by_name['ChannelController'] = _CHANNELCONTROLLER


_WENIWEBCHATCONTROLLER = _descriptor.ServiceDescriptor(
  name='WeniWebChatController',
  full_name='weni.flows.channel.WeniWebChatController',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=862,
  serialized_end=976,
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
