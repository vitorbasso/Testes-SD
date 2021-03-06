# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simpleServer.proto

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
  name='simpleServer.proto',
  package='simpleServer',
  syntax='proto3',
  serialized_pb=_b('\n\x12simpleServer.proto\x12\x0csimpleServer\"=\n\x13SimpleServerRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\"(\n\x14SimpleServerResponse\x12\x10\n\x08response\x18\x01 \x01(\t2b\n\x0cSimpleServer\x12R\n\x07Service\x12!.simpleServer.SimpleServerRequest\x1a\".simpleServer.SimpleServerResponse\"\x00\x62\x06proto3')
)




_SIMPLESERVERREQUEST = _descriptor.Descriptor(
  name='SimpleServerRequest',
  full_name='simpleServer.SimpleServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='simpleServer.SimpleServerRequest.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='simpleServer.SimpleServerRequest.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='simpleServer.SimpleServerRequest.data', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=97,
)


_SIMPLESERVERRESPONSE = _descriptor.Descriptor(
  name='SimpleServerResponse',
  full_name='simpleServer.SimpleServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='simpleServer.SimpleServerResponse.response', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=139,
)

DESCRIPTOR.message_types_by_name['SimpleServerRequest'] = _SIMPLESERVERREQUEST
DESCRIPTOR.message_types_by_name['SimpleServerResponse'] = _SIMPLESERVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleServerRequest = _reflection.GeneratedProtocolMessageType('SimpleServerRequest', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLESERVERREQUEST,
  __module__ = 'simpleServer_pb2'
  # @@protoc_insertion_point(class_scope:simpleServer.SimpleServerRequest)
  ))
_sym_db.RegisterMessage(SimpleServerRequest)

SimpleServerResponse = _reflection.GeneratedProtocolMessageType('SimpleServerResponse', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLESERVERRESPONSE,
  __module__ = 'simpleServer_pb2'
  # @@protoc_insertion_point(class_scope:simpleServer.SimpleServerResponse)
  ))
_sym_db.RegisterMessage(SimpleServerResponse)



_SIMPLESERVER = _descriptor.ServiceDescriptor(
  name='SimpleServer',
  full_name='simpleServer.SimpleServer',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=141,
  serialized_end=239,
  methods=[
  _descriptor.MethodDescriptor(
    name='Service',
    full_name='simpleServer.SimpleServer.Service',
    index=0,
    containing_service=None,
    input_type=_SIMPLESERVERREQUEST,
    output_type=_SIMPLESERVERRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIMPLESERVER)

DESCRIPTOR.services_by_name['SimpleServer'] = _SIMPLESERVER

# @@protoc_insertion_point(module_scope)
