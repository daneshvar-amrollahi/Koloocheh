# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nutellamd.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fnutellamd.proto\x1a\x1bgoogle/protobuf/empty.proto\"#\n\x07\x41\x64\x64ress\x12\n\n\x02ip\x18\x01 \x01(\x05\x12\x0c\n\x04port\x18\x02 \x01(\x05\"M\n\rSearchMessage\x12\x16\n\x04\x61\x64\x64r\x18\x01 \x01(\x0b\x32\x08.Address\x12\x10\n\x08\x66ileName\x18\x02 \x01(\t\x12\x12\n\nidentifier\x18\x03 \x01(\t\"<\n\x0eSearchResponse\x12\x16\n\x04\x61\x64\x64r\x18\x01 \x01(\x0b\x32\x08.Address\x12\x12\n\nidentifier\x18\x02 \x01(\t\"\"\n\x04\x46ile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t2\xbb\x01\n\nPeerToPeer\x12=\n\tHeartBeat\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\x36\n\nSearchFile\x12\x0e.SearchMessage\x1a\x16.google.protobuf.Empty\"\x00\x12\x36\n\tFoundFile\x12\x0f.SearchResponse\x1a\x16.google.protobuf.Empty\"\x00\x32>\n\nPeerMaster\x12\x30\n\nPeerJoined\x12\x08.Address\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')



_ADDRESS = DESCRIPTOR.message_types_by_name['Address']
_SEARCHMESSAGE = DESCRIPTOR.message_types_by_name['SearchMessage']
_SEARCHRESPONSE = DESCRIPTOR.message_types_by_name['SearchResponse']
_FILE = DESCRIPTOR.message_types_by_name['File']
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

_PEERTOPEER = DESCRIPTOR.services_by_name['PeerToPeer']
_PEERMASTER = DESCRIPTOR.services_by_name['PeerMaster']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDRESS._serialized_start=48
  _ADDRESS._serialized_end=83
  _SEARCHMESSAGE._serialized_start=85
  _SEARCHMESSAGE._serialized_end=162
  _SEARCHRESPONSE._serialized_start=164
  _SEARCHRESPONSE._serialized_end=224
  _FILE._serialized_start=226
  _FILE._serialized_end=260
  _PEERTOPEER._serialized_start=263
  _PEERTOPEER._serialized_end=450
  _PEERMASTER._serialized_start=452
  _PEERMASTER._serialized_end=514
# @@protoc_insertion_point(module_scope)
