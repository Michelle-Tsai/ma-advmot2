from maAdvMot2.AdvMotApi_CM2 import *
from maAdvMot2.MotionInfo import *
from maAdvMot2.AdvMotDrv import *
import os

if os.name == 'nt':
    lib = CDLL(r'C:\Windows\System32\ADVMOT.dll')
else:
    lib = CDLL('/usr/lib/libadvmot.so')

class AdvCmnAPI_CM2:
# Device
    try:
        mAcm2_DevOpen = lib.Acm2_DevOpen
        mAcm2_DevOpen.argtypes = [c_uint32, POINTER(DEVICEINFO)]
        mAcm2_DevOpen.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevInitialize = lib.Acm2_DevInitialize
        mAcm2_DevInitialize.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GetAvailableDevs = lib.Acm2_GetAvailableDevs
        mAcm2_GetAvailableDevs.argtypes = [POINTER(DEVLIST), c_uint32, POINTER(c_uint32)]
        mAcm2_GetAvailableDevs.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevExportMappingTable = lib.Acm2_DevExportMappingTable
        mAcm2_DevExportMappingTable.argtypes = [c_char_p]
        mAcm2_DevExportMappingTable.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevImportMappingTable = lib.Acm2_DevImportMappingTable
        mAcm2_DevImportMappingTable.argtypes = [POINTER(c_int8)]
        mAcm2_DevImportMappingTable.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GetMappedPhysicalID = lib.Acm2_GetMappedPhysicalID
        mAcm2_GetMappedPhysicalID.argtypes = [c_int, c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
        mAcm2_GetMappedPhysicalID.restype = c_uint32
    except:
        pass
    
    try:
        mAcm2_GetMappedLogicalIDList = lib.Acm2_GetMappedLogicalIDList
        mAcm2_GetMappedLogicalIDList.argtypes = [c_int, c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
        mAcm2_GetMappedLogicalIDList.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GetMappedObjInfo = lib.Acm2_GetMappedObjInfo
        mAcm2_GetMappedObjInfo.argtypes = [c_int, c_uint32, c_void_p]
        mAcm2_GetMappedObjInfo.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevAllClose = lib.Acm2_DevAllClose
        mAcm2_DevAllClose.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GetLastError = lib.Acm2_GetLastError
        mAcm2_GetLastError.argtypes = [c_uint, c_uint32]
        mAcm2_GetLastError.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GetProperty = lib.Acm2_GetProperty
        mAcm2_GetProperty.argtypes = [c_uint32, c_uint32, POINTER(c_double)]
        mAcm2_GetProperty.restype = c_uint32
    except:
        pass

    try:
        mAcm2_SetProperty = lib.Acm2_SetProperty
        mAcm2_SetProperty.argtypes = [c_uint32, POINTER(c_uint32), c_double]
        mAcm2_SetProperty.restype = c_uint32
    except:
        pass

    try:
        mAcm2_SetMultiProperty = lib.Acm2_SetMultiProperty
        mAcm2_SetMultiProperty.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_double), c_uint32, POINTER(c_uint32)]
        mAcm2_SetMultiProperty.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GetMultiProperty = lib.Acm2_GetMultiProperty
        mAcm2_GetMultiProperty.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_double), c_uint32, POINTER(c_uint32)]
        mAcm2_GetMultiProperty.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GetRawProperty = lib.Acm2_GetRawProperty
        mAcm2_GetRawProperty.argtypes = [c_uint32, c_uint32, c_void_p, POINTER(c_uint32)]
        mAcm2_GetRawProperty.restype = c_uint32
    except:
        pass

    try:
        mAcm2_EnableCallBackFuncForOneEvent = lib.Acm2_EnableCallBackFuncForOneEvent
        mAcm2_EnableCallBackFuncForOneEvent.argtypes = [c_uint32, c_int, CFUNCTYPE(c_uint32, c_uint32, c_void_p)]
        mAcm2_EnableCallBackFuncForOneEvent.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevLoadAllConfig = lib.Acm2_DevLoadAllConfig
        mAcm2_DevLoadAllConfig.argtypes = [c_char_p]
        mAcm2_DevLoadAllConfig.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevLoadConfig = lib.Acm2_DevLoadConfig
        mAcm2_DevLoadConfig.argtypes = [c_uint32, POINTER(c_int8)]
        mAcm2_DevLoadConfig.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevReadMailBox = lib.Acm2_DevReadMailBox
        mAcm2_DevReadMailBox.argtypes = [c_uint, c_uint32, c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        mAcm2_DevReadMailBox.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevWriteMailBox = lib.Acm2_DevWriteMailBox
        mAcm2_DevWriteMailBox.argtypes = [c_uint, c_uint32, c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        mAcm2_DevWriteMailBox.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GetErrors = lib.Acm2_GetErrors
        mAcm2_GetErrors.argtypes = [c_uint32, c_void_p, POINTER(c_uint32)]
        mAcm2_GetErrors.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ResetErrorRecord = lib.Acm2_ResetErrorRecord
        mAcm2_ResetErrorRecord.argtypes = [c_uint32]
        mAcm2_ResetErrorRecord.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevPreviewMotion = lib.Acm2_DevPreviewMotion
        mAcm2_DevPreviewMotion.argtypes = [c_uint32, POINTER(c_int8), POINTER(c_int8), c_uint16]
        mAcm2_DevPreviewMotion.restype = c_uint32
    except:
        pass
# Axis
    try:
        mAcm2_AxReturnPausePosition = lib.Acm2_AxReturnPausePosition
        mAcm2_AxReturnPausePosition.argtypes = [c_uint32]
        mAcm2_AxReturnPausePosition.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxSetSvOn = lib.Acm2_AxSetSvOn
        mAcm2_AxSetSvOn.argtypes = [c_uint32, c_uint]
        mAcm2_AxSetSvOn.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevSetAllSvOn = lib.Acm2_DevSetAllSvOn
        mAcm2_DevSetAllSvOn.argtypes = [c_uint]
        mAcm2_DevSetAllSvOn.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxSetErcOn = lib.Acm2_AxSetErcOn
        mAcm2_AxSetErcOn.argtypes = [c_uint32, c_uint]
        mAcm2_AxSetErcOn.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxResetAlm = lib.Acm2_AxResetAlm
        mAcm2_AxResetAlm.argtypes = [c_uint32, c_uint]
        mAcm2_AxResetAlm.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxPTP = lib.Acm2_AxPTP
        mAcm2_AxPTP.argtypes = [c_uint32, c_uint, c_double]
        mAcm2_AxPTP.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxMoveContinue = lib.Acm2_AxMoveContinue
        mAcm2_AxMoveContinue.argtypes = [c_uint32, c_uint]
        mAcm2_AxMoveContinue.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxMotionStop = lib.Acm2_AxMotionStop
        mAcm2_AxMotionStop.argtypes = [POINTER(c_uint32), c_uint32, c_uint, c_double]
        mAcm2_AxMotionStop.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxHome = lib.Acm2_AxHome
        mAcm2_AxHome.argtypes = [c_uint32, c_uint, c_uint]
        mAcm2_AxHome.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxMoveGantryHome = lib.Acm2_AxMoveGantryHome
        mAcm2_AxMoveGantryHome.argtypes = [c_uint32, c_uint, c_uint]
        mAcm2_AxMoveGantryHome.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxSetHomeSpeedProfile = lib.Acm2_AxSetHomeSpeedProfile
        mAcm2_AxSetHomeSpeedProfile.argtypes = [c_uint32, SPEED_PROFILE_PRM]
        mAcm2_AxSetHomeSpeedProfile.restype = c_uint32
    except:
        pass
    
    try:
        mAcm2_AxChangePos = lib.Acm2_AxChangePos
        mAcm2_AxChangePos.argtypes = [c_uint32, c_double]
        mAcm2_AxChangePos.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxChangeVel = lib.Acm2_AxChangeVel
        mAcm2_AxChangeVel.argtypes = [c_uint32, c_double, c_double, c_double]
        mAcm2_AxChangeVel.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxChangeVelByRate = lib.Acm2_AxChangeVelByRate
        mAcm2_AxChangeVelByRate.argtypes = [c_uint32, c_uint32, c_double, c_double]
        mAcm2_AxChangeVelByRate.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxMoveImpose = lib.Acm2_AxMoveImpose
        mAcm2_AxMoveImpose.argtypes = [c_uint32, c_double, c_double]
        mAcm2_AxMoveImpose.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxResetError = lib.Acm2_AxResetError
        mAcm2_AxResetError.argtypes = [c_uint32]
        mAcm2_AxResetError.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevResetAllError = lib.Acm2_DevResetAllError
        mAcm2_DevResetAllError.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxGetState = lib.Acm2_AxGetState
        mAcm2_AxGetState.argtypes = [c_uint32, c_uint, POINTER(c_uint32)]
        mAcm2_AxGetState.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxGetMotionIO = lib.Acm2_AxGetMotionIO
        mAcm2_AxGetMotionIO.argtypes = [c_uint32, POINTER(MOTION_IO)]
        mAcm2_AxGetMotionIO.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxSetPosition = lib.Acm2_AxSetPosition
        mAcm2_AxSetPosition.argtypes = [c_uint32, c_uint, c_double]
        mAcm2_AxSetPosition.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxGetPosition = lib.Acm2_AxGetPosition
        mAcm2_AxGetPosition.argtypes = [c_uint32, c_uint, POINTER(c_double)]
        mAcm2_AxGetPosition.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxGetMachPosition = lib.Acm2_AxGetMachPosition
        mAcm2_AxGetMachPosition.argtypes = [c_uint32, POINTER(c_double)]
        mAcm2_AxGetMachPosition.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxSetSpeedProfile = lib.Acm2_AxSetSpeedProfile
        mAcm2_AxSetSpeedProfile.argtypes = [c_uint32, SPEED_PROFILE_PRM]
        mAcm2_AxSetSpeedProfile.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxGetVel = lib.Acm2_AxGetVel
        mAcm2_AxGetVel.argtypes = [c_uint32, c_uint, POINTER(c_double)]
        mAcm2_AxGetVel.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxEnableExternalMode = lib.Acm2_AxEnableExternalMode
        mAcm2_AxEnableExternalMode.argtypes = [c_uint32, c_uint]
        mAcm2_AxEnableExternalMode.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxSoftJog = lib.Acm2_AxSoftJog
        mAcm2_AxSoftJog.argtypes = [c_uint32, c_uint]
        mAcm2_AxSoftJog.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxSetJogSpeedProfile = lib.Acm2_AxSetJogSpeedProfile
        mAcm2_AxSetJogSpeedProfile.argtypes = [c_uint32, JOG_SPEED_PROFILE_PRM]
        mAcm2_AxSetJogSpeedProfile.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxMotionStart = lib.Acm2_AxMotionStart
        mAcm2_AxMotionStart.argtypes = [c_uint32, c_uint32]
        mAcm2_AxMotionStart.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxPause = lib.Acm2_AxPause
        mAcm2_AxPause.argtypes = [c_uint32]
        mAcm2_AxPause.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxResume = lib.Acm2_AxResume
        mAcm2_AxResume.argtypes = [c_uint32]
        mAcm2_AxResume.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxResetPVTTable = lib.Acm2_AxResetPVTTable
        mAcm2_AxResetPVTTable.argtypes = [c_uint32]
        mAcm2_AxResetPVTTable.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxLoadPVTTable = lib.Acm2_AxLoadPVTTable
        mAcm2_AxLoadPVTTable.argtypes = [c_uint32, POINTER(c_double), POINTER(c_double), POINTER(c_double), c_uint32]
        mAcm2_AxLoadPVTTable.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxLoadPVTTableContinuous = lib.Acm2_AxLoadPVTTableContinuous
        mAcm2_AxLoadPVTTableContinuous.argtypes = [c_uint32, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), c_double, c_uint32]
        mAcm2_AxLoadPVTTableContinuous.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxMovePVT = lib.Acm2_AxMovePVT
        mAcm2_AxMovePVT.argtypes = [c_uint32]
        mAcm2_AxMovePVT.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxCheckPTBuffer = lib.Acm2_AxCheckPTBuffer
        mAcm2_AxCheckPTBuffer.argtypes = [c_uint32, POINTER(c_uint32)]
        mAcm2_AxCheckPTBuffer.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxAddPTData = lib.Acm2_AxAddPTData
        mAcm2_AxAddPTData.argtypes = [c_uint32, c_double, c_double]
        mAcm2_AxAddPTData.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxMovePT = lib.Acm2_AxMovePT
        mAcm2_AxMovePT.argtypes = [c_uint32]
        mAcm2_AxMovePT.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxResetPTData = lib.Acm2_AxResetPTData
        mAcm2_AxResetPTData.argtypes = [c_uint32]
        mAcm2_AxResetPTData.restype = c_uint32
    except:
        pass
# Follow
    try:
        mAcm2_AxGearIn = lib.Acm2_AxGearIn
        mAcm2_AxGearIn.argtypes = [c_uint32, c_uint32, GEAR_IN_PRM]
        mAcm2_AxGearIn.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxGantryIn = lib.Acm2_AxGantryIn
        mAcm2_AxGantryIn.argtypes = [c_uint32, c_uint32, GANTRY_IN_PRM]
        mAcm2_AxGantryIn.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxPhaseAx = lib.Acm2_AxPhaseAx
        mAcm2_AxPhaseAx.argtypes = [c_uint32, PHASE_AXIS_PRM]
        mAcm2_AxPhaseAx.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxSyncOut = lib.Acm2_AxSyncOut
        mAcm2_AxSyncOut.argtypes = [c_uint32]
        mAcm2_AxSyncOut.restype = c_uint32
    except:
        pass

# Group
    try:
        mAcm2_GpGetPausePosition = lib.Acm2_GpGetPausePosition
        mAcm2_GpGetPausePosition.argtypes = [c_uint32, POINTER(c_double)]
        mAcm2_GpGetPausePosition.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpCreate = lib.Acm2_GpCreate
        mAcm2_GpCreate.argtypes = [c_uint32, POINTER(c_uint32), c_uint32]
        mAcm2_GpCreate.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpGetAxesInGroup = lib.Acm2_GpGetAxesInGroup
        mAcm2_GpGetAxesInGroup.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
        mAcm2_GpGetAxesInGroup.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpResetError = lib.Acm2_GpResetError
        mAcm2_GpResetError.argtypes = [c_uint32]
        mAcm2_GpResetError.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpLine = lib.Acm2_GpLine
        mAcm2_GpLine.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_uint32)]
        mAcm2_GpLine.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpArc_Center = lib.Acm2_GpArc_Center
        mAcm2_GpArc_Center.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_uint]
        mAcm2_GpArc_Center.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpArc_3P = lib.Acm2_GpArc_3P
        mAcm2_GpArc_3P.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_double, c_uint]
        mAcm2_GpArc_3P.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpArc_Angle = lib.Acm2_GpArc_Angle
        mAcm2_GpArc_Angle.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_uint32), c_double, c_uint]
        mAcm2_GpArc_Angle.restype = c_uint32
    except:
        pass

    try:
        mAcm2_Gp3DArc_Center = lib.Acm2_Gp3DArc_Center
        mAcm2_Gp3DArc_Center.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_uint]
        mAcm2_Gp3DArc_Center.restype = c_uint32
    except:
        pass

    try:
        mAcm2_Gp3DArc_NormVec = lib.Acm2_Gp3DArc_NormVec
        mAcm2_Gp3DArc_NormVec.argtypese = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_float), c_double, c_uint]
        mAcm2_Gp3DArc_NormVec.restype = c_uint32
    except:
        pass

    try:
        mAcm2_Gp3DArc_3P = lib.Acm2_Gp3DArc_3P
        mAcm2_Gp3DArc_3P.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_uint, c_uint32]
        mAcm2_Gp3DArc_3P.restype = c_uint32
    except:
        pass

    try:
        mAcm2_Gp3DArc_3PAngle = lib.Acm2_Gp3DArc_3PAngle
        mAcm2_Gp3DArc_3PAngle.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_double, c_uint]
        mAcm2_Gp3DArc_3PAngle.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpHelix_Center = lib.Acm2_GpHelix_Center
        mAcm2_GpHelix_Center.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_uint]
        mAcm2_GpHelix_Center.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpHelix_3P = lib.Acm2_GpHelix_3P
        mAcm2_GpHelix_3P.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_uint]
        mAcm2_GpHelix_3P.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpHelix_Angle = lib.Acm2_GpHelix_Angle
        mAcm2_GpHelix_Angle.argtypes = [c_uint32, c_uint, POINTER(c_double), POINTER(c_double), POINTER(c_uint32), c_uint]
        mAcm2_GpHelix_Angle.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpResume = lib.Acm2_GpResume
        mAcm2_GpResume.argtypes = [c_uint32]
        mAcm2_GpResume.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpPause = lib.Acm2_GpPause
        mAcm2_GpPause.argtypes = [c_uint32]
        mAcm2_GpPause.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpMotionStop = lib.Acm2_GpMotionStop
        mAcm2_GpMotionStop.argtypes = [c_uint32, c_uint, c_double]
        mAcm2_GpMotionStop.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpChangeVel = lib.Acm2_GpChangeVel
        mAcm2_GpChangeVel.argtypes = [c_uint32, c_double, c_double, c_double]
        mAcm2_GpChangeVel.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpChangeVelByRate = lib.Acm2_GpChangeVelByRate
        mAcm2_GpChangeVelByRate.argtypes = [c_uint32, c_uint32, c_double, c_double]
        mAcm2_GpChangeVelByRate.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpGetVel = lib.Acm2_GpGetVel
        mAcm2_GpGetVel.argtypes = [c_uint32, c_uint, POINTER(c_double)]
        mAcm2_GpGetVel.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpSetSpeedProfile = lib.Acm2_GpSetSpeedProfile
        mAcm2_GpSetSpeedProfile.argtypes = [c_uint32, SPEED_PROFILE_PRM]
        mAcm2_GpSetSpeedProfile.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpGetState = lib.Acm2_GpGetState
        mAcm2_GpGetState.argtypes = [c_uint32, POINTER(c_uint32)]
        mAcm2_GpGetState.restype = c_uint32
    except:
        pass

# Path
    try:
        mAcm2_GpLoadPath = lib.Acm2_GpLoadPath
        mAcm2_GpLoadPath.argtypes = [c_uint32, POINTER(c_int8), POINTER(c_uint32)]
        mAcm2_GpLoadPath.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpAddPath = lib.Acm2_GpAddPath
        mAcm2_GpAddPath.argtypes = [c_uint32, c_uint32, c_uint, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), POINTER(c_uint32)]
        mAcm2_GpAddPath.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpMovePath = lib.Acm2_GpMovePath
        mAcm2_GpMovePath.argtypes = [c_uint32]
        mAcm2_GpMovePath.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpResetPath = lib.Acm2_GpResetPath
        mAcm2_GpResetPath.argtypes = [c_uint32]
        mAcm2_GpResetPath.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpGetPathStatus = lib.Acm2_GpGetPathStatus
        mAcm2_GpGetPathStatus.argtypes = [c_uint32, POINTER(PATH_STATUS)]
        mAcm2_GpGetPathStatus.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpMoveSelPath = lib.Acm2_GpMoveSelPath
        mAcm2_GpMoveSelPath.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32]
        mAcm2_GpMoveSelPath.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpGetPathIndexStatus = lib.Acm2_GpGetPathIndexStatus
        mAcm2_GpGetPathIndexStatus.argtypes = [c_uint32, c_uint32, POINTER(c_uint32), POINTER(c_uint32), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_uint32)]
        mAcm2_GpGetPathIndexStatus.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpDelay = lib.Acm2_GpDelay
        mAcm2_GpDelay.argtypes = [c_uint32, c_uint32]
        mAcm2_GpDelay.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpPathDO = lib.Acm2_GpPathDO
        mAcm2_GpPathDO.argtypes = [c_uint32, PATH_DO_PRM]
        mAcm2_GpPathDO.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpPathWaitDI = lib.Acm2_GpPathWaitDI
        mAcm2_GpPathWaitDI.argtypes = [c_uint32, PATH_DI_WAIT_PRM]
        mAcm2_GpPathWaitDI.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpPathWaitForAxis = lib.Acm2_GpPathWaitForAxis
        mAcm2_GpPathWaitForAxis.argtypes = [c_uint32, PATH_AX_WAIT_PRM]
        mAcm2_GpPathWaitForAxis.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpLookAheadPath = lib.Acm2_GpLookAheadPath
        mAcm2_GpLookAheadPath.argtypes = [c_uint32, c_uint16, POINTER(c_int8)]
        mAcm2_GpLookAheadPath.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpLookAheadPathFile = lib.Acm2_GpLookAheadPathFile
        mAcm2_GpLookAheadPathFile.argtypes = [c_uint32, c_uint16, POINTER(c_int8), POINTER(c_int8), POINTER(c_uint32)]
        mAcm2_GpLookAheadPathFile.restype = c_uint32
    except:
        pass

    try:
        mAcm2_GpLoadAndMovePath = lib.Acm2_GpLoadAndMovePath
        mAcm2_GpLoadAndMovePath.argtypes = [c_uint32, POINTER(c_int8), POINTER(c_uint32)]
        mAcm2_GpLoadAndMovePath.restype = c_uint32
    except:
        pass

# DIO
    try:
        mAcm2_ChSetDOBit = lib.Acm2_ChSetDOBit
        mAcm2_ChSetDOBit.argtypes = [c_uint32, c_uint32]
        mAcm2_ChSetDOBit.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetDOBit = lib.Acm2_ChGetDOBit
        mAcm2_ChGetDOBit.argtypes = [c_uint32, POINTER(c_uint32)]
        mAcm2_ChGetDOBit.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetDIBit = lib.Acm2_ChGetDIBit
        mAcm2_ChGetDIBit.argtypes = [c_uint32, POINTER(c_uint32)]
        mAcm2_ChGetDIBit.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChSetDOBitByRingN = lib.Acm2_ChSetDOBitByRingN
        mAcm2_ChSetDOBitByRingN.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32]
        mAcm2_ChSetDOBitByRingN.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetDOBitByRingN = lib.Acm2_ChGetDOBitByRingN
        mAcm2_ChGetDOBitByRingN.argtypes = [c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        mAcm2_ChGetDOBitByRingN.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetDIBitByRingN = lib.Acm2_ChGetDIBitByRingN
        mAcm2_ChGetDIBitByRingN.argtypes = [c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        mAcm2_ChGetDIBitByRingN.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChSetDOByte = lib.Acm2_ChSetDOByte
        mAcm2_ChSetDOByte.argtypes = [c_uint32, c_uint32, POINTER(c_uint32)]
        mAcm2_ChSetDOByte.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetDOByte = lib.Acm2_ChGetDOByte
        mAcm2_ChGetDOByte.argtypes = [c_uint32, c_uint32, POINTER(c_uint32)]
        mAcm2_ChGetDOByte.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetDIByte = lib.Acm2_ChGetDIByte
        mAcm2_ChGetDIByte.argtypes = [c_uint32, c_uint32, POINTER(c_uint32)]
        mAcm2_ChGetDIByte.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChSetDOByteByRingNo = lib.Acm2_ChSetDOByteByRingNo
        mAcm2_ChSetDOByteByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        mAcm2_ChSetDOByteByRingNo.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetDOByteByRingNo = lib.Acm2_ChGetDOByteByRingNo
        mAcm2_ChGetDOByteByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        mAcm2_ChGetDOByteByRingNo.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetDIByteByRingNo = lib.Acm2_ChGetDIByteByRingNo
        mAcm2_ChGetDIByteByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32, POINTER(c_uint32)]
        mAcm2_ChGetDIByteByRingNo.restype = c_uint32
    except:
        pass
# AIO
    try:
        mAcm2_ChSetAOData = lib.Acm2_ChSetAOData
        mAcm2_ChSetAOData.argtypes = [c_uint32, c_uint, c_double]
        mAcm2_ChSetAOData.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetAOData = lib.Acm2_ChGetAOData
        mAcm2_ChGetAOData.argtypes = [c_uint32, c_uint, POINTER(c_double)]
        mAcm2_ChGetAOData.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChSetAODataByRingNo = lib.Acm2_ChSetAODataByRingNo
        mAcm2_ChSetAODataByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, c_uint, c_double]
        mAcm2_ChSetAODataByRingNo.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetAODataByRingNo = lib.Acm2_ChGetAODataByRingNo
        mAcm2_ChGetAODataByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, c_uint, POINTER(c_double)]
        mAcm2_ChGetAODataByRingNo.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetAIData = lib.Acm2_ChGetAIData
        mAcm2_ChGetAIData.argtypes = [c_uint32, c_uint, POINTER(c_double)]
        mAcm2_ChGetAIData.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetAIDataByRingNo = lib.Acm2_ChGetAIDataByRingNo
        mAcm2_ChGetAIDataByRingNo.argtypes = [c_uint32, c_uint32, c_uint32, c_uint, POINTER(c_double)]
        mAcm2_ChGetAIDataByRingNo.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetCntData = lib.Acm2_ChGetCntData
        mAcm2_ChGetCntData.argtypes = [c_uint32, POINTER(c_double)]
        mAcm2_ChGetCntData.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChSetCntData = lib.Acm2_ChSetCntData
        mAcm2_ChSetCntData.argtypes = [c_uint32, c_double]
        mAcm2_ChSetCntData.restype = c_uint32
    except:
        pass
# Motion DIO:Compare
    try:
        mAcm2_ChLinkCmpFIFO = lib.Acm2_ChLinkCmpFIFO
        mAcm2_ChLinkCmpFIFO.argtypes = [c_uint32, POINTER(c_uint32), c_uint32]
        mAcm2_ChLinkCmpFIFO.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChLinkCmpObject = lib.Acm2_ChLinkCmpObject
        mAcm2_ChLinkCmpObject.argtypes = [c_uint32, c_uint, POINTER(c_uint32), c_uint32]
        mAcm2_ChLinkCmpObject.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetLinkedCmpObject = lib.Acm2_ChGetLinkedCmpObject
        mAcm2_ChGetLinkedCmpObject.argtypes = [c_uint32, c_uint, POINTER(c_uint32), POINTER(c_uint32)]
        mAcm2_ChGetLinkedCmpObject.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChEnableCmp = lib.Acm2_ChEnableCmp
        mAcm2_ChEnableCmp.argtypes = [c_uint32, c_uint32]
        mAcm2_ChEnableCmp.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChSetCmpOut = lib.Acm2_ChSetCmpOut
        mAcm2_ChSetCmpOut.argtypes = [c_uint32, c_uint]
        mAcm2_ChSetCmpOut.restype = c_uint32
    except:
        pass
    
    try:
        mAcm2_ChSetCmpDoOut = lib.Acm2_ChSetCmpDoOut
        mAcm2_ChSetCmpDoOut.argtypes = [c_uint32, c_uint]
        mAcm2_ChSetCmpDoOut.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxGetCmpData = lib.Acm2_AxGetCmpData
        mAcm2_AxGetCmpData.argtypes = [c_uint32, POINTER(c_double)]
        mAcm2_AxGetCmpData.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetCmpData = lib.Acm2_ChGetCmpData
        mAcm2_ChGetCmpData.argtypes = [c_uint32, POINTER(c_double), c_uint32]
        mAcm2_ChGetCmpData.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxSetCmpTable = lib.Acm2_AxSetCmpTable
        mAcm2_AxSetCmpTable.argtypes = [c_uint32, POINTER(c_double), c_uint32]
        mAcm2_AxSetCmpTable.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxSetCmpAuto = lib.Acm2_AxSetCmpAuto
        mAcm2_AxSetCmpAuto.argtypes = [c_uint32, c_double, c_double, c_double]
        mAcm2_AxSetCmpAuto.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChSetCmpAuto = lib.Acm2_ChSetCmpAuto
        mAcm2_ChSetCmpAuto.argtypes = [c_uint32, c_double, c_double, c_double]
        mAcm2_ChSetCmpAuto.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChSetCmpBufferData = lib.Acm2_ChSetCmpBufferData
        mAcm2_ChSetCmpBufferData.argtypes = [c_uint32, POINTER(c_double), c_uint32]
        mAcm2_ChSetCmpBufferData.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChSetMultiCmpTable = lib.Acm2_ChSetMultiCmpTable
        mAcm2_ChSetMultiCmpTable.argtypes = [c_uint32, c_uint, c_uint32]
        mAcm2_ChSetMultiCmpTable.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChSetMultiCmpBufferData = lib.Acm2_ChSetMultiCmpBufferData
        mAcm2_ChSetMultiCmpBufferData.argtypes = [c_uint32, POINTER(c_double), c_uint32, c_uint32]
        mAcm2_ChSetMultiCmpBufferData.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChResetCmpData = lib.Acm2_ChResetCmpData
        mAcm2_ChResetCmpData.argtypes = [c_uint32]
        mAcm2_ChResetCmpData.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetCmpBufferStatus = lib.Acm2_ChGetCmpBufferStatus
        mAcm2_ChGetCmpBufferStatus.argtypes = [c_uint32, POINTER(BUFFER_STATUS)]
        mAcm2_ChGetCmpBufferStatus.restype = c_uint32
    except:
        pass
# Motion IO: Latch
    try:
        mAcm2_ChLinkLatchAxis = lib.Acm2_ChLinkLatchAxis
        mAcm2_ChLinkLatchAxis.argtypes = [c_uint32, POINTER(c_uint32), c_uint32]
        mAcm2_ChLinkLatchAxis.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChLinkLatchObject = lib.Acm2_ChLinkLatchObject
        mAcm2_ChLinkLatchObject.argtypes = [c_uint32, c_uint, POINTER(c_uint32), c_uint32]
        mAcm2_ChLinkLatchObject.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetLinkedLatchObject = lib.Acm2_ChGetLinkedLatchObject
        mAcm2_ChGetLinkedLatchObject.argtypes = [c_uint32, POINTER(c_uint),POINTER(c_uint32), POINTER(c_uint32)]
        mAcm2_ChGetLinkedLatchObject.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChTriggerLatch = lib.Acm2_ChTriggerLatch
        mAcm2_ChTriggerLatch.argtypes = [c_uint32]
        mAcm2_ChTriggerLatch.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxReadLatchBuffer = lib.Acm2_AxReadLatchBuffer
        mAcm2_AxReadLatchBuffer.argtypes = [c_uint32, POINTER(c_double), POINTER(c_uint32)]
        mAcm2_AxReadLatchBuffer.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChReadLatchBuffer = lib.Acm2_ChReadLatchBuffer
        mAcm2_ChReadLatchBuffer.argtypes = [c_uint32, POINTER(c_double), c_uint32, POINTER(c_uint32)]
        mAcm2_ChReadLatchBuffer.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxGetLatchBufferStatus = lib.Acm2_AxGetLatchBufferStatus
        mAcm2_AxGetLatchBufferStatus.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
        mAcm2_AxGetLatchBufferStatus.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetLatchBufferStatus = lib.Acm2_ChGetLatchBufferStatus
        mAcm2_ChGetLatchBufferStatus.argtypes = [c_uint32, POINTER(BUFFER_STATUS)]
        mAcm2_ChGetLatchBufferStatus.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxResetLatchBuffer = lib.Acm2_AxResetLatchBuffer
        mAcm2_AxResetLatchBuffer.argtypes = [c_uint32]
        mAcm2_AxResetLatchBuffer.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChResetLatchBuffer = lib.Acm2_ChResetLatchBuffer
        mAcm2_ChResetLatchBuffer.argtypes = [c_uint32]
        mAcm2_ChResetLatchBuffer.restype = c_uint32
    except:
        pass
# Motion IO: PWM
    try:
        mAcm2_ChLinkPWMTable = lib.Acm2_ChLinkPWMTable
        mAcm2_ChLinkPWMTable.argtypes = [c_uint32, c_uint, c_uint32]
        mAcm2_ChLinkPWMTable.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetLinkedPWMTable = lib.Acm2_ChGetLinkedPWMTable
        mAcm2_ChGetLinkedPWMTable.argtypes = [c_uint32, POINTER(c_uint), POINTER(c_uint32), POINTER(c_uint32)]
        mAcm2_ChGetLinkedPWMTable.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChSetPWMTable = lib.Acm2_ChSetPWMTable
        mAcm2_ChSetPWMTable.argtypes = [c_uint32, POINTER(c_double), POINTER(c_double), c_uint32]
        mAcm2_ChSetPWMTable.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChLoadPWMTableFile = lib.Acm2_ChLoadPWMTableFile
        mAcm2_ChLoadPWMTableFile.argtypes = [c_uint32, POINTER(c_int8), POINTER(c_uint32)]
        mAcm2_ChLoadPWMTableFile.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetPWMTableStatus = lib.Acm2_ChGetPWMTableStatus
        mAcm2_ChGetPWMTableStatus.argtypes = [c_uint32, POINTER(PWM_TABLE_STATUS)]
        mAcm2_ChGetPWMTableStatus.restype = c_uint32
    except:
        pass
# Motion IO: External Drive
    try:
        mAcm2_ChGetExtDriveData = lib.Acm2_ChGetExtDriveData
        mAcm2_ChGetExtDriveData.argtypes = [c_uint32, POINTER(c_double)]
        mAcm2_ChGetExtDriveData.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChSetExtDriveData = lib.Acm2_ChSetExtDriveData
        mAcm2_ChSetExtDriveData.argtypes = [c_uint32, c_double]
        mAcm2_ChSetExtDriveData.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChLinkExtDriveObject = lib.Acm2_ChLinkExtDriveObject
        mAcm2_ChLinkExtDriveObject.argtypes = [c_uint32, c_uint, c_uint32]
        mAcm2_ChLinkExtDriveObject.restype = c_uint32
    except:
        pass

    try:
        mAcm2_ChGetLinkedExtDriveObject = lib.Acm2_ChGetLinkedExtDriveObject
        mAcm2_ChGetLinkedExtDriveObject.argtypes = [c_uint32, POINTER(c_uint), POINTER(c_uint32), POINTER(c_uint32)]
        mAcm2_ChGetLinkedExtDriveObject.restype = c_uint32
    except:
        pass
# Motion DAQ
    try:
        mAcm2_DevMDaqConfig = lib.Acm2_DevMDaqConfig
        mAcm2_DevMDaqConfig.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32, c_uint32, c_uint32]
        mAcm2_DevMDaqConfig.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevMDaqGetConfig = lib.Acm2_DevMDaqGetConfig
        mAcm2_DevMDaqGetConfig.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32)]
        mAcm2_DevMDaqGetConfig.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevMDaqStart = lib.Acm2_DevMDaqStart
        mAcm2_DevMDaqStart.argtypes = [c_uint32]
        mAcm2_DevMDaqStart.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevMDaqStop = lib.Acm2_DevMDaqStop
        mAcm2_DevMDaqStop.argtypes = [c_uint32]
        mAcm2_DevMDaqStop.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevMDaqReset = lib.Acm2_DevMDaqReset
        mAcm2_DevMDaqReset.argtypes = [c_uint32]
        mAcm2_DevMDaqReset.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevMDaqGetStatus = lib.Acm2_DevMDaqGetStatus
        mAcm2_DevMDaqGetStatus.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
        mAcm2_DevMDaqGetStatus.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevMDaqGetData = lib.Acm2_DevMDaqGetData
        mAcm2_DevMDaqGetData.argtypes = [c_uint32, c_uint32, c_uint32, POINTER(c_double)]
        mAcm2_DevMDaqGetData.restype = c_uint32
    except:
        pass
# Donwload DSP FW
    try:
        mAcm2_GetDSPFrmWareDwnLoadRate = lib.Acm2_GetDSPFrmWareDwnLoadRate
        mAcm2_GetDSPFrmWareDwnLoadRate.argtypes = [c_uint32, POINTER(c_double)]
        mAcm2_GetDSPFrmWareDwnLoadRate.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevDownLoadDSPFrmWare_STP2 = lib.Acm2_DevDownLoadDSPFrmWare_STP2
        mAcm2_DevDownLoadDSPFrmWare_STP2.argtypes = [c_uint32, POINTER(c_int8)]
        mAcm2_DevDownLoadDSPFrmWare_STP2.restype = c_uint32
    except:
        pass
# EtherCAT
    try:
        mAcm2_DevLoadENI = lib.Acm2_DevLoadENI
        mAcm2_DevLoadENI.argtypes = [c_uint32, c_char_p]
        mAcm2_DevLoadENI.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevConnect = lib.Acm2_DevConnect
        mAcm2_DevConnect.argtypes = [c_uint32]
        mAcm2_DevConnect.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevDisConnect = lib.Acm2_DevDisConnect
        mAcm2_DevDisConnect.argtypes = [c_uint32]
        mAcm2_DevDisConnect.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevGetSubDevicesID = lib.Acm2_DevGetSubDevicesID
        mAcm2_DevGetSubDevicesID.argtypes = [c_uint32, c_int, POINTER(c_uint32), POINTER(c_uint32)]
        mAcm2_DevGetSubDevicesID.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevGetMDeviceInfo = lib.Acm2_DevGetMDeviceInfo
        mAcm2_DevGetMDeviceInfo.argtypes = [c_uint32, POINTER(ADVAPI_MDEVICE_INFO)]
        mAcm2_DevGetMDeviceInfo.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevGetSubDeviceInfo = lib.Acm2_DevGetSubDeviceInfo
        mAcm2_DevGetSubDeviceInfo.argtypes = [c_uint32, c_uint, c_uint32, POINTER(ADVAPI_SUBDEVICE_INFO_CM2)]
        mAcm2_DevGetSubDeviceInfo.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevGetSubDeviceFwVersion = lib.Acm2_DevGetSubDeviceFwVersion
        mAcm2_DevGetSubDeviceFwVersion.argtypes = [c_uint32, c_int, c_uint32, c_char_p]
        mAcm2_DevGetSubDeviceFwVersion.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevSetSubDeviceID = lib.Acm2_DevSetSubDeviceID
        mAcm2_DevSetSubDeviceID.argtypes = [c_uint32, c_int, c_uint32, c_uint32]
        mAcm2_DevSetSubDeviceID.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevSetSubDeviceStates = lib.Acm2_DevSetSubDeviceStates
        mAcm2_DevSetSubDeviceStates.argtypes = [c_uint32, c_uint, c_uint32, POINTER(c_uint32)]
        mAcm2_DevSetSubDeviceStates.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevGetSubDeviceStates = lib.Acm2_DevGetSubDeviceStates
        mAcm2_DevGetSubDeviceStates.argtypes = [c_uint32, c_uint, c_uint32, POINTER(c_uint32)]
        mAcm2_DevGetSubDeviceStates.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevWriteSDO = lib.Acm2_DevWriteSDO
        mAcm2_DevWriteSDO.argtypes = [c_uint32, c_uint, c_uint32, c_uint32, c_uint32, c_uint32, c_uint32, c_void_p]
        mAcm2_DevWriteSDO.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevReadSDO = lib.Acm2_DevReadSDO
        mAcm2_DevReadSDO.argtypes = [c_uint32, c_uint, c_uint32, c_uint32, c_uint32, c_uint32, c_uint32, c_void_p]
        mAcm2_DevReadSDO.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevWritePDO = lib.Acm2_DevWritePDO
        mAcm2_DevWritePDO.argtypes = [c_uint32, c_uint, c_uint32, c_uint32, c_uint32, c_uint32, c_uint32, c_void_p]
        mAcm2_DevWritePDO.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevReadPDO = lib.Acm2_DevReadPDO
        mAcm2_DevReadPDO.argtypes = [c_uint32, c_uint, c_uint32, c_uint32, c_uint32, c_uint32, c_uint32, c_void_p]
        mAcm2_DevReadPDO.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevWriteReg = lib.Acm2_DevWriteReg
        mAcm2_DevWriteReg.argtypes = [c_uint32, c_uint, c_uint32, c_uint32, c_uint32, c_uint32, c_void_p]
        mAcm2_DevWriteReg.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevReadReg = lib.Acm2_DevReadReg
        mAcm2_DevReadReg.argtypes = [c_uint32, c_uint, c_uint32, c_uint32, c_uint32, c_uint32, c_void_p]
        mAcm2_DevReadReg.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevReadSubDeviceCommErrCnt = lib.Acm2_DevReadSubDeviceCommErrCnt
        mAcm2_DevReadSubDeviceCommErrCnt.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
        mAcm2_DevReadSubDeviceCommErrCnt.restype = c_uint32
    except:
        pass

    try:
        mAcm2_Ax1DCompensateTable = lib.Acm2_Ax1DCompensateTable
        mAcm2_Ax1DCompensateTable.argtypes = [c_uint32, c_double, c_double, POINTER(c_double), c_uint32, c_uint32]
        mAcm2_Ax1DCompensateTable.restype = c_uint32
    except:
        pass

    try:
        mAcm2_Ax2DCompensateTable = lib.Acm2_Ax2DCompensateTable
        mAcm2_Ax2DCompensateTable.argtypes = [c_uint32, c_uint32, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double), c_uint32, c_uint32]
        mAcm2_Ax2DCompensateTable.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxZAxisCompensateTable = lib.Acm2_AxZAxisCompensateTable
        mAcm2_AxZAxisCompensateTable.argtypes = [c_uint32, c_uint32, c_uint32, c_double, c_double, c_double, c_double, POINTER(c_double), c_uint32, c_uint32]
        mAcm2_AxZAxisCompensateTable.restype = c_uint32
    except:
        pass

    try:
        mAcm2_AxGetCompensatePosition = lib.Acm2_AxGetCompensatePosition
        mAcm2_AxGetCompensatePosition.argtypes = [c_uint32, POINTER(c_double)]
        mAcm2_AxGetCompensatePosition.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevOscChannelDataStart = lib.Acm2_DevOscChannelDataStart
        mAcm2_DevOscChannelDataStart.argtypes = [c_uint32]
        mAcm2_DevOscChannelDataStart.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevOscChannelDataStop = lib.Acm2_DevOscChannelDataStop
        mAcm2_DevOscChannelDataStop.argtypes = [c_uint32]
        mAcm2_DevOscChannelDataStop.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevGetOscChannelDataConfig = lib.Acm2_DevGetOscChannelDataConfig
        mAcm2_DevGetOscChannelDataConfig.argtypes = [c_uint32, c_uint16, POINTER(OSC_PROFILE_PRM)]
        mAcm2_DevGetOscChannelDataConfig.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevSetOscChannelDataConfig = lib.Acm2_DevSetOscChannelDataConfig
        mAcm2_DevSetOscChannelDataConfig.argtypes = [c_uint32, c_uint16, OSC_PROFILE_PRM]
        mAcm2_DevSetOscChannelDataConfig.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevGetOscChannelData = lib.Acm2_DevGetOscChannelData
        mAcm2_DevGetOscChannelData.argtypes = [c_uint32, c_uint16, c_uint32, POINTER(c_uint32), POINTER(c_double)]
        mAcm2_DevGetOscChannelData.restype = c_uint32
    except:
        pass

    try:
        mAcm2_DevGetOscChannelStatus = lib.Acm2_DevGetOscChannelStatus
        mAcm2_DevGetOscChannelStatus.argtypes = [c_uint32, POINTER(c_uint32)]
        mAcm2_DevGetOscChannelStatus.restype = c_uint32
    except:
        pass