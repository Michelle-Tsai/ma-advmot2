from ctypes import *
from utils import TypeDef

class DevInfoMap(Structure):
    _fields_ = [
        ("DevLogicID", TypeDef.U32),
        ("DeviceNumber", TypeDef.U32),
        ("DeviceHandle", TypeDef.I64),
        ("DeviceName", c_char*48),
    ]

class RingNoInfoMap(Structure):
    _fields_ = [
        ("PhysicRingNo", TypeDef.U32),
        ("LogicRingNo", TypeDef.U32),
        ("DeviceInfo", DevInfoMap),
    ]

class DiGenInfoMap(Structure):
    _fields_ = [
        ("PhysicRingNo", TypeDef.U32),
        ("LogicRingNo", TypeDef.U32),
        ("PhysicPortID", TypeDef.U32),
        ("LogicPortID", TypeDef.U32),
        ("SubDeviceID", TypeDef.U32),
        ("DeviceInfo", DevInfoMap),
    ]

class DoGenInfoMap(Structure):
    _fields_ = [
        ("PhysicRingNo", TypeDef.U32),
        ("LogicRingNo", TypeDef.U32),
        ("PhysicPortID", TypeDef.U32),
        ("LogicPortID", TypeDef.U32),
        ("SubDeviceID", TypeDef.U32),
        ("DeviceInfo", DevInfoMap),
    ]

class AiGenInfoMap(Structure):
    _fields_ = [
        ("PhysicRingNo", TypeDef.U32),
        ("LogicRingNo", TypeDef.U32),
        ("PhysicChannelID", TypeDef.U32),
        ("LogicChannelID", TypeDef.U32),
        ("SubDeviceID", TypeDef.U32),
        ("DeviceInfo", DevInfoMap),
    ]

class AoGenInfoMap(Structure):
    _fields_ = [
        ("PhysicRingNo", TypeDef.U32),
        ("LogicRingNo", TypeDef.U32),
        ("PhysicChannelID", TypeDef.U32),
        ("LogicChannelID", TypeDef.U32),
        ("SubDeviceID", TypeDef.U32),
        ("DeviceInfo", DevInfoMap),
    ]

class CntGenInfoMap(Structure):
    _fields_ = [
        ("PhysicRingNo", TypeDef.U32),
        ("LogicRingNo", TypeDef.U32),
        ("PhysicChannelID", TypeDef.U32),
        ("LogicChannelID", TypeDef.U32),
        ("SubDeviceID", TypeDef.U32),
        ("DeviceInfo", DevInfoMap),
    ]

class MPGInfoMap(Structure):
    _fields_ = [
        ("PhysicRingNo", TypeDef.U32),
        ("LogicRingNo", TypeDef.U32),
        ("PhysicChannelID", TypeDef.U32),
        ("LogicChannelID", TypeDef.U32),
        ("SubDeviceID", TypeDef.U32),
        ("DeviceInfo", DevInfoMap),
    ]

class DEVICEINFO(Structure):
    _fields_ = [
        ("AxisCnt", TypeDef.U32),
        ("GroupCnt", TypeDef.U32),
        ("DIEXCnt", TypeDef.U32),
        ("DOEXCnt", TypeDef.U32),
        ("RingCnt", TypeDef.U32),
        ("DIGenPortCnt", TypeDef.U32),
        ("DOGenPortCnt", TypeDef.U32),
        ("AIGenChannelCnt", TypeDef.U32),
        ("AOGenChannelCnt", TypeDef.U32),
        ("CounterChannelCnt", TypeDef.U32),
        ("MDAQCHCnt", TypeDef.U32),
        ("MPGChannelCnt", TypeDef.U32),
        ("DeviceName", c_char*48),
        ("DevNumber", TypeDef.U32),
        ("DeviceHandle", TypeDef.U64),
        ("AxisHandle", TypeDef.PU64),
        ("GroupHandle", TypeDef.PU64),
        ("LatchCHHandle", TypeDef.PU64),
        ("RingInfo", POINTER(RingNoInfoMap)),
        ("GenDIInfo", POINTER(DiGenInfoMap)),
        ("GenDOInfo", POINTER(DoGenInfoMap)),
        ("GenAIInfo", POINTER(AiGenInfoMap)),
        ("GenAOInfo", POINTER(AoGenInfoMap)),
        ("GenCounterInfo", POINTER(CntGenInfoMap)),
        ("MPGInfo", POINTER(MPGInfoMap)),
    ]