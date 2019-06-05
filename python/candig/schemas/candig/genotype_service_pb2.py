# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: candig/schemas/candig/genotype_service.proto

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


from candig.schemas.candig import variants_pb2 as candig_dot_schemas_dot_candig_dot_variants__pb2
from candig.schemas.google.api import annotations_pb2 as candig_dot_schemas_dot_google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='candig/schemas/candig/genotype_service.proto',
  package='candig.schemas.candig',
  syntax='proto3',
  serialized_pb=_b('\n,candig/schemas/candig/genotype_service.proto\x12\x15\x63\x61ndig.schemas.candig\x1a$candig/schemas/candig/variants.proto\x1a+candig/schemas/google/api/annotations.proto\"m\n\x0eGenotypeMatrix\x12\x14\n\x0cnindividuals\x18\x01 \x01(\r\x12\x11\n\tnvariants\x18\x02 \x01(\r\x12\x32\n\tgenotypes\x18\x03 \x03(\x0e\x32\x1f.candig.schemas.candig.Genotype\"\xa1\x01\n\x16SearchGenotypesRequest\x12\x16\n\x0evariant_set_id\x18\x01 \x01(\t\x12\x14\n\x0c\x63\x61ll_set_ids\x18\x02 \x03(\t\x12\x16\n\x0ereference_name\x18\x03 \x01(\t\x12\r\n\x05start\x18\x04 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x05 \x01(\x03\x12\x11\n\tpage_size\x18\x06 \x01(\x05\x12\x12\n\npage_token\x18\x07 \x01(\t\"\xb4\x01\n\x17SearchGenotypesResponse\x12\x30\n\x08variants\x18\x01 \x03(\x0b\x32\x1e.candig.schemas.candig.Variant\x12\x14\n\x0c\x63\x61ll_set_ids\x18\x02 \x03(\t\x12\x38\n\tgenotypes\x18\x03 \x01(\x0b\x32%.candig.schemas.candig.GenotypeMatrix\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t*\x83\x01\n\x08Genotype\x12\x12\n\x0eHOMOZYGOUS_REF\x10\x00\x12\x14\n\x10HETEROZYGOUS_ALT\x10\x01\x12\x12\n\x0eHOMOZYGOUS_ALT\x10\x02\x12\x12\n\x0eHEMIZYGOUS_REF\x10\x03\x12\x12\n\x0eHEMIZYGOUS_ALT\x10\x04\x12\t\n\x05OTHER\x10\x05\x12\x06\n\x02NA\x10\x06\x32\xaa\x01\n\x10GenotypesService\x12\x95\x01\n\x0fSearchGenotypes\x12-.candig.schemas.candig.SearchGenotypesRequest\x1a..candig.schemas.candig.SearchGenotypesResponse\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/v0.8.0/genotypes/search:\x01*b\x06proto3')
  ,
  dependencies=[candig_dot_schemas_dot_candig_dot_variants__pb2.DESCRIPTOR,candig_dot_schemas_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_GENOTYPE = _descriptor.EnumDescriptor(
  name='Genotype',
  full_name='candig.schemas.candig.Genotype',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HOMOZYGOUS_REF', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HETEROZYGOUS_ALT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOMOZYGOUS_ALT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEMIZYGOUS_REF', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEMIZYGOUS_ALT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NA', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=613,
  serialized_end=744,
)
_sym_db.RegisterEnumDescriptor(_GENOTYPE)

Genotype = enum_type_wrapper.EnumTypeWrapper(_GENOTYPE)
HOMOZYGOUS_REF = 0
HETEROZYGOUS_ALT = 1
HOMOZYGOUS_ALT = 2
HEMIZYGOUS_REF = 3
HEMIZYGOUS_ALT = 4
OTHER = 5
NA = 6



_GENOTYPEMATRIX = _descriptor.Descriptor(
  name='GenotypeMatrix',
  full_name='candig.schemas.candig.GenotypeMatrix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nindividuals', full_name='candig.schemas.candig.GenotypeMatrix.nindividuals', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nvariants', full_name='candig.schemas.candig.GenotypeMatrix.nvariants', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genotypes', full_name='candig.schemas.candig.GenotypeMatrix.genotypes', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_end=263,
)


_SEARCHGENOTYPESREQUEST = _descriptor.Descriptor(
  name='SearchGenotypesRequest',
  full_name='candig.schemas.candig.SearchGenotypesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variant_set_id', full_name='candig.schemas.candig.SearchGenotypesRequest.variant_set_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='call_set_ids', full_name='candig.schemas.candig.SearchGenotypesRequest.call_set_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='candig.schemas.candig.SearchGenotypesRequest.reference_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='candig.schemas.candig.SearchGenotypesRequest.start', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='candig.schemas.candig.SearchGenotypesRequest.end', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='candig.schemas.candig.SearchGenotypesRequest.page_size', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='candig.schemas.candig.SearchGenotypesRequest.page_token', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=266,
  serialized_end=427,
)


_SEARCHGENOTYPESRESPONSE = _descriptor.Descriptor(
  name='SearchGenotypesResponse',
  full_name='candig.schemas.candig.SearchGenotypesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variants', full_name='candig.schemas.candig.SearchGenotypesResponse.variants', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='call_set_ids', full_name='candig.schemas.candig.SearchGenotypesResponse.call_set_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genotypes', full_name='candig.schemas.candig.SearchGenotypesResponse.genotypes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='candig.schemas.candig.SearchGenotypesResponse.next_page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=430,
  serialized_end=610,
)

_GENOTYPEMATRIX.fields_by_name['genotypes'].enum_type = _GENOTYPE
_SEARCHGENOTYPESRESPONSE.fields_by_name['variants'].message_type = candig_dot_schemas_dot_candig_dot_variants__pb2._VARIANT
_SEARCHGENOTYPESRESPONSE.fields_by_name['genotypes'].message_type = _GENOTYPEMATRIX
DESCRIPTOR.message_types_by_name['GenotypeMatrix'] = _GENOTYPEMATRIX
DESCRIPTOR.message_types_by_name['SearchGenotypesRequest'] = _SEARCHGENOTYPESREQUEST
DESCRIPTOR.message_types_by_name['SearchGenotypesResponse'] = _SEARCHGENOTYPESRESPONSE
DESCRIPTOR.enum_types_by_name['Genotype'] = _GENOTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenotypeMatrix = _reflection.GeneratedProtocolMessageType('GenotypeMatrix', (_message.Message,), dict(
  DESCRIPTOR = _GENOTYPEMATRIX,
  __module__ = 'candig.schemas.candig.genotype_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.GenotypeMatrix)
  ))
_sym_db.RegisterMessage(GenotypeMatrix)

SearchGenotypesRequest = _reflection.GeneratedProtocolMessageType('SearchGenotypesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHGENOTYPESREQUEST,
  __module__ = 'candig.schemas.candig.genotype_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchGenotypesRequest)
  ))
_sym_db.RegisterMessage(SearchGenotypesRequest)

SearchGenotypesResponse = _reflection.GeneratedProtocolMessageType('SearchGenotypesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHGENOTYPESRESPONSE,
  __module__ = 'candig.schemas.candig.genotype_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchGenotypesResponse)
  ))
_sym_db.RegisterMessage(SearchGenotypesResponse)


# @@protoc_insertion_point(module_scope)
