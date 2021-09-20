# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/batch.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from injective.peggy.v1 import attestation_pb2 as injective_dot_peggy_dot_v1_dot_attestation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/peggy/v1/batch.proto',
  package='injective.peggy.v1',
  syntax='proto3',
  serialized_options=b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1einjective/peggy/v1/batch.proto\x12\x12injective.peggy.v1\x1a$injective/peggy/v1/attestation.proto\"\xa2\x01\n\x0fOutgoingTxBatch\x12\x13\n\x0b\x62\x61tch_nonce\x18\x01 \x01(\x04\x12\x15\n\rbatch_timeout\x18\x02 \x01(\x04\x12<\n\x0ctransactions\x18\x03 \x03(\x0b\x32&.injective.peggy.v1.OutgoingTransferTx\x12\x16\n\x0etoken_contract\x18\x04 \x01(\t\x12\r\n\x05\x62lock\x18\x05 \x01(\x04\"\xae\x01\n\x12OutgoingTransferTx\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12\x14\n\x0c\x64\x65st_address\x18\x03 \x01(\t\x12\x33\n\x0b\x65rc20_token\x18\x04 \x01(\x0b\x32\x1e.injective.peggy.v1.ERC20Token\x12\x31\n\terc20_fee\x18\x05 \x01(\x0b\x32\x1e.injective.peggy.v1.ERC20TokenBMZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/typesb\x06proto3'
  ,
  dependencies=[injective_dot_peggy_dot_v1_dot_attestation__pb2.DESCRIPTOR,])




_OUTGOINGTXBATCH = _descriptor.Descriptor(
  name='OutgoingTxBatch',
  full_name='injective.peggy.v1.OutgoingTxBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='batch_nonce', full_name='injective.peggy.v1.OutgoingTxBatch.batch_nonce', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_timeout', full_name='injective.peggy.v1.OutgoingTxBatch.batch_timeout', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transactions', full_name='injective.peggy.v1.OutgoingTxBatch.transactions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token_contract', full_name='injective.peggy.v1.OutgoingTxBatch.token_contract', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block', full_name='injective.peggy.v1.OutgoingTxBatch.block', index=4,
      number=5, type=4, cpp_type=4, label=1,
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
  serialized_start=93,
  serialized_end=255,
)


_OUTGOINGTRANSFERTX = _descriptor.Descriptor(
  name='OutgoingTransferTx',
  full_name='injective.peggy.v1.OutgoingTransferTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='injective.peggy.v1.OutgoingTransferTx.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender', full_name='injective.peggy.v1.OutgoingTransferTx.sender', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dest_address', full_name='injective.peggy.v1.OutgoingTransferTx.dest_address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='erc20_token', full_name='injective.peggy.v1.OutgoingTransferTx.erc20_token', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='erc20_fee', full_name='injective.peggy.v1.OutgoingTransferTx.erc20_fee', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=258,
  serialized_end=432,
)

_OUTGOINGTXBATCH.fields_by_name['transactions'].message_type = _OUTGOINGTRANSFERTX
_OUTGOINGTRANSFERTX.fields_by_name['erc20_token'].message_type = injective_dot_peggy_dot_v1_dot_attestation__pb2._ERC20TOKEN
_OUTGOINGTRANSFERTX.fields_by_name['erc20_fee'].message_type = injective_dot_peggy_dot_v1_dot_attestation__pb2._ERC20TOKEN
DESCRIPTOR.message_types_by_name['OutgoingTxBatch'] = _OUTGOINGTXBATCH
DESCRIPTOR.message_types_by_name['OutgoingTransferTx'] = _OUTGOINGTRANSFERTX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OutgoingTxBatch = _reflection.GeneratedProtocolMessageType('OutgoingTxBatch', (_message.Message,), {
  'DESCRIPTOR' : _OUTGOINGTXBATCH,
  '__module__' : 'injective.peggy.v1.batch_pb2'
  # @@protoc_insertion_point(class_scope:injective.peggy.v1.OutgoingTxBatch)
  })
_sym_db.RegisterMessage(OutgoingTxBatch)

OutgoingTransferTx = _reflection.GeneratedProtocolMessageType('OutgoingTransferTx', (_message.Message,), {
  'DESCRIPTOR' : _OUTGOINGTRANSFERTX,
  '__module__' : 'injective.peggy.v1.batch_pb2'
  # @@protoc_insertion_point(class_scope:injective.peggy.v1.OutgoingTransferTx)
  })
_sym_db.RegisterMessage(OutgoingTransferTx)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)