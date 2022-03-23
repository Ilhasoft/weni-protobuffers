# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weni/protobuf/flows/org.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dweni/protobuf/flows/org.proto\x12\x0eweni.flows.org\x1a\x1bgoogle/protobuf/empty.proto\"\x9f\x01\n\x03Org\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04uuid\x18\x03 \x01(\t\x12\x10\n\x08timezone\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x61te_format\x18\x05 \x01(\t\x12#\n\x05users\x18\x06 \x03(\x0b\x32\x14.weni.flows.org.User\x12\x16\n\tis_active\x18\t \x01(\x08H\x00\x88\x01\x01\x42\x0c\n\n_is_active\"Z\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x12\n\nfirst_name\x18\x04 \x01(\t\x12\x11\n\tlast_name\x18\x05 \x01(\t\"$\n\x0eOrgListRequest\x12\x12\n\nuser_email\x18\x01 \x01(\t\"F\n\x10OrgCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08timezone\x18\x02 \x01(\t\x12\x12\n\nuser_email\x18\x03 \x01(\t\"\"\n\x12OrgRetrieveRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"5\n\x11OrgDestroyRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x12\n\nuser_email\x18\x02 \x01(\t\"\xba\x03\n\x10OrgUpdateRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x18\n\x0bmodified_by\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04name\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08timezone\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x0b\x64\x61te_format\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x11\n\x04plan\x18\x06 \x01(\tH\x04\x88\x01\x01\x12\x15\n\x08plan_end\x18\x07 \x01(\tH\x05\x88\x01\x01\x12\x12\n\x05\x62rand\x18\x08 \x01(\tH\x06\x88\x01\x01\x12\x14\n\x07is_anon\x18\t \x01(\x08H\x07\x88\x01\x01\x12\x1a\n\ris_multi_user\x18\n \x01(\x08H\x08\x88\x01\x01\x12\x19\n\x0cis_multi_org\x18\x0b \x01(\x08H\t\x88\x01\x01\x12\x19\n\x0cis_suspended\x18\x0c \x01(\x08H\n\x88\x01\x01\x42\x0e\n\x0c_modified_byB\x07\n\x05_nameB\x0b\n\t_timezoneB\x0e\n\x0c_date_formatB\x07\n\x05_planB\x0b\n\t_plan_endB\x08\n\x06_brandB\n\n\x08_is_anonB\x10\n\x0e_is_multi_userB\x0f\n\r_is_multi_orgB\x0f\n\r_is_suspended2\xe5\x02\n\rOrgController\x12?\n\x04List\x12\x1e.weni.flows.org.OrgListRequest\x1a\x13.weni.flows.org.Org\"\x00\x30\x01\x12\x41\n\x06\x43reate\x12 .weni.flows.org.OrgCreateRequest\x1a\x13.weni.flows.org.Org\"\x00\x12\x45\n\x08Retrieve\x12\".weni.flows.org.OrgRetrieveRequest\x1a\x13.weni.flows.org.Org\"\x00\x12\x41\n\x06Update\x12 .weni.flows.org.OrgUpdateRequest\x1a\x13.weni.flows.org.Org\"\x00\x12\x46\n\x07\x44\x65stroy\x12!.weni.flows.org.OrgDestroyRequest\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')



_ORG = DESCRIPTOR.message_types_by_name['Org']
_USER = DESCRIPTOR.message_types_by_name['User']
_ORGLISTREQUEST = DESCRIPTOR.message_types_by_name['OrgListRequest']
_ORGCREATEREQUEST = DESCRIPTOR.message_types_by_name['OrgCreateRequest']
_ORGRETRIEVEREQUEST = DESCRIPTOR.message_types_by_name['OrgRetrieveRequest']
_ORGDESTROYREQUEST = DESCRIPTOR.message_types_by_name['OrgDestroyRequest']
_ORGUPDATEREQUEST = DESCRIPTOR.message_types_by_name['OrgUpdateRequest']
Org = _reflection.GeneratedProtocolMessageType('Org', (_message.Message,), {
  'DESCRIPTOR' : _ORG,
  '__module__' : 'weni.protobuf.flows.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.org.Org)
  })
_sym_db.RegisterMessage(Org)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'weni.protobuf.flows.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.org.User)
  })
_sym_db.RegisterMessage(User)

OrgListRequest = _reflection.GeneratedProtocolMessageType('OrgListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGLISTREQUEST,
  '__module__' : 'weni.protobuf.flows.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.org.OrgListRequest)
  })
_sym_db.RegisterMessage(OrgListRequest)

OrgCreateRequest = _reflection.GeneratedProtocolMessageType('OrgCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGCREATEREQUEST,
  '__module__' : 'weni.protobuf.flows.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.org.OrgCreateRequest)
  })
_sym_db.RegisterMessage(OrgCreateRequest)

OrgRetrieveRequest = _reflection.GeneratedProtocolMessageType('OrgRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGRETRIEVEREQUEST,
  '__module__' : 'weni.protobuf.flows.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.org.OrgRetrieveRequest)
  })
_sym_db.RegisterMessage(OrgRetrieveRequest)

OrgDestroyRequest = _reflection.GeneratedProtocolMessageType('OrgDestroyRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGDESTROYREQUEST,
  '__module__' : 'weni.protobuf.flows.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.org.OrgDestroyRequest)
  })
_sym_db.RegisterMessage(OrgDestroyRequest)

OrgUpdateRequest = _reflection.GeneratedProtocolMessageType('OrgUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORGUPDATEREQUEST,
  '__module__' : 'weni.protobuf.flows.org_pb2'
  # @@protoc_insertion_point(class_scope:weni.flows.org.OrgUpdateRequest)
  })
_sym_db.RegisterMessage(OrgUpdateRequest)

_ORGCONTROLLER = DESCRIPTOR.services_by_name['OrgController']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ORG._serialized_start=79
  _ORG._serialized_end=238
  _USER._serialized_start=240
  _USER._serialized_end=330
  _ORGLISTREQUEST._serialized_start=332
  _ORGLISTREQUEST._serialized_end=368
  _ORGCREATEREQUEST._serialized_start=370
  _ORGCREATEREQUEST._serialized_end=440
  _ORGRETRIEVEREQUEST._serialized_start=442
  _ORGRETRIEVEREQUEST._serialized_end=476
  _ORGDESTROYREQUEST._serialized_start=478
  _ORGDESTROYREQUEST._serialized_end=531
  _ORGUPDATEREQUEST._serialized_start=534
  _ORGUPDATEREQUEST._serialized_end=976
  _ORGCONTROLLER._serialized_start=979
  _ORGCONTROLLER._serialized_end=1336
# @@protoc_insertion_point(module_scope)
