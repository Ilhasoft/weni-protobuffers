# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weni/protobuf/inteligence/organization.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='weni/protobuf/inteligence/organization.proto',
  package='weni.bothub.org',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,weni/protobuf/inteligence/organization.proto\x12\x0fweni.bothub.org\x1a\x1bgoogle/protobuf/empty.proto\"F\n\x03Org\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x05users\x18\x03 \x03(\x0b\x32\x16.weni.bothub.org.Users\"f\n\x05Users\x12\x13\n\x0borg_user_id\x18\x01 \x01(\x05\x12\x16\n\x0eorg_user_email\x18\x02 \x01(\t\x12\x19\n\x11org_user_nickname\x18\x03 \x01(\t\x12\x15\n\rorg_user_name\x18\x04 \x01(\t\"$\n\x0eOrgListRequest\x12\x12\n\nuser_email\x18\x01 \x01(\t\"A\n\x10OrgCreateRequest\x12\x19\n\x11organization_name\x18\x01 \x01(\t\x12\x12\n\nuser_email\x18\x02 \x01(\t\"3\n\x11OrgDestroyRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nuser_email\x18\x02 \x01(\t\":\n\x10OrgUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\x04name\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"-\n\x1bOrgStatisticRetrieveRequest\x12\x0e\n\x06org_id\x18\x01 \x01(\x05\"*\n\x0cOrgStatistic\x12\x1a\n\x12repositories_count\x18\x01 \x01(\x05\x32\x8d\x03\n\rOrgController\x12\x41\n\x04List\x12\x1f.weni.bothub.org.OrgListRequest\x1a\x14.weni.bothub.org.Org\"\x00\x30\x01\x12\x43\n\x06\x43reate\x12!.weni.bothub.org.OrgCreateRequest\x1a\x14.weni.bothub.org.Org\"\x00\x12P\n\x06Update\x12!.weni.bothub.org.OrgUpdateRequest\x1a!.weni.bothub.org.OrgUpdateRequest\"\x00\x12G\n\x07\x44\x65stroy\x12\".weni.bothub.org.OrgDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12Y\n\x08Retrieve\x12,.weni.bothub.org.OrgStatisticRetrieveRequest\x1a\x1d.weni.bothub.org.OrgStatistic\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_ORG = _descriptor.Descriptor(
  name='Org',
  full_name='weni.bothub.org.Org',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='weni.bothub.org.Org.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.bothub.org.Org.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='users', full_name='weni.bothub.org.Org.users', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=94,
  serialized_end=164,
)


_USERS = _descriptor.Descriptor(
  name='Users',
  full_name='weni.bothub.org.Users',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_user_id', full_name='weni.bothub.org.Users.org_user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='org_user_email', full_name='weni.bothub.org.Users.org_user_email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='org_user_nickname', full_name='weni.bothub.org.Users.org_user_nickname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='org_user_name', full_name='weni.bothub.org.Users.org_user_name', index=3,
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
  serialized_start=166,
  serialized_end=268,
)


_ORGLISTREQUEST = _descriptor.Descriptor(
  name='OrgListRequest',
  full_name='weni.bothub.org.OrgListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_email', full_name='weni.bothub.org.OrgListRequest.user_email', index=0,
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
  serialized_start=270,
  serialized_end=306,
)


_ORGCREATEREQUEST = _descriptor.Descriptor(
  name='OrgCreateRequest',
  full_name='weni.bothub.org.OrgCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization_name', full_name='weni.bothub.org.OrgCreateRequest.organization_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='weni.bothub.org.OrgCreateRequest.user_email', index=1,
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
  serialized_start=308,
  serialized_end=373,
)


_ORGDESTROYREQUEST = _descriptor.Descriptor(
  name='OrgDestroyRequest',
  full_name='weni.bothub.org.OrgDestroyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='weni.bothub.org.OrgDestroyRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='weni.bothub.org.OrgDestroyRequest.user_email', index=1,
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
  serialized_start=375,
  serialized_end=426,
)


_ORGUPDATEREQUEST = _descriptor.Descriptor(
  name='OrgUpdateRequest',
  full_name='weni.bothub.org.OrgUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='weni.bothub.org.OrgUpdateRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.bothub.org.OrgUpdateRequest.name', index=1,
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
    _descriptor.OneofDescriptor(
      name='_name', full_name='weni.bothub.org.OrgUpdateRequest._name',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=428,
  serialized_end=486,
)


_ORGSTATISTICRETRIEVEREQUEST = _descriptor.Descriptor(
  name='OrgStatisticRetrieveRequest',
  full_name='weni.bothub.org.OrgStatisticRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_id', full_name='weni.bothub.org.OrgStatisticRetrieveRequest.org_id', index=0,
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
  serialized_start=488,
  serialized_end=533,
)


_ORGSTATISTIC = _descriptor.Descriptor(
  name='OrgStatistic',
  full_name='weni.bothub.org.OrgStatistic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='repositories_count', full_name='weni.bothub.org.OrgStatistic.repositories_count', index=0,
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
  serialized_start=535,
  serialized_end=577,
)

_ORG.fields_by_name['users'].message_type = _USERS
_ORGUPDATEREQUEST.oneofs_by_name['_name'].fields.append(
  _ORGUPDATEREQUEST.fields_by_name['name'])
_ORGUPDATEREQUEST.fields_by_name['name'].containing_oneof = _ORGUPDATEREQUEST.oneofs_by_name['_name']
DESCRIPTOR.message_types_by_name['Org'] = _ORG
DESCRIPTOR.message_types_by_name['Users'] = _USERS
DESCRIPTOR.message_types_by_name['OrgListRequest'] = _ORGLISTREQUEST
DESCRIPTOR.message_types_by_name['OrgCreateRequest'] = _ORGCREATEREQUEST
DESCRIPTOR.message_types_by_name['OrgDestroyRequest'] = _ORGDESTROYREQUEST
DESCRIPTOR.message_types_by_name['OrgUpdateRequest'] = _ORGUPDATEREQUEST
DESCRIPTOR.message_types_by_name['OrgStatisticRetrieveRequest'] = _ORGSTATISTICRETRIEVEREQUEST
DESCRIPTOR.message_types_by_name['OrgStatistic'] = _ORGSTATISTIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Org = _reflection.GeneratedProtocolMessageType('Org', (_message.Message,), {
  'DESCRIPTOR' : _ORG,
  '__module__' : 'weni.protobuf.inteligence.organization_pb2'
  # @@protoc_insertion_point(class_scope:weni.bothub.org.Org)
  })
_sym_db.RegisterMessage(Org)

Users = _reflection.GeneratedProtocolMessageType('Users', (_message.Message,), {
  'DESCRIPTOR' : _USERS,
  '__module__' : 'weni.protobuf.inteligence.organization_pb2'
  # @@protoc_insertion_point(class_scope:weni.bothub.org.Users)
  })
_sym_db.RegisterMessage(Users)

OrgListRequest = _reflection.GeneratedProtocolMessageType('OrgListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGLISTREQUEST,
  '__module__' : 'weni.protobuf.inteligence.organization_pb2'
  # @@protoc_insertion_point(class_scope:weni.bothub.org.OrgListRequest)
  })
_sym_db.RegisterMessage(OrgListRequest)

OrgCreateRequest = _reflection.GeneratedProtocolMessageType('OrgCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGCREATEREQUEST,
  '__module__' : 'weni.protobuf.inteligence.organization_pb2'
  # @@protoc_insertion_point(class_scope:weni.bothub.org.OrgCreateRequest)
  })
_sym_db.RegisterMessage(OrgCreateRequest)

OrgDestroyRequest = _reflection.GeneratedProtocolMessageType('OrgDestroyRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGDESTROYREQUEST,
  '__module__' : 'weni.protobuf.inteligence.organization_pb2'
  # @@protoc_insertion_point(class_scope:weni.bothub.org.OrgDestroyRequest)
  })
_sym_db.RegisterMessage(OrgDestroyRequest)

OrgUpdateRequest = _reflection.GeneratedProtocolMessageType('OrgUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGUPDATEREQUEST,
  '__module__' : 'weni.protobuf.inteligence.organization_pb2'
  # @@protoc_insertion_point(class_scope:weni.bothub.org.OrgUpdateRequest)
  })
_sym_db.RegisterMessage(OrgUpdateRequest)

OrgStatisticRetrieveRequest = _reflection.GeneratedProtocolMessageType('OrgStatisticRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGSTATISTICRETRIEVEREQUEST,
  '__module__' : 'weni.protobuf.inteligence.organization_pb2'
  # @@protoc_insertion_point(class_scope:weni.bothub.org.OrgStatisticRetrieveRequest)
  })
_sym_db.RegisterMessage(OrgStatisticRetrieveRequest)

OrgStatistic = _reflection.GeneratedProtocolMessageType('OrgStatistic', (_message.Message,), {
  'DESCRIPTOR' : _ORGSTATISTIC,
  '__module__' : 'weni.protobuf.inteligence.organization_pb2'
  # @@protoc_insertion_point(class_scope:weni.bothub.org.OrgStatistic)
  })
_sym_db.RegisterMessage(OrgStatistic)



_ORGCONTROLLER = _descriptor.ServiceDescriptor(
  name='OrgController',
  full_name='weni.bothub.org.OrgController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=580,
  serialized_end=977,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='weni.bothub.org.OrgController.List',
    index=0,
    containing_service=None,
    input_type=_ORGLISTREQUEST,
    output_type=_ORG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='weni.bothub.org.OrgController.Create',
    index=1,
    containing_service=None,
    input_type=_ORGCREATEREQUEST,
    output_type=_ORG,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='weni.bothub.org.OrgController.Update',
    index=2,
    containing_service=None,
    input_type=_ORGUPDATEREQUEST,
    output_type=_ORGUPDATEREQUEST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='weni.bothub.org.OrgController.Destroy',
    index=3,
    containing_service=None,
    input_type=_ORGDESTROYREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='weni.bothub.org.OrgController.Retrieve',
    index=4,
    containing_service=None,
    input_type=_ORGSTATISTICRETRIEVEREQUEST,
    output_type=_ORGSTATISTIC,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORGCONTROLLER)

DESCRIPTOR.services_by_name['OrgController'] = _ORGCONTROLLER

# @@protoc_insertion_point(module_scope)
