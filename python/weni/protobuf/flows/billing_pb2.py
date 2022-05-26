# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weni/protobuf/flows/billing.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='weni/protobuf/flows/billing.proto',
  package='weni.flows.billing',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!weni/protobuf/flows/billing.proto\x12\x12weni.flows.billing\x1a\x1fgoogle/protobuf/timestamp.proto\"<\n\x0e\x42illingRequest\x12\x0b\n\x03org\x18\x01 \x01(\t\x12\x0e\n\x06\x62\x65\x66ore\x18\x02 \x01(\t\x12\r\n\x05\x61\x66ter\x18\x03 \x01(\t\"(\n\rTotalResponse\x12\x17\n\x0f\x61\x63tive_contacts\x18\x01 \x01(\x05\"\x80\x01\n\x03Msg\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12+\n\x07sent_on\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\tdirection\x18\x04 \x01(\x0e\x32\x1d.weni.flows.billing.Direction\"%\n\x07\x43hannel\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x85\x01\n\x13\x41\x63tiveContactDetail\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12$\n\x03msg\x18\x03 \x01(\x0b\x32\x17.weni.flows.billing.Msg\x12,\n\x07\x63hannel\x18\x04 \x01(\x0b\x32\x1b.weni.flows.billing.Channel\"_\n\x16IncomingMessageRequest\x12\x10\n\x08org_uuid\x18\x01 \x01(\t\x12\x14\n\x0c\x63ontact_uuid\x18\x02 \x01(\t\x12\x0e\n\x06\x62\x65\x66ore\x18\x03 \x01(\t\x12\r\n\x05\x61\x66ter\x18\x04 \x01(\t\"z\n\x0bIncomingMsg\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x12\n\ncreated_on\x18\x03 \x01(\t\x12\x11\n\tdirection\x18\x04 \x01(\t\x12\x12\n\nchannel_id\x18\x05 \x01(\x05\x12\x14\n\x0c\x63hannel_type\x18\x06 \x01(\t*\"\n\tDirection\x12\t\n\x05INPUT\x10\x00\x12\n\n\x06OUTPUT\x10\x01\x32\xa4\x02\n\x11\x42illingController\x12P\n\x05Total\x12\".weni.flows.billing.BillingRequest\x1a!.weni.flows.billing.TotalResponse\"\x00\x12[\n\x08\x44\x65tailed\x12\".weni.flows.billing.BillingRequest\x1a\'.weni.flows.billing.ActiveContactDetail\"\x00\x30\x01\x12`\n\x0fIncomingMessage\x12*.weni.flows.billing.IncomingMessageRequest\x1a\x1f.weni.flows.billing.IncomingMsg\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='weni.flows.billing.Direction',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INPUT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OUTPUT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=721,
  serialized_end=755,
)
_sym_db.RegisterEnumDescriptor(_DIRECTION)

Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
INPUT = 0
OUTPUT = 1



_BILLINGREQUEST = _descriptor.Descriptor(
  name='BillingRequest',
  full_name='weni.flows.billing.BillingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org', full_name='weni.flows.billing.BillingRequest.org', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='before', full_name='weni.flows.billing.BillingRequest.before', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='after', full_name='weni.flows.billing.BillingRequest.after', index=2,
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
  serialized_start=90,
  serialized_end=150,
)


_TOTALRESPONSE = _descriptor.Descriptor(
  name='TotalResponse',
  full_name='weni.flows.billing.TotalResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='active_contacts', full_name='weni.flows.billing.TotalResponse.active_contacts', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=152,
  serialized_end=192,
)


_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='weni.flows.billing.Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.flows.billing.Msg.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='weni.flows.billing.Msg.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sent_on', full_name='weni.flows.billing.Msg.sent_on', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='weni.flows.billing.Msg.direction', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=195,
  serialized_end=323,
)


_CHANNEL = _descriptor.Descriptor(
  name='Channel',
  full_name='weni.flows.billing.Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.flows.billing.Channel.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.flows.billing.Channel.name', index=1,
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
  serialized_start=325,
  serialized_end=362,
)


_ACTIVECONTACTDETAIL = _descriptor.Descriptor(
  name='ActiveContactDetail',
  full_name='weni.flows.billing.ActiveContactDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.flows.billing.ActiveContactDetail.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.flows.billing.ActiveContactDetail.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='weni.flows.billing.ActiveContactDetail.msg', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel', full_name='weni.flows.billing.ActiveContactDetail.channel', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=365,
  serialized_end=498,
)


_INCOMINGMESSAGEREQUEST = _descriptor.Descriptor(
  name='IncomingMessageRequest',
  full_name='weni.flows.billing.IncomingMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_uuid', full_name='weni.flows.billing.IncomingMessageRequest.org_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contact_uuid', full_name='weni.flows.billing.IncomingMessageRequest.contact_uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='before', full_name='weni.flows.billing.IncomingMessageRequest.before', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='after', full_name='weni.flows.billing.IncomingMessageRequest.after', index=3,
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
  serialized_start=500,
  serialized_end=595,
)


_INCOMINGMSG = _descriptor.Descriptor(
  name='IncomingMsg',
  full_name='weni.flows.billing.IncomingMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.flows.billing.IncomingMsg.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='weni.flows.billing.IncomingMsg.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_on', full_name='weni.flows.billing.IncomingMsg.created_on', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='weni.flows.billing.IncomingMsg.direction', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='weni.flows.billing.IncomingMsg.channel_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_type', full_name='weni.flows.billing.IncomingMsg.channel_type', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=597,
  serialized_end=719,
)

_MSG.fields_by_name['sent_on'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MSG.fields_by_name['direction'].enum_type = _DIRECTION
_ACTIVECONTACTDETAIL.fields_by_name['msg'].message_type = _MSG
_ACTIVECONTACTDETAIL.fields_by_name['channel'].message_type = _CHANNEL
DESCRIPTOR.message_types_by_name['BillingRequest'] = _BILLINGREQUEST
DESCRIPTOR.message_types_by_name['TotalResponse'] = _TOTALRESPONSE
DESCRIPTOR.message_types_by_name['Msg'] = _MSG
DESCRIPTOR.message_types_by_name['Channel'] = _CHANNEL
DESCRIPTOR.message_types_by_name['ActiveContactDetail'] = _ACTIVECONTACTDETAIL
DESCRIPTOR.message_types_by_name['IncomingMessageRequest'] = _INCOMINGMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['IncomingMsg'] = _INCOMINGMSG
DESCRIPTOR.enum_types_by_name['Direction'] = _DIRECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BillingRequest = _reflection.GeneratedProtocolMessageType('BillingRequest', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGREQUEST,
  '__module__' : 'weni.protobuf.flows.billing_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.billing.BillingRequest)
  })
_sym_db.RegisterMessage(BillingRequest)

TotalResponse = _reflection.GeneratedProtocolMessageType('TotalResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOTALRESPONSE,
  '__module__' : 'weni.protobuf.flows.billing_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.billing.TotalResponse)
  })
_sym_db.RegisterMessage(TotalResponse)

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), {
  'DESCRIPTOR' : _MSG,
  '__module__' : 'weni.protobuf.flows.billing_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.billing.Msg)
  })
_sym_db.RegisterMessage(Msg)

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), {
  'DESCRIPTOR' : _CHANNEL,
  '__module__' : 'weni.protobuf.flows.billing_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.billing.Channel)
  })
_sym_db.RegisterMessage(Channel)

ActiveContactDetail = _reflection.GeneratedProtocolMessageType('ActiveContactDetail', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVECONTACTDETAIL,
  '__module__' : 'weni.protobuf.flows.billing_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.billing.ActiveContactDetail)
  })
_sym_db.RegisterMessage(ActiveContactDetail)

IncomingMessageRequest = _reflection.GeneratedProtocolMessageType('IncomingMessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _INCOMINGMESSAGEREQUEST,
  '__module__' : 'weni.protobuf.flows.billing_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.billing.IncomingMessageRequest)
  })
_sym_db.RegisterMessage(IncomingMessageRequest)

IncomingMsg = _reflection.GeneratedProtocolMessageType('IncomingMsg', (_message.Message,), {
  'DESCRIPTOR' : _INCOMINGMSG,
  '__module__' : 'weni.protobuf.flows.billing_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.billing.IncomingMsg)
  })
_sym_db.RegisterMessage(IncomingMsg)



_BILLINGCONTROLLER = _descriptor.ServiceDescriptor(
  name='BillingController',
  full_name='weni.flows.billing.BillingController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=758,
  serialized_end=1050,
  methods=[
  _descriptor.MethodDescriptor(
    name='Total',
    full_name='weni.flows.billing.BillingController.Total',
    index=0,
    containing_service=None,
    input_type=_BILLINGREQUEST,
    output_type=_TOTALRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Detailed',
    full_name='weni.flows.billing.BillingController.Detailed',
    index=1,
    containing_service=None,
    input_type=_BILLINGREQUEST,
    output_type=_ACTIVECONTACTDETAIL,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='IncomingMessage',
    full_name='weni.flows.billing.BillingController.IncomingMessage',
    index=2,
    containing_service=None,
    input_type=_INCOMINGMESSAGEREQUEST,
    output_type=_INCOMINGMSG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BILLINGCONTROLLER)

DESCRIPTOR.services_by_name['BillingController'] = _BILLINGCONTROLLER

# @@protoc_insertion_point(module_scope)
