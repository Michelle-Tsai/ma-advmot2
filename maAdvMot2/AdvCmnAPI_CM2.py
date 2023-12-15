from maAdvMot2.AdvMotApi_CM2 import *
from maAdvMot2.MotionInfo import *
from maAdvMot2.AdvMotDrv import *
from maAdvMot2.utils import TypeDef
lib = CDLL('/usr/lib/libadvmot.so')

class AdvCmnAPI_CM2:
    mAcm2_DevOpen = lib.Acm2_DevOpen
    mAcm2_DevOpen.argtypes = [TypeDef.U32, POINTER(DEVICEINFO)]
    mAcm2_DevOpen.restype = c_uint32

    mAcm2_DevClose = lib.Acm2_DevClose
    mAcm2_DevClose.argtypes = [TypeDef.PU64]
    mAcm2_DevClose.restype = c_uint32

    mAcm2_DevInitialize = lib.Acm2_DevInitialize
    mAcm2_DevInitialize.restype = c_uint32

    mAcm2_GetAvailableDevs = lib.Acm2_GetAvailableDevs
    mAcm2_GetAvailableDevs.argtypes = [POINTER(DEVLIST), c_uint32, POINTER(c_uint32)]
    mAcm2_GetAvailableDevs.restype = c_uint32

    mAcm2_DevExportMappingTable = lib.Acm2_DevExportMappingTable
    mAcm2_DevExportMappingTable.argtypes = [c_char_p]
    mAcm2_DevExportMappingTable.restype = c_uint32

    # mAcm2_DevImportMappingTable = lib.Acm2_DevImportMappingTable
    # mAcm2_DevImportMappingTable.argtypes = [POINTER(c_int8)]
    # mAcm2_DevImportMappingTable.restype = c_uint32

    # mAcm2_GetMappedPhysicalID = lib.Acm2_GetMappedPhysicalID
    # mAcm2_GetMappedPhysicalID.argtypes = [c_int, c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
    # mAcm2_GetMappedPhysicalID.restype = c_uint32

    # mAcm2_GetMappedLogicalIDList = lib.Acm2_GetMappedLogicalIDList
    # mAcm2_GetMappedLogicalIDList.argtypes = [c_int, c_uint32, POINTER(c_uint32), POINTER(c_uint32)]
    # mAcm2_GetMappedLogicalIDList.restype = c_uint32

    # mAcm2_GetMappedObjInfo = lib.Acm2_GetMappedObjInfo
    # mAcm2_GetMappedObjInfo.argtypes = [c_int, c_uint32, c_void_p]
    # mAcm2_GetMappedObjInfo.restype = c_uint32

    # mAcm2_DevAllClose = lib.Acm2_DevAllClose
    # mAcm2_DevAllClose.restype = c_uint32

    # mAcm2_DevOpen_Internal = lib.Acm2_DevOpen_Internal
    # mAcm2_DevOpen_Internal.argtypes = [c_uint32, POINTER(DEVICEINFO)]
    # mAcm2_DevOpen_Internal.restype = c_uint32

    mAcm2_DevLoadAllConfig = lib.Acm2_DevLoadAllConfig
    mAcm2_DevLoadAllConfig.argtypes = [c_char_p]
    mAcm2_DevLoadAllConfig.restype = c_uint32

    # mAcm2_DevLoadConfig = lib.Acm2_DevLoadConfig
    # mAcm2_DevLoadConfig.argtypes = [c_uint32, POINTER(c_int8)]
    # mAcm2_DevLoadConfig.restype = c_uint32

    # mAcm2_DevFwDownload = lib.Acm2_DevFwDownload
    # mAcm2_DevFwDownload.argtypes = [c_uint32, c_uint32, c_uint32]
    # mAcm2_DevFwDownload.restype = c_uint32

    # mAcm2_DevSubDeviceFwDownload = lib.Acm2_DevSubDeviceFwDownload
    # mAcm2_DevSubDeviceFwDownload.argtypes = [c_uint32, c_uint32, POINTER(c_int8), POINTER(c_int8), c_uint32]
    # mAcm2_DevSubDeviceFwDownload.restype = c_uint32

    # mAcm2_DevWriteEEPROM = lib.Acm2_DevWriteEEPROM
    # mAcm2_DevWriteEEPROM.argtypes = [c_uint32, c_uint16, c_uint16]
    # mAcm2_DevWriteEEPROM.restype = c_uint32

    # mAcm2_DevReadEEPROM = lib.Acm2_DevReadEEPROM
    # mAcm2_DevReadEEPROM.argtypes = [c_uint32, c_uint16, POINTER(c_uint16)]
    # mAcm2_DevReadEEPROM.restype = c_uint32

    # mAcm2_DevEnableLTC = lib.Acm2_DevEnableLTC
    # mAcm2_DevEnableLTC.argtypes = [c_uint32, c_uint32]
    # mAcm2_DevEnableLTC.restype = c_uint32

    # mAcm2_DevLTCSaftyDist = lib.Acm2_DevLTCSaftyDist
    # mAcm2_DevLTCSaftyDist.argtypes = [c_uint32, c_double]
    # mAcm2_DevLTCSaftyDist.restype = c_uint32

    # mAcm2_DevGetLTCSaftyDist = lib.Acm2_DevGetLTCSaftyDist
    # mAcm2_DevGetLTCSaftyDist.argtypes = [c_uint32, POINTER(c_double)]
    # mAcm2_DevGetLTCSaftyDist.restype = c_uint32

    # mAcm2_DevEnableCmp = lib.Acm2_DevEnableCmp
    # mAcm2_DevEnableCmp.argtypes = [c_uint32, c_uint32]
    # mAcm2_DevEnableCmp.restype = c_uint32

    # mAcm2_DevLtcLinkCmp = lib.Acm2_DevLtcLinkCmp
    # mAcm2_DevLtcLinkCmp.argtypes = [c_uint32, POINTER(c_uint32)]
    # mAcm2_DevLtcLinkCmp.restype = c_uint32

    # mAcm2_DevGetLtcLinkCmpStatus = lib.Acm2_DevGetLtcLinkCmpStatus
    # mAcm2_DevGetLtcLinkCmpStatus.argtypes = [c_uint32, POINTER(c_uint32)]
    # mAcm2_DevGetLtcLinkCmpStatus.restype = c_uint32

    # mAcm2_DevSetCmp = lib.Acm2_DevSetCmp
    # mAcm2_DevSetCmp.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32, c_uint32, c_uint32]
    # mAcm2_DevSetCmp.restype = c_uint32

    # mAcm2_DevGetCmp = lib.Acm2_DevGetCmp
    # mAcm2_DevGetCmp.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32)]
    # mAcm2_DevGetCmp.restype = c_uint32

    # mAcm2_DevSetCmpDO = lib.Acm2_DevSetCmpDO
    # mAcm2_DevSetCmpDO.argtypes = [c_uint32, c_int]
    # mAcm2_DevSetCmpDO.restype = c_uint32

    # mAcm2_DevSetCmpData = lib.Acm2_DevSetCmpData
    # mAcm2_DevSetCmpData.argtypes = [c_uint32, c_double]
    # mAcm2_DevSetCmpData.restype = c_uint32

    # mAcm2_DevSetCmpFIFOData = lib.Acm2_DevSetCmpFIFOData
    # mAcm2_DevSetCmpFIFOData.argtypes = [c_uint32, POINTER(c_double), c_uint32]
    # mAcm2_DevSetCmpFIFOData.restype = c_uint32

    # mAcm2_DevSetCmpAuto = lib.Acm2_DevSetCmpAuto
    # mAcm2_DevSetCmpAuto.argtypes = [c_uint32, c_double, c_double, c_double]
    # mAcm2_DevSetCmpAuto.restype = c_uint32

    # mAcm2_DevGetCmpData = lib.Acm2_DevGetCmpData
    # mAcm2_DevGetCmpData.argtypes = [c_uint32, POINTER(c_double)]
    # mAcm2_DevGetCmpData.restype = c_uint32

    # mAcm2_DevEnableCmpFIFO = lib.Acm2_DevEnableCmpFIFO
    # mAcm2_DevEnableCmpFIFO.argtypes = [c_uint32, c_uint32]
    # mAcm2_DevEnableCmpFIFO.restype = c_uint32

    # mAcm2_DevGetCmpFIFOCount = lib.Acm2_DevGetCmpFIFOCount
    # mAcm2_DevGetCmpFIFOCount.argtypes = [c_uint32, POINTER(c_uint32)]
    # mAcm2_DevGetCmpFIFOCount.restype = c_uint32

    # mAcm2_DevGetCmpCounter = lib.Acm2_DevGetCmpCounter
    # mAcm2_DevGetCmpCounter.argtypes = [c_uint32, POINTER(c_uint32)]
    # mAcm2_DevGetCmpCounter.restype = c_uint32

    # mAcm2_DevResetCmpFIFO = lib.Acm2_DevResetCmpFIFO
    # mAcm2_DevResetCmpFIFO.argtypes = [c_uint32]
    # mAcm2_DevResetCmpFIFO.restype = c_uint32

    # mAcm2_DevSetLTCInPol = lib.Acm2_DevSetLTCInPol
    # mAcm2_DevSetLTCInPol.argtypes = [c_uint32, c_uint32]
    # mAcm2_DevSetLTCInPol.restype = c_uint32

    # mAcm2_DevGetLTCInPol = lib.Acm2_DevGetLTCInPol
    # mAcm2_DevGetLTCInPol.argtypes = [c_uint32, POINTER(c_uint32)]
    # mAcm2_DevGetLTCInPol.restype = c_uint32

    # mAcm2_DevSetLTCInEdge = lib.Acm2_DevSetLTCInEdge
    # mAcm2_DevSetLTCInEdge.argtypes = [c_uint32, c_uint32]
    # mAcm2_DevSetLTCInEdge.restype = c_uint32

    # mAcm2_DevGetLTCInEdge = lib.Acm2_DevGetLTCInEdge
    # mAcm2_DevGetLTCInEdge.argtypes = [c_uint32, POINTER(c_uint32)]
    # mAcm2_DevGetLTCInEdge.restype = c_uint32

    # mAcm2_DevGetLTCData = lib.Acm2_DevGetLTCData
    # mAcm2_DevGetLTCData.argtypes = [c_uint32, POINTER(c_double), POINTER(c_double)]
    # mAcm2_DevGetLTCData.restype = c_uint32

    # mAcm2_DevGetLTCFlag = lib.Acm2_DevGetLTCFlag
    # mAcm2_DevGetLTCFlag.argtypes = [c_uint32, POINTER(c_uint32)]
    # mAcm2_DevGetLTCFlag.restype = c_uint32

    # mAcm2_DevResetLTC = lib.Acm2_DevResetLTC
    # mAcm2_DevResetLTC.argtypes = [c_uint32]
    # mAcm2_DevResetLTC.restype = c_uint32

    # mAcm2_DevReadLatchBuffer = lib.Acm2_DevReadLatchBuffer
    # mAcm2_DevReadLatchBuffer.argtypes = [c_uint32, POINTER(c_double), POINTER(c_double), POINTER(c_uint32)]
    # mAcm2_DevReadLatchBuffer.restype = c_uint32

    # mAcm2_DevGetLatchBufferStatus = lib.Acm2_DevGetLatchBufferStatus
    # mAcm2_DevGetLatchBufferStatus.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_uint32), POINTER(c_uint32)]
    # mAcm2_DevGetLatchBufferStatus.restype = c_uint32

    # mAcm2_DevResetLatchBuffer = lib.Acm2_DevResetLatchBuffer
    # mAcm2_DevResetLatchBuffer.argtypes = [c_uint32]
    # mAcm2_DevResetLatchBuffer.restype = c_uint32

    # mAcm2_DevResetCmpFlag = lib.Acm2_DevResetCmpFlag
    # mAcm2_DevResetCmpFlag.argtypes = [c_uint32]
    # mAcm2_DevResetCmpFlag.restype = c_uint32

    # mAcm2_DevResetCmpData = lib.Acm2_DevResetCmpData
    # mAcm2_DevResetCmpData.argtypes = [c_uint32]
    # mAcm2_DevResetCmpData.restype = c_uint32

    # mAcm2_DevGetCmpFlag = lib.Acm2_DevGetCmpFlag
    # mAcm2_DevGetCmpFlag.argtypes = [c_uint32, POINTER(c_uint32)]
    # mAcm2_DevGetCmpFlag.restype = c_uint32

    # mAcm2_DevGetLTCInSource = lib.Acm2_DevGetLTCInSource
    # mAcm2_DevGetLTCInSource.argtypes = [c_uint32, POINTER(c_uint32)]
    # mAcm2_DevGetLTCInSource.restype = c_uint32

    # mAcm2_DevSetLTCInSource = lib.Acm2_DevSetLTCInSource
    # mAcm2_DevSetLTCInSource.argtypes = [c_uint32, c_uint16]
    # mAcm2_DevSetLTCInSource.restype = c_uint32

    # mAcm2_DevPreviewMotion = lib.Acm2_DevPreviewMotion
    # mAcm2_DevPreviewMotion.argtypes = [c_uint32, POINTER(c_int8), POINTER(c_int8), c_uint16]
    # mAcm2_DevPreviewMotion.restype = c_uint32

    mAcm2_SetProperty = lib.Acm2_SetProperty
    mAcm2_SetProperty.argtypes = [c_uint32, POINTER(c_uint32), c_double]
    mAcm2_SetProperty.restype = c_uint32

    mAcm2_SetMultiProperty = lib.Acm2_SetMultiProperty
    mAcm2_SetMultiProperty.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_double), c_uint32, POINTER(c_uint32)]
    mAcm2_SetMultiProperty.restype = c_uint32

    mAcm2_GetProperty = lib.Acm2_GetProperty
    mAcm2_GetProperty.argtypes = [c_uint32, c_uint32, POINTER(c_double)]
    mAcm2_GetProperty.restype = c_uint32

    mAcm2_GetMultiProperty = lib.Acm2_GetMultiProperty
    mAcm2_GetMultiProperty.argtypes = [c_uint32, POINTER(c_uint32), POINTER(c_double), c_uint32, POINTER(c_uint32)]
    mAcm2_GetMultiProperty.restype = c_uint32

    # mAcm2_GetRawProperty = lib.Acm2_GetRawProperty
    # mAcm2_GetRawProperty.argtypes = [c_uint32, c_uint32, c_void_p, POINTER(c_uint32)]
    # mAcm2_GetRawProperty.restype = c_uint32

    mAcm2_DevLoadENI = lib.Acm2_DevLoadENI
    mAcm2_DevLoadENI.argtypes = [c_uint32, c_char_p]
    mAcm2_DevLoadENI.restype = c_uint32

    # mAcm2_DevConnect = lib.Acm2_DevConnect
    # mAcm2_DevConnect.argtypes = [c_uint32]
    # mAcm2_DevConnect.restype = c_uint32

    # mAcm2_DevDisConnect = lib.Acm2_DevDisConnect
    # mAcm2_DevDisConnect.argtypes = [c_uint32]
    # mAcm2_DevDisConnect.restype = c_uint32

    # mAcm2_DevReOpen = lib.Acm2_DevReOpen
    # mAcm2_DevReOpen.argtypes = [c_uint32]
    # mAcm2_DevReOpen.restype = c_uint32

    mAcm2_DevGetMDeviceInfo = lib.Acm2_DevGetMDeviceInfo
    mAcm2_DevGetMDeviceInfo.argtypes = [c_uint32, POINTER(ADVAPI_MDEVICE_INFO)]
    mAcm2_DevGetMDeviceInfo.restype = c_uint32

    # mAcm2_DevGetSubDeviceDataCnt = lib.Acm2_DevGetSubDeviceDataCnt
    # mAcm2_DevGetSubDeviceDataCnt.argtypes = [c_uint32, c_int, c_uint32, c_uint32, POINTER(c_uint32)]
    # mAcm2_DevGetSubDeviceDataCnt.restype = c_uint32

    # mAcm2_DevGetSubDeviceFwVersion = lib.Acm2_DevGetSubDeviceFwVersion
    # mAcm2_DevGetSubDeviceFwVersion.argtypes = [c_uint32, c_int, c_uint32, c_char_p]
    # mAcm2_DevGetSubDeviceFwVersion.restype = c_uint32

    # mAcm2_DevSetSubDeviceID = lib.Acm2_DevSetSubDeviceID
    # mAcm2_DevSetSubDeviceID.argtypes = [c_uint32, c_int, c_uint32, c_uint32]
    # mAcm2_DevSetSubDeviceID.restype = c_uint32

    # mAcm2_DevGetSubDeviceID = lib.Acm2_DevGetSubDeviceID
    # mAcm2_DevGetSubDeviceID.argtypes = [c_uint32, c_uint32, POINTER(c_uint32)]
    # mAcm2_DevGetSubDeviceID.restype = c_uint32

    # mAcm2_DevGetSubDevicesID = lib.Acm2_DevGetSubDevicesID
    # mAcm2_DevGetSubDevicesID.argtypes = [c_uint32, c_int, POINTER(c_uint32), POINTER(c_uint32)]
    # mAcm2_DevGetSubDevicesID.restype = c_uint32

    # mAcm2_DevSaveMapFile = lib.Acm2_DevSaveMapFile
    # mAcm2_DevSaveMapFile.argtypes = [c_uint32, POINTER(c_int8)]
    # mAcm2_DevSaveMapFile.restype = c_uint32

    # mAcm2_DevLoadMapFile = lib.Acm2_DevLoadMapFile
    # mAcm2_DevLoadMapFile.argtypes = [c_uint32, POINTER(c_int8)]
    # mAcm2_DevLoadMapFile.restype = c_uint32

    # mAcm2_DevUpLoadMapInfo = lib.Acm2_DevUpLoadMapInfo
    # mAcm2_DevUpLoadMapInfo.argtypes = [c_uint32, c_uint16, ]
    # mAcm2_DevUpLoadMapInfo.restype = c_uint32

    # mAcm2_DevDownLoadMapInfo = lib.Acm2_DevDownLoadMapInfo
    # mAcm2_DevDownLoadMapInfo.argtypes = [TypeDef.U32, TypeDef.U16, POINTER(DEV_IO_MAP_INFO), TypeDef.U32]
    # mAcm2_DevDownLoadMapInfo.restype = TypeDef.U32

    mAcm2_DevGetSubDeviceInfo = lib.Acm2_DevGetSubDeviceInfo
    mAcm2_DevGetSubDeviceInfo.argtypes = [TypeDef.U32, c_uint, TypeDef.U32, POINTER(ADVAPI_SUBDEVICE_INFO_CM2)]
    mAcm2_DevGetSubDeviceInfo.restype = TypeDef.U32

    # mAcm2_DevGetModuleInfo = lib.Acm2_DevGetModuleInfo
    # mAcm2_DevGetModuleInfo.argtypes = [TypeDef.U32, c_uint, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.PVOID]
    # mAcm2_DevGetModuleInfo.restype = TypeDef.U32

    # mAcm2_DevGetIOInfo = lib.Acm2_DevGetIOInfo
    # mAcm2_DevGetIOInfo.argtypes = [TypeDef.U32, c_uint, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.PVOID]
    # mAcm2_DevGetIOInfo.restype = TypeDef.U32

    # mAcm2_DevSetSubDeviceStates = lib.Acm2_DevSetSubDeviceStates
    # mAcm2_DevSetSubDeviceStates.argtypes = [TypeDef.U32, c_uint, TypeDef.U32, TypeDef.PU32]
    # mAcm2_DevSetSubDeviceStates.restype = TypeDef.U32

    mAcm2_DevGetSubDeviceStates = lib.Acm2_DevGetSubDeviceStates
    mAcm2_DevGetSubDeviceStates.argtypes = [TypeDef.U32, c_uint, TypeDef.U32, TypeDef.PU32]
    mAcm2_DevGetSubDeviceStates.restype = TypeDef.U32

    # mAcm2_DevGetComStatus = lib.Acm2_DevGetComStatus
    # mAcm2_DevGetComStatus.argtypes = [TypeDef.U32, TypeDef.PU32]
    # mAcm2_DevGetComStatus.restype = TypeDef.U32

    # mAcm2_DevGetErrorTable = lib.Acm2_DevGetErrorTable
    # mAcm2_DevGetErrorTable.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.PU32]
    # mAcm2_DevGetErrorTable.restype = TypeDef.U32

    # mAcm2_DevEnableEvent = lib.Acm2_DevEnableEvent
    # mAcm2_DevEnableEvent.argtypes = [TypeDef.U32, TypeDef.U32]
    # mAcm2_DevEnableEvent.restype = TypeDef.U32

    # mAcm2_DevCheckEvent = lib.Acm2_DevCheckEvent
    # mAcm2_DevCheckEvent.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.U32]
    # mAcm2_DevCheckEvent.restype = TypeDef.U32

    # mAcm2_DevEnableEvent_All = lib.Acm2_DevEnableEvent_All
    # mAcm2_DevEnableEvent_All.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.PU32, TypeDef.PU32, TypeDef.U32, TypeDef.U32]
    # mAcm2_DevEnableEvent_All.restype = TypeDef.U32

    # mAcm2_DevCheckEvent_All = lib.Acm2_DevCheckEvent_All
    # mAcm2_DevCheckEvent_All.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.PU32, TypeDef.PU32, TypeDef.U32, TypeDef.U32, TypeDef.U32]
    # mAcm2_DevCheckEvent_All.restype = TypeDef.U32

    # mAcm2_CancelCheckEvent = lib.Acm2_CancelCheckEvent
    # mAcm2_CancelCheckEvent.argtypes = [c_uint, TypeDef.U32]
    # mAcm2_CancelCheckEvent.restype = TypeDef.U32

    # mAcm2_EnableEventCallBack = lib.Acm2_EnableEventCallBack
    # mAcm2_EnableEventCallBack.argtypes = [TypeDef.U32]
    # mAcm2_EnableEventCallBack.restype = TypeDef.U32

    # mAcm2_RegCallBackFunc = lib.Acm2_RegCallBackFunc
    # mAcm2_RegCallBackFunc.argtypes = [c_uint, TypeDef.U32, PADV_USER_CALLBACK_FUNC, TypeDef.PVOID]
    # mAcm2_RegCallBackFunc.restype = TypeDef.U32

    # mAcm2_RegCallBackFuncForOneEvent = lib.Acm2_RegCallBackFuncForOneEvent
    # mAcm2_RegCallBackFuncForOneEvent.argtypes = [c_uint, TypeDef.U32, TypeDef.U32, PADV_USER_CALLBACK_FUNC, TypeDef.PVOID]
    # mAcm2_RegCallBackFuncForOneEvent.restype = TypeDef.U32

    # mAcm2_DevSetLTCInAxisID = lib.Acm2_DevSetLTCInAxisID
    # mAcm2_DevSetLTCInAxisID.argtypes = [TypeDef.U32, TypeDef.U32]
    # mAcm2_DevSetLTCInAxisID.restype = TypeDef.U32

    # mAcm2_DevGetLTCInAxisID = lib.Acm2_DevGetLTCInAxisID
    # mAcm2_DevGetLTCInAxisID.argtypes = [TypeDef.U32, TypeDef.PU32]
    # mAcm2_DevGetLTCInAxisID.restype = TypeDef.U32

    # mAcm2_DevSetCmpAxisID = lib.Acm2_DevSetCmpAxisID
    # mAcm2_DevSetCmpAxisID.argtypes = [TypeDef.U32, TypeDef.U32]
    # mAcm2_DevSetCmpAxisID.restype = TypeDef.U32

    # mAcm2_DevGetCmpAxisID = lib.Acm2_DevGetCmpAxisID
    # mAcm2_DevGetCmpAxisID.argtypes = [TypeDef.U32, TypeDef.PU32]
    # mAcm2_DevGetCmpAxisID.restype = TypeDef.U32

    # mAcm2_CheckVersion = lib.Acm2_CheckVersion
    # mAcm2_CheckVersion.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.PU32]
    # mAcm2_CheckVersion.restype = TypeDef.U32

    # mAcm2_AxSetSvOn = lib.Acm2_AxSetSvOn
    # mAcm2_AxSetSvOn.argtypes = [TypeDef.U32, c_uint]
    # mAcm2_AxSetSvOn.restype = TypeDef.U32

    # mAcm2_DevSetAllSvOn = lib.Acm2_DevSetAllSvOn
    # mAcm2_DevSetAllSvOn.argtypes = [c_uint]
    # mAcm2_DevSetAllSvOn.restype = TypeDef.U32

    # mAcm2_AxResetAlm = lib.Acm2_AxResetAlm
    # mAcm2_AxResetAlm.argtypes = [TypeDef.U32, c_uint]
    # mAcm2_AxResetAlm.restype = TypeDef.U32

    # mAcm2_AxSetErcOn = lib.Acm2_AxSetErcOn
    # mAcm2_AxSetErcOn.argtypes = [TypeDef.U32, c_uint]
    # mAcm2_AxSetErcOn.restype = TypeDef.U32

    # mAcm2_AxPTP = lib.Acm2_AxPTP
    # mAcm2_AxPTP.argtypes = [TypeDef.U32, c_uint, TypeDef.F64]
    # mAcm2_AxPTP.restype = TypeDef.U32

    # mAcm2_AxReturnPausePosition = lib.Acm2_AxReturnPausePosition
    # mAcm2_AxReturnPausePosition.argtypes = [TypeDef.U32]
    # mAcm2_AxReturnPausePosition.restype = TypeDef.U32

    # mAcm2_AxMoveRel_EC = lib.Acm2_AxMoveRel_EC
    # mAcm2_AxMoveRel_EC.argtypes = [TypeDef.U32, TypeDef.F64]
    # mAcm2_AxMoveRel_EC.restype = TypeDef.U32

    # mAcm2_AxMoveAbs_EC = lib.Acm2_AxMoveAbs_EC
    # mAcm2_AxMoveAbs_EC.argtypes = [TypeDef.U32, TypeDef.F64]
    # mAcm2_AxMoveAbs_EC.restype = TypeDef.U32

    # mAcm2_AxPhaseAx = lib.Acm2_AxPhaseAx
    # mAcm2_AxPhaseAx.argtypes = [TypeDef.U32, PHASE_AXIS_PRM]
    # mAcm2_AxPhaseAx.restype = TypeDef.U32

    # mAcm2_AxChangeVel = lib.Acm2_AxChangeVel
    # mAcm2_AxChangeVel.argtypes = [TypeDef.U32, TypeDef.F64, TypeDef.F64, TypeDef.F64]
    # mAcm2_AxChangeVel.restype = TypeDef.U32

    # mAcm2_AxChangeVelByRate = lib.Acm2_AxChangeVelByRate
    # mAcm2_AxChangeVelByRate.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.F64, TypeDef.F64]
    # mAcm2_AxChangeVelByRate.restype = TypeDef.U32

    # mAcm2_AxMoveContinue = lib.Acm2_AxMoveContinue
    # mAcm2_AxMoveContinue.argtypes = [TypeDef.U32, c_uint]
    # mAcm2_AxMoveContinue.restype = TypeDef.U32

    # mAcm2_AxChangePos = lib.Acm2_AxChangePos
    # mAcm2_AxChangePos.argtypes = [TypeDef.U32, TypeDef.F64]
    # mAcm2_AxChangePos.restype = TypeDef.U32

    # mAcm2_AxResetError = lib.Acm2_AxResetError
    # mAcm2_AxResetError.argtypes = [TypeDef.U32]
    # mAcm2_AxResetError.restype = TypeDef.U32

    # mAcm2_DevResetAllError = lib.Acm2_DevResetAllError
    # mAcm2_DevResetAllError.argtypes = []
    # mAcm2_DevResetAllError.restype = TypeDef.U32

    # mAcm2_AxHomeEx = lib.Acm2_AxHomeEx
    # mAcm2_AxHomeEx.argtypes = [TypeDef.U32, TypeDef.U32]
    # mAcm2_AxHomeEx.restype = TypeDef.U32

    # mAcm2_AxHome = lib.Acm2_AxHome
    # mAcm2_AxHome.argtypes = [TypeDef.U32, c_uint, c_uint]
    # mAcm2_AxHome.restype = TypeDef.U32

    # mAcm2_AxSetHomeSpeedProfile = lib.Acm2_AxSetHomeSpeedProfile
    # mAcm2_AxSetHomeSpeedProfile.argtypes = [TypeDef.U32, SPEED_PROFILE_PRM]
    # mAcm2_AxSetHomeSpeedProfile.restype = TypeDef.U32

    # mAcm2_AxMoveGantryHome = lib.Acm2_AxMoveGantryHome
    # mAcm2_AxMoveGantryHome.argtypes = [TypeDef.U32, c_uint, c_uint]
    # mAcm2_AxMoveGantryHome.restype = TypeDef.U32

    # mAcm2_AxGetState = lib.Acm2_AxGetState
    # mAcm2_AxGetState.argtypes = [TypeDef.U32, c_uint, TypeDef.PU32]
    # mAcm2_AxGetState.restype = TypeDef.U32

    # mAcm2_AxGetMotionIO = lib.Acm2_AxGetMotionIO
    # mAcm2_AxGetMotionIO.argtypes = [TypeDef.U32, POINTER(MOTION_IO)]
    # mAcm2_AxGetMotionIO.restype = TypeDef.U32

    mAcm2_GetLastError = lib.Acm2_GetLastError
    mAcm2_GetLastError.argtypes = [ADV_OBJ_TYPE, TypeDef.U32]
    mAcm2_GetLastError.restype = TypeDef.U32

    # mAcm2_AxGetPosition = lib.Acm2_AxGetPosition
    # mAcm2_AxGetPosition.argtypes = [TypeDef.U32, c_uint, TypeDef.PF64]
    # mAcm2_AxGetPosition.restype = TypeDef.U32

    # mAcm2_AxSetPosition = lib.Acm2_AxSetPosition
    # mAcm2_AxSetPosition.argtypes = [TypeDef.U32, c_uint, TypeDef.F64]
    # mAcm2_AxSetPosition.restype = TypeDef.U32

    # mAcm2_AxGetMachPosition = lib.Acm2_AxGetMachPosition
    # mAcm2_AxGetMachPosition.argtypes = [TypeDef.U32, TypeDef.PF64]
    # mAcm2_AxGetMachPosition.restype = TypeDef.U32

    # mAcm2_AxGetLagCounter = lib.Acm2_AxGetLagCounter
    # mAcm2_AxGetLagCounter.argtypes = [TypeDef.U32, TypeDef.PF64]
    # mAcm2_AxGetLagCounter.restype = TypeDef.U32

    # mAcm2_AxGetVel = lib.Acm2_AxGetVel
    # mAcm2_AxGetVel.argtypes = [TypeDef.U32, c_uint, TypeDef.PF64]
    # mAcm2_AxGetVel.restype = TypeDef.U32

    # mAcm2_GpGetState = lib.Acm2_GpGetState
    # mAcm2_GpGetState.argtypes = [TypeDef.U32, TypeDef.PU32]
    # mAcm2_GpGetState.restype = TypeDef.U32

    # mAcm2_GpResetError = lib.Acm2_GpResetError
    # mAcm2_GpResetError.argtypes = [TypeDef.U32]
    # mAcm2_GpResetError.restype = TypeDef.U32

    # mAcm2_GpLine = lib.Acm2_GpLine
    # mAcm2_GpLine.argtypes = [TypeDef.U32, c_uint, TypeDef.PF64, TypeDef.PU32]
    # mAcm2_GpLine.restype = TypeDef.U32

    # mAcm2_GpArc_Center = lib.Acm2_GpArc_Center
    # mAcm2_GpArc_Center.argtypes = [TypeDef.U32, c_uint, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, c_uint]
    # mAcm2_GpArc_Center.restype = TypeDef.U32

    # mAcm2_Gp3DArc_Center = lib.Acm2_Gp3DArc_Center
    # mAcm2_Gp3DArc_Center.argtypes = [TypeDef.U32, c_uint, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, c_uint]
    # mAcm2_Gp3DArc_Center.restype = TypeDef.U32

    # mAcm2_Gp3DArc_NormVec = lib.Acm2_Gp3DArc_NormVec
    # mAcm2_Gp3DArc_NormVec.argtypese = [TypeDef.U32, c_uint, TypeDef.PF64, TypeDef.PF64, TypeDef.PF32, TypeDef.F64, c_uint]
    # mAcm2_Gp3DArc_NormVec.restype = TypeDef.U32

    # mAcm2_Gp3DArc_3P = lib.Acm2_Gp3DArc_3P
    # mAcm2_Gp3DArc_3P.argtypes = [TypeDef.U32, c_uint, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, c_uint, TypeDef.U32]
    # mAcm2_Gp3DArc_3P.restype = TypeDef.U32

    # mAcm2_Gp3DArc_3PAngle = lib.Acm2_Gp3DArc_3PAngle
    # mAcm2_Gp3DArc_3PAngle.argtypes = [TypeDef.U32, c_uint, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, TypeDef.F64, c_uint]
    # mAcm2_Gp3DArc_3PAngle.restype = TypeDef.U32

    # mAcm2_GpArc_3P = lib.Acm2_GpArc_3P
    # mAcm2_GpArc_3P.argtypes = [TypeDef.U32, c_uint, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, TypeDef.F64, c_uint]
    # mAcm2_GpArc_3P.restype = TypeDef.U32

    # mAcm2_GpLoadPath = lib.Acm2_GpLoadPath
    # mAcm2_GpLoadPath.argtypes = [TypeDef.U32, TypeDef.PI8, TypeDef.PU32]
    # mAcm2_GpLoadPath.restype = TypeDef.U32

    # mAcm2_GpLoadAndMovePath = lib.Acm2_GpLoadAndMovePath
    # mAcm2_GpLoadAndMovePath.argtypes = [TypeDef.U32, TypeDef.PI8, TypeDef.PU32]
    # mAcm2_GpLoadAndMovePath.restype = TypeDef.U32

    # mAcm2_RbLoadPath = lib.Acm2_RbLoadPath
    # mAcm2_RbLoadPath.argtypes = [TypeDef.U32, TypeDef.PI8, TypeDef.PU32]
    # mAcm2_RbLoadPath.restype = TypeDef.U32

    # mAcm2_GpMovePath = lib.Acm2_GpMovePath
    # mAcm2_GpMovePath.argtypes = [TypeDef.U32]
    # mAcm2_GpMovePath.restype = TypeDef.U32

    # mAcm2_GpMoveAllPath = lib.Acm2_GpMoveAllPath
    # mAcm2_GpMoveAllPath.argtypes = [TypeDef.PU32, TypeDef.U32]
    # mAcm2_GpMoveAllPath.restype = TypeDef.U32

    # mAcm2_GpResetPath = lib.Acm2_GpResetPath
    # mAcm2_GpResetPath.argtypes = [TypeDef.U32]
    # mAcm2_GpResetPath.restype = TypeDef.U32

    # mAcm2_GpAddPath = lib.Acm2_GpAddPath
    # mAcm2_GpAddPath.argtypes = [TypeDef.U32, TypeDef.U32, c_uint, TypeDef.F64, TypeDef.F64, TypeDef.F64, TypeDef.F64, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32]
    # mAcm2_GpAddPath.restype = TypeDef.U32

    # mAcm2_GpLookAheadPath = lib.Acm2_GpLookAheadPath
    # mAcm2_GpLookAheadPath.argtypes = [TypeDef.U32, TypeDef.U16, TypeDef.PI8]
    # mAcm2_GpLookAheadPath.restype = TypeDef.U32

    # mAcm2_GpLookAheadPathFile = lib.Acm2_GpLookAheadPathFile
    # mAcm2_GpLookAheadPathFile.argtypes = [TypeDef.U32, TypeDef.U16, TypeDef.PI8, TypeDef.PI8, TypeDef.PU32]
    # mAcm2_GpLookAheadPathFile.restype = TypeDef.U32

    # mAcm2_GpGetPathStatus = lib.Acm2_GpGetPathStatus
    # mAcm2_GpGetPathStatus.argtypes = [TypeDef.U32, POINTER(PATH_STATUS)]
    # mAcm2_GpGetPathStatus.restype = TypeDef.U32

    # mAcm2_GpMotionStop = lib.Acm2_GpMotionStop
    # mAcm2_GpMotionStop.argtypes = [TypeDef.U32, c_uint, TypeDef.F64]
    # mAcm2_GpMotionStop.restype = TypeDef.U32

    # mAcm2_GpChangeVel = lib.Acm2_GpChangeVel
    # mAcm2_GpChangeVel.argtypes = [TypeDef.U32, TypeDef.F64, TypeDef.F64, TypeDef.F64]
    # mAcm2_GpChangeVel.restype = TypeDef.U32

    # mAcm2_GpChangeVelByRate = lib.Acm2_GpChangeVelByRate
    # mAcm2_GpChangeVelByRate.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.F64, TypeDef.F64]
    # mAcm2_GpChangeVelByRate.restype = TypeDef.U32
    
    # mAcm2_AxSetCmpData = lib.Acm2_AxSetCmpData
    # mAcm2_AxSetCmpData.argtypes = [TypeDef.U32, TypeDef.F64]
    # mAcm2_AxSetCmpData.restype = TypeDef.U32

    # mAcm2_AxGetCmpData = lib.Acm2_AxGetCmpData
    # mAcm2_AxGetCmpData.argtypes = [TypeDef.U32, TypeDef.PF64]
    # mAcm2_AxGetCmpData.restype = TypeDef.U32

    # mAcm2_ChGetCmpData = lib.Acm2_ChGetCmpData
    # mAcm2_ChGetCmpData.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.U32]
    # mAcm2_ChGetCmpData.restype = TypeDef.U32

    # mAcm2_AxSetPWMTableOnTime = lib.Acm2_AxSetPWMTableOnTime
    # mAcm2_AxSetPWMTableOnTime.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.U32]
    # mAcm2_AxSetPWMTableOnTime.restype = TypeDef.U32

    # mAcm2_AxGetPWMOutState = lib.Acm2_AxGetPWMOutState
    # mAcm2_AxGetPWMOutState.argtypes = [TypeDef.U32, TypeDef.PU32]
    # mAcm2_AxGetPWMOutState.restype = TypeDef.U32

    # mAcm2_AxPWMOut = lib.Acm2_AxPWMOut
    # mAcm2_AxPWMOut.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.U32]
    # mAcm2_AxPWMOut.restype = TypeDef.U32

    # mAcm2_AxSetCmpTable = lib.Acm2_AxSetCmpTable
    # mAcm2_AxSetCmpTable.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.U32]
    # mAcm2_AxSetCmpTable.restype = TypeDef.U32

    # mAcm2_ChSetCmpBufferData = lib.Acm2_ChSetCmpBufferData
    # mAcm2_ChSetCmpBufferData.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.U32]
    # mAcm2_ChSetCmpBufferData.restype = TypeDef.U32

    # mAcm2_AxSetCmpAuto = lib.Acm2_AxSetCmpAuto
    # mAcm2_AxSetCmpAuto.argtypes = [TypeDef.U32, TypeDef.F64, TypeDef.F64, TypeDef.F64]
    # mAcm2_AxSetCmpAuto.restype = TypeDef.U32

    # mAcm2_ChSetCmpAuto = lib.Acm2_ChSetCmpAuto
    # mAcm2_ChSetCmpAuto.argtypes = [TypeDef.U32, TypeDef.F64, TypeDef.F64, TypeDef.F64]
    # mAcm2_ChSetCmpAuto.restype = TypeDef.U32

    # mAcm2_AxEnableExternalMode = lib.Acm2_AxEnableExternalMode
    # mAcm2_AxEnableExternalMode.argtypes = [TypeDef.U32, c_uint]
    # mAcm2_AxEnableExternalMode.restype = TypeDef.U32

    # mAcm2_RbSetExtDrive = lib.Acm2_RbSetExtDrive
    # mAcm2_RbSetExtDrive.argtypes = [TypeDef.U32, TypeDef.U16]
    # mAcm2_RbSetExtDrive.restype = TypeDef.U32

    # mAcm2_RbJog = lib.Acm2_RbJog
    # mAcm2_RbJog.argtypes = [TypeDef.U32, TypeDef.U16]
    # mAcm2_RbJog.restype = TypeDef.U32

    # mAcm2_AxSimStartSuspendVel = lib.Acm2_AxSimStartSuspendVel
    # mAcm2_AxSimStartSuspendVel.argtypes = [TypeDef.U32, TypeDef.U16]
    # mAcm2_AxSimStartSuspendVel.restype = TypeDef.U32

    # mAcm2_AxSimStartSuspendAbs = lib.Acm2_AxSimStartSuspendAbs
    # mAcm2_AxSimStartSuspendAbs.argtypes = [TypeDef.U32, TypeDef.F64]
    # mAcm2_AxSimStartSuspendAbs.restype = TypeDef.U32

    # mAcm2_AxSimStartSuspendRel = lib.Acm2_AxSimStartSuspendRel
    # mAcm2_AxSimStartSuspendRel.argtypes = [TypeDef.U32, TypeDef.F64]
    # mAcm2_AxSimStartSuspendRel.restype = TypeDef.U32

    # mAcm2_AxSimStart = lib.Acm2_AxSimStart
    # mAcm2_AxSimStart.argtypes = [TypeDef.U32]
    # mAcm2_AxSimStart.restype = TypeDef.U32

    # mAcm2_AxSimStop = lib.Acm2_AxSimStop
    # mAcm2_AxSimStop.argtypes = [TypeDef.U32]
    # mAcm2_AxSimStop.restype = TypeDef.U32

    # mAcm2_AxMoveImpose = lib.Acm2_AxMoveImpose
    # mAcm2_AxMoveImpose.argtypes = [TypeDef.U32, TypeDef.F64, TypeDef.F64]
    # mAcm2_AxMoveImpose.restype = TypeDef.U32

    # mAcm2_AxGetLatchData = lib.Acm2_AxGetLatchData
    # mAcm2_AxGetLatchData.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.PF64]
    # mAcm2_AxGetLatchData.restype = TypeDef.U32

    # mAcm2_AxGetLatchFlag = lib.Acm2_AxGetLatchFlag
    # mAcm2_AxGetLatchFlag.argtypes = [TypeDef.U32, TypeDef.PU8]
    # mAcm2_AxGetLatchFlag.restype = TypeDef.U32

    # mAcm2_ChLinkLatchAxis = lib.Acm2_ChLinkLatchAxis
    # mAcm2_ChLinkLatchAxis.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.U32]
    # mAcm2_ChLinkLatchAxis.restype = TypeDef.U32

    # mAcm2_ChLinkLatchObject = lib.Acm2_ChLinkLatchObject
    # mAcm2_ChLinkLatchObject.argtypes = [TypeDef.U32, c_uint, TypeDef.PU32, TypeDef.U32]
    # mAcm2_ChLinkLatchObject.restype = TypeDef.U32

    # mAcm2_ChGetLinkedLatchObject = lib.Acm2_ChGetLinkedLatchObject
    # mAcm2_ChGetLinkedLatchObject.argtypes = [TypeDef.U32, POINTER(c_uint),TypeDef.PU32, TypeDef.PU32]
    # mAcm2_ChGetLinkedLatchObject.restype = TypeDef.U32

    # mAcm2_AxTriggerLatch = lib.Acm2_AxTriggerLatch
    # mAcm2_AxTriggerLatch.argtypes = [TypeDef.U32]
    # mAcm2_AxTriggerLatch.restype = TypeDef.U32

    # mAcm2_ChTriggerLatch = lib.Acm2_ChTriggerLatch
    # mAcm2_ChTriggerLatch.argtypes = [TypeDef.U32]
    # mAcm2_ChTriggerLatch.restype = TypeDef.U32

    # mAcm2_AxSetCmdPosi_Pulse = lib.Acm2_AxSetCmdPosi_Pulse
    # mAcm2_AxSetCmdPosi_Pulse.argtypes = [TypeDef.U32, TypeDef.F64]
    # mAcm2_AxSetCmdPosi_Pulse.restype = TypeDef.U32

    # mAcm2_AxSpecialDiSetBit = lib.Acm2_AxSpecialDiSetBit
    # mAcm2_AxSpecialDiSetBit.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.U32]
    # mAcm2_AxSpecialDiSetBit.restype = TypeDef.U32

    # mAcm2_GpGetVel = lib.Acm2_GpGetVel
    # mAcm2_GpGetVel.argtypes = [TypeDef.U32, c_uint, TypeDef.PF64]
    # mAcm2_GpGetVel.restype = TypeDef.U32

    # mAcm2_RbGetCmdVel = lib.Acm2_RbGetCmdVel
    # mAcm2_RbGetCmdVel.argtypes = [TypeDef.U32, TypeDef.PF64]
    # mAcm2_RbGetCmdVel.restype = TypeDef.U32

    # mAcm2_DevLoadCAMTableFile = lib.Acm2_DevLoadCAMTableFile
    # mAcm2_DevLoadCAMTableFile.argtypes = [TypeDef.U32, TypeDef.PI8, TypeDef.U32, TypeDef.PU32, TypeDef.PU32]
    # mAcm2_DevLoadCAMTableFile.restype = TypeDef.U32

    # mAcm2_DevDownloadCAMTable = lib.Acm2_DevDownloadCAMTable
    # mAcm2_DevDownloadCAMTable.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.PF64, TypeDef.PF64, TypeDef.U32]
    # mAcm2_DevDownloadCAMTable.restype = TypeDef.U32

    # mAcm2_DevConfigCAMTable = lib.Acm2_DevConfigCAMTable
    # mAcm2_DevConfigCAMTable.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32]
    # mAcm2_DevConfigCAMTable.restype = TypeDef.U32

    # mAcm2_AxCamIn = lib.Acm2_AxCamIn
    # mAcm2_AxCamIn.argtypes = [TypeDef.U32, TypeDef.U32, CAM_IN_PRM]
    # mAcm2_AxCamIn.restype = TypeDef.U32

    # mAcm2_AxGearIn = lib.Acm2_AxGearIn
    # mAcm2_AxGearIn.argtypes = [TypeDef.U32, TypeDef.U32, GEAR_IN_PRM]
    # mAcm2_AxGearIn.restype = TypeDef.U32

    # mAcm2_AxTangentInGp = lib.Acm2_AxTangentInGp
    # mAcm2_AxTangentInGp.argtypes = [TypeDef.U32, TypeDef.U32, TANGENT_IN_PRM]
    # mAcm2_AxTangentInGp.restype = TypeDef.U32

    # mAcm2_AxGantryIn = lib.Acm2_AxGantryIn
    # mAcm2_AxGantryIn.argtypes = [TypeDef.U32, TypeDef.U32, GANTRY_IN_PRM]
    # mAcm2_AxGantryIn.restype = TypeDef.U32

    # mAcm2_AxReadLatchBuffer = lib.Acm2_AxReadLatchBuffer
    # mAcm2_AxReadLatchBuffer.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PU32]
    # mAcm2_AxReadLatchBuffer.restype = TypeDef.U32

    # mAcm2_ChReadLatchBuffer = lib.Acm2_ChReadLatchBuffer
    # mAcm2_ChReadLatchBuffer.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.U32, TypeDef.PU32]
    # mAcm2_ChReadLatchBuffer.restype = TypeDef.U32

    # mAcm2_AxResetLatchBuffer = lib.Acm2_AxResetLatchBuffer
    # mAcm2_AxResetLatchBuffer.argtypes = [TypeDef.U32]
    # mAcm2_AxResetLatchBuffer.restype = TypeDef.U32

    # mAcm2_ChResetLatchBuffer = lib.Acm2_ChResetLatchBuffer
    # mAcm2_ChResetLatchBuffer.argtypes = [TypeDef.U32]
    # mAcm2_ChResetLatchBuffer.restype = TypeDef.U32

    # mAcm2_AxGetINxStopStatus = lib.Acm2_AxGetINxStopStatus
    # mAcm2_AxGetINxStopStatus.argtypes = [TypeDef.U32, TypeDef.PU32]
    # mAcm2_AxGetINxStopStatus.restype = TypeDef.U32

    # mAcm2_AxResetINxStopStatus = lib.Acm2_AxResetINxStopStatus
    # mAcm2_AxResetINxStopStatus.argtypes = [TypeDef.U32]
    # mAcm2_AxResetINxStopStatus.restype = TypeDef.U32

    # mAcm2_AxGetLatchBufferStatus = lib.Acm2_AxGetLatchBufferStatus
    # mAcm2_AxGetLatchBufferStatus.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.PU32]
    # mAcm2_AxGetLatchBufferStatus.restype = TypeDef.U32

    # mAcm2_ChGetLatchBufferStatus = lib.Acm2_ChGetLatchBufferStatus
    # mAcm2_ChGetLatchBufferStatus.argtypes = [TypeDef.U32, POINTER(BUFFER_STATUS)]
    # mAcm2_ChGetLatchBufferStatus.restype = TypeDef.U32

    # mAcm2_AxSoftJog = lib.Acm2_AxSoftJog
    # mAcm2_AxSoftJog.argtypes = [TypeDef.U32, c_uint]
    # mAcm2_AxSoftJog.restype = TypeDef.U32

    # mAcm2_AxChangeCmpIndex = lib.Acm2_AxChangeCmpIndex
    # mAcm2_AxChangeCmpIndex.argtypes = [TypeDef.U32, TypeDef.U32]
    # mAcm2_AxChangeCmpIndex.restype = TypeDef.U32

    # mAcm2_GpGetINxStopStatus = lib.Acm2_GpGetINxStopStatus
    # mAcm2_GpGetINxStopStatus.argtypes = [TypeDef.U32, TypeDef.PU32]
    # mAcm2_GpGetINxStopStatus.restype = TypeDef.U32

    # mAcm2_GpResetINxStopStatus = lib.Acm2_GpResetINxStopStatus
    # mAcm2_GpResetINxStopStatus.argtypes = [TypeDef.U32]
    # mAcm2_GpResetINxStopStatus.restype = TypeDef.U32

    # mAcm2_AxDownloadTorqueTable = lib.Acm2_AxDownloadTorqueTable
    # mAcm2_AxDownloadTorqueTable.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.U32]
    # mAcm2_AxDownloadTorqueTable.restype = TypeDef.U32

    # mAcm2_AxLoadTorqueTableFile = lib.Acm2_AxLoadTorqueTableFile
    # mAcm2_AxLoadTorqueTableFile.argtypes = [TypeDef.U32, TypeDef.PI8, TypeDef.PU32]
    # mAcm2_AxLoadTorqueTableFile.restype = TypeDef.U32

    # mAcm2_AxMoveTorque = lib.Acm2_AxMoveTorque
    # mAcm2_AxMoveTorque.argtypes = [TypeDef.U32, TypeDef.F64, TypeDef.F64, TypeDef.F64, TypeDef.F64, TypeDef.U8]
    # mAcm2_AxMoveTorque.restype = TypeDef.U32

    # mAcm2_AxGetActTorque = lib.Acm2_AxGetActTorque
    # mAcm2_AxGetActTorque.argtypes = [TypeDef.U32, TypeDef.PI32]
    # mAcm2_AxGetActTorque.restype = TypeDef.U32

    # mAcm2_AxResetPVTTable = lib.Acm2_AxResetPVTTable
    # mAcm2_AxResetPVTTable.argtypes = [TypeDef.U32]
    # mAcm2_AxResetPVTTable.restype = TypeDef.U32

    # mAcm2_AxLoadPVTTable = lib.Acm2_AxLoadPVTTable
    # mAcm2_AxLoadPVTTable.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.PF64, TypeDef.U32]
    # mAcm2_AxLoadPVTTable.restype = TypeDef.U32

    # mAcm2_AxMovePVT = lib.Acm2_AxMovePVT
    # mAcm2_AxMovePVT.argtypes = [TypeDef.U32]
    # mAcm2_AxMovePVT.restype = TypeDef.U32

    # mAcm2_AxCheckPTBuffer = lib.Acm2_AxCheckPTBuffer
    # mAcm2_AxCheckPTBuffer.argtypes = [TypeDef.U32, TypeDef.PU32]
    # mAcm2_AxCheckPTBuffer.restype = TypeDef.U32

    # mAcm2_AxAddPTData = lib.Acm2_AxAddPTData
    # mAcm2_AxAddPTData.argtypes = [TypeDef.U32, TypeDef.F64, TypeDef.F64]
    # mAcm2_AxAddPTData.restype = TypeDef.U32

    # mAcm2_AxMovePT = lib.Acm2_AxMovePT
    # mAcm2_AxMovePT.argtypes = [TypeDef.U32]
    # mAcm2_AxMovePT.restype = TypeDef.U32

    # mAcm2_AxResetPTData = lib.Acm2_AxResetPTData
    # mAcm2_AxResetPTData.argtypes = [TypeDef.U32]
    # mAcm2_AxResetPTData.restype = TypeDef.U32

    # mAcm2_GpHelix_Center = lib.Acm2_GpHelix_Center
    # mAcm2_GpHelix_Center.argtypes = [TypeDef.U32, c_uint, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, c_uint]
    # mAcm2_GpHelix_Center.restype = TypeDef.U32

    # mAcm2_GpHelix_3P = lib.Acm2_GpHelix_3P
    # mAcm2_GpHelix_3P.argtypes = [TypeDef.U32, c_uint, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, c_uint]
    # mAcm2_GpHelix_3P.restype = TypeDef.U32

    # mAcm2_GpHelix_Angle = lib.Acm2_GpHelix_Angle
    # mAcm2_GpHelix_Angle.argtypes = [TypeDef.U32, c_uint, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, c_uint]
    # mAcm2_GpHelix_Angle.restype = TypeDef.U32

    # mAcm2_GpMoveSelPath = lib.Acm2_GpMoveSelPath
    # mAcm2_GpMoveSelPath.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32]
    # mAcm2_GpMoveSelPath.restype = TypeDef.U32

    # mAcm2_RbMoveSelPath = lib.Acm2_RbMoveSelPath
    # mAcm2_RbMoveSelPath.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U8]
    # mAcm2_RbMoveSelPath.restype = TypeDef.U32

    # mAcm2_GpGetPathIndexStatus = lib.Acm2_GpGetPathIndexStatus
    # mAcm2_GpGetPathIndexStatus.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.PU32, TypeDef.PU32, TypeDef.PF64, TypeDef.PF64, TypeDef.PF64, TypeDef.PF64, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32]
    # mAcm2_GpGetPathIndexStatus.restype = TypeDef.U32

    # mAcm2_RbGetPathIndexStatus = lib.Acm2_RbGetPathIndexStatus
    # mAcm2_RbGetPathIndexStatus.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.PU16, TypeDef.PU16, TypeDef.PF64, TypeDef.PF64, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32]
    # mAcm2_RbGetPathIndexStatus.restype = TypeDef.U32

    # mAcm2_DevDownLoadDSPFrmWare_STP1 = lib.Acm2_DevDownLoadDSPFrmWare_STP1
    # mAcm2_DevDownLoadDSPFrmWare_STP1.argtypes = [TypeDef.U32]
    # mAcm2_DevDownLoadDSPFrmWare_STP1.restype = TypeDef.U32

    # mAcm2_DevDownLoadDSPFrmWare_STP2 = lib.Acm2_DevDownLoadDSPFrmWare_STP2
    # mAcm2_DevDownLoadDSPFrmWare_STP2.argtypes = [TypeDef.U32, TypeDef.PI8]
    # mAcm2_DevDownLoadDSPFrmWare_STP2.restype = TypeDef.U32

    # mAcm2_DevDownLoadDSPFrmWare_STP3 = lib.Acm2_DevDownLoadDSPFrmWare_STP3
    # mAcm2_DevDownLoadDSPFrmWare_STP3.argtypes = [TypeDef.U32]
    # mAcm2_DevDownLoadDSPFrmWare_STP3.restype = TypeDef.U32

    # mAcm2_GetDSPFrmWareDwnLoadRate = lib.Acm2_GetDSPFrmWareDwnLoadRate
    # mAcm2_GetDSPFrmWareDwnLoadRate.argtypes = [TypeDef.U32, TypeDef.PF64]
    # mAcm2_GetDSPFrmWareDwnLoadRate.restype = TypeDef.U32

    # mAcm2_DownLoadCPLD_ST1 = lib.Acm2_DownLoadCPLD_ST1
    # mAcm2_DownLoadCPLD_ST1.argtypes = [TypeDef.U32, TypeDef.U16]
    # mAcm2_DownLoadCPLD_ST1.restype = TypeDef.U32

    # mAcm2_DownLoadCPLD_ST2 = lib.Acm2_DownLoadCPLD_ST2
    # mAcm2_DownLoadCPLD_ST2.argtypes = [TypeDef.U32, TypeDef.U16, TypeDef.PI8]
    # mAcm2_DownLoadCPLD_ST2.restype = TypeDef.U32

    # mAcm2_GetCPLDDownLoadRate = lib.Acm2_GetCPLDDownLoadRate
    # mAcm2_GetCPLDDownLoadRate.argtypes = [TypeDef.U32, TypeDef.PF64]
    # mAcm2_GetCPLDDownLoadRate.restype = TypeDef.U32

    # mAcm2_DownLoadMCU_ST1 = lib.Acm2_DownLoadMCU_ST1
    # mAcm2_DownLoadMCU_ST1.argtypes = [TypeDef.U32, TypeDef.U16]
    # mAcm2_DownLoadMCU_ST1.restype = TypeDef.U32

    # mAcm2_DownLoadMCU_ST2 = lib.Acm2_DownLoadMCU_ST2
    # mAcm2_DownLoadMCU_ST2.argtypes = [TypeDef.U32, TypeDef.U16, TypeDef.PI8]
    # mAcm2_DownLoadMCU_ST2.restype = TypeDef.U32

    # mAcm2_GetMCUDownLoadRate = lib.Acm2_GetMCUDownLoadRate
    # mAcm2_GetMCUDownLoadRate.argtypes = [TypeDef.U32, TypeDef.PF64]
    # mAcm2_GetMCUDownLoadRate.restype = TypeDef.U32

    # mAcm2_DevMDaqConfig = lib.Acm2_DevMDaqConfig
    # mAcm2_DevMDaqConfig.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32]
    # mAcm2_DevMDaqConfig.restype = TypeDef.U32

    # mAcm2_DevMDaqGetConfig = lib.Acm2_DevMDaqGetConfig
    # mAcm2_DevMDaqGetConfig.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.PU32, TypeDef.PU32, TypeDef.PU32, TypeDef.PU32]
    # mAcm2_DevMDaqGetConfig.restype = TypeDef.U32

    # mAcm2_DevMDaqStart = lib.Acm2_DevMDaqStart
    # mAcm2_DevMDaqStart.argtypes = [TypeDef.U32]
    # mAcm2_DevMDaqStart.restype = TypeDef.U32

    # mAcm2_DevMDaqStop = lib.Acm2_DevMDaqStop
    # mAcm2_DevMDaqStop.argtypes = [TypeDef.U32]
    # mAcm2_DevMDaqStop.restype = TypeDef.U32

    # mAcm2_DevMDaqReset = lib.Acm2_DevMDaqReset
    # mAcm2_DevMDaqReset.argtypes = [TypeDef.U32]
    # mAcm2_DevMDaqReset.restype = TypeDef.U32

    # mAcm2_DevMDaqGetStatus = lib.Acm2_DevMDaqGetStatus
    # mAcm2_DevMDaqGetStatus.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.PU32]
    # mAcm2_DevMDaqGetStatus.restype = TypeDef.U32

    # mAcm2_DevMDaqGetData = lib.Acm2_DevMDaqGetData
    # mAcm2_DevMDaqGetData.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.PF64]
    # mAcm2_DevMDaqGetData.restype = TypeDef.U32

    # mAcm2_DevWriteEEPROM_Ex = lib.Acm2_DevWriteEEPROM_Ex
    # mAcm2_DevWriteEEPROM_Ex.argtypes = [TypeDef.U32, TypeDef.U16, TypeDef.PU32, TypeDef.U32, TypeDef.PU32, TypeDef.U32]
    # mAcm2_DevWriteEEPROM_Ex.restype = TypeDef.U32

    # mAcm2_DevReadEEPROM_Ex = lib.Acm2_DevReadEEPROM_Ex
    # mAcm2_DevReadEEPROM_Ex.argtypes = [TypeDef.U32, TypeDef.U16, TypeDef.PU32, TypeDef.U32, TypeDef.PU32, TypeDef.U32]
    # mAcm2_DevReadEEPROM_Ex.restype = TypeDef.U32

    # mAcm2_GpArc_Angle = lib.Acm2_GpArc_Angle
    # mAcm2_GpArc_Angle.argtypes = [TypeDef.U32, c_uint, TypeDef.PF64, TypeDef.PU32, TypeDef.F64, c_uint]
    # mAcm2_GpArc_Angle.restype = TypeDef.U32

    # mAcm2_GpMoveArcRel_Angle = lib.Acm2_GpMoveArcRel_Angle
    # mAcm2_GpMoveArcRel_Angle.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.F64, TypeDef.PU32, TypeDef.I16]
    # mAcm2_GpMoveArcRel_Angle.restype = TypeDef.U32

    # mAcm2_GpMoveArcAbs_Angle = lib.Acm2_GpMoveArcAbs_Angle
    # mAcm2_GpMoveArcAbs_Angle.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.F64, TypeDef.PU32, TypeDef.I16]
    # mAcm2_GpMoveArcAbs_Angle.restype = TypeDef.U32

    # mAcm2_AxSetChannelCmpSetting = lib.Acm2_AxSetChannelCmpSetting
    # mAcm2_AxSetChannelCmpSetting.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32]
    # mAcm2_AxSetChannelCmpSetting.restype = TypeDef.U32

    # mAcm2_AxGetChannelCmpSetting = lib.Acm2_AxGetChannelCmpSetting
    # mAcm2_AxGetChannelCmpSetting.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.PU32, TypeDef.PU32, TypeDef.PU32, TypeDef.PU32]
    # mAcm2_AxGetChannelCmpSetting.restype = TypeDef.U32

    # mAcm2_AxAddChannelCmpDatas = lib.Acm2_AxAddChannelCmpDatas
    # mAcm2_AxAddChannelCmpDatas.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.PF64, TypeDef.U32]
    # mAcm2_AxAddChannelCmpDatas.restype = TypeDef.U32

    # mAcm2_AxResetChannelCmp = lib.Acm2_AxResetChannelCmp
    # mAcm2_AxResetChannelCmp.argtypes = [TypeDef.U32, TypeDef.U32]
    # mAcm2_AxResetChannelCmp.restype = TypeDef.U32

    # mAcm2_AxGetChannelCmpData = lib.Acm2_AxGetChannelCmpData
    # mAcm2_AxGetChannelCmpData.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.PF64]
    # mAcm2_AxGetChannelCmpData.restype = TypeDef.U32

    # mAcm2_AxLoadChannelNextData = lib.Acm2_AxLoadChannelNextData
    # mAcm2_AxLoadChannelNextData.argtypes = [TypeDef.U32, TypeDef.U32]
    # mAcm2_AxLoadChannelNextData.restype = TypeDef.U32

    # mAcm2_AxGetCmpbufferRemainCount = lib.Acm2_AxGetCmpbufferRemainCount
    # mAcm2_AxGetCmpbufferRemainCount.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.PU32]
    # mAcm2_AxGetCmpbufferRemainCount.restype = TypeDef.U32

    # mAcm2_RbGetActualPosition = lib.Acm2_RbGetActualPosition
    # mAcm2_RbGetActualPosition.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.U32]
    # mAcm2_RbGetActualPosition.restype = TypeDef.U32

    # mAcm2_RbGetCmdPosition = lib.Acm2_RbGetCmdPosition
    # mAcm2_RbGetCmdPosition.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.U32]
    # mAcm2_RbGetCmdPosition.restype = TypeDef.U32

    # mAcm2_RbGetArmActualPosition = lib.Acm2_RbGetArmActualPosition
    # mAcm2_RbGetArmActualPosition.argtypes = [TypeDef.U32, TypeDef.U16, TypeDef.PF64]
    # mAcm2_RbGetArmActualPosition.restype = TypeDef.U32

    # mAcm2_RbGetArmCmdPosition = lib.Acm2_RbGetArmCmdPosition
    # mAcm2_RbGetArmCmdPosition.argtypes = [TypeDef.U32, TypeDef.U16, TypeDef.PF64]
    # mAcm2_RbGetArmCmdPosition.restype = TypeDef.U32

    # mAcm2_RbGetWorldPosFromJoint = lib.Acm2_RbGetWorldPosFromJoint
    # mAcm2_RbGetWorldPosFromJoint.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64]
    # mAcm2_RbGetWorldPosFromJoint.restype = TypeDef.U32

    # mAcm2_GetDevNum = lib.Acm2_GetDevNum
    # mAcm2_GetDevNum.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.PU32]
    # mAcm2_GetDevNum.restype = TypeDef.U32

    # mAcm2_RbOpen = lib.Acm2_RbOpen
    # mAcm2_RbOpen.argtypes = [TypeDef.U32]
    # mAcm2_RbOpen.restype = TypeDef.U32

    # mAcm2_RbInitial = lib.Acm2_RbInitial
    # mAcm2_RbInitial.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.PF64, TypeDef.PF64, TypeDef.PI32, TypeDef.U32]
    # mAcm2_RbInitial.restype = TypeDef.U32

    # mAcm2_RbClose = lib.Acm2_RbClose
    # mAcm2_RbClose.argtypes = [TypeDef.U32]
    # mAcm2_RbClose.restype = TypeDef.U32

    # mAcm2_RbResetError = lib.Acm2_RbResetError
    # mAcm2_RbResetError.argtypes = [TypeDef.U32]
    # mAcm2_RbResetError.restype = TypeDef.U32

    # mAcm2_RbGetState = lib.Acm2_RbGetState
    # mAcm2_RbGetState.argtypes = [TypeDef.U32, TypeDef.PU16]
    # mAcm2_RbGetState.restype = TypeDef.U32

    # mAcm2_RbSetActPosition = lib.Acm2_RbSetActPosition
    # mAcm2_RbSetActPosition.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.U32]
    # mAcm2_RbSetActPosition.restype = TypeDef.U32

    # mAcm2_RbMoveRel = lib.Acm2_RbMoveRel
    # mAcm2_RbMoveRel.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PU32]
    # mAcm2_RbMoveRel.restype = TypeDef.U32

    # mAcm2_RbMoveAbs = lib.Acm2_RbMoveAbs
    # mAcm2_RbMoveAbs.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PU32]
    # mAcm2_RbMoveAbs.restype = TypeDef.U32

    # mAcm2_RbMoveDirectRel = lib.Acm2_RbMoveDirectRel
    # mAcm2_RbMoveDirectRel.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PU32]
    # mAcm2_RbMoveDirectRel.restype = TypeDef.U32

    # mAcm2_RbMoveDirectAbs = lib.Acm2_RbMoveDirectAbs
    # mAcm2_RbMoveDirectAbs.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PU32]
    # mAcm2_RbMoveDirectAbs.restype = TypeDef.U32

    # mAcm2_RbMoveLinearRel = lib.Acm2_RbMoveLinearRel
    # mAcm2_RbMoveLinearRel.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PU32]
    # mAcm2_RbMoveLinearRel.restype = TypeDef.U32

    # mAcm2_RbMoveLinearAbs = lib.Acm2_RbMoveLinearAbs
    # mAcm2_RbMoveLinearAbs.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PU32]
    # mAcm2_RbMoveLinearAbs.restype = TypeDef.U32

    # mAcm2_RbMoveArcAbs = lib.Acm2_RbMoveArcAbs
    # mAcm2_RbMoveArcAbs.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, TypeDef.I16]
    # mAcm2_RbMoveArcAbs.restype = TypeDef.U32

    # mAcm2_RbMoveArcRel = lib.Acm2_RbMoveArcRel
    # mAcm2_RbMoveArcRel.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, TypeDef.I16]
    # mAcm2_RbMoveArcRel.restype = TypeDef.U32

    # mAcm2_RbMoveArcRel_3P = lib.Acm2_RbMoveArcRel_3P
    # mAcm2_RbMoveArcRel_3P.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, TypeDef.I16]
    # mAcm2_RbMoveArcRel_3P.restype = TypeDef.U32

    # mAcm2_RbMoveArcAbs_3P = lib.Acm2_RbMoveArcAbs_3P
    # mAcm2_RbMoveArcAbs_3P.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, TypeDef.I16]
    # mAcm2_RbMoveArcAbs_3P.restype = TypeDef.U32

    # mAcm2_RbMoveArcRel_Angle = lib.Acm2_RbMoveArcRel_Angle
    # mAcm2_RbMoveArcRel_Angle.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.F64, TypeDef.PU32, TypeDef.I16]
    # mAcm2_RbMoveArcRel_Angle.restype = TypeDef.U32

    # mAcm2_RbMoveArcAbs_Angle = lib.Acm2_RbMoveArcAbs_Angle
    # mAcm2_RbMoveArcAbs_Angle.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.F64, TypeDef.PU32, TypeDef.I16]
    # mAcm2_RbMoveArcAbs_Angle.restype = TypeDef.U32

    # mAcm2_RbMove3DArcAbs = lib.Acm2_RbMove3DArcAbs
    # mAcm2_RbMove3DArcAbs.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, TypeDef.I16]
    # mAcm2_RbMove3DArcAbs.restype = TypeDef.U32

    # mAcm2_RbMove3DArcRel = lib.Acm2_RbMove3DArcRel
    # mAcm2_RbMove3DArcRel.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, TypeDef.I16]
    # mAcm2_RbMove3DArcRel.restype = TypeDef.U32

    # mAcm2_RbMove3DArcAbs_V = lib.Acm2_RbMove3DArcAbs_V
    # mAcm2_RbMove3DArcAbs_V.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.F64, TypeDef.PU32, TypeDef.I16]
    # mAcm2_RbMove3DArcAbs_V.restype = TypeDef.U32

    # mAcm2_RbMove3DArcRel_V = lib.Acm2_RbMove3DArcRel_V
    # mAcm2_RbMove3DArcRel_V.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.F64, TypeDef.PU32, TypeDef.I16]
    # mAcm2_RbMove3DArcRel_V.restype = TypeDef.U32

    # mAcm2_RbMove3DArcAbs_3P = lib.Acm2_RbMove3DArcAbs_3P
    # mAcm2_RbMove3DArcAbs_3P.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, TypeDef.I16, TypeDef.U16]
    # mAcm2_RbMove3DArcAbs_3P.restype = TypeDef.U32

    # mAcm2_RbMove3DArcRel_3P = lib.Acm2_RbMove3DArcRel_3P
    # mAcm2_RbMove3DArcRel_3P.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, TypeDef.I16, TypeDef.U16]
    # mAcm2_RbMove3DArcRel_3P.restype = TypeDef.U32

    # mAcm2_RbMove3DArcRel_3PAngle = lib.Acm2_RbMove3DArcRel_3PAngle
    # mAcm2_RbMove3DArcRel_3PAngle.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, TypeDef.I16, TypeDef.F64]
    # mAcm2_RbMove3DArcRel_3PAngle.restype = TypeDef.U32

    # mAcm2_RbMove3DArcAbs_3PAngle = lib.Acm2_RbMove3DArcAbs_3PAngle
    # mAcm2_RbMove3DArcAbs_3PAngle.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32, TypeDef.I16, TypeDef.F64]
    # mAcm2_RbMove3DArcAbs_3PAngle.restype = TypeDef.U32

    # mAcm2_RbAddPath = lib.Acm2_RbAddPath
    # mAcm2_RbAddPath.argtypes = [TypeDef.U32, TypeDef.U16, TypeDef.U16, TypeDef.F64, TypeDef.F64, TypeDef.PF64, TypeDef.PF64, TypeDef.PU32]
    # mAcm2_RbAddPath.restype = TypeDef.U32

    # mAcm2_RbResetPath = lib.Acm2_RbResetPath
    # mAcm2_RbResetPath.argtypes = [TypeDef.U32]
    # mAcm2_RbResetPath.restype = TypeDef.U32

    # mAcm2_RbGetPathStatus = lib.Acm2_RbGetPathStatus
    # mAcm2_RbGetPathStatus.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.PU32, TypeDef.PU32, TypeDef.PU32]
    # mAcm2_RbGetPathStatus.restype = TypeDef.U32

    # mAcm2_RbMovePath = lib.Acm2_RbMovePath
    # mAcm2_RbMovePath.argtypes = [TypeDef.U32]
    # mAcm2_RbMovePath.restype = TypeDef.U32

    # mAcm2_RbChangeVel = lib.Acm2_RbChangeVel
    # mAcm2_RbChangeVel.argtypes = [TypeDef.U32, TypeDef.F64]
    # mAcm2_RbChangeVel.restype = TypeDef.U32

    # mAcm2_RbChangeVelByRate = lib.Acm2_RbChangeVelByRate
    # mAcm2_RbChangeVelByRate.argtypes = [TypeDef.U32, TypeDef.U32]
    # mAcm2_RbChangeVelByRate.restype = TypeDef.U32

    # mAcm2_RbStopDec = lib.Acm2_RbStopDec
    # mAcm2_RbStopDec.argtypes = [TypeDef.U32]
    # mAcm2_RbStopDec.restype = TypeDef.U32

    # mAcm2_RbStopEmg = lib.Acm2_RbStopEmg
    # mAcm2_RbStopEmg.argtypes = [TypeDef.U32]
    # mAcm2_RbStopEmg.restype = TypeDef.U32

    # mAcm2_RbPauseMotion = lib.Acm2_RbPauseMotion
    # mAcm2_RbPauseMotion.argtypes = [TypeDef.U32]
    # mAcm2_RbPauseMotion.restype = TypeDef.U32

    # mAcm2_RbResumeMotion = lib.Acm2_RbResumeMotion
    # mAcm2_RbResumeMotion.argtypes = [TypeDef.U32]
    # mAcm2_RbResumeMotion.restype = TypeDef.U32

    # mAcm2_DevWriteMailBox = lib.Acm2_DevWriteMailBox
    # mAcm2_DevWriteMailBox.argtypes = [c_uint, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.PU32]
    # mAcm2_DevWriteMailBox.restype = TypeDef.U32

    # mAcm2_DevReadMailBox = lib.Acm2_DevReadMailBox
    # mAcm2_DevReadMailBox.argtypes = [c_uint, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.PU32]
    # mAcm2_DevReadMailBox.restype = TypeDef.U32

    mAcm2_DevWriteSDO = lib.Acm2_DevWriteSDO
    mAcm2_DevWriteSDO.argtypes = [TypeDef.U32, c_uint, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.PVOID]
    mAcm2_DevWriteSDO.restype = TypeDef.U32

    mAcm2_DevReadSDO = lib.Acm2_DevReadSDO
    mAcm2_DevReadSDO.argtypes = [TypeDef.U32, c_uint, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.PVOID]
    mAcm2_DevReadSDO.restype = TypeDef.U32

    mAcm2_DevWritePDO = lib.Acm2_DevWritePDO
    mAcm2_DevWritePDO.argtypes = [TypeDef.U32, c_uint, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.PVOID]
    mAcm2_DevWritePDO.restype = TypeDef.U32

    mAcm2_DevReadPDO = lib.Acm2_DevReadPDO
    mAcm2_DevReadPDO.argtypes = [TypeDef.U32, c_uint, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.PVOID]
    mAcm2_DevReadPDO.restype = TypeDef.U32

    mAcm2_DevWriteReg = lib.Acm2_DevWriteReg
    mAcm2_DevWriteReg.argtypes = [TypeDef.U32, c_uint, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.PVOID]
    mAcm2_DevWriteReg.restype = TypeDef.U32

    mAcm2_DevReadReg = lib.Acm2_DevReadReg
    mAcm2_DevReadReg.argtypes = [TypeDef.U32, c_uint, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.PVOID]
    mAcm2_DevReadReg.restype = TypeDef.U32

    # mAcm2_DevReadEmgMessage = lib.Acm2_DevReadEmgMessage
    # mAcm2_DevReadEmgMessage.argtypes = [TypeDef.U32, c_uint, TypeDef.U32, TypeDef.U32, TypeDef.PU8]
    # mAcm2_DevReadEmgMessage.restype = TypeDef.U32

    # mAcm2_DevReadSubDeviceCommErrCnt = lib.Acm2_DevReadSubDeviceCommErrCnt
    # mAcm2_DevReadSubDeviceCommErrCnt.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.PU32]
    # mAcm2_DevReadSubDeviceCommErrCnt.restype = TypeDef.U32

    # mAcm2_GpPause = lib.Acm2_GpPause
    # mAcm2_GpPause.argtypes = [TypeDef.U32]
    # mAcm2_GpPause.restype = TypeDef.U32

    # mAcm2_GpResume = lib.Acm2_GpResume
    # mAcm2_GpResume.argtypes = [TypeDef.U32]
    # mAcm2_GpResume.restype = TypeDef.U32

    # mAcm2_ServoSetCom = lib.Acm2_ServoSetCom
    # mAcm2_ServoSetCom.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.U32]
    # mAcm2_ServoSetCom.restype = TypeDef.U32

    # mAcm2_ServoGetAbsPosition = lib.Acm2_ServoGetAbsPosition
    # mAcm2_ServoGetAbsPosition.argtypes = [TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.U32, TypeDef.PF64]
    # mAcm2_ServoGetAbsPosition.restype = TypeDef.U32

    # mAcm2_DevMultiTrigSetPWMTableOnTime = lib.Acm2_DevMultiTrigSetPWMTableOnTime
    # mAcm2_DevMultiTrigSetPWMTableOnTime.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.U32]
    # mAcm2_DevMultiTrigSetPWMTableOnTime.restype = TypeDef.U32

    # mAcm2_DevMultiTrigSetCmpDO = lib.Acm2_DevMultiTrigSetCmpDO
    # mAcm2_DevMultiTrigSetCmpDO.argtypes = [TypeDef.U32, TypeDef.U32]
    # mAcm2_DevMultiTrigSetCmpDO.restype = TypeDef.U32

    # mAcm2_DevMultiTrigForceCmpOut = lib.Acm2_DevMultiTrigForceCmpOut
    # mAcm2_DevMultiTrigForceCmpOut.argtypes = [TypeDef.U32, c_uint]
    # mAcm2_DevMultiTrigForceCmpOut.restype = TypeDef.U32

    # mAcm2_AxSetCmpDO = lib.Acm2_AxSetCmpDO
    # mAcm2_AxSetCmpDO.argtypes = [TypeDef.U32, c_uint]
    # mAcm2_AxSetCmpDO.restype = TypeDef.U32

    # mAcm2_ChSetCmpOut = lib.Acm2_ChSetCmpOut
    # mAcm2_ChSetCmpOut.argtypes = [TypeDef.U32, c_uint]
    # mAcm2_ChSetCmpOut.restype = TypeDef.U32

    # mAcm2_ChSetCmpDoOut = lib.Acm2_ChSetCmpDoOut
    # mAcm2_ChSetCmpDoOut.argtypes = [TypeDef.U32, c_uint]
    # mAcm2_ChSetCmpDoOut.restype = TypeDef.U32

    # mAcm2_ChLinkCmpFIFO = lib.Acm2_ChLinkCmpFIFO
    # mAcm2_ChLinkCmpFIFO.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.U32]
    # mAcm2_ChLinkCmpFIFO.restype = TypeDef.U32

    # mAcm2_ChLinkCmpObject = lib.Acm2_ChLinkCmpObject
    # mAcm2_ChLinkCmpObject.argtypes = [TypeDef.U32, ADV_OBJ_TYPE, TypeDef.PU32, TypeDef.U32]
    # mAcm2_ChLinkCmpObject.restype = TypeDef.U32

    # mAcm2_ChGetLinkedCmpObject = lib.Acm2_ChGetLinkedCmpObject
    # mAcm2_ChGetLinkedCmpObject.argtypes = [TypeDef.U32, ADV_OBJ_TYPE, TypeDef.PU32, TypeDef.PU32]
    # mAcm2_ChGetLinkedCmpObject.restype = TypeDef.U32

    # mAcm2_ChEnableCmp = lib.Acm2_ChEnableCmp
    # mAcm2_ChEnableCmp.argtypes = [TypeDef.U32, TypeDef.U32]
    # mAcm2_ChEnableCmp.restype = TypeDef.U32

    # mAcm2_AxResetMPGOffset = lib.Acm2_AxResetMPGOffset
    # mAcm2_AxResetMPGOffset.argtypes = [TypeDef.U32]
    # mAcm2_AxResetMPGOffset.restype = TypeDef.U32

    # mAcm2_AxMovePTPBufferRel = lib.Acm2_AxMovePTPBufferRel
    # mAcm2_AxMovePTPBufferRel.argtypes = [TypeDef.U32, TypeDef.U16, TypeDef.PF64, TypeDef.PF64, TypeDef.PF64, TypeDef.PU16, TypeDef.U32]
    # mAcm2_AxMovePTPBufferRel.restype = TypeDef.U32

    # mAcm2_AxMovePTPBufferAbs = lib.Acm2_AxMovePTPBufferAbs
    # mAcm2_AxMovePTPBufferAbs.argtypes = [TypeDef.U32, TypeDef.U16, TypeDef.PF64, TypeDef.PF64, TypeDef.PF64, TypeDef.PU16, TypeDef.U32]
    # mAcm2_AxMovePTPBufferAbs.restype = TypeDef.U32

    # mAcm2_EnableCallBackFuncForOneEvent = lib.Acm2_EnableCallBackFuncForOneEvent
    # mAcm2_EnableCallBackFuncForOneEvent.argtypes = [TypeDef.U32, c_int, PADV_USER_CALLBACK_FUNC]
    # mAcm2_EnableCallBackFuncForOneEvent.restype = TypeDef.U32

    # mAcm2_GetErrors = lib.Acm2_GetErrors
    # mAcm2_GetErrors.argtypes = [TypeDef.U32, TypeDef.PVOID, TypeDef.PU32]
    # mAcm2_GetErrors.restype = TypeDef.U32

    # mAcm2_ResetErrorRecord = lib.Acm2_ResetErrorRecord
    # mAcm2_ResetErrorRecord.argtypes = [TypeDef.U32]
    # mAcm2_ResetErrorRecord.restype = TypeDef.U32

    # mAcm2_AxSetSpeedProfile = lib.Acm2_AxSetSpeedProfile
    # mAcm2_AxSetSpeedProfile.argtypes = [TypeDef.U32, SPEED_PROFILE_PRM]
    # mAcm2_AxSetSpeedProfile.restype = TypeDef.U32

    # mAcm2_AxMotionStart = lib.Acm2_AxMotionStart
    # mAcm2_AxMotionStart.argtypes = [TypeDef.U32, TypeDef.U32]
    # mAcm2_AxMotionStart.restype = TypeDef.U32

    # mAcm2_AxMotionStop = lib.Acm2_AxMotionStop
    # mAcm2_AxMotionStop.argtypes = [TypeDef.PU32, TypeDef.U32, c_uint, TypeDef.F64]
    # mAcm2_AxMotionStop.restype = TypeDef.U32

    # mAcm2_AxSetJogSpeedProfile = lib.Acm2_AxSetJogSpeedProfile
    # mAcm2_AxSetJogSpeedProfile.argtypes = [TypeDef.U32, JOG_SPEED_PROFILE_PRM]
    # mAcm2_AxSetJogSpeedProfile.restype = TypeDef.U32

    # mAcm2_AxSyncOut = lib.Acm2_AxSyncOut
    # mAcm2_AxSyncOut.argtypes = [TypeDef.U32]
    # mAcm2_AxSyncOut.restype = TypeDef.U32

    # mAcm2_AxPause = lib.Acm2_AxPause
    # mAcm2_AxPause.argtypes = [TypeDef.U32]
    # mAcm2_AxPause.restype = TypeDef.U32

    # mAcm2_AxResume = lib.Acm2_AxResume
    # mAcm2_AxResume.argtypes = [TypeDef.U32]
    # mAcm2_AxResume.restype = TypeDef.U32

    # mAcm2_GpGetPausePosition = lib.Acm2_GpGetPausePosition
    # mAcm2_GpGetPausePosition.argtypes = [TypeDef.U32, TypeDef.PF64]
    # mAcm2_GpGetPausePosition.restype = TypeDef.U32

    # mAcm2_GpCreate = lib.Acm2_GpCreate
    # mAcm2_GpCreate.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.U32]
    # mAcm2_GpCreate.restype = TypeDef.U32

    # mAcm2_GpGetAxesInGroup = lib.Acm2_GpGetAxesInGroup
    # mAcm2_GpGetAxesInGroup.argtypes = [TypeDef.U32, TypeDef.PU32, TypeDef.PU32]
    # mAcm2_GpGetAxesInGroup.restype = TypeDef.U32

    # mAcm2_GpUpdate = lib.Acm2_GpUpdate
    # mAcm2_GpUpdate.argtypes = [TypeDef.U32]
    # mAcm2_GpUpdate.restype = TypeDef.U32

    # mAcm2_GpSetSpeedProfile = lib.Acm2_GpSetSpeedProfile
    # mAcm2_GpSetSpeedProfile.argtypes = [TypeDef.U32, SPEED_PROFILE_PRM]
    # mAcm2_GpSetSpeedProfile.restype = TypeDef.U32

    # mAcm2_GpDelay = lib.Acm2_GpDelay
    # mAcm2_GpDelay.argtypes = [TypeDef.U32, TypeDef.U32]
    # mAcm2_GpDelay.restype = TypeDef.U32

    # mAcm2_GpPathDO = lib.Acm2_GpPathDO
    # mAcm2_GpPathDO.argtypes = [TypeDef.U32, PATH_DO_PRM]
    # mAcm2_GpPathDO.restype = TypeDef.U32

    # mAcm2_GpPathWaitDI = lib.Acm2_GpPathWaitDI
    # mAcm2_GpPathWaitDI.argtypes = [TypeDef.U32, PATH_DI_WAIT_PRM]
    # mAcm2_GpPathWaitDI.restype = TypeDef.U32

    # mAcm2_GpPathWaitForAxis = lib.Acm2_GpPathWaitForAxis
    # mAcm2_GpPathWaitForAxis.argtypes = [TypeDef.U32, PATH_AX_WAIT_PRM]
    # mAcm2_GpPathWaitForAxis.restype = TypeDef.U32

    # mAcm2_ChResetCmpData = lib.Acm2_ChResetCmpData
    # mAcm2_ChResetCmpData.argtypes = [TypeDef.U32]
    # mAcm2_ChResetCmpData.restype = TypeDef.U32

    # mAcm2_ChGetCmpBufferStatus = lib.Acm2_ChGetCmpBufferStatus
    # mAcm2_ChGetCmpBufferStatus.argtypes = [TypeDef.U32, POINTER(BUFFER_STATUS)]
    # mAcm2_ChGetCmpBufferStatus.restype = TypeDef.U32

    # mAcm2_ChChangeCmpIndex = lib.Acm2_ChChangeCmpIndex
    # mAcm2_ChChangeCmpIndex.argtypes = [TypeDef.U32, TypeDef.U32]
    # mAcm2_ChChangeCmpIndex.restype = TypeDef.U32

    # mAcm2_ChSetMultiCmpBufferData = lib.Acm2_ChSetMultiCmpBufferData
    # mAcm2_ChSetMultiCmpBufferData.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.U32, TypeDef.U32]
    # mAcm2_ChSetMultiCmpBufferData.restype = TypeDef.U32

    # mAcm2_ChSetMultiCmpTable = lib.Acm2_ChSetMultiCmpTable
    # mAcm2_ChSetMultiCmpTable.argtypes = [TypeDef.U32, ADV_OBJ_TYPE, TypeDef.U32]
    # mAcm2_ChSetMultiCmpTable.restype = TypeDef.U32

    # mAcm2_ChLinkPWMTable = lib.Acm2_ChLinkPWMTable
    # mAcm2_ChLinkPWMTable.argtypes = [TypeDef.U32, ADV_OBJ_TYPE, TypeDef.U32]
    # mAcm2_ChLinkPWMTable.restype = TypeDef.U32

    # mAcm2_ChGetLinkedPWMTable = lib.Acm2_ChGetLinkedPWMTable
    # mAcm2_ChGetLinkedPWMTable.argtypes = [TypeDef.U32, POINTER(ADV_OBJ_TYPE), TypeDef.PU32, TypeDef.PU32]
    # mAcm2_ChGetLinkedPWMTable.restype = TypeDef.U32

    # mAcm2_ChSetPWMTable = lib.Acm2_ChSetPWMTable
    # mAcm2_ChSetPWMTable.argtypes = [TypeDef.U32, TypeDef.PF64, TypeDef.PF64, TypeDef.U32]
    # mAcm2_ChSetPWMTable.restype = TypeDef.U32

    # mAcm2_ChLoadPWMTableFile = lib.Acm2_ChLoadPWMTableFile
    # mAcm2_ChLoadPWMTableFile.argtypes = [TypeDef.U32, TypeDef.PI8, TypeDef.PU32]
    # mAcm2_ChLoadPWMTableFile.restype = TypeDef.U32

    # mAcm2_ChGetPWMTableStatus = lib.Acm2_ChGetPWMTableStatus
    # mAcm2_ChGetPWMTableStatus.argtypes = [TypeDef.U32, POINTER(PWM_TABLE_STATUS)]
    # mAcm2_ChGetPWMTableStatus.restype = TypeDef.U32

    mAcm2_GetErrorMessage = lib.Acm2_GetErrorMessage
    mAcm2_GetErrorMessage.argtypes = [TypeDef.U32, TypeDef.PI8, TypeDef.U32]
    mAcm2_GetErrorMessage.restype = TypeDef.U32

    # mAcm2_DevSetOscChannelDataConfig = lib.Acm2_DevSetOscChannelDataConfig
    # mAcm2_DevSetOscChannelDataConfig.argtypes = [TypeDef.U32, TypeDef.U16, OSC_PROFILE_PRM]
    # mAcm2_DevSetOscChannelDataConfig.restype = TypeDef.U32

    # mAcm2_DevGetOscChannelDataConfig = lib.Acm2_DevGetOscChannelDataConfig
    # mAcm2_DevGetOscChannelDataConfig.argtypes = [TypeDef.U32, TypeDef.U16, POINTER(OSC_PROFILE_PRM)]
    # mAcm2_DevGetOscChannelDataConfig.restype = TypeDef.U32

    # mAcm2_DevOscChannelDataStart = lib.Acm2_DevOscChannelDataStart
    # mAcm2_DevOscChannelDataStart.argtypes = [TypeDef.U32]
    # mAcm2_DevOscChannelDataStart.restype = TypeDef.U32

    # mAcm2_DevOscChannelDataStop = lib.Acm2_DevOscChannelDataStop
    # mAcm2_DevOscChannelDataStop.argtypes = [TypeDef.U32]
    # mAcm2_DevOscChannelDataStop.restype = TypeDef.U32

    # mAcm2_DevGetOscChannelData = lib.Acm2_DevGetOscChannelData
    # mAcm2_DevGetOscChannelData.argtypes = [TypeDef.U32, TypeDef.U16, TypeDef.U32, TypeDef.PU32, TypeDef.PF64]
    # mAcm2_DevGetOscChannelData.restype = TypeDef.U32

    # mAcm2_DevGetOscChannelStatus = lib.Acm2_DevGetOscChannelStatus
    # mAcm2_DevGetOscChannelStatus.argtypes = [TypeDef.U32, TypeDef.PU32]
    # mAcm2_DevGetOscChannelStatus.restype = TypeDef.U32