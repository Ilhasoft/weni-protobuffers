# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weni/protobuf/flows/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='weni/protobuf/flows/user.proto',
  package='weni.flows.user',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eweni/protobuf/flows/user.proto\x12\x0fweni.flows.user\"E\n\x1dUserPermissionRetrieveRequest\x12\x12\n\nuser_email\x18\x01 \x01(\t\x12\x10\n\x08org_uuid\x18\x02 \x01(\t\"W\n\x1bUserPermissionUpdateRequest\x12\x10\n\x08org_uuid\x18\x01 \x01(\t\x12\x12\n\nuser_email\x18\x02 \x01(\t\x12\x12\n\npermission\x18\x03 \x01(\t\"d\n\nPermission\x12\x15\n\radministrator\x18\x01 \x01(\x08\x12\x0e\n\x06viewer\x18\x02 \x01(\x08\x12\x0e\n\x06\x65\x64itor\x18\x03 \x01(\x08\x12\x10\n\x08surveyor\x18\x04 \x01(\x08\x12\r\n\x05\x61gent\x18\x05 \x01(\x08\"$\n\x13UserRetrieveRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"1\n\x0eUpdateUserLang\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\"\x98\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x12\n\nfirst_name\x18\x04 \x01(\t\x12\x11\n\tlast_name\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x61te_joined\x18\x06 \x01(\t\x12\x11\n\tis_active\x18\x07 \x01(\x08\x12\x14\n\x0cis_superuser\x18\x08 \x01(\x08\x32\xa3\x02\n\x18UserPermissionController\x12Y\n\x08Retrieve\x12..weni.flows.user.UserPermissionRetrieveRequest\x1a\x1b.weni.flows.user.Permission\"\x00\x12U\n\x06Update\x12,.weni.flows.user.UserPermissionUpdateRequest\x1a\x1b.weni.flows.user.Permission\"\x00\x12U\n\x06Remove\x12,.weni.flows.user.UserPermissionUpdateRequest\x1a\x1b.weni.flows.user.Permission\"\x00\x32\x9f\x01\n\x0eUserController\x12I\n\x08Retrieve\x12$.weni.flows.user.UserRetrieveRequest\x1a\x15.weni.flows.user.User\"\x00\x12\x42\n\x06Update\x12\x1f.weni.flows.user.UpdateUserLang\x1a\x15.weni.flows.user.User\"\x00\x62\x06proto3'
)




_USERPERMISSIONRETRIEVEREQUEST = _descriptor.Descriptor(
  name='UserPermissionRetrieveRequest',
  full_name='weni.flows.user.UserPermissionRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_email', full_name='weni.flows.user.UserPermissionRetrieveRequest.user_email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='org_uuid', full_name='weni.flows.user.UserPermissionRetrieveRequest.org_uuid', index=1,
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
  serialized_start=51,
  serialized_end=120,
)


_USERPERMISSIONUPDATEREQUEST = _descriptor.Descriptor(
  name='UserPermissionUpdateRequest',
  full_name='weni.flows.user.UserPermissionUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_uuid', full_name='weni.flows.user.UserPermissionUpdateRequest.org_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_email', full_name='weni.flows.user.UserPermissionUpdateRequest.user_email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='permission', full_name='weni.flows.user.UserPermissionUpdateRequest.permission', index=2,
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
  serialized_start=122,
  serialized_end=209,
)


_PERMISSION = _descriptor.Descriptor(
  name='Permission',
  full_name='weni.flows.user.Permission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='administrator', full_name='weni.flows.user.Permission.administrator', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='viewer', full_name='weni.flows.user.Permission.viewer', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='editor', full_name='weni.flows.user.Permission.editor', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='surveyor', full_name='weni.flows.user.Permission.surveyor', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agent', full_name='weni.flows.user.Permission.agent', index=4,
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
  serialized_start=211,
  serialized_end=311,
)


_USERRETRIEVEREQUEST = _descriptor.Descriptor(
  name='UserRetrieveRequest',
  full_name='weni.flows.user.UserRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='weni.flows.user.UserRetrieveRequest.email', index=0,
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
  serialized_start=313,
  serialized_end=349,
)


_UPDATEUSERLANG = _descriptor.Descriptor(
  name='UpdateUserLang',
  full_name='weni.flows.user.UpdateUserLang',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='weni.flows.user.UpdateUserLang.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language', full_name='weni.flows.user.UpdateUserLang.language', index=1,
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
  serialized_start=351,
  serialized_end=400,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='weni.flows.user.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='weni.flows.user.User.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='weni.flows.user.User.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='weni.flows.user.User.username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='weni.flows.user.User.first_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='weni.flows.user.User.last_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_joined', full_name='weni.flows.user.User.date_joined', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_active', full_name='weni.flows.user.User.is_active', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_superuser', full_name='weni.flows.user.User.is_superuser', index=7,
      number=8, type=8, cpp_type=7, label=1,
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
  serialized_start=403,
  serialized_end=555,
)

DESCRIPTOR.message_types_by_name['UserPermissionRetrieveRequest'] = _USERPERMISSIONRETRIEVEREQUEST
DESCRIPTOR.message_types_by_name['UserPermissionUpdateRequest'] = _USERPERMISSIONUPDATEREQUEST
DESCRIPTOR.message_types_by_name['Permission'] = _PERMISSION
DESCRIPTOR.message_types_by_name['UserRetrieveRequest'] = _USERRETRIEVEREQUEST
DESCRIPTOR.message_types_by_name['UpdateUserLang'] = _UPDATEUSERLANG
DESCRIPTOR.message_types_by_name['User'] = _USER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserPermissionRetrieveRequest = _reflection.GeneratedProtocolMessageType('UserPermissionRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERPERMISSIONRETRIEVEREQUEST,
  '__module__' : 'weni.protobuf.flows.user_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.user.UserPermissionRetrieveRequest)
  })
_sym_db.RegisterMessage(UserPermissionRetrieveRequest)

UserPermissionUpdateRequest = _reflection.GeneratedProtocolMessageType('UserPermissionUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERPERMISSIONUPDATEREQUEST,
  '__module__' : 'weni.protobuf.flows.user_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.user.UserPermissionUpdateRequest)
  })
_sym_db.RegisterMessage(UserPermissionUpdateRequest)

Permission = _reflection.GeneratedProtocolMessageType('Permission', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSION,
  '__module__' : 'weni.protobuf.flows.user_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.user.Permission)
  })
_sym_db.RegisterMessage(Permission)

UserRetrieveRequest = _reflection.GeneratedProtocolMessageType('UserRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERRETRIEVEREQUEST,
  '__module__' : 'weni.protobuf.flows.user_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.user.UserRetrieveRequest)
  })
_sym_db.RegisterMessage(UserRetrieveRequest)

UpdateUserLang = _reflection.GeneratedProtocolMessageType('UpdateUserLang', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERLANG,
  '__module__' : 'weni.protobuf.flows.user_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.user.UpdateUserLang)
  })
_sym_db.RegisterMessage(UpdateUserLang)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'weni.protobuf.flows.user_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.user.User)
  })
_sym_db.RegisterMessage(User)



_USERPERMISSIONCONTROLLER = _descriptor.ServiceDescriptor(
  name='UserPermissionController',
  full_name='weni.flows.user.UserPermissionController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=558,
  serialized_end=849,
  methods=[
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='weni.flows.user.UserPermissionController.Retrieve',
    index=0,
    containing_service=None,
    input_type=_USERPERMISSIONRETRIEVEREQUEST,
    output_type=_PERMISSION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='weni.flows.user.UserPermissionController.Update',
    index=1,
    containing_service=None,
    input_type=_USERPERMISSIONUPDATEREQUEST,
    output_type=_PERMISSION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Remove',
    full_name='weni.flows.user.UserPermissionController.Remove',
    index=2,
    containing_service=None,
    input_type=_USERPERMISSIONUPDATEREQUEST,
    output_type=_PERMISSION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERPERMISSIONCONTROLLER)

DESCRIPTOR.services_by_name['UserPermissionController'] = _USERPERMISSIONCONTROLLER


_USERCONTROLLER = _descriptor.ServiceDescriptor(
  name='UserController',
  full_name='weni.flows.user.UserController',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=852,
  serialized_end=1011,
  methods=[
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='weni.flows.user.UserController.Retrieve',
    index=0,
    containing_service=None,
    input_type=_USERRETRIEVEREQUEST,
    output_type=_USER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='weni.flows.user.UserController.Update',
    index=1,
    containing_service=None,
    input_type=_UPDATEUSERLANG,
    output_type=_USER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERCONTROLLER)

DESCRIPTOR.services_by_name['UserController'] = _USERCONTROLLER

# @@protoc_insertion_point(module_scope)
