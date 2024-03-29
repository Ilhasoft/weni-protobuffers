# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weni/protobuf/connect/organization.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='weni/protobuf/connect/organization.proto',
  package='weni.connect.project',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(weni/protobuf/connect/organization.proto\x12\x14weni.connect.project\"\x9a\x01\n\x14OrganizationResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12 \n\x18inteligence_organization\x18\x04 \x01(\x05\x12\x19\n\x11\x65xtra_integration\x18\x05 \x01(\x05\x12\x14\n\x0cis_suspended\x18\x06 \x01(\x08\"\'\n\x17OrganizationListRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"+\n\x1bOrganizationRetrieveRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t2\xec\x01\n\x16OrganizationController\x12\x65\n\x04List\x12-.weni.connect.project.OrganizationListRequest\x1a*.weni.connect.project.OrganizationResponse\"\x00\x30\x01\x12k\n\x08Retrieve\x12\x31.weni.connect.project.OrganizationRetrieveRequest\x1a*.weni.connect.project.OrganizationResponse\"\x00\x62\x06proto3'
)




_ORGANIZATIONRESPONSE = _descriptor.Descriptor(
  name='OrganizationResponse',
  full_name='weni.connect.project.OrganizationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.connect.project.OrganizationResponse.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.connect.project.OrganizationResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='weni.connect.project.OrganizationResponse.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inteligence_organization', full_name='weni.connect.project.OrganizationResponse.inteligence_organization', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra_integration', full_name='weni.connect.project.OrganizationResponse.extra_integration', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_suspended', full_name='weni.connect.project.OrganizationResponse.is_suspended', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=67,
  serialized_end=221,
)


_ORGANIZATIONLISTREQUEST = _descriptor.Descriptor(
  name='OrganizationListRequest',
  full_name='weni.connect.project.OrganizationListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.connect.project.OrganizationListRequest.uuid', index=0,
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
  serialized_start=223,
  serialized_end=262,
)


_ORGANIZATIONRETRIEVEREQUEST = _descriptor.Descriptor(
  name='OrganizationRetrieveRequest',
  full_name='weni.connect.project.OrganizationRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.connect.project.OrganizationRetrieveRequest.uuid', index=0,
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
  serialized_start=264,
  serialized_end=307,
)

DESCRIPTOR.message_types_by_name['OrganizationResponse'] = _ORGANIZATIONRESPONSE
DESCRIPTOR.message_types_by_name['OrganizationListRequest'] = _ORGANIZATIONLISTREQUEST
DESCRIPTOR.message_types_by_name['OrganizationRetrieveRequest'] = _ORGANIZATIONRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrganizationResponse = _reflection.GeneratedProtocolMessageType('OrganizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _ORGANIZATIONRESPONSE,
  '__module__' : 'weni.protobuf.connect.organization_pb2'
  # @@protoc_insertion_point(class_scope:weni.connect.project.OrganizationResponse)
  })
_sym_db.RegisterMessage(OrganizationResponse)

OrganizationListRequest = _reflection.GeneratedProtocolMessageType('OrganizationListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGANIZATIONLISTREQUEST,
  '__module__' : 'weni.protobuf.connect.organization_pb2'
  # @@protoc_insertion_point(class_scope:weni.connect.project.OrganizationListRequest)
  })
_sym_db.RegisterMessage(OrganizationListRequest)

OrganizationRetrieveRequest = _reflection.GeneratedProtocolMessageType('OrganizationRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGANIZATIONRETRIEVEREQUEST,
  '__module__' : 'weni.protobuf.connect.organization_pb2'
  # @@protoc_insertion_point(class_scope:weni.connect.project.OrganizationRetrieveRequest)
  })
_sym_db.RegisterMessage(OrganizationRetrieveRequest)



_ORGANIZATIONCONTROLLER = _descriptor.ServiceDescriptor(
  name='OrganizationController',
  full_name='weni.connect.project.OrganizationController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=310,
  serialized_end=546,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='weni.connect.project.OrganizationController.List',
    index=0,
    containing_service=None,
    input_type=_ORGANIZATIONLISTREQUEST,
    output_type=_ORGANIZATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='weni.connect.project.OrganizationController.Retrieve',
    index=1,
    containing_service=None,
    input_type=_ORGANIZATIONRETRIEVEREQUEST,
    output_type=_ORGANIZATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORGANIZATIONCONTROLLER)

DESCRIPTOR.services_by_name['OrganizationController'] = _ORGANIZATIONCONTROLLER

# @@protoc_insertion_point(module_scope)
