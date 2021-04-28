# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: circuit_computation_result.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import float3_pb2 as float3__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="circuit_computation_result.proto",
    package="",
    syntax="proto3",
    serialized_options=b"\252\002\010Protobuf",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n circuit_computation_result.proto\x1a\x0c\x66loat3.proto"\xfd\x01\n\x18\x43ircuitComputationResult\x12\x12\n\ncircuit_id\x18\x01 \x01(\t\x12\x14\n\x0c\x63ircuit_hash\x18\x02 \x01(\t\x12\x43\n\x1etime_block_computation_results\x18\x03 \x03(\x0b\x32\x1b.TimeBlockComputationResult\x12\x38\n\x18measurement_gate_results\x18\x04 \x03(\x0b\x32\x16.MeasurementGateResult\x12\x38\n\x18time_block_error_results\x18\x05 \x03(\x0b\x32\x16.TimeBlockErrorResults"n\n\x1aTimeBlockComputationResult\x12\x15\n\rtime_block_id\x18\x01 \x01(\t\x12\x12\n\namplitudes\x18\x02 \x03(\x02\x12\x0e\n\x06phases\x18\x03 \x03(\x02\x12\x15\n\rentanglements\x18\x04 \x03(\x02"9\n\x15MeasurementGateResult\x12\x0f\n\x07gate_id\x18\x01 \x01(\t\x12\x0f\n\x07outcome\x18\x02 \x01(\x08"\xae\x03\n\x15TimeBlockErrorResults\x12J\n\x13qubit_error_results\x18\x01 \x03(\x0b\x32-.TimeBlockErrorResults.QubitErrorResultsEntry\x1a\xe5\x01\n\x10QubitErrorResult\x12\x0b\n\x01x\x18\x01 \x01(\x08H\x00\x12\x0b\n\x01y\x18\x02 \x01(\x08H\x00\x12\x0b\n\x01z\x18\x03 \x01(\x08H\x00\x12\x46\n\tarb_error\x18\x04 \x01(\x0b\x32\x31.TimeBlockErrorResults.QubitErrorResult.ArbParamsH\x00\x1aT\n\tArbParams\x12\x19\n\x08xyz_axes\x18\x01 \x01(\x0b\x32\x07.Float3\x12\x16\n\x0erotation_angle\x18\x02 \x01(\x02\x12\x14\n\x0cglobal_phase\x18\x03 \x01(\x02\x42\x0c\n\nerror_type\x1a\x61\n\x16QubitErrorResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.TimeBlockErrorResults.QubitErrorResult:\x02\x38\x01\x42\x0b\xaa\x02\x08Protobufb\x06proto3',
    dependencies=[
        float3__pb2.DESCRIPTOR,
    ],
)


_CIRCUITCOMPUTATIONRESULT = _descriptor.Descriptor(
    name="CircuitComputationResult",
    full_name="CircuitComputationResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="circuit_id",
            full_name="CircuitComputationResult.circuit_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="circuit_hash",
            full_name="CircuitComputationResult.circuit_hash",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="time_block_computation_results",
            full_name="CircuitComputationResult.time_block_computation_results",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="measurement_gate_results",
            full_name="CircuitComputationResult.measurement_gate_results",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="time_block_error_results",
            full_name="CircuitComputationResult.time_block_error_results",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=51,
    serialized_end=304,
)


_TIMEBLOCKCOMPUTATIONRESULT = _descriptor.Descriptor(
    name="TimeBlockComputationResult",
    full_name="TimeBlockComputationResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="time_block_id",
            full_name="TimeBlockComputationResult.time_block_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="amplitudes",
            full_name="TimeBlockComputationResult.amplitudes",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="phases",
            full_name="TimeBlockComputationResult.phases",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="entanglements",
            full_name="TimeBlockComputationResult.entanglements",
            index=3,
            number=4,
            type=2,
            cpp_type=6,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=306,
    serialized_end=416,
)


_MEASUREMENTGATERESULT = _descriptor.Descriptor(
    name="MeasurementGateResult",
    full_name="MeasurementGateResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="gate_id",
            full_name="MeasurementGateResult.gate_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="outcome",
            full_name="MeasurementGateResult.outcome",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=418,
    serialized_end=475,
)


_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT_ARBPARAMS = _descriptor.Descriptor(
    name="ArbParams",
    full_name="TimeBlockErrorResults.QubitErrorResult.ArbParams",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="xyz_axes",
            full_name="TimeBlockErrorResults.QubitErrorResult.ArbParams.xyz_axes",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="rotation_angle",
            full_name="TimeBlockErrorResults.QubitErrorResult.ArbParams.rotation_angle",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="global_phase",
            full_name="TimeBlockErrorResults.QubitErrorResult.ArbParams.global_phase",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=711,
    serialized_end=795,
)

_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT = _descriptor.Descriptor(
    name="QubitErrorResult",
    full_name="TimeBlockErrorResults.QubitErrorResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="x",
            full_name="TimeBlockErrorResults.QubitErrorResult.x",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="y",
            full_name="TimeBlockErrorResults.QubitErrorResult.y",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="z",
            full_name="TimeBlockErrorResults.QubitErrorResult.z",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="arb_error",
            full_name="TimeBlockErrorResults.QubitErrorResult.arb_error",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT_ARBPARAMS,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="error_type",
            full_name="TimeBlockErrorResults.QubitErrorResult.error_type",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=580,
    serialized_end=809,
)

_TIMEBLOCKERRORRESULTS_QUBITERRORRESULTSENTRY = _descriptor.Descriptor(
    name="QubitErrorResultsEntry",
    full_name="TimeBlockErrorResults.QubitErrorResultsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="TimeBlockErrorResults.QubitErrorResultsEntry.key",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="TimeBlockErrorResults.QubitErrorResultsEntry.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=811,
    serialized_end=908,
)

_TIMEBLOCKERRORRESULTS = _descriptor.Descriptor(
    name="TimeBlockErrorResults",
    full_name="TimeBlockErrorResults",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="qubit_error_results",
            full_name="TimeBlockErrorResults.qubit_error_results",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT,
        _TIMEBLOCKERRORRESULTS_QUBITERRORRESULTSENTRY,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=478,
    serialized_end=908,
)

_CIRCUITCOMPUTATIONRESULT.fields_by_name[
    "time_block_computation_results"
].message_type = _TIMEBLOCKCOMPUTATIONRESULT
_CIRCUITCOMPUTATIONRESULT.fields_by_name[
    "measurement_gate_results"
].message_type = _MEASUREMENTGATERESULT
_CIRCUITCOMPUTATIONRESULT.fields_by_name[
    "time_block_error_results"
].message_type = _TIMEBLOCKERRORRESULTS
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT_ARBPARAMS.fields_by_name[
    "xyz_axes"
].message_type = float3__pb2._FLOAT3
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT_ARBPARAMS.containing_type = (
    _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT
)
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.fields_by_name[
    "arb_error"
].message_type = _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT_ARBPARAMS
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.containing_type = _TIMEBLOCKERRORRESULTS
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.oneofs_by_name["error_type"].fields.append(
    _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.fields_by_name["x"]
)
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.fields_by_name[
    "x"
].containing_oneof = _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.oneofs_by_name[
    "error_type"
]
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.oneofs_by_name["error_type"].fields.append(
    _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.fields_by_name["y"]
)
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.fields_by_name[
    "y"
].containing_oneof = _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.oneofs_by_name[
    "error_type"
]
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.oneofs_by_name["error_type"].fields.append(
    _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.fields_by_name["z"]
)
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.fields_by_name[
    "z"
].containing_oneof = _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.oneofs_by_name[
    "error_type"
]
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.oneofs_by_name["error_type"].fields.append(
    _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.fields_by_name["arb_error"]
)
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.fields_by_name[
    "arb_error"
].containing_oneof = _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT.oneofs_by_name[
    "error_type"
]
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULTSENTRY.fields_by_name[
    "value"
].message_type = _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULTSENTRY.containing_type = _TIMEBLOCKERRORRESULTS
_TIMEBLOCKERRORRESULTS.fields_by_name[
    "qubit_error_results"
].message_type = _TIMEBLOCKERRORRESULTS_QUBITERRORRESULTSENTRY
DESCRIPTOR.message_types_by_name["CircuitComputationResult"] = _CIRCUITCOMPUTATIONRESULT
DESCRIPTOR.message_types_by_name[
    "TimeBlockComputationResult"
] = _TIMEBLOCKCOMPUTATIONRESULT
DESCRIPTOR.message_types_by_name["MeasurementGateResult"] = _MEASUREMENTGATERESULT
DESCRIPTOR.message_types_by_name["TimeBlockErrorResults"] = _TIMEBLOCKERRORRESULTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CircuitComputationResult = _reflection.GeneratedProtocolMessageType(
    "CircuitComputationResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _CIRCUITCOMPUTATIONRESULT,
        "__module__": "circuit_computation_result_pb2"
        # @@protoc_insertion_point(class_scope:CircuitComputationResult)
    },
)
_sym_db.RegisterMessage(CircuitComputationResult)

TimeBlockComputationResult = _reflection.GeneratedProtocolMessageType(
    "TimeBlockComputationResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _TIMEBLOCKCOMPUTATIONRESULT,
        "__module__": "circuit_computation_result_pb2"
        # @@protoc_insertion_point(class_scope:TimeBlockComputationResult)
    },
)
_sym_db.RegisterMessage(TimeBlockComputationResult)

MeasurementGateResult = _reflection.GeneratedProtocolMessageType(
    "MeasurementGateResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _MEASUREMENTGATERESULT,
        "__module__": "circuit_computation_result_pb2"
        # @@protoc_insertion_point(class_scope:MeasurementGateResult)
    },
)
_sym_db.RegisterMessage(MeasurementGateResult)

TimeBlockErrorResults = _reflection.GeneratedProtocolMessageType(
    "TimeBlockErrorResults",
    (_message.Message,),
    {
        "QubitErrorResult": _reflection.GeneratedProtocolMessageType(
            "QubitErrorResult",
            (_message.Message,),
            {
                "ArbParams": _reflection.GeneratedProtocolMessageType(
                    "ArbParams",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT_ARBPARAMS,
                        "__module__": "circuit_computation_result_pb2"
                        # @@protoc_insertion_point(class_scope:TimeBlockErrorResults.QubitErrorResult.ArbParams)
                    },
                ),
                "DESCRIPTOR": _TIMEBLOCKERRORRESULTS_QUBITERRORRESULT,
                "__module__": "circuit_computation_result_pb2"
                # @@protoc_insertion_point(class_scope:TimeBlockErrorResults.QubitErrorResult)
            },
        ),
        "QubitErrorResultsEntry": _reflection.GeneratedProtocolMessageType(
            "QubitErrorResultsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _TIMEBLOCKERRORRESULTS_QUBITERRORRESULTSENTRY,
                "__module__": "circuit_computation_result_pb2"
                # @@protoc_insertion_point(class_scope:TimeBlockErrorResults.QubitErrorResultsEntry)
            },
        ),
        "DESCRIPTOR": _TIMEBLOCKERRORRESULTS,
        "__module__": "circuit_computation_result_pb2"
        # @@protoc_insertion_point(class_scope:TimeBlockErrorResults)
    },
)
_sym_db.RegisterMessage(TimeBlockErrorResults)
_sym_db.RegisterMessage(TimeBlockErrorResults.QubitErrorResult)
_sym_db.RegisterMessage(TimeBlockErrorResults.QubitErrorResult.ArbParams)
_sym_db.RegisterMessage(TimeBlockErrorResults.QubitErrorResultsEntry)


DESCRIPTOR._options = None
_TIMEBLOCKERRORRESULTS_QUBITERRORRESULTSENTRY._options = None
# @@protoc_insertion_point(module_scope)