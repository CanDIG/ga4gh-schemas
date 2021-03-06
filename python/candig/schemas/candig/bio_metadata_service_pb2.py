# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: candig/schemas/candig/bio_metadata_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from candig.schemas.candig import bio_metadata_pb2 as candig_dot_schemas_dot_candig_dot_bio__metadata__pb2
from candig.schemas.candig import common_pb2 as candig_dot_schemas_dot_candig_dot_common__pb2
from candig.schemas.google.api import annotations_pb2 as candig_dot_schemas_dot_google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='candig/schemas/candig/bio_metadata_service.proto',
  package='candig.schemas.candig',
  syntax='proto3',
  serialized_pb=_b('\n0candig/schemas/candig/bio_metadata_service.proto\x12\x15\x63\x61ndig.schemas.candig\x1a(candig/schemas/candig/bio_metadata.proto\x1a\"candig/schemas/candig/common.proto\x1a+candig/schemas/google/api/annotations.proto\"q\n\x18SearchIndividualsRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\"-\n\x14GetIndividualRequest\x12\x15\n\rindividual_id\x18\x01 \x01(\t\"l\n\x19SearchIndividualsResponse\x12\x36\n\x0bindividuals\x18\x01 \x03(\x0b\x32!.candig.schemas.candig.Individual\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x1e\n\x0cTempoRequest\x12\x0e\n\x06valami\x18\x01 \x01(\t\"\x1f\n\rTempoResponse\x12\x0e\n\x06valami\x18\x01 \x01(\t\"y\n\x17SearchBiosamplesRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rindividual_id\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\"+\n\x13GetBiosampleRequest\x12\x14\n\x0c\x62iosample_id\x18\x01 \x01(\t\"i\n\x18SearchBiosamplesResponse\x12\x34\n\nbiosamples\x18\x01 \x03(\x0b\x32 .candig.schemas.candig.Biosample\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"e\n\x18SearchExperimentsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x62iosample_id\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\"-\n\x14GetExperimentRequest\x12\x15\n\rexperiment_id\x18\x01 \x01(\t\"l\n\x19SearchExperimentsResponse\x12\x36\n\x0b\x65xperiments\x18\x01 \x03(\x0b\x32!.candig.schemas.candig.Experiment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"b\n\x15SearchAnalysesRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x62iosample_id\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\")\n\x12GetAnalysisRequest\x12\x13\n\x0b\x61nalysis_id\x18\x01 \x01(\t\"d\n\x16SearchAnalysesResponse\x12\x31\n\x08\x61nalyses\x18\x01 \x03(\x0b\x32\x1f.candig.schemas.candig.Analysis\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xb0\t\n\x12\x42ioMetadataService\x12\x9d\x01\n\x11SearchIndividuals\x12/.candig.schemas.candig.SearchIndividualsRequest\x1a\x30.candig.schemas.candig.SearchIndividualsResponse\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v0.8.0/individuals/search:\x01*\x12\x9d\x01\n\x11SearchExperiments\x12/.candig.schemas.candig.SearchExperimentsRequest\x1a\x30.candig.schemas.candig.SearchExperimentsResponse\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v0.8.0/experiments/search:\x01*\x12\x91\x01\n\x0eSearchAnalyses\x12,.candig.schemas.candig.SearchAnalysesRequest\x1a-.candig.schemas.candig.SearchAnalysesResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/v0.8.0/analyses/search:\x01*\x12\x99\x01\n\x10SearchBiosamples\x12..candig.schemas.candig.SearchBiosamplesRequest\x1a/.candig.schemas.candig.SearchBiosamplesResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v0.8.0/biosamples/search:\x01*\x12\x8c\x01\n\rGetIndividual\x12+.candig.schemas.candig.GetIndividualRequest\x1a!.candig.schemas.candig.Individual\"+\x82\xd3\xe4\x93\x02%\x12#/v0.8.0/individuals/{individual_id}\x12\x8c\x01\n\rGetExperiment\x12+.candig.schemas.candig.GetExperimentRequest\x1a!.candig.schemas.candig.Experiment\"+\x82\xd3\xe4\x93\x02%\x12#/v0.8.0/experiments/{experiment_id}\x12\x81\x01\n\x0bGetAnalysis\x12).candig.schemas.candig.GetAnalysisRequest\x1a\x1f.candig.schemas.candig.Analysis\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v0.8.0/analyses/{analysis_id}\x12\x87\x01\n\x0cGetBiosample\x12*.candig.schemas.candig.GetBiosampleRequest\x1a .candig.schemas.candig.Biosample\")\x82\xd3\xe4\x93\x02#\x12!/v0.8.0/biosamples/{biosample_id}b\x06proto3')
  ,
  dependencies=[candig_dot_schemas_dot_candig_dot_bio__metadata__pb2.DESCRIPTOR,candig_dot_schemas_dot_candig_dot_common__pb2.DESCRIPTOR,candig_dot_schemas_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SEARCHINDIVIDUALSREQUEST = _descriptor.Descriptor(
  name='SearchIndividualsRequest',
  full_name='candig.schemas.candig.SearchIndividualsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='candig.schemas.candig.SearchIndividualsRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='candig.schemas.candig.SearchIndividualsRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='candig.schemas.candig.SearchIndividualsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='candig.schemas.candig.SearchIndividualsRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='candig.schemas.candig.SearchIndividualsRequest.type', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=198,
  serialized_end=311,
)


_GETINDIVIDUALREQUEST = _descriptor.Descriptor(
  name='GetIndividualRequest',
  full_name='candig.schemas.candig.GetIndividualRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='candig.schemas.candig.GetIndividualRequest.individual_id', index=0,
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
  serialized_start=313,
  serialized_end=358,
)


_SEARCHINDIVIDUALSRESPONSE = _descriptor.Descriptor(
  name='SearchIndividualsResponse',
  full_name='candig.schemas.candig.SearchIndividualsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='individuals', full_name='candig.schemas.candig.SearchIndividualsResponse.individuals', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='candig.schemas.candig.SearchIndividualsResponse.next_page_token', index=1,
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
  serialized_start=360,
  serialized_end=468,
)


_TEMPOREQUEST = _descriptor.Descriptor(
  name='TempoRequest',
  full_name='candig.schemas.candig.TempoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valami', full_name='candig.schemas.candig.TempoRequest.valami', index=0,
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
  serialized_start=470,
  serialized_end=500,
)


_TEMPORESPONSE = _descriptor.Descriptor(
  name='TempoResponse',
  full_name='candig.schemas.candig.TempoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valami', full_name='candig.schemas.candig.TempoResponse.valami', index=0,
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
  serialized_start=502,
  serialized_end=533,
)


_SEARCHBIOSAMPLESREQUEST = _descriptor.Descriptor(
  name='SearchBiosamplesRequest',
  full_name='candig.schemas.candig.SearchBiosamplesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='candig.schemas.candig.SearchBiosamplesRequest.dataset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='candig.schemas.candig.SearchBiosamplesRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_id', full_name='candig.schemas.candig.SearchBiosamplesRequest.individual_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='candig.schemas.candig.SearchBiosamplesRequest.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='candig.schemas.candig.SearchBiosamplesRequest.page_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=535,
  serialized_end=656,
)


_GETBIOSAMPLEREQUEST = _descriptor.Descriptor(
  name='GetBiosampleRequest',
  full_name='candig.schemas.candig.GetBiosampleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='candig.schemas.candig.GetBiosampleRequest.biosample_id', index=0,
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
  serialized_start=658,
  serialized_end=701,
)


_SEARCHBIOSAMPLESRESPONSE = _descriptor.Descriptor(
  name='SearchBiosamplesResponse',
  full_name='candig.schemas.candig.SearchBiosamplesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='biosamples', full_name='candig.schemas.candig.SearchBiosamplesResponse.biosamples', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='candig.schemas.candig.SearchBiosamplesResponse.next_page_token', index=1,
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
  serialized_start=703,
  serialized_end=808,
)


_SEARCHEXPERIMENTSREQUEST = _descriptor.Descriptor(
  name='SearchExperimentsRequest',
  full_name='candig.schemas.candig.SearchExperimentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='candig.schemas.candig.SearchExperimentsRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='candig.schemas.candig.SearchExperimentsRequest.biosample_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='candig.schemas.candig.SearchExperimentsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='candig.schemas.candig.SearchExperimentsRequest.page_token', index=3,
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
  serialized_start=810,
  serialized_end=911,
)


_GETEXPERIMENTREQUEST = _descriptor.Descriptor(
  name='GetExperimentRequest',
  full_name='candig.schemas.candig.GetExperimentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiment_id', full_name='candig.schemas.candig.GetExperimentRequest.experiment_id', index=0,
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
  serialized_start=913,
  serialized_end=958,
)


_SEARCHEXPERIMENTSRESPONSE = _descriptor.Descriptor(
  name='SearchExperimentsResponse',
  full_name='candig.schemas.candig.SearchExperimentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiments', full_name='candig.schemas.candig.SearchExperimentsResponse.experiments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='candig.schemas.candig.SearchExperimentsResponse.next_page_token', index=1,
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
  serialized_start=960,
  serialized_end=1068,
)


_SEARCHANALYSESREQUEST = _descriptor.Descriptor(
  name='SearchAnalysesRequest',
  full_name='candig.schemas.candig.SearchAnalysesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='candig.schemas.candig.SearchAnalysesRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='candig.schemas.candig.SearchAnalysesRequest.biosample_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='candig.schemas.candig.SearchAnalysesRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='candig.schemas.candig.SearchAnalysesRequest.page_token', index=3,
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
  serialized_start=1070,
  serialized_end=1168,
)


_GETANALYSISREQUEST = _descriptor.Descriptor(
  name='GetAnalysisRequest',
  full_name='candig.schemas.candig.GetAnalysisRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='analysis_id', full_name='candig.schemas.candig.GetAnalysisRequest.analysis_id', index=0,
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
  serialized_start=1170,
  serialized_end=1211,
)


_SEARCHANALYSESRESPONSE = _descriptor.Descriptor(
  name='SearchAnalysesResponse',
  full_name='candig.schemas.candig.SearchAnalysesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='analyses', full_name='candig.schemas.candig.SearchAnalysesResponse.analyses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='candig.schemas.candig.SearchAnalysesResponse.next_page_token', index=1,
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
  serialized_start=1213,
  serialized_end=1313,
)

_SEARCHINDIVIDUALSRESPONSE.fields_by_name['individuals'].message_type = candig_dot_schemas_dot_candig_dot_bio__metadata__pb2._INDIVIDUAL
_SEARCHBIOSAMPLESRESPONSE.fields_by_name['biosamples'].message_type = candig_dot_schemas_dot_candig_dot_bio__metadata__pb2._BIOSAMPLE
_SEARCHEXPERIMENTSRESPONSE.fields_by_name['experiments'].message_type = candig_dot_schemas_dot_candig_dot_common__pb2._EXPERIMENT
_SEARCHANALYSESRESPONSE.fields_by_name['analyses'].message_type = candig_dot_schemas_dot_candig_dot_common__pb2._ANALYSIS
DESCRIPTOR.message_types_by_name['SearchIndividualsRequest'] = _SEARCHINDIVIDUALSREQUEST
DESCRIPTOR.message_types_by_name['GetIndividualRequest'] = _GETINDIVIDUALREQUEST
DESCRIPTOR.message_types_by_name['SearchIndividualsResponse'] = _SEARCHINDIVIDUALSRESPONSE
DESCRIPTOR.message_types_by_name['TempoRequest'] = _TEMPOREQUEST
DESCRIPTOR.message_types_by_name['TempoResponse'] = _TEMPORESPONSE
DESCRIPTOR.message_types_by_name['SearchBiosamplesRequest'] = _SEARCHBIOSAMPLESREQUEST
DESCRIPTOR.message_types_by_name['GetBiosampleRequest'] = _GETBIOSAMPLEREQUEST
DESCRIPTOR.message_types_by_name['SearchBiosamplesResponse'] = _SEARCHBIOSAMPLESRESPONSE
DESCRIPTOR.message_types_by_name['SearchExperimentsRequest'] = _SEARCHEXPERIMENTSREQUEST
DESCRIPTOR.message_types_by_name['GetExperimentRequest'] = _GETEXPERIMENTREQUEST
DESCRIPTOR.message_types_by_name['SearchExperimentsResponse'] = _SEARCHEXPERIMENTSRESPONSE
DESCRIPTOR.message_types_by_name['SearchAnalysesRequest'] = _SEARCHANALYSESREQUEST
DESCRIPTOR.message_types_by_name['GetAnalysisRequest'] = _GETANALYSISREQUEST
DESCRIPTOR.message_types_by_name['SearchAnalysesResponse'] = _SEARCHANALYSESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchIndividualsRequest = _reflection.GeneratedProtocolMessageType('SearchIndividualsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHINDIVIDUALSREQUEST,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchIndividualsRequest)
  ))
_sym_db.RegisterMessage(SearchIndividualsRequest)

GetIndividualRequest = _reflection.GeneratedProtocolMessageType('GetIndividualRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETINDIVIDUALREQUEST,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.GetIndividualRequest)
  ))
_sym_db.RegisterMessage(GetIndividualRequest)

SearchIndividualsResponse = _reflection.GeneratedProtocolMessageType('SearchIndividualsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHINDIVIDUALSRESPONSE,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchIndividualsResponse)
  ))
_sym_db.RegisterMessage(SearchIndividualsResponse)

TempoRequest = _reflection.GeneratedProtocolMessageType('TempoRequest', (_message.Message,), dict(
  DESCRIPTOR = _TEMPOREQUEST,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.TempoRequest)
  ))
_sym_db.RegisterMessage(TempoRequest)

TempoResponse = _reflection.GeneratedProtocolMessageType('TempoResponse', (_message.Message,), dict(
  DESCRIPTOR = _TEMPORESPONSE,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.TempoResponse)
  ))
_sym_db.RegisterMessage(TempoResponse)

SearchBiosamplesRequest = _reflection.GeneratedProtocolMessageType('SearchBiosamplesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHBIOSAMPLESREQUEST,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchBiosamplesRequest)
  ))
_sym_db.RegisterMessage(SearchBiosamplesRequest)

GetBiosampleRequest = _reflection.GeneratedProtocolMessageType('GetBiosampleRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBIOSAMPLEREQUEST,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.GetBiosampleRequest)
  ))
_sym_db.RegisterMessage(GetBiosampleRequest)

SearchBiosamplesResponse = _reflection.GeneratedProtocolMessageType('SearchBiosamplesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHBIOSAMPLESRESPONSE,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchBiosamplesResponse)
  ))
_sym_db.RegisterMessage(SearchBiosamplesResponse)

SearchExperimentsRequest = _reflection.GeneratedProtocolMessageType('SearchExperimentsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHEXPERIMENTSREQUEST,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchExperimentsRequest)
  ))
_sym_db.RegisterMessage(SearchExperimentsRequest)

GetExperimentRequest = _reflection.GeneratedProtocolMessageType('GetExperimentRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETEXPERIMENTREQUEST,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.GetExperimentRequest)
  ))
_sym_db.RegisterMessage(GetExperimentRequest)

SearchExperimentsResponse = _reflection.GeneratedProtocolMessageType('SearchExperimentsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHEXPERIMENTSRESPONSE,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchExperimentsResponse)
  ))
_sym_db.RegisterMessage(SearchExperimentsResponse)

SearchAnalysesRequest = _reflection.GeneratedProtocolMessageType('SearchAnalysesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHANALYSESREQUEST,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchAnalysesRequest)
  ))
_sym_db.RegisterMessage(SearchAnalysesRequest)

GetAnalysisRequest = _reflection.GeneratedProtocolMessageType('GetAnalysisRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETANALYSISREQUEST,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.GetAnalysisRequest)
  ))
_sym_db.RegisterMessage(GetAnalysisRequest)

SearchAnalysesResponse = _reflection.GeneratedProtocolMessageType('SearchAnalysesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHANALYSESRESPONSE,
  __module__ = 'candig.schemas.candig.bio_metadata_service_pb2'
  # @@protoc_insertion_point(class_scope:candig.schemas.candig.SearchAnalysesResponse)
  ))
_sym_db.RegisterMessage(SearchAnalysesResponse)


# @@protoc_insertion_point(module_scope)
