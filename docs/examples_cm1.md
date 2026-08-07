# Common Motion API 1.0 (AdvCmnAPI_CM)
#### Acm_GetAvailableDevs

```cpp
U32 Acm_GetAvailableDevs(DEVLIST *DeviceList, U32 MaxEntries, PU32 OutEntries)
```

```python
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.MotionInfo import *
from AcmP.AdvMotPropID_CM2 import PropertyID
from AcmP.AdvMotErr_CM2 import ErrorCode

# Initialize
maxDevCnt = 10
maxDevList = (DEVLIST * maxDevCnt)()
maxDev = c_uint32(0)
errCde = c_uint32(ErrorCode.SUCCESS.value)
devHandle = c_void_p()

errCde = AdvMot.Acm_GetAvailableDevs(maxDevList, maxDevCnt, byref(maxDev))
for i in range(maxDev.value):
    print('{index:<5} 0x{devNum:x} {devName}'.format(index=i,
    devNum=maxDevList[i].dwDeviceNum, devName=maxDevList[i].szDeviceName))
# Open Device
errCde = AdvMot.Acm_DevOpen(devNum.value, byref(devHandle))
# Close Device
errCde = AdvMot.Acm_DevClose(byref(devHandle))
```

#### Acm_GetErrorMessage

```cpp
BOOL Acm_GetErrorMessage(U32 ErrorCode, PI8 lpszError,  U32 nMaxError)
```

#### Acm_DevOpen

```cpp
U32 Acm_DevOpen(U32 DeviceNumber, PHAND DeviceHandle)
```

#### Acm_DevReOpen

```cpp
U32 Acm_DevOpen(U32 DeviceNumber, PHAND DeviceHandle)
```

#### Acm_DevClose

```cpp
U32 Acm_DevClose(PHAND DeviceHandle)
```

#### Acm_GetLastError

```cpp
U32 Acm_GetLastError(HAND Handle)
```
#### Acm_GetProperty

```cpp
U32 Acm_GetProperty(HAND Handle, U32 PropertyID, PVOID Buffer, PU32 BufferLength)
```

#### Acm_SetProperty

```cpp
U32 Acm_SetProperty(HAND Handle, U32 PropertyID, PVOID Buffer, U32 BufferLength)
```

#### Acm_GetU32Property

```cpp
U32 Acm_GetU32Property(HAND Handle, U32 PropertyID, PU32 Value)
```

#### Acm_GetI32Property

```cpp
U32 Acm_GetI32Property(HAND Handle, U32 PropertyID, PI32 Value)
```

#### Acm_GetF64Property

```cpp
U32 Acm_GetF64Property(HAND Handle, U32 PropertyID, PF64 Value)
```

#### Acm_GetStringProperty

```cpp
U32 Acm_GetStringProperty(HAND Handle, U32 PropertyID, PU8 Value);
```

#### Acm_SetU32Property

```cpp
U32 Acm_SetU32Property(HAND Handle, U32 PropertyID, U32 Value)
```

#### Acm_SetI32Property

```cpp
U32 Acm_SetI32Property(HAND Handle, U32 PropertyID, I32 Value)
```

#### Acm_SetF64Property

```cpp
U32 Acm_SetF64Property(HAND Handle, U32 PropertyID, F64 Value)
```

#### Acm_SetStringProperty

```cpp
U32 Acm_SetStringProperty(HAND Handle, U32 PropertyID, PU8 Value)
```

#### Acm_GetMultiProperty

```cpp
U32 Acm_GetMultiProperty (HAND Handle, PU32 PropertyIDArray, PF64 ValueArray, U32 PropertyCnt, PU32 ErrorBuffer)
```

#### Acm_SetMultiU32Property

```cpp
U32 Acm_SetMultiU32Property(HAND Handle, PU32 PropertyIDArray, PU32 ValueArray, U32 PropertyCnt)
```

#### Acm_SetMultiI32Property

```cpp
U32 Acm_SetMultiI32Property(HAND Handle, PU32 PropertyIDArray, PI32 ValueArray, U32 PropertyCnt)
```

#### Acm_SetMultiF64Property

```cpp
U32 Acm_SetMultiF64Property(HAND Handle, PU32 PropertyIDArray, PF64 ValueArray, U32 PropertyCnt)
```

#### Acm_GetChannelProperty

```cpp
U32 Acm_GetChannelProperty(HAND Handle, U32 ChannelID, U32 PropertyID,  PF64 Value)
```

#### Acm_SetChannelProperty

```cpp
U32 Acm_SetChannelProperty(HAND Handle, U32 ChannelID, U32 PropertyID,  F64 Value)
```

#### Acm_GetMultiChannelProperty

```cpp
U32 Acm_GetMultiChannelProperty(HAND Handle, U32 PropertyID, U32 StartChID, U32 ChCount, PF64 ValueArray)
```

#### Acm_SetMultiChannelProperty

```cpp
U32 Acm_SetMultiChannelProperty(HAND Handle, U32 PropertyID, U32 StartChID, U32 ChCount, PF64 ValueArray)
```

#### Acm_DevEnableEvent

```cpp
U32 Acm_DevEnableEvent(HAND DeviceHandle, U32 DevEnableEvt)
```

#### Acm_DevCheckEvent

```cpp
U32 Acm_DevCheckEvent(HAND DeviceHandle, PU32 DevCheckEvt, U32 Millisecond);
```

#### Acm_EnableMotionEvent

```cpp
U32 Acm_EnableMotionEvent(HAND DeviceHandle, PU32 AxEnableEvtArray, PU32 GpEnableEvtArray, U32 AxArrayElements, U32 GpArrayElements)
```

#### Acm_CheckMotionEvent

```cpp
U32 Acm_CheckMotionEvent(HAND DeviceHandle, PU32 AxEvtStatusArray, PU32 GpEvtStatusArray, U32 AxArrayElements, U32 GpArrayElements, U32 Millisecond)
```

#### Acm_CancelCheckEvent

```cpp
U32 Acm_CancelCheckEvent(HAND ObjectHandle)
```

#### Acm_DevEnableEvent_All

```cpp
U32 Acm_DevEnableEvent_All(HAND DeviceHandle, PU32 DevEnableEvtArray, PU32 AxEnableEvtArray, PU32 GpEnableEvtArray, U32 AxArrayElements,U32 GpArrayElements)
```

#### Acm_DevCheckEvent_All

```cpp
U32 Acm_DevCheckEvent_All(HAND DeviceHandle, PU32 DevEvtStatusArray, PU32 AxEvtStatusArray, PU32 GpEvtStatusArray, U32 AxArrayElements, U32 GpArrayElements, U32 Millisecond);
```

#### Acm_DevLoadConfig

```cpp
U32 Acm_DevLoadConfig(HAND DeviceHandle, PI8 ConfigPath)
```

#### Acm_DevSlaveFwDownload

```cpp
U32 Acm_DevSlaveFwDownload(HAND DeviceHandle, U16 RingNo, U16 Position, PI8 FileName, PI8 FilePath, U32 Password)
```

#### Acm_DevWriteDPMData

```cpp
U32 Acm_DevWriteDPMData(HAND Handle, U16 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```

#### Acm_DevWriteMultiMailBox

```cpp
U32 Acm_DevWriteMultiMailBox(HAND Handle, U8 object_id, PU16 par_id, PU32 DataBuffer, PU32 ErrorBuffer, U32 ArrayElements)
```

#### Acm_WriteRingBuffer

```cpp
U32 Acm_WriteRingBuffer(HAND Handle, U32 cmd_id, U32 data_index, U32 data_cnt, PU32 dataBuffer)
```

#### Acm_ReadRingBuffer

```cpp
U32 Acm_ReadRingBuffer(HAND Handle, PU32 cmd_id, PU32 data_index, U32 data_cnt, PU32 dataBuffer)
```

#### Acm_DevGetComStatus

```cpp
U32 Acm_DevGetComStatus(HAND DeviceHandle, U16 RingNo, PU16 pStatus)
```

#### Acm_DevGetErrorTable

```cpp
U32 Acm_DevGetErrorTable(HAND DeviceHandle, U16 RingNo, PU32 ErrorTableArray, PU32 ArrayElements)
```

#### Acm_DevGetIOInfo

```cpp
U32 Acm_DevGetIOInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Slot, U8 DataType, PVOID pInfo)
```

#### Acm_CheckVersion

```cpp
U32 Acm_CheckVersion(HAND DeviceHandle, U32 VersionID, PU32 Result)
```

#### Acm_DevMultiTrigSetPWMTableOnTime

```cpp
U32 Acm_DevMultiTrigSetPWMTableOnTime(HAND DeviceHandle, PU32 TimeTableArray, U32 ArrayCount)
```

#### Acm_DevMultiTrigSetCmpDO

```cpp
U32 Acm_DevMultiTrigSetCmpDO(HAND DeviceHandle,U32 OFForON)
```

#### Acm_DevMultiTrigForceCmpOut

```cpp
U32 Acm_DevMultiTrigForceCmpOut(HAND DeviceHandle, U32 OFForON)
```

#### Acm_DevMutiTrigSetCmpDO

```cpp
U32 Acm_DevMutiTrigSetCmpDO(HAND DeviceHandle,U32 OFForON)
```

#### Acm_DevMutiTrigForceCmpOut

```cpp
U32 Acm_DevMutiTrigForceCmpOut(HAND DeviceHandle, U32 OFForON)
```

#### Acm_MasStartRing

```cpp
U32 Acm_MasStartRing(HAND DeviceHandle, U16 RingNo)
```

#### Acm_MasStopRing

```cpp
U32 Acm_MasStopRing(HAND DeviceHandle, U16 RingNo)
```

#### Acm_MasGetComStatus

```cpp
U32 Acm_MasGetComStatus(HAND DeviceHandle, U16 RingNo, PU16 pStatus)
```

#### Acm_MasGetComCyclicTime

```cpp
U32 Acm_MasGetComCyclicTime(HAND DeviceHandle, U16 RingNo, PF64 pTime)
```

#### Acm_MasGetDataCyclicTime

```cpp
U32 Acm_MasGetDataCyclicTime(HAND DeviceHandle, U16 RingNo, PF64 DataCyclicTime)
```

#### Acm_MasGetActiveTable

```cpp
U32 Acm_MasGetActiveTable(HAND DeviceHandle, U16 RingNo, PU32 ActiveTableArray, PU32 ArrayElements)
```

#### Acm_MasGetErrorTable

```cpp
U32 Acm_MasGetErrorTable(HAND DeviceHandle, U16 RingNo, PU32 ErrorTableArray, PU32 ArrayElements)
```

#### Acm_MasGetSlaveInfo

```cpp
U32 Acm_MasGetSlaveInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PU32 pInfo)
```

#### Acm_MasLogComStatus

```cpp
U32 Acm_MasLogComStatus(HAND DeviceHandle, U16 RingNo)
```

#### Acm_DevDownloadScanData

```cpp
U32 Acm_DevDownloadScanData(HAND DeviceHandle, PDEV_PRE_SCAN_DATA pScanDataArray, U32 ArrayLength)
```

#### Acm_DevMDaqConfig

```cpp
U32 Acm_DevMDaqConfig(HAND DeviceHandle, U16 ChannelID, U32 Period, U32 AxisNo, U32 Method, U32 ChanType, U32 Count)
```

#### Acm_DevMDaqStart

```cpp
U32 Acm_DevMDaqStart(HAND DeviceHandle)
```

#### Acm_DevMDaqStop

```cpp
U32 Acm_DevMDaqStop(HAND DeviceHandle)
```

#### Acm_DevMDaqReset

```cpp
U32 Acm_DevMDaqReset(HAND DeviceHandle, U16 ChannelID)
```

#### Acm_DevMDaqGetStatus

```cpp
U32 Acm_DevMDaqGetStatus(HAND DeviceHandle, U16 ChannelID, PU16 CurrentCnt, PU8 Status)
```

#### Acm_DevMDaqGetData

```cpp
U32 Acm_DevMDaqGetData(HAND DeviceHandle, U16 ChannelID, U16 StartIndex, U16 MaxCount, PI32 DataBuffer)
```

#### Acm_DevMDaqGetConfig

```cpp
U32 Acm_DevMDaqGetConfig(HAND DeviceHandle, U16 ChannelID, PU32 Period, PU32 AxisNo, PU32 Method, PU32 ChanType, PU32 Count)
```

#### Acm_RegCallBackFunc

```cpp
U32 Acm_RegCallBackFunc(HAND Handle, ADV_USER_CALLBACK_FUNC CallBackFun, PVOID UserParamter)
```

#### Acm_EnableEventCallBack

```cpp
U32 Acm_EnableEventCallBack(HAND DeviceHandle)
```

#### Acm_RegCallBackFuncForOneEvent

```cpp
U32 Acm_RegCallBackFuncForOneEvent(HAND Handle, U32 EvtChannel, ADV_USER_CALLBACK_FUNC CallBackFun, PVOID UserParamter)
```

#### Acm_DevEnableMotionEvent

```cpp
U32 Acm_DevEnableMotionEvent(HAND DeviceHandle, PU32 AxEnableEvtArray, PU32 GpEnableEvtArray, U32 AxArrayElements, U32 GpArrayElements)
```

#### Acm_ServoSetCom

```cpp
U32 Acm_ServoSetCom(U32 ComPortID, U32 Baudrate, U32 Timeout)
```

#### Acm_ServoGetAbsPosition

```cpp
U32 Acm_ServoGetAbsPosition(U32 ComPortID, U32 ServoType, U32 ServoID, U32 ServoAbsResolution, U32 ServoCmdResolution, U32 EncoderDir, PF64 AbsPosition)
```

#### Acm_AxSetCmdPosi_Pulse

```cpp
U32 Acm_AxSetCmdPosi_Pulse(HAND AxisHandle,F64 Position)
```

#### Acm_AxSpecialDiSetBit

```cpp
U32 Acm_AxSpecialDiSetBit(HAND AxisHandle,U16 DiType,U8 BitData)
```

#### Acm_DevEnableLTC

```cpp
U32 Acm_DevEnableLTC(HAND DeviceHandle, U16 LtcID, U16 EnableMode)
```

#### Acm_DevLTCSaftyDist

```cpp
U32 Acm_DevLTCSaftyDist(HAND DeviceHandle, U16 LtcID, F64 SaftyDist)
```

#### Acm_DevEnableCmp

```cpp
U32 Acm_DevEnableCmp(HAND DeviceHandle, U16 CmpID, U16 EnableMode)
```

#### Acm_DevLtcLinkCmp

```cpp
U32 Acm_DevLtcLinkCmp(HAND DeviceHandle, HAND AxisHandle, U16 EnableLink, U16 LtcID, U16 CmpID, F64 Offset)
```

#### Acm_DevSetCmp

```cpp
U32 Acm_DevSetCmp(HAND DeviceHandle, U16 CmpID, U32 CmpLogic, U32 CmpSrc, U32 CmpMethod, U32 DOMode, U32 DOWidth)
```

#### Acm_DevSetCmpDO

```cpp
U32 Acm_DevSetCmpDO(HAND DeviceHandle, U16 CmpID, U16 OnOff)
```

#### Acm_DevSetCmpData

```cpp
U32 Acm_DevSetCmpData(HAND DeviceHandle, U16 CmpID, F64 Data)
```

#### Acm_DevSetCmpAuto

```cpp
U32 Acm_DevSetCmpAuto(HAND DeviceHandle, U16 CmpID, F64 Start, F64 End, F64 Interval)
```

#### Acm_DevGetCmpData

```cpp
U32 Acm_DevGetCmpData(HAND DeviceHandle, U16 CmpID, PF64 Data)
```

#### Acm_DevEnableCmpFIFO

```cpp
U32 Acm_DevEnableCmpFIFO(HAND DeviceHandle, U16 CmpID, U16 Enable)
```

#### Acm_DevGetCmpFIFOCount

```cpp
U32 Acm_DevGetCmpFIFOCount(HAND DeviceHandle, U16 CmpID, PU16 DataCount)
```

#### Acm_DevGetCmpCounter

```cpp
U32 Acm_DevGetCmpCounter(HAND DeviceHandle, U16 CmpID, PU32 DataCount)
```

#### Acm_DevResetCmpFIFO

```cpp
U32 Acm_DevResetCmpFIFO(HAND DeviceHandle, U16 CmpID)
```

#### Acm_DevSetLTCInEdge

```cpp
U32 Acm_DevSetLTCInEdge(HAND DeviceHandle, U16 LtcID, U16 Edge)
```

#### Acm_DevGetLTCData

```cpp
U32 Acm_DevGetLTCData(HAND DeviceHandle, U16 LtcID, PF64 CommandPosition, PF64 Actualposition)
```

#### Acm_DevGetLTCFlag

```cpp
U32 Acm_DevGetLTCFlag(HAND DeviceHandle, U16 LtcID, PU8 LtcFlag)
```

#### Acm_DevResetLTC

```cpp
U32 Acm_DevResetLTC(HAND DeviceHandle, U16 LtcID)
```

#### Acm_DevGetCmpFlag

```cpp
U32 Acm_DevGetCmpFlag(HAND DeviceHandle, U16 CmpID, PU8 CmpFlag)
```

#### Acm_DevResetCmpFlag

```cpp
U32 Acm_DevResetCmpFlag(HAND DeviceHandle, U16 CmpID)
```

#### Acm_DevGetLtcLinkCmpStatus

```cpp
U32 Acm_DevGetLtcLinkCmpStatus(HAND DeviceHandle, U16 LtcID, PU16 LinkStatus)
```

#### Acm_DevResetCmpData

```cpp
U32 Acm_DevResetCmpData(HAND DeviceHandle, U16 CmpID)
```

#### Acm_DevGetLTCInEdge

```cpp
U32 Acm_DevGetLTCInEdge(HAND DeviceHandle, U16 LtcID, PU16 Edge)
```

#### Acm_DevGetLTCInPol

```cpp
U32 Acm_DevGetLTCInPol(HAND DeviceHandle, U16 LtcID, PU16 Logic)
```

#### Acm_DevGetLTCSaftyDist

```cpp
U32 Acm_DevGetLTCSaftyDist(HAND DeviceHandle, U16 LtcID, PF64 SaftyDist)
```

#### Acm_DevGetLTCInSource

```cpp
U32 Acm_DevGetLTCInSource(HAND DeviceHandle, U16 LtcID, PU16 Source)
```

#### Acm_DevSetLTCInSource

```cpp
U32 Acm_DevSetLTCInSource(HAND DeviceHandle, U16 LtcID, U16 Source)
```

#### Acm_DevGetCmp

```cpp
U32 Acm_DevGetCmp(HAND DeviceHandle, U16 CmpID, PU32 CmpLogic, PU32 CmpSrc, PU32 CmpMethod, PU32 DOMode, PU32 DOWidth)
```

#### Acm_DevReadLatchBuffer

```cpp
U32 Acm_DevReadLatchBuffer(HAND DeviceHandle, U16 LtcID, PF64 CommandPositionArray, PF64 ActualPositionArray, PU32 DataCnt)
```

#### Acm_DevGetLatchBufferStatus

```cpp
U32 Acm_DevGetLatchBufferStatus(HAND DeviceHandle, U16 LtcID, PU32 RemainCnt, PU32 SpaceCnt, PU32 LtcCounter)
```

#### Acm_DevResetLatchBuffer

```cpp
U32 Acm_DevResetLatchBuffer(HAND DeviceHandle, U16 LtcID)
```

#### Acm_DevSetLTCInAxisID

```cpp
U32 Acm_DevSetLTCInAxisID(HAND DeviceHandle, U16 LtcID, U32 AxisID)
```

#### Acm_DevGetLTCInAxisID

```cpp
U32 Acm_DevGetLTCInAxisID(HAND DeviceHandle, U16 LtcID, PU32 AxisID)
```

#### Acm_DevSetCmpAxisID

```cpp
U32 Acm_DevSetCmpAxisID(HAND DeviceHandle, U16 CmpID, U32 AxisID)
```

#### Acm_DevGetCmpAxisID

```cpp
U32 Acm_DevGetCmpAxisID(HAND DeviceHandle, U16 CmpID, PU32 AxisID)
```

#### Acm_GetDevNum

```cpp
U32 Acm_GetDevNum(U32 DevType,U32 BoardID,PU32 DeviceNumber)
```

#### Acm_DevSaveMapFile

```cpp
U32 Acm_DevSaveMapFile(HAND DeviceHandle, PI8 FilePath)
```

#### Acm_DevLoadMapFile

```cpp
U32 Acm_DevLoadMapFile(HAND DeviceHandle, PI8 FilePath)
```

#### Acm_DevUpLoadMapInfo

```cpp
U32 Acm_DevUpLoadMapInfo(HAND DeviceHandle, U16 MapType, PDEV_IO_MAP_INFO MapInfoArray, PU32 ArrayLength)
```

#### Acm_DevDownLoadMapInfo

```cpp
U32 Acm_DevDownLoadMapInfo(HAND DeviceHandle, U16 MapType, PDEV_IO_MAP_INFO MapInfoArray, U32 ArrayLength)
```

#### Acm_DevSetSlaveStates

```cpp
U32 Acm_DevSetSlaveStates(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 SlvState)
```

#### Acm_DevGetSlaveStates

```cpp
U32 Acm_DevGetSlaveStates(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PU16 SlvState)
```

#### Acm_DevGetSlaveTxPDO

```cpp
U32 Acm_DevGetSlaveTxPDO(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 StartOffset, U16 Length, PU8 DataArray)
```

#### Acm_DevGetSlaveRxPDO

```cpp
U32 Acm_DevGetSlaveRxPDO(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 StartOffset, U16 Length, PU8 DataArray)
```

#### Acm_DevWriteSDOComplete

```cpp
U32 Acm_DevWriteSDOComplete(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Index, U16 DataSize, PVOID pValue)
```

#### Acm_DevWriteSDOData

```cpp
U32 Acm_DevWriteSDOData(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Index, U16 SubIndex, U16 Type, U16 DataSize, PVOID pValue)
```

#### Acm_DevReadSDOData

```cpp
U32 Acm_DevReadSDOData(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Index, U16 SubIndex, U16 Type, U16 DataSize, PVOID pValue)
```

#### Acm_DevWriteRegData

```cpp
U32 Acm_DevWriteRegData(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Address, U16 Type, U16 DataSize, PVOID pValue)
```

#### Acm_DevReadRegData

```cpp
U32 Acm_DevReadRegData(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Address, U16 Type, U16 DataSize, PVOID pValue);
```

#### Acm_DevReadEmgMessage

```cpp
U32 Acm_DevReadEmgMessage(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 DataSize, PU8 EmgMessage);
```

#### Acm_DevReadSlvCommErrCnt

```cpp
U32 Acm_DevReadSlvCommErrCnt(HAND DeviceHandle, U16 RingNo, PU32 ErrCntArray, PU32 ArrayElements)
```

#### Acm_DaqLinkPDO

```cpp
U32 Acm_DaqLinkPDO(HAND DeviceHandle, PORT_TYPE Type, U16 Channel, U32 RingNo, U32 SlaveID, U32 EntryIndex, U32 EntrySubIndex);
```

#### Acm_AxMoveTorque

```cpp
U32 Acm_AxMoveTorque(HAND AxisHandle, F64 Distance, F64 Torque, F64 Velocity, F64 PressTime, U8 Mode)
```

#### Acm_AxGetActTorque

```cpp
U32 Acm_AxGetActTorque(HAND AxisHandle, PI32 Torque)
```

#### Acm_Ax2DCompensateInAx

```cpp
U32 Acm_Ax2DCompensateInAx(HAND AxisHandle, HAND RelAxisHandle, PF64 Coefficient, PF64 RelCoefficient, U32 ArrayElements)
```

#### Acm_Ax1DCompensateTable

```cpp
U32 Acm_Ax1DCompensateTable (HAND AxisHandle, F64 OriginPos, F64 Pitch, PF64 OffsetData, U32 OffsetElements, U32 Direction)
```

#### Acm_DevZAxisCompensateTable

```cpp
U32 Acm_DevZAxisCompensateTable(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, HAND ZAxisHandle, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataZ, U32 OffsetElementsX, U32 OffsetElementsY)
```

#### Acm_Dev2DCompensateTable

```cpp
U32 Acm_Dev2DCompensateTable(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataX, PF64 OffsetDataY, U32 OffsetElementsX, U32 OffsetElementsY)
```

#### Acm_DevZAxisCompensateTableEx

```cpp
U32 Acm_DevZAxisCompensateTableEx(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, HAND ZAxisHandle, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataZ, U32 OffsetElementsX, U32 OffsetElementsY, U32 Direction)
```

#### Acm_Dev2DCompensateTableEx

```cpp
U32 Acm_Dev2DCompensateTableEx(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataX, PF64 OffsetDataY, U32 OffsetElementsX, U32 OffsetElementsY, U32 Direction)
```

#### Acm_AxGetCompensatePosition

```cpp
U32 Acm_AxGetCompensatePosition(HAND AxisHandle, PF64 Position)
```

#### Acm_DevMultiTrigInitial

```cpp
U32 Acm_DevMultiTrigInitial(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Enable, U8 PWM, U8 LTC, U8 MPG)
```

#### Acm_EnableOneDevEventCallBack

```cpp
U32 Acm_EnableOneDevEventCallBack(HANDLE DeviceHandle, ULONG EventID)
```

#### Acm_AxGetRawData

```cpp
U32 Acm_AxGetRawData(HAND AxisHandle, U8 index, PF64 RawData)
```

#### Acm_AxSetRawData

```cpp
U32 Acm_AxSetRawData(HAND AxisHandle, U8 index, F64 RawData)
```

#### Acm_AxReturnPausePosition

```cpp
U32 Acm_AxReturnPausePosition(HAND AxHandle)
```

#### Acm_AxAddOnAx

```cpp
U32 Acm_AxAddOnAx(HAND AxisHandle, HAND MasAxisHandle)
```

#### Acm_AxAddRemove

```cpp
U32 Acm_AxAddRemove(HAND AxisHandle, HAND MasAxisHandle)
```

#### Acm_AxGetAddOnNum

```cpp
U32 Acm_AxGetAddOnNum(HAND AxisHandle, PI32 num)
```

#### Acm_AxSetCompensateDistance

```cpp
U32 Acm_AxSetCompensateDistance(HAND AxisHandle, F64 Distance)
```

#### Acm_AxGetCompensateDistance

```cpp
U32 Acm_AxGetCompensateDistance(HAND AxisHandle, PF64 Distance)
```

#### Acm_AxOpen

```cpp
U32 Acm_AxOpen(HAND DeviceHandle, U16 PhyAxis, PHAND AxisHandle)
```

```python
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.MotionInfo import *
from AcmP.AdvMotPropID_CM2 import PropertyID
from AcmP.AdvMotErr_CM2 import ErrorCode

# Initialize
maxDevCnt = 10
maxDevList = (DEVLIST * maxDevCnt)()
maxDev = c_uint32(0)
errCde = c_uint32(ErrorCode.SUCCESS.value)
devHandle = c_void_p()
axid = c_uint16(0)
axHand = c_void_p()

errCde = AdvMot.Acm_GetAvailableDevs(maxDevList, maxDevCnt, byref(maxDev))
for i in range(maxDev.value):
    print('{index:<5} 0x{devNum:x} {devName}'.format(index=i,
    devNum=maxDevList[i].dwDeviceNum, devName=maxDevList[i].szDeviceName))
# Open Device
errCde = AdvMot.Acm_DevOpen(devNum.value, byref(devHandle))
# Open Axis
errCde = AdvMot.Acm_AxOpen(devHandle, axid, byref(axHand))
# Close Axis
errCde = AdvMot.Acm_AxClose(axHand)
# Close Device
errCde = AdvMot.Acm_DevClose(byref(devHandle))
```

#### Acm_AxOpenbyID

```cpp
U32 Acm_AxOpenbyID(HAND DeviceHandle, U16 SlaveID, U8 SubID, PHAND AxisHandle)
```

#### Acm_AxClose

```cpp
U32 Acm_AxClose(PHAND AxisHandle)
```

#### Acm_AxSetSvOn

```cpp
U32 Acm_AxSetSvOn(HAND AxisHandle, U32 OnOff)
```

#### Acm_AxResetAlm

```cpp
U32 Acm_AxResetAlm(HAND AxisHandle, U32 OnOff)
```

#### Acm_AxMoveRel

```cpp
U32 Acm_AxMoveRel(HAND AxisHandle, F64 Distance)
```

#### Acm_AxMoveRel_T

```cpp
U32 Acm_AxMoveRel_T(HAND AxisHandle, F64 Distance, F64 Time, F64 Factor)
```

#### Acm_AxMoveRel_SD

```cpp
U32 Acm_AxMoveRel_SD(HAND AxisHandle, F64 Distance, F64 SDDistance)
```

#### Acm_AxMoveRel_EC

```cpp
U32 Acm_AxMoveRel_EC(HAND AxisHandle, F64 Position)
```

#### Acm_AxMoveAbs

```cpp
U32 Acm_AxMoveAbs(HAND AxisHandle, F64 Position)
```

#### Acm_AxMoveAbs_T

```cpp
U32 Acm_AxMoveAbs_T(HAND AxisHandle, F64 Position, F64 Time, F64 Factor)
```

#### Acm_AxMoveAbs_SD

```cpp
U32 Acm_AxMoveAbs_SD(HAND AxisHandle, F64 Position, F64 SDPosition)
```

#### Acm_AxMoveAbs_EC

```cpp
U32 Acm_AxMoveAbs_EC(HAND AxisHandle, F64 Position)
```

#### Acm_AxMoveVel

```cpp
U32 Acm_AxMoveVel(HAND AxisHandle, U16 Direction)
```

#### Acm_AxStopDec

```cpp
U32 Acm_AxStopDec(HAND AxisHandle)
```

#### Acm_AxStopDecEx

```cpp
U32 Acm_AxStopDecEx(HAND AxisHandle, F64 NewDec)
```

#### Acm_AxStopEmg

```cpp
U32 Acm_AxStopEmg(HAND AxisHandle)
```

#### Acm_AxMoveImpose

```cpp
U32 Acm_AxMoveImpose(HAND AxisHandle, F64 Position, F64 NewVel)
```

#### Acm_AxHomeEx

```cpp
U32 Acm_AxHomeEx(HAND AxisHandle, U32 DirMode)
```

#### Acm_AxHome

```cpp
U32 Acm_AxHome(HAND AxisHandle, U32 HomeMode, U32 DirMode)
```

#### Acm_AxMoveHome

```cpp
U32 Acm_AxMoveHome(HAND AxisHandle, U32 HomeMode, U32 Dir)
```

#### Acm_AxMoveGantryHome

```cpp
U32 Acm_AxMoveGantryHome(HAND AxisHandle, U32 HomeMode, U32 Dir)
```

#### Acm_AxChangeVel

```cpp
U32 Acm_AxChangeVel(HAND AxisHandle, F64 NewVel)
```

#### Acm_AxChangePos

```cpp
U32 Acm_AxChangePos(HAND AxisHandle, F64 NewPos)
```

#### Acm_AxChangeVelByRate

```cpp
U32 Acm_AxChangeVelByRate(HAND AxisHandle, U32 Rate)
```

#### Acm_AxChangeVelExByRate

```cpp
U32 Acm_AxChangeVelExByRate(HAND AxisHandle, U32 Rate, F64 NewAcc, F64 NewDec);
```

#### Acm_AxResetError

```cpp
U32 Acm_AxResetError(HAND AxisHandle)
```

#### Acm_AxGetState

```cpp
U32 Acm_AxGetState(HAND AxisHandle, PU16 State)
```

#### Acm_AxGetMotionIO

```cpp
U32 Acm_AxGetMotionIO(HAND AxisHandle, PU32 Status)
```

#### Acm_AxGetMotionStatus

```cpp
U32 Acm_AxGetMotionStatus(HAND AxisHandle, PU32 Status)
```

#### Acm_AxGetCmdPosition

```cpp
U32 Acm_AxGetCmdPosition(HAND AxisHandle, PF64 Position)
```

#### Acm_AxGetMachPosition

```cpp
U32 Acm_AxGetMachPosition(HAND AxisHandle, PF64 Position)
```

#### Acm_AxSetCmdPosition

```cpp
U32 Acm_AxSetCmdPosition(HAND AxisHandle, F64 Position)
```

#### Acm_AxGetActualPosition

```cpp
U32 Acm_AxGetActualPosition(HAND AxisHandle, PF64 Position)
```

#### Acm_AxSetActualPosition

```cpp
U32 Acm_AxSetActualPosition(HAND AxisHandle, F64 Position)
```

#### Acm_AxGetCmdVelocity

```cpp
U32 Acm_AxGetCmdVelocity(HAND AxisHandle, PF64 Velocity)
```

#### Acm_AxGetActVelocity

```cpp
U32 Acm_AxGetActVelocity(HAND AxisHandle, PF64 Velocity)
```

#### Acm_AxGetLagCounter

```cpp
U32 Acm_AxGetLagCounter(HAND AxisHandle, PF64 Position)
```

#### Acm_AxSetExtDrive

```cpp
U32 Acm_AxSetExtDrive(HAND AxisHandle, U16 ExtDrvMode)
```

#### Acm_AxDoSetBit

```cpp
U32 Acm_AxDoSetBit(HAND AxisHandle, U16	DoChannel, U8 BitData)
```

#### Acm_AxDiSetBit

```cpp
U32 Acm_AxDiSetBit(HAND AxisHandle, U16	DiChannel, U8 BitData)
```

#### Acm_AxDoGetBit

```cpp
U32 Acm_AxDoGetBit(HAND AxisHandle, U16	DoChannel, PU8 BitData)
```

#### Acm_AxDiGetBit

```cpp
U32 Acm_AxDiGetBit(HAND AxisHandle, U16	DiChannel, PU8 BitData)
```

#### Acm_AxDoSetByte

```cpp
U32 Acm_AxDoSetByte(HAND AxisHandle, U16 DoPort, U8 ByteData)
```

#### Acm_AxDoGetByte

```cpp
U32 Acm_AxDoGetByte(HAND AxisHandle, U16 DoPort, PU8 ByteData)
```

#### Acm_AxDiGetByte

```cpp
U32 Acm_AxDiGetByte(HAND AxisHandle, U16 DiPort, PU8 ByteData)
```

#### Acm_AxSimStartSuspendVel

```cpp
U32 Acm_AxSimStartSuspendVel(HAND AxisHandle, U16 DriDir)
```

#### Acm_AxSimStartSuspendRel

```cpp
U32 Acm_AxSimStartSuspendRel(HAND AxisHandle,F64 Distance)
```

#### Acm_AxSimStartSuspendAbs

```cpp
U32 Acm_AxSimStartSuspendAbs(HAND AxisHandle,F64 EndPoint)
```

#### Acm_AxSimStart

```cpp
U32 Acm_AxSimStart(HAND AxisHandle)
```

#### Acm_AxSimStop

```cpp
U32 Acm_AxSimStop(HAND AxisHandle)
```

#### Acm_AxGetLatchData

```cpp
U32 Acm_AxGetLatchData(HAND AxisHandle, U32 PositionNo, PF64 Position)
```

#### Acm_AxStartSoftLatch

```cpp
U32 Acm_AxStartSoftLatch(U32 AxisHandle)
```

#### Acm_AxResetLatch

```cpp
U32 Acm_AxResetLatch(HAND AxisHandle)
```

#### Acm_AxGetLatchFlag

```cpp
U32 Acm_AxGetLatchFlag(HAND AxisHandle, PU8 LatchFlag)
```

#### Acm_AxTriggerLatch

```cpp
U32 Acm_AxTriggerLatch(HAND AxisHandle)
```

#### Acm_AxReadLatchBuffer

```cpp
U32 Acm_AxReadLatchBuffer(HAND AxisHandle, PF64 LatchDataArray, PU32 DataCnt)
```

#### Acm_AxResetLatchBuffer

```cpp
U32 Acm_AxResetLatchBuffer(HAND AxisHandle)
```

#### Acm_AxGetLatchBufferStatus

```cpp
U32 Acm_AxGetLatchBufferStatus(HAND AxisHandle, PU32 RemainCnt, PU32 SpaceCnt)
```

#### Acm_AxGearInAx

```cpp
U32 Acm_AxGearInAx(HAND AxisHandle, HAND MasAxisHandle, I32 Numerator, I32 Denominator, U32 RefSrc, U32 Absolute)
```

#### Acm_AxTangentInGp

```cpp
U32 Acm_AxTangentInGp(HAND AxisHandle, HAND MasGroupHandle, PI16 StartVectorArray, U8 Working_plane, I16 Direction)
```

#### Acm_AxGantryInAx

```cpp
U32	Acm_AxGantryInAx(HAND AxisHandle, HAND MasAxisHandle, I16 RefMasterSrc, I16 direction)
```

#### Acm_AxPhaseAx

```cpp
U32 Acm_AxPhaseAx(HAND AxisHandle, F64 Acc, F64 Dec, F64 PhaseSpeed, F64 PhaseDist)
```

#### Acm_AxSetChannelCmpSetting

```cpp
U32 Acm_AxSetChannelCmpSetting(HAND AxisHandle, U16 ChannelID, U32 CmpSrc, U32 CmpMethod, U32 CmpPulseMode, U32 CmpPulseWidth)
```

#### Acm_AxGetChannelCmpSetting

```cpp
U32 Acm_AxGetChannelCmpSetting(HAND AxisHandle, U16 ChannelID, PU32 CmpSrc, PU32 CmpMethod, PU32 CmpPulseMode, PU32 CmpPulseWidth)
```

#### Acm_AxResetChannelCmp

```cpp
U32 Acm_AxResetChannelCmp(HAND AxisHandle, U16 ChannelID)
```

#### Acm_AxAddChannelCmpDatas

```cpp
U32 Acm_AxAddChannelCmpDatas(HAND AxisHandle, U16 ChannelID, PF64 TableArray, U32 ArrayCount)
```

#### Acm_AxGetChannelCmpData

```cpp
U32 Acm_AxGetChannelCmpData(HAND AxisHandle, U16 ChannelID, PF64 CmpData)
```

#### Acm_AxLoadChannelNextData

```cpp
U32 Acm_AxLoadChannelNextData(HAND AxisHandle, U16 ChannelID)
```

#### Acm_AxGetCmpbufferRemainCount

```cpp
U32 Acm_AxGetCmpbufferRemainCount(HAND AxisHandle, U16 ChannelID,PU32 DataCount)
```

#### Acm_AxSetCmpAuto

```cpp
U32 Acm_AxSetCmpAuto(HAND AxisHandle, F64 Start, F64 End, F64 Interval)
```

#### Acm_AxGetCmpData

```cpp
U32 Acm_AxGetCmpData(HAND AxisHandle, PF64 CmpPosition)
```

#### Acm_AxSetCmpData

```cpp
U32 Acm_AxSetCmpData(HAND AxisHandle, F64 CmpPosition)
```

#### Acm_AxSetCmpBufferData

```cpp
U32 Acm_AxSetCmpBufferData(HAND AxisHandle, PF64 TableArray, I32 ArrayCount)
```

#### Acm_AxResetCmpData

```cpp
U32 Acm_AxResetCmpData(HAND AxisHandle)
```

#### Acm_AxGetCmpBufferStatus

```cpp
U32 Acm_AxGetCmpBufferStatus(HAND AxisHandle, PU32 CurIndex, PU32 RemainCnt, PU32 SpaceCnt)
```

#### Acm_AxResetMPGOffset

```cpp
U32 Acm_AxResetMPGOffset(HAND AxisHandle)
```

#### Acm_AxMovePTPBufferRel

```cpp
U32 Acm_AxMovePTPBufferRel(HAND AxisHandle, U16 MotionMode, PF64 PositionArray, PF64 FLArray, PF64 FHArray, PU16 TSArray, U32 ArrayLength)
```

#### Acm_AxMovePTPBufferAbs

```cpp
U32 Acm_AxMovePTPBufferAbs(HAND AxisHandle, U16 MotionMode, PF64 PositionArray, PF64 FLArray, PF64 FHArray, PU16 TSArray, U32 ArrayLength)
```

#### Acm_AxEnableCompensation

```cpp
U32 Acm_AxEnableCompensation(HAND AxisHandle,F64 ZStartPos)
```

#### Acm_AxGetCompensationValue

```cpp
U32 Acm_AxGetCompensationValue(HAND AxisHandle, F64 XData, F64 YData, PF64 PCompensationValue)
```

#### Acm_AxSetCompenPara

```cpp
U32 Acm_AxSetCompenPara(HAND AxisHandle, HAND GroupHandle, U32 XScanDataCnt, U32 YScanDataCnt, U32 CompMode)
```

#### Acm_AxDIStartMoveAbs

```cpp
U32 Acm_AxDIStartMoveAbs(HAND AxisHandle, U16 DIChannel, F64 Position)
```

#### Acm_AxDIStartMoveRel

```cpp
U32 Acm_AxDIStartMoveRel(HAND AxisHandle, U16 DIChannel, F64 Distance)
```

#### Acm_AxDIStartMoveVel

```cpp
U32 Acm_AxDIStartMoveVel(HAND AxisHandle, U16 DIChannel, U16 Direction)
```

#### Acm_AxDisableDIStart

```cpp
U32 Acm_AxDisableDIStart(HAND AxisHandle)
```

#### Acm_AxSetPWMTableOnTime

```cpp
U32 Acm_AxSetPWMTableOnTime(HAND AxisHandle, PU32 TimeTableArray, I32 ArrayCount)
```

#### Acm_AxGetINxStopStatus

```cpp
U32 Acm_AxGetINxStopStatus(HAND AxisHandle,PU32 Stop_Flag)
```

#### Acm_AxResetINxStopStatus

```cpp
U32 Acm_AxResetINxStopStatus(HAND AxisHandle)
```

#### Acm_AxJog

```cpp
U32 Acm_AxJog(HAND AxisHandle,U16 Direction)
```

#### Acm_AxSetCmpDO

```cpp
U32 Acm_AxSetCmpDO(HAND AxisHandle,U32 OFForON)
```

#### Acm_AxDownloadTorqueTable

```cpp
U32 Acm_AxDownloadTorqueTable(HAND AxisHandle, PF64 PositionArray, PF64 TorqueArray, U32 ArrayElements)
```

#### Acm_AxLoadTorqueTableFile

```cpp
U32 Acm_AxLoadTorqueTableFile(HAND AxisHandle, PI8 FilePath, PU32 PointsCount)
```

#### Acm_AxResetPVTTable

```cpp
U32 Acm_AxResetPVTTable(HAND AxisHandle)
```

#### Acm_AxLoadPVTTable

```cpp
U32 Acm_AxLoadPVTTable(HAND AxisHandle, PF64 Position, PF64 Velocity, PF64 Time, U32 ArrayElements)
```

#### Acm_AxCalculatePVTTableContinuous

```cpp
U32 Acm_AxCalculatePVTTableContinuous(HAND AxisHandle, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, U32 ArrayElements, PF64 Time)
```

#### Acm_AxLoadPVTTableContinuous

```cpp
U32 Acm_AxLoadPVTTableContinuous(HAND AxisHandle, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, F64 TimeDelay, U32 ArrayElements)
```

#### Acm_AxStartPVT

```cpp
U32 Acm_AxStartPVT(HAND AxisHandle, U8 Repeat)
```

#### Acm_AxStartAllPVT

```cpp
U32 Acm_AxStartAllPVT(PHAND AxisHandle, U8 Repeat, U32 ArrayElements)
```

#### Acm_AxCheckPTBuffer

```cpp
U32 Acm_AxCheckPTBuffer(HAND AxisHandle, PU16 Freespace)
```

#### Acm_AxAddPTData

```cpp
U32 Acm_AxAddPTData(HAND AxisHandle, F64 Position, F64 Time)
```

#### Acm_AxStartPT

```cpp
U32 Acm_AxStartPT(HAND AxisHandle, U8 Repeat)
```

#### Acm_AxStartAllPT

```cpp
U32 Acm_AxStartAllPT(PHAND AxisHandle, U8 Repeat, U32 ArrayElements)
```

#### Acm_AxResetPTData

```cpp
U32 Acm_AxResetPTData(HAND AxisHandle)
```

#### Acm_AxAddPVAData

```cpp
U32 Acm_AxAddPVAData(HAND AxisHandle, F64 Position, PF64 VelArray, PF64 AccArray, PF64 DecArray, U32 ArrayElements)
```

#### Acm_GpOpen

```cpp
U32 Acm_GpOpen(HAND DevHandle,PHAND GpHandle,USHORT GpID)
```

#### Acm_GpAddAxis

```cpp
U32 Acm_GpAddAxis(PHAND GpHandle,HAND AxHandle)
```

#### Acm_GpRemAxis

```cpp
U32 Acm_GpRemAxis(HAND GroupHandle, HAND AxisHandle)
```

#### Acm_GpClose

```cpp
U32 Acm_GpClose(PHAND GroupHandle)
```

#### Acm_GpGetState

```cpp
U32 Acm_GpGetState(HAND GroupHandle, PU16 State)
```

#### Acm_GpResetError

```cpp
U32 Acm_GpResetError(HAND GroupHandle)
```

#### Acm_GpIpoMask

```cpp
U32 Acm_GpIpoMask(HAND GroupHandle, HAND AxHandle, U32 Mask)
```

#### Acm_GpMoveLinearRel

```cpp
U32 Acm_GpMoveLinearRel(HAND GroupHandle, PF64 DistanceArray, PU32 ArrayElements)
```

#### Acm_GpMoveLinearAbs

```cpp
U32 Acm_GpMoveLinearAbs(HAND GroupHandle, PF64 PositionArray, PU32 ArrayElements)
```

#### Acm_GpMoveDirectRel

```cpp
U32 Acm_GpMoveDirectRel(HAND GroupHandle, PF64 DistanceArray, PU32 ArrayElements)
```

#### Acm_GpMoveDirectAbs

```cpp
U32 Acm_GpMoveDirectAbs(HAND GroupHandle, PF64 PositionArray, PU32 ArrayElements)
```

#### Acm_GpMoveCircularRel

```cpp
U32 Acm_GpMoveCircularRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 ArrayElements, I16 Direction)
```

#### Acm_GpMoveCircularAbs

```cpp
U32 Acm_GpMoveCircularAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 ArrayElements, I16 Direction)
```

#### Acm_GpMoveCircularRel_3P

```cpp
U32 Acm_GpMoveCircularRel_3P(HAND GroupHandle, PF64	RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)

```

#### Acm_GpMoveCircularAbs_3P

```cpp
U32 Acm_GpMoveCircularAbs_3P(HAND GroupHandle, PF64	RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveCircularRel_Angle

```cpp
U32 Acm_GpMoveCircularRel_Angle(HAND GroupHandle, PF64 CenterArray, U16 Degree, PU32 ArrayElements, I16 Direction)

```

#### Acm_GpMoveCircularAbs_Angle

```cpp
U32 Acm_GpMoveCircularAbs_Angle(HAND GroupHandle, PF64 CenterArray, U16 Degree, PU32 ArrayElements, I16 Direction)
```

#### Acm_GpMoveArcRel_Angle

```cpp
U32 Acm_GpMoveArcRel_Angle(HAND GroupHandle, PF64 CenterArray, F64 Degree, PU32 ArrayElements, I16 Direction)
```

#### Acm_GpMoveArcAbs_Angle

```cpp
U32 Acm_GpMoveArcAbs_Angle(HAND GroupHandle, PF64 CenterArray, F64 Degree, PU32 ArrayElements, I16 Direction)
```

#### Acm_GpMove3DArcAbs

```cpp
U32 Acm_GpMove3DArcAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMove3DArcRel

```cpp
U32 Acm_GpMove3DArcRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)

```

#### Acm_GpMove3DArcAbs_V

```cpp
U32 Acm_GpMove3DArcAbs_V(HAND GroupHandle, PF64 CenterArray, PF64 NVectorArray, F64 Degree, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMove3DArcRel_V

```cpp
U32 Acm_GpMove3DArcRel_V(HAND GroupHandle, PF64 CenterArray, PF64 NVectorArray, F64 Degree, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMove3DArcAbs_3P

```cpp
U32 Acm_GpMove3DArcAbs_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, U16 cycCount)
```

#### Acm_GpMove3DArcRel_3P

```cpp
U32 Acm_GpMove3DArcRel_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, U16 cycCount)
```

#### Acm_GpMove3DArcAbs_3PAngle

```cpp
U32 Acm_GpMove3DArcAbs_3PAngle(HAND GroupHandle, PF64 RefPoint_1, PF64 RefPoint_2, PU32 pArrayElements, I16 Direction, F64 Degree)
```

#### Acm_GpMove3DArcRel_3PAngle

```cpp
U32 Acm_GpMove3DArcRel_3PAngle(HAND GroupHandle, PF64 RefPoint_1, PF64 RefPoint_2, PU32 pArrayElements, I16 Direction, F64 Degree)

```

#### Acm_GpMoveHelixAbs

```cpp
U32 Acm_GpMoveHelixAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveHelixRel

```cpp
U32 Acm_GpMoveHelixRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)

```

#### Acm_GpMoveHelixAbs_3P

```cpp
U32 Acm_GpMoveHelixAbs_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMove3DArcRel_3PAngle

```cpp
U32 Acm_GpMove3DArcRel_3PAngle(HAND GroupHandle, PF64 RefPoint_1, PF64 RefPoint_2, PU32 pArrayElements, I16 Direction, F64 Degree)
```

#### Acm_GpMoveHelixAbs

```cpp
U32 Acm_GpMoveHelixAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveHelixRel

```cpp
U32 Acm_GpMoveHelixRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveHelixAbs_3P

```cpp
U32 Acm_GpMoveHelixAbs_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveHelixRel_3P

```cpp
U32 Acm_GpMoveHelixRel_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveHelixRel_Angle

```cpp
U32 Acm_GpMoveHelixRel_Angle(HAND GroupHandle, PF64	CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveHelixAbs_Angle

```cpp
U32 Acm_GpMoveHelixAbs_Angle(HAND GroupHandle, PF64	CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveEllipticalRel

```cpp
U32 Acm_GpMoveEllipticalRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, F64 RatioSemiAxes)
```

#### Acm_GpMoveEllipticalAbs

```cpp
U32 Acm_GpMoveEllipticalAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, F64 RatioSemiAxes)
```

#### Acm_GpLoadPath

```cpp
U32 Acm_GpLoadPath(HAND GroupHandle, PI8 FilePath, PHAND PathHandle, PU32 pTotalCount)
```

#### Acm_GpUnloadPath

```cpp
U32 Acm_GpUnloadPath(HAND GroupHandle, PHAND PathHandle)
```

#### Acm_GpMovePath

```cpp
U32 Acm_GpMovePath(HAND GroupHandle, HAND PathHandle)
```

#### Acm_GpMoveAllPath

```cpp
U32 Acm_GpMoveAllPath(PHAND GroupHandle, U32 ArrayElements)
```

#### Acm_GpAddPath

```cpp
U32 Acm_GpAddPath(HAND GroupHandle, U16 MoveCmd, U16 MoveMode, F64 FH, F64 FL, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)
```

#### Acm_GpAddPath2

```cpp
U32 Acm_GpAddPath2(HAND GroupHandle, U16 MoveCmd, U16 MoveMode, F64 FH, F64 FL, F64 ACC, F64 DEC, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)
```

#### Acm_GpLookAheadPath

```cpp
U32 Acm_GpLookAheadPath(HAND GroupHandle, U16 BufferSize, PI8 OutputFile)
```

#### Acm_GpResetPath

```cpp
U32 Acm_GpResetPath (PHAND GroupHandle)
```

#### Acm_GpGetPathStatus

```cpp
U32 Acm_GpGetPathStatus(HAND GroupHandle, PU32 pCurIndex, PU32 pCurCmdFunc, PU32 pRemainCount, PU32 pFreeSpaceCount)
```

#### Acm_GpMoveSelPath

```cpp
U32 Acm_GpMoveSelPath(HAND GroupHandle, HAND PathHandle, U32 StartIndex, U32 EndIndex, U8 Repeat)
```

#### Acm_GpGetPathIndexStatus

```cpp
U32 Acm_GpGetPathIndexStatus(HAND GroupHandle, U32 Index, PU16 CmdFunc, PU16 MoveMode, PF64 FH, PF64 FL, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements);

```

#### Acm_GpAddBSplinePath

```cpp
U32 Acm_GpAddBSplinePath(HAND GroupHandle, F64 FH, F64 FL, F64 *CtrlP0List, F64 *CtrlP1List, U32 CtrlPCount, F64 *NodeList, U32 NodeCount, U32 Degree, U32 CutPointCount)
```

#### Acm_GpAddCSplinePath

```cpp
U32 Acm_GpAddCSplinePath(HAND GroupHandle, F64 FH, F64 FL, F64 *CtrlP0List, F64 *CtrlP1List, F64 *Tightness, U32 CtrlPCount, U32 CutPointCount)

```

#### Acm_GpResumeMotion

```cpp
U32 Acm_GpResumeMotion(HAND GroupHandle)
```

#### Acm_GpPauseMotion

```cpp
U32 Acm_GpPauseMotion(HAND GroupHandle)
```

#### Acm_GpStopDec

```cpp
U32 Acm_GpStopDec(HAND GroupHandle)
```

#### Acm_GpStopDecEx

```cpp
U32 Acm_GpStopDecEx(HAND GroupHandle, F64 NewDec)
```

#### Acm_GpStopEmg

```cpp
U32 Acm_GpStopEmg(HAND GroupHandle)
```

#### Acm_GpChangeVel

```cpp
U32 Acm_GpChangeVel(HAND GroupHandle, F64 NewVelocity)
```

#### Acm_GpChangeVelByRate

```cpp
U32 Acm_GpChangeVelByRate(HAND GroupHandle, U32 Rate)
```

#### Acm_GpGetCmdVel

```cpp
U32 Acm_GpGetCmdVel(HAND GroupHandle, PF64 CmdVel)
```

#### Acm_GpGetINxStopStatus

```cpp
U32 Acm_GpGetINxStopStatus(HAND GroupHandle,PU32 Stop_Flag)
```

#### Acm_GpResetINxStopStatus

```cpp
U32 Acm_GpResetINxStopStatus(HAND GroupHandle)
```

#### Acm_GpGetPausePosition

```cpp
U32 Acm_GpGetPausePosition(HAND GroupHandle, PF64 RefPausePosition)
```

#### Acm_GpSetRawData

```cpp
U32 Acm_GpSetRawData(HAND GroupHandle, U8 index, F64 RawData)
```

#### Acm_GpGetRawData

```cpp
U32 Acm_GpGetRawData(HAND GroupHandle, U8 index, PF64 RawData)
```

#### Acm_DaqDiGetByte

```cpp
U32 Acm_DaqDiGetByte(HAND DeviceHandle, U16 DiPort, PU8 ByteData)
```

#### Acm_DaqDiGetBit

```cpp
U32 Acm_DaqDiGetBit(HAND DeviceHandle, U16 DiChannel, PU8 BitData)
```

#### Acm_DaqDoSetByte

```cpp
U32 Acm_DaqDoSetByte(HAND DeviceHandle, U16 DoPort, U8	ByteData)
```

#### Acm_DaqDoSetBit

```cpp
U32 Acm_DaqDoSetBit(HAND DeviceHandle, U16 DoChannel, U8 BitData)
```

#### Acm_DaqDiSetBit

```cpp
U32 Acm_DaqDiSetBit(HAND DeviceHandle, U16 DiChannel, U8 BitData)
```

#### Acm_DaqDoGetByte

```cpp
U32 Acm_DaqDoGetByte(HAND DeviceHandle, U16 DoPort, PU8 ByteData)
```

#### Acm_DaqDoGetBit

```cpp
U32 Acm_DaqDoGetBit(HAND DeviceHandle, U16 DoChannel, PU8 BitData)
```

#### Acm_DaqDiGetBytes

```cpp
U32 Acm_DaqDiGetBytes(HAND DeviceHandle, U16 StartPort, U16 NumPort, PU8 ByteDataArray)
```

#### Acm_DaqDoSetBytes

```cpp
U32 Acm_DaqDoSetBytes(HAND DeviceHandle, U16 StartPort, U16 NumPort, PU8 ByteDataArray)
```

#### Acm_DaqDoGetBytes

```cpp
U32 Acm_DaqDoGetBytes(HAND DeviceHandle, U16 StartPort, U16 NumPort, PU8 ByteDataArray)
```

#### Acm_DaqDiGetByteEx

```cpp
U32 Acm_DaqDiGetByteEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 DiPort, PU8 ByteData)
```

#### Acm_DaqDoSetByteEx

```cpp
U32 Acm_DaqDoSetByteEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 DoPort, U8 ByteData)
```

#### Acm_DaqDoGetByteEx

```cpp
U32 Acm_DaqDoGetByteEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 DoPort, PU8 ByteData)
```

#### Acm_DaqDoGetBitEx

```cpp
U32 Acm_DaqDoGetBitEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 DoChannel, PU8 BitData)
```

#### Acm_DaqAiGetRawData

```cpp
U32 Acm_DaqAiGetRawData(HAND DeviceHandle, U16 AiChannel, PU16 AiData)
```

#### Acm_DaqAiGetEngData

```cpp
U32 Acm_DaqAiGetEngData(HAND DeviceHandle, U16 AiChannel, PF32 AiData)
```

#### Acm_DaqAiGetVoltData

```cpp
U32 Acm_DaqAiGetVoltData(HAND DeviceHandle, U16	AiChannel, PF32	AiData)
```

#### Acm_DaqAiGetCurrData

```cpp
U32 Acm_DaqAiGetCurrData(HAND DeviceHandle, U16	AiChannel, PF32	AiData)
```

#### Acm_DaqAiZeroCalibration

```cpp
U32 Acm_DaqAiZeroCalibration(HAND DeviceHandle, U16	AiChannel)
```

#### Acm_DaqAiSpanCalibration

```cpp
U32 Acm_DaqAiSpanCalibration(HAND DeviceHandle, U16	AiChannel)
```

#### Acm_DaqAiGetChannelStatus

```cpp
U32 Acm_DaqAiGetChannelStatus(HAND DeviceHandle, U16 AiChannel, PU32 ChanStatus)
```

#### Acm_DaqAoSetRawData

```cpp
U32 Acm_DaqAoSetRawData(HAND DeviceHandle, U16 AoChannel, U16 AoData)
```

#### Acm_DaqAoSetEngData

```cpp
U32 Acm_DaqAoSetEngData(HAND DeviceHandle, U16 AoChannel, F32 AoData)
```

#### Acm_DaqAoSetVoltData

```cpp
U32 Acm_DaqAoSetVoltData(HAND DeviceHandle, U16	AoChannel, F32 AoData)
```

#### Acm_DaqAoSetCurrData

```cpp
U32 Acm_DaqAoSetCurrData(HAND DeviceHandle, U16	AoChannel, F32 AoData)
```

#### Acm_DaqAoGetRawData

```cpp
U32 Acm_DaqAoGetRawData(HAND DeviceHandle, U16 AoChannel, PU16 AoData)
```

#### Acm_DaqAoGetEngData

```cpp
U32 Acm_DaqAoGetEngData(HAND DeviceHandle, U16 AoChannel, PF32 AoData)
```

#### Acm_DaqAoGetVoltData

```cpp
U32 Acm_DaqAoGetVoltData(HAND DeviceHandle, U16	AoChannel, PF32 AoData)
```

#### Acm_DaqAoGetCurrData

```cpp
U32 Acm_DaqAoGetCurrData(HAND DeviceHandle, U16	AoChannel, PF32 AoData)
```

#### Acm_DaqAoSetCaliType

```cpp
U32 Acm_DaqAoSetCaliType(HAND DeviceHandle, U16	AoChannel, U16 TrimType)
```

#### Acm_DaqAoSetCaliValue

```cpp
U32 Acm_DaqAoSetCaliValue(HAND DeviceHandle, U16 AoChannel, U16 CaliData)
```

#### Acm_DaqAoCaliDone

```cpp
U32 Acm_DaqAoCaliDone(HAND DeviceHandle, U16 AoChannel, bool done)
```

#### Acm_DaqAoCaliDefault

```cpp
U32 Acm_DaqAoCaliDefault(HAND DeviceHandle, U16	AoChannel)
```

#### Acm_DaqAoGetChannelStatus

```cpp
U32 Acm_DaqAoGetChannelStatus(HAND DeviceHandle, U16 AoChannel, PU32 ChanStatus)
```

#### Acm_DaqSetScaledProperty

```cpp
U32 Acm_DaqSetScaledProperty(HAND DeviceHandle, PORT_TYPE Type, U16 Channel, F32 UpperBound, F32 LowerBound, U16 Resolution, I16 TransType)
```

#### Acm_DaqAiGetRawDataEx

```cpp
U32 Acm_DaqAiGetRawDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AiChannel, PU16 AiData)
```

#### Acm_DaqAiGetEngDataEx

```cpp
U32 Acm_DaqAiGetEngDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AiChannel, PF32 AiData)
```

#### Acm_DaqAiGetVoltDataEx

```cpp
U32 Acm_DaqAiGetVoltDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AiChannel, PF32 AiData)
```

#### Acm_DaqAiGetCurrDataEx

```cpp
U32 Acm_DaqAiGetCurrDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AiChannel, PF32 AiData)
```

#### Acm_DaqAiGetChannelStatusEx

```cpp
U32 Acm_DaqAiGetChannelStatusEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AiChannel, PU32 ChanStatus)
```

#### Acm_DaqAoSetRawDataEx

```cpp
U32 Acm_DaqAoSetRawDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, U16 AoData)
```

#### Acm_DaqAoSetEngDataEx

```cpp
U32 Acm_DaqAoSetEngDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, F32 AoData)
```

#### Acm_DaqAoSetVoltDataEx

```cpp
U32 Acm_DaqAoSetVoltDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, F32 AoData)
```

#### Acm_DaqAoSetCurrDataEx

```cpp
U32 Acm_DaqAoSetCurrDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, F32 AoData)
```

#### Acm_DaqAoGetRawDataEx

```cpp
U32 Acm_DaqAoGetRawDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, PU16 AoData)
```

#### Acm_DaqAoGetEngDataEx

```cpp
U32 Acm_DaqAoGetEngDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, PF32 AoData)
```

#### Acm_DaqAoGetVoltDataEx

```cpp
U32 Acm_DaqAoGetVoltDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, PF32 AoData)
```

#### Acm_DaqAoGetCurrDataEx

```cpp
U32 Acm_DaqAoGetCurrDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, PF32 AoData)
```

#### Acm_DaqGetIOLinkStatus

```cpp
U32 Acm_DaqGetIOLinkStatus(HAND DeviceHandle, PU32 pStatus)
```

#### Acm_DaqCntTriggerCmp

```cpp
U32 Acm_DaqCntTriggerCmp(HAND DeviceHandle, U16 CntChannel)
```

#### Acm_DaqCntResetLatch

```cpp
U32 Acm_DaqCntResetLatch(HAND DeviceHandle, U16 CntChannel)
```

#### Acm_DaqCntResetCmp

```cpp
U32 Acm_DaqCntResetCmp(HAND DeviceHandle, U16 CntChannel)
```

#### Acm_DaqCntResetCnt

```cpp
U32 Acm_DaqCntResetCnt(HAND DeviceHandle, U16 CntChannel)
```

#### Acm_DaqCntGetCounterData

```cpp
U32 Acm_DaqCntGetCounterData(HAND DeviceHandle, U16 CntChannel, PF64 CounterData)
```

#### Acm_DaqCntSetCounterData

```cpp
U32 Acm_DaqCntSetCounterData(HAND DeviceHandle, U16 CntChannel, F64 CounterData)
```

#### Acm_DaqCntGetCounterFrequency

```cpp
U32 Acm_DaqCntGetCounterFrequency(HAND DeviceHandle, U16 CntChannel, PF64 Frequency)
```

#### Acm_DaqCntGetExtDriveData

```cpp
U32 Acm_DaqCntGetExtDriveData(HAND DeviceHandle, U16 CntChannel, PF64 CounterData)
```

#### Acm_DaqCntSetExtDriveData

```cpp
U32 Acm_DaqCntSetExtDriveData(HAND DeviceHandle, U16 CntChannel, F64 CounterData)
```

#### Acm_DaqCntGetLatchData

```cpp
U32 Acm_DaqCntGetLatchData(HAND DeviceHandle, U16 CntChannel, PF64 LatchData)
```

#### Acm_DaqCntGetCmpData

```cpp
U32 Acm_DaqCntGetCmpData(HAND DeviceHandle, U16 CntChannel, PF64 CmpData)
```

#### Acm_DaqCntSetCmpData

```cpp
U32 Acm_DaqCntSetCmpData(HAND DeviceHandle, U16 CntChannel, F64 CmpData)
```

#### Acm_DaqCntSetCmpTable

```cpp
U32 Acm_DaqCntSetCmpTable(HAND DeviceHandle, U16 CntChannel, PF64 TableArray, I32 ArrayCount)
```

#### Acm_DaqCntSetCmpAuto

```cpp
U32 Acm_DaqCntSetCmpAuto(HAND DeviceHandle, U16 CntChannel, F64 Start, F64 End, F64 Interval)
```

#### Acm_DaqCntGetLatchBufferStatus

```cpp
U32 Acm_DaqCntGetLatchBufferStatus(HAND DeviceHandle, U16 CntChannel, PU32 RemainCnt, PU32 SpaceCnt)
```

#### Acm_DaqCntReadLatchBuffer

```cpp
U32 Acm_DaqCntReadLatchBuffer(HAND DeviceHandle, U16 CntChannel, PF64 LatchDataArray, PU32 DataCnt)
```

#### Acm_DaqCntTriggerCmpEx

```cpp
U32 Acm_DaqCntTriggerCmpEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel)
```

#### Acm_DaqCntTriggerLatchEx

```cpp
U32 Acm_DaqCntTriggerLatchEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel)
```

#### Acm_DaqCntResetLatchEx

```cpp
U32 Acm_DaqCntResetLatchEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel)
```

#### Acm_DaqCntResetCmpEx

```cpp
U32 Acm_DaqCntResetCmpEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel)
```

#### Acm_DaqCntResetCntEx

```cpp
U32 Acm_DaqCntResetCntEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel)
```

#### Acm_DaqCntGetCounterDataEx

```cpp
U32 Acm_DaqCntGetCounterDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 CounterData)
```

#### Acm_DaqCntSetCounterDataEx

```cpp
U32 Acm_DaqCntSetCounterDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, F64 CounterData)
```

#### Acm_DaqCntGetCounterFrequencyEx

```cpp
U32 Acm_DaqCntGetCounterFrequencyEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 Frequency)
```

#### Acm_DaqCntGetExtDriveDataEx

```cpp
U32 Acm_DaqCntGetExtDriveDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 CounterData)
```

#### Acm_DaqCntSetExtDriveDataEx

```cpp
U32 Acm_DaqCntSetExtDriveDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, F64 CounterData)
```

#### Acm_DaqCntGetLatchDataEx

```cpp
U32 Acm_DaqCntGetLatchDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 LatchData)
```

#### Acm_DaqCntGetCmpDataEx

```cpp
U32 Acm_DaqCntGetCmpDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 CmpData)
```

#### Acm_DaqCntSetCmpDataEx

```cpp
U32 Acm_DaqCntSetCmpDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, F64 CmpData)
```

#### Acm_DaqCntSetCmpTableEx

```cpp
U32 Acm_DaqCntSetCmpTableEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 TableArray, I32 ArrayCount)
```

#### Acm_DaqCntSetCmpAutoEx

```cpp
U32 Acm_DaqCntSetCmpAutoEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, F64 Start, F64 End, F64 Interval)
```

#### Acm_DaqCntGetLatchBufferStatusEx

```cpp
U32 Acm_DaqCntGetLatchBufferStatusEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PU32 RemainCnt, PU32 SpaceCnt)
```

#### Acm_DaqCntReadLatchBufferEx

```cpp
U32 Acm_DaqCntReadLatchBufferEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 LatchDataArray, PU32 DataCnt)
```

#### Acm_AxPWMOut

```cpp
U32 Acm_AxPWMOut(HAND AxisHandle,U32 OFForON,U32 PulseCount)
```

#### Acm_AxGetPWMOutState

```cpp
U32 Acm_AxGetPWMOutState(HAND AxisHandle,PU32 OFForON)
```

#### Acm_DevECATOpen

```cpp
U32 Acm_DevECATOpen(U32 DeviceNumber, U16 Ring0SlaveCount, U16 Ring1SlaveCount, U16 Timeout, PHAND DeviceHandle)
```

#### Acm_DevReadMailBox

```cpp
U32 Acm_DevReadMailBox(HAND Handle, U16 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```

#### Acm_DevReadMultiMailBox

```cpp
U32 Acm_DevReadMultiMailBox(HAND Handle, U8 object_id, PU16 par_id, PU32 DataBuffer, PU32 ErrorBuffer, U32 ArrayElements)
```

#### Acm_DevWriteMailBox

```cpp
U32 Acm_DevWriteMailBox(HAND Handle, U16 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```

#### Acm_LoadENI

```cpp
U32 Acm_LoadENI(HAND DeviceHandle, PI8 FilePath)
```

#### Acm_DevGetMasInfo

```cpp
U32 Acm_DevGetMasInfo(HAND DeviceHandle, PVOID pMasInfo, PU16 SlaveIPArray, PU32 SlvCnt)
```

#### Acm_DevGetMasStates

```cpp
U32 Acm_DevGetMasStates(HAND DeviceHandle, U16 RingNo, PU16 SlvCounters, PU16 SlvStates)
```

#### Acm_DevGetSlaveInfo

```cpp
U32 Acm_DevGetSlaveInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PVOID pInfo)
```

#### Acm_DevGetModuleInfo

```cpp
U32 Acm_DevGetModuleInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PU32 ModIDArray, PU32 ModCnt)
```

#### Acm_DevGetSlaveDataCnt

```cpp
U32 Acm_DevGetSlaveDataCnt(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U8 DataType, PU32 DataCnt)
```

#### Acm_DevGetSlaveFwVersion

```cpp
U32 Acm_DevGetSlaveFwVersion(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, OUT PI8 VersionInfo)
```

#### Acm_DevSetSlaveID

```cpp
U32 Acm_DevSetSlaveID(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 SlaveNewIP)
```
