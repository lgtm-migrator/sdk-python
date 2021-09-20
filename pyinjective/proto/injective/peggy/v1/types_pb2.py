# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: injective/peggy/v1/types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='injective/peggy/v1/types.proto',
  package='injective.peggy.v1',
  syntax='proto3',
  serialized_options=b'ZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1einjective/peggy/v1/types.proto\x12\x12injective.peggy.v1\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\":\n\x0f\x42ridgeValidator\x12\r\n\x05power\x18\x01 \x01(\x04\x12\x18\n\x10\x65thereum_address\x18\x02 \x01(\t\"\xba\x01\n\x06Valset\x12\r\n\x05nonce\x18\x01 \x01(\x04\x12\x34\n\x07members\x18\x02 \x03(\x0b\x32#.injective.peggy.v1.BridgeValidator\x12\x0e\n\x06height\x18\x03 \x01(\x04\x12\x45\n\rreward_amount\x18\x04 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12\x14\n\x0creward_token\x18\x05 \x01(\t\"]\n\x1fLastObservedEthereumBlockHeight\x12\x1b\n\x13\x63osmos_block_height\x18\x01 \x01(\x04\x12\x1d\n\x15\x65thereum_block_height\x18\x02 \x01(\x04\"M\n\x0eLastClaimEvent\x12\x1c\n\x14\x65thereum_event_nonce\x18\x01 \x01(\x04\x12\x1d\n\x15\x65thereum_event_height\x18\x02 \x01(\x04\",\n\x0c\x45RC20ToDenom\x12\r\n\x05\x65rc20\x18\x01 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\tBMZKgithub.com/InjectiveLabs/injective-core/injective-chain/modules/peggy/typesb\x06proto3'
  ,
  dependencies=[cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,])




_BRIDGEVALIDATOR = _descriptor.Descriptor(
  name='BridgeValidator',
  full_name='injective.peggy.v1.BridgeValidator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='power', full_name='injective.peggy.v1.BridgeValidator.power', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ethereum_address', full_name='injective.peggy.v1.BridgeValidator.ethereum_address', index=1,
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
  serialized_start=108,
  serialized_end=166,
)


_VALSET = _descriptor.Descriptor(
  name='Valset',
  full_name='injective.peggy.v1.Valset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='injective.peggy.v1.Valset.nonce', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='members', full_name='injective.peggy.v1.Valset.members', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='injective.peggy.v1.Valset.height', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reward_amount', full_name='injective.peggy.v1.Valset.reward_amount', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reward_token', full_name='injective.peggy.v1.Valset.reward_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=169,
  serialized_end=355,
)


_LASTOBSERVEDETHEREUMBLOCKHEIGHT = _descriptor.Descriptor(
  name='LastObservedEthereumBlockHeight',
  full_name='injective.peggy.v1.LastObservedEthereumBlockHeight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cosmos_block_height', full_name='injective.peggy.v1.LastObservedEthereumBlockHeight.cosmos_block_height', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ethereum_block_height', full_name='injective.peggy.v1.LastObservedEthereumBlockHeight.ethereum_block_height', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=357,
  serialized_end=450,
)


_LASTCLAIMEVENT = _descriptor.Descriptor(
  name='LastClaimEvent',
  full_name='injective.peggy.v1.LastClaimEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ethereum_event_nonce', full_name='injective.peggy.v1.LastClaimEvent.ethereum_event_nonce', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ethereum_event_height', full_name='injective.peggy.v1.LastClaimEvent.ethereum_event_height', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=452,
  serialized_end=529,
)


_ERC20TODENOM = _descriptor.Descriptor(
  name='ERC20ToDenom',
  full_name='injective.peggy.v1.ERC20ToDenom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='erc20', full_name='injective.peggy.v1.ERC20ToDenom.erc20', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='denom', full_name='injective.peggy.v1.ERC20ToDenom.denom', index=1,
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
  serialized_start=531,
  serialized_end=575,
)

_VALSET.fields_by_name['members'].message_type = _BRIDGEVALIDATOR
DESCRIPTOR.message_types_by_name['BridgeValidator'] = _BRIDGEVALIDATOR
DESCRIPTOR.message_types_by_name['Valset'] = _VALSET
DESCRIPTOR.message_types_by_name['LastObservedEthereumBlockHeight'] = _LASTOBSERVEDETHEREUMBLOCKHEIGHT
DESCRIPTOR.message_types_by_name['LastClaimEvent'] = _LASTCLAIMEVENT
DESCRIPTOR.message_types_by_name['ERC20ToDenom'] = _ERC20TODENOM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BridgeValidator = _reflection.GeneratedProtocolMessageType('BridgeValidator', (_message.Message,), {
  'DESCRIPTOR' : _BRIDGEVALIDATOR,
  '__module__' : 'injective.peggy.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:injective.peggy.v1.BridgeValidator)
  })
_sym_db.RegisterMessage(BridgeValidator)

Valset = _reflection.GeneratedProtocolMessageType('Valset', (_message.Message,), {
  'DESCRIPTOR' : _VALSET,
  '__module__' : 'injective.peggy.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:injective.peggy.v1.Valset)
  })
_sym_db.RegisterMessage(Valset)

LastObservedEthereumBlockHeight = _reflection.GeneratedProtocolMessageType('LastObservedEthereumBlockHeight', (_message.Message,), {
  'DESCRIPTOR' : _LASTOBSERVEDETHEREUMBLOCKHEIGHT,
  '__module__' : 'injective.peggy.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:injective.peggy.v1.LastObservedEthereumBlockHeight)
  })
_sym_db.RegisterMessage(LastObservedEthereumBlockHeight)

LastClaimEvent = _reflection.GeneratedProtocolMessageType('LastClaimEvent', (_message.Message,), {
  'DESCRIPTOR' : _LASTCLAIMEVENT,
  '__module__' : 'injective.peggy.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:injective.peggy.v1.LastClaimEvent)
  })
_sym_db.RegisterMessage(LastClaimEvent)

ERC20ToDenom = _reflection.GeneratedProtocolMessageType('ERC20ToDenom', (_message.Message,), {
  'DESCRIPTOR' : _ERC20TODENOM,
  '__module__' : 'injective.peggy.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:injective.peggy.v1.ERC20ToDenom)
  })
_sym_db.RegisterMessage(ERC20ToDenom)


DESCRIPTOR._options = None
_VALSET.fields_by_name['reward_amount']._options = None
# @@protoc_insertion_point(module_scope)