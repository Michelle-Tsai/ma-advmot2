from AdvMotApi_CM2 import *
from MotionInfo import *
from utils import TypeDef
lib = CDLL('/usr/lib/libadvmot.so')

mAcm2_DevOpen = lib.Acm2_DevOpen
mAcm2_DevOpen.argtypes = [TypeDef.U32, POINTER(DEVICEINFO)]
mAcm2_DevOpen.restype = c_uint32

mAcm2_DevClose = lib.Acm2_DevClose
mAcm2_DevClose.argtypes = [POINTER(c_uint64)]
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
