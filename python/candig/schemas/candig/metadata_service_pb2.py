# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: candig/schemas/candig/metadata_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from candig.schemas.candig import metadata_pb2 as candig_dot_schemas_dot_candig_dot_metadata__pb2
from candig.schemas.google.api import annotations_pb2 as candig_dot_schemas_dot_google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='candig/schemas/candig/metadata_service.proto',
  package='candig.schemas.candig',
  syntax='proto3',
  serialized_pb=_b('\n,candig/schemas/candig/metadata_service.proto\x12\x15\x63\x61ndig.schemas.candig\x1a$candig/schemas/candig/metadata.proto\x1a+candig/schemas/google/api/annotations.proto\">\n\x15SearchDatasetsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\"c\n\x16SearchDatasetsResponse\x12\x30\n\x08\x64\x61tasets\x18\x01 \x03(\x0b\x32\x1e.candig.schemas.candig.Dataset\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\'\n\x11GetDatasetRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t2\xa4\x02\n\x0fMetadataService\x12\x91\x01\n\x0eSearchDatasets\x12,.candig.schemas.candig.SearchDatasetsRequest\x1a-.candig.schemas.candig.SearchDatasetsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/v0.8.0/datasets/search:\x01*\x12}\n\nGetDataset\x12(.candig.schemas.candig.GetDatasetRequest\x1a\x1e.candig.schemas.candig.Dataset\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v0.8.0/datasets/{dataset_id}b\x06proto3')
  ,
  dependencies=[candig_dot_schemas_dot_candig_dot_metadata__pb2.DESCRIPTOR,candig_dot_schemas_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SEARCHDATASETSREQUEST = _descriptor.Descriptor(
  name='SearchDatasetsRequest',
  full_name='candig.schemas.candig.SearchDatasetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page_size', full_name='candig.schemas.candig.SearchDatasetsRequest.page_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='candig.schemas.candig.SearchDatasetsRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=216,
)


_SEARCHDATASETSRESPONSE = _descriptor.Descriptor(
  name='SearchDatasetsResponse',
  full_name='candig.schemas.candig.SearchDatasetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datasets', full_name='candig.schemas.candig.SearchDatasetsResponse.datasets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='candig.schemas.candig.SearchDatasetsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=317,
)


_GETDATASETREQUEST = _descriptor.Descriptor(
  name='GetDatasetRequest',
  full_name='candig.schemas.candig.GetDatasetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='candig.schemas.candig.GetDatasetRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=358,
)

_SEARCHDATASETSRESPONSE.fields_by_name['datasets'].message_type = candig_dot_schemas_dot_candig_dot_metadata__pb2._DATASET
DESCRIPTOR.message_types_by_name['SearchDatasetsRequest'] = _SEARCHDATASETSREQUEST
DESCRIPTOR.message_types_by_name['SearchDatasetsResponse'] = _SEARCHDATASETSRESPONSE
DESCRIPTOR.message_types_by_name['GetDatasetRequest'] = _GETDATASETREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchDatasetsRequest = _reflection.GeneratedProtocolMessageType('SearchDatasetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHDATASETSREQUEST,
  __module__ = 'candig.schemas.candig.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchDatasetsRequest)
  ))
_sym_db.RegisterMessage(SearchDatasetsRequest)

SearchDatasetsResponse = _reflection.GeneratedProtocolMessageType('SearchDatasetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHDATASETSRESPONSE,
  __module__ = 'candig.schemas.candig.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchDatasetsResponse)
  ))
_sym_db.RegisterMessage(SearchDatasetsResponse)

GetDatasetRequest = _reflection.GeneratedProtocolMessageType('GetDatasetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETDATASETREQUEST,
  __module__ = 'candig.schemas.candig.metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.GetDatasetRequest)
  ))
_sym_db.RegisterMessage(GetDatasetRequest)


# @@protoc_insertion_point(module_scope)
