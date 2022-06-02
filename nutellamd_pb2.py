# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nutellamd.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nutellamd.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fnutellamd.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x1b\n\x0bTestMessage\x12\x0c\n\x04text\x18\x01 \x01(\t\"#\n\x07\x41\x64\x64ress\x12\n\n\x02ip\x18\x01 \x01(\x05\x12\x0c\n\x04port\x18\x02 \x01(\x05\"M\n\rSearchMessage\x12\x16\n\x04\x61\x64\x64r\x18\x01 \x01(\x0b\x32\x08.Address\x12\x10\n\x08\x66ileName\x18\x02 \x01(\t\x12\x12\n\nidentifier\x18\x03 \x01(\t\"\x1e\n\x0eSearchResponse\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\t\"\"\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t2\xac\x01\n\nPeerToPeer\x12=\n\tHeartBeat\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\'\n\x07TestRpc\x12\x0c.TestMessage\x1a\x0c.TestMessage\"\x00\x12\x36\n\nSearchFile\x12\x0e.SearchMessage\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_TESTMESSAGE = _descriptor.Descriptor(
  name='TestMessage',
  full_name='TestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='TestMessage.text', index=0,
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
  serialized_start=48,
  serialized_end=75,
)


_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='Address.ip', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='Address.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=77,
  serialized_end=112,
)


_SEARCHMESSAGE = _descriptor.Descriptor(
  name='SearchMessage',
  full_name='SearchMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr', full_name='SearchMessage.addr', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fileName', full_name='SearchMessage.fileName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='SearchMessage.identifier', index=2,
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
  serialized_start=114,
  serialized_end=191,
)


_SEARCHRESPONSE = _descriptor.Descriptor(
  name='SearchResponse',
  full_name='SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr', full_name='SearchResponse.addr', index=0,
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
  serialized_start=193,
  serialized_end=223,
)


_FILE = _descriptor.Descriptor(
  name='File',
  full_name='File',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='File.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='File.data', index=1,
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
  serialized_start=225,
  serialized_end=259,
)

_SEARCHMESSAGE.fields_by_name['addr'].message_type = _ADDRESS
DESCRIPTOR.message_types_by_name['TestMessage'] = _TESTMESSAGE
DESCRIPTOR.message_types_by_name['Address'] = _ADDRESS
DESCRIPTOR.message_types_by_name['SearchMessage'] = _SEARCHMESSAGE
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE
DESCRIPTOR.message_types_by_name['File'] = _FILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestMessage = _reflection.GeneratedProtocolMessageType('TestMessage', (_message.Message,), {
  'DESCRIPTOR' : _TESTMESSAGE,
  '__module__' : 'nutellamd_pb2'
  # @@protoc_insertion_point(class_scope:TestMessage)
  })
_sym_db.RegisterMessage(TestMessage)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESS,
  '__module__' : 'nutellamd_pb2'
  # @@protoc_insertion_point(class_scope:Address)
  })
_sym_db.RegisterMessage(Address)

SearchMessage = _reflection.GeneratedProtocolMessageType('SearchMessage', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHMESSAGE,
  '__module__' : 'nutellamd_pb2'
  # @@protoc_insertion_point(class_scope:SearchMessage)
  })
_sym_db.RegisterMessage(SearchMessage)

SearchResponse = _reflection.GeneratedProtocolMessageType('SearchResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHRESPONSE,
  '__module__' : 'nutellamd_pb2'
  # @@protoc_insertion_point(class_scope:SearchResponse)
  })
_sym_db.RegisterMessage(SearchResponse)

File = _reflection.GeneratedProtocolMessageType('File', (_message.Message,), {
  'DESCRIPTOR' : _FILE,
  '__module__' : 'nutellamd_pb2'
  # @@protoc_insertion_point(class_scope:File)
  })
_sym_db.RegisterMessage(File)



_PEERTOPEER = _descriptor.ServiceDescriptor(
  name='PeerToPeer',
  full_name='PeerToPeer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=262,
  serialized_end=434,
  methods=[
  _descriptor.MethodDescriptor(
    name='HeartBeat',
    full_name='PeerToPeer.HeartBeat',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TestRpc',
    full_name='PeerToPeer.TestRpc',
    index=1,
    containing_service=None,
    input_type=_TESTMESSAGE,
    output_type=_TESTMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchFile',
    full_name='PeerToPeer.SearchFile',
    index=2,
    containing_service=None,
    input_type=_SEARCHMESSAGE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PEERTOPEER)

DESCRIPTOR.services_by_name['PeerToPeer'] = _PEERTOPEER

# @@protoc_insertion_point(module_scope)
