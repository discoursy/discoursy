# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: derailed.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0e\x64\x65railed.proto\x12\rderailed.grpc"&\n\x07Message\x12\r\n\x05\x65vent\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t"A\n\x04Publ\x12\x10\n\x08guild_id\x18\x01 \x01(\t\x12\'\n\x07message\x18\x02 \x01(\x0b\x32\x16.derailed.grpc.Message"\x18\n\x05Publr\x12\x0f\n\x07message\x18\x01 \x01(\t" \n\x0cGetGuildInfo\x12\x10\n\x08guild_id\x18\x01 \x01(\t"8\n\x10RepliedGuildInfo\x12\x11\n\tpresences\x18\x01 \x01(\x05\x12\x11\n\tavailable\x18\x02 \x01(\x08"A\n\x05UPubl\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\'\n\x07message\x18\x02 \x01(\x0b\x32\x16.derailed.grpc.Message"\x19\n\x06UPublr\x12\x0f\n\x07message\x18\x01 \x01(\t2\x91\x01\n\x05Guild\x12\x36\n\x07publish\x12\x13.derailed.grpc.Publ\x1a\x14.derailed.grpc.Publr"\x00\x12P\n\x0eget_guild_info\x12\x1b.derailed.grpc.GetGuildInfo\x1a\x1f.derailed.grpc.RepliedGuildInfo"\x00\x32@\n\x04User\x12\x38\n\x07publish\x12\x14.derailed.grpc.UPubl\x1a\x15.derailed.grpc.UPublr"\x00\x42+\n\x11one.derailed.grpcB\rDerailedProtoP\x01\xa2\x02\x04\x44RLPb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'derailed_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\021one.derailed.grpcB\rDerailedProtoP\001\242\002\004DRLP'
    _MESSAGE._serialized_start = 33
    _MESSAGE._serialized_end = 71
    _PUBL._serialized_start = 73
    _PUBL._serialized_end = 138
    _PUBLR._serialized_start = 140
    _PUBLR._serialized_end = 164
    _GETGUILDINFO._serialized_start = 166
    _GETGUILDINFO._serialized_end = 198
    _REPLIEDGUILDINFO._serialized_start = 200
    _REPLIEDGUILDINFO._serialized_end = 256
    _UPUBL._serialized_start = 258
    _UPUBL._serialized_end = 323
    _UPUBLR._serialized_start = 325
    _UPUBLR._serialized_end = 350
    _GUILD._serialized_start = 353
    _GUILD._serialized_end = 498
    _USER._serialized_start = 500
    _USER._serialized_end = 564
# @@protoc_insertion_point(module_scope)