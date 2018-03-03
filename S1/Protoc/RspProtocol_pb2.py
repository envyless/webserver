# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RspProtocol.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='RspProtocol.proto',
  package='',
  serialized_pb=_b('\n\x11RspProtocol.proto\"-\n\x08UserData\x12\x11\n\tnick_name\x18\x01 \x02(\t\x12\x0e\n\x06monney\x18\x02 \x02(\x03*;\n\x08RspLogIn\x12\x0f\n\x0bRSP_ID_FAIL\x10\x00\x12\x0f\n\x0bRSP_PW_FAIL\x10\x01\x12\r\n\tRSP_LOGIN\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_RSPLOGIN = _descriptor.EnumDescriptor(
  name='RspLogIn',
  full_name='RspLogIn',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RSP_ID_FAIL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RSP_PW_FAIL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RSP_LOGIN', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=68,
  serialized_end=127,
)
_sym_db.RegisterEnumDescriptor(_RSPLOGIN)

RspLogIn = enum_type_wrapper.EnumTypeWrapper(_RSPLOGIN)
RSP_ID_FAIL = 0
RSP_PW_FAIL = 1
RSP_LOGIN = 2



_USERDATA = _descriptor.Descriptor(
  name='UserData',
  full_name='UserData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nick_name', full_name='UserData.nick_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='monney', full_name='UserData.monney', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=21,
  serialized_end=66,
)

DESCRIPTOR.message_types_by_name['UserData'] = _USERDATA
DESCRIPTOR.enum_types_by_name['RspLogIn'] = _RSPLOGIN

UserData = _reflection.GeneratedProtocolMessageType('UserData', (_message.Message,), dict(
  DESCRIPTOR = _USERDATA,
  __module__ = 'RspProtocol_pb2'
  # @@protoc_insertion_point(class_scope:UserData)
  ))
_sym_db.RegisterMessage(UserData)


# @@protoc_insertion_point(module_scope)
