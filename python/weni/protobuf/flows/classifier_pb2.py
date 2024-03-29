# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weni/protobuf/flows/classifier.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='weni/protobuf/flows/classifier.proto',
  package='weni.flows.classifier',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$weni/protobuf/flows/classifier.proto\x12\x15weni.flows.classifier\x1a\x1bgoogle/protobuf/empty.proto\"n\n\x15\x43lassifierListRequest\x12\x10\n\x08org_uuid\x18\x01 \x01(\t\x12\x11\n\tis_active\x18\x02 \x01(\x08\x12\x1c\n\x0f\x63lassifier_type\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x12\n\x10_classifier_type\"j\n\nClassifier\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x17\n\x0f\x63lassifier_type\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\t\x12\x11\n\tis_active\x18\x05 \x01(\x08\"q\n\x17\x43lassifierCreateRequest\x12\x0b\n\x03org\x18\x01 \x01(\t\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x17\n\x0f\x63lassifier_type\x18\x04 \x01(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x06 \x01(\t\")\n\x19\x43lassifierRetrieveRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"<\n\x18\x43lassifierDestroyRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x12\n\nuser_email\x18\x02 \x01(\t2\x8b\x03\n\x14\x43lassifierController\x12]\n\x06\x43reate\x12..weni.flows.classifier.ClassifierCreateRequest\x1a!.weni.flows.classifier.Classifier\"\x00\x12\x61\n\x08Retrieve\x12\x30.weni.flows.classifier.ClassifierRetrieveRequest\x1a!.weni.flows.classifier.Classifier\"\x00\x12T\n\x07\x44\x65stroy\x12/.weni.flows.classifier.ClassifierDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12[\n\x04List\x12,.weni.flows.classifier.ClassifierListRequest\x1a!.weni.flows.classifier.Classifier\"\x00\x30\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_CLASSIFIERLISTREQUEST = _descriptor.Descriptor(
  name='ClassifierListRequest',
  full_name='weni.flows.classifier.ClassifierListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_uuid', full_name='weni.flows.classifier.ClassifierListRequest.org_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_active', full_name='weni.flows.classifier.ClassifierListRequest.is_active', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classifier_type', full_name='weni.flows.classifier.ClassifierListRequest.classifier_type', index=2,
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
    _descriptor.OneofDescriptor(
      name='_classifier_type', full_name='weni.flows.classifier.ClassifierListRequest._classifier_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=92,
  serialized_end=202,
)


_CLASSIFIER = _descriptor.Descriptor(
  name='Classifier',
  full_name='weni.flows.classifier.Classifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.flows.classifier.Classifier.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classifier_type', full_name='weni.flows.classifier.Classifier.classifier_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.flows.classifier.Classifier.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='weni.flows.classifier.Classifier.access_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_active', full_name='weni.flows.classifier.Classifier.is_active', index=4,
      number=5, type=8, cpp_type=7, label=1,
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
  serialized_start=204,
  serialized_end=310,
)


_CLASSIFIERCREATEREQUEST = _descriptor.Descriptor(
  name='ClassifierCreateRequest',
  full_name='weni.flows.classifier.ClassifierCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org', full_name='weni.flows.classifier.ClassifierCreateRequest.org', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='weni.flows.classifier.ClassifierCreateRequest.user', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classifier_type', full_name='weni.flows.classifier.ClassifierCreateRequest.classifier_type', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.flows.classifier.ClassifierCreateRequest.name', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='weni.flows.classifier.ClassifierCreateRequest.access_token', index=4,
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
  serialized_start=312,
  serialized_end=425,
)


_CLASSIFIERRETRIEVEREQUEST = _descriptor.Descriptor(
  name='ClassifierRetrieveRequest',
  full_name='weni.flows.classifier.ClassifierRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.flows.classifier.ClassifierRetrieveRequest.uuid', index=0,
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
  serialized_start=427,
  serialized_end=468,
)


_CLASSIFIERDESTROYREQUEST = _descriptor.Descriptor(
  name='ClassifierDestroyRequest',
  full_name='weni.flows.classifier.ClassifierDestroyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.flows.classifier.ClassifierDestroyRequest.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='weni.flows.classifier.ClassifierDestroyRequest.user_email', index=1,
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
  serialized_start=470,
  serialized_end=530,
)

_CLASSIFIERLISTREQUEST.oneofs_by_name['_classifier_type'].fields.append(
  _CLASSIFIERLISTREQUEST.fields_by_name['classifier_type'])
_CLASSIFIERLISTREQUEST.fields_by_name['classifier_type'].containing_oneof = _CLASSIFIERLISTREQUEST.oneofs_by_name['_classifier_type']
DESCRIPTOR.message_types_by_name['ClassifierListRequest'] = _CLASSIFIERLISTREQUEST
DESCRIPTOR.message_types_by_name['Classifier'] = _CLASSIFIER
DESCRIPTOR.message_types_by_name['ClassifierCreateRequest'] = _CLASSIFIERCREATEREQUEST
DESCRIPTOR.message_types_by_name['ClassifierRetrieveRequest'] = _CLASSIFIERRETRIEVEREQUEST
DESCRIPTOR.message_types_by_name['ClassifierDestroyRequest'] = _CLASSIFIERDESTROYREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassifierListRequest = _reflection.GeneratedProtocolMessageType('ClassifierListRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERLISTREQUEST,
  '__module__' : 'weni.protobuf.flows.classifier_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.classifier.ClassifierListRequest)
  })
_sym_db.RegisterMessage(ClassifierListRequest)

Classifier = _reflection.GeneratedProtocolMessageType('Classifier', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIER,
  '__module__' : 'weni.protobuf.flows.classifier_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.classifier.Classifier)
  })
_sym_db.RegisterMessage(Classifier)

ClassifierCreateRequest = _reflection.GeneratedProtocolMessageType('ClassifierCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERCREATEREQUEST,
  '__module__' : 'weni.protobuf.flows.classifier_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.classifier.ClassifierCreateRequest)
  })
_sym_db.RegisterMessage(ClassifierCreateRequest)

ClassifierRetrieveRequest = _reflection.GeneratedProtocolMessageType('ClassifierRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERRETRIEVEREQUEST,
  '__module__' : 'weni.protobuf.flows.classifier_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.classifier.ClassifierRetrieveRequest)
  })
_sym_db.RegisterMessage(ClassifierRetrieveRequest)

ClassifierDestroyRequest = _reflection.GeneratedProtocolMessageType('ClassifierDestroyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFIERDESTROYREQUEST,
  '__module__' : 'weni.protobuf.flows.classifier_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.classifier.ClassifierDestroyRequest)
  })
_sym_db.RegisterMessage(ClassifierDestroyRequest)



_CLASSIFIERCONTROLLER = _descriptor.ServiceDescriptor(
  name='ClassifierController',
  full_name='weni.flows.classifier.ClassifierController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=533,
  serialized_end=928,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='weni.flows.classifier.ClassifierController.Create',
    index=0,
    containing_service=None,
    input_type=_CLASSIFIERCREATEREQUEST,
    output_type=_CLASSIFIER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='weni.flows.classifier.ClassifierController.Retrieve',
    index=1,
    containing_service=None,
    input_type=_CLASSIFIERRETRIEVEREQUEST,
    output_type=_CLASSIFIER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='weni.flows.classifier.ClassifierController.Destroy',
    index=2,
    containing_service=None,
    input_type=_CLASSIFIERDESTROYREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='weni.flows.classifier.ClassifierController.List',
    index=3,
    containing_service=None,
    input_type=_CLASSIFIERLISTREQUEST,
    output_type=_CLASSIFIER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CLASSIFIERCONTROLLER)

DESCRIPTOR.services_by_name['ClassifierController'] = _CLASSIFIERCONTROLLER

# @@protoc_insertion_point(module_scope)
