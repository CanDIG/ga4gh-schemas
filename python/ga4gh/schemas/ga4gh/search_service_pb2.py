# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/schemas/ga4gh/search_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh.schemas.google.api import annotations_pb2 as ga4gh_dot_schemas_dot_google_dot_api_dot_annotations__pb2
from ga4gh.schemas.ga4gh import clinical_metadata_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2
from ga4gh.schemas.ga4gh import variants_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_variants__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/schemas/ga4gh/search_service.proto',
  package='ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n(ga4gh/schemas/ga4gh/search_service.proto\x12\x05ga4gh\x1a*ga4gh/schemas/google/api/annotations.proto\x1a+ga4gh/schemas/ga4gh/clinical_metadata.proto\x1a\"ga4gh/schemas/ga4gh/variants.proto\"8\n\x06\x46ilter\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x10\n\x08operator\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"P\n\tComponent\x12\x14\n\x0c\x63omponent_id\x18\x01 \x01(\t\x12\r\n\x05table\x18\x02 \x01(\t\x12\x1e\n\x07\x66ilters\x18\x03 \x03(\x0b\x32\r.ga4gh.Filter\"N\n\x07Operand\x12\x16\n\x0c\x63omponent_id\x18\x01 \x01(\tH\x00\x12\x1e\n\x06nested\x18\x02 \x01(\x0b\x32\x0c.ga4gh.LogicH\x00\x42\x0b\n\tcomponent\"+\n\x08Operands\x12\x1f\n\x07operand\x18\x01 \x03(\x0b\x32\x0e.ga4gh.Operand\"O\n\x05Logic\x12\x1e\n\x03\x61nd\x18\x01 \x01(\x0b\x32\x0f.ga4gh.OperandsH\x00\x12\x1d\n\x02or\x18\x02 \x01(\x0b\x32\x0f.ga4gh.OperandsH\x00\x42\x07\n\x05\x41ndor\"&\n\x06Result\x12\r\n\x05table\x18\x01 \x01(\t\x12\r\n\x05\x66ield\x18\x02 \x03(\t\"\xad\x01\n\x12SearchQueryRequest\x12\x1b\n\x05logic\x18\x01 \x01(\x0b\x32\x0c.ga4gh.Logic\x12$\n\ncomponents\x18\x02 \x03(\x0b\x32\x10.ga4gh.Component\x12\x1e\n\x07results\x18\x03 \x03(\x0b\x32\r.ga4gh.Result\x12\r\n\x05limit\x18\x04 \x01(\x05\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t\"\x9f\x03\n\x13SearchQueryResponse\x12 \n\x08patients\x18\x01 \x03(\x0b\x32\x0e.ga4gh.Patient\x12&\n\x0b\x65nrollments\x18\x02 \x03(\x0b\x32\x11.ga4gh.Enrollment\x12 \n\x08\x63onsents\x18\x03 \x03(\x0b\x32\x0e.ga4gh.Consent\x12#\n\tdiagnoses\x18\x04 \x03(\x0b\x32\x10.ga4gh.Diagnosis\x12\x1e\n\x07samples\x18\x05 \x03(\x0b\x32\r.ga4gh.Sample\x12$\n\ntreatments\x18\x06 \x03(\x0b\x32\x10.ga4gh.Treatment\x12 \n\x08outcomes\x18\x07 \x03(\x0b\x32\x0e.ga4gh.Outcome\x12*\n\rcomplications\x18\x08 \x03(\x0b\x32\x13.ga4gh.Complication\x12(\n\x0ctumourboards\x18\t \x03(\x0b\x32\x12.ga4gh.Tumourboard\x12 \n\x08variants\x18\n \x03(\x0b\x32\x0e.ga4gh.Variant\x12\x17\n\x0fnext_page_token\x18\x0b \x01(\t2o\n\rSearchService\x12^\n\x07GetItem\x12\x19.ga4gh.SearchQueryRequest\x1a\x1a.ga4gh.SearchQueryResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v0.6.0a10/search:\x01*b\x06proto3')
  ,
  dependencies=[ga4gh_dot_schemas_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2.DESCRIPTOR,ga4gh_dot_schemas_dot_ga4gh_dot_variants__pb2.DESCRIPTOR,])




_FILTER = _descriptor.Descriptor(
  name='Filter',
  full_name='ga4gh.Filter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='ga4gh.Filter.field', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operator', full_name='ga4gh.Filter.operator', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='ga4gh.Filter.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=176,
  serialized_end=232,
)


_COMPONENT = _descriptor.Descriptor(
  name='Component',
  full_name='ga4gh.Component',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='component_id', full_name='ga4gh.Component.component_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table', full_name='ga4gh.Component.table', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filters', full_name='ga4gh.Component.filters', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=234,
  serialized_end=314,
)


_OPERAND = _descriptor.Descriptor(
  name='Operand',
  full_name='ga4gh.Operand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='component_id', full_name='ga4gh.Operand.component_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nested', full_name='ga4gh.Operand.nested', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='component', full_name='ga4gh.Operand.component',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=316,
  serialized_end=394,
)


_OPERANDS = _descriptor.Descriptor(
  name='Operands',
  full_name='ga4gh.Operands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operand', full_name='ga4gh.Operands.operand', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=396,
  serialized_end=439,
)


_LOGIC = _descriptor.Descriptor(
  name='Logic',
  full_name='ga4gh.Logic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='and', full_name='ga4gh.Logic.and', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='or', full_name='ga4gh.Logic.or', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='Andor', full_name='ga4gh.Logic.Andor',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=441,
  serialized_end=520,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='ga4gh.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table', full_name='ga4gh.Result.table', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field', full_name='ga4gh.Result.field', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=522,
  serialized_end=560,
)


_SEARCHQUERYREQUEST = _descriptor.Descriptor(
  name='SearchQueryRequest',
  full_name='ga4gh.SearchQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='logic', full_name='ga4gh.SearchQueryRequest.logic', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='components', full_name='ga4gh.SearchQueryRequest.components', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='results', full_name='ga4gh.SearchQueryRequest.results', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='limit', full_name='ga4gh.SearchQueryRequest.limit', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ga4gh.SearchQueryRequest.page_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='ga4gh.SearchQueryRequest.page_token', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=563,
  serialized_end=736,
)


_SEARCHQUERYRESPONSE = _descriptor.Descriptor(
  name='SearchQueryResponse',
  full_name='ga4gh.SearchQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='patients', full_name='ga4gh.SearchQueryResponse.patients', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enrollments', full_name='ga4gh.SearchQueryResponse.enrollments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consents', full_name='ga4gh.SearchQueryResponse.consents', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diagnoses', full_name='ga4gh.SearchQueryResponse.diagnoses', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='samples', full_name='ga4gh.SearchQueryResponse.samples', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='treatments', full_name='ga4gh.SearchQueryResponse.treatments', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outcomes', full_name='ga4gh.SearchQueryResponse.outcomes', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='complications', full_name='ga4gh.SearchQueryResponse.complications', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tumourboards', full_name='ga4gh.SearchQueryResponse.tumourboards', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variants', full_name='ga4gh.SearchQueryResponse.variants', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='ga4gh.SearchQueryResponse.next_page_token', index=10,
      number=11, type=9, cpp_type=9, label=1,
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
  serialized_start=739,
  serialized_end=1154,
)

_COMPONENT.fields_by_name['filters'].message_type = _FILTER
_OPERAND.fields_by_name['nested'].message_type = _LOGIC
_OPERAND.oneofs_by_name['component'].fields.append(
  _OPERAND.fields_by_name['component_id'])
_OPERAND.fields_by_name['component_id'].containing_oneof = _OPERAND.oneofs_by_name['component']
_OPERAND.oneofs_by_name['component'].fields.append(
  _OPERAND.fields_by_name['nested'])
_OPERAND.fields_by_name['nested'].containing_oneof = _OPERAND.oneofs_by_name['component']
_OPERANDS.fields_by_name['operand'].message_type = _OPERAND
_LOGIC.fields_by_name['and'].message_type = _OPERANDS
_LOGIC.fields_by_name['or'].message_type = _OPERANDS
_LOGIC.oneofs_by_name['Andor'].fields.append(
  _LOGIC.fields_by_name['and'])
_LOGIC.fields_by_name['and'].containing_oneof = _LOGIC.oneofs_by_name['Andor']
_LOGIC.oneofs_by_name['Andor'].fields.append(
  _LOGIC.fields_by_name['or'])
_LOGIC.fields_by_name['or'].containing_oneof = _LOGIC.oneofs_by_name['Andor']
_SEARCHQUERYREQUEST.fields_by_name['logic'].message_type = _LOGIC
_SEARCHQUERYREQUEST.fields_by_name['components'].message_type = _COMPONENT
_SEARCHQUERYREQUEST.fields_by_name['results'].message_type = _RESULT
_SEARCHQUERYRESPONSE.fields_by_name['patients'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._PATIENT
_SEARCHQUERYRESPONSE.fields_by_name['enrollments'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._ENROLLMENT
_SEARCHQUERYRESPONSE.fields_by_name['consents'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._CONSENT
_SEARCHQUERYRESPONSE.fields_by_name['diagnoses'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._DIAGNOSIS
_SEARCHQUERYRESPONSE.fields_by_name['samples'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._SAMPLE
_SEARCHQUERYRESPONSE.fields_by_name['treatments'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._TREATMENT
_SEARCHQUERYRESPONSE.fields_by_name['outcomes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._OUTCOME
_SEARCHQUERYRESPONSE.fields_by_name['complications'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._COMPLICATION
_SEARCHQUERYRESPONSE.fields_by_name['tumourboards'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_clinical__metadata__pb2._TUMOURBOARD
_SEARCHQUERYRESPONSE.fields_by_name['variants'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_variants__pb2._VARIANT
DESCRIPTOR.message_types_by_name['Filter'] = _FILTER
DESCRIPTOR.message_types_by_name['Component'] = _COMPONENT
DESCRIPTOR.message_types_by_name['Operand'] = _OPERAND
DESCRIPTOR.message_types_by_name['Operands'] = _OPERANDS
DESCRIPTOR.message_types_by_name['Logic'] = _LOGIC
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['SearchQueryRequest'] = _SEARCHQUERYREQUEST
DESCRIPTOR.message_types_by_name['SearchQueryResponse'] = _SEARCHQUERYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Filter = _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), dict(
  DESCRIPTOR = _FILTER,
  __module__ = 'ga4gh.schemas.ga4gh.search_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.Filter)
  ))
_sym_db.RegisterMessage(Filter)

Component = _reflection.GeneratedProtocolMessageType('Component', (_message.Message,), dict(
  DESCRIPTOR = _COMPONENT,
  __module__ = 'ga4gh.schemas.ga4gh.search_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.Component)
  ))
_sym_db.RegisterMessage(Component)

Operand = _reflection.GeneratedProtocolMessageType('Operand', (_message.Message,), dict(
  DESCRIPTOR = _OPERAND,
  __module__ = 'ga4gh.schemas.ga4gh.search_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.Operand)
  ))
_sym_db.RegisterMessage(Operand)

Operands = _reflection.GeneratedProtocolMessageType('Operands', (_message.Message,), dict(
  DESCRIPTOR = _OPERANDS,
  __module__ = 'ga4gh.schemas.ga4gh.search_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.Operands)
  ))
_sym_db.RegisterMessage(Operands)

Logic = _reflection.GeneratedProtocolMessageType('Logic', (_message.Message,), dict(
  DESCRIPTOR = _LOGIC,
  __module__ = 'ga4gh.schemas.ga4gh.search_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.Logic)
  ))
_sym_db.RegisterMessage(Logic)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'ga4gh.schemas.ga4gh.search_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.Result)
  ))
_sym_db.RegisterMessage(Result)

SearchQueryRequest = _reflection.GeneratedProtocolMessageType('SearchQueryRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHQUERYREQUEST,
  __module__ = 'ga4gh.schemas.ga4gh.search_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchQueryRequest)
  ))
_sym_db.RegisterMessage(SearchQueryRequest)

SearchQueryResponse = _reflection.GeneratedProtocolMessageType('SearchQueryResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHQUERYRESPONSE,
  __module__ = 'ga4gh.schemas.ga4gh.search_service_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.SearchQueryResponse)
  ))
_sym_db.RegisterMessage(SearchQueryResponse)



_SEARCHSERVICE = _descriptor.ServiceDescriptor(
  name='SearchService',
  full_name='ga4gh.SearchService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1156,
  serialized_end=1267,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetItem',
    full_name='ga4gh.SearchService.GetItem',
    index=0,
    containing_service=None,
    input_type=_SEARCHQUERYREQUEST,
    output_type=_SEARCHQUERYRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\026\"\021/v0.6.0a10/search:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_SEARCHSERVICE)

DESCRIPTOR.services_by_name['SearchService'] = _SEARCHSERVICE

# @@protoc_insertion_point(module_scope)
