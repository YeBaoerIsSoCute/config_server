# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63onfig.proto\x12\x06\x63onfig\"0\n\x10GetConfigRequest\x12\x0f\n\x07section\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"\"\n\x11GetConfigResponse\x12\r\n\x05value\x18\x01 \x01(\t\"?\n\x10SetConfigRequest\x12\x0f\n\x07section\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"$\n\x11SetConfigResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\x97\x01\n\rConfigService\x12\x42\n\tGetConfig\x12\x18.config.GetConfigRequest\x1a\x19.config.GetConfigResponse\"\x00\x12\x42\n\tSetConfig\x12\x18.config.SetConfigRequest\x1a\x19.config.SetConfigResponse\"\x00\x42\nZ\x08protobufb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\010protobuf'
  _globals['_GETCONFIGREQUEST']._serialized_start=24
  _globals['_GETCONFIGREQUEST']._serialized_end=72
  _globals['_GETCONFIGRESPONSE']._serialized_start=74
  _globals['_GETCONFIGRESPONSE']._serialized_end=108
  _globals['_SETCONFIGREQUEST']._serialized_start=110
  _globals['_SETCONFIGREQUEST']._serialized_end=173
  _globals['_SETCONFIGRESPONSE']._serialized_start=175
  _globals['_SETCONFIGRESPONSE']._serialized_end=211
  _globals['_CONFIGSERVICE']._serialized_start=214
  _globals['_CONFIGSERVICE']._serialized_end=365
# @@protoc_insertion_point(module_scope)