# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_communicator.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17grpc_communicator.proto\" \n\nDataBuffer\x12\x12\n\ndata_bytes\x18\x01 \x01(\x0c\"!\n\x0c\x43lientHeader\x12\x11\n\tclient_id\x18\x01 \x01(\t\"-\n\x0cServerHeader\x12\x1d\n\x06status\x18\x01 \x01(\x0e\x32\r.ServerStatus\"H\n\x14\x43onfigurationRequest\x12\x1d\n\x06header\x18\x01 \x01(\x0b\x32\r.ClientHeader\x12\x11\n\tmeta_data\x18\x02 \x01(\t\"M\n\x15\x43onfigurationResponse\x12\x1d\n\x06header\x18\x01 \x01(\x0b\x32\r.ServerHeader\x12\x15\n\rconfiguration\x18\x02 \x01(\t\"I\n\x15GetGlobalModelRequest\x12\x1d\n\x06header\x18\x01 \x01(\x0b\x32\r.ClientHeader\x12\x11\n\tmeta_data\x18\x02 \x01(\t\"_\n\x15GetGlobalModelRespone\x12\x1d\n\x06header\x18\x01 \x01(\x0b\x32\r.ServerHeader\x12\x14\n\x0cglobal_model\x18\x02 \x01(\x0c\x12\x11\n\tmeta_data\x18\x03 \x01(\t\"a\n\x18UpdateGlobalModelRequest\x12\x1d\n\x06header\x18\x01 \x01(\x0b\x32\r.ClientHeader\x12\x13\n\x0blocal_model\x18\x02 \x01(\x0c\x12\x11\n\tmeta_data\x18\x03 \x01(\t\"c\n\x19UpdateGlobalModelResponse\x12\x1d\n\x06header\x18\x01 \x01(\x0b\x32\r.ServerHeader\x12\x14\n\x0cglobal_model\x18\x02 \x01(\x0c\x12\x11\n\tmeta_data\x18\x03 \x01(\t\"W\n\x13\x43ustomActionRequest\x12\x1d\n\x06header\x18\x01 \x01(\x0b\x32\r.ClientHeader\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x11\n\tmeta_data\x18\x03 \x01(\t\"F\n\x14\x43ustomActionResponse\x12\x1d\n\x06header\x18\x01 \x01(\x0b\x32\r.ServerHeader\x12\x0f\n\x07results\x18\x02 \x01(\t*,\n\x0cServerStatus\x12\x07\n\x03RUN\x10\x00\x12\x08\n\x04\x44ONE\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x32\x86\x02\n\x10GRPCCommunicator\x12\x43\n\x10GetConfiguration\x12\x15.ConfigurationRequest\x1a\x16.ConfigurationResponse\"\x00\x12\x39\n\x0eGetGlobalModel\x12\x16.GetGlobalModelRequest\x1a\x0b.DataBuffer\"\x00\x30\x01\x12\x33\n\x11UpdateGlobalModel\x12\x0b.DataBuffer\x1a\x0b.DataBuffer\"\x00(\x01\x30\x01\x12=\n\x0c\x43ustomAction\x12\x14.CustomActionRequest\x1a\x15.CustomActionResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_communicator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SERVERSTATUS']._serialized_start=829
  _globals['_SERVERSTATUS']._serialized_end=873
  _globals['_DATABUFFER']._serialized_start=27
  _globals['_DATABUFFER']._serialized_end=59
  _globals['_CLIENTHEADER']._serialized_start=61
  _globals['_CLIENTHEADER']._serialized_end=94
  _globals['_SERVERHEADER']._serialized_start=96
  _globals['_SERVERHEADER']._serialized_end=141
  _globals['_CONFIGURATIONREQUEST']._serialized_start=143
  _globals['_CONFIGURATIONREQUEST']._serialized_end=215
  _globals['_CONFIGURATIONRESPONSE']._serialized_start=217
  _globals['_CONFIGURATIONRESPONSE']._serialized_end=294
  _globals['_GETGLOBALMODELREQUEST']._serialized_start=296
  _globals['_GETGLOBALMODELREQUEST']._serialized_end=369
  _globals['_GETGLOBALMODELRESPONE']._serialized_start=371
  _globals['_GETGLOBALMODELRESPONE']._serialized_end=466
  _globals['_UPDATEGLOBALMODELREQUEST']._serialized_start=468
  _globals['_UPDATEGLOBALMODELREQUEST']._serialized_end=565
  _globals['_UPDATEGLOBALMODELRESPONSE']._serialized_start=567
  _globals['_UPDATEGLOBALMODELRESPONSE']._serialized_end=666
  _globals['_CUSTOMACTIONREQUEST']._serialized_start=668
  _globals['_CUSTOMACTIONREQUEST']._serialized_end=755
  _globals['_CUSTOMACTIONRESPONSE']._serialized_start=757
  _globals['_CUSTOMACTIONRESPONSE']._serialized_end=827
  _globals['_GRPCCOMMUNICATOR']._serialized_start=876
  _globals['_GRPCCOMMUNICATOR']._serialized_end=1138
# @@protoc_insertion_point(module_scope)
