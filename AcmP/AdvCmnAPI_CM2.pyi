"""Type stub for AdvCmnAPI_CM2（由 gen_api_pyi.py 從 AdvCmnAPI_CM2.py 自動產生）。

所有函式都是 class 上的 staticmethod，直接以 Class.Func(...) 呼叫。
enum 參數 (ABS_MODE 等)：AdvMotDrv 的 enum 若為 int-based 可直接傳成員，否則請用 .value。
"""

from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from ctypes import _CArgObject, _CData, _Pointer
from ctypes import *
from typing import Any, TypeAlias, TypeVar

_T = TypeVar("_T", bound=_CData)
# POINTER(X) 參數可傳：byref(x)、pointer(x)、(X * n)() 陣列、或 None
_PtrArg: TypeAlias = _Pointer[_T] | Array[_T] | _CArgObject | None
# c_void_p 參數可傳：整數位址 / handle、c_void_p、byref(...)、任何 ctypes 物件、None
_VoidPtrArg: TypeAlias = int | c_void_p | _CArgObject | _CData | None

lib: CDLL

class AdvCmnAPI_CM2:
    @staticmethod
    def Acm2_GetErrorMessage(ErrorCode: int, lpszError: bytes | Array[c_char] | None, nMaxError: int, /) -> int:
        """U32 Acm2_GetErrorMessage(U32 ErrorCode, PI8 lpszError, U32 nMaxError)"""
    @staticmethod
    def Acm2_DevInitialize() -> int:
        """U32 Acm2_DevInitialize()"""
    @staticmethod
    def Acm2_GetAvailableDevs(DeviceList: _PtrArg[DEVLIST], MaxEntries: int, OutEntries: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GetAvailableDevs(DEVLIST *DeviceList, U32 MaxEntries, PU32 OutEntries)"""
    @staticmethod
    def Acm2_GetObjectCount(ObjType: ADV_OBJ_TYPE | int, ObjCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GetObjectCount(ADV_OBJ_TYPE ObjType, PU32 ObjCnt)"""
    @staticmethod
    def Acm2_GetMappedPhysicalID(ObjType: ADV_OBJ_TYPE | int, ObjLogicalID: int, DeviceNumber: _PtrArg[c_uint32], ObjPhysicalID: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GetMappedPhysicalID(ADV_OBJ_TYPE ObjType, U32 ObjLogicalID, PU32 DeviceNumber, PU32 ObjPhysicalID)"""
    @staticmethod
    def Acm2_GetMappedLogicalIDList(ObjType: ADV_OBJ_TYPE | int, DeviceLogicalID: int, LogicallIDList: _PtrArg[c_uint32], ObjCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GetMappedLogicalIDList(ADV_OBJ_TYPE ObjType, U32 DeviceLogicalID, PU32 LogicallIDList, PU32 ObjCnt)"""
    @staticmethod
    def Acm2_GetMappedObjInfo(ObjType: ADV_OBJ_TYPE | int, ObjLogicalID: int, pObjInfo: _VoidPtrArg, /) -> int:
        """U32 Acm2_GetMappedObjInfo(ADV_OBJ_TYPE ObjType, U32 ObjLogicalID, OUT VOID *pObjInfo)"""
    @staticmethod
    def Acm2_DevAllClose() -> int:
        """U32 Acm2_DevAllClose()"""
    @staticmethod
    def Acm2_GetLastError(ObjType: ADV_OBJ_TYPE | int, ObjLogicalID: int, /) -> int:
        """U32 Acm2_GetLastError(ADV_OBJ_TYPE ObjType, U32 ObjLogicalID)"""
    @staticmethod
    def Acm2_GetProperty(ObjID: int, PropertyID: int, Value: _PtrArg[c_double], /) -> int:
        """U32 Acm2_GetProperty(U32 ObjID, U32 PropertyID, PF64 Value)"""
    @staticmethod
    def Acm2_SetProperty(ObjID: int, PropertyID: int, Value: float, /) -> int:
        """U32 Acm2_SetProperty(U32 ObjID, U32 PropertyID, F64 Value)"""
    @staticmethod
    def Acm2_SetMultiProperty(ObjID: int, PropertyID: _PtrArg[c_uint32], Value: _PtrArg[c_double], Data_Cnt: int, ErrorBuffer: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_SetMultiProperty(U32 ObjID, PU32 PropertyID, PF64 Value, U32 Data_Cnt, PU32 ErrorBuffer)"""
    @staticmethod
    def Acm2_GetMultiProperty(ObjID: int, PropertyID: _PtrArg[c_uint32], Value: _PtrArg[c_double], Data_Cnt: int, ErrorBuffer: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GetMultiProperty(U32 ObjID, PU32 PropertyID, PF64 Value, U32 Data_Cnt, PU32 ErrorBuffer)"""
    @staticmethod
    def Acm2_GetRawProperty(ObjID: int, PropertyID: int, Value: _VoidPtrArg, BufferLength: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GetRawProperty(U32 ObjID, U32 PropertyID, PVOID Value, PU32 BufferLength)"""
    @staticmethod
    def Acm2_EnableCallBackFuncForOneEvent(ObjID: int, EventID: ADV_EVENT_SUBSCRIBE | int, CallBackFun: CALLBACK_FUNC, /) -> int:
        """U32 Acm2_EnableCallBackFuncForOneEvent(U32 ObjID, ADV_EVENT_SUBSCRIBE EventID, ADV_USER_CALLBACK_FUNC CallBackFun)"""
    @staticmethod
    def Acm2_DevLoadAllConfig(ConfigPath: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm2_DevLoadAllConfig(PI8 ConfigPath)"""
    @staticmethod
    def Acm2_DevLoadConfig(DevID: int, ConfigPath: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm2_DevLoadConfig(U32 DevID, PI8 ConfigPath)"""
    @staticmethod
    def Acm2_DevReadMailBox(ObjType: ADV_OBJ_TYPE | int, DevID: int, par_id: int, data_index: int, data_count: int, DataBuffer: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_DevReadMailBox(ADV_OBJ_TYPE ObjType, U32 DevID, U32 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)"""
    @staticmethod
    def Acm2_DevWriteMailBox(ObjType: ADV_OBJ_TYPE | int, DevID: int, par_id: int, data_index: int, data_count: int, DataBuffer: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_DevWriteMailBox(ADV_OBJ_TYPE ObjType, U32 DevID, U32 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)"""
    @staticmethod
    def Acm2_GetErrors(DevID: int, Error: _VoidPtrArg, ErrorCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GetErrors(U32 DevID, PVOID Error, PU32 ErrorCount)"""
    @staticmethod
    def Acm2_ResetErrorRecord(DevID: int, /) -> int:
        """U32 Acm2_ResetErrorRecord(U32 DevID)"""
    @staticmethod
    def Acm2_DevPreviewMotion(DevID: int, InputFile: bytes | Array[c_char] | None, OutputFile: bytes | Array[c_char] | None, NumberOfAxes: int, /) -> int:
        """U32 Acm2_DevPreviewMotion(U32 DevID, PI8 InputFile, PI8 OutputFile, U16 NumberOfAxes)"""
    @staticmethod
    def Acm2_AxReturnPausePosition(AxID: int, /) -> int:
        """U32 Acm2_AxReturnPausePosition(U32 AxID)"""
    @staticmethod
    def Acm2_AxSetSvOn(AxID: int, OnOff: DO_ONOFF | int, /) -> int:
        """U32 Acm2_AxSetSvOn(U32 AxID, DO_ONOFF OnOff)"""
    @staticmethod
    def Acm2_DevSetAllSvOn(OnOff: DO_ONOFF | int, /) -> int:
        """U32 Acm2_DevSetAllSvOn(DO_ONOFF OnOff)"""
    @staticmethod
    def Acm2_AxSetErcOn(AxID: int, OnOff: DO_ONOFF | int, /) -> int:
        """U32 Acm2_AxSetErcOn(U32 AxID, DO_ONOFF OnOff)"""
    @staticmethod
    def Acm2_AxResetAlm(AxID: int, OnOff: DO_ONOFF | int, /) -> int:
        """U32 Acm2_AxResetAlm(U32 AxID, DO_ONOFF OnOff)"""
    @staticmethod
    def Acm2_AxPTP(AxID: int, ptpMode: ABS_MODE | int, Distance: float, /) -> int:
        """U32 Acm2_AxPTP(U32 AxID, ABS_MODE ptpMode, F64 Distance)"""
    @staticmethod
    def Acm2_AxMoveContinue(AxID: int, Direction: MOTION_DIRECTION | int, /) -> int:
        """U32 Acm2_AxMoveContinue(U32 AxID, MOTION_DIRECTION Direction)"""
    @staticmethod
    def Acm2_AxMotionStop(AxisArray: _PtrArg[c_uint32], ArrayElements: int, StopMode: MOTION_STOP_MODE | int, NewDec: float, /) -> int:
        """U32 Acm2_AxMotionStop(PU32 AxisArray, U32 ArrayElements, MOTION_STOP_MODE StopMode, F64 NewDec)"""
    @staticmethod
    def Acm2_AxHome(AxID: int, HomeMode: HOME_MODE | int, Direction: MOTION_DIRECTION | int, /) -> int:
        """U32 Acm2_AxHome(U32 AxID, HOME_MODE HomeMode, MOTION_DIRECTION Direction)"""
    @staticmethod
    def Acm2_AxMoveGantryHome(AxID: int, HomeMode: HOME_MODE | int, Direction: MOTION_DIRECTION | int, /) -> int:
        """U32 Acm2_AxMoveGantryHome(U32 AxID, HOME_MODE HomeMode, MOTION_DIRECTION Direction)"""
    @staticmethod
    def Acm2_AxSetHomeSpeedProfile(AxID: int, ProfileVel: SPEED_PROFILE_PRM, /) -> int:
        """U32 Acm2_AxSetHomeSpeedProfile(U32 AxID, SPEED_PROFILE_PRM ProfileVel)"""
    @staticmethod
    def Acm2_AxChangePos(AxID: int, NewPos: float, /) -> int:
        """U32 Acm2_AxChangePos(U32 AxID, F64 NewPos)"""
    @staticmethod
    def Acm2_AxChangeVel(AxID: int, NewVel: float, NewAcc: float, NewDec: float, /) -> int:
        """U32 Acm2_AxChangeVel(U32 AxID, F64 NewVel, F64 NewAcc, F64 NewDec)"""
    @staticmethod
    def Acm2_AxChangeVelByRate(AxID: int, Rate: int, NewAcc: float, NewDec: float, /) -> int:
        """U32 Acm2_AxChangeVelByRate(U32 AxID, U32 Rate, F64 NewAcc, F64 NewDec)"""
    @staticmethod
    def Acm2_AxMoveImpose(AxID: int, Position: float, NewVelocity: float, /) -> int:
        """U32 Acm2_AxMoveImpose(U32 AxID, F64 Position, F64 NewVelocity)"""
    @staticmethod
    def Acm2_AxResetError(AxID: int, /) -> int:
        """U32 Acm2_AxResetError(U32 AxID)"""
    @staticmethod
    def Acm2_AxEnableTrig(AxID: int, TrigPrm: int, /) -> int:
        """U32 Acm2_AxEnableTrig(U32 AxID, TRIG_PRM TrigPrm)"""
    @staticmethod
    def Acm2_DevResetAllError() -> int:
        """U32 Acm2_DevResetAllError()"""
    @staticmethod
    def Acm2_DevCheckAllAxReady(Timeout: int, /) -> int:
        """U32 Acm2_DevCheckAllAxReady(U32 Timeout)"""
    @staticmethod
    def Acm2_AxGetState(AxID: int, StatusType: AXIS_STATUS_TYPE | int, State: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_AxGetState(U32 AxID, AXIS_STATUS_TYPE StatusType, PU32 State)"""
    @staticmethod
    def Acm2_AxGetMotionIO(AxID: int, Status: _PtrArg[MOTION_IO], /) -> int:
        """U32 Acm2_AxGetMotionIO(U32 AxID, MOTION_IO *Status)"""
    @staticmethod
    def Acm2_AxSetPosition(AxID: int, PosType: POSITION_TYPE | int, Position: float, /) -> int:
        """U32 Acm2_AxSetPosition(U32 AxID, POSITION_TYPE PosType, F64 Position)"""
    @staticmethod
    def Acm2_DevSetAllPosition(PosType: POSITION_TYPE | int, Position: float, /) -> int:
        """U32 Acm2_DevSetAllPosition(POSITION_TYPE PosType, F64 Position)"""
    @staticmethod
    def Acm2_AxGetPosition(AxID: int, PosType: POSITION_TYPE | int, Position: _PtrArg[c_double], /) -> int:
        """U32 Acm2_AxGetPosition(U32 AxID, POSITION_TYPE PosType, PF64 Position)"""
    @staticmethod
    def Acm2_AxGetMachPosition(AxID: int, Position: _PtrArg[c_double], /) -> int:
        """U32 Acm2_AxGetMachPosition(U32 AxID, PF64 Position)"""
    @staticmethod
    def Acm2_AxSetSpeedProfile(AxID: int, ProfileVel: SPEED_PROFILE_PRM, /) -> int:
        """U32 Acm2_AxSetSpeedProfile(U32 AxID, SPEED_PROFILE_PRM ProfileVel)"""
    @staticmethod
    def Acm2_AxGetVel(AxID: int, VelType: VELOCITY_TYPE | int, Velocity: _PtrArg[c_double], /) -> int:
        """U32 Acm2_AxGetVel(U32 AxID, VELOCITY_TYPE VelType, PF64 Velocity)"""
    @staticmethod
    def Acm2_AxEnableExternalMode(AxID: int, ExtDrvMode: EXT_DRIVE_MODE | int, /) -> int:
        """U32 Acm2_AxEnableExternalMode(U32 AxID, EXT_DRIVE_MODE ExtDrvMode)"""
    @staticmethod
    def Acm2_AxDownloadTorqueTable(AxID: int, PositionArray: _PtrArg[c_double], TorqueArray: _PtrArg[c_double], ArrayElements: int, /) -> int:
        """U32 Acm2_AxDownloadTorqueTable(U32 AxID, PF64 PositionArray, PF64 TorqueArray, U32 ArrayElements)"""
    @staticmethod
    def Acm2_AxLoadTorqueTableFile(AxID: int, FilePath: bytes | Array[c_char] | None, PointsCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_AxLoadTorqueTableFile(U32 AxID, PI8 FilePath, PU32 PointsCount)"""
    @staticmethod
    def Acm2_AxMoveTorque(AxID: int, Distance: float, Torque: float, TorqueSlope: float, Velocity: float, PressTime: float, Mode: int, /) -> int:
        """U32 Acm2_AxMoveTorque(U32 AxID, F64 Distance, F64 Torque, F64 TorqueSlope, F64 Velocity, F64 PressTime, U32 Mode)"""
    @staticmethod
    def Acm2_AxGetActTorque(AxID: int, Torque: _PtrArg[c_double], /) -> int:
        """U32 Acm2_AxGetActTorque(U32 AxID, PF64 Torque)"""
    @staticmethod
    def Acm2_AxSoftJog(AxID: int, Direction: MOTION_DIRECTION | int, /) -> int:
        """U32 Acm2_AxSoftJog(U32 AxID, MOTION_DIRECTION Direction)"""
    @staticmethod
    def Acm2_AxSetJogSpeedProfile(AxID: int, ProfileVel: JOG_SPEED_PROFILE_PRM, /) -> int:
        """U32 Acm2_AxSetJogSpeedProfile(U32 AxID, JOG_SPEED_PROFILE_PRM ProfileVel)"""
    @staticmethod
    def Acm2_AxMotionStart(AxisArray: _PtrArg[c_uint32], ArrayElements: int, /) -> int:
        """U32 Acm2_AxMotionStart(PU32 AxisArray, U32 ArrayElements)"""
    @staticmethod
    def Acm2_AxPause(AxID: int, /) -> int:
        """U32 Acm2_AxPause(U32 AxID)"""
    @staticmethod
    def Acm2_AxResume(AxID: int, /) -> int:
        """U32 Acm2_AxResume(U32 AxID)"""
    @staticmethod
    def Acm2_AxResetPVTTable(AxID: int, /) -> int:
        """U32 Acm2_AxResetPVTTable(U32 AxID)"""
    @staticmethod
    def Acm2_AxLoadPVTTable(AxID: int, Position: _PtrArg[c_double], Velocity: _PtrArg[c_double], Time: _PtrArg[c_double], ArrayElements: int, /) -> int:
        """U32 Acm2_AxLoadPVTTable(U32 AxID, PF64 Position, PF64 Velocity, PF64 Time, U32 ArrayElements)"""
    @staticmethod
    def Acm2_AxCalculatePVTTableContinuous(AxID: int, Position: _PtrArg[c_double], Velocity: _PtrArg[c_double], JerkFactor: _PtrArg[c_double], MaxVel: _PtrArg[c_double], Acc: _PtrArg[c_double], Dec: _PtrArg[c_double], ArrayElements: int, Time: _PtrArg[c_double], /) -> int:
        """U32 Acm2_AxCalculatePVTTableContinuous(U32 AxID, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, U32 ArrayElements, PF64 Time)"""
    @staticmethod
    def Acm2_AxLoadPVTTableContinuous(AxID: int, Position: _PtrArg[c_double], Velocity: _PtrArg[c_double], JerkFactor: _PtrArg[c_double], MaxVel: _PtrArg[c_double], Acc: _PtrArg[c_double], Dec: _PtrArg[c_double], TimeDelay: float, ArrayElements: int, /) -> int:
        """U32 Acm2_AxLoadPVTTableContinuous(U32 AxID, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, F64 TimeDelay, U32 ArrayElements)"""
    @staticmethod
    def Acm2_AxMovePVT(AxID: int, /) -> int:
        """U32 Acm2_AxMovePVT(U32 AxID)"""
    @staticmethod
    def Acm2_AxCheckPTBuffer(AxID: int, Freespace: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_AxCheckPTBuffer(U32 AxID, PU32 Freespace)"""
    @staticmethod
    def Acm2_AxAddPTData(AxID: int, Position: float, Time: float, /) -> int:
        """U32 Acm2_AxAddPTData(U32 AxID, F64 Position, F64 Time)"""
    @staticmethod
    def Acm2_AxMovePT(AxID: int, /) -> int:
        """U32 Acm2_AxMovePT(U32 AxID)"""
    @staticmethod
    def Acm2_AxResetPTData(AxID: int, /) -> int:
        """U32 Acm2_AxResetPTData(U32 AxID)"""
    @staticmethod
    def Acm2_AxGearIn(PrimaryAxisID: int, FollowingAxisID: int, GearInParameter: GEAR_IN_PRM, /) -> int:
        """U32 Acm2_AxGearIn(U32 PrimaryAxisID, U32 FollowingAxisID, GEAR_IN_PRM GearInParameter)"""
    @staticmethod
    def Acm2_AxTangentInGp(AxID: int, PrimaryGpID: int, TangentInParameter: TANGENT_IN_PRM, /) -> int:
        """U32 Acm2_AxTangentInGp(U32 AxID, U32 PrimaryGpID, TANGENT_IN_PRM TangentInParameter)"""
    @staticmethod
    def Acm2_AxGantryIn(PrimaryAxisID: int, FollowingAxisID: int, GantryInParameter: GANTRY_IN_PRM, /) -> int:
        """U32 Acm2_AxGantryIn(U32 PrimaryAxisID, U32 FollowingAxisID, GANTRY_IN_PRM GantryInParameter)"""
    @staticmethod
    def Acm2_AxPhaseAx(AxID: int, PhaseAxParameter: PHASE_AXIS_PRM, /) -> int:
        """U32 Acm2_AxPhaseAx(U32 AxID, PHASE_AXIS_PRM PhaseAxParameter)"""
    @staticmethod
    def Acm2_AxSyncOut(FollowingAxisID: int, /) -> int:
        """U32 Acm2_AxSyncOut(U32 FollowingAxisID)"""
    @staticmethod
    def Acm2_GpGetPausePosition(GpID: int, RefPausePositionArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GpGetPausePosition(U32 GpID, PF64 RefPausePositionArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm2_GpCreate(GpID: int, AxisArray: _PtrArg[c_uint32], ArrayElements: int, /) -> int:
        """U32 Acm2_GpCreate(U32 GpID, PU32 AxisArray, U32 ArrayElements)"""
    @staticmethod
    def Acm2_GpGetAxesInGroup(GpID: int, AxisArray: _PtrArg[c_uint32], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GpGetAxesInGroup(U32 GpID, PU32 AxisArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm2_GpUpdate(GpID: int, /) -> int:
        """U32 Acm2_GpUpdate(U32 GpID)"""
    @staticmethod
    def Acm2_GpResetError(GpID: int, /) -> int:
        """U32 Acm2_GpResetError(U32 GpID)"""
    @staticmethod
    def Acm2_GpEnableTrig(GpID: int, TrigPrm: TRIG_PRM, /) -> int:
        """U32 Acm2_GpEnableTrig(U32 GpID, TRIG_PRM TrigPrm)"""
    @staticmethod
    def Acm2_GpLine(GpID: int, LineMode: GP_LINE_MODE | int, EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GpLine(U32 GpID, GP_LINE_MODE LineMode, PF64 EndArray, PU32 pArrayElements)"""
    @staticmethod
    def Acm2_GpArc_Center(GpID: int, ArcMode: ABS_MODE | int, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: ARC_DIRECTION | int, /) -> int:
        """U32 Acm2_GpArc_Center(U32 GpID, ABS_MODE ArcMode, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION Direction)"""
    @staticmethod
    def Acm2_GpArc_3P(GpID: int, ArcMode: ABS_MODE | int, RefArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: ARC_DIRECTION | int, /) -> int:
        """U32 Acm2_GpArc_3P(U32 GpID, ABS_MODE ArcMode, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION Direction)"""
    @staticmethod
    def Acm2_GpArc_Angle(GpID: int, ArcMode: ABS_MODE | int, CenterArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Angle: float, Direction: ARC_DIRECTION | int, /) -> int:
        """U32 Acm2_GpArc_Angle(U32 GpID, ABS_MODE ArcMode, PF64 CenterArray, PU32 pArrayElements, F64 Angle, ARC_DIRECTION Direction)"""
    @staticmethod
    def Acm2_Gp3DArc_Center(GpID: int, ArcMode: ABS_MODE | int, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: ARC_DIRECTION | int, /) -> int:
        """U32 Acm2_Gp3DArc_Center(U32 GpID, ABS_MODE ArcMode, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION Direction)"""
    @staticmethod
    def Acm2_Gp3DArc_NormVec(GpID: int, ArcMode: ABS_MODE | int, CenterArray: _PtrArg[c_double], NormalVec: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Angle: float, Direction: ARC_DIRECTION | int, /) -> int:
        """U32 Acm2_Gp3DArc_NormVec(U32 GpID, ABS_MODE ArcMode, PF64 CenterArray, PF64 NormalVec, PU32 pArrayElements, F64 Angle, ARC_DIRECTION Direction)"""
    @staticmethod
    def Acm2_Gp3DArc_3P(GpID: int, ArcMode: ABS_MODE | int, RefArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: ARC_DIRECTION | int, cycCount: int, /) -> int:
        """U32 Acm2_Gp3DArc_3P(U32 GpID, ABS_MODE ArcMode, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION Direction, U32 cycCount)"""
    @staticmethod
    def Acm2_Gp3DArc_3PAngle(GpID: int, ArcMode: ABS_MODE | int, RefPoint_1: _PtrArg[c_double], RefPoint_2: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Angle: float, Direction: ARC_DIRECTION | int, /) -> int:
        """U32 Acm2_Gp3DArc_3PAngle(U32 GpID, ABS_MODE ArcMode, PF64 RefPoint_1, PF64 RefPoint_2, PU32 pArrayElements, F64 Angle, ARC_DIRECTION Direction)"""
    @staticmethod
    def Acm2_GpHelix_Center(GpID: int, HelixMode: ABS_MODE | int, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: ARC_DIRECTION | int, /) -> int:
        """U32 Acm2_GpHelix_Center(U32 GpID, ABS_MODE HelixMode, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION Direction)"""
    @staticmethod
    def Acm2_GpHelix_3P(GpID: int, HelixMode: ABS_MODE | int, RefArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: ARC_DIRECTION | int, /) -> int:
        """U32 Acm2_GpHelix_3P(U32 GpID, ABS_MODE HelixMode, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION Direction)"""
    @staticmethod
    def Acm2_GpHelix_Angle(GpID: int, HelixMode: ABS_MODE | int, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: ARC_DIRECTION | int, /) -> int:
        """U32 Acm2_GpHelix_Angle(U32 GpID, ABS_MODE HelixMode, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION Direction)"""
    @staticmethod
    def Acm2_GpResume(GpID: int, /) -> int:
        """U32 Acm2_GpResume(U32 GpID)"""
    @staticmethod
    def Acm2_GpPause(GpID: int, /) -> int:
        """U32 Acm2_GpPause(U32 GpID)"""
    @staticmethod
    def Acm2_GpMotionStop(GpID: int, StopMode: MOTION_STOP_MODE | int, NewDec: float, /) -> int:
        """U32 Acm2_GpMotionStop(U32 GpID, MOTION_STOP_MODE StopMode, F64 NewDec)"""
    @staticmethod
    def Acm2_GpChangePos(GpID: int, Mode: ABS_MODE, DistanceArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GpChangePos(U32 GpID, ABS_MODE Mode, PF64 DistanceArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm2_GpChangeVel(GpID: int, NewVelocity: float, NewAcc: float, NewDec: float, /) -> int:
        """U32 Acm2_GpChangeVel(U32 GpID, F64 NewVelocity, F64 NewAcc, F64 NewDec)"""
    @staticmethod
    def Acm2_GpChangeVelByRate(GpID: int, Rate: int, NewAcc: float, NewDec: float, /) -> int:
        """U32 Acm2_GpChangeVelByRate(U32 GpID, U32 Rate, F64 NewAcc, F64 NewDec)"""
    @staticmethod
    def Acm2_GpGetVel(GpID: int, VelType: VELOCITY_TYPE | int, Velocity: _PtrArg[c_double], /) -> int:
        """U32 Acm2_GpGetVel(U32 GpID, VELOCITY_TYPE VelType, PF64 Velocity)"""
    @staticmethod
    def Acm2_GpSetSpeedProfile(GpID: int, ProfileVel: SPEED_PROFILE_PRM, /) -> int:
        """U32 Acm2_GpSetSpeedProfile(U32 GpID, SPEED_PROFILE_PRM ProfileVel)"""
    @staticmethod
    def Acm2_GpGetState(GpID: int, State: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GpGetState(U32 GpID, PU32 State)"""
    @staticmethod
    def Acm2_GpLoadPath(GpID: int, FilePath: bytes | Array[c_char] | None, pTotalCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GpLoadPath(U32 GpID, PI8 FilePath, PU32 pTotalCount)"""
    @staticmethod
    def Acm2_GpAddPath(GpID: int, MoveCmd: int, MoveMode: PATH_MOVE_MODE_CM2 | int, FH: float, FL: float, Acc: float, Dec: float, EndPoint_DataArray: _PtrArg[c_double], CenPoint_DataArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GpAddPath(U32 GpID, U32 MoveCmd, PATH_MOVE_MODE_CM2 MoveMode, F64 FH, F64 FL, F64 Acc, F64 Dec, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm2_GpMovePath(GpID: int, /) -> int:
        """U32 Acm2_GpMovePath(U32 GpID)"""
    @staticmethod
    def Acm2_GpResetPath(GpID: int, /) -> int:
        """U32 Acm2_GpResetPath(U32 GpID)"""
    @staticmethod
    def Acm2_GpGetPathStatus(GpID: int, pathstatus: _PtrArg[PATH_STATUS], /) -> int:
        """U32 Acm2_GpGetPathStatus(U32 GpID, PATH_STATUS *pathstatus)"""
    @staticmethod
    def Acm2_GpMoveSelPath(GpID: int, StartIndex: int, EndIndex: int, Repeat: int, /) -> int:
        """U32 Acm2_GpMoveSelPath(U32 GpID, U32 StartIndex, U32 EndIndex, U32 Repeat)"""
    @staticmethod
    def Acm2_GpGetPathIndexStatus(GpID: int, Index: int, CmdFunc: _PtrArg[c_uint32], MoveMode: _PtrArg[c_uint32], FH: _PtrArg[c_double], FL: _PtrArg[c_double], Acc: _PtrArg[c_double], Dec: _PtrArg[c_double], EndPoint_DataArray: _PtrArg[c_double], CenPoint_DataArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GpGetPathIndexStatus(U32 GpID, U32 Index, PU32 CmdFunc, PU32 MoveMode, PF64 FH, PF64 FL, PF64 Acc, PF64 Dec, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm2_GpDelay(GpID: int, DelayTime: int, /) -> int:
        """U32 Acm2_GpDelay(U32 GpID, U32 DelayTime)"""
    @staticmethod
    def Acm2_GpPathDO(GpID: int, PathDOPrm: PATH_DO_PRM, /) -> int:
        """U32 Acm2_GpPathDO(U32 GpID, PATH_DO_PRM PathDOPrm)"""
    @staticmethod
    def Acm2_GpPathWaitDI(GpID: int, DIWaitPrm: PATH_DI_WAIT_PRM, /) -> int:
        """U32 Acm2_GpPathWaitDI(U32 GpID, PATH_DI_WAIT_PRM DIWaitPrm)"""
    @staticmethod
    def Acm2_GpPathWaitForAxis(GpID: int, AxWaitPrm: PATH_AX_WAIT_PRM, /) -> int:
        """U32 Acm2_GpPathWaitForAxis(U32 GpID, PATH_AX_WAIT_PRM AxWaitPrm)"""
    @staticmethod
    def Acm2_GpPathDIConditional(GpID: int, MoveCmd: int, PathDIPrm: PATH_DI_WAIT_PRM, /) -> int:
        """U32 Acm2_GpPathDIConditional(U32 GpID, U32 MoveCmd, PATH_DI_WAIT_PRM PathDIPrm)"""
    @staticmethod
    def Acm2_GpPathDOConditional(GpID: int, MoveCmd: int, PathDOPrm: PATH_DO_PRM, /) -> int:
        """U32 Acm2_GpPathDOConditional(U32 GpID, U32 MoveCmd, PATH_DO_PRM PathDOPrm)"""
    @staticmethod
    def Acm2_GpPathAxisConditional(GpID: int, MoveCmd: int, AxWaitPrm: PATH_AX_WAIT_PRM, /) -> int:
        """U32 Acm2_GpPathAxisConditional(U32 GpID, U32 MoveCmd, PATH_AX_WAIT_PRM AxWaitPrm)"""
    @staticmethod
    def Acm2_GpPathVarConditional(GpID: int, MoveCmd: int, VarPrm: PATH_VAR_PRM, /) -> int:
        """U32 Acm2_GpPathVarConditional(U32 GpID, U32 MoveCmd, PATH_VAR_PRM VarPrm)"""
    @staticmethod
    def Acm2_GpPathConditional(GpID: int, MoveCmd: int, /) -> int:
        """U32 Acm2_GpPathConditional(U32 GpID, U32 MoveCmd)"""
    @staticmethod
    def Acm2_GpPathOperator(GpID: int, OperatorPrm: PATH_OPERATOR_PRM, /) -> int:
        """U32 Acm2_GpPathOperator(U32 GpID, PATH_OPERATOR_PRM OperatorPrm)"""
    @staticmethod
    def Acm2_GpPathStartRecordBuffer(GpID: int, /) -> int:
        """U32 Acm2_GpPathStartRecordBuffer(U32 GpID)"""
    @staticmethod
    def Acm2_GpPathEndRecordBuffer(GpID: int, OutResult: _PtrArg[VALIDATE_RESULT], /) -> int:
        """U32 Acm2_GpPathEndRecordBuffer(U32 GpID, VALIDATE_RESULT* OutResult)"""
    @staticmethod
    def Acm2_GpLookAheadPath(GpID: int, BufferSize: int, OutputFile: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm2_GpLookAheadPath(U32 GpID, U16 BufferSize, PI8 OutputFile)"""
    @staticmethod
    def Acm2_GpLookAheadPathFile(GpID: int, BufferSize: int, InputPathFile: bytes | Array[c_char] | None, OutputFile: bytes | Array[c_char] | None, PathCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GpLookAheadPathFile(U32 GpID, U16 BufferSize, PI8 InputPathFile, PI8 OutputFile, PU32 PathCount)"""
    @staticmethod
    def Acm2_GpLoadAndMovePath(GpID: int, FilePath: bytes | Array[c_char] | None, TotalCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_GpLoadAndMovePath(U32 GpID, PI8 FilePath, PU32 TotalCount)"""
    @staticmethod
    def Acm2_ChSetDOBit(DoChannel: int, BitData: int, /) -> int:
        """U32 Acm2_ChSetDOBit(U32 DoChannel, U32 BitData)"""
    @staticmethod
    def Acm2_ChGetDOBit(DoChannel: int, BitData: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetDOBit(U32 DoChannel, PU32 BitData)"""
    @staticmethod
    def Acm2_ChGetDIBit(DiChannel: int, BitData: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetDIBit(U32 DiChannel, PU32 BitData)"""
    @staticmethod
    def Acm2_ChSetDOBitByRingNo(RingNo: int, SubDeviceID: int, DoChannel: int, BitData: int, /) -> int:
        """U32 Acm2_ChSetDOBitByRingNo(U32 RingNo, U32 SubDeviceID, U32 DoChannel, U32 BitData)"""
    @staticmethod
    def Acm2_ChGetDOBitByRingNo(RingNo: int, SubDeviceID: int, DoChannel: int, BitData: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetDOBitByRingNo(U32 RingNo, U32 SubDeviceID, U32 DoChannel, PU32 BitData)"""
    @staticmethod
    def Acm2_ChGetDIBitByRingNo(RingNo: int, SubDeviceID: int, DiChannel: int, BitData: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetDIBitByRingNo(U32 RingNo, U32 SubDeviceID, U32 DiChannel, PU32 BitData)"""
    @staticmethod
    def Acm2_ChSetDOByte(StartPort: int, PortNum: int, ByteDataArray: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChSetDOByte(U32 StartPort, U32 PortNum, PU32 ByteDataArray)"""
    @staticmethod
    def Acm2_ChGetDOByte(StartPort: int, PortNum: int, ByteDataArray: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetDOByte(U32 StartPort, U32 PortNum, PU32 ByteDataArray)"""
    @staticmethod
    def Acm2_ChGetDIByte(StartPort: int, PortNum: int, ByteDataArray: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetDIByte(U32 StartPort, U32 PortNum, PU32 ByteDataArray)"""
    @staticmethod
    def Acm2_ChSetDOByteByRingNo(RingNo: int, SubDeviceID: int, CHStartPort: int, PortNum: int, ByteDataArray: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChSetDOByteByRingNo(U32 RingNo, U32 SubDeviceID, U32 CHStartPort, U32 PortNum, PU32 ByteDataArray)"""
    @staticmethod
    def Acm2_ChGetDOByteByRingNo(RingNo: int, SubDeviceID: int, CHStartPort: int, PortNum: int, ByteDataArray: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetDOByteByRingNo(U32 RingNo, U32 SubDeviceID, U32 CHStartPort, U32 PortNum, PU32 ByteDataArray)"""
    @staticmethod
    def Acm2_ChGetDIByteByRingNo(RingNo: int, SubDeviceID: int, CHStartPort: int, PortNum: int, ByteDataArray: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetDIByteByRingNo(U32 RingNo, U32 SubDeviceID, U32 CHStartPort, U32 PortNum, PU32 ByteDataArray)"""
    @staticmethod
    def Acm2_ChSetAOData(AoChannel: int, Type: DAQ_DATA_TYPE | int, AoData: float, /) -> int:
        """U32 Acm2_ChSetAOData(U32 AoChannel, DAQ_DATA_TYPE Type, F64 AoData)"""
    @staticmethod
    def Acm2_ChGetAOData(AoChannel: int, Type: DAQ_DATA_TYPE | int, AoData: _PtrArg[c_double], /) -> int:
        """U32 Acm2_ChGetAOData(U32 AoChannel, DAQ_DATA_TYPE Type, PF64 AoData)"""
    @staticmethod
    def Acm2_ChGetAOStatus(AoChannel: int, ChanStatus: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetAOStatus(U32 AoChannel, PU32 ChanStatus)"""
    @staticmethod
    def Acm2_ChSetAODataByRingNo(RingNo: int, SubDeviceID: int, AoChannel: int, Type: DAQ_DATA_TYPE | int, AoData: float, /) -> int:
        """U32 Acm2_ChSetAODataByRingNo(U32 RingNo, U32 SubDeviceID, U32 AoChannel, DAQ_DATA_TYPE Type, F64 AoData)"""
    @staticmethod
    def Acm2_ChGetAODataByRingNo(RingNo: int, SubDeviceID: int, AoChannel: int, Type: DAQ_DATA_TYPE | int, AoData: _PtrArg[c_double], /) -> int:
        """U32 Acm2_ChGetAODataByRingNo(U32 RingNo, U32 SubDeviceID, U32 AoChannel, DAQ_DATA_TYPE Type, PF64 AoData)"""
    @staticmethod
    def Acm2_ChGetAOStatusByRingNo(RingNo: int, SubDeviceID: int, AoChannel: int, ChanStatus: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetAOStatusByRingNo(U32 RingNo, U32 SubDeviceID, U32 AoChannel, PU32 ChanStatus)"""
    @staticmethod
    def Acm2_ChGetAIStatus(AiChannel: int, ChanStatus: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetAIStatus(U32 AiChannel, PU32 ChanStatus)"""
    @staticmethod
    def Acm2_ChGetAIData(AiChannel: int, Type: DAQ_DATA_TYPE | int, AiData: _PtrArg[c_double], /) -> int:
        """U32 Acm2_ChGetAIData(U32 AiChannel, DAQ_DATA_TYPE Type, PF64 AiData)"""
    @staticmethod
    def Acm2_ChGetAIStatusByRingNo(RingNo: int, SubDeviceID: int, AiChannel: int, ChanStatus: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetAIStatusByRingNo(U32 RingNo, U32 SubDeviceID, U32 AiChannel, PU32 ChanStatus)"""
    @staticmethod
    def Acm2_ChGetAIDataByRingNo(RingNo: int, SubDeviceID: int, AiChannel: int, Type: DAQ_DATA_TYPE | int, AiData: _PtrArg[c_double], /) -> int:
        """U32 Acm2_ChGetAIDataByRingNo(U32 RingNo, U32 SubDeviceID, U32 AiChannel, DAQ_DATA_TYPE Type, PF64 AiData)"""
    @staticmethod
    def Acm2_ChSetScaledProperty(ChID: int, ObjType: ADV_OBJ_TYPE | int, UpperBound: float, LowerBound: float, Resolution: int, TransType: DAQ_TRANS_TYPE | int, /) -> int:
        """U32 Acm2_ChSetScaledProperty(U32 ChID, ADV_OBJ_TYPE ObjType, F64 UpperBound, F64 LowerBound, U32 Resolution, DAQ_TRANS_TYPE TransType)"""
    @staticmethod
    def Acm2_ChGetCntData(CntChannel: int, CounterData: _PtrArg[c_double], /) -> int:
        """U32 Acm2_ChGetCntData(U32 CntChannel, PF64 CounterData)"""
    @staticmethod
    def Acm2_ChSetCntData(CntChannel: int, CounterData: float, /) -> int:
        """U32 Acm2_ChSetCntData(U32 CntChannel, F64 CounterData)"""
    @staticmethod
    def Acm2_ChLinkCmpFIFO(ChID: int, AxisArray: _PtrArg[c_uint32], ArrayElement: int, /) -> int:
        """U32 Acm2_ChLinkCmpFIFO(U32 ChID, PU32 AxisArray, U32 ArrayElement)"""
    @staticmethod
    def Acm2_ChLinkCmpObject(ChID: int, ObjType: ADV_OBJ_TYPE | int, ObjArray: _PtrArg[c_uint32], ArrayElement: int, /) -> int:
        """U32 Acm2_ChLinkCmpObject(U32 ChID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)"""
    @staticmethod
    def Acm2_ChGetLinkedCmpObject(ChID: int, ObjType: _PtrArg[c_uint], ObjArray: _PtrArg[c_uint32], ArrayElement: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetLinkedCmpObject(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)"""
    @staticmethod
    def Acm2_ChLinkSWCmp(SWCmpID: int, DOChannel: int, /) -> int:
        """U32 Acm2_ChLinkSWCmp(U32 SWCmpID, U32 DOChannel)"""
    @staticmethod
    def Acm2_ChGetLinkedSWCmp(SWCmpID: int, DOChannel: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetLinkedSWCmp(U32 SWCmpID, PU32 DOChannel)"""
    @staticmethod
    def Acm2_ChEnableCmp(ChID: int, Enable: int, /) -> int:
        """U32 Acm2_ChEnableCmp(U32 ChID, U32 Enable)"""
    @staticmethod
    def Acm2_ChSetCmpOut(ChID: int, OnOff: DO_ONOFF | int, /) -> int:
        """U32 Acm2_ChSetCmpOut(U32 ChID, DO_ONOFF OnOff)"""
    @staticmethod
    def Acm2_ChSetCmpDoOut(ChID: int, OnOff: DO_ONOFF | int, /) -> int:
        """U32 Acm2_ChSetCmpDoOut(U32 ChID, DO_ONOFF OnOff)"""
    @staticmethod
    def Acm2_AxGetCmpData(AxID: int, CmpData: _PtrArg[c_double], /) -> int:
        """U32 Acm2_AxGetCmpData(U32 AxID, PF64 CmpData)"""
    @staticmethod
    def Acm2_ChGetCmpData(ChID: int, CmpData: _PtrArg[c_double], ObjectArrayCount: int, /) -> int:
        """U32 Acm2_ChGetCmpData(U32 ChID, PF64 CmpData, U32 ObjectArrayCount)"""
    @staticmethod
    def Acm2_AxSetCmpTable(AxID: int, TableArray: _PtrArg[c_double], ArrayElement: int, /) -> int:
        """U32 Acm2_AxSetCmpTable(U32 AxID, PF64 TableArray, U32 ArrayElement)"""
    @staticmethod
    def Acm2_AxSetCmpAuto(AxID: int, StartPosition: float, EndPosition: float, Interval: float, /) -> int:
        """U32 Acm2_AxSetCmpAuto(U32 AxID, F64 StartPosition, F64 EndPosition, F64 Interval)"""
    @staticmethod
    def Acm2_ChSetCmpAuto(ChID: int, StartPosition: float, EndPosition: float, Interval: float, /) -> int:
        """U32 Acm2_ChSetCmpAuto(U32 ChID, F64 StartPosition, F64 EndPosition, F64 Interval)"""
    @staticmethod
    def Acm2_ChSetCmpBufferData(ChID: int, TableArray: _PtrArg[c_double], ArrayCount: int, /) -> int:
        """U32 Acm2_ChSetCmpBufferData(U32 ChID, PF64 TableArray, U32 ArrayCount)"""
    @staticmethod
    def Acm2_ChSetMultiCmpTable(ChID: int, TableArray: _PtrArg[c_double], ObjectArrayCount: int, DataArrayCount: int, /) -> int:
        """U32 Acm2_ChSetMultiCmpTable(U32 ChID, PF64 TableArray, U32 ObjectArrayCount, U32 DataArrayCount)"""
    @staticmethod
    def Acm2_ChSetMultiCmpBufferData(ChID: int, MultiCmpTable: _PtrArg[c_double], ObjectArrayCount: int, DataArrayCount: int, /) -> int:
        """U32 Acm2_ChSetMultiCmpBufferData(U32 ChID, PF64 MultiCmpTable, U32 ObjectArrayCount, U32 DataArrayCount)"""
    @staticmethod
    def Acm2_ChResetCmpData(ChID: int, /) -> int:
        """U32 Acm2_ChResetCmpData(U32 ChID)"""
    @staticmethod
    def Acm2_ChGetCmpBufferStatus(ChID: int, BufferStatus: _PtrArg[BUFFER_STATUS], /) -> int:
        """U32 Acm2_ChGetCmpBufferStatus(U32 ChID, PBUFFER_STATUS BufferStatus)"""
    @staticmethod
    def Acm2_ChGetCmpCounter(ChID: int, CmpCounter: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetCmpCounter(U32 ChID, PU32 CmpCounter)"""
    @staticmethod
    def Acm2_ChLinkLatchAxis(ChID: int, AxisArray: _PtrArg[c_uint32], ArrayElement: int, /) -> int:
        """U32 Acm2_ChLinkLatchAxis(U32 ChID, PU32 AxisArray, U32 ArrayElement)"""
    @staticmethod
    def Acm2_ChLinkLatchObject(ChID: int, ObjType: ADV_OBJ_TYPE | int, ObjArray: _PtrArg[c_uint32], ArrayElement: int, /) -> int:
        """U32 Acm2_ChLinkLatchObject(U32 ChID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)"""
    @staticmethod
    def Acm2_ChGetLinkedLatchObject(ChID: int, ObjType: _PtrArg[c_uint], ObjArray: _PtrArg[c_uint32], ArrayElement: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetLinkedLatchObject(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)"""
    @staticmethod
    def Acm2_ChTriggerLatch(ChID: int, /) -> int:
        """U32 Acm2_ChTriggerLatch(U32 ChID)"""
    @staticmethod
    def Acm2_AxReadLatchBuffer(AxID: int, LatchDataArray: _PtrArg[c_double], DataCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_AxReadLatchBuffer(U32 AxID, PF64 LatchDataArray, PU32 DataCnt)"""
    @staticmethod
    def Acm2_ChReadLatchBuffer(ChID: int, LatchDataArray: _PtrArg[c_double], ObjectArrayCount: int, DataArrayCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChReadLatchBuffer(U32 ChID, PF64 LatchDataArray, U32 ObjectArrayCount, PU32 DataArrayCount)"""
    @staticmethod
    def Acm2_AxGetLatchBufferStatus(AxID: int, RemainCnt: _PtrArg[c_uint32], SpaceCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_AxGetLatchBufferStatus(U32 AxID, PU32 RemainCnt, PU32 SpaceCnt)"""
    @staticmethod
    def Acm2_ChGetLatchBufferStatus(ChID: int, BufferStatus: _PtrArg[BUFFER_STATUS], /) -> int:
        """U32 Acm2_ChGetLatchBufferStatus(U32 ChID, PBUFFER_STATUS BufferStatus)"""
    @staticmethod
    def Acm2_AxResetLatchBuffer(AxID: int, /) -> int:
        """U32 Acm2_AxResetLatchBuffer(U32 AxID)"""
    @staticmethod
    def Acm2_ChResetLatchBuffer(ChID: int, /) -> int:
        """U32 Acm2_ChResetLatchBuffer(U32 ChID)"""
    @staticmethod
    def Acm2_ChLinkPWMTable(ChID: int, ObjType: ADV_OBJ_TYPE | int, ObjID: int, /) -> int:
        """U32 Acm2_ChLinkPWMTable(U32 ChID, ADV_OBJ_TYPE ObjType, U32 ObjID)"""
    @staticmethod
    def Acm2_ChLinkPWMTableObject(ChID: int, ObjType: ADV_OBJ_TYPE | int, ObjArray: _PtrArg[c_uint32], ArrayElement: int, /) -> int:
        """U32 Acm2_ChLinkPWMTableObject(U32 ChID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)"""
    @staticmethod
    def Acm2_ChGetLinkedPWMTable(ChID: int, ObjType: _PtrArg[c_uint], ObjArray: _PtrArg[c_uint32], ArrayElement: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetLinkedPWMTable(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)"""
    @staticmethod
    def Acm2_ChSetPWMTable(ChID: int, VelocityArray: _PtrArg[c_double], PWMArray: _PtrArg[c_double], ArrayElements: int, /) -> int:
        """U32 Acm2_ChSetPWMTable(U32 ChID, PF64 VelocityArray, PF64 PWMArray, U32 ArrayElements)"""
    @staticmethod
    def Acm2_ChLoadPWMTableFile(ChID: int, FilePath: bytes | Array[c_char] | None, PointsCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChLoadPWMTableFile(U32 ChID, PI8 FilePath, PU32 PointsCount)"""
    @staticmethod
    def Acm2_ChGetPWMTableStatus(ChID: int, PWMStatus: _PtrArg[PWM_TABLE_STATUS], /) -> int:
        """U32 Acm2_ChGetPWMTableStatus(U32 ChID, PWM_TABLE_STATUS *PWMStatus)"""
    @staticmethod
    def Acm2_ChGetExtDriveData(ExtChannel: int, CounterData: _PtrArg[c_double], /) -> int:
        """U32 Acm2_ChGetExtDriveData(U32 ExtChannel, PF64 CounterData)"""
    @staticmethod
    def Acm2_ChSetExtDriveData(ExtChannel: int, CounterData: float, /) -> int:
        """U32 Acm2_ChSetExtDriveData(U32 ExtChannel, F64 CounterData)"""
    @staticmethod
    def Acm2_ChLinkExtDriveObject(ChID: int, ObjType: ADV_OBJ_TYPE | int, ObjID: int, /) -> int:
        """U32 Acm2_ChLinkExtDriveObject(U32 ChID, ADV_OBJ_TYPE ObjType, U32 ObjID)"""
    @staticmethod
    def Acm2_ChGetLinkedExtDriveObject(ChID: int, ObjType: _PtrArg[c_uint], ObjArray: _PtrArg[c_uint32], ArrayElement: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_ChGetLinkedExtDriveObject(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)"""
    @staticmethod
    def Acm2_DevMDaqConfig(ChannelID: int, Period: int, AxisNo: int, Method: int, ChanType: int, Count: int, /) -> int:
        """U32 Acm2_DevMDaqConfig(U32 ChannelID, U32 Period, U32 AxisNo, U32 Method, U32 ChanType, U32 Count)"""
    @staticmethod
    def Acm2_DevMDaqGetConfig(ChannelID: int, Period: _PtrArg[c_uint32], AxisNo: _PtrArg[c_uint32], Method: _PtrArg[c_uint32], ChanType: _PtrArg[c_uint32], Count: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_DevMDaqGetConfig(U32 ChannelID, PU32 Period, PU32 AxisNo, PU32 Method, PU32 ChanType, PU32 Count)"""
    @staticmethod
    def Acm2_DevMDaqStart(DevID: int, /) -> int:
        """U32 Acm2_DevMDaqStart(U32 DevID)"""
    @staticmethod
    def Acm2_DevMDaqStop(DevID: int, /) -> int:
        """U32 Acm2_DevMDaqStop(U32 DevID)"""
    @staticmethod
    def Acm2_DevMDaqReset(ChannelID: int, /) -> int:
        """U32 Acm2_DevMDaqReset(U32 ChannelID)"""
    @staticmethod
    def Acm2_DevMDaqGetStatus(ChannelID: int, CurrentCnt: _PtrArg[c_uint32], Status: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_DevMDaqGetStatus(U32 ChannelID, PU32 CurrentCnt, PU32 Status)"""
    @staticmethod
    def Acm2_DevMDaqGetData(ChannelID: int, StartIndex: int, MaxCount: int, DataBuffer: _PtrArg[c_double], /) -> int:
        """U32 Acm2_DevMDaqGetData(U32 ChannelID, U32 StartIndex, U32 MaxCount, PF64 DataBuffer)"""
    @staticmethod
    def Acm2_DevLoadENI(RingNo: int, ENIFile: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm2_DevLoadENI(U32 RingNo, PI8 ENIFile)"""
    @staticmethod
    def Acm2_DevConnect(RingNo: int, /) -> int:
        """U32 Acm2_DevConnect(U32 RingNo)"""
    @staticmethod
    def Acm2_DevDisConnect(RingNo: int, /) -> int:
        """U32 Acm2_DevDisConnect(U32 RingNo)"""
    @staticmethod
    def Acm2_DevGetSubDevicesID(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceIDArray: _PtrArg[c_uint32], SubDeviceCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_DevGetSubDevicesID(U32 RingNo, ECAT_ID_TYPE IDType, PU32 SubDeviceIDArray, PU32 SubDeviceCnt)"""
    @staticmethod
    def Acm2_DevGetMDeviceInfo(RingNo: int, pMDeviceInfo: _PtrArg[ADVAPI_MDEVICE_INFO], /) -> int:
        """U32 Acm2_DevGetMDeviceInfo(U32 RingNo, PADVAPI_MDEVICE_INFO pMDeviceInfo)"""
    @staticmethod
    def Acm2_DevGetSubDeviceInfo(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, pInfo: _PtrArg[ADVAPI_SUBDEVICE_INFO_CM2], /) -> int:
        """U32 Acm2_DevGetSubDeviceInfo(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, PADVAPI_SUBDEVICE_INFO_CM2 pInfo)"""
    @staticmethod
    def Acm2_DevGetSubDeviceDataCnt(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, DataType: int, DataCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_DevGetSubDeviceDataCnt(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 DataType, PU32 DataCnt)"""
    @staticmethod
    def Acm2_DevGetSubDeviceFwVersion(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, VersionInfo: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm2_DevGetSubDeviceFwVersion(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, OUT PI8 VersionInfo)"""
    @staticmethod
    def Acm2_DevSetSubDeviceID(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, SubDeviceNewID: int, /) -> int:
        """U32 Acm2_DevSetSubDeviceID(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 SubDeviceNewID)"""
    @staticmethod
    def Acm2_DevSetSubDeviceStates(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, SubDeviceState: int, /) -> int:
        """U32 Acm2_DevSetSubDeviceStates(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 SubDeviceState)"""
    @staticmethod
    def Acm2_DevGetSubDeviceStates(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, SubDeviceState: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_DevGetSubDeviceStates(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, PU32 SubDeviceState)"""
    @staticmethod
    def Acm2_DevWriteSDOComplete(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, Index: int, DataSize: int, pValue: _VoidPtrArg, /) -> int:
        """U32 Acm2_DevWriteSDOComplete(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 DataSize, PVOID pValue)"""
    @staticmethod
    def Acm2_DevWriteSDO(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, Index: int, SubIndex: int, Type: int, DataSize: int, pValue: _VoidPtrArg, /) -> int:
        """U32 Acm2_DevWriteSDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, IN PVOID pValue)"""
    @staticmethod
    def Acm2_DevReadSDO(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, Index: int, SubIndex: int, Type: int, DataSize: int, pValue: _VoidPtrArg, /) -> int:
        """U32 Acm2_DevReadSDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, OUT PVOID pValue)"""
    @staticmethod
    def Acm2_DevWritePDO(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, Index: int, SubIndex: int, Type: int, DataSize: int, pValue: _VoidPtrArg, /) -> int:
        """U32 Acm2_DevWritePDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, IN PVOID pValue)"""
    @staticmethod
    def Acm2_DevReadPDO(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, Index: int, SubIndex: int, Type: int, DataSize: int, pValue: _VoidPtrArg, /) -> int:
        """U32 Acm2_DevReadPDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, OUT PVOID pValue)"""
    @staticmethod
    def Acm2_DevWriteReg(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, Address: int, Type: int, DataSize: int, pValue: _VoidPtrArg, /) -> int:
        """U32 Acm2_DevWriteReg(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Address, U32 Type, U32 DataSize, IN PVOID pValue)"""
    @staticmethod
    def Acm2_DevReadReg(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, Address: int, Type: int, DataSize: int, pValue: _VoidPtrArg, /) -> int:
        """U32 Acm2_DevReadReg(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Address, U32 Type, U32 DataSize, OUT PVOID pValue)"""
    @staticmethod
    def Acm2_DevWriteFoE(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, FileName: bytes | Array[c_char] | None, FilePath: bytes | Array[c_char] | None, Password: int, /) -> int:
        """U32 Acm2_DevWriteFoE(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, PI8 FileName, PI8 FilePath, U32 Password)"""
    @staticmethod
    def Acm2_DevReadSubDeviceCommErrCnt(RingNo: int, ErrCntArray: _PtrArg[c_uint32], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_DevReadSubDeviceCommErrCnt(U32 RingNo, PU32 ErrCntArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm2_DevSaveAllMapFile(FilePath: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm2_DevSaveAllMapFile(PI8 FilePath)"""
    @staticmethod
    def Acm2_DevSaveMapFile(RingNo: int, FilePath: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm2_DevSaveMapFile(U32 RingNo, PI8 FilePath)"""
    @staticmethod
    def Acm2_DevLoadAllMapFile(FilePath: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm2_DevLoadAllMapFile(PI8 FilePath)"""
    @staticmethod
    def Acm2_DevLoadMapFile(RingNo: int, FilePath: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm2_DevLoadMapFile(U32 RingNo, PI8 FilePath)"""
    @staticmethod
    def Acm2_Ax1DCompensateTable(AxID: int, OriginPos: float, Pitch: float, OffsetData: _PtrArg[c_double], OffsetElements: int, Direction: int, /) -> int:
        """U32 Acm2_Ax1DCompensateTable(U32 AxID, F64 OriginPos, F64 Pitch, PF64 OffsetData, U32 OffsetElements, U32 Direction)"""
    @staticmethod
    def Acm2_Ax2DCompensateTable(AxID: int, RelAxID: int, OriginPosX: float, OriginPosY: float, PitchX: float, PitchY: float, OffsetDataX: _PtrArg[c_double], OffsetDataY: _PtrArg[c_double], OffsetElementsX: int, OffsetElementsY: int, /) -> int:
        """U32 Acm2_Ax2DCompensateTable(U32 AxID, U32 RelAxID, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataX, PF64 OffsetDataY, U32 OffsetElementsX, U32 OffsetElementsY)"""
    @staticmethod
    def Acm2_AxZAxisCompensateTable(AxID: int, RelAxID: int, ZAxID: int, OriginPosX: float, OriginPosY: float, PitchX: float, PitchY: float, OffsetDataZ: _PtrArg[c_double], OffsetElementsX: int, OffsetElementsY: int, /) -> int:
        """U32 Acm2_AxZAxisCompensateTable(U32 AxID, U32 RelAxID, U32 ZAxID, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataZ, U32 OffsetElementsX, U32 OffsetElementsY)"""
    @staticmethod
    def Acm2_AxGetCompensatePosition(AxID: int, Position: _PtrArg[c_double], /) -> int:
        """U32 Acm2_AxGetCompensatePosition(U32 AxID, PF64 Position)"""
    @staticmethod
    def Acm2_AxGetPreview1DCompensatePosition(AxID: int, Position: float, Direction: int, PreviewPosition: _PtrArg[c_double], /) -> int:
        """U32 Acm2_AxGetPreview1DCompensatePosition(U32 AxID, F64 Position, U32 Direction, PF64 PreviewPosition)"""
    @staticmethod
    def Acm2_AxGetPreview2DCompensatePosition(AxID: int, RelAxID: int, Position: float, RelPosition: float, Direction: int, RelDirection: int, PreviewPosition: _PtrArg[c_double], PreviewRelPosition: _PtrArg[c_double], /) -> int:
        """U32 Acm2_AxGetPreview2DCompensatePosition(U32 AxID, U32 RelAxID, F64 Position, F64 RelPosition, U32 Direction, U32 RelDirection, PF64 PreviewPosition, PF64 PreviewRelPosition)"""
    @staticmethod
    def Acm2_AxGetPreviewZAxisCompensatePosition(AxID: int, RelAxID: int, ZAxID: int, Position: float, RelPosition: float, Direction: int, RelDirection: int, PreviewZPosition: _PtrArg[c_double], /) -> int:
        """U32 Acm2_AxGetPreviewZAxisCompensatePosition(U32 AxID, U32 RelAxID, U32 ZAxID, F64 Position, F64 RelPosition, U32 Direction, U32 RelDirection, PF64 PreviewZPosition)"""
    @staticmethod
    def Acm2_DevMultiTrigInitial(RingNo: int, IDType: ECAT_ID_TYPE | int, SubDeviceID: int, Enable: int, PWM: int, LTC: int, MPG: int, /) -> int:
        """U32 Acm2_DevMultiTrigInitial(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Enable, U32 PWM, U32 LTC, U32 MPG)"""
    @staticmethod
    def Acm2_DevOscChannelDataStart() -> int:
        """U32 Acm2_DevOscChannelDataStart()"""
    @staticmethod
    def Acm2_DevOscChannelDataStop() -> int:
        """U32 Acm2_DevOscChannelDataStop()"""
    @staticmethod
    def Acm2_DevGetOscChannelDataConfig(ChannelID: int, oscflg: _PtrArg[OSC_PROFILE_PRM], /) -> int:
        """U32 Acm2_DevGetOscChannelDataConfig(U32 ChannelID, POSC_PROFILE_PRM oscflg)"""
    @staticmethod
    def Acm2_DevSetOscChannelDataConfig(ChannelID: int, oscflg: OSC_PROFILE_PRM, /) -> int:
        """U32 Acm2_DevSetOscChannelDataConfig(U32 ChannelID, OSC_PROFILE_PRM oscflg)"""
    @staticmethod
    def Acm2_DevGetOscChannelData(ChannelID: int, DataIndex: int, MaxCount: _PtrArg[c_uint32], DataBuffer: _PtrArg[c_double], /) -> int:
        """U32 Acm2_DevGetOscChannelData(U32 ChannelID, U32 DataIndex, PU32 MaxCount, PF64 DataBuffer)"""
    @staticmethod
    def Acm2_DevGetOscChannelStatus(Status: _PtrArg[c_uint32], /) -> int:
        """U32 Acm2_DevGetOscChannelStatus(PU32 Status)"""

class AdvCmnAPI:
    @staticmethod
    def Acm_GetAvailableDevs(DeviceList: _PtrArg[DEVLIST], MaxEntries: int, OutEntries: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GetAvailableDevs(DEVLIST *DeviceList, U32 MaxEntries, PU32 OutEntries)"""
    @staticmethod
    def Acm_GetErrorMessage(ErrorCode: int, lpszError: bytes | Array[c_char] | None, nMaxError: int, /) -> bool:
        """BOOL Acm_GetErrorMessage(U32 ErrorCode, PI8 lpszError, U32 nMaxError)"""
    @staticmethod
    def Acm_GetNewErrorMessage(ErrorCode2: int, lpszError: bytes | Array[c_char] | None, nMaxError: int, /) -> int:
        """U32 Acm_GetNewErrorMessage(U32 ErrorCode2, PI8 lpszError, U32 nMaxError)"""
    @staticmethod
    def Acm_DevOpen(DeviceNumber: int, DeviceHandle: _PtrArg[c_void_p], /) -> int:
        """U32 Acm_DevOpen(U32 DeviceNumber, PHAND DeviceHandle)"""
    @staticmethod
    def Acm_DevECATOpen(DeviceNumber: int, Ring0SlaveCount: int, Ring1SlaveCount: int, Timeout: int, DeviceHandle: _PtrArg[c_void_p], /) -> int:
        """U32 Acm_DevECATOpen(U32 DeviceNumber, U16 Ring0SlaveCount, U16 Ring1SlaveCount, U16 Timeout, PHAND DeviceHandle)"""
    @staticmethod
    def Acm_DevReOpen(DeviceHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_DevReOpen(HAND DeviceHandle)"""
    @staticmethod
    def Acm_DevClose(DeviceHandle: _PtrArg[c_void_p], /) -> int:
        """U32 Acm_DevClose(PHAND DeviceHandle)"""
    @staticmethod
    def Acm_GetLastError(Handle: _VoidPtrArg, /) -> int:
        """U32 Acm_GetLastError(HAND Handle)"""
    @staticmethod
    def Acm_GetProperty(Handle: _VoidPtrArg, PropertyID: int, Buffer: _VoidPtrArg, BufferLength: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GetProperty(HAND Handle, U32 PropertyID, PVOID Buffer, PU32 BufferLength)"""
    @staticmethod
    def Acm_SetProperty(Handle: _VoidPtrArg, PropertyID: int, Buffer: _VoidPtrArg, BufferLength: int, /) -> int:
        """U32 Acm_SetProperty(HAND Handle, U32 PropertyID, PVOID Buffer, U32 BufferLength)"""
    @staticmethod
    def Acm_GetU32Property(Handle: _VoidPtrArg, PropertyID: int, Value: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GetU32Property(HAND Handle, U32 PropertyID, PU32 Value)"""
    @staticmethod
    def Acm_GetI32Property(Handle: _VoidPtrArg, PropertyID: int, Value: _PtrArg[c_int32], /) -> int:
        """U32 Acm_GetI32Property(HAND Handle, U32 PropertyID, PI32 Value)"""
    @staticmethod
    def Acm_GetF64Property(Handle: _VoidPtrArg, PropertyID: int, Value: _PtrArg[c_double], /) -> int:
        """U32 Acm_GetF64Property(HAND Handle, U32 PropertyID, PF64 Value)"""
    @staticmethod
    def Acm_GetStringProperty(Handle: _VoidPtrArg, PropertyID: int, Value: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_GetStringProperty(HAND Handle, U32 PropertyID, PU8 Value)"""
    @staticmethod
    def Acm_SetU32Property(Handle: _VoidPtrArg, PropertyID: int, Value: int, /) -> int:
        """U32 Acm_SetU32Property(HAND Handle, U32 PropertyID, U32 Value)"""
    @staticmethod
    def Acm_SetI32Property(Handle: _VoidPtrArg, PropertyID: int, Value: int, /) -> int:
        """U32 Acm_SetI32Property(HAND Handle, U32 PropertyID, I32 Value)"""
    @staticmethod
    def Acm_SetF64Property(Handle: _VoidPtrArg, PropertyID: int, Value: float, /) -> int:
        """U32 Acm_SetF64Property(HAND Handle, U32 PropertyID, F64 Value)"""
    @staticmethod
    def Acm_SetStringProperty(Handle: _VoidPtrArg, PropertyID: int, Value: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_SetStringProperty(HAND Handle, U32 PropertyID, PU8 Value)"""
    @staticmethod
    def Acm_GetMultiProperty(Handle: _VoidPtrArg, PropertyIDArray: _PtrArg[c_uint32], ValueArray: _PtrArg[c_double], PropertyCnt: int, ErrorBuffer: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GetMultiProperty(HAND Handle, PU32 PropertyIDArray, PF64 ValueArray, U32 PropertyCnt, PU32 ErrorBuffer)"""
    @staticmethod
    def Acm_SetMultiProperty(Handle: _VoidPtrArg, PropertyIDArray: _PtrArg[c_uint32], ValueArray: _PtrArg[c_double], PropertyCnt: int, ErrorBuffer: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_SetMultiProperty(HAND Handle, PU32 PropertyIDArray, PF64 ValueArray, U32 PropertyCnt, PU32 ErrorBuffer)"""
    @staticmethod
    def Acm_SetMultiU32Property(Handle: _VoidPtrArg, PropertyIDArray: _PtrArg[c_uint32], ValueArray: _PtrArg[c_uint32], PropertyCnt: int, /) -> int:
        """U32 Acm_SetMultiU32Property(HAND Handle, PU32 PropertyIDArray, PU32 ValueArray, U32 PropertyCnt)"""
    @staticmethod
    def Acm_SetMultiI32Property(Handle: _VoidPtrArg, PropertyIDArray: _PtrArg[c_uint32], ValueArray: _PtrArg[c_int32], PropertyCnt: int, /) -> int:
        """U32 Acm_SetMultiI32Property(HAND Handle, PU32 PropertyIDArray, PI32 ValueArray, U32 PropertyCnt)"""
    @staticmethod
    def Acm_SetMultiF64Property(Handle: _VoidPtrArg, PropertyIDArray: _PtrArg[c_uint32], ValueArray: _PtrArg[c_double], PropertyCnt: int, /) -> int:
        """U32 Acm_SetMultiF64Property(HAND Handle, PU32 PropertyIDArray, PF64 ValueArray, U32 PropertyCnt)"""
    @staticmethod
    def Acm_GetChannelProperty(Handle: _VoidPtrArg, ChannelID: int, PropertyID: int, Value: _PtrArg[c_double], /) -> int:
        """U32 Acm_GetChannelProperty(HAND Handle, U32 ChannelID, U32 PropertyID, PF64 Value)"""
    @staticmethod
    def Acm_SetChannelProperty(Handle: _VoidPtrArg, ChannelID: int, PropertyID: int, Value: float, /) -> int:
        """U32 Acm_SetChannelProperty(HAND Handle, U32 ChannelID, U32 PropertyID, F64 Value)"""
    @staticmethod
    def Acm_GetMultiChannelProperty(Handle: _VoidPtrArg, PropertyID: int, StartChID: int, ChCount: int, ValueArray: _PtrArg[c_double], /) -> int:
        """U32 Acm_GetMultiChannelProperty(HAND Handle, U32 PropertyID, U32 StartChID, U32 ChCount, PF64 ValueArray)"""
    @staticmethod
    def Acm_SetMultiChannelProperty(Handle: _VoidPtrArg, PropertyID: int, StartChID: int, ChCount: int, ValueArray: _PtrArg[c_double], /) -> int:
        """U32 Acm_SetMultiChannelProperty(HAND Handle, U32 PropertyID, U32 StartChID, U32 ChCount, PF64 ValueArray)"""
    @staticmethod
    def Acm_DevEnableEvent(DeviceHandle: _VoidPtrArg, DevEnableEvt: int, /) -> int:
        """U32 Acm_DevEnableEvent(HAND DeviceHandle, U32 DevEnableEvt)"""
    @staticmethod
    def Acm_DevCheckEvent(DeviceHandle: _VoidPtrArg, DevCheckEvt: _PtrArg[c_uint32], Millisecond: int, /) -> int:
        """U32 Acm_DevCheckEvent(HAND DeviceHandle, PU32 DevCheckEvt, U32 Millisecond)"""
    @staticmethod
    def Acm_EnableMotionEvent(DeviceHandle: _VoidPtrArg, AxEnableEvtArray: _PtrArg[c_uint32], GpEnableEvtArray: _PtrArg[c_uint32], AxArrayElements: int, GpArrayElements: int, /) -> int:
        """U32 Acm_EnableMotionEvent(HAND DeviceHandle, PU32 AxEnableEvtArray, PU32 GpEnableEvtArray, U32 AxArrayElements, U32 GpArrayElements)"""
    @staticmethod
    def Acm_CheckMotionEvent(DeviceHandle: _VoidPtrArg, AxEvtStatusArray: _PtrArg[c_uint32], GpEvtStatusArray: _PtrArg[c_uint32], AxArrayElements: int, GpArrayElements: int, Millisecond: int, /) -> int:
        """U32 Acm_CheckMotionEvent(HAND DeviceHandle, PU32 AxEvtStatusArray, PU32 GpEvtStatusArray, U32 AxArrayElements, U32 GpArrayElements, U32 Millisecond)"""
    @staticmethod
    def Acm_CancelCheckEvent(ObjectHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_CancelCheckEvent(HAND ObjectHandle)"""
    @staticmethod
    def Acm_DevEnableEvent_All(DeviceHandle: _VoidPtrArg, DevEnableEvtArray: _PtrArg[c_uint32], AxEnableEvtArray: _PtrArg[c_uint32], GpEnableEvtArray: _PtrArg[c_uint32], AxArrayElements: int, GpArrayElements: int, /) -> int:
        """U32 Acm_DevEnableEvent_All(HAND DeviceHandle, PU32 DevEnableEvtArray, PU32 AxEnableEvtArray, PU32 GpEnableEvtArray, U32 AxArrayElements, U32 GpArrayElements)"""
    @staticmethod
    def Acm_DevCheckEvent_All(DeviceHandle: _VoidPtrArg, DevEvtStatusArray: _PtrArg[c_uint32], AxEvtStatusArray: _PtrArg[c_uint32], GpEvtStatusArray: _PtrArg[c_uint32], AxArrayElements: int, GpArrayElements: int, Millisecond: int, /) -> int:
        """U32 Acm_DevCheckEvent_All(HAND DeviceHandle, PU32 DevEvtStatusArray, PU32 AxEvtStatusArray, PU32 GpEvtStatusArray, U32 AxArrayElements, U32 GpArrayElements, U32 Millisecond)"""
    @staticmethod
    def Acm_DevLoadConfig(DeviceHandle: _VoidPtrArg, ConfigPath: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm_DevLoadConfig(HAND DeviceHandle, PI8 ConfigPath)"""
    @staticmethod
    def Acm_DevSlaveFwDownload(DeviceHandle: _VoidPtrArg, RingNo: int, Position: int, FileName: bytes | Array[c_char] | None, FilePath: bytes | Array[c_char] | None, Password: int, /) -> int:
        """U32 Acm_DevSlaveFwDownload(HAND DeviceHandle, U16 RingNo, U16 Position, PI8 FileName, PI8 FilePath, U32 Password)"""
    @staticmethod
    def Acm_DevDownloadCAMTable(DeviceHandle: _VoidPtrArg, CamTableID: int, pMasterArray: _PtrArg[c_double], pSlaveArray: _PtrArg[c_double], pPointRangeArray: _PtrArg[c_double], pPointSlopeArray: _PtrArg[c_double], ArrayElements: int, /) -> int:
        """U32 Acm_DevDownloadCAMTable(HAND DeviceHandle, U32 CamTableID, PF64 pMasterArray, PF64 pSlaveArray, PF64 pPointRangeArray, PF64 pPointSlopeArray, U32 ArrayElements)"""
    @staticmethod
    def Acm_DevLoadCAMTableFile(DeviceHandle: _VoidPtrArg, FilePath: bytes | Array[c_char] | None, CamTableID: int, Range: _PtrArg[c_uint32], PointsCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevLoadCAMTableFile(HAND DeviceHandle, PI8 FilePath, U32 CamTableID, PU32 Range, PU32 PointsCount)"""
    @staticmethod
    def Acm_DevConfigCAMTable(DeviceHandle: _VoidPtrArg, CamTableID: int, Periodic: int, MasterAbsolute: int, SlaveAbsolute: int, /) -> int:
        """U32 Acm_DevConfigCAMTable(HAND DeviceHandle, U32 CamTableID, U32 Periodic, U32 MasterAbsolute, U32 SlaveAbsolute)"""
    @staticmethod
    def Acm_DevReadMailBox(Handle: _VoidPtrArg, par_id: int, data_index: int, data_count: int, DataBuffer: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevReadMailBox(HAND Handle, U16 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)"""
    @staticmethod
    def Acm_DevReadMultiMailBox(Handle: _VoidPtrArg, object_id: int, par_id: _PtrArg[c_uint16], DataBuffer: _PtrArg[c_uint32], ErrorBuffer: _PtrArg[c_uint32], ArrayElements: int, /) -> int:
        """U32 Acm_DevReadMultiMailBox(HAND Handle, U8 object_id, PU16 par_id, PU32 DataBuffer, PU32 ErrorBuffer, U32 ArrayElements)"""
    @staticmethod
    def Acm_DevWriteMailBox(Handle: _VoidPtrArg, par_id: int, data_index: int, data_count: int, DataBuffer: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevWriteMailBox(HAND Handle, U16 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)"""
    @staticmethod
    def Acm_DevWriteDPMData(Handle: _VoidPtrArg, par_id: int, data_index: int, data_count: int, DataBuffer: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevWriteDPMData(HAND Handle, U16 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)"""
    @staticmethod
    def Acm_DevWriteMultiMailBox(Handle: _VoidPtrArg, object_id: int, par_id: _PtrArg[c_uint16], DataBuffer: _PtrArg[c_uint32], ErrorBuffer: _PtrArg[c_uint32], ArrayElements: int, /) -> int:
        """U32 Acm_DevWriteMultiMailBox(HAND Handle, U8 object_id, PU16 par_id, PU32 DataBuffer, PU32 ErrorBuffer, U32 ArrayElements)"""
    @staticmethod
    def Acm_WriteRingBuffer(Handle: _VoidPtrArg, cmd_id: int, data_index: int, data_cnt: int, dataBuffer: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_WriteRingBuffer(HAND Handle, U32 cmd_id, U32 data_index, U32 data_cnt, PU32 dataBuffer)"""
    @staticmethod
    def Acm_ReadRingBuffer(Handle: _VoidPtrArg, cmd_id: _PtrArg[c_uint32], data_index: _PtrArg[c_uint32], data_cnt: int, dataBuffer: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_ReadRingBuffer(HAND Handle, PU32 cmd_id, PU32 data_index, U32 data_cnt, PU32 dataBuffer)"""
    @staticmethod
    def Acm_LoadENI(DeviceHandle: _VoidPtrArg, FilePath: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm_LoadENI(HAND DeviceHandle, PI8 FilePath)"""
    @staticmethod
    def Acm_DevLoadENI(DeviceHandle: _VoidPtrArg, RingNo: int, FilePath: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm_DevLoadENI(HAND DeviceHandle, U16 RingNo, PI8 FilePath)"""
    @staticmethod
    def Acm_DevConnect(DeviceHandle: _VoidPtrArg, RingNo: int, /) -> int:
        """U32 Acm_DevConnect(HAND DeviceHandle, U16 RingNo)"""
    @staticmethod
    def Acm_DevDisConnect(DeviceHandle: _VoidPtrArg, RingNo: int, /) -> int:
        """U32 Acm_DevDisConnect(HAND DeviceHandle, U16 RingNo)"""
    @staticmethod
    def Acm_DevGetComStatus(DeviceHandle: _VoidPtrArg, RingNo: int, pStatus: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_DevGetComStatus(HAND DeviceHandle, U16 RingNo, PU16 pStatus)"""
    @staticmethod
    def Acm_DevGetErrorTable(DeviceHandle: _VoidPtrArg, RingNo: int, ErrorTableArray: _PtrArg[c_uint32], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevGetErrorTable(HAND DeviceHandle, U16 RingNo, PU32 ErrorTableArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm_DevGetMasInfo(DeviceHandle: _VoidPtrArg, pMasInfo: _VoidPtrArg, SlaveIPArray: _PtrArg[c_uint16], SlvCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevGetMasInfo(HAND DeviceHandle, PVOID pMasInfo, PU16 SlaveIPArray, PU32 SlvCnt)"""
    @staticmethod
    def Acm_DevGetMasStates(DeviceHandle: _VoidPtrArg, RingNo: int, SlvCounters: _PtrArg[c_uint16], SlvStates: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_DevGetMasStates(HAND DeviceHandle, U16 RingNo, PU16 SlvCounters, PU16 SlvStates)"""
    @staticmethod
    def Acm_DevGetSlaveInfo(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, pInfo: _VoidPtrArg, /) -> int:
        """U32 Acm_DevGetSlaveInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PVOID pInfo)"""
    @staticmethod
    def Acm_DevGetModuleInfo(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, ModIDArray: _PtrArg[c_uint32], ModCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevGetModuleInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PU32 ModIDArray, PU32 ModCnt)"""
    @staticmethod
    def Acm_DevGetIOInfo(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Slot: int, DataType: int, pInfo: _VoidPtrArg, /) -> int:
        """U32 Acm_DevGetIOInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Slot, U8 DataType, PVOID pInfo)"""
    @staticmethod
    def Acm_DevGetSlaveDataCnt(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, DataType: int, DataCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevGetSlaveDataCnt(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U8 DataType, PU32 DataCnt)"""
    @staticmethod
    def Acm_DevGetSlaveFwVersion(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, VersionInfo: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm_DevGetSlaveFwVersion(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, OUT PI8 VersionInfo)"""
    @staticmethod
    def Acm_DevSetSlaveID(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, SlaveNewIP: int, /) -> int:
        """U32 Acm_DevSetSlaveID(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 SlaveNewIP)"""
    @staticmethod
    def Acm_CheckVersion(DeviceHandle: _VoidPtrArg, VersionID: int, Result: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_CheckVersion(HAND DeviceHandle, U32 VersionID, PU32 Result)"""
    @staticmethod
    def Acm_DevMultiTrigSetPWMTableOnTime(DeviceHandle: _VoidPtrArg, TimeTableArray: _PtrArg[c_uint32], ArrayCount: int, /) -> int:
        """U32 Acm_DevMultiTrigSetPWMTableOnTime(HAND DeviceHandle, PU32 TimeTableArray, U32 ArrayCount)"""
    @staticmethod
    def Acm_DevMultiTrigSetCmpDO(DeviceHandle: _VoidPtrArg, OFForON: int, /) -> int:
        """U32 Acm_DevMultiTrigSetCmpDO(HAND DeviceHandle, U32 OFForON)"""
    @staticmethod
    def Acm_DevMultiTrigForceCmpOut(DeviceHandle: _VoidPtrArg, OFForON: int, /) -> int:
        """U32 Acm_DevMultiTrigForceCmpOut(HAND DeviceHandle, U32 OFForON)"""
    @staticmethod
    def Acm_DevMutiTrigSetCmpDO(DeviceHandle: _VoidPtrArg, OFForON: int, /) -> int:
        """U32 Acm_DevMutiTrigSetCmpDO(HAND DeviceHandle, U32 OFForON)"""
    @staticmethod
    def Acm_DevMutiTrigForceCmpOut(DeviceHandle: _VoidPtrArg, OFForON: int, /) -> int:
        """U32 Acm_DevMutiTrigForceCmpOut(HAND DeviceHandle, U32 OFForON)"""
    @staticmethod
    def Acm_MasStartRing(DeviceHandle: _VoidPtrArg, RingNo: int, /) -> int:
        """U32 Acm_MasStartRing(HAND DeviceHandle, U16 RingNo)"""
    @staticmethod
    def Acm_MasStopRing(DeviceHandle: _VoidPtrArg, RingNo: int, /) -> int:
        """U32 Acm_MasStopRing(HAND DeviceHandle, U16 RingNo)"""
    @staticmethod
    def Acm_MasGetComStatus(DeviceHandle: _VoidPtrArg, RingNo: int, pStatus: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_MasGetComStatus(HAND DeviceHandle, U16 RingNo, PU16 pStatus)"""
    @staticmethod
    def Acm_MasGetComCyclicTime(DeviceHandle: _VoidPtrArg, RingNo: int, pTime: _PtrArg[c_double], /) -> int:
        """U32 Acm_MasGetComCyclicTime(HAND DeviceHandle, U16 RingNo, PF64 pTime)"""
    @staticmethod
    def Acm_MasGetDataCyclicTime(DeviceHandle: _VoidPtrArg, RingNo: int, DataCyclicTime: _PtrArg[c_double], /) -> int:
        """U32 Acm_MasGetDataCyclicTime(HAND DeviceHandle, U16 RingNo, PF64 DataCyclicTime)"""
    @staticmethod
    def Acm_MasGetActiveTable(DeviceHandle: _VoidPtrArg, RingNo: int, ActiveTableArray: _PtrArg[c_uint32], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_MasGetActiveTable(HAND DeviceHandle, U16 RingNo, PU32 ActiveTableArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm_MasGetErrorTable(DeviceHandle: _VoidPtrArg, RingNo: int, ErrorTableArray: _PtrArg[c_uint32], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_MasGetErrorTable(HAND DeviceHandle, U16 RingNo, PU32 ErrorTableArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm_MasGetSlaveInfo(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, pInfo: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_MasGetSlaveInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PU32 pInfo)"""
    @staticmethod
    def Acm_MasLogComStatus(DeviceHandle: _VoidPtrArg, RingNo: int, /) -> int:
        """U32 Acm_MasLogComStatus(HAND DeviceHandle, U16 RingNo)"""
    @staticmethod
    def Acm_MasTrigOut(DeviceHandle: _VoidPtrArg, RingNo: int, /) -> int:
        """U32 Acm_MasTrigOut(HAND DeviceHandle, U16 RingNo)"""
    @staticmethod
    def Acm_MasGetRingStatus(DeviceHandle: _VoidPtrArg, RingNo: int, pStatus: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_MasGetRingStatus(HAND DeviceHandle, U16 RingNo, PU16 pStatus)"""
    @staticmethod
    def Acm_AxOpen(DeviceHandle: _VoidPtrArg, PhyAxis: int, AxisHandle: _PtrArg[c_void_p], /) -> int:
        """U32 Acm_AxOpen(HAND DeviceHandle, U16 PhyAxis, PHAND AxisHandle)"""
    @staticmethod
    def Acm_AxOpenbyID(DeviceHandle: _VoidPtrArg, SlaveID: int, SubID: int, AxisHandle: _PtrArg[c_void_p], /) -> int:
        """U32 Acm_AxOpenbyID(HAND DeviceHandle, U16 SlaveID, U8 SubID, PHAND AxisHandle)"""
    @staticmethod
    def Acm_AxClose(AxisHandle: _PtrArg[c_void_p], /) -> int:
        """U32 Acm_AxClose(PHAND AxisHandle)"""
    @staticmethod
    def Acm_AxSetSvOn(AxisHandle: _VoidPtrArg, OnOff: int, /) -> int:
        """U32 Acm_AxSetSvOn(HAND AxisHandle, U32 OnOff)"""
    @staticmethod
    def Acm_AxSetErcOn(AxisHandle: _VoidPtrArg, OnOff: int, /) -> int:
        """U32 Acm_AxSetErcOn(HAND AxisHandle, U32 OnOff)"""
    @staticmethod
    def Acm_AxResetAlm(AxisHandle: _VoidPtrArg, OnOff: int, /) -> int:
        """U32 Acm_AxResetAlm(HAND AxisHandle, U32 OnOff)"""
    @staticmethod
    def Acm_AxMoveRel(AxisHandle: _VoidPtrArg, Distance: float, /) -> int:
        """U32 Acm_AxMoveRel(HAND AxisHandle, F64 Distance)"""
    @staticmethod
    def Acm_AxMoveRel_T(AxisHandle: _VoidPtrArg, Distance: float, Time: float, Factor: float, /) -> int:
        """U32 Acm_AxMoveRel_T(HAND AxisHandle, F64 Distance, F64 Time, F64 Factor)"""
    @staticmethod
    def Acm_AxMoveRel_SD(AxisHandle: _VoidPtrArg, Distance: float, SDDistance: float, /) -> int:
        """U32 Acm_AxMoveRel_SD(HAND AxisHandle, F64 Distance, F64 SDDistance)"""
    @staticmethod
    def Acm_AxMoveRel_EC(AxisHandle: _VoidPtrArg, Position: float, /) -> int:
        """U32 Acm_AxMoveRel_EC(HAND AxisHandle, F64 Position)"""
    @staticmethod
    def Acm_AxMoveAbs(AxisHandle: _VoidPtrArg, Position: float, /) -> int:
        """U32 Acm_AxMoveAbs(HAND AxisHandle, F64 Position)"""
    @staticmethod
    def Acm_AxMoveAbs_T(AxisHandle: _VoidPtrArg, Position: float, Time: float, Factor: float, /) -> int:
        """U32 Acm_AxMoveAbs_T(HAND AxisHandle, F64 Position, F64 Time, F64 Factor)"""
    @staticmethod
    def Acm_AxMoveAbs_SD(AxisHandle: _VoidPtrArg, Position: float, SDPosition: float, /) -> int:
        """U32 Acm_AxMoveAbs_SD(HAND AxisHandle, F64 Position, F64 SDPosition)"""
    @staticmethod
    def Acm_AxMoveAbs_EC(AxisHandle: _VoidPtrArg, Position: float, /) -> int:
        """U32 Acm_AxMoveAbs_EC(HAND AxisHandle, F64 Position)"""
    @staticmethod
    def Acm_AxMoveVel(AxisHandle: _VoidPtrArg, Direction: int, /) -> int:
        """U32 Acm_AxMoveVel(HAND AxisHandle, U16 Direction)"""
    @staticmethod
    def Acm_AxStopDec(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxStopDec(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxStopEmg(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxStopEmg(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxMoveImpose(AxisHandle: _VoidPtrArg, Position: float, NewVel: float, /) -> int:
        """U32 Acm_AxMoveImpose(HAND AxisHandle, F64 Position, F64 NewVel)"""
    @staticmethod
    def Acm_AxHome(AxisHandle: _VoidPtrArg, HomeMode: int, DirMode: int, /) -> int:
        """U32 Acm_AxHome(HAND AxisHandle, U32 HomeMode, U32 DirMode)"""
    @staticmethod
    def Acm_AxMoveHome(AxisHandle: _VoidPtrArg, HomeMode: int, Dir: int, /) -> int:
        """U32 Acm_AxMoveHome(HAND AxisHandle, U32 HomeMode, U32 Dir)"""
    @staticmethod
    def Acm_AxMoveGantryHome(AxisHandle: _VoidPtrArg, HomeMode: int, Dir: int, /) -> int:
        """U32 Acm_AxMoveGantryHome(HAND AxisHandle, U32 HomeMode, U32 Dir)"""
    @staticmethod
    def Acm_AxPauseMotion(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxPauseMotion(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxResumeMotion(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxResumeMotion(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxChangeVel(AxisHandle: _VoidPtrArg, NewVel: float, /) -> int:
        """U32 Acm_AxChangeVel(HAND AxisHandle, F64 NewVel)"""
    @staticmethod
    def Acm_AxChangePos(AxisHandle: _VoidPtrArg, NewPos: float, /) -> int:
        """U32 Acm_AxChangePos(HAND AxisHandle, F64 NewPos)"""
    @staticmethod
    def Acm_AxChangeVelByRate(AxisHandle: _VoidPtrArg, Rate: int, /) -> int:
        """U32 Acm_AxChangeVelByRate(HAND AxisHandle, U32 Rate)"""
    @staticmethod
    def Acm_AxResetError(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxResetError(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxEnableTrig(AxisHandle: _VoidPtrArg, TrigPrm: int, /) -> int:
        """U32 Acm_AxEnableTrig(HAND AxisHandle, TRIG_PRM TrigPrm)"""
    @staticmethod
    def Acm_AxGetState(AxisHandle: _VoidPtrArg, State: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_AxGetState(HAND AxisHandle, PU16 State)"""
    @staticmethod
    def Acm_AxGetMotionIO(AxisHandle: _VoidPtrArg, Status: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_AxGetMotionIO(HAND AxisHandle, PU32 Status)"""
    @staticmethod
    def Acm_AxGetMotionStatus(AxisHandle: _VoidPtrArg, Status: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_AxGetMotionStatus(HAND AxisHandle, PU32 Status)"""
    @staticmethod
    def Acm_AxGetCmdPosition(AxisHandle: _VoidPtrArg, Position: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetCmdPosition(HAND AxisHandle, PF64 Position)"""
    @staticmethod
    def Acm_AxGetMachPosition(AxisHandle: _VoidPtrArg, Position: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetMachPosition(HAND AxisHandle, PF64 Position)"""
    @staticmethod
    def Acm_AxSetCmdPosition(AxisHandle: _VoidPtrArg, Position: float, /) -> int:
        """U32 Acm_AxSetCmdPosition(HAND AxisHandle, F64 Position)"""
    @staticmethod
    def Acm_AxGetActualPosition(AxisHandle: _VoidPtrArg, Position: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetActualPosition(HAND AxisHandle, PF64 Position)"""
    @staticmethod
    def Acm_AxSetActualPosition(AxisHandle: _VoidPtrArg, Position: float, /) -> int:
        """U32 Acm_AxSetActualPosition(HAND AxisHandle, F64 Position)"""
    @staticmethod
    def Acm_AxGetCmdVelocity(AxisHandle: _VoidPtrArg, Velocity: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetCmdVelocity(HAND AxisHandle, PF64 Velocity)"""
    @staticmethod
    def Acm_AxGetActVelocity(AxisHandle: _VoidPtrArg, Velocity: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetActVelocity(HAND AxisHandle, PF64 Velocity)"""
    @staticmethod
    def Acm_AxGetLagCounter(AxisHandle: _VoidPtrArg, Position: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetLagCounter(HAND AxisHandle, PF64 Position)"""
    @staticmethod
    def Acm_AxSetExtDrive(AxisHandle: _VoidPtrArg, ExtDrvMode: int, /) -> int:
        """U32 Acm_AxSetExtDrive(HAND AxisHandle, U16 ExtDrvMode)"""
    @staticmethod
    def Acm_AxDoSetBit(AxisHandle: _VoidPtrArg, DoChannel: int, BitData: int, /) -> int:
        """U32 Acm_AxDoSetBit(HAND AxisHandle, U16 DoChannel, U8 BitData)"""
    @staticmethod
    def Acm_AxDiSetBit(AxisHandle: _VoidPtrArg, DiChannel: int, BitData: int, /) -> int:
        """U32 Acm_AxDiSetBit(HAND AxisHandle, U16 DiChannel, U8 BitData)"""
    @staticmethod
    def Acm_AxDoGetBit(AxisHandle: _VoidPtrArg, DoChannel: int, BitData: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_AxDoGetBit(HAND AxisHandle, U16 DoChannel, PU8 BitData)"""
    @staticmethod
    def Acm_AxDiGetBit(AxisHandle: _VoidPtrArg, DiChannel: int, BitData: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_AxDiGetBit(HAND AxisHandle, U16 DiChannel, PU8 BitData)"""
    @staticmethod
    def Acm_AxDoSetByte(AxisHandle: _VoidPtrArg, DoPort: int, ByteData: int, /) -> int:
        """U32 Acm_AxDoSetByte(HAND AxisHandle, U16 DoPort, U8 ByteData)"""
    @staticmethod
    def Acm_AxDoGetByte(AxisHandle: _VoidPtrArg, DoPort: int, ByteData: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_AxDoGetByte(HAND AxisHandle, U16 DoPort, PU8 ByteData)"""
    @staticmethod
    def Acm_AxDiGetByte(AxisHandle: _VoidPtrArg, DiPort: int, ByteData: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_AxDiGetByte(HAND AxisHandle, U16 DiPort, PU8 ByteData)"""
    @staticmethod
    def Acm_AxSimStartSuspendVel(AxisHandle: _VoidPtrArg, DriDir: int, /) -> int:
        """U32 Acm_AxSimStartSuspendVel(HAND AxisHandle, U16 DriDir)"""
    @staticmethod
    def Acm_AxSimStartSuspendRel(AxisHandle: _VoidPtrArg, Distance: float, /) -> int:
        """U32 Acm_AxSimStartSuspendRel(HAND AxisHandle, F64 Distance)"""
    @staticmethod
    def Acm_AxSimStartSuspendAbs(AxisHandle: _VoidPtrArg, EndPoint: float, /) -> int:
        """U32 Acm_AxSimStartSuspendAbs(HAND AxisHandle, F64 EndPoint)"""
    @staticmethod
    def Acm_AxSimStart(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxSimStart(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxSimStop(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxSimStop(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxGetLatchData(AxisHandle: _VoidPtrArg, PositionNo: int, Position: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetLatchData(HAND AxisHandle, U32 PositionNo, PF64 Position)"""
    @staticmethod
    def Acm_AxStartSoftLatch(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxStartSoftLatch(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxResetLatch(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxResetLatch(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxGetLatchFlag(AxisHandle: _VoidPtrArg, LatchFlag: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_AxGetLatchFlag(HAND AxisHandle, PU8 LatchFlag)"""
    @staticmethod
    def Acm_AxTriggerLatch(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxTriggerLatch(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxReadLatchBuffer(AxisHandle: _VoidPtrArg, LatchDataArray: _PtrArg[c_double], DataCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_AxReadLatchBuffer(HAND AxisHandle, PF64 LatchDataArray, PU32 DataCnt)"""
    @staticmethod
    def Acm_AxResetLatchBuffer(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxResetLatchBuffer(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxGetLatchBufferStatus(AxisHandle: _VoidPtrArg, RemainCnt: _PtrArg[c_uint32], SpaceCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_AxGetLatchBufferStatus(HAND AxisHandle, PU32 RemainCnt, PU32 SpaceCnt)"""
    @staticmethod
    def Acm_AxCamInAx(AxisHandle: _VoidPtrArg, MasAxisHandle: _VoidPtrArg, MasterOffset: float, SlaveOffset: float, MasterScaling: float, SlaveScaling: float, CamTableID: int, RefSrc: int, /) -> int:
        """U32 Acm_AxCamInAx(HAND AxisHandle, HAND MasAxisHandle, F64 MasterOffset, F64 SlaveOffset, F64 MasterScaling, F64 SlaveScaling, U32 CamTableID, U32 RefSrc)"""
    @staticmethod
    def Acm_AxGearInAx(AxisHandle: _VoidPtrArg, MasAxisHandle: _VoidPtrArg, Numerator: int, Denominator: int, RefSrc: int, Absolute: int, /) -> int:
        """U32 Acm_AxGearInAx(HAND AxisHandle, HAND MasAxisHandle, I32 Numerator, I32 Denominator, U32 RefSrc, U32 Absolute)"""
    @staticmethod
    def Acm_AxTangentInGp(AxisHandle: _VoidPtrArg, MasGroupHandle: _VoidPtrArg, StartVectorArray: _PtrArg[c_int16], Working_plane: int, Direction: int, /) -> int:
        """U32 Acm_AxTangentInGp(HAND AxisHandle, HAND MasGroupHandle, PI16 StartVectorArray, U8 Working_plane, I16 Direction)"""
    @staticmethod
    def Acm_AxGantryInAx(AxisHandle: _VoidPtrArg, MasAxisHandle: _VoidPtrArg, RefMasterSrc: int, direction: int, /) -> int:
        """U32 Acm_AxGantryInAx(HAND AxisHandle, HAND MasAxisHandle, I16 RefMasterSrc, I16 direction)"""
    @staticmethod
    def Acm_AxSyncOut(FollowingAxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxSyncOut(HAND FollowingAxisHandle)"""
    @staticmethod
    def Acm_AxPhaseAx(AxisHandle: _VoidPtrArg, Acc: float, Dec: float, PhaseSpeed: float, PhaseDist: float, /) -> int:
        """U32 Acm_AxPhaseAx(HAND AxisHandle, F64 Acc, F64 Dec, F64 PhaseSpeed, F64 PhaseDist)"""
    @staticmethod
    def Acm_AxSetChannelCmpSetting(AxisHandle: _VoidPtrArg, ChannelID: int, CmpSrc: int, CmpMethod: int, CmpPulseMode: int, CmpPulseWidth: int, /) -> int:
        """U32 Acm_AxSetChannelCmpSetting(HAND AxisHandle, U16 ChannelID, U32 CmpSrc, U32 CmpMethod, U32 CmpPulseMode, U32 CmpPulseWidth)"""
    @staticmethod
    def Acm_AxGetChannelCmpSetting(AxisHandle: _VoidPtrArg, ChannelID: int, CmpSrc: _PtrArg[c_uint32], CmpMethod: _PtrArg[c_uint32], CmpPulseMode: _PtrArg[c_uint32], CmpPulseWidth: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_AxGetChannelCmpSetting(HAND AxisHandle, U16 ChannelID, PU32 CmpSrc, PU32 CmpMethod, PU32 CmpPulseMode, PU32 CmpPulseWidth)"""
    @staticmethod
    def Acm_AxResetChannelCmp(AxisHandle: _VoidPtrArg, ChannelID: int, /) -> int:
        """U32 Acm_AxResetChannelCmp(HAND AxisHandle, U16 ChannelID)"""
    @staticmethod
    def Acm_AxAddChannelCmpDatas(AxisHandle: _VoidPtrArg, ChannelID: int, TableArray: _PtrArg[c_double], ArrayCount: int, /) -> int:
        """U32 Acm_AxAddChannelCmpDatas(HAND AxisHandle, U16 ChannelID, PF64 TableArray, U32 ArrayCount)"""
    @staticmethod
    def Acm_AxGetChannelCmpData(AxisHandle: _VoidPtrArg, ChannelID: int, CmpData: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetChannelCmpData(HAND AxisHandle, U16 ChannelID, PF64 CmpData)"""
    @staticmethod
    def Acm_AxLoadChannelNextData(AxisHandle: _VoidPtrArg, ChannelID: int, /) -> int:
        """U32 Acm_AxLoadChannelNextData(HAND AxisHandle, U16 ChannelID)"""
    @staticmethod
    def Acm_AxGetCmpbufferRemainCount(AxisHandle: _VoidPtrArg, ChannelID: int, DataCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_AxGetCmpbufferRemainCount(HAND AxisHandle, U16 ChannelID, PU32 DataCount)"""
    @staticmethod
    def Acm_AxSetCmpAuto(AxisHandle: _VoidPtrArg, Start: float, End: float, Interval: float, /) -> int:
        """U32 Acm_AxSetCmpAuto(HAND AxisHandle, F64 Start, F64 End, F64 Interval)"""
    @staticmethod
    def Acm_AxGetCmpData(AxisHandle: _VoidPtrArg, CmpPosition: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetCmpData(HAND AxisHandle, PF64 CmpPosition)"""
    @staticmethod
    def Acm_AxSetCmpData(AxisHandle: _VoidPtrArg, CmpPosition: float, /) -> int:
        """U32 Acm_AxSetCmpData(HAND AxisHandle, F64 CmpPosition)"""
    @staticmethod
    def Acm_AxSetCmpTable(AxisHandle: _VoidPtrArg, TableArray: _PtrArg[c_double], ArrayCount: int, /) -> int:
        """U32 Acm_AxSetCmpTable(HAND AxisHandle, PF64 TableArray, I32 ArrayCount)"""
    @staticmethod
    def Acm_AxChangeCmpIndex(AxisHandle: _VoidPtrArg, CmpIndex: int, /) -> int:
        """U32 Acm_AxChangeCmpIndex(HAND AxisHandle, U32 CmpIndex)"""
    @staticmethod
    def Acm_AxSetCmpBufferData(AxisHandle: _VoidPtrArg, TableArray: _PtrArg[c_double], ArrayCount: int, /) -> int:
        """U32 Acm_AxSetCmpBufferData(HAND AxisHandle, PF64 TableArray, I32 ArrayCount)"""
    @staticmethod
    def Acm_AxResetCmpData(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxResetCmpData(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxGetCmpBufferStatus(AxisHandle: _VoidPtrArg, CurIndex: _PtrArg[c_uint32], RemainCnt: _PtrArg[c_uint32], SpaceCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_AxGetCmpBufferStatus(HAND AxisHandle, PU32 CurIndex, PU32 RemainCnt, PU32 SpaceCnt)"""
    @staticmethod
    def Acm_AxGetCmpCounter(AxisHandle: _VoidPtrArg, CmpCounter: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_AxGetCmpCounter(HAND AxisHandle, PU32 CmpCounter)"""
    @staticmethod
    def Acm_AxResetMPGOffset(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxResetMPGOffset(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxMovePTPBufferRel(AxisHandle: _VoidPtrArg, MotionMode: int, PositionArray: _PtrArg[c_double], FLArray: _PtrArg[c_double], FHArray: _PtrArg[c_double], TSArray: _PtrArg[c_uint16], ArrayLength: int, /) -> int:
        """U32 Acm_AxMovePTPBufferRel(HAND AxisHandle, U16 MotionMode, PF64 PositionArray, PF64 FLArray, PF64 FHArray, PU16 TSArray, U32 ArrayLength)"""
    @staticmethod
    def Acm_AxMovePTPBufferAbs(AxisHandle: _VoidPtrArg, MotionMode: int, PositionArray: _PtrArg[c_double], FLArray: _PtrArg[c_double], FHArray: _PtrArg[c_double], TSArray: _PtrArg[c_uint16], ArrayLength: int, /) -> int:
        """U32 Acm_AxMovePTPBufferAbs(HAND AxisHandle, U16 MotionMode, PF64 PositionArray, PF64 FLArray, PF64 FHArray, PU16 TSArray, U32 ArrayLength)"""
    @staticmethod
    def Acm_AxEnableCompensation(AxisHandle: _VoidPtrArg, ZStartPos: float, /) -> int:
        """U32 Acm_AxEnableCompensation(HAND AxisHandle, F64 ZStartPos)"""
    @staticmethod
    def Acm_AxGetCompensationValue(AxisHandle: _VoidPtrArg, XData: float, YData: float, PCompensationValue: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetCompensationValue(HAND AxisHandle, F64 XData, F64 YData, PF64 PCompensationValue)"""
    @staticmethod
    def Acm_AxSetCompenPara(AxisHandle: _VoidPtrArg, GroupHandle: _VoidPtrArg, XScanDataCnt: int, YScanDataCnt: int, CompMode: int, /) -> int:
        """U32 Acm_AxSetCompenPara(HAND AxisHandle, HAND GroupHandle, U32 XScanDataCnt, U32 YScanDataCnt, U32 CompMode)"""
    @staticmethod
    def Acm_AxDIStartMoveAbs(AxisHandle: _VoidPtrArg, DIChannel: int, Position: float, /) -> int:
        """U32 Acm_AxDIStartMoveAbs(HAND AxisHandle, U16 DIChannel, F64 Position)"""
    @staticmethod
    def Acm_AxDIStartMoveRel(AxisHandle: _VoidPtrArg, DIChannel: int, Distance: float, /) -> int:
        """U32 Acm_AxDIStartMoveRel(HAND AxisHandle, U16 DIChannel, F64 Distance)"""
    @staticmethod
    def Acm_AxDIStartMoveVel(AxisHandle: _VoidPtrArg, DIChannel: int, Direction: int, /) -> int:
        """U32 Acm_AxDIStartMoveVel(HAND AxisHandle, U16 DIChannel, U16 Direction)"""
    @staticmethod
    def Acm_AxDisableDIStart(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxDisableDIStart(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxSetPWMTableOnTime(AxisHandle: _VoidPtrArg, TimeTableArray: _PtrArg[c_uint32], ArrayCount: int, /) -> int:
        """U32 Acm_AxSetPWMTableOnTime(HAND AxisHandle, PU32 TimeTableArray, I32 ArrayCount)"""
    @staticmethod
    def Acm_AxGetINxStopStatus(AxisHandle: _VoidPtrArg, Stop_Flag: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_AxGetINxStopStatus(HAND AxisHandle, PU32 Stop_Flag)"""
    @staticmethod
    def Acm_AxResetINxStopStatus(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxResetINxStopStatus(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxJog(AxisHandle: _VoidPtrArg, Direction: int, /) -> int:
        """U32 Acm_AxJog(HAND AxisHandle, U16 Direction)"""
    @staticmethod
    def Acm_AxSetCmpDO(AxisHandle: _VoidPtrArg, OFForON: int, /) -> int:
        """U32 Acm_AxSetCmpDO(HAND AxisHandle, U32 OFForON)"""
    @staticmethod
    def Acm_AxDownloadTorqueTable(AxisHandle: _VoidPtrArg, PositionArray: _PtrArg[c_double], TorqueArray: _PtrArg[c_double], ArrayElements: int, /) -> int:
        """U32 Acm_AxDownloadTorqueTable(HAND AxisHandle, PF64 PositionArray, PF64 TorqueArray, U32 ArrayElements)"""
    @staticmethod
    def Acm_AxLoadTorqueTableFile(AxisHandle: _VoidPtrArg, FilePath: bytes | Array[c_char] | None, PointsCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_AxLoadTorqueTableFile(HAND AxisHandle, PI8 FilePath, PU32 PointsCount)"""
    @staticmethod
    def Acm_AxResetPVTTable(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxResetPVTTable(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxLoadPVTTable(AxisHandle: _VoidPtrArg, Position: _PtrArg[c_double], Velocity: _PtrArg[c_double], Time: _PtrArg[c_double], ArrayElements: int, /) -> int:
        """U32 Acm_AxLoadPVTTable(HAND AxisHandle, PF64 Position, PF64 Velocity, PF64 Time, U32 ArrayElements)"""
    @staticmethod
    def Acm_AxCalculatePVTTableContinuous(AxisHandle: _VoidPtrArg, Position: _PtrArg[c_double], Velocity: _PtrArg[c_double], JerkFactor: _PtrArg[c_double], MaxVel: _PtrArg[c_double], Acc: _PtrArg[c_double], Dec: _PtrArg[c_double], ArrayElements: int, Time: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxCalculatePVTTableContinuous(HAND AxisHandle, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, U32 ArrayElements, PF64 Time)"""
    @staticmethod
    def Acm_AxLoadPVTTableContinuous(AxisHandle: _VoidPtrArg, Position: _PtrArg[c_double], Velocity: _PtrArg[c_double], JerkFactor: _PtrArg[c_double], MaxVel: _PtrArg[c_double], Acc: _PtrArg[c_double], Dec: _PtrArg[c_double], TimeDelay: float, ArrayElements: int, /) -> int:
        """U32 Acm_AxLoadPVTTableContinuous(HAND AxisHandle, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, F64 TimeDelay, U32 ArrayElements)"""
    @staticmethod
    def Acm_AxStartPVT(AxisHandle: _VoidPtrArg, Repeat: int, /) -> int:
        """U32 Acm_AxStartPVT(HAND AxisHandle, U8 Repeat)"""
    @staticmethod
    def Acm_AxStartAllPVT(AxisHandle: _VoidPtrArg, Repeat: int, ArrayElements: int, /) -> int:
        """U32 Acm_AxStartAllPVT(PHAND AxisHandle, U8 Repeat, U32 ArrayElements)"""
    @staticmethod
    def Acm_AxCheckPTBuffer(AxisHandle: _VoidPtrArg, Freespace: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_AxCheckPTBuffer(HAND AxisHandle, PU16 Freespace)"""
    @staticmethod
    def Acm_AxAddPTData(AxisHandle: _VoidPtrArg, Position: float, Time: float, /) -> int:
        """U32 Acm_AxAddPTData(HAND AxisHandle, F64 Position, F64 Time)"""
    @staticmethod
    def Acm_AxStartPT(AxisHandle: _VoidPtrArg, Repeat: int, /) -> int:
        """U32 Acm_AxStartPT(HAND AxisHandle, U8 Repeat)"""
    @staticmethod
    def Acm_AxStartAllPT(AxisHandle: _VoidPtrArg, Repeat: int, ArrayElements: int, /) -> int:
        """U32 Acm_AxStartAllPT(PHAND AxisHandle, U8 Repeat, U32 ArrayElements)"""
    @staticmethod
    def Acm_AxResetPTData(AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxResetPTData(HAND AxisHandle)"""
    @staticmethod
    def Acm_AxAddPVAData(AxisHandle: _VoidPtrArg, Position: float, VelArray: _PtrArg[c_double], AccArray: _PtrArg[c_double], DecArray: _PtrArg[c_double], ArrayElements: int, /) -> int:
        """U32 Acm_AxAddPVAData(HAND AxisHandle, F64 Position, PF64 VelArray, PF64 AccArray, PF64 DecArray, U32 ArrayElements)"""
    @staticmethod
    def Acm_GpOpen(DevHandle: _VoidPtrArg, GpHandle: _PtrArg[c_void_p], GpID: int, /) -> int:
        """U32 Acm_GpOpen(HAND DevHandle, PHAND GpHandle, USHORT GpID)"""
    @staticmethod
    def Acm_GpAddAxis(GpHandle: _PtrArg[c_void_p], AxHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_GpAddAxis(PHAND GpHandle, HAND AxHandle)"""
    @staticmethod
    def Acm_GpRemAxis(GroupHandle: _VoidPtrArg, AxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_GpRemAxis(HAND GroupHandle, HAND AxisHandle)"""
    @staticmethod
    def Acm_GpClose(GroupHandle: _PtrArg[c_void_p], /) -> int:
        """U32 Acm_GpClose(PHAND GroupHandle)"""
    @staticmethod
    def Acm_GpGetAxesInGroup(GroupHandle: _VoidPtrArg, AxisArray: _PtrArg[c_uint32], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GpGetAxesInGroup(HAND GroupHandle, PU32 AxisArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm_GpGetState(GroupHandle: _VoidPtrArg, State: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_GpGetState(HAND GroupHandle, PU16 State)"""
    @staticmethod
    def Acm_GpResetError(GroupHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_GpResetError(HAND GroupHandle)"""
    @staticmethod
    def Acm_GpEnableTrig(GroupHandle: _VoidPtrArg, TrigPrm: TRIG_PRM, /) -> int:
        """U32 Acm_GpEnableTrig(HAND GroupHandle, TRIG_PRM TrigPrm)"""
    @staticmethod
    def Acm_GpIpoMask(GroupHandle: _VoidPtrArg, AxHandle: _VoidPtrArg, Mask: int, /) -> int:
        """U32 Acm_GpIpoMask(HAND GroupHandle, HAND AxHandle, U32 Mask)"""
    @staticmethod
    def Acm_GpChangePos(GroupHandle: _VoidPtrArg, Mode: int, DistanceArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GpChangePos(HAND GroupHandle, U32 Mode, PF64 DistanceArray, PU32 pArrayElements)"""
    @staticmethod
    def Acm_GpMoveLinearRel(GroupHandle: _VoidPtrArg, DistanceArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GpMoveLinearRel(HAND GroupHandle, PF64 DistanceArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm_GpMoveLinearAbs(GroupHandle: _VoidPtrArg, PositionArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GpMoveLinearAbs(HAND GroupHandle, PF64 PositionArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm_GpMoveDirectRel(GroupHandle: _VoidPtrArg, DistanceArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GpMoveDirectRel(HAND GroupHandle, PF64 DistanceArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm_GpMoveDirectAbs(GroupHandle: _VoidPtrArg, PositionArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GpMoveDirectAbs(HAND GroupHandle, PF64 PositionArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm_GpMoveCircularRel(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveCircularRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 ArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveCircularAbs(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveCircularAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 ArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveCircularRel_3P(GroupHandle: _VoidPtrArg, RefArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveCircularRel_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveCircularAbs_3P(GroupHandle: _VoidPtrArg, RefArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveCircularAbs_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveCircularRel_Angle(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], Degree: int, ArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveCircularRel_Angle(HAND GroupHandle, PF64 CenterArray, U16 Degree, PU32 ArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveCircularAbs_Angle(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], Degree: int, ArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveCircularAbs_Angle(HAND GroupHandle, PF64 CenterArray, U16 Degree, PU32 ArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveArcRel_Angle(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], Degree: float, ArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveArcRel_Angle(HAND GroupHandle, PF64 CenterArray, F64 Degree, PU32 ArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveArcAbs_Angle(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], Degree: float, ArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveArcAbs_Angle(HAND GroupHandle, PF64 CenterArray, F64 Degree, PU32 ArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMove3DArcAbs(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMove3DArcAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMove3DArcRel(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMove3DArcRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMove3DArcAbs_V(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], NVectorArray: _PtrArg[c_double], Degree: float, pArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMove3DArcAbs_V(HAND GroupHandle, PF64 CenterArray, PF64 NVectorArray, F64 Degree, PU32 pArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMove3DArcRel_V(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], NVectorArray: _PtrArg[c_double], Degree: float, pArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMove3DArcRel_V(HAND GroupHandle, PF64 CenterArray, PF64 NVectorArray, F64 Degree, PU32 pArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMove3DArcAbs_3P(GroupHandle: _VoidPtrArg, RefArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, cycCount: int, /) -> int:
        """U32 Acm_GpMove3DArcAbs_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, U16 cycCount)"""
    @staticmethod
    def Acm_GpMove3DArcRel_3P(GroupHandle: _VoidPtrArg, RefArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, cycCount: int, /) -> int:
        """U32 Acm_GpMove3DArcRel_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, U16 cycCount)"""
    @staticmethod
    def Acm_GpMove3DArcAbs_3PAngle(GroupHandle: _VoidPtrArg, RefPoint_1: _PtrArg[c_double], RefPoint_2: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, Degree: float, /) -> int:
        """U32 Acm_GpMove3DArcAbs_3PAngle(HAND GroupHandle, PF64 RefPoint_1, PF64 RefPoint_2, PU32 pArrayElements, I16 Direction, F64 Degree)"""
    @staticmethod
    def Acm_GpMove3DArcRel_3PAngle(GroupHandle: _VoidPtrArg, RefPoint_1: _PtrArg[c_double], RefPoint_2: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, Degree: float, /) -> int:
        """U32 Acm_GpMove3DArcRel_3PAngle(HAND GroupHandle, PF64 RefPoint_1, PF64 RefPoint_2, PU32 pArrayElements, I16 Direction, F64 Degree)"""
    @staticmethod
    def Acm_GpMoveHelixAbs(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveHelixAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveHelixRel(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveHelixRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveSpiral(GroupHandle: _VoidPtrArg, fStartRadius: float, fGrowthRate: float, fStartAngle_deg: float, fSweepAngle_deg: float, Direction: int, /) -> int:
        """U32 Acm_GpMoveSpiral(HAND GroupHandle, F64 fStartRadius, F64 fGrowthRate, F64 fStartAngle_deg, F64 fSweepAngle_deg, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveSpiralCenRel(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], fPitch: float, fSweepAngle_deg: float, Direction: int, /) -> int:
        """U32 Acm_GpMoveSpiralCenRel(HAND GroupHandle, PF64 CenterArray, PU32 ArrayElements, F64 fPitch, F64 fSweepAngle_deg, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveSpiralCenAbs(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], fPitch: float, fSweepAngle_deg: float, Direction: int, /) -> int:
        """U32 Acm_GpMoveSpiralCenAbs(HAND GroupHandle, PF64 CenterArray, PU32 ArrayElements, F64 fPitch, F64 fSweepAngle_deg, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveSpiralByRange(GroupHandle: _VoidPtrArg, fRstart: float, fRend: float, fTurns: float, /) -> int:
        """U32 Acm_GpMoveSpiralByRange(HAND GroupHandle, F64 fRstart, F64 fRend, F64 fTurns)"""
    @staticmethod
    def Acm_GpMoveSpiralCenPitchRel(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], RefEndArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], fPitch: float, Direction: int, /) -> int:
        """U32 Acm_GpMoveSpiralCenPitchRel(HAND GroupHandle, PF64 CenterArray, PF64 RefEndArray, PU32 ArrayElements, F64 fPitch, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveSpiralCenPitchAbs(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], RefEndArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], fPitch: float, Direction: int, /) -> int:
        """U32 Acm_GpMoveSpiralCenPitchAbs(HAND GroupHandle, PF64 CenterArray, PF64 RefEndArray, PU32 ArrayElements, F64 fPitch, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveSpiralCenEndPitchRel(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], fPitch: float, Direction: int, /) -> int:
        """U32 Acm_GpMoveSpiralCenEndPitchRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 ArrayElements, F64 fPitch, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveSpiralCenEndPitchAbs(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], fPitch: float, Direction: int, /) -> int:
        """U32 Acm_GpMoveSpiralCenEndPitchAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 ArrayElements, F64 fPitch, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveHelixAbs_3P(GroupHandle: _VoidPtrArg, RefArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveHelixAbs_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveHelixRel_3P(GroupHandle: _VoidPtrArg, RefArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveHelixRel_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveHelixRel_Angle(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveHelixRel_Angle(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveHelixAbs_Angle(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, /) -> int:
        """U32 Acm_GpMoveHelixAbs_Angle(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)"""
    @staticmethod
    def Acm_GpMoveEllipticalRel(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, RatioSemiAxes: float, /) -> int:
        """U32 Acm_GpMoveEllipticalRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, F64 RatioSemiAxes)"""
    @staticmethod
    def Acm_GpMoveEllipticalAbs(GroupHandle: _VoidPtrArg, CenterArray: _PtrArg[c_double], EndArray: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], Direction: int, RatioSemiAxes: float, /) -> int:
        """U32 Acm_GpMoveEllipticalAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, F64 RatioSemiAxes)"""
    @staticmethod
    def Acm_GpLoadPath(GroupHandle: _VoidPtrArg, FilePath: bytes | Array[c_char] | None, PathHandle: _PtrArg[c_void_p], pTotalCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GpLoadPath(HAND GroupHandle, PI8 FilePath, PHAND PathHandle, PU32 pTotalCount)"""
    @staticmethod
    def Acm_GpUnloadPath(GroupHandle: _VoidPtrArg, PathHandle: _PtrArg[c_void_p], /) -> int:
        """U32 Acm_GpUnloadPath(HAND GroupHandle, PHAND PathHandle)"""
    @staticmethod
    def Acm_GpMovePath(GroupHandle: _VoidPtrArg, PathHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_GpMovePath(HAND GroupHandle, HAND PathHandle)"""
    @staticmethod
    def Acm_GpMoveAllPath(GroupHandle: _PtrArg[c_void_p], ArrayElements: int, /) -> int:
        """U32 Acm_GpMoveAllPath(PHAND GroupHandle, U32 ArrayElements)"""
    @staticmethod
    def Acm_GpLookAheadPath(GroupHandle: _VoidPtrArg, BufferSize: int, OutputFile: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm_GpLookAheadPath(HAND GroupHandle, U16 BufferSize, PI8 OutputFile)"""
    @staticmethod
    def Acm_GpResetPath(GroupHandle: _PtrArg[c_void_p], /) -> int:
        """U32 Acm_GpResetPath(PHAND GroupHandle)"""
    @staticmethod
    def Acm_GpGetPathStatus(GroupHandle: _VoidPtrArg, pCurIndex: _PtrArg[c_uint32], pCurCmdFunc: _PtrArg[c_uint32], pRemainCount: _PtrArg[c_uint32], pFreeSpaceCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GpGetPathStatus(HAND GroupHandle, PU32 pCurIndex, PU32 pCurCmdFunc, PU32 pRemainCount, PU32 pFreeSpaceCount)"""
    @staticmethod
    def Acm_GpMoveSelPath(GroupHandle: _VoidPtrArg, PathHandle: _VoidPtrArg, StartIndex: int, EndIndex: int, Repeat: int, /) -> int:
        """U32 Acm_GpMoveSelPath(HAND GroupHandle, HAND PathHandle, U32 StartIndex, U32 EndIndex, U8 Repeat)"""
    @staticmethod
    def Acm_GpGetPathIndexStatus(GroupHandle: _VoidPtrArg, Index: int, CmdFunc: _PtrArg[c_uint16], MoveMode: _PtrArg[c_uint16], FH: _PtrArg[c_double], FL: _PtrArg[c_double], EndPoint_DataArray: _PtrArg[c_double], CenPoint_DataArray: _PtrArg[c_double], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GpGetPathIndexStatus(HAND GroupHandle, U32 Index, PU16 CmdFunc, PU16 MoveMode, PF64 FH, PF64 FL, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)"""
    @staticmethod
    def Acm_GpDelay(GroupHandle: _VoidPtrArg, DelayTime: int, /) -> int:
        """U32 Acm_GpDelay(HAND GroupHandle, U32 DelayTime)"""
    @staticmethod
    def Acm_GpPathDO(GroupHandle: _VoidPtrArg, PathDOPrm: PATH_DO_PRM, /) -> int:
        """U32 Acm_GpPathDO(HAND GroupHandle, PATH_DO_PRM PathDOPrm)"""
    @staticmethod
    def Acm_GpPathWaitDI(GroupHandle: _VoidPtrArg, DIWaitPrm: PATH_DI_WAIT_PRM, /) -> int:
        """U32 Acm_GpPathWaitDI(HAND GroupHandle, PATH_DI_WAIT_PRM DIWaitPrm)"""
    @staticmethod
    def Acm_GpPathWaitForAxis(GroupHandle: _VoidPtrArg, AxWaitPrm: PATH_AX_WAIT_PRM, /) -> int:
        """U32 Acm_GpPathWaitForAxis(HAND GroupHandle, PATH_AX_WAIT_PRM AxWaitPrm)"""
    @staticmethod
    def Acm_GpPathDIConditional(GroupHandle: _VoidPtrArg, MoveCmd: int, PathDIPrm: PATH_DI_WAIT_PRM, /) -> int:
        """U32 Acm_GpPathDIConditional(HAND GroupHandle, U16 MoveCmd, PATH_DI_WAIT_PRM PathDIPrm)"""
    @staticmethod
    def Acm_GpPathDOConditional(GroupHandle: _VoidPtrArg, MoveCmd: int, PathDOPrm: PATH_DO_PRM, /) -> int:
        """U32 Acm_GpPathDOConditional(HAND GroupHandle, U16 MoveCmd, PATH_DO_PRM PathDOPrm)"""
    @staticmethod
    def Acm_GpPathAxisConditional(GroupHandle: _VoidPtrArg, MoveCmd: int, AxPrm: PATH_AX_WAIT_PRM, /) -> int:
        """U32 Acm_GpPathAxisConditional(HAND GroupHandle, U16 MoveCmd, PATH_AX_WAIT_PRM AxPrm)"""
    @staticmethod
    def Acm_GpPathVarConditional(GroupHandle: _VoidPtrArg, MoveCmd: int, VarPrm: PATH_VAR_PRM, /) -> int:
        """U32 Acm_GpPathVarConditional(HAND GroupHandle, U16 MoveCmd, PATH_VAR_PRM VarPrm)"""
    @staticmethod
    def Acm_GpPathConditional(GroupHandle: _VoidPtrArg, MoveCmd: int, /) -> int:
        """U32 Acm_GpPathConditional(HAND GroupHandle, U16 MoveCmd)"""
    @staticmethod
    def Acm_GpPathOperator(GroupHandle: _VoidPtrArg, OperatorPrm: PATH_OPERATOR_PRM, /) -> int:
        """U32 Acm_GpPathOperator(HAND GroupHandle, PATH_OPERATOR_PRM OperatorPrm)"""
    @staticmethod
    def Acm_GpPathStartRecordBuffer(GroupHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_GpPathStartRecordBuffer(HAND GroupHandle)"""
    @staticmethod
    def Acm_GpPathEndRecordBuffer(GroupHandle: _VoidPtrArg, OutResult: _PtrArg[VALIDATE_RESULT], /) -> int:
        """U32 Acm_GpPathEndRecordBuffer(HAND GroupHandle, VALIDATE_RESULT* OutResult)"""
    @staticmethod
    def Acm_GpAddBSplinePath(GroupHandle: _VoidPtrArg, FH: float, FL: float, CtrlP0List: _PtrArg[c_double], CtrlP1List: _PtrArg[c_double], CtrlPCount: int, NodeList: _PtrArg[c_double], NodeCount: int, Degree: int, CutPointCount: int, /) -> int:
        """U32 Acm_GpAddBSplinePath(HAND GroupHandle, F64 FH, F64 FL, F64 *CtrlP0List, F64 *CtrlP1List, U32 CtrlPCount, F64 *NodeList, U32 NodeCount, U32 Degree, U32 CutPointCount)"""
    @staticmethod
    def Acm_GpAddCSplinePath(arg0: _VoidPtrArg, arg1: float, arg2: float, arg3: _PtrArg[c_double], arg4: _PtrArg[c_double], arg5: _PtrArg[c_double], arg6: int, arg7: int, /) -> int:
        """U32 Acm_GpAddCSplinePath(HAND arg0, F64 arg1, F64 arg2, PF64 arg3, PF64 arg4, PF64 arg5, U32 arg6, U32 arg7)"""
    @staticmethod
    def Acm_GpResumeMotion(GroupHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_GpResumeMotion(HAND GroupHandle)"""
    @staticmethod
    def Acm_GpPauseMotion(GroupHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_GpPauseMotion(HAND GroupHandle)"""
    @staticmethod
    def Acm_GpStopDec(GroupHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_GpStopDec(HAND GroupHandle)"""
    @staticmethod
    def Acm_GpStopEmg(GroupHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_GpStopEmg(HAND GroupHandle)"""
    @staticmethod
    def Acm_GpChangeVel(GroupHandle: _VoidPtrArg, NewVelocity: float, /) -> int:
        """U32 Acm_GpChangeVel(HAND GroupHandle, F64 NewVelocity)"""
    @staticmethod
    def Acm_GpChangeVelByRate(GroupHandle: _VoidPtrArg, Rate: int, /) -> int:
        """U32 Acm_GpChangeVelByRate(HAND GroupHandle, U32 Rate)"""
    @staticmethod
    def Acm_GpGetCmdVel(GroupHandle: _VoidPtrArg, CmdVel: _PtrArg[c_double], /) -> int:
        """U32 Acm_GpGetCmdVel(HAND GroupHandle, PF64 CmdVel)"""
    @staticmethod
    def Acm_GpGetINxStopStatus(GroupHandle: _VoidPtrArg, Stop_Flag: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GpGetINxStopStatus(HAND GroupHandle, PU32 Stop_Flag)"""
    @staticmethod
    def Acm_GpResetINxStopStatus(GroupHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_GpResetINxStopStatus(HAND GroupHandle)"""
    @staticmethod
    def Acm_DaqDiGetByte(DeviceHandle: _VoidPtrArg, DiPort: int, ByteData: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DaqDiGetByte(HAND DeviceHandle, U16 DiPort, PU8 ByteData)"""
    @staticmethod
    def Acm_DaqDiGetBit(DeviceHandle: _VoidPtrArg, DiChannel: int, BitData: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DaqDiGetBit(HAND DeviceHandle, U16 DiChannel, PU8 BitData)"""
    @staticmethod
    def Acm_DaqDoSetByte(DeviceHandle: _VoidPtrArg, DoPort: int, ByteData: int, /) -> int:
        """U32 Acm_DaqDoSetByte(HAND DeviceHandle, U16 DoPort, U8 ByteData)"""
    @staticmethod
    def Acm_DaqDoSetBit(DeviceHandle: _VoidPtrArg, DoChannel: int, BitData: int, /) -> int:
        """U32 Acm_DaqDoSetBit(HAND DeviceHandle, U16 DoChannel, U8 BitData)"""
    @staticmethod
    def Acm_DaqDoGetByte(DeviceHandle: _VoidPtrArg, DoPort: int, ByteData: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DaqDoGetByte(HAND DeviceHandle, U16 DoPort, PU8 ByteData)"""
    @staticmethod
    def Acm_DaqDoGetBit(DeviceHandle: _VoidPtrArg, DoChannel: int, BitData: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DaqDoGetBit(HAND DeviceHandle, U16 DoChannel, PU8 BitData)"""
    @staticmethod
    def Acm_DaqDiGetBytes(DeviceHandle: _VoidPtrArg, StartPort: int, NumPort: int, ByteDataArray: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DaqDiGetBytes(HAND DeviceHandle, U16 StartPort, U16 NumPort, PU8 ByteDataArray)"""
    @staticmethod
    def Acm_DaqDoSetBytes(DeviceHandle: _VoidPtrArg, StartPort: int, NumPort: int, ByteDataArray: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DaqDoSetBytes(HAND DeviceHandle, U16 StartPort, U16 NumPort, PU8 ByteDataArray)"""
    @staticmethod
    def Acm_DaqDoGetBytes(DeviceHandle: _VoidPtrArg, StartPort: int, NumPort: int, ByteDataArray: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DaqDoGetBytes(HAND DeviceHandle, U16 StartPort, U16 NumPort, PU8 ByteDataArray)"""
    @staticmethod
    def Acm_DaqAiGetRawData(DeviceHandle: _VoidPtrArg, AiChannel: int, AiData: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_DaqAiGetRawData(HAND DeviceHandle, U16 AiChannel, PU16 AiData)"""
    @staticmethod
    def Acm_DaqAiGetEngData(DeviceHandle: _VoidPtrArg, AiChannel: int, AiData: _PtrArg[c_float], /) -> int:
        """U32 Acm_DaqAiGetEngData(HAND DeviceHandle, U16 AiChannel, PF32 AiData)"""
    @staticmethod
    def Acm_DaqAiGetVoltData(DeviceHandle: _VoidPtrArg, AiChannel: int, AiData: _PtrArg[c_float], /) -> int:
        """U32 Acm_DaqAiGetVoltData(HAND DeviceHandle, U16 AiChannel, PF32 AiData)"""
    @staticmethod
    def Acm_DaqAiGetCurrData(DeviceHandle: _VoidPtrArg, AiChannel: int, AiData: _PtrArg[c_float], /) -> int:
        """U32 Acm_DaqAiGetCurrData(HAND DeviceHandle, U16 AiChannel, PF32 AiData)"""
    @staticmethod
    def Acm_DaqAiZeroCalibration(DeviceHandle: _VoidPtrArg, AiChannel: int, /) -> int:
        """U32 Acm_DaqAiZeroCalibration(HAND DeviceHandle, U16 AiChannel)"""
    @staticmethod
    def Acm_DaqAiSpanCalibration(DeviceHandle: _VoidPtrArg, AiChannel: int, /) -> int:
        """U32 Acm_DaqAiSpanCalibration(HAND DeviceHandle, U16 AiChannel)"""
    @staticmethod
    def Acm_DaqAiGetChannelStatus(DeviceHandle: _VoidPtrArg, AiChannel: int, ChanStatus: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DaqAiGetChannelStatus(HAND DeviceHandle, U16 AiChannel, PU32 ChanStatus)"""
    @staticmethod
    def Acm_DaqAoSetRawData(DeviceHandle: _VoidPtrArg, AoChannel: int, AoData: int, /) -> int:
        """U32 Acm_DaqAoSetRawData(HAND DeviceHandle, U16 AoChannel, U16 AoData)"""
    @staticmethod
    def Acm_DaqAoSetEngData(DeviceHandle: _VoidPtrArg, AoChannel: int, AoData: float, /) -> int:
        """U32 Acm_DaqAoSetEngData(HAND DeviceHandle, U16 AoChannel, F32 AoData)"""
    @staticmethod
    def Acm_DaqAoSetVoltData(DeviceHandle: _VoidPtrArg, AoChannel: int, AoData: float, /) -> int:
        """U32 Acm_DaqAoSetVoltData(HAND DeviceHandle, U16 AoChannel, F32 AoData)"""
    @staticmethod
    def Acm_DaqAoSetCurrData(DeviceHandle: _VoidPtrArg, AoChannel: int, AoData: float, /) -> int:
        """U32 Acm_DaqAoSetCurrData(HAND DeviceHandle, U16 AoChannel, F32 AoData)"""
    @staticmethod
    def Acm_DaqAoGetRawData(DeviceHandle: _VoidPtrArg, AoChannel: int, AoData: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_DaqAoGetRawData(HAND DeviceHandle, U16 AoChannel, PU16 AoData)"""
    @staticmethod
    def Acm_DaqAoGetEngData(DeviceHandle: _VoidPtrArg, AoChannel: int, AoData: _PtrArg[c_float], /) -> int:
        """U32 Acm_DaqAoGetEngData(HAND DeviceHandle, U16 AoChannel, PF32 AoData)"""
    @staticmethod
    def Acm_DaqAoGetVoltData(DeviceHandle: _VoidPtrArg, AoChannel: int, AoData: _PtrArg[c_float], /) -> int:
        """U32 Acm_DaqAoGetVoltData(HAND DeviceHandle, U16 AoChannel, PF32 AoData)"""
    @staticmethod
    def Acm_DaqAoGetCurrData(DeviceHandle: _VoidPtrArg, AoChannel: int, AoData: _PtrArg[c_float], /) -> int:
        """U32 Acm_DaqAoGetCurrData(HAND DeviceHandle, U16 AoChannel, PF32 AoData)"""
    @staticmethod
    def Acm_DaqAoSetCaliType(DeviceHandle: _VoidPtrArg, AoChannel: int, TrimType: int, /) -> int:
        """U32 Acm_DaqAoSetCaliType(HAND DeviceHandle, U16 AoChannel, U16 TrimType)"""
    @staticmethod
    def Acm_DaqAoSetCaliValue(DeviceHandle: _VoidPtrArg, AoChannel: int, CaliData: int, /) -> int:
        """U32 Acm_DaqAoSetCaliValue(HAND DeviceHandle, U16 AoChannel, U16 CaliData)"""
    @staticmethod
    def Acm_DaqAoCaliDone(DeviceHandle: _VoidPtrArg, AoChannel: int, done: bool, /) -> int:
        """U32 Acm_DaqAoCaliDone(HAND DeviceHandle, U16 AoChannel, bool done)"""
    @staticmethod
    def Acm_DaqAoCaliDefault(DeviceHandle: _VoidPtrArg, AoChannel: int, /) -> int:
        """U32 Acm_DaqAoCaliDefault(HAND DeviceHandle, U16 AoChannel)"""
    @staticmethod
    def Acm_DaqAoGetChannelStatus(DeviceHandle: _VoidPtrArg, AoChannel: int, ChanStatus: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DaqAoGetChannelStatus(HAND DeviceHandle, U16 AoChannel, PU32 ChanStatus)"""
    @staticmethod
    def Acm_DaqAoLinkAxData(DeviceHandle: _VoidPtrArg, AoChannel: int, AxisHandle: _VoidPtrArg, Type: int, Max: float, Min: float, /) -> int:
        """U32 Acm_DaqAoLinkAxData(HAND DeviceHandle, U16 AoChannel, HAND AxisHandle, U16 Type, F64 Max, F64 Min)"""
    @staticmethod
    def Acm_DaqSetScaledProperty(DeviceHandle: _VoidPtrArg, Type: int, Channel: int, UpperBound: float, LowerBound: float, Resolution: int, TransType: int, /) -> int:
        """U32 Acm_DaqSetScaledProperty(HAND DeviceHandle, U32 Type, U16 Channel, F32 UpperBound, F32 LowerBound, U16 Resolution, I16 TransType)"""
    @staticmethod
    def Acm_DaqGetIOLinkStatus(DeviceHandle: _VoidPtrArg, pStatus: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DaqGetIOLinkStatus(HAND DeviceHandle, PU32 pStatus)"""
    @staticmethod
    def Acm_DaqCntTriggerCmp(DeviceHandle: _VoidPtrArg, CntChannel: int, /) -> int:
        """U32 Acm_DaqCntTriggerCmp(HAND DeviceHandle, U16 CntChannel)"""
    @staticmethod
    def Acm_DaqCntTriggerLatch(DeviceHandle: _VoidPtrArg, CntChannel: int, /) -> int:
        """U32 Acm_DaqCntTriggerLatch(HAND DeviceHandle, U16 CntChannel)"""
    @staticmethod
    def Acm_DaqCntResetLatch(DeviceHandle: _VoidPtrArg, CntChannel: int, /) -> int:
        """U32 Acm_DaqCntResetLatch(HAND DeviceHandle, U16 CntChannel)"""
    @staticmethod
    def Acm_DaqCntResetCmp(DeviceHandle: _VoidPtrArg, CntChannel: int, /) -> int:
        """U32 Acm_DaqCntResetCmp(HAND DeviceHandle, U16 CntChannel)"""
    @staticmethod
    def Acm_DaqCntResetCnt(DeviceHandle: _VoidPtrArg, CntChannel: int, /) -> int:
        """U32 Acm_DaqCntResetCnt(HAND DeviceHandle, U16 CntChannel)"""
    @staticmethod
    def Acm_DaqCntGetCounterData(DeviceHandle: _VoidPtrArg, CntChannel: int, CounterData: _PtrArg[c_double], /) -> int:
        """U32 Acm_DaqCntGetCounterData(HAND DeviceHandle, U16 CntChannel, PF64 CounterData)"""
    @staticmethod
    def Acm_DaqCntSetCounterData(DeviceHandle: _VoidPtrArg, CntChannel: int, CounterData: float, /) -> int:
        """U32 Acm_DaqCntSetCounterData(HAND DeviceHandle, U16 CntChannel, F64 CounterData)"""
    @staticmethod
    def Acm_DaqCntGetCounterFrequency(DeviceHandle: _VoidPtrArg, CntChannel: int, Frequency: _PtrArg[c_double], /) -> int:
        """U32 Acm_DaqCntGetCounterFrequency(HAND DeviceHandle, U16 CntChannel, PF64 Frequency)"""
    @staticmethod
    def Acm_DaqCntGetExtDriveData(DeviceHandle: _VoidPtrArg, CntChannel: int, CounterData: _PtrArg[c_double], /) -> int:
        """U32 Acm_DaqCntGetExtDriveData(HAND DeviceHandle, U16 CntChannel, PF64 CounterData)"""
    @staticmethod
    def Acm_DaqCntSetExtDriveData(DeviceHandle: _VoidPtrArg, CntChannel: int, CounterData: float, /) -> int:
        """U32 Acm_DaqCntSetExtDriveData(HAND DeviceHandle, U16 CntChannel, F64 CounterData)"""
    @staticmethod
    def Acm_DaqCntGetLatchData(DeviceHandle: _VoidPtrArg, CntChannel: int, LatchData: _PtrArg[c_double], /) -> int:
        """U32 Acm_DaqCntGetLatchData(HAND DeviceHandle, U16 CntChannel, PF64 LatchData)"""
    @staticmethod
    def Acm_DaqCntGetCmpData(DeviceHandle: _VoidPtrArg, CntChannel: int, CmpData: _PtrArg[c_double], /) -> int:
        """U32 Acm_DaqCntGetCmpData(HAND DeviceHandle, U16 CntChannel, PF64 CmpData)"""
    @staticmethod
    def Acm_DaqCntSetCmpData(DeviceHandle: _VoidPtrArg, CntChannel: int, CmpData: float, /) -> int:
        """U32 Acm_DaqCntSetCmpData(HAND DeviceHandle, U16 CntChannel, F64 CmpData)"""
    @staticmethod
    def Acm_DaqCntSetCmpTable(DeviceHandle: _VoidPtrArg, CntChannel: int, TableArray: _PtrArg[c_double], ArrayCount: int, /) -> int:
        """U32 Acm_DaqCntSetCmpTable(HAND DeviceHandle, U16 CntChannel, PF64 TableArray, I32 ArrayCount)"""
    @staticmethod
    def Acm_DaqCntSetCmpAuto(DeviceHandle: _VoidPtrArg, CntChannel: int, Start: float, End: float, Interval: float, /) -> int:
        """U32 Acm_DaqCntSetCmpAuto(HAND DeviceHandle, U16 CntChannel, F64 Start, F64 End, F64 Interval)"""
    @staticmethod
    def Acm_DaqCntGetLatchBufferStatus(DeviceHandle: _VoidPtrArg, CntChannel: int, RemainCnt: _PtrArg[c_uint32], SpaceCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DaqCntGetLatchBufferStatus(HAND DeviceHandle, U16 CntChannel, PU32 RemainCnt, PU32 SpaceCnt)"""
    @staticmethod
    def Acm_DaqCntReadLatchBuffer(DeviceHandle: _VoidPtrArg, CntChannel: int, LatchDataArray: _PtrArg[c_double], DataCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DaqCntReadLatchBuffer(HAND DeviceHandle, U16 CntChannel, PF64 LatchDataArray, PU32 DataCnt)"""
    @staticmethod
    def Acm_ChLinkCmpObject(DeviceHandle: _VoidPtrArg, CmpID: int, ObjType: ADV_OBJ_TYPE | int, ObjArray: _PtrArg[c_uint32], ArrayElement: int, /) -> int:
        """U32 Acm_ChLinkCmpObject(HAND DeviceHandle, U32 CmpID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)"""
    @staticmethod
    def Acm_ChGetLinkedCmpObject(DeviceHandle: _VoidPtrArg, CmpID: int, ObjType: _PtrArg[c_uint], ObjArray: _PtrArg[c_uint32], ArrayElement: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_ChGetLinkedCmpObject(HAND DeviceHandle, U32 CmpID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)"""
    @staticmethod
    def Acm_ChEnableCmp(DeviceHandle: _VoidPtrArg, CmpID: int, Enable: int, /) -> int:
        """U32 Acm_ChEnableCmp(HAND DeviceHandle, U32 CmpID, U32 Enable)"""
    @staticmethod
    def Acm_ChSetCmpOut(DeviceHandle: _VoidPtrArg, CmpID: int, OnOff: DO_ONOFF | int, /) -> int:
        """U32 Acm_ChSetCmpOut(HAND DeviceHandle, U32 CmpID, DO_ONOFF OnOff)"""
    @staticmethod
    def Acm_ChSetCmpDoOut(DeviceHandle: _VoidPtrArg, CmpID: int, OnOff: DO_ONOFF | int, /) -> int:
        """U32 Acm_ChSetCmpDoOut(HAND DeviceHandle, U32 CmpID, DO_ONOFF OnOff)"""
    @staticmethod
    def Acm_ChGetCmpData(DeviceHandle: _VoidPtrArg, CmpID: int, CmpData: _PtrArg[c_double], ObjectArrayCount: int, /) -> int:
        """U32 Acm_ChGetCmpData(HAND DeviceHandle, U32 CmpID, PF64 CmpData, U32 ObjectArrayCount)"""
    @staticmethod
    def Acm_ChSetCmpAuto(DeviceHandle: _VoidPtrArg, CmpID: int, StartPosition: float, EndPosition: float, Interval: float, /) -> int:
        """U32 Acm_ChSetCmpAuto(HAND DeviceHandle, U32 CmpID, F64 StartPosition, F64 EndPosition, F64 Interval)"""
    @staticmethod
    def Acm_ChSetCmpBufferData(DeviceHandle: _VoidPtrArg, CmpID: int, TableArray: _PtrArg[c_double], ArrayCount: int, /) -> int:
        """U32 Acm_ChSetCmpBufferData(HAND DeviceHandle, U32 CmpID, PF64 TableArray, U32 ArrayCount)"""
    @staticmethod
    def Acm_ChSetMultiCmpBufferData(DeviceHandle: _VoidPtrArg, CmpID: int, MultiCmpTable: _PtrArg[c_double], ObjectArrayCount: int, DataArrayCount: int, /) -> int:
        """U32 Acm_ChSetMultiCmpBufferData(HAND DeviceHandle, U32 CmpID, PF64 MultiCmpTable, U32 ObjectArrayCount, U32 DataArrayCount)"""
    @staticmethod
    def Acm_ChResetCmpData(DeviceHandle: _VoidPtrArg, CmpID: int, /) -> int:
        """U32 Acm_ChResetCmpData(HAND DeviceHandle, U32 CmpID)"""
    @staticmethod
    def Acm_ChGetCmpBufferStatus(DeviceHandle: _VoidPtrArg, CmpID: int, BufferStatus: _PtrArg[BUFFER_STATUS], /) -> int:
        """U32 Acm_ChGetCmpBufferStatus(HAND DeviceHandle, U32 CmpID, PBUFFER_STATUS BufferStatus)"""
    @staticmethod
    def Acm_ChLinkLatchObject(DeviceHandle: _VoidPtrArg, LtcID: int, ObjType: ADV_OBJ_TYPE | int, ObjArray: _PtrArg[c_uint32], ArrayElement: int, /) -> int:
        """U32 Acm_ChLinkLatchObject(HAND DeviceHandle, U32 LtcID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)"""
    @staticmethod
    def Acm_ChGetLinkedLatchObject(DeviceHandle: _VoidPtrArg, LtcID: int, ObjType: _PtrArg[c_uint], ObjArray: _PtrArg[c_uint32], ArrayElement: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_ChGetLinkedLatchObject(HAND DeviceHandle, U32 LtcID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)"""
    @staticmethod
    def Acm_ChTriggerLatch(DeviceHandle: _VoidPtrArg, LtcID: int, /) -> int:
        """U32 Acm_ChTriggerLatch(HAND DeviceHandle, U32 LtcID)"""
    @staticmethod
    def Acm_ChReadLatchBuffer(DeviceHandle: _VoidPtrArg, LtcID: int, LatchDataArray: _PtrArg[c_double], ObjectArrayCount: int, DataArrayCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_ChReadLatchBuffer(HAND DeviceHandle, U32 LtcID, PF64 LatchDataArray, U32 ObjectArrayCount, PU32 DataArrayCount)"""
    @staticmethod
    def Acm_ChGetLatchBufferStatus(DeviceHandle: _VoidPtrArg, LtcID: int, BufferStatus: _PtrArg[BUFFER_STATUS], /) -> int:
        """U32 Acm_ChGetLatchBufferStatus(HAND DeviceHandle, U32 LtcID, PBUFFER_STATUS BufferStatus)"""
    @staticmethod
    def Acm_ChResetLatchBuffer(DeviceHandle: _VoidPtrArg, LtcID: int, /) -> int:
        """U32 Acm_ChResetLatchBuffer(HAND DeviceHandle, U32 LtcID)"""
    @staticmethod
    def Acm_AxPWMOut(AxisHandle: _VoidPtrArg, OFForON: int, PulseCount: int, /) -> int:
        """U32 Acm_AxPWMOut(HAND AxisHandle, U32 OFForON, U32 PulseCount)"""
    @staticmethod
    def Acm_AxGetPWMOutState(AxisHandle: _VoidPtrArg, OFForON: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_AxGetPWMOutState(HAND AxisHandle, PU32 OFForON)"""
    @staticmethod
    def Acm_DevMDaqConfig(DeviceHandle: _VoidPtrArg, ChannelID: int, Period: int, AxisNo: int, Method: int, ChanType: int, Count: int, /) -> int:
        """U32 Acm_DevMDaqConfig(HAND DeviceHandle, U16 ChannelID, U32 Period, U32 AxisNo, U32 Method, U32 ChanType, U32 Count)"""
    @staticmethod
    def Acm_DevMDaqStart(DeviceHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_DevMDaqStart(HAND DeviceHandle)"""
    @staticmethod
    def Acm_DevMDaqStop(DeviceHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_DevMDaqStop(HAND DeviceHandle)"""
    @staticmethod
    def Acm_DevMDaqReset(DeviceHandle: _VoidPtrArg, ChannelID: int, /) -> int:
        """U32 Acm_DevMDaqReset(HAND DeviceHandle, U16 ChannelID)"""
    @staticmethod
    def Acm_DevMDaqGetStatus(DeviceHandle: _VoidPtrArg, ChannelID: int, CurrentCnt: _PtrArg[c_uint16], Status: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DevMDaqGetStatus(HAND DeviceHandle, U16 ChannelID, PU16 CurrentCnt, PU8 Status)"""
    @staticmethod
    def Acm_DevMDaqGetData(DeviceHandle: _VoidPtrArg, ChannelID: int, StartIndex: int, MaxCount: int, DataBuffer: _PtrArg[c_int32], /) -> int:
        """U32 Acm_DevMDaqGetData(HAND DeviceHandle, U16 ChannelID, U16 StartIndex, U16 MaxCount, PI32 DataBuffer)"""
    @staticmethod
    def Acm_DevMDaqGetConfig(DeviceHandle: _VoidPtrArg, ChannelID: int, Period: _PtrArg[c_uint32], AxisNo: _PtrArg[c_uint32], Method: _PtrArg[c_uint32], ChanType: _PtrArg[c_uint32], Count: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevMDaqGetConfig(HAND DeviceHandle, U16 ChannelID, PU32 Period, PU32 AxisNo, PU32 Method, PU32 ChanType, PU32 Count)"""
    @staticmethod
    def Acm_RegCallBackFunc(Handle: _VoidPtrArg, CallBackFun: CALLBACK_FUNC, UserParamter: _VoidPtrArg, /) -> int:
        """U32 Acm_RegCallBackFunc(HAND Handle, ADV_USER_CALLBACK_FUNC CallBackFun, PVOID UserParamter)"""
    @staticmethod
    def Acm_EnableEventCallBack(DeviceHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_EnableEventCallBack(HAND DeviceHandle)"""
    @staticmethod
    def Acm_RegCallBackFuncForOneEvent(Handle: _VoidPtrArg, EvtChannel: int, CallBackFun: CALLBACK_FUNC, UserParamter: _VoidPtrArg, /) -> int:
        """U32 Acm_RegCallBackFuncForOneEvent(HAND Handle, U32 EvtChannel, ADV_USER_CALLBACK_FUNC CallBackFun, PVOID UserParamter)"""
    @staticmethod
    def Acm_DevEnableMotionEvent(DeviceHandle: _VoidPtrArg, AxEnableEvtArray: _PtrArg[c_uint32], GpEnableEvtArray: _PtrArg[c_uint32], AxArrayElements: int, GpArrayElements: int, /) -> int:
        """U32 Acm_DevEnableMotionEvent(HAND DeviceHandle, PU32 AxEnableEvtArray, PU32 GpEnableEvtArray, U32 AxArrayElements, U32 GpArrayElements)"""
    @staticmethod
    def Acm_ServoSetCom(ComPortID: int, Baudrate: int, Timeout: int, /) -> int:
        """U32 Acm_ServoSetCom(U32 ComPortID, U32 Baudrate, U32 Timeout)"""
    @staticmethod
    def Acm_ServoGetAbsPosition(ComPortID: int, ServoType: int, ServoID: int, ServoAbsResolution: int, ServoCmdResolution: int, EncoderDir: int, AbsPosition: _PtrArg[c_double], /) -> int:
        """U32 Acm_ServoGetAbsPosition(U32 ComPortID, U32 ServoType, U32 ServoID, U32 ServoAbsResolution, U32 ServoCmdResolution, U32 EncoderDir, PF64 AbsPosition)"""
    @staticmethod
    def Acm_AxSetCmdPosi_Pulse(AxisHandle: _VoidPtrArg, Position: float, /) -> int:
        """U32 Acm_AxSetCmdPosi_Pulse(HAND AxisHandle, F64 Position)"""
    @staticmethod
    def Acm_AxSpecialDiSetBit(AxisHandle: _VoidPtrArg, DiType: int, BitData: int, /) -> int:
        """U32 Acm_AxSpecialDiSetBit(HAND AxisHandle, U16 DiType, U8 BitData)"""
    @staticmethod
    def Acm_DevEnableLTC(DeviceHandle: _VoidPtrArg, LtcID: int, EnableMode: int, /) -> int:
        """U32 Acm_DevEnableLTC(HAND DeviceHandle, U16 LtcID, U16 EnableMode)"""
    @staticmethod
    def Acm_DevLTCSaftyDist(DeviceHandle: _VoidPtrArg, LtcID: int, SaftyDist: float, /) -> int:
        """U32 Acm_DevLTCSaftyDist(HAND DeviceHandle, U16 LtcID, F64 SaftyDist)"""
    @staticmethod
    def Acm_DevEnableCmp(DeviceHandle: _VoidPtrArg, CmpID: int, EnableMode: int, /) -> int:
        """U32 Acm_DevEnableCmp(HAND DeviceHandle, U16 CmpID, U16 EnableMode)"""
    @staticmethod
    def Acm_DevLtcLinkCmp(DeviceHandle: _VoidPtrArg, AxisHandle: _VoidPtrArg, EnableLink: int, LtcID: int, CmpID: int, Offset: float, /) -> int:
        """U32 Acm_DevLtcLinkCmp(HAND DeviceHandle, HAND AxisHandle, U16 EnableLink, U16 LtcID, U16 CmpID, F64 Offset)"""
    @staticmethod
    def Acm_DevSetCmp(DeviceHandle: _VoidPtrArg, CmpID: int, CmpLogic: int, CmpSrc: int, CmpMethod: int, DOMode: int, DOWidth: int, /) -> int:
        """U32 Acm_DevSetCmp(HAND DeviceHandle, U16 CmpID, U32 CmpLogic, U32 CmpSrc, U32 CmpMethod, U32 DOMode, U32 DOWidth)"""
    @staticmethod
    def Acm_DevSetCmpDO(DeviceHandle: _VoidPtrArg, CmpID: int, OnOff: int, /) -> int:
        """U32 Acm_DevSetCmpDO(HAND DeviceHandle, U16 CmpID, U16 OnOff)"""
    @staticmethod
    def Acm_DevSetCmpData(DeviceHandle: _VoidPtrArg, CmpID: int, Data: float, /) -> int:
        """U32 Acm_DevSetCmpData(HAND DeviceHandle, U16 CmpID, F64 Data)"""
    @staticmethod
    def Acm_DevSetCmpAuto(DeviceHandle: _VoidPtrArg, CmpID: int, Start: float, End: float, Interval: float, /) -> int:
        """U32 Acm_DevSetCmpAuto(HAND DeviceHandle, U16 CmpID, F64 Start, F64 End, F64 Interval)"""
    @staticmethod
    def Acm_DevGetCmpData(DeviceHandle: _VoidPtrArg, CmpID: int, Data: _PtrArg[c_double], /) -> int:
        """U32 Acm_DevGetCmpData(HAND DeviceHandle, U16 CmpID, PF64 Data)"""
    @staticmethod
    def Acm_DevEnableCmpFIFO(DeviceHandle: _VoidPtrArg, CmpID: int, Enable: int, /) -> int:
        """U32 Acm_DevEnableCmpFIFO(HAND DeviceHandle, U16 CmpID, U16 Enable)"""
    @staticmethod
    def Acm_DevGetCmpFIFOCount(DeviceHandle: _VoidPtrArg, CmpID: int, DataCount: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_DevGetCmpFIFOCount(HAND DeviceHandle, U16 CmpID, PU16 DataCount)"""
    @staticmethod
    def Acm_DevGetCmpCounter(DeviceHandle: _VoidPtrArg, CmpID: int, DataCount: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevGetCmpCounter(HAND DeviceHandle, U16 CmpID, PU32 DataCount)"""
    @staticmethod
    def Acm_DevResetCmpFIFO(DeviceHandle: _VoidPtrArg, CmpID: int, /) -> int:
        """U32 Acm_DevResetCmpFIFO(HAND DeviceHandle, U16 CmpID)"""
    @staticmethod
    def Acm_DevSetLTCInPol(DeviceHandle: _VoidPtrArg, LtcID: int, Logic: int, /) -> int:
        """U32 Acm_DevSetLTCInPol(HAND DeviceHandle, U16 LtcID, U16 Logic)"""
    @staticmethod
    def Acm_DevSetLTCInEdge(DeviceHandle: _VoidPtrArg, LtcID: int, Edge: int, /) -> int:
        """U32 Acm_DevSetLTCInEdge(HAND DeviceHandle, U16 LtcID, U16 Edge)"""
    @staticmethod
    def Acm_DevGetLTCData(DeviceHandle: _VoidPtrArg, LtcID: int, CommandPosition: _PtrArg[c_double], Actualposition: _PtrArg[c_double], /) -> int:
        """U32 Acm_DevGetLTCData(HAND DeviceHandle, U16 LtcID, PF64 CommandPosition, PF64 Actualposition)"""
    @staticmethod
    def Acm_DevGetLTCFlag(DeviceHandle: _VoidPtrArg, LtcID: int, LtcFlag: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DevGetLTCFlag(HAND DeviceHandle, U16 LtcID, PU8 LtcFlag)"""
    @staticmethod
    def Acm_DevResetLTC(DeviceHandle: _VoidPtrArg, LtcID: int, /) -> int:
        """U32 Acm_DevResetLTC(HAND DeviceHandle, U16 LtcID)"""
    @staticmethod
    def Acm_DevGetCmpFlag(DeviceHandle: _VoidPtrArg, CmpID: int, CmpFlag: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DevGetCmpFlag(HAND DeviceHandle, U16 CmpID, PU8 CmpFlag)"""
    @staticmethod
    def Acm_DevResetCmpFlag(DeviceHandle: _VoidPtrArg, CmpID: int, /) -> int:
        """U32 Acm_DevResetCmpFlag(HAND DeviceHandle, U16 CmpID)"""
    @staticmethod
    def Acm_DevGetLtcLinkCmpStatus(DeviceHandle: _VoidPtrArg, LtcID: int, LinkStatus: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_DevGetLtcLinkCmpStatus(HAND DeviceHandle, U16 LtcID, PU16 LinkStatus)"""
    @staticmethod
    def Acm_DevResetCmpData(DeviceHandle: _VoidPtrArg, CmpID: int, /) -> int:
        """U32 Acm_DevResetCmpData(HAND DeviceHandle, U16 CmpID)"""
    @staticmethod
    def Acm_DevGetLTCInEdge(DeviceHandle: _VoidPtrArg, LtcID: int, Edge: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_DevGetLTCInEdge(HAND DeviceHandle, U16 LtcID, PU16 Edge)"""
    @staticmethod
    def Acm_DevGetLTCInPol(DeviceHandle: _VoidPtrArg, LtcID: int, Logic: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_DevGetLTCInPol(HAND DeviceHandle, U16 LtcID, PU16 Logic)"""
    @staticmethod
    def Acm_DevGetLTCSaftyDist(DeviceHandle: _VoidPtrArg, LtcID: int, SaftyDist: _PtrArg[c_double], /) -> int:
        """U32 Acm_DevGetLTCSaftyDist(HAND DeviceHandle, U16 LtcID, PF64 SaftyDist)"""
    @staticmethod
    def Acm_DevGetLTCInSource(DeviceHandle: _VoidPtrArg, LtcID: int, Source: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_DevGetLTCInSource(HAND DeviceHandle, U16 LtcID, PU16 Source)"""
    @staticmethod
    def Acm_DevSetLTCInSource(DeviceHandle: _VoidPtrArg, LtcID: int, Source: int, /) -> int:
        """U32 Acm_DevSetLTCInSource(HAND DeviceHandle, U16 LtcID, U16 Source)"""
    @staticmethod
    def Acm_DevGetCmp(DeviceHandle: _VoidPtrArg, CmpID: int, CmpLogic: _PtrArg[c_uint32], CmpSrc: _PtrArg[c_uint32], CmpMethod: _PtrArg[c_uint32], DOMode: _PtrArg[c_uint32], DOWidth: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevGetCmp(HAND DeviceHandle, U16 CmpID, PU32 CmpLogic, PU32 CmpSrc, PU32 CmpMethod, PU32 DOMode, PU32 DOWidth)"""
    @staticmethod
    def Acm_ChLinkSWCmpObject(DeviceHandle: _VoidPtrArg, SWCmpID: int, ObjType: ADV_OBJ_TYPE | int, ObjArray: _PtrArg[c_uint32], ArrayElement: int, /) -> int:
        """U32 Acm_ChLinkSWCmpObject(HAND DeviceHandle, U16 SWCmpID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)"""
    @staticmethod
    def Acm_DaqDoLinkSWCmpObject(DeviceHandle: _VoidPtrArg, SWCmpID: int, DOChannel: int, /) -> int:
        """U32 Acm_DaqDoLinkSWCmpObject(HAND DeviceHandle, U16 SWCmpID, U32 DOChannel)"""
    @staticmethod
    def Acm_ChGetLinkedSWCmpObject(DeviceHandle: _VoidPtrArg, SWCmpID: int, ObjType: _PtrArg[c_uint], ObjArray: _PtrArg[c_uint32], ArrayElement: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_ChGetLinkedSWCmpObject(HAND DeviceHandle, U16 SWCmpID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)"""
    @staticmethod
    def Acm_DaqDoGetLinkedSWCmpObject(DeviceHandle: _VoidPtrArg, SWCmpID: int, DOChannel: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DaqDoGetLinkedSWCmpObject(HAND DeviceHandle, U16 SWCmpID, PU32 DOChannel)"""
    @staticmethod
    def Acm_DevReadLatchBuffer(DeviceHandle: _VoidPtrArg, LtcID: int, CommandPositionArray: _PtrArg[c_double], ActualPositionArray: _PtrArg[c_double], DataCnt: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevReadLatchBuffer(HAND DeviceHandle, U16 LtcID, PF64 CommandPositionArray, PF64 ActualPositionArray, PU32 DataCnt)"""
    @staticmethod
    def Acm_DevGetLatchBufferStatus(DeviceHandle: _VoidPtrArg, LtcID: int, RemainCnt: _PtrArg[c_uint32], SpaceCnt: _PtrArg[c_uint32], LtcCounter: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevGetLatchBufferStatus(HAND DeviceHandle, U16 LtcID, PU32 RemainCnt, PU32 SpaceCnt, PU32 LtcCounter)"""
    @staticmethod
    def Acm_DevResetLatchBuffer(DeviceHandle: _VoidPtrArg, LtcID: int, /) -> int:
        """U32 Acm_DevResetLatchBuffer(HAND DeviceHandle, U16 LtcID)"""
    @staticmethod
    def Acm_DevSetLTCInAxisID(DeviceHandle: _VoidPtrArg, LtcID: int, AxisID: int, /) -> int:
        """U32 Acm_DevSetLTCInAxisID(HAND DeviceHandle, U16 LtcID, U32 AxisID)"""
    @staticmethod
    def Acm_DevGetLTCInAxisID(DeviceHandle: _VoidPtrArg, LtcID: int, AxisID: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevGetLTCInAxisID(HAND DeviceHandle, U16 LtcID, PU32 AxisID)"""
    @staticmethod
    def Acm_DevSetCmpAxisID(DeviceHandle: _VoidPtrArg, CmpID: int, AxisID: int, /) -> int:
        """U32 Acm_DevSetCmpAxisID(HAND DeviceHandle, U16 CmpID, U32 AxisID)"""
    @staticmethod
    def Acm_DevGetCmpAxisID(DeviceHandle: _VoidPtrArg, CmpID: int, AxisID: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevGetCmpAxisID(HAND DeviceHandle, U16 CmpID, PU32 AxisID)"""
    @staticmethod
    def Acm_GetDevNum(DevType: int, BoardID: int, DeviceNumber: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GetDevNum(U32 DevType, U32 BoardID, PU32 DeviceNumber)"""
    @staticmethod
    def Acm_DevSaveMapFile(DeviceHandle: _VoidPtrArg, FilePath: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm_DevSaveMapFile(HAND DeviceHandle, PI8 FilePath)"""
    @staticmethod
    def Acm_DevLoadMapFile(DeviceHandle: _VoidPtrArg, FilePath: bytes | Array[c_char] | None, /) -> int:
        """U32 Acm_DevLoadMapFile(HAND DeviceHandle, PI8 FilePath)"""
    @staticmethod
    def Acm_DevUpLoadMapInfo(DeviceHandle: _VoidPtrArg, MapType: int, MapInfoArray: _PtrArg[DEV_IO_MAP_INFO], ArrayLength: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevUpLoadMapInfo(HAND DeviceHandle, U16 MapType, PDEV_IO_MAP_INFO MapInfoArray, PU32 ArrayLength)"""
    @staticmethod
    def Acm_DevDownLoadMapInfo(DeviceHandle: _VoidPtrArg, MapType: int, MapInfoArray: _PtrArg[DEV_IO_MAP_INFO], ArrayLength: int, /) -> int:
        """U32 Acm_DevDownLoadMapInfo(HAND DeviceHandle, U16 MapType, PDEV_IO_MAP_INFO MapInfoArray, U32 ArrayLength)"""
    @staticmethod
    def Acm_DevSetSlaveStates(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, SlvState: int, /) -> int:
        """U32 Acm_DevSetSlaveStates(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 SlvState)"""
    @staticmethod
    def Acm_DevGetSlaveStates(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, SlvState: _PtrArg[c_uint16], /) -> int:
        """U32 Acm_DevGetSlaveStates(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PU16 SlvState)"""
    @staticmethod
    def Acm_DevGetSlaveTxPDO(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, StartOffset: int, Length: int, DataArray: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DevGetSlaveTxPDO(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 StartOffset, U16 Length, PU8 DataArray)"""
    @staticmethod
    def Acm_DevGetSlaveRxPDO(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, StartOffset: int, Length: int, DataArray: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DevGetSlaveRxPDO(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 StartOffset, U16 Length, PU8 DataArray)"""
    @staticmethod
    def Acm_DevGetSlaveRxTxPDO(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Length: int, DataArray: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DevGetSlaveRxTxPDO(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Length, PU8 DataArray)"""
    @staticmethod
    def Acm_DevWriteSDOComplete(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Index: int, DataSize: int, pValue: _PtrArg[c_void_p], /) -> int:
        """U32 Acm_DevWriteSDOComplete(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 DataSize, IN PVOID pValue)"""
    @staticmethod
    def Acm_DevWriteSDOData(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Index: int, SubIndex: int, Type: int, DataSize: int, pValue: _PtrArg[c_void_p], /) -> int:
        """U32 Acm_DevWriteSDOData(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize, IN PVOID pValue)"""
    @staticmethod
    def Acm_DevReadSDOData(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Index: int, SubIndex: int, Type: int, DataSize: int, pValue: _PtrArg[c_void_p], /) -> int:
        """U32 Acm_DevReadSDOData(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize, OUT PVOID pValue)"""
    @staticmethod
    def Acm_DevReadSDOData_Req(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Index: int, SubIndex: int, Type: int, DataSize: int, /) -> int:
        """U32 Acm_DevReadSDOData_Req(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize)"""
    @staticmethod
    def Acm_DevReadSDOData_Res(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Index: int, SubIndex: int, Type: int, DataSize: int, pValue: _VoidPtrArg, /) -> int:
        """U32 Acm_DevReadSDOData_Res(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize, OUT PVOID pValue)"""
    @staticmethod
    def Acm_DevWriteSDOData_Req(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Index: int, SubIndex: int, Type: int, DataSize: int, pValue: _VoidPtrArg, /) -> int:
        """U32 Acm_DevWriteSDOData_Req(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize, IN PVOID pValue)"""
    @staticmethod
    def Acm_DevWriteSDOData_Res(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Index: int, SubIndex: int, Type: int, DataSize: int, /) -> int:
        """U32 Acm_DevWriteSDOData_Res(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize)"""
    @staticmethod
    def Acm_DevReadMultiSDOData_Req(DeviceHandle: _VoidPtrArg, RingNo: int, Requests: _PtrArg[MULTI_SDO_REQ], SDOCnt: int, /) -> int:
        """U32 Acm_DevReadMultiSDOData_Req(HAND DeviceHandle, U16 RingNo, PMULTI_SDO_REQ Requests, U16 SDOCnt)"""
    @staticmethod
    def Acm_DevReadMultiSDOData_Res(DeviceHandle: _VoidPtrArg, RingNo: int, Requests: _PtrArg[MULTI_SDO_REQ], SDOCnt: int, /) -> int:
        """U32 Acm_DevReadMultiSDOData_Res(HAND DeviceHandle, U16 RingNo, PMULTI_SDO_REQ Requests, U16 SDOCnt)"""
    @staticmethod
    def Acm_DevWriteMultiSDOData_Req(DeviceHandle: _VoidPtrArg, RingNo: int, Requests: _PtrArg[MULTI_SDO_REQ], SDOCnt: int, /) -> int:
        """U32 Acm_DevWriteMultiSDOData_Req(HAND DeviceHandle, U16 RingNo, PMULTI_SDO_REQ Requests, U16 SDOCnt)"""
    @staticmethod
    def Acm_DevWriteMultiSDOData_Res(DeviceHandle: _VoidPtrArg, RingNo: int, Requests: _PtrArg[MULTI_SDO_REQ], SDOCnt: int, /) -> int:
        """U32 Acm_DevWriteMultiSDOData_Res(HAND DeviceHandle, U16 RingNo, PMULTI_SDO_REQ Requests, U16 SDOCnt)"""
    @staticmethod
    def Acm_DevWritePDOData(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Index: int, SubIndex: int, Type: int, DataSize: int, pValue: _VoidPtrArg, /) -> int:
        """U32 Acm_DevWritePDOData(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize, IN PVOID pValue)"""
    @staticmethod
    def Acm_DevReadPDOData(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Index: int, SubIndex: int, Type: int, DataSize: int, pValue: _VoidPtrArg, /) -> int:
        """U32 Acm_DevReadPDOData(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize, OUT PVOID pValue)"""
    @staticmethod
    def Acm_DevWriteRegData(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Address: int, Type: int, DataSize: int, pValue: _VoidPtrArg, /) -> int:
        """U32 Acm_DevWriteRegData(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Address, IN U16 Type, IN U16 DataSize, IN PVOID pValue)"""
    @staticmethod
    def Acm_DevReadRegData(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Address: int, Type: int, DataSize: int, pValue: _VoidPtrArg, /) -> int:
        """U32 Acm_DevReadRegData(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Address, IN U16 Type, IN U16 DataSize, OUT PVOID pValue)"""
    @staticmethod
    def Acm_DevReadEmgMessage(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, DataSize: int, EmgMessage: _PtrArg[c_uint8], /) -> int:
        """U32 Acm_DevReadEmgMessage(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 DataSize, OUT PU8 EmgMessage)"""
    @staticmethod
    def Acm_DevReadSlvCommErrCnt(DeviceHandle: _VoidPtrArg, RingNo: int, ErrCntArray: _PtrArg[c_uint32], ArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevReadSlvCommErrCnt(HAND DeviceHandle, IN U16 RingNo, IN PU32 ErrCntArray, IN PU32 ArrayElements)"""
    @staticmethod
    def Acm_DaqLinkPDO(DeviceHandle: _VoidPtrArg, Type: int, Channel: int, RingNo: int, SlaveID: int, EntryIndex: int, EntrySubIndex: int, ProductCode: int, /) -> int:
        """U32 Acm_DaqLinkPDO(HAND DeviceHandle, U32 Type, U16 Channel, U32 RingNo, U32 SlaveID, U32 EntryIndex, U32 EntrySubIndex, U32 ProductCode)"""
    @staticmethod
    def Acm_AxMoveTorque(AxisHandle: _VoidPtrArg, Distance: float, Torque: float, TorqueSlope: float, Velocity: float, PressTime: float, Mode: int, /) -> int:
        """U32 Acm_AxMoveTorque(HAND AxisHandle, F64 Distance, F64 Torque, F64 TorqueSlope, F64 Velocity, F64 PressTime, U8 Mode)"""
    @staticmethod
    def Acm_AxGetActTorque(AxisHandle: _VoidPtrArg, Torque: _PtrArg[c_int32], /) -> int:
        """U32 Acm_AxGetActTorque(HAND AxisHandle, PI32 Torque)"""
    @staticmethod
    def Acm_Ax2DCompensateInAx(AxisHandle: _VoidPtrArg, RelAxisHandle: _VoidPtrArg, Coefficient: _PtrArg[c_double], RelCoefficient: _PtrArg[c_double], ArrayElements: int, /) -> int:
        """U32 Acm_Ax2DCompensateInAx(HAND AxisHandle, HAND RelAxisHandle, PF64 Coefficient, PF64 RelCoefficient, U32 ArrayElements)"""
    @staticmethod
    def Acm_Ax1DCompensateTable(AxisHandle: _VoidPtrArg, OriginPos: float, Pitch: float, OffsetData: _PtrArg[c_double], OffsetElements: int, Direction: int, /) -> int:
        """U32 Acm_Ax1DCompensateTable(HAND AxisHandle, F64 OriginPos, F64 Pitch, PF64 OffsetData, U32 OffsetElements, U32 Direction)"""
    @staticmethod
    def Acm_DevZAxisCompensateTable(DeviceHandle: _VoidPtrArg, AxisHandle: _VoidPtrArg, RelAxisHandle: _VoidPtrArg, ZAxisHandle: _VoidPtrArg, OriginPosX: float, OriginPosY: float, PitchX: float, PitchY: float, OffsetDataZ: _PtrArg[c_double], OffsetElementsX: int, OffsetElementsY: int, /) -> int:
        """U32 Acm_DevZAxisCompensateTable(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, HAND ZAxisHandle, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataZ, U32 OffsetElementsX, U32 OffsetElementsY)"""
    @staticmethod
    def Acm_Dev2DCompensateTable(DeviceHandle: _VoidPtrArg, AxisHandle: _VoidPtrArg, RelAxisHandle: _VoidPtrArg, OriginPosX: float, OriginPosY: float, PitchX: float, PitchY: float, OffsetDataX: _PtrArg[c_double], OffsetDataY: _PtrArg[c_double], OffsetElementsX: int, OffsetElementsY: int, /) -> int:
        """U32 Acm_Dev2DCompensateTable(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataX, PF64 OffsetDataY, U32 OffsetElementsX, U32 OffsetElementsY)"""
    @staticmethod
    def Acm_AxGetCompensatePosition(AxisHandle: _VoidPtrArg, Position: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetCompensatePosition(HAND AxisHandle, PF64 Position)"""
    @staticmethod
    def Acm_AxZAxisCompensateTable(AxisHandle: _VoidPtrArg, ZAxisHandle: _VoidPtrArg, OriginPos: float, Pitch: float, OffsetDataZ: _PtrArg[c_double], OffsetElementsZ: int, Direction: int, /) -> int:
        """U32 Acm_AxZAxisCompensateTable(HAND AxisHandle, HAND ZAxisHandle, F64 OriginPos, F64 Pitch, PF64 OffsetDataZ, U32 OffsetElementsZ, U32 Direction)"""
    @staticmethod
    def Acm_AxGetPreview1DCompensatePosition(AxisHandle: _VoidPtrArg, Position: float, Direction: int, PreviewPosition: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetPreview1DCompensatePosition(HAND AxisHandle, F64 Position, U32 Direction, PF64 PreviewPosition)"""
    @staticmethod
    def Acm_DevGetPreview2DCompensatePosition(DeviceHandle: _VoidPtrArg, AxisHandle: _VoidPtrArg, RelAxisHandle: _VoidPtrArg, Position: float, RelPosition: float, Direction: int, RelDirection: int, PreviewPosition: _PtrArg[c_double], PreviewRelPosition: _PtrArg[c_double], /) -> int:
        """U32 Acm_DevGetPreview2DCompensatePosition(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, F64 Position, F64 RelPosition, U32 Direction, U32 RelDirection, PF64 PreviewPosition, PF64 PreviewRelPosition)"""
    @staticmethod
    def Acm_DevGetPreviewZAxisCompensatePosition(DeviceHandle: _VoidPtrArg, AxisHandle: _VoidPtrArg, RelAxisHandle: _VoidPtrArg, ZAxisHandle: _VoidPtrArg, Position: float, RelPosition: float, Direction: int, RelDirection: int, PreviewZPosition: _PtrArg[c_double], /) -> int:
        """U32 Acm_DevGetPreviewZAxisCompensatePosition(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, HAND ZAxisHandle, F64 Position, F64 RelPosition, U32 Direction, U32 RelDirection, PF64 PreviewZPosition)"""
    @staticmethod
    def Acm_DevMultiTrigInitial(DeviceHandle: _VoidPtrArg, RingNo: int, SlaveIP: int, Enable: int, PWM: int, LTC: int, MPG: int, /) -> int:
        """U32 Acm_DevMultiTrigInitial(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Enable, IN U8 PWM, IN U8 LTC, IN U8 MPG)"""
    @staticmethod
    def Acm_DevOscChannelDataStart(DeviceHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_DevOscChannelDataStart(HAND DeviceHandle)"""
    @staticmethod
    def Acm_DevOscChannelDataStop(DeviceHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_DevOscChannelDataStop(HAND DeviceHandle)"""
    @staticmethod
    def Acm_DevGetOscChannelDataConfig(DeviceHandle: _VoidPtrArg, ChannelID: int, oscflg: _PtrArg[OSC_PROFILE_PRM], /) -> int:
        """U32 Acm_DevGetOscChannelDataConfig(HAND DeviceHandle, U32 ChannelID, POSC_PROFILE_PRM oscflg)"""
    @staticmethod
    def Acm_DevSetOscChannelDataConfig(DeviceHandle: _VoidPtrArg, ChannelID: int, oscflg: OSC_PROFILE_PRM, /) -> int:
        """U32 Acm_DevSetOscChannelDataConfig(HAND DeviceHandle, U32 ChannelID, OSC_PROFILE_PRM oscflg)"""
    @staticmethod
    def Acm_DevGetOscChannelData(DeviceHandle: _VoidPtrArg, ChannelID: int, DataIndex: int, MaxCount: _PtrArg[c_uint32], DataBuffer: _PtrArg[c_double], /) -> int:
        """U32 Acm_DevGetOscChannelData(HAND DeviceHandle, U32 ChannelID, U32 DataIndex, PU32 MaxCount, PF64 DataBuffer)"""
    @staticmethod
    def Acm_DevGetOscChannelStatus(DeviceHandle: _VoidPtrArg, Status: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_DevGetOscChannelStatus(HAND DeviceHandle, PU32 Status)"""
    @staticmethod
    def Acm_GpEnableAxisFollow(GroupHandle: _VoidPtrArg, AxisArray: _PtrArg[c_uint32], OffsetValue: _PtrArg[c_double], RatioArray: _PtrArg[c_double], /) -> int:
        """U32 Acm_GpEnableAxisFollow(HAND GroupHandle, PU32 AxisArray, PF64 OffsetValue, PF64 RatioArray)"""
    @staticmethod
    def Acm_GpStopAxisFollow(GroupHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_GpStopAxisFollow(HAND GroupHandle)"""
    @staticmethod
    def Acm_GpSetFollowWpOffset(GroupHandle: _VoidPtrArg, WpCenterPos: _PtrArg[c_double], WpOffset: _PtrArg[c_double], /) -> int:
        """U32 Acm_GpSetFollowWpOffset(HAND GroupHandle, PF64 WpCenterPos, PF64 WpOffset)"""
    @staticmethod
    def Acm_EnableOneDevEventCallBack(DeviceHandle: _VoidPtrArg, EventID: int, /) -> int:
        """U32 Acm_EnableOneDevEventCallBack(HANDLE DeviceHandle, ULONG EventID)"""
    @staticmethod
    def Acm_AxGetRawData(AxisHandle: _VoidPtrArg, index: int, RawData: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetRawData(HAND AxisHandle, U8 index, PF64 RawData)"""
    @staticmethod
    def Acm_AxSetRawData(AxisHandle: _VoidPtrArg, index: int, RawData: float, /) -> int:
        """U32 Acm_AxSetRawData(HAND AxisHandle, U8 index, F64 RawData)"""
    @staticmethod
    def Acm_GpGetRawData(GroupHandle: _VoidPtrArg, index: int, RawData: _PtrArg[c_double], /) -> int:
        """U32 Acm_GpGetRawData(HAND GroupHandle, U8 index, PF64 RawData)"""
    @staticmethod
    def Acm_GpSetRawData(GroupHandle: _VoidPtrArg, index: int, RawData: float, /) -> int:
        """U32 Acm_GpSetRawData(HAND GroupHandle, U8 index, F64 RawData)"""
    @staticmethod
    def Acm_GpGetPausePosition(GroupHandle: _VoidPtrArg, RefPausePosition: _PtrArg[c_double], pArrayElements: _PtrArg[c_uint32], /) -> int:
        """U32 Acm_GpGetPausePosition(HAND GroupHandle, PF64 RefPausePosition, PU32 pArrayElements)"""
    @staticmethod
    def Acm_AxReturnPausePosition(AxHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxReturnPausePosition(HAND AxHandle)"""
    @staticmethod
    def Acm_AxAddOnAx(AxisHandle: _VoidPtrArg, MasAxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxAddOnAx(HAND AxisHandle, HAND MasAxisHandle)"""
    @staticmethod
    def Acm_AxAddRemove(AxisHandle: _VoidPtrArg, MasAxisHandle: _VoidPtrArg, /) -> int:
        """U32 Acm_AxAddRemove(HAND AxisHandle, HAND MasAxisHandle)"""
    @staticmethod
    def Acm_AxGetAddOnNum(AxisHandle: _VoidPtrArg, num: _PtrArg[c_int32], /) -> int:
        """U32 Acm_AxGetAddOnNum(HAND AxisHandle, PI32 num)"""
    @staticmethod
    def Acm_AxSetCompensateDistance(AxisHandle: _VoidPtrArg, Distance: float, /) -> int:
        """U32 Acm_AxSetCompensateDistance(HAND AxisHandle, F64 Distance)"""
    @staticmethod
    def Acm_AxGetCompensateDistance(AxisHandle: _VoidPtrArg, Distance: _PtrArg[c_double], /) -> int:
        """U32 Acm_AxGetCompensateDistance(HAND AxisHandle, PF64 Distance)"""

class AmcLogAPI:
    @staticmethod
    def Amc_SetApiLog(arg0: bytes | Array[c_char] | None, arg1: bytes | Array[c_char] | None, arg2: _PtrArg[AMC_API_LOG_OPT], arg3: int, /) -> int:
        """U32 Amc_SetApiLog(PI8 arg0, PI8 arg1, AMC_API_LOG_OPT* arg2, U64 arg3)"""
    @staticmethod
    def Amc_StartApiLog() -> int:
        """U32 Amc_StartApiLog()"""
    @staticmethod
    def Amc_StopApiLog() -> int:
        """U32 Amc_StopApiLog()"""
    @staticmethod
    def Amc_OpenApiLogFile(arg0: bytes | Array[c_char] | None, arg1: _PtrArg[c_void_p], /) -> int:
        """U32 Amc_OpenApiLogFile(PI8 arg0, PHAND arg1)"""
    @staticmethod
    def Amc_GetApiLogData(arg0: _VoidPtrArg, arg1: _PtrArg[c_uint8], arg2: int, arg3: _PtrArg[AMC_API_LOG_HEADER], /) -> int:
        """U32 Amc_GetApiLogData(HAND arg0, PU8 arg1, U32 arg2, AMC_API_LOG_HEADER* arg3)"""
    @staticmethod
    def Amc_CloseApiLogFile(arg0: _VoidPtrArg, /) -> int:
        """U32 Amc_CloseApiLogFile(HAND arg0)"""
    @staticmethod
    def Amc_ApiLogToString(arg0: _PtrArg[AMC_API_LOG_HEADER], arg1: _PtrArg[c_uint8], arg2: bytes | Array[c_char] | None, arg3: int, /) -> int:
        """U32 Amc_ApiLogToString(AMC_API_LOG_HEADER* arg0, PU8 arg1, PI8 arg2, U64 arg3)"""
    @staticmethod
    def Amc_ApiLogGetStatus(arg0: _PtrArg[AMC_API_LOG_STATUS], /) -> int:
        """U32 Amc_ApiLogGetStatus(AMC_API_LOG_STATUS* arg0)"""
    @staticmethod
    def Amc_DataLog_SetLog(DevID: int, Channel: int, source: _PtrArg[AMC_DATA_LOG_SOURCE], index: int, /) -> int:
        """U32 Amc_DataLog_SetLog(U32 DevID, U32 Channel, const LogDataSource* source, U16 index)"""
    @staticmethod
    def Amc_DataLog_GetLog(DevID: int, Channel: int, source: _PtrArg[AMC_DATA_LOG_SOURCE], index: int, /) -> int:
        """U32 Amc_DataLog_GetLog(U32 DevID, U32 Channel, LogDataSource* source, U16 index)"""
    @staticmethod
    def Amc_DataLog_SetLogOption(DevID: int, Channel: int, options: _PtrArg[AMC_DATA_LOG_OPTIONS], /) -> int:
        """U32 Amc_DataLog_SetLogOption(U32 DevID, U32 Channel, const DataLogOptions* options)"""
    @staticmethod
    def Amc_DataLog_GetLogOption(DevID: int, Channel: int, options: _PtrArg[AMC_DATA_LOG_OPTIONS], /) -> int:
        """U32 Amc_DataLog_GetLogOption(U32 DevID, U32 Channel, DataLogOptions* options)"""
    @staticmethod
    def Amc_DataLog_SetLogFilePath(DevID: int, Channel: int, dirPath: bytes | Array[c_char] | None, fileName: bytes | Array[c_char] | None, /) -> int:
        """U32 Amc_DataLog_SetLogFilePath(U32 DevID, U32 Channel, const char* dirPath, const char* fileName)"""
    @staticmethod
    def Amc_DataLog_GetLogFilePath(DevID: int, Channel: int, dirPath: bytes | Array[c_char] | None, fileName: bytes | Array[c_char] | None, /) -> int:
        """U32 Amc_DataLog_GetLogFilePath(U32 DevID, U32 Channel, char* dirPath, char* fileName)"""
    @staticmethod
    def Amc_DataLog_GetRotatedLogFilePaths(DevID: int, Channel: int, fileNamesBuffer: bytes | Array[c_char] | None, bufferSize: _PtrArg[c_uint32], fileCount: _PtrArg[c_uint32], /) -> int:
        """U32 Amc_DataLog_GetRotatedLogFilePaths(U32 DevID, U32 Channel, char* fileNamesBuffer, U32* bufferSize, PU32 fileCount)"""
    @staticmethod
    def Amc_DataLog_SetLogHeader(DevID: int, Channel: int, header: bytes | Array[c_char] | None, /) -> int:
        """U32 Amc_DataLog_SetLogHeader(U32 DevID, U32 Channel, const char* header)"""
    @staticmethod
    def Amc_DataLog_GetLogHeader(DevID: int, Channel: int, header: bytes | Array[c_char] | None, /) -> int:
        """U32 Amc_DataLog_GetLogHeader(U32 DevID, U32 Channel, char* header)"""
    @staticmethod
    def Amc_DataLog_GetStatus(DevID: int, Channel: int, outStatus: _PtrArg[AMC_DATA_LOG_STATUS], /) -> int:
        """U32 Amc_DataLog_GetStatus(U32 DevID, U32 Channel, LogStatus* outStatus)"""
    @staticmethod
    def Amc_DataLog_StartLog(DevID: int, Channel: int, /) -> int:
        """U32 Amc_DataLog_StartLog(U32 DevID, U32 Channel)"""
    @staticmethod
    def Amc_DataLog_StopLog(DevID: int, Channel: int, /) -> int:
        """U32 Amc_DataLog_StopLog(U32 DevID, U32 Channel)"""
    @staticmethod
    def Amc_DataLog_ResetLog(DevID: int, Channel: int, /) -> int:
        """U32 Amc_DataLog_ResetLog(U32 DevID, U32 Channel)"""
    @staticmethod
    def Amc_DataLog_GetLogFile(DevID: int, Channel: int, remoteFilePath: bytes | Array[c_char] | None, outBuffer: bytes | Array[c_char] | None, bufferSize: _PtrArg[c_uint32], /) -> int:
        """U32 Amc_DataLog_GetLogFile(U32 DevID, U32 Channel, const char* remoteFilePath, char* outBuffer, U32* bufferSize)"""
