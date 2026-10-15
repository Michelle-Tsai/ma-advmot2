# Advantech AcmP SDK
This documentation is for Advantech python SDK - AcmP

* You can find SDK at  [pypi.org](https://pypi.org/project/AcmP)
* You can find source code at  [Github](https://github.com/Michelle-Tsai/ma-advmot2)
* For support, please mail to  [Advantech](mailto:info@advantech.com)

## Available Devices

* [Advantech PCI-1245](https://www.advantech.com/zh-tw/products/e37baca6-8e5d-40f4-83c6-6bf379307dcf/pci-1245/mod_f9cb4a51-0b3b-46c4-a847-edaeafb279eb)
* [Advantech PCI-1285](https://www.advantech.com/zh-tw/products/e37baca6-8e5d-40f4-83c6-6bf379307dcf/pci-1285/mod_28c57210-33f3-4118-b4c4-79e3c4df0168)
* [Advantech PCI-1203](https://www.advantech.com/zh-tw/products/7d3c9775-8c30-4f65-83ec-755bee93b1d4/pci-1203/mod_8a5fd662-913c-4bb4-b7d4-a01cb12edcfb)
* [Advantech PCIE-1245](https://www.advantech.com/zh-tw/products/e37baca6-8e5d-40f4-83c6-6bf379307dcf/pcie-1245/mod_212c4df1-455d-4153-8293-e0a216690702)
* Advantech PCIE-1203M
* AMC Core

## Search the documentation
> ****
    For security reasons, Chromium-based browsers strictly prohibit local HTML files (file:///) from reading adjacent JSON files.

* We recommend hosting the files on any static web server (Including [VS Code - Live Preview Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server))

---

## Installation
This SDK supports Python version 3.10 or later

```shell
$ pip install AcmP
```

### How to use?
> **Warning**
    Due to our driver running with **admin/root authentication**, it's important to execute the project with admin/root privileges.

    Before using this package, please ensure the following items are already installed

* **Windows**
    * Shared driver: `ADVMOT.dll`
        * For PCI-1245: `PCI1245.sys`, `PCI1245.dll`
        * For PCI-1285: `PCI1285.sys`, `PCI1285.dll`
        * For PCI-1203: `PCI1203.sys`, `PCI1203.dll`
        * For PCIE-1203M: `PCIE1203Ms.sys`, `PCIE1203M.dll`
        * For PCIE-1245: `PCIE1245s.sys`, `PCIE1245.dll`
        * For AMC Core: `AMC_Core.dll`
    !!! tips
        You can check the installation using the following commands.
        ```powershell
        ls C:\Windows\ -Recurse -Filter *ADVMOT* -ErrorAction SilentlyContinue
        ls C:\Windows\ -Recurse -Filter *PCIE1203* -ErrorAction SilentlyContinue
        ls C:\Windows\ -Recurse -Filter *PCI1203* -ErrorAction SilentlyContinue
        ls C:\Windows\ -Recurse -Filter *PCI1245* -ErrorAction SilentlyContinue
        ls C:\Windows\ -Recurse -Filter *PCI1285* -ErrorAction SilentlyContinue
        ```

* **Linux**
    * Shared driver: `libadvmot.so`
        * For PCIE-1203M: `pcie1203m.ko`, `libpcie1203.so`
        * For PCIE-1245: `pcie1245.ko`, `libpcie1245.so`
    !!! tips
        You can check the installation using the following commands.
        ```shell
        $ lsmod | grep PCI
        $ ls /lib | grep adv
        $ ls /lib | grep pcie
        ```

---

## Common Motion API 1.0 (AdvCmnAPI_CM)
##### Acm_GetAvailableDevs

```cpp
U32 Acm_GetAvailableDevs(DEVLIST *DeviceList, U32 MaxEntries, PU32 OutEntries)
```

```python
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID
from AcmP.AdvMotErr_CM2 import ErrorCode

## Initialize
maxDevCnt = 10
maxDevList = (DEVLIST * maxDevCnt)()
maxDev = c_uint32(0)
errCde = c_uint32(ErrorCode.SUCCESS.value)
devHandle = c_void_p()

errCde = AdvMot.Acm_GetAvailableDevs(maxDevList, maxDevCnt, byref(maxDev))
for i in range(maxDev.value):
    print('{index:<5} 0x{devNum:x} {devName}'.format(index=i,
    devNum=maxDevList[i].dwDeviceNum, devName=maxDevList[i].szDeviceName))
## Open Device
errCde = AdvMot.Acm_DevOpen(devNum.value, byref(devHandle))
## Close Device
errCde = AdvMot.Acm_DevClose(byref(devHandle))
```

##### Acm_GetErrorMessage

```cpp
BOOL Acm_GetErrorMessage(U32 ErrorCode, PI8 lpszError,  U32 nMaxError)
```

##### Acm_GetNewErrorMessage
```cpp
U32 Acm_GetNewErrorMessage(U32 ErrorCode2, PI8 lpszError, U32 nMaxError)
```

##### Acm_DevOpen

```cpp
U32 Acm_DevOpen(U32 DeviceNumber, PHAND DeviceHandle)
```

##### Acm_DevECATOpen
```cpp
U32 Acm_DevECATOpen(U32 DeviceNumber, U16 Ring0SlaveCount, U16 Ring1SlaveCount, U16 Timeout, PHAND DeviceHandle)
```

##### Acm_DevReOpen

```cpp
U32 Acm_DevOpen(U32 DeviceNumber, PHAND DeviceHandle)
```

##### Acm_DevClose

```cpp
U32 Acm_DevClose(PHAND DeviceHandle)
```

##### Acm_GetLastError

```cpp
U32 Acm_GetLastError(HAND Handle)
```
##### Acm_GetProperty

```cpp
U32 Acm_GetProperty(HAND Handle, U32 PropertyID, PVOID Buffer, PU32 BufferLength)
```

##### Acm_SetProperty

```cpp
U32 Acm_SetProperty(HAND Handle, U32 PropertyID, PVOID Buffer, U32 BufferLength)
```

##### Acm_GetU32Property

```cpp
U32 Acm_GetU32Property(HAND Handle, U32 PropertyID, PU32 Value)
```

##### Acm_GetI32Property

```cpp
U32 Acm_GetI32Property(HAND Handle, U32 PropertyID, PI32 Value)
```

##### Acm_GetF64Property

```cpp
U32 Acm_GetF64Property(HAND Handle, U32 PropertyID, PF64 Value)
```

##### Acm_GetStringProperty

```cpp
U32 Acm_GetStringProperty(HAND Handle, U32 PropertyID, PU8 Value);
```

##### Acm_SetU32Property

```cpp
U32 Acm_SetU32Property(HAND Handle, U32 PropertyID, U32 Value)
```

##### Acm_SetI32Property

```cpp
U32 Acm_SetI32Property(HAND Handle, U32 PropertyID, I32 Value)
```

##### Acm_SetF64Property

```cpp
U32 Acm_SetF64Property(HAND Handle, U32 PropertyID, F64 Value)
```

##### Acm_SetStringProperty

```cpp
U32 Acm_SetStringProperty(HAND Handle, U32 PropertyID, PU8 Value)
```

##### Acm_GetMultiProperty

```cpp
U32 Acm_GetMultiProperty (HAND Handle, PU32 PropertyIDArray, PF64 ValueArray, U32 PropertyCnt, PU32 ErrorBuffer)
```

##### Acm_SetMultiU32Property

```cpp
U32 Acm_SetMultiU32Property(HAND Handle, PU32 PropertyIDArray, PU32 ValueArray, U32 PropertyCnt)
```

##### Acm_SetMultiI32Property

```cpp
U32 Acm_SetMultiI32Property(HAND Handle, PU32 PropertyIDArray, PI32 ValueArray, U32 PropertyCnt)
```

##### Acm_SetMultiF64Property

```cpp
U32 Acm_SetMultiF64Property(HAND Handle, PU32 PropertyIDArray, PF64 ValueArray, U32 PropertyCnt)
```

##### Acm_GetChannelProperty

```cpp
U32 Acm_GetChannelProperty(HAND Handle, U32 ChannelID, U32 PropertyID,  PF64 Value)
```

##### Acm_SetChannelProperty

```cpp
U32 Acm_SetChannelProperty(HAND Handle, U32 ChannelID, U32 PropertyID,  F64 Value)
```

##### Acm_GetMultiChannelProperty

```cpp
U32 Acm_GetMultiChannelProperty(HAND Handle, U32 PropertyID, U32 StartChID, U32 ChCount, PF64 ValueArray)
```

##### Acm_SetMultiChannelProperty

```cpp
U32 Acm_SetMultiChannelProperty(HAND Handle, U32 PropertyID, U32 StartChID, U32 ChCount, PF64 ValueArray)
```

##### Acm_DevEnableEvent

```cpp
U32 Acm_DevEnableEvent(HAND DeviceHandle, U32 DevEnableEvt)
```

##### Acm_DevCheckEvent

```cpp
U32 Acm_DevCheckEvent(HAND DeviceHandle, PU32 DevCheckEvt, U32 Millisecond);
```

##### Acm_EnableMotionEvent

```cpp
U32 Acm_EnableMotionEvent(HAND DeviceHandle, PU32 AxEnableEvtArray, PU32 GpEnableEvtArray, U32 AxArrayElements, U32 GpArrayElements)
```

##### Acm_CheckMotionEvent

```cpp
U32 Acm_CheckMotionEvent(HAND DeviceHandle, PU32 AxEvtStatusArray, PU32 GpEvtStatusArray, U32 AxArrayElements, U32 GpArrayElements, U32 Millisecond)
```

##### Acm_CancelCheckEvent

```cpp
U32 Acm_CancelCheckEvent(HAND ObjectHandle)
```

##### Acm_DevEnableEvent_All

```cpp
U32 Acm_DevEnableEvent_All(HAND DeviceHandle, PU32 DevEnableEvtArray, PU32 AxEnableEvtArray, PU32 GpEnableEvtArray, U32 AxArrayElements,U32 GpArrayElements)
```

##### Acm_DevCheckEvent_All

```cpp
U32 Acm_DevCheckEvent_All(HAND DeviceHandle, PU32 DevEvtStatusArray, PU32 AxEvtStatusArray, PU32 GpEvtStatusArray, U32 AxArrayElements, U32 GpArrayElements, U32 Millisecond);
```

##### Acm_DevLoadConfig

```cpp
U32 Acm_DevLoadConfig(HAND DeviceHandle, PI8 ConfigPath)
```

##### Acm_DevSlaveFwDownload

```cpp
U32 Acm_DevSlaveFwDownload(HAND DeviceHandle, U16 RingNo, U16 Position, PI8 FileName, PI8 FilePath, U32 Password)
```

##### Acm_DevDownloadCAMTable
```cpp
U32 Acm_DevDownloadCAMTable (HAND DeviceHandle, U32 CamTableID, PF64 pMasterArray, PF64 pSlaveArray, PF64 pPointRangeArray, PF64 pPointSlopeArray, U32 ArrayElements)
```

##### Acm_DevConfigCAMTable
```cpp
U32 Acm_DevConfigCAMTable(HAND DeviceHandle, U32 CamTableID, U32 Periodic, U32 MasterAbsolute, U32 SlaveAbsolute)
```

##### Acm_DevReadMailBox

```cpp
U32 Acm_DevReadMailBox(HAND Handle, U16 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```

##### Acm_DevReadMultiMailBox

```cpp
U32 Acm_DevReadMultiMailBox(HAND Handle, U8 object_id, PU16 par_id, PU32 DataBuffer, PU32 ErrorBuffer, U32 ArrayElements)
```

##### Acm_DevWriteMailBox

```cpp
U32 Acm_DevWriteMailBox(HAND Handle, U16 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```

##### Acm_DevWriteDPMData

```cpp
U32 Acm_DevWriteDPMData(HAND Handle, U16 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```

##### Acm_DevWriteMultiMailBox

```cpp
U32 Acm_DevWriteMultiMailBox(HAND Handle, U8 object_id, PU16 par_id, PU32 DataBuffer, PU32 ErrorBuffer, U32 ArrayElements)
```

##### Acm_WriteRingBuffer

```cpp
U32 Acm_WriteRingBuffer(HAND Handle, U32 cmd_id, U32 data_index, U32 data_cnt, PU32 dataBuffer)
```

##### Acm_ReadRingBuffer

```cpp
U32 Acm_ReadRingBuffer(HAND Handle, PU32 cmd_id, PU32 data_index, U32 data_cnt, PU32 dataBuffer)
```

##### Acm_LoadENI

```cpp
U32 Acm_LoadENI(HAND DeviceHandle, PI8 FilePath)
```

##### Acm_DevConnect
```cpp
U32 Acm_DevConnect(HAND DeviceHandle, U16 RingNo)
```

##### Acm_DevDisConnect
```cpp
U32 Acm_DevDisConnect(HAND DeviceHandle, U16 RingNo)
```

##### Acm_DevGetComStatus

```cpp
U32 Acm_DevGetComStatus(HAND DeviceHandle, U16 RingNo, PU16 pStatus)
```

##### Acm_DevGetErrorTable

```cpp
U32 Acm_DevGetErrorTable(HAND DeviceHandle, U16 RingNo, PU32 ErrorTableArray, PU32 ArrayElements)
```

##### Acm_DevGetMasInfo

```cpp
U32 Acm_DevGetMasInfo(HAND DeviceHandle, PVOID pMasInfo, PU16 SlaveIPArray, PU32 SlvCnt)
```

##### Acm_DevGetMasStates

```cpp
U32 Acm_DevGetMasStates(HAND DeviceHandle, U16 RingNo, PU16 SlvCounters, PU16 SlvStates)
```

##### Acm_DevGetSlaveInfo

```cpp
U32 Acm_DevGetSlaveInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PVOID pInfo)
```

##### Acm_DevGetModuleInfo

```cpp
U32 Acm_DevGetModuleInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PU32 ModIDArray, PU32 ModCnt)
```

##### Acm_DevGetIOInfo

```cpp
U32 Acm_DevGetIOInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Slot, U8 DataType, PVOID pInfo)
```

##### Acm_DevGetSlaveDataCnt

```cpp
U32 Acm_DevGetSlaveDataCnt(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U8 DataType, PU32 DataCnt)
```

##### Acm_DevGetSlaveFwVersion

```cpp
U32 Acm_DevGetSlaveFwVersion(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, OUT PI8 VersionInfo)
```

##### Acm_DevSetSlaveID

```cpp
U32 Acm_DevSetSlaveID(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 SlaveNewIP)
```

##### Acm_CheckVersion

```cpp
U32 Acm_CheckVersion(HAND DeviceHandle, U32 VersionID, PU32 Result)
```

##### Acm_DevMultiTrigSetPWMTableOnTime

```cpp
U32 Acm_DevMultiTrigSetPWMTableOnTime(HAND DeviceHandle, PU32 TimeTableArray, U32 ArrayCount)
```

##### Acm_DevMultiTrigSetCmpDO

```cpp
U32 Acm_DevMultiTrigSetCmpDO(HAND DeviceHandle,U32 OFForON)
```

##### Acm_DevMultiTrigForceCmpOut

```cpp
U32 Acm_DevMultiTrigForceCmpOut(HAND DeviceHandle, U32 OFForON)
```

##### Acm_DevMutiTrigSetCmpDO

```cpp
U32 Acm_DevMutiTrigSetCmpDO(HAND DeviceHandle,U32 OFForON)
```

##### Acm_DevMutiTrigForceCmpOut

```cpp
U32 Acm_DevMutiTrigForceCmpOut(HAND DeviceHandle, U32 OFForON)
```

##### Acm_MasStartRing

```cpp
U32 Acm_MasStartRing(HAND DeviceHandle, U16 RingNo)
```

##### Acm_MasStopRing

```cpp
U32 Acm_MasStopRing(HAND DeviceHandle, U16 RingNo)
```

##### Acm_MasGetComStatus

```cpp
U32 Acm_MasGetComStatus(HAND DeviceHandle, U16 RingNo, PU16 pStatus)
```

##### Acm_MasGetComCyclicTime

```cpp
U32 Acm_MasGetComCyclicTime(HAND DeviceHandle, U16 RingNo, PF64 pTime)
```

##### Acm_MasGetDataCyclicTime

```cpp
U32 Acm_MasGetDataCyclicTime(HAND DeviceHandle, U16 RingNo, PF64 DataCyclicTime)
```

##### Acm_MasGetActiveTable

```cpp
U32 Acm_MasGetActiveTable(HAND DeviceHandle, U16 RingNo, PU32 ActiveTableArray, PU32 ArrayElements)
```

##### Acm_MasGetErrorTable

```cpp
U32 Acm_MasGetErrorTable(HAND DeviceHandle, U16 RingNo, PU32 ErrorTableArray, PU32 ArrayElements)
```

##### Acm_MasGetSlaveInfo

```cpp
U32 Acm_MasGetSlaveInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PU32 pInfo)
```

##### Acm_MasLogComStatus

```cpp
U32 Acm_MasLogComStatus(HAND DeviceHandle, U16 RingNo)
```

##### Acm_AxOpen

```cpp
U32 Acm_AxOpen(HAND DeviceHandle, U16 PhyAxis, PHAND AxisHandle)
```

```python
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID
from AcmP.AdvMotErr_CM2 import ErrorCode

## Initialize
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
## Open Device
errCde = AdvMot.Acm_DevOpen(devNum.value, byref(devHandle))
## Open Axis
errCde = AdvMot.Acm_AxOpen(devHandle, axid, byref(axHand))
## Close Axis
errCde = AdvMot.Acm_AxClose(axHand)
## Close Device
errCde = AdvMot.Acm_DevClose(byref(devHandle))
```

##### Acm_AxOpenbyID

```cpp
U32 Acm_AxOpenbyID(HAND DeviceHandle, U16 SlaveID, U8 SubID, PHAND AxisHandle)
```

##### Acm_AxClose

```cpp
U32 Acm_AxClose(PHAND AxisHandle)
```

##### Acm_AxSetSvOn

```cpp
U32 Acm_AxSetSvOn(HAND AxisHandle, U32 OnOff)
```

##### Acm_AxResetAlm

```cpp
U32 Acm_AxResetAlm(HAND AxisHandle, U32 OnOff)
```

##### Acm_AxMoveRel

```cpp
U32 Acm_AxMoveRel(HAND AxisHandle, F64 Distance)
```

##### Acm_AxMoveRel_T

```cpp
U32 Acm_AxMoveRel_T(HAND AxisHandle, F64 Distance, F64 Time, F64 Factor)
```

##### Acm_AxMoveRel_SD

```cpp
U32 Acm_AxMoveRel_SD(HAND AxisHandle, F64 Distance, F64 SDDistance)
```

##### Acm_AxMoveRel_EC

```cpp
U32 Acm_AxMoveRel_EC(HAND AxisHandle, F64 Position)
```

##### Acm_AxMoveAbs

```cpp
U32 Acm_AxMoveAbs(HAND AxisHandle, F64 Position)
```

##### Acm_AxMoveAbs_T

```cpp
U32 Acm_AxMoveAbs_T(HAND AxisHandle, F64 Position, F64 Time, F64 Factor)
```

##### Acm_AxMoveAbs_SD

```cpp
U32 Acm_AxMoveAbs_SD(HAND AxisHandle, F64 Position, F64 SDPosition)
```

##### Acm_AxMoveAbs_EC

```cpp
U32 Acm_AxMoveAbs_EC(HAND AxisHandle, F64 Position)
```

##### Acm_AxMoveVel

```cpp
U32 Acm_AxMoveVel(HAND AxisHandle, U16 Direction)
```

##### Acm_AxStopDec

```cpp
U32 Acm_AxStopDec(HAND AxisHandle)
```

##### Acm_AxStopEmg

```cpp
U32 Acm_AxStopEmg(HAND AxisHandle)
```

##### Acm_AxMoveImpose

```cpp
U32 Acm_AxMoveImpose(HAND AxisHandle, F64 Position, F64 NewVel)
```

##### Acm_AxHome

```cpp
U32 Acm_AxHome(HAND AxisHandle, U32 HomeMode, U32 DirMode)
```

##### Acm_AxMoveHome

```cpp
U32 Acm_AxMoveHome(HAND AxisHandle, U32 HomeMode, U32 Dir)
```

##### Acm_AxMoveGantryHome

```cpp
U32 Acm_AxMoveGantryHome(HAND AxisHandle, U32 HomeMode, U32 Dir)
```

##### Acm_AxPauseMotion
```cpp
U32 Acm_AxPauseMotion(HAND AxisHandle)
```

##### Acm_AxResumeMotion
```
U32 Acm_AxResumeMotion(HAND AxisHandle)
```

##### Acm_AxChangeVel

```cpp
U32 Acm_AxChangeVel(HAND AxisHandle, F64 NewVel)
```

##### Acm_AxChangePos

```cpp
U32 Acm_AxChangePos(HAND AxisHandle, F64 NewPos)
```

##### Acm_AxChangeVelByRate

```cpp
U32 Acm_AxChangeVelByRate(HAND AxisHandle, U32 Rate)
```

##### Acm_AxResetError

```cpp
U32 Acm_AxResetError(HAND AxisHandle)
```

##### Acm_AxEnableTrig
```cpp
U32 Acm_AxEnableTrig(HAND AxisHandle, TRIG_PRM TrigPrm)
```

##### Acm_AxGetState

```cpp
U32 Acm_AxGetState(HAND AxisHandle, PU16 State)
```

##### Acm_AxGetMotionIO

```cpp
U32 Acm_AxGetMotionIO(HAND AxisHandle, PU32 Status)
```

##### Acm_AxGetMotionStatus

```cpp
U32 Acm_AxGetMotionStatus(HAND AxisHandle, PU32 Status)
```

##### Acm_AxGetCmdPosition

```cpp
U32 Acm_AxGetCmdPosition(HAND AxisHandle, PF64 Position)
```

##### Acm_AxGetMachPosition

```cpp
U32 Acm_AxGetMachPosition(HAND AxisHandle, PF64 Position)
```

##### Acm_AxSetCmdPosition

```cpp
U32 Acm_AxSetCmdPosition(HAND AxisHandle, F64 Position)
```

##### Acm_AxGetActualPosition

```cpp
U32 Acm_AxGetActualPosition(HAND AxisHandle, PF64 Position)
```

##### Acm_AxSetActualPosition

```cpp
U32 Acm_AxSetActualPosition(HAND AxisHandle, F64 Position)
```

##### Acm_AxGetCmdVelocity

```cpp
U32 Acm_AxGetCmdVelocity(HAND AxisHandle, PF64 Velocity)
```

##### Acm_AxGetActVelocity

```cpp
U32 Acm_AxGetActVelocity(HAND AxisHandle, PF64 Velocity)
```

##### Acm_AxGetLagCounter

```cpp
U32 Acm_AxGetLagCounter(HAND AxisHandle, PF64 Position)
```

##### Acm_AxSetExtDrive

```cpp
U32 Acm_AxSetExtDrive(HAND AxisHandle, U16 ExtDrvMode)
```

##### Acm_AxDoSetBit

```cpp
U32 Acm_AxDoSetBit(HAND AxisHandle, U16	DoChannel, U8 BitData)
```

##### Acm_AxDiSetBit

```cpp
U32 Acm_AxDiSetBit(HAND AxisHandle, U16	DiChannel, U8 BitData)
```

##### Acm_AxDoGetBit

```cpp
U32 Acm_AxDoGetBit(HAND AxisHandle, U16	DoChannel, PU8 BitData)
```

##### Acm_AxDiGetBit

```cpp
U32 Acm_AxDiGetBit(HAND AxisHandle, U16	DiChannel, PU8 BitData)
```

##### Acm_AxDoSetByte

```cpp
U32 Acm_AxDoSetByte(HAND AxisHandle, U16 DoPort, U8 ByteData)
```

##### Acm_AxDoGetByte

```cpp
U32 Acm_AxDoGetByte(HAND AxisHandle, U16 DoPort, PU8 ByteData)
```

##### Acm_AxDiGetByte

```cpp
U32 Acm_AxDiGetByte(HAND AxisHandle, U16 DiPort, PU8 ByteData)
```

##### Acm_AxSimStartSuspendVel

```cpp
U32 Acm_AxSimStartSuspendVel(HAND AxisHandle, U16 DriDir)
```

##### Acm_AxSimStartSuspendRel

```cpp
U32 Acm_AxSimStartSuspendRel(HAND AxisHandle,F64 Distance)
```

##### Acm_AxSimStartSuspendAbs

```cpp
U32 Acm_AxSimStartSuspendAbs(HAND AxisHandle,F64 EndPoint)
```

##### Acm_AxSimStart

```cpp
U32 Acm_AxSimStart(HAND AxisHandle)
```

##### Acm_AxSimStop

```cpp
U32 Acm_AxSimStop(HAND AxisHandle)
```

##### Acm_AxGetLatchData

```cpp
U32 Acm_AxGetLatchData(HAND AxisHandle, U32 PositionNo, PF64 Position)
```

##### Acm_AxStartSoftLatch

```cpp
U32 Acm_AxStartSoftLatch(U32 AxisHandle)
```

##### Acm_AxResetLatch

```cpp
U32 Acm_AxResetLatch(HAND AxisHandle)
```

##### Acm_AxGetLatchFlag

```cpp
U32 Acm_AxGetLatchFlag(HAND AxisHandle, PU8 LatchFlag)
```

##### Acm_AxTriggerLatch

```cpp
U32 Acm_AxTriggerLatch(HAND AxisHandle)
```

##### Acm_AxReadLatchBuffer

```cpp
U32 Acm_AxReadLatchBuffer(HAND AxisHandle, PF64 LatchDataArray, PU32 DataCnt)
```

##### Acm_AxResetLatchBuffer

```cpp
U32 Acm_AxResetLatchBuffer(HAND AxisHandle)
```

##### Acm_AxGetLatchBufferStatus

```cpp
U32 Acm_AxGetLatchBufferStatus(HAND AxisHandle, PU32 RemainCnt, PU32 SpaceCnt)
```

##### Acm_AxGearInAx

```cpp
U32 Acm_AxGearInAx(HAND AxisHandle, HAND MasAxisHandle, I32 Numerator, I32 Denominator, U32 RefSrc, U32 Absolute)
```

##### Acm_AxTangentInGp

```cpp
U32 Acm_AxTangentInGp(HAND AxisHandle, HAND MasGroupHandle, PI16 StartVectorArray, U8 Working_plane, I16 Direction)
```

##### Acm_AxGantryInAx

```cpp
U32	Acm_AxGantryInAx(HAND AxisHandle, HAND MasAxisHandle, I16 RefMasterSrc, I16 direction)
```

##### Acm_AxSyncOut
```cpp
U32 Acm_AxSyncOut(HAND FollowingAxisHandle)
```

##### Acm_AxPhaseAx

```cpp
U32 Acm_AxPhaseAx(HAND AxisHandle, F64 Acc, F64 Dec, F64 PhaseSpeed, F64 PhaseDist)
```

##### Acm_AxSetChannelCmpSetting

```cpp
U32 Acm_AxSetChannelCmpSetting(HAND AxisHandle, U16 ChannelID, U32 CmpSrc, U32 CmpMethod, U32 CmpPulseMode, U32 CmpPulseWidth)
```

##### Acm_AxGetChannelCmpSetting

```cpp
U32 Acm_AxGetChannelCmpSetting(HAND AxisHandle, U16 ChannelID, PU32 CmpSrc, PU32 CmpMethod, PU32 CmpPulseMode, PU32 CmpPulseWidth)
```

##### Acm_AxResetChannelCmp

```cpp
U32 Acm_AxResetChannelCmp(HAND AxisHandle, U16 ChannelID)
```

##### Acm_AxAddChannelCmpDatas

```cpp
U32 Acm_AxAddChannelCmpDatas(HAND AxisHandle, U16 ChannelID, PF64 TableArray, U32 ArrayCount)
```

##### Acm_AxGetChannelCmpData

```cpp
U32 Acm_AxGetChannelCmpData(HAND AxisHandle, U16 ChannelID, PF64 CmpData)
```

##### Acm_AxLoadChannelNextData

```cpp
U32 Acm_AxLoadChannelNextData(HAND AxisHandle, U16 ChannelID)
```

##### Acm_AxGetCmpbufferRemainCount

```cpp
U32 Acm_AxGetCmpbufferRemainCount(HAND AxisHandle, U16 ChannelID,PU32 DataCount)
```

##### Acm_AxSetCmpAuto

```cpp
U32 Acm_AxSetCmpAuto(HAND AxisHandle, F64 Start, F64 End, F64 Interval)
```

##### Acm_AxGetCmpData

```cpp
U32 Acm_AxGetCmpData(HAND AxisHandle, PF64 CmpPosition)
```

##### Acm_AxSetCmpData

```cpp
U32 Acm_AxSetCmpData(HAND AxisHandle, F64 CmpPosition)
```

##### Acm_AxSetCmpBufferData

```cpp
U32 Acm_AxSetCmpBufferData(HAND AxisHandle, PF64 TableArray, I32 ArrayCount)
```

##### Acm_AxResetCmpData

```cpp
U32 Acm_AxResetCmpData(HAND AxisHandle)
```

##### Acm_AxGetCmpBufferStatus

```cpp
U32 Acm_AxGetCmpBufferStatus(HAND AxisHandle, PU32 CurIndex, PU32 RemainCnt, PU32 SpaceCnt)
```

##### Acm_AxGetCmpCounter
```cpp
U32 Acm_AxGetCmpCounter(HAND AxisHandle, PU32 CmpCounter)
```

##### Acm_AxResetMPGOffset

```cpp
U32 Acm_AxResetMPGOffset(HAND AxisHandle)
```

##### Acm_AxMovePTPBufferRel

```cpp
U32 Acm_AxMovePTPBufferRel(HAND AxisHandle, U16 MotionMode, PF64 PositionArray, PF64 FLArray, PF64 FHArray, PU16 TSArray, U32 ArrayLength)
```

##### Acm_AxMovePTPBufferAbs

```cpp
U32 Acm_AxMovePTPBufferAbs(HAND AxisHandle, U16 MotionMode, PF64 PositionArray, PF64 FLArray, PF64 FHArray, PU16 TSArray, U32 ArrayLength)
```

##### Acm_AxEnableCompensation

```cpp
U32 Acm_AxEnableCompensation(HAND AxisHandle,F64 ZStartPos)
```

##### Acm_AxGetCompensationValue

```cpp
U32 Acm_AxGetCompensationValue(HAND AxisHandle, F64 XData, F64 YData, PF64 PCompensationValue)
```

##### Acm_AxSetCompenPara

```cpp
U32 Acm_AxSetCompenPara(HAND AxisHandle, HAND GroupHandle, U32 XScanDataCnt, U32 YScanDataCnt, U32 CompMode)
```

##### Acm_AxDIStartMoveAbs

```cpp
U32 Acm_AxDIStartMoveAbs(HAND AxisHandle, U16 DIChannel, F64 Position)
```

##### Acm_AxDIStartMoveRel

```cpp
U32 Acm_AxDIStartMoveRel(HAND AxisHandle, U16 DIChannel, F64 Distance)
```

##### Acm_AxDIStartMoveVel

```cpp
U32 Acm_AxDIStartMoveVel(HAND AxisHandle, U16 DIChannel, U16 Direction)
```

##### Acm_AxDisableDIStart

```cpp
U32 Acm_AxDisableDIStart(HAND AxisHandle)
```

##### Acm_AxSetPWMTableOnTime

```cpp
U32 Acm_AxSetPWMTableOnTime(HAND AxisHandle, PU32 TimeTableArray, I32 ArrayCount)
```

##### Acm_AxGetINxStopStatus

```cpp
U32 Acm_AxGetINxStopStatus(HAND AxisHandle,PU32 Stop_Flag)
```

##### Acm_AxResetINxStopStatus

```cpp
U32 Acm_AxResetINxStopStatus(HAND AxisHandle)
```

##### Acm_AxJog

```cpp
U32 Acm_AxJog(HAND AxisHandle,U16 Direction)
```

##### Acm_AxSetCmpDO

```cpp
U32 Acm_AxSetCmpDO(HAND AxisHandle,U32 OFForON)
```

##### Acm_AxDownloadTorqueTable

```cpp
U32 Acm_AxDownloadTorqueTable(HAND AxisHandle, PF64 PositionArray, PF64 TorqueArray, U32 ArrayElements)
```

##### Acm_AxLoadTorqueTableFile

```cpp
U32 Acm_AxLoadTorqueTableFile(HAND AxisHandle, PI8 FilePath, PU32 PointsCount)
```

##### Acm_AxResetPVTTable

```cpp
U32 Acm_AxResetPVTTable(HAND AxisHandle)
```

##### Acm_AxLoadPVTTable

```cpp
U32 Acm_AxLoadPVTTable(HAND AxisHandle, PF64 Position, PF64 Velocity, PF64 Time, U32 ArrayElements)
```

##### Acm_AxCalculatePVTTableContinuous

```cpp
U32 Acm_AxCalculatePVTTableContinuous(HAND AxisHandle, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, U32 ArrayElements, PF64 Time)
```

##### Acm_AxLoadPVTTableContinuous

```cpp
U32 Acm_AxLoadPVTTableContinuous(HAND AxisHandle, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, F64 TimeDelay, U32 ArrayElements)
```

##### Acm_AxStartPVT

```cpp
U32 Acm_AxStartPVT(HAND AxisHandle, U8 Repeat)
```

##### Acm_AxStartAllPVT

```cpp
U32 Acm_AxStartAllPVT(PHAND AxisHandle, U8 Repeat, U32 ArrayElements)
```

##### Acm_AxCheckPTBuffer

```cpp
U32 Acm_AxCheckPTBuffer(HAND AxisHandle, PU16 Freespace)
```

##### Acm_AxAddPTData

```cpp
U32 Acm_AxAddPTData(HAND AxisHandle, F64 Position, F64 Time)
```

##### Acm_AxStartPT

```cpp
U32 Acm_AxStartPT(HAND AxisHandle, U8 Repeat)
```

##### Acm_AxStartAllPT

```cpp
U32 Acm_AxStartAllPT(PHAND AxisHandle, U8 Repeat, U32 ArrayElements)
```

##### Acm_AxResetPTData

```cpp
U32 Acm_AxResetPTData(HAND AxisHandle)
```

##### Acm_AxAddPVAData

```cpp
U32 Acm_AxAddPVAData(HAND AxisHandle, F64 Position, PF64 VelArray, PF64 AccArray, PF64 DecArray, U32 ArrayElements)
```

##### Acm_GpOpen

```cpp
U32 Acm_GpOpen(HAND DevHandle,PHAND GpHandle,USHORT GpID)
```

##### Acm_GpGetAxesInGroup
```cpp
U32 Acm_GpGetAxesInGroup(HAND GroupHandle, PU32 AxisArray, PU32 ArrayElements)
```

##### Acm_GpGetState
```cpp
U32 Acm_GpGetState(HAND GroupHandle, PU16 State)
```

##### Acm_GpAddAxis

```cpp
U32 Acm_GpAddAxis(PHAND GpHandle,HAND AxHandle)
```

##### Acm_GpRemAxis

```cpp
U32 Acm_GpRemAxis(HAND GroupHandle, HAND AxisHandle)
```

##### Acm_GpClose

```cpp
U32 Acm_GpClose(PHAND GroupHandle)
```

##### Acm_GpGetState

```cpp
U32 Acm_GpGetState(HAND GroupHandle, PU16 State)
```

##### Acm_GpResetError

```cpp
U32 Acm_GpResetError(HAND GroupHandle)
```

##### Acm_GpIpoMask

```cpp
U32 Acm_GpIpoMask(HAND GroupHandle, HAND AxHandle, U32 Mask)
```

##### Acm_GpChangePos
```cpp
U32 Acm_GpChangePos(HAND GroupHandle, U32 Mode, PF64 DistanceArray, PU32 pArrayElements)
```

##### Acm_GpMoveLinearRel

```cpp
U32 Acm_GpMoveLinearRel(HAND GroupHandle, PF64 DistanceArray, PU32 ArrayElements)
```

##### Acm_GpMoveLinearAbs

```cpp
U32 Acm_GpMoveLinearAbs(HAND GroupHandle, PF64 PositionArray, PU32 ArrayElements)
```

##### Acm_GpMoveDirectRel

```cpp
U32 Acm_GpMoveDirectRel(HAND GroupHandle, PF64 DistanceArray, PU32 ArrayElements)
```

##### Acm_GpMoveDirectAbs

```cpp
U32 Acm_GpMoveDirectAbs(HAND GroupHandle, PF64 PositionArray, PU32 ArrayElements)
```

##### Acm_GpMoveCircularRel

```cpp
U32 Acm_GpMoveCircularRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 ArrayElements, I16 Direction)
```

##### Acm_GpMoveCircularAbs

```cpp
U32 Acm_GpMoveCircularAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 ArrayElements, I16 Direction)
```

##### Acm_GpMoveCircularRel_3P

```cpp
U32 Acm_GpMoveCircularRel_3P(HAND GroupHandle, PF64	RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)

```

##### Acm_GpMoveCircularAbs_3P

```cpp
U32 Acm_GpMoveCircularAbs_3P(HAND GroupHandle, PF64	RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

##### Acm_GpMoveCircularRel_Angle

```cpp
U32 Acm_GpMoveCircularRel_Angle(HAND GroupHandle, PF64 CenterArray, U16 Degree, PU32 ArrayElements, I16 Direction)

```

##### Acm_GpMoveCircularAbs_Angle

```cpp
U32 Acm_GpMoveCircularAbs_Angle(HAND GroupHandle, PF64 CenterArray, U16 Degree, PU32 ArrayElements, I16 Direction)
```

##### Acm_GpMoveArcRel_Angle

```cpp
U32 Acm_GpMoveArcRel_Angle(HAND GroupHandle, PF64 CenterArray, F64 Degree, PU32 ArrayElements, I16 Direction)
```

##### Acm_GpMoveArcAbs_Angle

```cpp
U32 Acm_GpMoveArcAbs_Angle(HAND GroupHandle, PF64 CenterArray, F64 Degree, PU32 ArrayElements, I16 Direction)
```

##### Acm_GpMove3DArcAbs

```cpp
U32 Acm_GpMove3DArcAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

##### Acm_GpMove3DArcRel

```cpp
U32 Acm_GpMove3DArcRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)

```

##### Acm_GpMove3DArcAbs_V

```cpp
U32 Acm_GpMove3DArcAbs_V(HAND GroupHandle, PF64 CenterArray, PF64 NVectorArray, F64 Degree, PU32 pArrayElements, I16 Direction)
```

##### Acm_GpMove3DArcRel_V

```cpp
U32 Acm_GpMove3DArcRel_V(HAND GroupHandle, PF64 CenterArray, PF64 NVectorArray, F64 Degree, PU32 pArrayElements, I16 Direction)
```

##### Acm_GpMove3DArcAbs_3P

```cpp
U32 Acm_GpMove3DArcAbs_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, U16 cycCount)
```

##### Acm_GpMove3DArcRel_3P

```cpp
U32 Acm_GpMove3DArcRel_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, U16 cycCount)
```

##### Acm_GpMove3DArcAbs_3PAngle

```cpp
U32 Acm_GpMove3DArcAbs_3PAngle(HAND GroupHandle, PF64 RefPoint_1, PF64 RefPoint_2, PU32 pArrayElements, I16 Direction, F64 Degree)
```

##### Acm_GpMove3DArcRel_3PAngle

```cpp
U32 Acm_GpMove3DArcRel_3PAngle(HAND GroupHandle, PF64 RefPoint_1, PF64 RefPoint_2, PU32 pArrayElements, I16 Direction, F64 Degree)

```

##### Acm_GpMoveHelixAbs

```cpp
U32 Acm_GpMoveHelixAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

##### Acm_GpMoveHelixRel

```cpp
U32 Acm_GpMoveHelixRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

##### Acm_GpMoveSpiral
```cpp
U32 Acm_GpMoveSpiral(HAND GroupHandle, F64 fStartRadius, F64 fGrowthRate, F64 fStartAngle_deg, F64 fSweepAngle_deg, I16 Direction)
```

##### Acm_GpMoveSpiralCenRel
```cpp
U32 Acm_GpMoveSpiralCenRel(HAND GroupHandle, PF64 CenterArray, PU32 ArrayElements, F64 fPitch, F64 fSweepAngle_deg, I16 Direction)
```

##### Acm_GpMoveSpiralCenAbs
```cpp
U32 Acm_GpMoveSpiralCenAbs(HAND GroupHandle, PF64 CenterArray, PU32 ArrayElements, F64 fPitch, F64 fSweepAngle_deg, I16 Direction)
```

##### Acm_GpMoveSpiralByRange
```cpp
U32 Acm_GpMoveSpiralByRange(HAND GroupHandle, F64 fRstart, F64 fRend, F64 fTurns)
```

##### Acm_GpMoveSpiralCenPitchRel
```cpp
U32 Acm_GpMoveSpiralCenPitchRel(HAND GroupHandle, PF64 CenterArray, PF64 RefEndArray, PU32 ArrayElements, F64 fPitch, I16 Direction)
```

##### Acm_GpMoveSpiralCenPitchAbs
```cpp
U32 Acm_GpMoveSpiralCenPitchAbs(HAND GroupHandle, PF64 CenterArray, PF64 RefEndArray, PU32 ArrayElements, F64 fPitch, I16 Direction)
```

##### Acm_GpMoveSpiralCenEndPitchRel
```cpp
U32 Acm_GpMoveSpiralCenEndPitchRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 ArrayElements, F64 fPitch, I16 Direction)
```

##### Acm_GpMoveSpiralCenEndPitchAbs
```cpp
U32 Acm_GpMoveSpiralCenEndPitchAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 ArrayElements, F64 fPitch, I16 Direction)
```

##### Acm_GpMoveHelixAbs_3P

```cpp
U32 Acm_GpMoveHelixAbs_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

##### Acm_GpMove3DArcRel_3PAngle

```cpp
U32 Acm_GpMove3DArcRel_3PAngle(HAND GroupHandle, PF64 RefPoint_1, PF64 RefPoint_2, PU32 pArrayElements, I16 Direction, F64 Degree)
```

##### Acm_GpMoveHelixAbs

```cpp
U32 Acm_GpMoveHelixAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

##### Acm_GpMoveHelixRel

```cpp
U32 Acm_GpMoveHelixRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

##### Acm_GpMoveHelixAbs_3P

```cpp
U32 Acm_GpMoveHelixAbs_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

##### Acm_GpMoveHelixRel_3P

```cpp
U32 Acm_GpMoveHelixRel_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

##### Acm_GpMoveHelixRel_Angle

```cpp
U32 Acm_GpMoveHelixRel_Angle(HAND GroupHandle, PF64	CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

##### Acm_GpMoveHelixAbs_Angle

```cpp
U32 Acm_GpMoveHelixAbs_Angle(HAND GroupHandle, PF64	CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

##### Acm_GpMoveEllipticalRel

```cpp
U32 Acm_GpMoveEllipticalRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, F64 RatioSemiAxes)
```

##### Acm_GpMoveEllipticalAbs

```cpp
U32 Acm_GpMoveEllipticalAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, F64 RatioSemiAxes)
```

##### Acm_GpLoadPath

```cpp
U32 Acm_GpLoadPath(HAND GroupHandle, PI8 FilePath, PHAND PathHandle, PU32 pTotalCount)
```

##### Acm_GpUnloadPath

```cpp
U32 Acm_GpUnloadPath(HAND GroupHandle, PHAND PathHandle)
```

##### Acm_GpMovePath

```cpp
U32 Acm_GpMovePath(HAND GroupHandle, HAND PathHandle)
```

##### Acm_GpMoveAllPath

```cpp
U32 Acm_GpMoveAllPath(PHAND GroupHandle, U32 ArrayElements)
```

##### Acm_GpAddPath

```cpp
U32 Acm_GpAddPath(HAND GroupHandle, U16 MoveCmd, U16 MoveMode, F64 FH, F64 FL, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)
```

##### Acm_GpLookAheadPath

```cpp
U32 Acm_GpLookAheadPath(HAND GroupHandle, U16 BufferSize, PI8 OutputFile)
```

##### Acm_GpResetPath

```cpp
U32 Acm_GpResetPath (PHAND GroupHandle)
```

##### Acm_GpGetPathStatus

```cpp
U32 Acm_GpGetPathStatus(HAND GroupHandle, PU32 pCurIndex, PU32 pCurCmdFunc, PU32 pRemainCount, PU32 pFreeSpaceCount)
```

##### Acm_GpMoveSelPath

```cpp
U32 Acm_GpMoveSelPath(HAND GroupHandle, HAND PathHandle, U32 StartIndex, U32 EndIndex, U8 Repeat)
```

##### Acm_GpGetPathIndexStatus

```cpp
U32 Acm_GpGetPathIndexStatus(HAND GroupHandle, U32 Index, PU16 CmdFunc, PU16 MoveMode, PF64 FH, PF64 FL, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements);
```

##### Acm_GpDelay
```cpp
U32 Acm_GpDelay(HAND GroupHandle, U32 DelayTime)
```

##### Acm_GpPathDO
```cpp
U32 Acm_GpPathDO(HAND GroupHandle, PATH_DO_PRM PathDOPrm)
```

##### Acm_GpPathWaitDI
```cpp
U32 Acm_GpPathWaitDI(HAND GroupHandle, PATH_DI_WAIT_PRM DIWaitPrm)
```

##### Acm_GpPathWaitForAxis
```cpp
U32 Acm_GpPathWaitForAxis(HAND GroupHandle, PATH_AX_WAIT_PRM AxWaitPrm)
```

##### Acm_GpPathDIConditional
```cpp
U32 Acm_GpPathDIConditional(HAND GroupHandle, U16 MoveCmd, PATH_DI_WAIT_PRM PathDIPrm)
```

##### Acm_GpPathDOConditional
```cpp
U32 Acm_GpPathDOConditional(HAND GroupHandle, U16 MoveCmd, PATH_DO_PRM PathDOPrm)
```

##### Acm_GpPathAxisConditional
```cpp
U32 Acm_GpPathAxisConditional(HAND GroupHandle, U16 MoveCmd, PATH_AX_WAIT_PRM AxPrm)
```

##### Acm_GpPathVarConditional
```cpp
U32 Acm_GpPathVarConditional(HAND GroupHandle, U16 MoveCmd, PATH_VAR_PRM VarPrm)
```

##### Acm_GpPathConditional
```cpp
U32 Acm_GpPathConditional(HAND GroupHandle, U16 MoveCmd)
```

##### Acm_GpPathOperator
```cpp
U32 Acm_GpPathOperator(HAND GroupHandle, PATH_OPERATOR_PRM OperatorPrm)
```

##### Acm_GpPathStartRecordBuffer
```cpp
U32 Acm_GpPathStartRecordBuffer(HAND GroupHandle)
```

##### Acm_GpPathEndRecordBuffer
```cpp
U32 Acm_GpPathEndRecordBuffer(HAND GroupHandle, VALIDATE_RESULT* OutResult)
```

##### Acm_GpAddBSplinePath

```cpp
U32 Acm_GpAddBSplinePath(HAND GroupHandle, F64 FH, F64 FL, F64 *CtrlP0List, F64 *CtrlP1List, U32 CtrlPCount, F64 *NodeList, U32 NodeCount, U32 Degree, U32 CutPointCount)
```

##### Acm_GpAddCSplinePath

```cpp
U32 Acm_GpAddCSplinePath(HAND GroupHandle, F64 FH, F64 FL, F64 *CtrlP0List, F64 *CtrlP1List, F64 *Tightness, U32 CtrlPCount, U32 CutPointCount)

```

##### Acm_GpResumeMotion

```cpp
U32 Acm_GpResumeMotion(HAND GroupHandle)
```

##### Acm_GpPauseMotion

```cpp
U32 Acm_GpPauseMotion(HAND GroupHandle)
```

##### Acm_GpStopDec

```cpp
U32 Acm_GpStopDec(HAND GroupHandle)
```

##### Acm_GpStopEmg

```cpp
U32 Acm_GpStopEmg(HAND GroupHandle)
```

##### Acm_GpChangeVel

```cpp
U32 Acm_GpChangeVel(HAND GroupHandle, F64 NewVelocity)
```

##### Acm_GpChangeVelByRate

```cpp
U32 Acm_GpChangeVelByRate(HAND GroupHandle, U32 Rate)
```

##### Acm_GpGetCmdVel

```cpp
U32 Acm_GpGetCmdVel(HAND GroupHandle, PF64 CmdVel)
```

##### Acm_GpGetINxStopStatus

```cpp
U32 Acm_GpGetINxStopStatus(HAND GroupHandle,PU32 Stop_Flag)
```

##### Acm_GpResetINxStopStatus

```cpp
U32 Acm_GpResetINxStopStatus(HAND GroupHandle)
```

##### Acm_DaqDiGetByte

```cpp
U32 Acm_DaqDiGetByte(HAND DeviceHandle, U16 DiPort, PU8 ByteData)
```

##### Acm_DaqDiGetBit

```cpp
U32 Acm_DaqDiGetBit(HAND DeviceHandle, U16 DiChannel, PU8 BitData)
```

##### Acm_DaqDoSetByte

```cpp
U32 Acm_DaqDoSetByte(HAND DeviceHandle, U16 DoPort, U8	ByteData)
```

##### Acm_DaqDoSetBit

```cpp
U32 Acm_DaqDoSetBit(HAND DeviceHandle, U16 DoChannel, U8 BitData)
```

##### Acm_GpGetPausePosition

```cpp
U32 Acm_GpGetPausePosition(HAND GroupHandle, PF64 RefPausePosition)
```

##### Acm_GpSetRawData

```cpp
U32 Acm_GpSetRawData(HAND GroupHandle, U8 index, F64 RawData)
```

##### Acm_GpGetRawData

```cpp
U32 Acm_GpGetRawData(HAND GroupHandle, U8 index, PF64 RawData)
```

##### Acm_DaqDiSetBit

```cpp
U32 Acm_DaqDiSetBit(HAND DeviceHandle, U16 DiChannel, U8 BitData)
```

##### Acm_DaqDoGetByte

```cpp
U32 Acm_DaqDoGetByte(HAND DeviceHandle, U16 DoPort, PU8 ByteData)
```

##### Acm_DaqDoGetBit

```cpp
U32 Acm_DaqDoGetBit(HAND DeviceHandle, U16 DoChannel, PU8 BitData)
```

##### Acm_DaqDiGetBytes

```cpp
U32 Acm_DaqDiGetBytes(HAND DeviceHandle, U16 StartPort, U16 NumPort, PU8 ByteDataArray)
```

##### Acm_DaqDoSetBytes

```cpp
U32 Acm_DaqDoSetBytes(HAND DeviceHandle, U16 StartPort, U16 NumPort, PU8 ByteDataArray)
```

##### Acm_DaqDoGetBytes

```cpp
U32 Acm_DaqDoGetBytes(HAND DeviceHandle, U16 StartPort, U16 NumPort, PU8 ByteDataArray)
```

##### Acm_DaqAiGetRawData

```cpp
U32 Acm_DaqAiGetRawData(HAND DeviceHandle, U16 AiChannel, PU16 AiData)
```

##### Acm_DaqAiGetEngData

```cpp
U32 Acm_DaqAiGetEngData(HAND DeviceHandle, U16 AiChannel, PF32 AiData)
```

##### Acm_DaqAiGetVoltData

```cpp
U32 Acm_DaqAiGetVoltData(HAND DeviceHandle, U16	AiChannel, PF32	AiData)
```

##### Acm_DaqAiGetCurrData

```cpp
U32 Acm_DaqAiGetCurrData(HAND DeviceHandle, U16	AiChannel, PF32	AiData)
```

##### Acm_DaqAiZeroCalibration

```cpp
U32 Acm_DaqAiZeroCalibration(HAND DeviceHandle, U16	AiChannel)
```

##### Acm_DaqAiSpanCalibration

```cpp
U32 Acm_DaqAiSpanCalibration(HAND DeviceHandle, U16	AiChannel)
```

##### Acm_DaqAiGetChannelStatus

```cpp
U32 Acm_DaqAiGetChannelStatus(HAND DeviceHandle, U16 AiChannel, PU32 ChanStatus)
```

##### Acm_DaqAoSetRawData

```cpp
U32 Acm_DaqAoSetRawData(HAND DeviceHandle, U16 AoChannel, U16 AoData)
```

##### Acm_DaqAoSetEngData

```cpp
U32 Acm_DaqAoSetEngData(HAND DeviceHandle, U16 AoChannel, F32 AoData)
```

##### Acm_DaqAoSetVoltData

```cpp
U32 Acm_DaqAoSetVoltData(HAND DeviceHandle, U16	AoChannel, F32 AoData)
```

##### Acm_DaqAoSetCurrData

```cpp
U32 Acm_DaqAoSetCurrData(HAND DeviceHandle, U16	AoChannel, F32 AoData)
```

##### Acm_DaqAoGetRawData

```cpp
U32 Acm_DaqAoGetRawData(HAND DeviceHandle, U16 AoChannel, PU16 AoData)
```

##### Acm_DaqAoGetEngData

```cpp
U32 Acm_DaqAoGetEngData(HAND DeviceHandle, U16 AoChannel, PF32 AoData)
```

##### Acm_DaqAoGetVoltData

```cpp
U32 Acm_DaqAoGetVoltData(HAND DeviceHandle, U16	AoChannel, PF32 AoData)
```

##### Acm_DaqAoGetCurrData

```cpp
U32 Acm_DaqAoGetCurrData(HAND DeviceHandle, U16	AoChannel, PF32 AoData)
```

##### Acm_DaqAoSetCaliType

```cpp
U32 Acm_DaqAoSetCaliType(HAND DeviceHandle, U16	AoChannel, U16 TrimType)
```

##### Acm_DaqAoSetCaliValue

```cpp
U32 Acm_DaqAoSetCaliValue(HAND DeviceHandle, U16 AoChannel, U16 CaliData)
```

##### Acm_DaqAoCaliDone

```cpp
U32 Acm_DaqAoCaliDone(HAND DeviceHandle, U16 AoChannel, bool done)
```

##### Acm_DaqAoCaliDefault

```cpp
U32 Acm_DaqAoCaliDefault(HAND DeviceHandle, U16	AoChannel)
```

##### Acm_DaqAoGetChannelStatus

```cpp
U32 Acm_DaqAoGetChannelStatus(HAND DeviceHandle, U16 AoChannel, PU32 ChanStatus)
```

##### Acm_DaqAoLinkAxData
```cpp
U32 Acm_DaqAoLinkAxData(HAND DeviceHandle, U16 AoChannel, HAND AxisHandle, U16 Type, F64 Max, F64 Min)
```

##### Acm_DaqSetScaledProperty

```cpp
U32 Acm_DaqSetScaledProperty(HAND DeviceHandle, PORT_TYPE Type, U16 Channel, F32 UpperBound, F32 LowerBound, U16 Resolution, I16 TransType)
```

##### Acm_DaqGetIOLinkStatus

```cpp
U32 Acm_DaqGetIOLinkStatus(HAND DeviceHandle, PU32 pStatus)
```

##### Acm_DaqCntTriggerCmp

```cpp
U32 Acm_DaqCntTriggerCmp(HAND DeviceHandle, U16 CntChannel)
```

##### Acm_DaqCntResetLatch

```cpp
U32 Acm_DaqCntResetLatch(HAND DeviceHandle, U16 CntChannel)
```

##### Acm_DaqCntResetCmp

```cpp
U32 Acm_DaqCntResetCmp(HAND DeviceHandle, U16 CntChannel)
```

##### Acm_DaqCntResetCnt

```cpp
U32 Acm_DaqCntResetCnt(HAND DeviceHandle, U16 CntChannel)
```

##### Acm_DaqCntGetCounterData

```cpp
U32 Acm_DaqCntGetCounterData(HAND DeviceHandle, U16 CntChannel, PF64 CounterData)
```

##### Acm_DaqCntSetCounterData

```cpp
U32 Acm_DaqCntSetCounterData(HAND DeviceHandle, U16 CntChannel, F64 CounterData)
```

##### Acm_DaqCntGetCounterFrequency

```cpp
U32 Acm_DaqCntGetCounterFrequency(HAND DeviceHandle, U16 CntChannel, PF64 Frequency)
```

##### Acm_DaqCntGetExtDriveData

```cpp
U32 Acm_DaqCntGetExtDriveData(HAND DeviceHandle, U16 CntChannel, PF64 CounterData)
```

##### Acm_DaqCntSetExtDriveData

```cpp
U32 Acm_DaqCntSetExtDriveData(HAND DeviceHandle, U16 CntChannel, F64 CounterData)
```

##### Acm_DaqCntGetLatchData

```cpp
U32 Acm_DaqCntGetLatchData(HAND DeviceHandle, U16 CntChannel, PF64 LatchData)
```

##### Acm_DaqCntGetCmpData

```cpp
U32 Acm_DaqCntGetCmpData(HAND DeviceHandle, U16 CntChannel, PF64 CmpData)
```

##### Acm_DaqCntSetCmpData

```cpp
U32 Acm_DaqCntSetCmpData(HAND DeviceHandle, U16 CntChannel, F64 CmpData)
```

##### Acm_DaqCntSetCmpTable

```cpp
U32 Acm_DaqCntSetCmpTable(HAND DeviceHandle, U16 CntChannel, PF64 TableArray, I32 ArrayCount)
```

##### Acm_DaqCntSetCmpAuto

```cpp
U32 Acm_DaqCntSetCmpAuto(HAND DeviceHandle, U16 CntChannel, F64 Start, F64 End, F64 Interval)
```

##### Acm_DaqCntGetLatchBufferStatus

```cpp
U32 Acm_DaqCntGetLatchBufferStatus(HAND DeviceHandle, U16 CntChannel, PU32 RemainCnt, PU32 SpaceCnt)
```

##### Acm_DaqCntReadLatchBuffer

```cpp
U32 Acm_DaqCntReadLatchBuffer(HAND DeviceHandle, U16 CntChannel, PF64 LatchDataArray, PU32 DataCnt)
```

##### Acm_ChLinkCmpObject
```cpp
U32 Acm_ChLinkCmpObject(HAND DeviceHandle, U32 CmpID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)
```

##### Acm_ChGetLinkedCmpObject
```cpp
U32 Acm_ChGetLinkedCmpObject(HAND DeviceHandle, U32 CmpID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```

##### Acm_ChEnableCmp
```cpp
U32 Acm_ChEnableCmp(HAND DeviceHandle, U32 CmpID, U32 Enable)
```

##### Acm_ChSetCmpOut
```cpp
U32 Acm_ChSetCmpOut(HAND DeviceHandle, U32 CmpID, DO_ONOFF OnOff)
```

##### Acm_ChSetCmpDoOut
```cpp
U32 Acm_ChSetCmpDoOut(HAND DeviceHandle, U32 CmpID, DO_ONOFF OnOff)
```

##### Acm_ChGetCmpData
```cpp
U32 Acm_ChGetCmpData(HAND DeviceHandle, U32 CmpID, PF64 CmpData, U32 ObjectArrayCount)
```

##### Acm_ChSetCmpAuto
```cpp
U32 Acm_ChSetCmpAuto(HAND DeviceHandle, U32 CmpID, F64 StartPosition, F64 EndPosition, F64 Interval)
```

##### Acm_ChSetCmpBufferData
```cpp
U32 Acm_ChSetCmpBufferData(HAND DeviceHandle, U32 CmpID, PF64 TableArray, U32 ArrayCount)
```

##### Acm_ChSetMultiCmpBufferData
```cpp
U32 Acm_ChSetMultiCmpBufferData(HAND DeviceHandle, U32 CmpID, PF64 MultiCmpTable, U32 ObjectArrayCount, U32 DataArrayCount)
```

##### Acm_ChResetCmpData
```cpp
U32 Acm_ChResetCmpData(HAND DeviceHandle, U32 CmpID)
```

##### Acm_ChGetCmpBufferStatus
```cpp
U32 Acm_ChGetCmpBufferStatus(HAND DeviceHandle, U32 CmpID, PBUFFER_STATUS BufferStatus)
```

##### Acm_ChLinkLatchObject
```cpp
U32 Acm_ChLinkLatchObject(HAND DeviceHandle, U32 LtcID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)
```

##### Acm_ChGetLinkedLatchObject
```cpp
U32 Acm_ChGetLinkedLatchObject(HAND DeviceHandle, U32 LtcID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```

##### Acm_ChTriggerLatch
```cpp
U32 Acm_ChTriggerLatch(HAND DeviceHandle, U32 LtcID)
```

##### Acm_ChReadLatchBuffer
```cpp
U32 Acm_ChReadLatchBuffer(HAND DeviceHandle, U32 LtcID, PF64 LatchDataArray, U32 ObjectArrayCount, PU32 DataArrayCount)
```

##### Acm_ChGetLatchBufferStatus
```cpp
U32 Acm_ChGetLatchBufferStatus(HAND DeviceHandle, U32 LtcID, PBUFFER_STATUS BufferStatus)
```

##### Acm_ChResetLatchBuffer
```cpp
U32 Acm_ChResetLatchBuffer(HAND DeviceHandle, U32 LtcID)
```

##### Acm_AxPWMOut

```cpp
U32 Acm_AxPWMOut(HAND AxisHandle,U32 OFForON,U32 PulseCount)
```

##### Acm_AxGetPWMOutState

```cpp
U32 Acm_AxGetPWMOutState(HAND AxisHandle,PU32 OFForON)
```

##### Acm_DevMDaqConfig

```cpp
U32 Acm_DevMDaqConfig(HAND DeviceHandle, U16 ChannelID, U32 Period, U32 AxisNo, U32 Method, U32 ChanType, U32 Count)
```

##### Acm_DevMDaqStart

```cpp
U32 Acm_DevMDaqStart(HAND DeviceHandle)
```

##### Acm_DevMDaqStop

```cpp
U32 Acm_DevMDaqStop(HAND DeviceHandle)
```

##### Acm_DevMDaqReset

```cpp
U32 Acm_DevMDaqReset(HAND DeviceHandle, U16 ChannelID)
```

##### Acm_DevMDaqGetStatus

```cpp
U32 Acm_DevMDaqGetStatus(HAND DeviceHandle, U16 ChannelID, PU16 CurrentCnt, PU8 Status)
```

##### Acm_DevMDaqGetData

```cpp
U32 Acm_DevMDaqGetData(HAND DeviceHandle, U16 ChannelID, U16 StartIndex, U16 MaxCount, PI32 DataBuffer)
```

##### Acm_DevMDaqGetConfig

```cpp
U32 Acm_DevMDaqGetConfig(HAND DeviceHandle, U16 ChannelID, PU32 Period, PU32 AxisNo, PU32 Method, PU32 ChanType, PU32 Count)
```

##### Acm_RegCallBackFunc

```cpp
U32 Acm_RegCallBackFunc(HAND Handle, ADV_USER_CALLBACK_FUNC CallBackFun, PVOID UserParamter)
```

##### Acm_EnableEventCallBack

```cpp
U32 Acm_EnableEventCallBack(HAND DeviceHandle)
```

##### Acm_RegCallBackFuncForOneEvent

```cpp
U32 Acm_RegCallBackFuncForOneEvent(HAND Handle, U32 EvtChannel, ADV_USER_CALLBACK_FUNC CallBackFun, PVOID UserParamter)
```

##### Acm_DevEnableMotionEvent

```cpp
U32 Acm_DevEnableMotionEvent(HAND DeviceHandle, PU32 AxEnableEvtArray, PU32 GpEnableEvtArray, U32 AxArrayElements, U32 GpArrayElements)
```

##### Acm_ServoSetCom

```cpp
U32 Acm_ServoSetCom(U32 ComPortID, U32 Baudrate, U32 Timeout)
```

##### Acm_ServoGetAbsPosition

```cpp
U32 Acm_ServoGetAbsPosition(U32 ComPortID, U32 ServoType, U32 ServoID, U32 ServoAbsResolution, U32 ServoCmdResolution, U32 EncoderDir, PF64 AbsPosition)
```

##### Acm_AxSetCmdPosi_Pulse

```cpp
U32 Acm_AxSetCmdPosi_Pulse(HAND AxisHandle,F64 Position)
```

##### Acm_AxSpecialDiSetBit

```cpp
U32 Acm_AxSpecialDiSetBit(HAND AxisHandle,U16 DiType,U8 BitData)
```

##### Acm_DevEnableLTC

```cpp
U32 Acm_DevEnableLTC(HAND DeviceHandle, U16 LtcID, U16 EnableMode)
```

##### Acm_DevLTCSaftyDist

```cpp
U32 Acm_DevLTCSaftyDist(HAND DeviceHandle, U16 LtcID, F64 SaftyDist)
```

##### Acm_DevEnableCmp

```cpp
U32 Acm_DevEnableCmp(HAND DeviceHandle, U16 CmpID, U16 EnableMode)
```

##### Acm_DevLtcLinkCmp

```cpp
U32 Acm_DevLtcLinkCmp(HAND DeviceHandle, HAND AxisHandle, U16 EnableLink, U16 LtcID, U16 CmpID, F64 Offset)
```

##### Acm_DevSetCmp

```cpp
U32 Acm_DevSetCmp(HAND DeviceHandle, U16 CmpID, U32 CmpLogic, U32 CmpSrc, U32 CmpMethod, U32 DOMode, U32 DOWidth)
```

##### Acm_DevSetCmpDO

```cpp
U32 Acm_DevSetCmpDO(HAND DeviceHandle, U16 CmpID, U16 OnOff)
```

##### Acm_DevSetCmpData

```cpp
U32 Acm_DevSetCmpData(HAND DeviceHandle, U16 CmpID, F64 Data)
```

##### Acm_DevSetCmpAuto

```cpp
U32 Acm_DevSetCmpAuto(HAND DeviceHandle, U16 CmpID, F64 Start, F64 End, F64 Interval)
```

##### Acm_DevGetCmpData

```cpp
U32 Acm_DevGetCmpData(HAND DeviceHandle, U16 CmpID, PF64 Data)
```

##### Acm_DevEnableCmpFIFO

```cpp
U32 Acm_DevEnableCmpFIFO(HAND DeviceHandle, U16 CmpID, U16 Enable)
```

##### Acm_DevGetCmpFIFOCount

```cpp
U32 Acm_DevGetCmpFIFOCount(HAND DeviceHandle, U16 CmpID, PU16 DataCount)
```

##### Acm_DevGetCmpCounter

```cpp
U32 Acm_DevGetCmpCounter(HAND DeviceHandle, U16 CmpID, PU32 DataCount)
```

##### Acm_DevResetCmpFIFO

```cpp
U32 Acm_DevResetCmpFIFO(HAND DeviceHandle, U16 CmpID)
```

##### Acm_DevSetLTCInEdge

```cpp
U32 Acm_DevSetLTCInEdge(HAND DeviceHandle, U16 LtcID, U16 Edge)
```

##### Acm_DevGetLTCData

```cpp
U32 Acm_DevGetLTCData(HAND DeviceHandle, U16 LtcID, PF64 CommandPosition, PF64 Actualposition)
```

##### Acm_DevGetLTCFlag

```cpp
U32 Acm_DevGetLTCFlag(HAND DeviceHandle, U16 LtcID, PU8 LtcFlag)
```

##### Acm_DevResetLTC

```cpp
U32 Acm_DevResetLTC(HAND DeviceHandle, U16 LtcID)
```

##### Acm_DevGetCmpFlag

```cpp
U32 Acm_DevGetCmpFlag(HAND DeviceHandle, U16 CmpID, PU8 CmpFlag)
```

##### Acm_DevResetCmpFlag

```cpp
U32 Acm_DevResetCmpFlag(HAND DeviceHandle, U16 CmpID)
```

##### Acm_DevGetLtcLinkCmpStatus

```cpp
U32 Acm_DevGetLtcLinkCmpStatus(HAND DeviceHandle, U16 LtcID, PU16 LinkStatus)
```

##### Acm_DevResetCmpData

```cpp
U32 Acm_DevResetCmpData(HAND DeviceHandle, U16 CmpID)
```

##### Acm_DevGetLTCInEdge

```cpp
U32 Acm_DevGetLTCInEdge(HAND DeviceHandle, U16 LtcID, PU16 Edge)
```

##### Acm_DevGetLTCInPol

```cpp
U32 Acm_DevGetLTCInPol(HAND DeviceHandle, U16 LtcID, PU16 Logic)
```

##### Acm_DevGetLTCSaftyDist

```cpp
U32 Acm_DevGetLTCSaftyDist(HAND DeviceHandle, U16 LtcID, PF64 SaftyDist)
```

##### Acm_DevGetLTCInSource

```cpp
U32 Acm_DevGetLTCInSource(HAND DeviceHandle, U16 LtcID, PU16 Source)
```

##### Acm_DevSetLTCInSource

```cpp
U32 Acm_DevSetLTCInSource(HAND DeviceHandle, U16 LtcID, U16 Source)
```

##### Acm_DevGetCmp

```cpp
U32 Acm_DevGetCmp(HAND DeviceHandle, U16 CmpID, PU32 CmpLogic, PU32 CmpSrc, PU32 CmpMethod, PU32 DOMode, PU32 DOWidth)
```

##### Acm_ChLinkSWCmpObject
```cpp
U32 Acm_ChLinkSWCmpObject(HAND DeviceHandle, U16 SWCmpID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)
```

##### Acm_DaqDoLinkSWCmpObject
```cpp
U32 Acm_DaqDoLinkSWCmpObject(HAND DeviceHandle, U16 SWCmpID, U32 DOChannel)
```

##### Acm_ChGetLinkedSWCmpObject
```cpp
U32 Acm_ChGetLinkedSWCmpObject(HAND DeviceHandle, U16 SWCmpID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```

##### Acm_DaqDoGetLinkedSWCmpObject
```cpp
U32 Acm_DaqDoGetLinkedSWCmpObject(HAND DeviceHandle, U16 SWCmpID, PU32 DOChannel)
```

##### Acm_DevReadLatchBuffer

```cpp
U32 Acm_DevReadLatchBuffer(HAND DeviceHandle, U16 LtcID, PF64 CommandPositionArray, PF64 ActualPositionArray, PU32 DataCnt)
```

##### Acm_DevGetLatchBufferStatus

```cpp
U32 Acm_DevGetLatchBufferStatus(HAND DeviceHandle, U16 LtcID, PU32 RemainCnt, PU32 SpaceCnt, PU32 LtcCounter)
```

##### Acm_DevResetLatchBuffer

```cpp
U32 Acm_DevResetLatchBuffer(HAND DeviceHandle, U16 LtcID)
```

##### Acm_DevSetLTCInAxisID

```cpp
U32 Acm_DevSetLTCInAxisID(HAND DeviceHandle, U16 LtcID, U32 AxisID)
```

##### Acm_DevGetLTCInAxisID

```cpp
U32 Acm_DevGetLTCInAxisID(HAND DeviceHandle, U16 LtcID, PU32 AxisID)
```

##### Acm_DevSetCmpAxisID

```cpp
U32 Acm_DevSetCmpAxisID(HAND DeviceHandle, U16 CmpID, U32 AxisID)
```

##### Acm_DevGetCmpAxisID

```cpp
U32 Acm_DevGetCmpAxisID(HAND DeviceHandle, U16 CmpID, PU32 AxisID)
```

##### Acm_GetDevNum

```cpp
U32 Acm_GetDevNum(U32 DevType,U32 BoardID,PU32 DeviceNumber)
```

##### Acm_DevSaveMapFile

```cpp
U32 Acm_DevSaveMapFile(HAND DeviceHandle, PI8 FilePath)
```

##### Acm_DevLoadMapFile

```cpp
U32 Acm_DevLoadMapFile(HAND DeviceHandle, PI8 FilePath)
```

##### Acm_DevUpLoadMapInfo

```cpp
U32 Acm_DevUpLoadMapInfo(HAND DeviceHandle, U16 MapType, PDEV_IO_MAP_INFO MapInfoArray, PU32 ArrayLength)
```

##### Acm_DevDownLoadMapInfo

```cpp
U32 Acm_DevDownLoadMapInfo(HAND DeviceHandle, U16 MapType, PDEV_IO_MAP_INFO MapInfoArray, U32 ArrayLength)
```

##### Acm_DevSetSlaveStates

```cpp
U32 Acm_DevSetSlaveStates(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 SlvState)
```

##### Acm_DevGetSlaveStates

```cpp
U32 Acm_DevGetSlaveStates(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PU16 SlvState)
```

##### Acm_DevGetSlaveTxPDO

```cpp
U32 Acm_DevGetSlaveTxPDO(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 StartOffset, U16 Length, PU8 DataArray)
```

##### Acm_DevGetSlaveRxPDO

```cpp
U32 Acm_DevGetSlaveRxPDO(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 StartOffset, U16 Length, PU8 DataArray)
```

##### Acm_DevWriteSDOComplete

```cpp
U32 Acm_DevWriteSDOComplete(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Index, U16 DataSize, PVOID pValue)
```

##### Acm_DevWriteSDOData

```cpp
U32 Acm_DevWriteSDOData(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Index, U16 SubIndex, U16 Type, U16 DataSize, PVOID pValue)
```

##### Acm_DevReadSDOData

```cpp
U32 Acm_DevReadSDOData(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Index, U16 SubIndex, U16 Type, U16 DataSize, PVOID pValue)
```

##### Acm_DevReadSDOData_Req
```cpp
U32 Acm_DevReadSDOData_Req(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize)
```

##### Acm_DevReadSDOData_Res
```cpp
U32 Acm_DevReadSDOData_Res(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize, OUT PVOID pValue)
```

##### Acm_DevWriteSDOData_Req
```cpp
U32 Acm_DevWriteSDOData_Req(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize, IN PVOID pValue)
```

##### Acm_DevWriteSDOData_Res
```cpp
U32 Acm_DevWriteSDOData_Res(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize)
```

##### Acm_DevReadMultiSDOData_Req
```cpp
U32 Acm_DevReadMultiSDOData_Req(HAND DeviceHandle, U16 RingNo, PMULTI_SDO_REQ Requests, U16 SDOCnt)
```

##### Acm_DevReadMultiSDOData_Res
```cpp
U32 Acm_DevReadMultiSDOData_Res(HAND DeviceHandle, U16 RingNo, PMULTI_SDO_REQ Requests, U16 SDOCnt)
```

##### Acm_DevWritePDOData
```cpp
U32 Acm_DevWritePDOData(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize, IN PVOID pValue)
```

##### Acm_DevReadPDOData
```cpp
U32 Acm_DevReadPDOData(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Index, IN U16 SubIndex, IN U16 Type, IN U16 DataSize, OUT PVOID pValue)
```

##### Acm_DevWriteRegData

```cpp
U32 Acm_DevWriteRegData(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Address, U16 Type, U16 DataSize, PVOID pValue)
```

##### Acm_DevReadRegData

```cpp
U32 Acm_DevReadRegData(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Address, U16 Type, U16 DataSize, PVOID pValue);
```

##### Acm_DevReadEmgMessage

```cpp
U32 Acm_DevReadEmgMessage(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 DataSize, PU8 EmgMessage);
```

##### Acm_DevReadSlvCommErrCnt

```cpp
U32 Acm_DevReadSlvCommErrCnt(HAND DeviceHandle, U16 RingNo, PU32 ErrCntArray, PU32 ArrayElements)
```

##### Acm_DaqLinkPDO

```cpp
U32 Acm_DaqLinkPDO(HAND DeviceHandle, PORT_TYPE Type, U16 Channel, U32 RingNo, U32 SlaveID, U32 EntryIndex, U32 EntrySubIndex);
```

##### Acm_AxMoveTorque

```cpp
U32 Acm_AxMoveTorque(HAND AxisHandle, F64 Distance, F64 Torque, F64 Velocity, F64 PressTime, U8 Mode)
```

##### Acm_AxGetActTorque

```cpp
U32 Acm_AxGetActTorque(HAND AxisHandle, PI32 Torque)
```

##### Acm_Ax2DCompensateInAx

```cpp
U32 Acm_Ax2DCompensateInAx(HAND AxisHandle, HAND RelAxisHandle, PF64 Coefficient, PF64 RelCoefficient, U32 ArrayElements)
```

##### Acm_Ax1DCompensateTable

```cpp
U32 Acm_Ax1DCompensateTable (HAND AxisHandle, F64 OriginPos, F64 Pitch, PF64 OffsetData, U32 OffsetElements, U32 Direction)
```

##### Acm_DevZAxisCompensateTable

```cpp
U32 Acm_DevZAxisCompensateTable(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, HAND ZAxisHandle, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataZ, U32 OffsetElementsX, U32 OffsetElementsY)
```

##### Acm_Dev2DCompensateTable

```cpp
U32 Acm_Dev2DCompensateTable(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataX, PF64 OffsetDataY, U32 OffsetElementsX, U32 OffsetElementsY)
```

##### Acm_AxGetCompensatePosition
```cpp
U32 Acm_AxGetCompensatePosition(HAND AxisHandle, PF64 Position)
```

##### Acm_AxZAxisCompensateTable
```cpp
U32 Acm_AxZAxisCompensateTable(HAND AxisHandle, HAND ZAxisHandle, F64 OriginPos, F64 Pitch, PF64 OffsetDataZ, U32 OffsetElementsZ, U32 Direction)
```

##### Acm_AxGetPreview1DCompensatePosition
```cpp
U32 Acm_AxGetPreview1DCompensatePosition(HAND AxisHandle, F64 Position, U32 Direction, PF64 PreviewPosition)
```

##### Acm_DevGetPreview2DCompensatePosition
```cpp
U32 Acm_DevGetPreview2DCompensatePosition(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, F64 Position, F64 RelPosition, U32 Direction, U32 RelDirection, PF64 PreviewPosition, PF64 PreviewRelPosition)
```

##### Acm_DevGetPreviewZAxisCompensatePosition
```cpp
U32 Acm_DevGetPreviewZAxisCompensatePosition(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, HAND ZAxisHandle, F64 Position, F64 RelPosition, U32 Direction, U32 RelDirection, PF64 PreviewZPosition)
```

##### Acm_DevMultiTrigInitial

```cpp
U32 Acm_DevMultiTrigInitial(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Enable, U8 PWM, U8 LTC, U8 MPG)
```

##### Acm_DevOscChannelDataStart
```cpp
U32 Acm_DevMultiTrigInitial(HAND DeviceHandle, IN U16 RingNo, IN U16 SlaveIP, IN U16 Enable, IN U8 PWM, IN U8 LTC, IN U8 MPG)
```

##### Acm_DevOscChannelDataStart
```cpp
U32 Acm_DevOscChannelDataStart(HAND DeviceHandle)
```

##### Acm_DevOscChannelDataStop
```cpp
U32 Acm_DevOscChannelDataStop(HAND DeviceHandle)
```

##### Acm_DevGetOscChannelDataConfig
```cpp
U32 Acm_DevGetOscChannelDataConfig(HAND DeviceHandle, U32 ChannelID, POSC_PROFILE_PRM oscflg)
```

##### Acm_DevSetOscChannelDataConfig
```cpp
U32 Acm_DevSetOscChannelDataConfig(HAND DeviceHandle, U32 ChannelID, OSC_PROFILE_PRM oscflg)
```

##### Acm_DevGetOscChannelData
```cpp
U32 Acm_DevGetOscChannelData(HAND DeviceHandle, U32 ChannelID, U32 DataIndex, PU32 MaxCount, PF64 DataBuffer)
```

##### Acm_DevGetOscChannelStatus
```cpp
U32 Acm_DevGetOscChannelStatus(HAND DeviceHandle, PU32 Status)
```

##### Acm_GpEnableAxisFollow
```cpp
U32 Acm_GpEnableAxisFollow(HAND GroupHandle, PU32 AxisArray, PF64 OffsetValue, PF64 RatioArray)
```

##### Acm_GpStopAxisFollow
```cpp
U32 Acm_GpStopAxisFollow(HAND GroupHandle)
```

##### Acm_GpSetFollowWpOffset
```cpp
U32 Acm_GpSetFollowWpOffset(HAND GroupHandle, PF64 WpCenterPos, PF64 WpOffset)
```

##### Acm_EnableOneDevEventCallBack
```cpp
U32 Acm_EnableOneDevEventCallBack(HANDLE DeviceHandle, ULONG EventID)
```

##### Acm_AxGetRawData
```cpp
U32 Acm_AxGetRawData(HAND AxisHandle, U8 index, PF64 RawData)
```

##### Acm_AxSetRawData
```cpp
U32 Acm_AxSetRawData(HAND AxisHandle, U8 index, F64 RawData)
```

##### Acm_AxReturnPausePosition
```cpp
U32 Acm_AxReturnPausePosition(HAND AxHandle)
```

##### Acm_AxAddOnAx
```cpp
U32 Acm_AxAddOnAx(HAND AxisHandle, HAND MasAxisHandle)
```

##### Acm_AxAddRemove
```cpp
U32 Acm_AxAddRemove(HAND AxisHandle, HAND MasAxisHandle)
```

##### Acm_AxGetAddOnNum
```cpp
U32 Acm_AxGetAddOnNum(HAND AxisHandle, PI32 num)
```

##### Acm_AxSetCompensateDistance
```cpp
U32 Acm_AxSetCompensateDistance(HAND AxisHandle, F64 Distance)
```

##### Acm_AxGetCompensateDistance
```cpp
U32 Acm_AxGetCompensateDistance(HAND AxisHandle, PF64 Distance)
```


---

## Common Motion API 2.0 (AdvCmnAPI_CM2)
##### Acm2_GetErrorMessage
Get error message.
```cpp
U32 Acm2_GetErrorMessage(U32 ErrorCode, PI8 lpszError, U32 nMaxError)
```

##### Acm2_DevInitialize
Initial the device.

```cpp
U32 Acm2_DevInitialize()
```

##### Acm2_GetAvailableDevs
Get all device list.
```cpp
U32 Acm2_GetAvailableDevs(DEVLIST *DeviceList, U32 MaxEntries, PU32 OutEntries)
```

##### Acm2_GetObjectCount
Get object count from object type
```cpp
U32 Acm2_GetObjectCount(ADV_OBJ_TYPE ObjType, PU32 ObjCnt)
```

##### Acm2_GetMappedPhysicalID
Get mapped physical id of device.

```cpp
U32 Acm2_GetMappedPhysicalID(ADV_OBJ_TYPE ObjType, U32 ObjLogicalID, PU32 DeviceNumber, PU32 ObjPhysicalID)
```

##### Acm2_GetMappedLogicalIDList
Get mapped list of logical id.

```cpp
U32 Acm2_GetMappedLogicalIDList(ADV_OBJ_TYPE ObjType, U32 DeviceLogicalID, PU32 LogicallIDList, PU32 ObjCnt)
```

##### Acm2_GetMappedObjInfo
Get mapped object information.

```cpp
U32 Acm2_GetMappedObjInfo(ADV_OBJ_TYPE ObjType, U32 ObjLogicalID, VOID *pObjInfo)
```

##### Acm2_DevAllClose
Close all device at same time.

```cpp
U32 Acm2_DevAllClose()
```
```python
## Example code
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST

number_hex = '0x63000000'
number_int = int(number_hex, 16)
device_number = c_uint32(number_int)
dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Close device
errCde = AdvMot.Acm2_DevAllClose()
```

##### Acm2_GetLastError
Get last error of system.

```cpp
U32 Acm2_GetLastError(ADV_OBJ_TYPE ObjType, U32 ObjLogicalID)
```

##### Acm2_GetProperty
Get device/axis property.

```cpp
U32 Acm2_GetProperty(U32 ObjID, U32 PropertyID, PF64 Value)
```
```python
## Example code
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()
do_ch = c_uint32(0)
property_id = c_uint(PropertyID2.CFG_CH_DaqDoFuncSelect.value)
val = c_double(1)
## Set local DO channel 0 as gerneral DO
errCde = AdvMot.Acm2_SetProperty(do_ch, property_id, val)
get_val = c_double(0)
## Get local DO channel 0 property value
errCde = AdvMot.Acm2_GetProperty(do_ch, property_id, byref(get_val))
```

##### Acm2_SetProperty
Set device/axis property.

```cpp
U32 Acm2_SetProperty(U32 ObjID, U32 PropertyID, F64 Value)
```

##### Acm2_SetMultiProperty
Set multiple properties at once.

```cpp
U32 Acm2_SetMultiProperty(U32 ObjID, PU32 PropertyID, PF64 Value, U32 Data_Cnt, PU32 ErrorBuffer)
```

##### Acm2_GetMultiProperty
Get multiple properties at once.

```cpp
U32 Acm2_GetMultiProperty(U32 ObjID, PU32 PropertyID, PF64 Value, U32 Data_Cnt, PU32 ErrorBuffer)
```
```python
## Example code
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()
## Set axis 0 speed info at once
ax_id = c_uint32(0)
property_arr = [c_uint32(PropertyID2.PAR_AxVelLow.value), c_uint32(PropertyID2.PAR_AxVelHigh.value)]
trans_ppt_arr = (c_uint32 * len(property_arr))(*property_arr)
## Default value of velocity low is 2000, and velocity high is 8000.
value_arr = [c_double(1000), c_double(2000)]
trans_val_arr = (c_double * len(value_arr))(*value_arr)
data_cnt = c_uint32(2)
err_buffer = (c_uint32 * data_cnt.value)()
## Set value
errCde = AdvMot.Acm2_SetMultiProperty(ax_id, trans_ppt_arr, trans_val_arr, data_cnt, err_buffer)
## Check value
get_val = (c_double * data_cnt.value)()
errCde = AdvMot.Acm2_GetMultiProperty(ax_id, trans_ppt_arr, get_val, data_cnt, err_buffer)
for i in range(data_cnt.value):
    print('set[{0}]:{1}, get:{2}'.format(i, value_arr[i].value, get_val[i]))
```

##### Acm2_GetRawProperty
Get raw property value.

```cpp
U32 Acm2_GetRawProperty(U32 ObjID, U32 PropertyID, PVOID Value, PU32 BufferLength)
```

##### Acm2_EnableCallBackFuncForOneEvent
Set callback function for event.

```cpp
U32 Acm2_EnableCallBackFuncForOneEvent(U32 ObjID, ADV_EVENT_SUBSCRIBE EventID, ADV_USER_CALLBACK_FUNC CallBackFun)
```
```python
import time
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotPropID_CM2 import PropertyID2

@CFUNCTYPE(c_uint32, c_uint32, c_void_p)
def EvtAxMotionDone(axid, reservedParam):
    ax_motion_cnt.value = ax_motion_cnt.value + 1;
    print('[EvtAxMotionDone] AX:{0}, counter:{1}'.format(axid, ax_motion_cnt.value))
    return 0;

@CFUNCTYPE(c_uint32, c_uint32, c_void_p)
def EmptyFunction(val, res):
    return 0;

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

ax_id = c_uint32(0)
abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
distance = c_double(1000)
ax_motion_cnt.value = 0
## Set callback function, enable event
errCde = AdvMot.Acm2_EnableCallBackFuncForOneEvent(ax_id, c_int(ADV_EVENT_SUBSCRIBE.AXIS_MOTION_DONE.value), EvtAxMotionDone)
## Move
for i range(2):
    errCde = AdvMot.Acm2_AxPTP(ax_id, abs_mode, distance)
    # Check status
    state = c_uint32(0)
    state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
    while (state.value != AXIS_STATE.STA_AX_READY.value):
        time.sleep(1)
        AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
time.sleep(1)
print('AX:{0} is done, event cnt is:{1}'.format(ax_id.value, ax_motion_cnt.value))
## Remove callback function, disable event
errCde = AdvMot.Acm2_EnableCallBackFuncForOneEvent(ax_id, c_int(ADV_EVENT_SUBSCRIBE.EVENT_DISABLE.value), EmptyFunction)
```


##### Acm2_DevLoadAllConfig
Load all configuration at once.

```cpp
U32 Acm2_DevLoadAllConfig(PI8 ConfigPath)
```

##### Acm2_DevLoadConfig
Load configuration.

```cpp
U32 Acm2_DevLoadConfig(U32 DevID, PI8 ConfigPath)
```

##### Acm2_DevReadMailBox
Read mailbox of device.

```cpp
U32 Acm2_DevReadMailBox(ADV_OBJ_TYPE ObjType, U32 ObjID, U32 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```

##### Acm2_DevWriteMailBox
Write mailbox of device.

```cpp
U32 Acm2_DevWriteMailBox(ADV_OBJ_TYPE ObjType, U32 ObjID, U32 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```

##### Acm2_GetErrors
Get error of device.

```cpp
U32 Acm2_GetErrors(U32 DevID, PVOID Error, PU32 ErrorCount)
```

##### Acm2_ResetErrorRecord
Reset error.

```cpp
U32 Acm2_ResetErrorRecord(U32 DevID)
```

##### Acm2_DevPreviewMotion
Preview motion.

```cpp
U32 Acm2_DevPreviewMotion(U32 DevID, PI8 InputFile, PI8 OutputFile, U16 NumberOfAxes)
```

##### Acm2_AxReturnPausePosition
Get axis pause position.

```cpp
U32 Acm2_AxReturnPausePosition(U32 AxID)
```

##### Acm2_AxSetSvOn
Set axis servo on/off.

```cpp
U32 Acm2_AxSetSvOn(U32 AxID, DO_ONOFF OnOff)
```

##### Acm2_DevSetAllSvOn
Set all axes servo on.off.

```cpp
U32 Acm2_DevSetAllSvOn(DO_ONOFF OnOff)
```

##### Acm2_AxSetErcOn
Set axis erc on/off.

```cpp
U32 Acm2_AxSetErcOn(U32 AxID, DO_ONOFF OnOff)
```

##### Acm2_AxResetAlm
Reset axis alarm logic.

```cpp
U32 Acm2_AxResetAlm(U32 AxID, DO_ONOFF OnOff)
```

##### Acm2_AxPTP
Set axis move with position.

```cpp
U32 Acm2_AxPTP(U32 AxID, ABS_MODE ptpMode, F64 Distance)
```

##### Acm2_AxMoveContinue
Set aixs continue move.

```cpp
U32 Acm2_AxMoveContinue(U32 AxID, MOTION_DIRECTION Direction)
```

##### Acm2_AxMotionStop
Force axis stop motion.

```cpp
U32 Acm2_AxMotionStop(PU32 AxisArray, U32 ArrayElements, MOTION_STOP_MODE StopMode, F64 NewDec)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

ax_id = c_uint32(0)
move_dir = c_uint(MOTION_DIRECTION.DIRECTION_POS.value)
errCde = AdvMot.Acm2_AxMoveContinue(ax_id, move_dir)
time.sleep(2)
ax_arr = [c_uint32(0)]
axArr = (c_uint32 * len(ax_arr))(*ax_arr)
stop_mode = c_uint(MOTION_STOP_MODE.MOTION_STOP_MODE_DEC.value)
new_dec = c_double(3000)
errCde = AdvMot.Acm2_AxMotionStop(axArr, len(ax_arr), stop_mode, new_dec)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis position
starting_pos = c_double(0)
pos = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
errCde = AdvMot.Acm2_AxGetPosition(ax_id, pos_type, byref(pos))
```

##### Acm2_AxHome
Set axis moving home with direction and home mode.

```cpp
U32 Acm2_AxHome(U32 AxID, HOME_MODE HomeMode, MOTION_DIRECTION Direction)
```

##### Acm2_AxMoveGantryHome
Set axis moving home with gantry.

```cpp
U32 Acm2_AxMoveGantryHome(U32 AxID, HOME_MODE HomeMode, MOTION_DIRECTION Direction)
```

##### Acm2_AxSetHomeSpeedProfile
Set axis home speed config.

```cpp
U32 Acm2_AxSetHomeSpeedProfile(U32 AxID, SPEED_PROFILE_PRM ProfileVel)
```

##### Acm2_AxChangePos
Set axis position.

```cpp
U32 Acm2_AxChangePos(U32 AxID, F64 NewPosition)
```

##### Acm2_AxChangeVel
Set axis velocity.

```cpp
U32 Acm2_AxChangeVel(U32 AxID, F64 NewVelocity, F64 NewAcc, F64 NewDec)
```

##### Acm2_AxChangeVelByRate
Set axis velocity by rate.

```cpp
U32 Acm2_AxChangeVelByRate(U32 AxID, U32 Rate, F64 NewAcc, F64 NewDec)
```

##### Acm2_AxMoveImpose
Set axis impose.

```cpp
U32 Acm2_AxMoveImpose(U32 AxID, F64 Position, F64 NewVelocity)
```

##### Acm2_AxResetError
Reset error of axis.

```cpp
U32 Acm2_AxResetError(U32 AxID)
```

##### Acm2_AxEnableTrig
```cpp
U32 Acm2_AxEnableTrig(U32 AxID, TRIG_PRM TrigPrm)
```

##### Acm2_DevResetAllError
Reset all device error.

```cpp
U32 Acm2_DevResetAllError()
```
```python
## Example code
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()
## Clear all error
errCde = AdvMot.Acm2_DevResetAllError()

ax_id = c_uint32(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
pos = c_double(0)
## Set axis 0 command position as 0
errCde = AdvMot.Acm2_AxSetPosition(ax_id, pos_type, pos)
```

##### Acm2_DevCheckAllAxReady
Check whether axes are ready
```cpp
U32 Acm2_DevCheckAllAxReady(U32 Timeout)
```

##### Acm2_AxGetState
Get axis state.

```cpp
U32 Acm2_AxGetState(U32 AxID, AXIS_STATUS_TYPE StatusType, PU32 State)
```
```python
## Example code
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotDrv import POSITION_TYPE, ABS_MODE, AXIS_STATUS_TYPE

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()
axid = c_uint32(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
pos = c_double(0)
distance = c_double(1000)
abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
state = c_uint32(16)
## Get axis 0 command position
errCde = AdvMot.Acm2_AxGetPosition(axid, pos_type, byref(pos))
## Move axis 0 to position 1000(command position)
errCde = AdvMot.Acm2_AxPTP(axid, abs_mode, distance)
## Check axis 0 status
errCde = AdvMot.Acm2_AxGetState(axid, state_type, byref(state))
```

##### Acm2_AxGetMotionIO
Get axis motion IO status.

```cpp
U32 Acm2_AxGetMotionIO(U32 AxID, MOTION_IO *Status)
```

##### Acm2_AxSetPosition
Set axis position.

```cpp
U32 Acm2_AxSetPosition(U32 AxID, POSITION_TYPE PosType, F64 Position)
```

##### Acm2_DevSetAllPosition
Set axes position
```cpp
U32 Acm2_DevSetAllPosition(POSITION_TYPE PosType, F64 Position)
```

##### Acm2_AxGetPosition
Get axis position by axis number, and position type.

```cpp
U32 Acm2_AxGetPosition(U32 AxID, POSITION_TYPE PosType, PF64 Position)
```
```python
## Example code
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotDrv import POSITION_TYPE

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()
axid = c_uint32(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
pos = c_double(0)
## Get axis 0 command position
errCde = AdvMot.Acm2_AxGetPosition(axid, pos_type, byref(pos))
```

##### Acm2_AxGetMachPosition
```cpp
U32 Acm2_AxGetMachPosition(U32 AxID, PF64 Position)
```

##### Acm2_AxSetSpeedProfile
Set axis speed information.

```cpp
U32 Acm2_AxSetSpeedProfile(U32 AxID, SPEED_PROFILE_PRM ProfileVel)
```
```python
## Example code
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

ax_id = c_uint32(0)
speed_info = SPEED_PROFILE_PRM()
speed_info.FH = c_double(3000)
speed_info.FL = c_double(1500)
speed_info.Acc = c_double(11000)
speed_info.Dec = c_double(9900)
speed_info.JerkFac = c_double(0)
## Set speed information
errCde = AdvMot.Acm2_AxSetSpeedProfile(ax_id, speed_info)
```

##### Acm2_AxGetVel
Get axis current velocity.

```cpp
U32 Acm2_AxGetVel(U32 AxID, VELOCITY_TYPE VelType, PF64 Velocity)
```
```python
## Example code
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotDrv import VELOCITY_TYPE

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

ax_id = c_uint32(0)
get_vel = c_double(0)
vel_Type = c_uint(VELOCITY_TYPE.VELOCITY_CMD.value)
## Get axis 0 current velocity
errCde = AdvMot.Acm2_AxGetVel(ax_id, vel_Type, byref(get_vel))
```

##### Acm2_AxEnableExternalMode
Enable axis external mode.

```cpp
U32 Acm2_AxEnableExternalMode(U32 AxID, EXT_DRIVE_MODE ExtDrvMode)
```

##### Acm2_AxDownloadTorqueTable
```cpp
U32 Acm2_AxDownloadTorqueTable(U32 AxID, PF64 PositionArray, PF64 TorqueArray, U32 ArrayElements)
```

##### Acm2_AxLoadTorqueTableFile
```cpp
U32 Acm2_AxLoadTorqueTableFile(U32 AxID, PI8 FilePath, PU32 PointsCount)
```

##### Acm2_AxMoveTorque
```cpp
U32 Acm2_AxMoveTorque(U32 AxID, F64 Distance, F64 Torque, F64 TorqueSlope, F64 Velocity, F64 PressTime, U32 Mode)
```

##### Acm2_AxGetActTorque
```cpp
U32 Acm2_AxGetActTorque(U32 AxID, PF64 Torque)
```

##### Acm2_AxSoftJog
Set axis jog.

```cpp
U32 Acm2_AxSoftJog(U32 AxID, MOTION_DIRECTION Direction)
```

##### Acm2_AxSetJogSpeedProfile
Set axis jog speed information.

```cpp
U32 Acm2_AxSetJogSpeedProfile(U32 AxID, JOG_SPEED_PROFILE_PRM ProfileVel)
```
```python
## Example code
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

ax_id = c_uint32(0)
jog_speed_info = JOG_SPEED_PROFILE_PRM()
jog_speed_info.FH = c_double(8000)
jog_speed_info.FL = c_double(1000)
jog_speed_info.Acc = c_double(10000)
jog_speed_info.Dec = c_double(5000)
jog_speed_info.VLTime = c_double(2000)
## Set axis 0 jog speed information
errCde = AdvMot.Acm2_AxSetJogSpeedProfile(ax_id, jog_speed_info)
```

##### Acm2_AxMotionStart
Start motion.

```cpp
U32 Acm2_AxMotionStart(PU32 AxisArray, U32 ArrayElements)
```

##### Acm2_AxPause
Pause motion.

```cpp
U32 Acm2_AxPause(U32 AxID)
```

##### Acm2_AxResume
Resume motion.

```cpp
U32 Acm2_AxResume(U32 AxID)
```

##### Acm2_AxResetPVTTable
Reset axis PVT table.

```cpp
U32 Acm2_AxResetPVTTable(U32 AxID)
```

##### Acm2_AxLoadPVTTable
Load axis PVT table.

```cpp
U32 Acm2_AxLoadPVTTable(U32 AxID, PF64 Position, PF64 Velocity, PF64 Time, U32 ArrayElements)
```

##### Acm2_AxCalculatePVTTableContinuous
```cpp
U32 Acm2_AxCalculatePVTTableContinuous(U32 AxID, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, U32 ArrayElements, PF64 Time)
```

##### Acm2_AxLoadPVTTableContinuous
Continuous loading PVT table.

```cpp
U32 Acm2_AxLoadPVTTableContinuous(U32 AxID, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, F64 TimeDelay, U32 ArrayElements)
```

##### Acm2_AxMovePVT
Move PVT motion.

```cpp
U32 Acm2_AxMovePVT(U32 AxID)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

ax_id = c_uint32(0)
## Reset PVT table
errCde = AdvMot.Acm2_AxResetPVTTable(ax_id)
''' PVT table
|Position|Vel |Time|
|--------|----|----|
|0       |0   |0   |
|5000    |4000|2000|
|15000   |5000|3000|
|30000   |8000|4000|
'''
pos_arr = [c_double(0), c_double(5000), c_double(15000), c_double(30000)]
posArr = (c_double * len(pos_arr))(*pos_arr)
vel_arr = [c_double(0), c_double(4000), c_double(5000), c_double(8000)]
velArr = (c_double * len(vel_arr))(*vel_arr)
time_arr = [c_double(0), c_double(2000), c_double(3000), c_double(4000)]
timeArr = (c_double * len(time_arr))(*time_arr)
## Set table of PVT
errCde = AdvMot.Acm2_AxLoadPVTTable(ax_id, posArr, velArr, timeArr, len(pos_arr))
## Set PVT
errCde = AdvMot.Acm2_AxMovePVT(ax_id)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
get_pos = c_double(0)
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
## Get axis 0 state
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Check axis 0 is ready
if (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(ax_id, pos_type, byref(get_pos))
```

##### Acm2_AxCheckPTBuffer
Check axis PT buffer.

```cpp
U32 Acm2_AxCheckPTBuffer(U32 AxID, PU32 Freespace)
```

##### Acm2_AxAddPTData
Add axis PT data.

```cpp
U32 Acm2_AxAddPTData(U32 AxID, F64 Position, F64 Time)
```

##### Acm2_AxMovePT
Move PT motion.

```cpp
U32 Acm2_AxMovePT(U32 AxID)
```

##### Acm2_AxResetPTData
Reset axis PT data.

```cpp
U32 Acm2_AxResetPTData(U32 AxID)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

ax_id = c_uint32(0)
## Reset PT table
errCde = AdvMot.Acm2_AxResetPTData(ax_id)
''' PT table
|Position|Time|
|--------|----|
|0       |0   |
|5000    |2000|
|15000   |3000|
|30000   |5000|
'''
pos_arr = [c_double(0), c_double(5000), c_double(15000), c_double(30000)]
time_arr = [c_double(0), c_double(2000), c_double(3000), c_double(5000)]
## Set PT table
for i range(len(pos_arr)):
    errCde = AdvMot.Acm2_AxAddPTData(ax_id, pos_arr[i], time_arr[i])
## Start move PT table
errCde = AdvMot.Acm2_AxMovePT(ax_id)

pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
get_pos = c_double(0)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(ax_id, pos_type, byref(get_pos))
```

##### Acm2_AxGearIn
Set axis gear.

```cpp
U32 Acm2_AxGearIn(U32 PrimaryAxisID, U32 FollowingAxisID, GEAR_IN_PRM GearInParameter)
```

##### Acm2_AxTangentInGp
```cpp
U32 Acm2_AxTangentInGp(U32 AxID, U32	PrimaryGpID, TANGENT_IN_PRM	TangentInParameter)
```

##### Acm2_AxGantryIn
Set axis gantry.

```cpp
U32	Acm2_AxGantryIn(U32	PrimaryAxisID, U32 FollowingAxisID, GANTRY_IN_PRM GantryInParameter)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

primary_ax = c_uint32(0)
follow_ax = c_uint32(1)
## Reset following axis
errCde = AdvMot.Acm2_AxSyncOut(follow_ax)
## Set gantry parameter
gantry_param = GANTRY_IN_PRM()
## Set gantry reference source as command position
gantry_param.RefSrc = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Set gantry direction as positive
gantry_param.Direction = c_uint(MOTION_DIRECTION.DIRECTION_POS.value)
## Set gantry
errCde = AdvMot.Acm2_AxGantryIn(primary_ax, follow_ax, gantry_param)
## Move primary axis
abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
distance = c_double(10000)
errCde = AdvMot.Acm2_AxPTP(primary_ax, abs_mode, distance)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 (primary) position
errCde = AdvMot.Acm2_AxGetPosition(primary_ax, pos_type, byref(get_pos_0))
## Get axis 1 (following) position
errCde = AdvMot.Acm2_AxGetPosition(follow_ax, pos_type, byref(get_pos_1))
## Reset following axis
errCde = AdvMot.Acm2_AxSyncOut(follow_ax)
```

##### Acm2_AxPhaseAx
Set axis phase.

```cpp
U32 Acm2_AxPhaseAx(U32 AxID, PHASE_AXIS_PRM PhaseAxParameter)
```

##### Acm2_AxSyncOut
Lift the gantry.

```cpp
U32 Acm2_AxSyncOut(U32 FollowingAxisID)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

primary_ax = c_uint32(0)
follow_ax = c_uint32(1)
## Reset following axis
errCde = AdvMot.Acm2_AxSyncOut(follow_ax)
gear_param = GEAR_IN_PRM()
## Position type as command position
gear_param.RefSrc = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Mode as relative mode
gear_param.Mode = c_uint32(0)
## Set gear ratio
gear_param.GearPosition = c_double(0)
gear_param.GearRatioRate.Num = c_double(1)
gear_param.GearRatioRate.Den = c_double(1)
## Set gear
errCde = AdvMot.Acm2_AxGearIn(primary_ax, follow_ax, gear_param)
## Move primary axis
abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
distance = c_double(10000)
errCde = AdvMot.Acm2_AxPTP(primary_ax, abs_mode, distance)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 (primary) position
errCde = AdvMot.Acm2_AxGetPosition(primary_ax, pos_type, byref(get_pos_0))
## Get axis 1 (following) position
errCde = AdvMot.Acm2_AxGetPosition(follow_ax, pos_type, byref(get_pos_1))
## Reset following axis
errCde = AdvMot.Acm2_AxSyncOut(follow_ax)
```

##### Acm2_GpGetPausePosition
Get group pause position.

```cpp
U32 Acm2_GpGetPausePosition(U32 GpID, PF64 PosArray)
```

##### Acm2_GpCreate
Create group.

```cpp
U32 Acm2_GpCreate(U32 GpID, PU32 AxisArray, U32 ArrayElements)
```

##### Acm2_GpGetAxesInGroup
Check axes group.

```cpp
U32 Acm2_GpGetAxesInGroup(U32 GpID, PU32 AxisArray, PU32 ArrayElements)
```

##### Acm2_GpUpdate
```cpp
U32 Acm2_GpUpdate(U32 GpID)
```

##### Acm2_GpResetError
Reset error of group.

```cpp
U32 Acm2_GpResetError(U32 GpID)
```

##### Acm2_GpEnableTrig
```cpp
U32 Acm2_GpEnableTrig(U32 GpID, TRIG_PRM TrigPrm)
```

##### Acm2_GpLine
Move group line.

```cpp
U32 Acm2_GpLine(U32 GpID, GP_LINE_MODE LineMode, PF64 EndArray, PU32 ArrayElements)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
## Set group move as relative
gp_move_mode = c_uint(GP_LINE_MODE.LINE_REL.value)
## Set group end position: axis(0) = 10000, axis(1) = 10000
end_pos_arr = [c_double(10000), c_double(10000)]
arr_element = c_uint32(len(end_pos_arr))
end_arr = (c_double * len(end_pos_arr))(*end_pos_arr)
## Group 0 move line
errCde = AdvMot.Acm2_GpLine(gp_id, gp_move_mode, end_arr, byref(arr_element))
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 (primary) position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 (following) position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_GpArc_Center
Set group arc center.

```cpp
U32 Acm2_GpArc_Center(U32  GpID, ABS_MODE ArcMode, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION  Direction)
```
```python
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
## Set 2D Arc mode
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
## Set 2D Arc CW center, end position
'''
| axis | Arc center | Arc end |
|------|------------|---------|
|   0  |    8000    |  16000  |
|   1  |      0     |    0    |
'''
center_ax_arr = [c_double(8000), c_double(0)]
center_arr = (c_double * len(center_ax_arr))(*center_ax_arr)
end_ax_arr = [c_double(16000), c_double(0)]
end_arr = (c_double * len(end_ax_arr))(*end_ax_arr)
arr_element = c_uint32(len(end_ax_arr))
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
errCde = AdvMot.Acm2_GpArc_Center(gp_id, arc_mode, center_arr, end_arr, byref(arr_element), dir_mode)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_GpArc_3P
Set group arc point.

```cpp
U32 Acm2_GpArc_3P(U32 GpID, ABS_MODE ArcMode, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION Direction)
```
```python
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
## # Set 2D Arc mode as relative, which the starting point of circular is (0, 0)
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
## Set 2D Arc CW center, end position
'''
| axis | point 1 | end point |
|------|---------|-----------|
| 0(x) |   8000  |   16000   |
| 1(y) |   8000  |     0     |
'''
ref_arr = [c_double(8000), c_double(8000)]
refArr = (c_double * len(ref_arr))(*ref_arr)
end_arr = [c_double(16000), c_double(0)]
endArr = (c_double * len(end_arr))(*end_arr)
arr_element = c_uint32(len(ref_arr))
## Set arc movement as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
errCde = AdvMot.Acm2_GpArc_3P(gp_id, arc_mode, refArr, endArr, byref(arr_element), dir_mode)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_GpArc_Angle
Set group arc angle.

```cpp
U32 Acm2_GpArc_Angle(U32 GpID, ABS_MODE ArcMode, PF64 CenterArray, PU32 pArrayElements, F64 Degree, ARC_DIRECTION Direction)
```
```python
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
## Set 2D Arc mode as relative, which the starting point of circular is (0, 0)
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
## Set center as (20000, 20000)
center_arr = [c_double(20000), c_double(20000)]
centerArr = (c_double * len(center_arr))(*center_arr)
arr_element = c_uint32(len(center_arr))
## Set degree as 45
degree = c_double(45)
## Set arc movement as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
errCde = AdvMot.Acm2_GpArc_Angle(gp_id, arc_mode, centerArr, byref(arr_element), degree, dir_mode)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_Gp3DArc_Center
Set 3D group arc center.

```cpp
U32 Acm2_Gp3DArc_Center(U32 GpID, ABS_MODE ArcMode, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION  Direction)
```
```python
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
## Set 3D Arc mode
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
## Set 3D Arc CW, with 120 degree
'''
| axis | Arc center | Arc end |
|------|------------|---------|
|   0  |    20000   |  20000  |
|   1  |    20000   |  40000  |
|   2  |      0     |  20000  |
'''
center_ax_arr = [c_double(20000), c_double(20000), c_double(0)]
center_arr = (c_double * len(center_ax_arr))(*center_ax_arr)
end_ax_arr = [c_double(20000), c_double(40000), c_double(20000)]
end_arr = (c_double * len(end_ax_arr))(*end_ax_arr)
arr_element = c_uint32(len(end_ax_arr))
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
errCde = AdvMot.Acm2_Gp3DArc_Center(gp_id, arc_mode, center_arr, end_arr, byref(arr_element), dir_mode)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_Gp3DArc_NormVec
Set 3D group arc norm vector.

```cpp
U32 Acm2_Gp3DArc_NormVec(U32 GpID, ABS_MODE ArcMode, PF64 CenterArray, PF64 NormalVec, PU32 pArrayElements, F64  Angle, ARC_DIRECTION Direction)
```
```python
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
## Set 3D Arc mode
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
## Set direction as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
## Set 3D Arc CW, with 120 degree
'''
| axis | Arc center | Arc end |
|------|------------|---------|
|   0  |    20000   |  20000  |
|   1  |    20000   |  40000  |
|   2  |      0     |  20000  |
'''
center_arr = [c_double(20000), c_double(20000), c_double(0)]
centerArr = (c_double * len(center_arr))(*center_arr)
v1 = np.array([(0-center_arr[0].value), (0-center_arr[1].value), (0-center_arr[2].value)])
arc_end_arr = [c_double(20000), c_double(40000), c_double(20000)]
v2 = np.array([(arc_end_arr[0].value-center_arr[0].value), (arc_end_arr[1].value-center_arr[1].value), (arc_end_arr[2].value-center_arr[2].value)])
cross_product = np.cross(v1, v2)
normalize_cross = cross_product / (center_arr[0].value * center_arr[0].value)
norm_vec_arr = [c_double(normalize_cross[0]), c_double(normalize_cross[1]), c_double(normalize_cross[2])]
normVecArr = (c_double * len(norm_vec_arr))(*norm_vec_arr)
arr_element = c_uint32(len(center_arr))
angle = c_double(120)
errCde = AdvMot.Acm2_Gp3DArc_NormVec(gp_id, arc_mode, centerArr, normVecArr, byref(arr_element), angle, dir_mode)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_Gp3DArc_3P
Set arc movement with 3 points of circular.

```cpp
U32 Acm2_Gp3DArc_3P(U32 GpID, ABS_MODE ArcMode, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION  Direction, U32 cycCount)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
## # Set 3D Arc mode as relative, which the starting point of circular is (0, 0, 0)
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
## Set 3D Arc CW, with 120 degree
'''
| axis | point 1 | end point |
|------|---------|-----------|
| 0(x) |  20000  |   20000   |
| 1(y) |  20000  |   40000   |
| 2(z) |    0    |   20000   |
'''
ref_arr = [c_double(20000), c_double(20000), c_double(0)]
refArr = (c_double * len(ref_arr))(*ref_arr)
end_arr = [c_double(20000), c_double(40000), c_double(20000)]
endArr = (c_double * len(end_arr))(*end_arr)
arr_element = c_uint32(len(ref_arr))
## Set direction as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
cyc_cnt = c_uint32(0)
## Set arc movement with 3 points of circular
errCde = AdvMot.Acm2_Gp3DArc_3P(gp_id, arc_mode, refArr, endArr, byref(arr_element), dir_mode, cyc_cnt)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_Gp3DArc_3PAngle
Set 3D group arc points, angle.

```cpp
U32 Acm2_Gp3DArc_3PAngle(U32 GpID, ABS_MODE ArcMode, PF64 RefPoint_1, PF64 RefPoint_2, PU32 pArrayElements, F64 Degree, ARC_DIRECTION Direction)
```
```python
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
## # Set 3D Arc mode as relative, which the starting point of circular is (0, 0, 0)
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
## Set direction as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
## Set 3D Arc CW, with 120 degree
'''
| axis | point 1 | end point |
|------|---------|-----------|
| 0(x) |  20000  |   20000   |
| 1(y) |  20000  |   40000   |
| 2(z) |    0    |   20000   |
'''
ref_arr = [c_double(20000), c_double(20000), c_double(0)]
refArr = (c_double * len(ref_arr))(*ref_arr)
end_arr = [c_double(20000), c_double(40000), c_double(20000)]
endArr = (c_double * len(end_arr))(*end_arr)
arr_element = c_uint32(len(ref_arr))
degree = c_double(120)
## Set arc movement with 3 point of circular
errCde = AdvMot.Acm2_Gp3DArc_3PAngle(gp_id, arc_mode, refArr, endArr, byref(arr_element), degree, dir_mode)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
## Check value
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_GpHelix_Center
Set group helix center.

```cpp
U32 Acm2_GpHelix_Center(U32 GpID, ABS_MODE HelixMode, PF64 CenterArray, PF64 EndArray, PU32	pArrayElements, ARC_DIRECTION Direction)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
## Set mode as relative
helix_mode = c_uint(ABS_MODE.MOVE_REL.value)
## Set center as (10000, 0, 0)
center_arr = [c_double(10000), c_double(0), c_double(0)]
centerArr = (c_double * len(center_arr))(*center_arr)
## Set end position as (20000, 0, 20000)
end_arr = [c_double(20000), c_double(0), c_double(20000)]
endArr = (c_double * len(end_arr))(*end_arr)
arr_element = c_uint32(len(end_arr))
## Set direction as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
## Set Helix movement
errCde = AdvMot.Acm2_GpHelix_Center(gp_id, helix_mode, centerArr, endArr, byref(arr_element), dir_mode)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
## Check value
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_GpHelix_3P
Set group helix points.

```cpp
U32 Acm2_GpHelix_3P(U32 GpID, ABS_MODE HelixMode, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION Direction)
```
```python
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
## Set mode as relative
helix_mode = c_uint(ABS_MODE.MOVE_REL.value)
## Set center as (8000, 0, 0)
center_arr = [c_double(8000), c_double(0), c_double(0)]
centerArr = (c_double * len(center_arr))(*center_arr)
## Set end position as (16000, 16000, 10000)
end_arr = [c_double(16000), c_double(16000), c_double(10000)]
endArr = (c_double * len(end_arr))(*end_arr)
arr_element = c_uint32(len(center_arr))
## Set direction as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
## Set Helix movement
errCde = AdvMot.Acm2_GpHelix_3P(gp_id, helix_mode, centerArr, endArr, byref(arr_element), dir_mode)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
## Check value
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_GpHelix_Angle
Set group helix angle.

```cpp
U32 Acm2_GpHelix_Angle(U32 GpID, ABS_MODE HelixMode, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION Direction)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
## Set mode as relative
helix_mode = c_uint(ABS_MODE.MOVE_REL.value)
## Set center as (200, 0)
center_arr = [c_double(200), c_double(0), c_double(0)]
centerArr = (c_double * len(center_arr))(*center_arr)
## Set 120 as degree
end_arr = [c_double(4000), c_double(4000), c_double(120)]
endArr = (c_double * len(end_arr))(*end_arr)
arr_element = c_uint32(len(center_arr))
## Set direction as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
## Set Helix movement
errCde = AdvMot.Acm2_GpHelix_Angle(gp_id, helix_mode, centerArr, endArr, byref(arr_element), dir_mode)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
## Check value
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_GpResume

```cpp
U32 Acm2_GpResume(U32 GpID)
```

##### Acm2_GpPause
Set group pause motion.

```cpp
U32 Acm2_GpPause(U32 GpID)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
for idx range(len_get.value):
## Set mode as relative
move_mode = c_uint(GP_LINE_MODE.LINE_REL.value)
end_arr = [c_double(20000), c_double(20000), c_double(20000)]
endArr = (c_double * len(end_arr))(*end_arr)
arr_element = c_uint32(len(end_arr))
errCde = AdvMot.Acm2_GpLine(gp_id, move_mode, endArr, arr_element)
## Pause movement
errCde = AdvMot.Acm2_GpPause(gp_id)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
## Check value: Not equal to target position
## Resume movement
errCde = AdvMot.Acm2_GpResume(gp_id)
## Check status
while state.value != AXIS_STATE.STA_AX_READY.value:
    time.sleep(1)
    test_GetAxState()
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
## Check value: Equal to target position
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_GpMotionStop
Stop group motion.

```cpp
U32 Acm2_GpMotionStop(U32 GpID, MOTION_STOP_MODE StopMode, F64 NewDec)
```

##### Acm2_GpChangePos
```cpp
U32 Acm2_GpChangePos(U32 GpID, ABS_MODE Mode, PF64 DistanceArray, PU32 ArrayElements)
```

##### Acm2_GpChangeVel
Change velocity of group.

```cpp
U32 Acm2_GpChangeVel(U32 GpID, F64 NewVelocity, F64 NewAcc, F64 NewDec)
```

##### Acm2_GpChangeVelByRate
Change group velocity by rate.

```cpp
U32 Acm2_GpChangeVelByRate(U32 GpID, U32 Rate, F64 NewAcc, F64 NewDec)
```

##### Acm2_GpGetVel
Get group velocity.

```cpp
U32 Acm2_GpGetVel(U32 GpID, VELOCITY_TYPE VelType, PF64 Velocity)
```
```python
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
for idx range(len_get.value):
## Set mode as relative
move_mode = c_uint(GP_LINE_MODE.LINE_REL.value)
end_arr = [c_double(200000), c_double(200000), c_double(200000)]
endArr = (c_double * len(end_arr))(*end_arr)
arr_element = c_uint32(len(end_arr))
errCde = AdvMot.Acm2_GpLine(gp_id, move_mode, endArr, arr_element)
## Check group status
time.sleep(2)
gp_state = c_uint32(0)
errCde = AdvMot.Acm2_GpGetState(gp_id, byref(gp_state))
print('gp_state:0x{0:x}'.format(gp_state.value))
## Change velocity
new_vel = c_double(5000)
new_acc = c_double(9000)
new_dec = c_double(4000)
errCde = AdvMot.Acm2_GpChangeVel(gp_id, new_vel, new_acc, new_dec)
vel_type = c_uint(VELOCITY_TYPE.VELOCITY_CMD.value)
get_gp_vel = c_double(0)
time.sleep(2)
errCde = AdvMot.Acm2_GpGetVel(gp_id, vel_type, byref(get_gp_vel))
print('gp vel:{0}'.format(get_gp_vel.value))
## Set stop mode as deceleration to stop
stop_mode = c_uint(MOTION_STOP_MODE.MOTION_STOP_MODE_DEC.value)
errCde = AdvMot.Acm2_GpMotionStop(gp_id, stop_mode, new_dec)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
## Check value: Not equal to target position
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_GpSetSpeedProfile
Get group speed information.

```cpp
U32 Acm2_GpSetSpeedProfile(U32 GpID, SPEED_PROFILE_PRM ProfileVel)
```

##### Acm2_GpGetState
Get group status.

```cpp
U32 Acm2_GpGetState(U32 GpID, PU32 State)
```

##### Acm2_GpLoadPath
Load path table group.

```cpp
U32 Acm2_GpLoadPath(U32 GpID, PI8 FilePath, PU32 TotalCount)
```

##### Acm2_GpAddPath
Add path into group.

```cpp
U32 Acm2_GpAddPath(U32 GpID, U32 MoveCmd, PATH_MOVE_MODE_CM2 MoveMode, F64 FH, F64 FL, F64 Acc, F64 Dec, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)
```

##### Acm2_GpMovePath
Start move group after add path.

```cpp
U32 Acm2_GpMovePath(U32 GpID)
```

##### Acm2_GpResetPath
Reset group path table.

```cpp
U32 Acm2_GpResetPath(U32 GpID)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
for idx range(len_get.value):
## Reset group path
errCde = AdvMot.Acm2_GpResetPath(gp_id)
## Set 2D Arc CW center, end position
'''
| axis | Arc center | Arc end |
|------|------------|---------|
|   0  |    8000    |  16000  |
|   1  |      0     |    0    |
'''
## Set path table
'''
| index | move command | move mode | Vel High | Vel Low | Acc | Dec |   End Point  | Center Point |
|-------|--------------|-----------|----------|---------|-----|-----|--------------|--------------|
|   0   |  Rel2DArcCCW |BUFFER_MODE|   8000   |   1000  |10000|10000|(16000, 16000)| (8000, 8000) |
|   1   |    EndPath   |BUFFER_MODE|     0    |     0   |  0  |  0  |       0      |      0       |
'''
move_cmd_arr = [c_uint32(MOTION_PATH_CMD.Rel2DArcCCW.value), c_uint32(MOTION_PATH_CMD.EndPath.value)]
move_mode = c_uint(PATH_MOVE_MODE_CM2.BUFFER_MODE.value)
fh = [c_double(8000), c_double(0)]
fl = [c_double(1000), c_double(0)]
acc = [c_double(10000), c_double(0)]
dec = [c_double(10000), c_double(0)]
end_arr = [
    [c_double(16000), c_double(16000)], 
    [c_double(0), c_double(0)]
]
center_arr = [
    [c_double(8000), c_double(8000)], 
    [c_double(0), c_double(0)]
]
arr_element = c_uint32(len(end_arr[0]))
for i range(1):
    endArr = (c_double * len(end_arr[i]))(*end_arr[i])
    centerArr = (c_double * len(center_arr[i]))(*center_arr[i])
    errCde = AdvMot.Acm2_GpAddPath(gp_id, move_cmd_arr[i], move_mode, fh[i], fl[i], acc[i], dec[i], endArr, centerArr, arr_element)
## Start move path
errCde = AdvMot.Acm2_GpMovePath(gp_id)
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Check value: Equal to target position
## Reset group path
errCde = AdvMot.Acm2_GpResetPath(gp_id)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_GpGetPathStatus
Get group path status.

```cpp
U32 Acm2_GpGetPathStatus(U32 GpID, PATH_STATUS *pathStatus)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
## Creat group 0, and set axis 0, 1 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
## get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
## Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
for idx range(len_get.value):
## Reset group path
errCde = AdvMot.Acm2_GpResetPath(gp_id)
## Create path file by path editor inside the Utility
path_bin_file = b'test\\testPath.bin'
'''
| index | move command | move mode | Vel High | Vel Low | Acc | Dec |   End Point  |
|-------|--------------|-----------|----------|---------|-----|-----|--------------|
|   0   |   Rel2DLine  |BUFFER_MODE|   8000   |   1000  |10000|10000|(10000, 10000)|
|   1   |   Rel2DLine  |BUFFER_MODE|   8000   |   1000  |10000|10000|(10000, 10000)|
|   2   |    EndPath   |BUFFER_MODE|     0    |     0   |  0  |  0  |       0      |
'''
cnt = c_uint32(0)
errCde = AdvMot.Acm2_GpLoadPath(gp_id, path_bin_file, byref(cnt))
## Start move path
errCde = AdvMot.Acm2_GpMovePath(gp_id)
path_status = c_uint(0)
errCde = AdvMot.Acm2_GpGetPathStatus(gp_id, byref(path_status))
## Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
## Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
## Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
## Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
## Check value: Equal to target position
## Reset group path
errCde = AdvMot.Acm2_GpResetPath(gp_id)
## Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```

##### Acm2_GpMoveSelPath

```cpp
U32 Acm2_GpMoveSelPath(U32 GpID, U32 StartIndex, U32 EndIndex, U32 Repeat)
```

##### Acm2_GpGetPathIndexStatus
Get group information by the index of path table.

```cpp
U32 Acm2_GpGetPathIndexStatus(U32 GpID, U32 Index, PU32 CmdFunc, PU32 MoveMode, PF64 FH, PF64 FL, PF64 Acc, PF64 Dec, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)
```

##### Acm2_GpDelay
Delay group.

```cpp
U32 Acm2_GpDelay(U32 GpID, U32 DelayTime)
```

##### Acm2_GpPathDO
Set device do on/off between path.

```cpp
U32 Acm2_GpPathDO(U32 GpID, PATH_DO_PRM  PathDOPrm)
```

##### Acm2_GpPathWaitDI
Wait DI status between path.

```cpp
U32 Acm2_GpPathWaitDI(U32 GpID, PATH_DI_WAIT_PRM DIWaitPrm)
```

##### Acm2_GpPathWaitForAxis
Wait axis between path.

```cpp
U32 Acm2_GpPathWaitForAxis(U32 GpID, PATH_AX_WAIT_PRM AxWaitPrm)
```

##### Acm2_GpPathDIConditional
```cpp
U32 Acm2_GpPathDIConditional(U32 GpID, U32 MoveCmd, PATH_DI_WAIT_PRM PathDIPrm)
```

##### Acm2_GpPathDOConditional
```cpp
U32 Acm2_GpPathDOConditional(U32 GpID, U32 MoveCmd, PATH_DO_PRM PathDOPrm)
```

##### Acm2_GpPathAxisConditional
```cpp
U32 Acm2_GpPathAxisConditional(U32 GpID, U32 MoveCmd, PATH_AX_WAIT_PRM AxWaitPrm)
```

##### Acm2_GpPathVarConditional
```cpp
U32 Acm2_GpPathVarConditional(U32 GpID, U32 MoveCmd, PATH_VAR_PRM VarPrm)
```

##### Acm2_GpPathConditional
```cpp
U32 Acm2_GpPathConditional(U32 GpID, U32 MoveCmd)
```

##### Acm2_GpPathOperator 
```cpp
U32 Acm2_GpPathOperator(U32 GpID, PATH_OPERATOR_PRM OperatorPrm)
```

##### Acm2_GpPathStartRecordBuffer
```cpp
U32 Acm2_GpPathStartRecordBuffer(U32 GpID)
```

##### Acm2_GpPathEndRecordBuffer
```cpp
U32 Acm2_GpPathEndRecordBuffer(U32 GpID, VALIDATE_RESULT* OutResult)
```

##### Acm2_GpLookAheadPath

```cpp
U32 Acm2_GpLookAheadPath(U32 GpID, U16 BufferSize, PI8 OutputFile)
```

##### Acm2_GpLookAheadPathFile

```cpp
U32 Acm2_GpLookAheadPathFile(U32 GpID, U16 BufferSize, PI8 InputPathFile, PI8 OutputFile, PU32 PathCount)
```

##### Acm2_GpLoadAndMovePath
```cpp
U32 Acm2_GpLoadAndMovePath(U32 GpID, PI8 FilePath, PU32 TotalCount)
```

##### Acm2_ChSetDOBit
Set DO bit by channel.

```cpp
U32 Acm2_ChSetDOBit(U32 DoChannel, U32 BitData)
```
```python
## Example code
## Using the example code after LoadENI & Connect
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

## Set DO channel, local DO on PCIE-1203 is 0~1, rest of device will set from channel 8~
do_channel8 = c_uint32(8)
do_channel14 = c_uint32(14)
bit_data = c_uint32(DO_ONOFF.DO_ON.value)
## Set DO(8) on
errCde = AdvMot.Acm2_ChSetDOBit(do_channel8, bit_data)
## Set DO(14) on
errCde = AdvMot.Acm2_ChSetDOBit(do_channel14, bit_data)
time.sleep(0.5)
get_data8 = c_uint32(0)
get_data14 = c_uint32(0)
## Get DO(8) value
errCde = AdvMot.Acm2_ChGetDOBit(do_channel8, byref(get_data8))
## Get DO(14) value
errCde = AdvMot.Acm2_ChGetDOBit(do_channel8, byref(get_data14))
```

##### Acm2_ChGetDOBit
Get DO bit by channel.

```cpp
U32 Acm2_ChGetDOBit(U32 DoChannel, PU32 BitData)
```
```python
## Example code
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

do_ch = c_uint32(0)
property_id = c_uint(PropertyID2.CFG_CH_DaqDoFuncSelect.value)
val = c_double(1)
## Set local DO channel 0 as gerneral DO
errCde = AdvMot.Acm2_SetProperty(do_ch, property_id, val)
get_val = c_double(0)
## Get local DO channel 0 property value
errCde = AdvMot.Acm2_GetProperty(do_ch, property_id, byref(get_val))
## Set local DO channel 0 ON
data = c_uint32(1)
errCde = AdvMot.Acm2_ChSetDOBit(do_ch, data)
## Get local DO channel 0 value
get_data = c_uint32(0)
errCde = AdvMot.Acm2_ChGetDOBit(do_ch, byref(get_data))
```

##### Acm2_ChGetDIBit
Get DI bit by channel.

```cpp
U32 Acm2_ChGetDIBit(U32 DiChannel, PU32 BitData)
```

##### Acm2_ChSetDOBitByRingNo
Set DO bit by channel, and ring number.

```cpp
U32 Acm2_ChSetDOBitByRingNo(U32 RingNo, U32 SlaveID, U32 DoChannel, U32 BitData)
```

##### Acm2_ChGetDOBitByRingNo
Get DO bit by ring number, and channel.

```cpp
U32 Acm2_ChGetDOBitByRingNo(U32 RingNo, U32 SlaveID, U32 DoChannel, PU32 BitData)
```

##### Acm2_ChGetDIBitByRingNo
Get DI bit by ring number, and channel.

```cpp
U32 Acm2_ChGetDIBitByRingNo(U32 RingNo, U32 SlaveID, U32 DiChannel, PU32 BitData)
```

##### Acm2_ChSetDOByte
Set DO channel byte.

```cpp
U32 Acm2_ChSetDOByte(U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```

##### Acm2_ChGetDOByte
Get DO channel byte.

```cpp
U32 Acm2_ChGetDOByte(U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

## Using this example code after connect AMAX-5057SO
## Check how to start a EtherCAT subdevice by Acm2_DevConnect

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

## Local DO of PCIE1203 is port 0
port_num = c_uint32(1)
start_ch = c_uint32(0)
get_byte_value = [c_uint32(0)] * 8
time.sleep(0.5)
## Get DO byte of 5057SO (0~7)
errCde = AdvMot.Acm2_ChGetDOByte(start_ch, port_num, byref(get_byte_value[0]))
set_byte_value_on = [c_uint32(DO_ONOFF.DO_ON.value)] * 8
set_byte_value_off = [c_uint32(DO_ONOFF.DO_OFF.value)] * 8
set_value_arr_on = (c_uint32 * len(set_byte_value_on))(*set_byte_value_on)
set_value_arr_off = (c_uint32 * len(set_byte_value_off))(*set_byte_value_off)
time.sleep(0.5)
## Set DO byte of 5057SO (0~7)
errCde = AdvMot.Acm2_ChSetDOByte(start_ch, port_num, set_value_arr_on)
time.sleep(1)
## Get DO byte of 5057SO (0~7)
errCde = AdvMot.Acm2_ChGetDOByte(start_ch, port_num, byref(get_byte_value[0]))
time.sleep(0.5)
## Set DO byte of 5057SO (0~7)
errCde = AdvMot.Acm2_ChSetDOByte(start_ch, port_num, set_value_arr_off)
```

##### Acm2_ChGetDIByte
Get DI channel byte.

```cpp
U32 Acm2_ChGetDIByte(U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```

##### Acm2_ChSetDOByteByRingNo
Set DO byte by ring number.

```cpp
U32 Acm2_ChSetDOByteByRingNo(U32 RingNo, U32 SlaveID, U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```

##### Acm2_ChGetDOByteByRingNo
Get DO byte by ring number.

```cpp
U32 Acm2_ChGetDOByteByRingNo(U32 RingNo, U32 SlaveID, U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```

##### Acm2_ChGetDIByteByRingNo
Get DI byte by ring number.

```cpp
U32 Acm2_ChGetDIByteByRingNo(U32 RingNo, U32 SlaveID, U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```

##### Acm2_ChSetAOData
Set AO data.

```cpp
U32 Acm2_ChSetAOData(U32 AoChannel, DAQ_DATA_TYPE Type, F64 AoData)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

## Using this example code after connect AMAX-4820, AMAX-4817
## Check how to start a EtherCAT subdevice by Acm2_DevConnect

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

## Ring as IO Ring
ring_no = c_uint32(1)
## set by position
id_type = c_uint(ECAT_ID_TYPE.SUBDEVICE_POS.value)
## Sort AMAX-4820 second posiotn
sub_dev_pos = c_uint32(2)
## Set AO(0) output range as -10V ~ 10V
pdo_type = c_uint32(ECAT_TYPE.ECAT_TYPE_U16.value)
pdo_data_size = c_uint32(sizeof(c_uint16))
pdo_index = c_uint32(0x2180)
val_range = c_uint16(3)
pdo_range_sub_index = c_uint32(0x02)
errCde = AdvMot.Acm2_DevWriteSDO(ring_no, id_type, sub_dev_pos, pdo_index, pdo_range_sub_index, pdo_type, pdo_data_size, byref(val_range))
## Set AO(0) output enable
pdo_enable_sub_index = c_uint32(0x01)
val_enable = c_uint16(1)
errCde = AdvMot.Acm2_DevWriteSDO(ring_no, id_type, sub_dev_pos, pdo_index, pdo_enable_sub_index, pdo_type, pdo_data_size, byref(val_enable))
## AMAX-4820 default AO(0) ~ AO(3)
ao_ch = c_uint32(0)
## Set AO(0) as 10V
data_type = c_uint(DAQ_DATA_TYPE.SCALED_DATA.value)
ao_data = c_double(10)
errCde = AdvMot.Acm2_ChSetAOData(ao_ch, data_type, ao_data)
## Get AO(0) data
get_data_ao = c_double(0)
errCde = AdvMot.Acm2_ChGetAOData(ao_ch, data_type, byref(get_data_ao))
assertAlmostEqual(ao_data.value, get_data_ao.value, delta=1.0)
## Get AI(0) data
get_data_ai = c_double(0)
errCde = AdvMot.Acm2_ChGetAIData(ao_ch, data_type, byref(get_data_ai))
```

##### Acm2_ChGetAOData
Get AO data.

```cpp
U32 Acm2_ChGetAOData(U32 AoChannel, DAQ_DATA_TYPE Type, PF64 AoData)
```

##### Acm2_ChGetAOStatus
```cpp
U32 Acm2_ChGetAOStatus(U32 AoChannel, PU32 ChanStatus)
```

##### Acm2_ChSetAODataByRingNo
Set AO data by ring number.

```cpp
U32 Acm2_ChSetAODataByRingNo(U32 RingNo, U32 SlaveID, U32 AoChannel, DAQ_DATA_TYPE Type, F64 AoData)
```

##### Acm2_ChGetAODataByRingNo
Get AO data by ring number.

```cpp
U32 Acm2_ChGetAODataByRingNo(U32 RingNo, U32 SlaveID, U32 AoChannel, DAQ_DATA_TYPE Type, PF64 AoData)
```

##### Acm2_ChGetAOStatusByRingNo
```cpp
U32 Acm2_ChGetAOStatusByRingNo(U32 RingNo, U32 SubDeviceID, U32 AoChannel, PU32 ChanStatus)
```

##### Acm2_ChGetAIStatus
```cpp
U32 Acm2_ChGetAIStatus(U32 AiChannel, PU32 ChanStatus)
```

##### Acm2_ChGetAIData
Get AI data.

```cpp
U32 Acm2_ChGetAIData(U32 AiChannel, DAQ_DATA_TYPE Type, PF64 AiData)
```

##### Acm2_ChGetAIStatusByRingNo
```cpp
U32 Acm2_ChGetAIStatusByRingNo(U32 RingNo, U32 SubDeviceID, U32 AiChannel, PU32 ChanStatus)
```

##### Acm2_ChGetAIDataByRingNo
Get AI data by ring number.

```cpp
U32 Acm2_ChGetAIDataByRingNo(U32 RingNo, U32 SlaveID, U32 AiChannel, DAQ_DATA_TYPE Type, PF64 AiData)
```

##### Acm2_ChSetScaledProperty
```cpp
U32 Acm2_ChSetScaledProperty(U32 ChID, ADV_OBJ_TYPE ObjType, F64 UpperBound, F64 LowerBound, U32 Resolution, DAQ_TRANS_TYPE TransType)
```

##### Acm2_ChGetCntData
Get counter data.

```cpp
U32 Acm2_ChGetCntData(U32 CntChannel, PF64 CounterData)
```

##### Acm2_ChSetCntData
Set counter data.

```cpp
U32 Acm2_ChSetCntData(U32 CntChannel, F64 CounterData)
```

##### Acm2_ChLinkCmpFIFO
Set compare position.

```cpp
U32 Acm2_ChLinkCmpFIFO(U32 ChID, PU32 AxisArray, U32 ArrayElement)
```

##### Acm2_ChLinkCmpObject
Link compare do with axis/counter.

```cpp
U32 Acm2_ChLinkCmpObject(U32 ChID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

## Using this example code after connect AMAX-4820, AMAX-4817
## Check how to start a EtherCAT subdevice by Acm2_DevConnect

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

cnt_ch = c_uint32(1)
## Local CMP Diff channel is 2
cmp_ch = c_uint32(2)
## Set encoder(0) pulse mode as CW/CCW.
ppt_arr = c_uint32(PropertyID2.CFG_CH_DaqCntPulseInMode.value)
val_arr = c_double(PULSE_IN_MODE.I_CW_CCW.value)
get_val = c_double(0)
get_cnt_data = c_double(0)
errCde = AdvMot.Acm2_SetProperty(cnt_ch, ppt_arr, val_arr)
errCde = AdvMot.Acm2_GetProperty(cnt_ch, ppt_arr, byref(get_val))
errCde = AdvMot.Acm2_ChGetCntData(cnt_ch, byref(get_cnt_data))
## Link local encoder/counter to compare
cnt_arr = [cnt_ch]
trans_cnt_arr = (c_uint32 * len(cnt_arr))(*cnt_arr)
axis_type = c_uint(ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL.value)
## Reset Link connection
errCde = AdvMot.Acm2_ChLinkCmpObject(cmp_ch, axis_type, trans_cnt_arr, 0)
errCde = AdvMot.Acm2_ChLinkCmpObject(cmp_ch, axis_type, trans_cnt_arr, len(cnt_arr))
## Set compare property, disable compare before setting.
cmp_set_arr = [c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoOutputMode.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoLogic.value)]
val_arr = [c_double(COMPARE_ENABLE.CMP_DISABLE.value),
            c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value),
            c_double(COMPARE_LOGIC.CP_ACT_LOW.value)]
for i range(len(cmp_set_arr)):
    errCde = AdvMot.Acm2_SetProperty(cmp_ch, cmp_set_arr[i].value, val_arr[i])
## Get value
get_val = c_double(0)
for i range(len(val_arr)):
    errCde = AdvMot.Acm2_GetProperty(cmp_ch, cmp_set_arr[i], byref(get_val))
end_pos = c_double(2500)
## Enable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_ENABLE.value).value)
## Set compare data table
## Compare DO behavior: ---ON---        ---OFF---        ---ON---       ---OFF---
set_cmp_data_arr = [c_double(500), c_double(1000), c_double(1500), c_double(2000)]
trans_cmp_data_arr = (c_double * len(set_cmp_data_arr))(*set_cmp_data_arr)
errCde = AdvMot.Acm2_ChSetCmpBufferData(cmp_ch, trans_cmp_data_arr, len(set_cmp_data_arr))
## Reset encoder data as 0
reset_cnt_data = c_double(0)
errCde = AdvMot.Acm2_ChSetCntData(cnt_ch, reset_cnt_data)
## Get encoder data
get_cnt_data = c_double(0)
while get_cnt_data.value <= end_pos.value:
    time.sleep(0.1)
    errCde = AdvMot.Acm2_ChGetCntData(cnt_ch, byref(get_cnt_data))
## Disable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
```

##### Acm2_ChGetLinkedCmpObject
Get compare do linked object.

```cpp
U32 Acm2_ChGetLinkedCmpObject(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```

##### Acm2_ChLinkSWCmp
Link software compare channel with digital output.

```cpp
U32 Acm2_ChLinkSWCmp(U32 SWCmpID, U32 DOChannel)
```

##### Acm2_ChGetLinkedSWCmp
Get software compare channel linked do channel.
```cpp
U32 Acm2_ChGetLinkedSWCmp(U32 SWCmpID, PU32 DOChannel)
```

##### Acm2_ChEnableCmp
Enable compare channel.

```cpp
U32 Acm2_ChEnableCmp(U32 ChID, U32 Enable)
```

##### Acm2_ChSetCmpOut
Set compare channel on/off.

```cpp
U32 Acm2_ChSetCmpOut(U32 ChID, DO_ONOFF OnOff)
```

##### Acm2_ChSetCmpDoOut
Set compare on/off.

```cpp
U32 Acm2_ChSetCmpDoOut(U32 ChID, DO_ONOFF OnOff)
```

##### Acm2_AxGetCmpData
Get compared data by axis.

```cpp
U32 Acm2_AxGetCmpData(U32 AxID, PF64 CmpData)
```

##### Acm2_ChGetCmpData
Get compared data by channel.

```cpp
U32 Acm2_ChGetCmpData(U32 CmpChannel, PF64 CmpData, U32 ObjectArrayCount)
```

##### Acm2_AxSetCmpTable
Set compare table by axis.

```cpp
U32 Acm2_AxSetCmpTable(U32 AxID, PF64 TableArray, U32 ArrayElement)
```
```python
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

## Pulse mode
cnt_ch = c_uint32(0)
cmp_ch = c_uint32(0)
## Set encoder(0) pulse mode as CW/CCW.
ppt_arr = c_uint32(PropertyID2.CFG_CH_DaqCntPulseInMode.value)
val_arr = c_double(PULSE_IN_MODE.I_CW_CCW.value)
get_val = c_double(0)
errCde = AdvMot.Acm2_SetProperty(cnt_ch, ppt_arr, val_arr)
errCde = AdvMot.Acm2_GetProperty(cnt_ch, ppt_arr, byref(get_val))
## Set compare property, disable compare before setting.
cmp_set_arr = [c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoOutputMode.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoLogic.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoPulseWidth.value)]
val_arr = [c_double(COMPARE_ENABLE.CMP_DISABLE.value),
            c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value),
            c_double(COMPARE_LOGIC.CP_ACT_LOW.value),
            c_double(500000)]
for i range(len(cmp_set_arr)):
    errCde = AdvMot.Acm2_SetProperty(cmp_ch, cmp_set_arr[i].value, val_arr[i])
## Get value
get_val = c_double(0)
for i range(len(val_arr)):
    errCde = AdvMot.Acm2_GetProperty(cmp_ch, cmp_set_arr[i], byref(get_val))
## Link local encoder/counter to compare
cnt_arr = [cnt_ch]
trans_cnt_arr = (c_uint32 * len(cnt_arr))(*cnt_arr)
axis_type = c_uint(ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL.value)
errCde = AdvMot.Acm2_ChLinkCmpObject(cmp_ch, axis_type, trans_cnt_arr, len(cnt_arr))
end_pos = c_double(2500)
## Set compare data table
## Compare DO behavior: ---ON---        ---OFF---        ---ON---       ---OFF---
set_cmp_data_arr = [c_double(500), c_double(1000), c_double(1500), c_double(2000)]
trans_cmp_data_arr = (c_double * len(set_cmp_data_arr))(*set_cmp_data_arr)
errCde = AdvMot.Acm2_ChSetCmpBufferData(cmp_ch, trans_cmp_data_arr, len(set_cmp_data_arr))
## Reset encoder data as 0
reset_cnt_data = c_double(0)
errCde = AdvMot.Acm2_ChSetCntData(cnt_ch, reset_cnt_data)
## Enable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_ENABLE.value).value)
## Get encoder data
get_cnt_data = c_double(0)
while get_cnt_data.value < end_pos.value:
    time.sleep(0.1)
    errCde = AdvMot.Acm2_ChGetCntData(cnt_ch, byref(get_cnt_data))
## Disable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
```


##### Acm2_AxSetCmpAuto
Set auto compare by axis.

```cpp
U32 Acm2_AxSetCmpAuto(U32 AxID, F64 StartPosition, F64 EndPosition, F64 Interval)
```

##### Acm2_ChSetCmpAuto
Set auto compare by channel.

```cpp
U32 Acm2_ChSetCmpAuto(U32 CmpChannel, F64 StartPosition, F64 EndPosition, F64 Interval)
```

##### Acm2_ChSetCmpBufferData
Set compare buffer.

```cpp
U32 Acm2_ChSetCmpBufferData(U32 CmpChannel, PF64 TableArray, U32 ArrayElement)
```
```python
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

## Toggle Mode
cnt_ch = c_uint32(0)
cmp_ch = c_uint32(0)
## Set encoder(0) pulse mode as CW/CCW.
ppt_arr = c_uint32(PropertyID2.CFG_CH_DaqCntPulseInMode.value)
val_arr = c_double(PULSE_IN_MODE.I_CW_CCW.value)
get_val = c_double(0)
errCde = AdvMot.Acm2_SetProperty(cnt_ch, ppt_arr, val_arr)
errCde = AdvMot.Acm2_GetProperty(cnt_ch, ppt_arr, byref(get_val))
## Set compare property, disable compare before setting.
cmp_set_arr = [c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoOutputMode.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoLogic.value)]
val_arr = [c_double(COMPARE_ENABLE.CMP_DISABLE.value),
            c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value),
            c_double(COMPARE_LOGIC.CP_ACT_LOW.value)]
for i range(len(cmp_set_arr)):
    errCde = AdvMot.Acm2_SetProperty(cmp_ch, cmp_set_arr[i].value, val_arr[i])
## Get value
get_val = c_double(0)
for i range(len(val_arr)):
    errCde = AdvMot.Acm2_GetProperty(cmp_ch, cmp_set_arr[i], byref(get_val))
## Link local encoder/counter to compare
cnt_arr = [cnt_ch]
trans_cnt_arr = (c_uint32 * len(cnt_arr))(*cnt_arr)
axis_type = c_uint(ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL.value)
errCde = AdvMot.Acm2_ChLinkCmpObject(cmp_ch, axis_type, trans_cnt_arr, len(cnt_arr))
end_pos = c_double(2500)
## Set compare data table
## Compare DO behavior: ---ON---        ---OFF---        ---ON---       ---OFF---
set_cmp_data_arr = [c_double(500), c_double(1000), c_double(1500), c_double(2000)]
trans_cmp_data_arr = (c_double * len(set_cmp_data_arr))(*set_cmp_data_arr)
errCde = AdvMot.Acm2_ChSetCmpBufferData(cmp_ch, trans_cmp_data_arr, len(set_cmp_data_arr))
## Reset encoder data as 0
reset_cnt_data = c_double(0)
errCde = AdvMot.Acm2_ChSetCntData(cnt_ch, reset_cnt_data)
## Enable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_ENABLE.value).value)
## Get encoder data
get_cnt_data = c_double(0)
while get_cnt_data.value < end_pos.value:
    time.sleep(0.1)
    errCde = AdvMot.Acm2_ChGetCntData(cnt_ch, byref(get_cnt_data))
## Disable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
```


##### Acm2_ChSetMultiCmpTable
Set compare table.

```cpp
U32 Acm2_ChSetMultiCmpTable(U32 ChID, PF64 TableArray, U32 ObjectArrayCount, U32 DataArrayCount)
```
```python
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

cnt_ch = [c_uint32(0), c_uint32(1)]
cmp_ch = c_uint32(0)
ltc_ch = c_uint32(0)
## Set encoder(0) pulse mode as CW/CCW.
ppt_arr = c_uint32(PropertyID2.CFG_CH_DaqCntPulseInMode.value)
val_arr = c_double(PULSE_IN_MODE.I_CW_CCW.value)
get_val = c_double(0)
for i range(len(cnt_ch)):
    errCde = AdvMot.Acm2_SetProperty(cnt_ch[i], ppt_arr, val_arr)
    errCde = AdvMot.Acm2_GetProperty(cnt_ch[i], ppt_arr, byref(get_val))
## Link local encoder/counter to compare
cnt_arr = cnt_ch
trans_cnt_arr = (c_uint32 * len(cnt_arr))(*cnt_arr)
axis_type = c_uint(ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL.value)
errCde = AdvMot.Acm2_ChLinkCmpObject(cmp_ch, axis_type, trans_cnt_arr, len(cnt_arr))
get_obj_type = c_uint(0)
get_linked_arr = (c_uint32 * 2)()
get_linked_cnt = c_uint32(2)
## Get linked local encoder/counter to compare
errCde = AdvMot.Acm2_ChGetLinkedCmpObject(cmp_ch, byref(get_obj_type), get_linked_arr, byref(get_linked_cnt))
print('[CMP] Linked type:{0}, linked count:{1}'.format(get_obj_type.value, get_linked_cnt.value))
for i range(get_linked_cnt.value):
    print('Linked channel:{0}'.format(get_linked_arr[i]))
## Set compare property, disable compare before setting.
cmp_set_arr = [c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value),
            c_uint32(PropertyID2.CFG_CH_DaqCmpDoOutputMode.value),
            c_uint32(PropertyID2.CFG_CH_DaqCmpDoLogic.value),
            c_uint32(PropertyID2.CFG_CH_DaqCmpDoPulseWidth.value),
            c_uint32(PropertyID2.CFG_CH_DaqCmpDeviation.value)]
val_arr = [c_double(COMPARE_ENABLE.CMP_DISABLE.value),
        c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value),
        c_double(COMPARE_LOGIC.CP_ACT_LOW.value),
        c_double(500000), c_double(100)]
for i range(len(cmp_set_arr)):
    errCde = AdvMot.Acm2_SetProperty(cmp_ch, cmp_set_arr[i].value, val_arr[i])
## Get CMP proerty
get_val = c_double(0)
for i range(len(val_arr)):
    errCde = AdvMot.Acm2_GetProperty(cmp_ch, cmp_set_arr[i], byref(get_val))
## Get linked local encoder/counter to latch
errCde = AdvMot.Acm2_ChGetLinkedLatchObject(ltc_ch, byref(get_obj_type), get_linked_arr, byref(get_linked_cnt))
print('[LTC] Linked type:{0}, linked count:{1}'.format(get_obj_type.value, get_linked_cnt.value))
for i range(get_linked_cnt.value):
    print('Linked channel:{0}'.format(get_linked_arr[i]))
## Reset LTC buffer
errCde = AdvMot.Acm2_ChResetLatchBuffer(ltc_ch)
## Set LTC property
ltc_set_ppt_arr = [c_uint32(PropertyID2.CFG_CH_DaqLtcMinDist.value),
                c_uint32(PropertyID2.CFG_CH_DaqLtcLogic.value),
                c_uint32(PropertyID2.CFG_CH_DaqLtcEnable.value)]
ltc_val_arr = [c_double(10), c_double(COMPARE_LOGIC.CP_ACT_LOW.value), c_double(COMPARE_ENABLE.CMP_ENABLE.value)]
for i range(len(ltc_set_ppt_arr)):
    errCde = AdvMot.Acm2_SetProperty(ltc_ch, ltc_set_ppt_arr[i].value, ltc_val_arr[i])
## Get LTC property
get_val_ltc = c_double(0)
for i range(len(ltc_val_arr)):
    errCde = AdvMot.Acm2_GetProperty(ltc_ch, ltc_set_ppt_arr[i], byref(get_val_ltc))

## Set compare data
set_cmp_data_arr = [c_double(500), c_double(1000), c_double(1500), c_double(2000), c_double(2500), c_double(3000),
                    c_double(550), c_double(1050), c_double(1550), c_double(2050), c_double(2550), c_double(3050)]
trans_cmp_data_arr = (c_double * len(set_cmp_data_arr))(*set_cmp_data_arr)
errCde = AdvMot.Acm2_ChSetMultiCmpBufferData(cmp_ch, trans_cmp_data_arr, len(cnt_ch), c_uint32(int(len(set_cmp_data_arr) / len(cnt_ch))))
## Reset encoder data as 0
reset_cnt_data = c_double(0)
for i range(len(cnt_ch)):
    errCde = AdvMot.Acm2_ChSetCntData(cnt_ch[i], reset_cnt_data)
## Enable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_ENABLE.value).value)
## Get encoder data
get_cnt_data = c_double(0)
end_pos = c_double(3500)
while get_cnt_data.value <= end_pos.value:
    time.sleep(0.1)
    for i range(len(cnt_ch)):
        tmp_ch = c_uint32(i)
        errCde = AdvMot.Acm2_ChGetCntData(tmp_ch, byref(get_cnt_data))
## Get LTC data
get_ltc_buf_status = BUFFER_STATUS()
act_data_cnt = c_uint32(128)
get_ltc_data_arr = (c_double * act_data_cnt.value)()
errCde = AdvMot.Acm2_ChGetLatchBufferStatus(ltc_ch, byref(get_ltc_buf_status))
print('RemainCount:{0}, FreeSpaceCount:{1}'.format(get_ltc_buf_status.RemainCount, get_ltc_buf_status.FreeSpaceCount))
errCde = AdvMot.Acm2_ChReadLatchBuffer(ltc_ch, get_ltc_data_arr, act_data_cnt, byref(act_data_cnt))
print('act_data_cnt:{0}'.format(act_data_cnt.value))
for i range(act_data_cnt.value):
    print('get_ltc_data_arr[{0}]:{1}'.format(i, get_ltc_data_arr[i]))
## Disable compare and latch
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqLtcEnable.value).value,
                                        c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
errCde = AdvMot.Acm2_SetProperty(ltc_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value,
                                        c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
```

##### Acm2_ChSetMultiCmpBufferData
Set multi compare buffer.

```cpp
U32 Acm2_ChSetMultiCmpBufferData(U32 ChID, PF64 MultiCmpTable, U32 ObjectArrayCount, U32 DataArrayCount)
```

##### Acm2_ChResetCmpData
Reset compare data.

```cpp
U32 Acm2_ChResetCmpData(U32 CmpChannel)
```

##### Acm2_ChGetCmpBufferStatus
Get compared buffer status.

```cpp
U32	Acm2_ChGetCmpBufferStatus(U32 CmpChannel, PBUFFER_STATUS bufferstatus)
```

##### Acm2_ChGetCmpCounter
```cpp
U32 Acm2_ChGetCmpCounter(U32 ChID, PU32 CmpCounter)
```

##### Acm2_ChLinkLatchAxis
Link latch to axis.
```cpp
U32 Acm2_ChLinkLatchAxis(U32 ChID, PU32 AxisArray, U32 AxisCount)
```

##### Acm2_ChLinkLatchObject
Lift latch to object.
```cpp
U32 Acm2_ChLinkLatchObject(U32 ChID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)
```

##### Acm2_ChGetLinkedLatchObject
Get linked latch object.
```cpp
U32 Acm2_ChGetLinkedLatchObject(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```

##### Acm2_ChTriggerLatch
Trigger latch by channel.

```cpp
U32 Acm2_ChTriggerLatch(U32 ChID)
```

##### Acm2_AxReadLatchBuffer
Read latch buffer.

```cpp
U32	Acm2_AxReadLatchBuffer(U32 AxID, PF64 LatchDataArray, PU32 DataCnt)
```

##### Acm2_ChReadLatchBuffer
Read latch buffer by channel.

```cpp
U32	Acm2_ChReadLatchBuffer(U32 LtcChannel, PF64 LatchDataArray, U32 ObjectArrayCount, PU32 DataArrayCount)
```

##### Acm2_AxGetLatchBufferStatus
Get latch buffer status.

```cpp
U32	Acm2_AxGetLatchBufferStatus(U32 AxID, PU32 RemainCnt, PU32 SpaceCnt)
```

##### Acm2_ChGetLatchBufferStatus
Get latch buffer status by channel.

```cpp
U32	Acm2_ChGetLatchBufferStatus(U32 LtcChannel, BUFFER_STATUS *bufferstatus)
```
```python
## Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

## Using this example code after connect AMAX-4820, AMAX-4817
## Check how to start a EtherCAT subdevice by Acm2_DevConnect

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

cnt_ch = c_uint32(0)
cmp_ch = c_uint32(0)
ltc_ch = c_uint32(0)
## Set encoder(0) pulse mode as CW/CCW.
ppt_arr = c_uint32(PropertyID2.CFG_CH_DaqCntPulseInMode.value)
val_arr = c_double(PULSE_IN_MODE.I_CW_CCW.value)
get_val = c_double(0)
errCde = AdvMot.Acm2_SetProperty(cnt_ch, ppt_arr, val_arr)
errCde = AdvMot.Acm2_GetProperty(cnt_ch, ppt_arr, byref(get_val))
## Link local encoder/counter to compare
cnt_arr = [cnt_ch]
trans_cnt_arr = (c_uint32 * len(cnt_arr))(*cnt_arr)
axis_type = c_uint(ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL.value)
errCde = AdvMot.Acm2_ChLinkCmpObject(cmp_ch, axis_type, trans_cnt_arr, len(cnt_arr))
## Set compare property, disable compare before setting.
cmp_set_arr = [c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoOutputMode.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoLogic.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoPulseWidth.value)]
val_arr = [c_double(COMPARE_ENABLE.CMP_DISABLE.value),
            c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value),
            c_double(COMPARE_LOGIC.CP_ACT_LOW.value),
            c_double(500000)]
for i range(len(cmp_set_arr)):
    errCde = AdvMot.Acm2_SetProperty(cmp_ch, cmp_set_arr[i].value, val_arr[i])
## Get CMP proerty
get_val = c_double(0)
for i range(len(val_arr)):
    errCde = AdvMot.Acm2_GetProperty(cmp_ch, cmp_set_arr[i], byref(get_val))

## Get linked local encoder/counter to latch
get_obj_type = c_uint(0)
get_linked_arr = (c_uint32 * 2)()
get_linked_cnt = c_uint32(2)
errCde = AdvMot.Acm2_ChGetLinkedLatchObject(ltc_ch, byref(get_obj_type), get_linked_arr, byref(get_linked_cnt))
print('Linked type:{0}, linked count:{1}'.format(get_obj_type.value, get_linked_cnt.value))
for i range(get_linked_cnt.value):
    print('Linked channel:{0}'.format(get_linked_arr[i]))
## Reset LTC buffer
errCde = AdvMot.Acm2_ChResetLatchBuffer(ltc_ch)
## Set LTC property
ltc_set_ppt_arr = [c_uint32(PropertyID2.CFG_CH_DaqLtcMinDist.value),
                    c_uint32(PropertyID2.CFG_CH_DaqLtcLogic.value),
                    c_uint32(PropertyID2.CFG_CH_DaqLtcEnable.value)]
ltc_val_arr = [c_double(10), c_double(COMPARE_LOGIC.CP_ACT_LOW.value), c_double(COMPARE_ENABLE.CMP_ENABLE.value)]
for i range(len(ltc_set_ppt_arr)):
    errCde = AdvMot.Acm2_SetProperty(ltc_ch, ltc_set_ppt_arr[i].value, ltc_val_arr[i])
## Get LTC property
get_val_ltc = c_double(0)
for i range(len(ltc_val_arr)):
    errCde = AdvMot.Acm2_GetProperty(ltc_ch, ltc_set_ppt_arr[i], byref(get_val_ltc))

## Set compare data
set_cmp_data_arr = [c_double(500), c_double(1000), c_double(1500), c_double(2000)]
trans_cmp_data_arr = (c_double * len(set_cmp_data_arr))(*set_cmp_data_arr)
errCde = AdvMot.Acm2_ChSetCmpBufferData(cmp_ch, trans_cmp_data_arr, len(set_cmp_data_arr))
## Reset encoder data as 0
reset_cnt_data = c_double(0)
errCde = AdvMot.Acm2_ChSetCntData(cnt_ch, reset_cnt_data)
## Enable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_ENABLE.value).value)
## Get encoder data
get_cnt_data = c_double(0)
end_pos = c_double(2500)
while get_cnt_data.value <= end_pos.value:
    time.sleep(0.1)
    for i range(2):
        tmp_ch = c_uint32(i)
        errCde = AdvMot.Acm2_ChGetCntData(tmp_ch, byref(get_cnt_data))
        print('[{0}]get_cnt_data:{1}'.format(i, get_cnt_data.value))
    errCde = AdvMot.Acm2_ChGetCntData(cnt_ch, byref(get_cnt_data))
## Get LTC data
get_ltc_buf_status = BUFFER_STATUS()
get_data_cnt = c_uint32(10)
act_data_cnt = c_uint32(128)
get_ltc_data_arr = (c_double * get_data_cnt.value)()
errCde = AdvMot.Acm2_ChGetLatchBufferStatus(ltc_ch, byref(get_ltc_buf_status))
print('RemainCount:{0}, FreeSpaceCount:{1}'.format(get_ltc_buf_status.RemainCount, get_ltc_buf_status.FreeSpaceCount))
errCde = AdvMot.Acm2_ChReadLatchBuffer(ltc_ch, get_ltc_data_arr, get_data_cnt, byref(act_data_cnt))
print('act_data_cnt:{0}'.format(act_data_cnt.value))
for i range(act_data_cnt.value):
    print('get_ltc_data_arr[{0}]:{1}'.format(i, get_ltc_data_arr[i]))
## Disable compare and latch
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqLtcEnable.value).value,
                                            c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
errCde = AdvMot.Acm2_SetProperty(ltc_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value,
                                            c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
```

##### Acm2_AxResetLatchBuffer
Reset latch buffer.

```cpp
U32	Acm2_AxResetLatchBuffer(U32 AxID)
```

##### Acm2_ChResetLatchBuffer
Reset latch buffer by channel.

```cpp
U32	Acm2_ChResetLatchBuffer(U32 LtcChannel)
```

##### Acm2_ChLinkPWMTable
Link PWM with object.

```cpp
U32 Acm2_ChLinkPWMTable(U32 ChID, ADV_OBJ_TYPE ObjType, U32 ObjectID)
```

##### Acm2_ChGetLinkedPWMTable
Get linked PWM Acm2_ChSetPWMTabletable by channel.

```cpp
U32 Acm2_ChGetLinkedPWMTable(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```

##### Acm2_ChSetPWMTable
Set PWM table by channel.

```cpp
U32 Acm2_ChSetPWMTable(U32 ChID, PF64 VelocityArray, PF64 PWMArray, U32 ArrayElements)
```

##### Acm2_ChLoadPWMTableFile
Loal PWM table file.

```cpp
U32 Acm2_ChLoadPWMTableFile(U32 ChID, PI8 FilePath, PU32 PointsCount)
```

##### Acm2_ChGetPWMTableStatus
Get PWM table status.

```cpp
U32	Acm2_ChGetPWMTableStatus(U32 ChID, PWM_TABLE_STATUS *PWMStatus)
```

##### Acm2_ChGetExtDriveData
Get external drive data by channel.

```cpp
U32 Acm2_ChGetExtDriveData(U32 ExtChannel, PF64 CounterData)
```

##### Acm2_ChSetExtDriveData
Set external drive data by channel.

```cpp
U32 Acm2_ChSetExtDriveData(U32 ExtChannel, F64 CounterData)
```

##### Acm2_ChLinkExtDriveObject
Link external drive object.

```cpp
U32 Acm2_ChLinkExtDriveObject(U32 ChID, ADV_OBJ_TYPE ObjType, U32 ObjectID)
```

##### Acm2_ChGetLinkedExtDriveObject
Get linked external drive object.

```cpp
U32 Acm2_ChGetLinkedExtDriveObject(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```

##### Acm2_DevMDaqConfig
Set MDAQ config.

```cpp
U32 Acm2_DevMDaqConfig(U32 ChannelID, U32 Period, U32 AxisNo, U32 Method, U32 ChanType, U32 Count)
```

##### Acm2_DevMDaqGetConfig
Get MDAQ config.

```cpp
U32 Acm2_DevMDaqGetConfig(U32 ChannelID, PU32 Period, PU32 AxisNo, PU32 Method, PU32 ChanType, PU32 Count)
```

##### Acm2_DevMDaqStart
Start MDAQ.

```cpp
U32 Acm2_DevMDaqStart(U32 DevID)
```

##### Acm2_DevMDaqStop
Stop MDAQ.

```cpp
U32 Acm2_DevMDaqStop(U32 DevID)
```

##### Acm2_DevMDaqReset
Reset MDAQ.

```cpp
U32 Acm2_DevMDaqReset(U32 ChannelID)
```

##### Acm2_DevMDaqGetStatus
Get MDAQ status.

```cpp
U32 Acm2_DevMDaqGetStatus(U32 ChannelID, PU32 CurrentCnt, PU32 Status)
```

##### Acm2_DevMDaqGetData
Get MDAQ data.

```cpp
U32 Acm2_DevMDaqGetData(U32 ChannelID, U32 StartIndex, U32 MaxCount, PF64 DataBuffer)
```

##### Acm2_DevLoadENI
Download ENI file.

```cpp
U32 Acm2_DevLoadENI(U32 RingNo, PI8 ENIFile)
```

##### Acm2_DevConnect
Connect subdevices.

```cpp
U32 Acm2_DevConnect(U32 RingNo)
```
```python
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

## eni file can be create by the Utility
eni_path = b'test\\63000000_eni1.xml'
## Motion ring number:0, IO Ring number:1, IORing is SM mode only
ring_no = c_uint32(1)
errCde = AdvMot.Acm2_DevLoadENI(ring_no, eni_path)
## After load eni file, StartFieldbus/Connect to subdevices.
errCde = AdvMot.Acm2_DevConnect(ring_no)
## Set EtherCAT type as position
ecat_type = c_uint(ECAT_ID_TYPE.SUBDEVICE_POS.value)
## SubDevice position 0 is AMAX-5074
sub_dev0 = c_uint32(0)
## SubDevice position 1 is AMAX-5057SO
sub_dev1 = c_uint32(1)
get_sub_dev_state0 = c_uint32(0)
get_sub_dev_state1 = c_uint32(0)
while (get_sub_dev_state0.value != SUB_DEV_STATE.EC_SLAVE_STATE_OP.value) or (get_sub_dev_state1.value != SUB_DEV_STATE.EC_SLAVE_STATE_OP.value):
    # Get AMAX-5074 status
    errCde = AdvMot.Acm2_DevGetSubDeviceStates(ring_no, ecat_type, sub_dev0, byref(get_sub_dev_state0))
    # Get AMAX-5057SO status
    errCde = AdvMot.Acm2_DevGetSubDeviceStates(ring_no, ecat_type, sub_dev1, byref(get_sub_dev_state1))
    time.sleep(0.5)
```

##### Acm2_DevDisConnect
Disconnect subdevices

```cpp
U32 Acm2_DevDisConnect(U32 RingNo)
```
```python
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

## Motion ring number:0, IO Ring number:1, IORing is SM mode only
ring_no0 = c_uint32(0)
ring_no1 = c_uint32(1)
## Disconnect devices
errCde = AdvMot.Acm2_DevDisConnect(ring_no0)
errCde = AdvMot.Acm2_DevDisConnect(ring_no1)
```

##### Acm2_DevGetSubDevicesID
Get subdevices id.

```cpp
U32 Acm2_DevGetSubDevicesID(U32 RingNo, ECAT_ID_TYPE IDType, PU32 SubDeviceIDArray, PU32 SubDeviceCnt)
```

##### Acm2_DevGetMDeviceInfo
Get main device information.

```cpp
U32 Acm2_DevGetMDeviceInfo(U32 RingNo, PADVAPI_MDEVICE_INFO pMDeviceInfo)
```
```python
import os
import time
import xml.etree.ElementTree as xml
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

ring_no = c_uint32(1)
main_dev_info = ADVAPI_MDEVICE_INFO()
errCde = AdvMot.Acm2_DevGetMDeviceInfo(ring_no, byref(main_dev_info))
print('slave_count:{0}'.format(main_dev_info.slave_count))
```

##### Acm2_DevGetSubDeviceInfo
Get subdevice information.

```cpp
U32 Acm2_DevGetSubDeviceInfo(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, PADVAPI_SUBDEVICE_INFO_CM2 pInfo)
```
```python
import os
import time
import xml.etree.ElementTree as xml
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

ring_no = c_uint32(1)
## Get subdevice ID
id_type = c_uint(ECAT_ID_TYPE.SUBDEVICE_ID.value)
id_cnt = c_uint32(3)
phys_addr_arr = [0] * id_cnt.value
sub_dev_info_arr = (ADVAPI_SUBDEVICE_INFO_CM2*2)()
id_arr = (c_uint32 * id_cnt.value)()
errCde = AdvMot.Acm2_DevGetSubDevicesID(ring_no, id_type, id_arr, byref(id_cnt))
if os.name == 'nt':
    tree = xml.parse('test\\eni1.xml')
else:
    tree = xml.parse('test/eni1.xml')
idx = 0
## Check value from xml
for subdev tree.findall('.//Slave'):
    phys_addr = int(subdev.find('Info/PhysAddr').text)
    phys_addr_arr[idx] = phys_addr
    idx += 1
for i range(id_cnt.value):
    sub_dev_info = ADVAPI_SUBDEVICE_INFO_CM2()
    errCde = AdvMot.Acm2_DevGetSubDeviceInfo(ring_no, c_uint(ECAT_ID_TYPE.SUBDEVICE_POS.value), i, byref(sub_dev_info))
```

##### Acm2_DevGetSubDeviceFwVersion
Get subdevice fw information.

```cpp
U32 Acm2_DevGetSubDeviceFwVersion(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, char *VersionInfo)
```

##### Acm2_DevSetSubDeviceID
Set subdevice id.

```cpp
U32 Acm2_DevSetSubDeviceID(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 SubDeviceNewID)
```

##### Acm2_DevSetSubDeviceStates
Set subdevice status.

```cpp
U32 Acm2_DevSetSubDeviceStates(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 SubDeviceState)
```

##### Acm2_DevGetSubDeviceStates
Get subdevice states.

```cpp
U32 Acm2_DevGetSubDeviceStates(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, PU32 SubDeviceState)
```
```python
import os
import time
import xml.etree.ElementTree as xml
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

## eni file can be create by the Utility
if os.name == 'nt':
    eni_path = b'test\\eni1.xml'
else:
    eni_path = b'test/eni1.xml'
## Motion ring number:0, IO Ring number:1, IORing is SM mode only
ring_no = c_uint32(1)
errCde = AdvMot.Acm2_DevLoadENI(ring_no, eni_path)
## After load eni file, StartFieldbus/Connect to subdevices.
errCde = AdvMot.Acm2_DevConnect(ring_no)
## Set EtherCAT type as position
ecat_type = c_uint(ECAT_ID_TYPE.SUBDEVICE_POS.value)
## SubDevice position 0 is AMAX-5074
sub_dev0 = c_uint32(0)
## SubDevice position 1 is AMAX-5057SO
sub_dev1 = c_uint32(1)
get_sub_dev_state0 = c_uint32(0)
get_sub_dev_state1 = c_uint32(0)
while (get_sub_dev_state0.value != SUB_DEV_STATE.EC_SLAVE_STATE_OP.value) or (get_sub_dev_state1.value != SUB_DEV_STATE.EC_SLAVE_STATE_OP.value):
    # Get AMAX-5074 status
    errCde = AdvMot.Acm2_DevGetSubDeviceStates(ring_no, ecat_type, sub_dev0, byref(get_sub_dev_state0))
    # Get AMAX-5057SO status
    errCde = AdvMot.Acm2_DevGetSubDeviceStates(ring_no, ecat_type, sub_dev1, byref(get_sub_dev_state1))
    time.sleep(0.5)
```

##### Acm2_DevWriteSDOComplete
```cpp
U32 Acm2_DevWriteSDOComplete(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 DataSize, PVOID pValue)
```

##### Acm2_DevWriteSDO
Write data by SDO.

```cpp
U32 Acm2_DevWriteSDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, VOID *pValue)
```

##### Acm2_DevReadSDO
Read data by SDO.

```cpp
U32 Acm2_DevReadSDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, VOID *pValue)
```

##### Acm2_DevWritePDO
Write data by PDO.

```cpp
U32 Acm2_DevWritePDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, VOID *pValue)
```

##### Acm2_DevReadPDO
Read data by PDO.

```cpp
U32 Acm2_DevReadPDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, VOID *pValue)
```
```python
import os
import time
import xml.etree.ElementTree as xml
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
## Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
## Initial device
errCde = AdvMot.Acm2_DevInitialize()

## Ring as IO Ring
ring_no = c_uint32(1)
## set by position
id_type = c_uint(ECAT_ID_TYPE.SUBDEVICE_POS.value)
sub_dev_pos = c_uint32(1)
## AMAX-5057SO 0x3101:01 is DO(0)
pdo_idx = c_uint32(0x3101)
pdo_sub_idx = c_uint32(0x01)
## DO(0) data type is boolean
pdo_type = c_uint32(ECAT_TYPE.ECAT_TYPE_BOOL.value)
pdo_data_size = c_uint32(sizeof(c_bool))
val_on = c_bool(1)
val_off = c_bool(0)
get_value = c_bool(0)
## Set DO(0) on by PDO
errCde = AdvMot.Acm2_DevWritePDO(ring_no, id_type, sub_dev_pos, pdo_idx, pdo_sub_idx, pdo_type, pdo_data_size, byref(val_on))
## Get DO(0) value by PDO
errCde = AdvMot.Acm2_DevReadPDO(ring_no, id_type, sub_dev_pos, pdo_idx, pdo_sub_idx, pdo_type, pdo_data_size, byref(get_value))
## Set DO(0) off by PDO
errCde = AdvMot.Acm2_DevWritePDO(ring_no, id_type, sub_dev_pos, pdo_idx, pdo_sub_idx, pdo_type, pdo_data_size, byref(val_off))
## Get DO(0) value by PDO
errCde = AdvMot.Acm2_DevReadPDO(ring_no, id_type, sub_dev_pos, pdo_idx, pdo_sub_idx, pdo_type, pdo_data_size, byref(get_value))
```

##### Acm2_DevWriteReg
Write data by reg.

```cpp
U32 Acm2_DevWriteReg(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Address, U32 Type, U32 DataSize, VOID *pValue)
```

##### Acm2_DevReadReg
Read data by reg.

```cpp
U32 Acm2_DevReadReg(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Address, U32 Type, U32 DataSize, VOID *pValue)
```

##### Acm2_DevWriteFoE
```cpp
U32 Acm2_DevWriteFoE(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, PI8 FileName, PI8 FilePath, U32 Password)
```

##### Acm2_DevReadSubDeviceCommErrCnt
Read subdevice communication error counter.

```cpp
U32 Acm2_DevReadSubDeviceCommErrCnt(U32 RingNo, PU32 ErrCntArray, PU32 ArrayElements)
```

##### Acm2_DevSaveAllMapFile
Upload input/output mapping table from device.

```cpp
U32 Acm2_DevSaveAllMapFile(PI8 FilePath)
```

##### Acm2_DevSaveMapFile
```cpp
U32 Acm2_DevSaveMapFile(U32 RingNo, PI8 FilePath)
```

##### Acm2_DevLoadAllMapFile
Download input/output mapping table to device.

```cpp
U32 Acm2_DevLoadAllMapFile(PI8 FilePath)
```

##### Acm2_DevLoadMapFile
```cpp
U32 Acm2_DevLoadMapFile(U32 RingNo, PI8 FilePath)
```

##### Acm2_Ax1DCompensateTable
Set compensate table with one axis.

```cpp
U32 Acm2_Ax1DCompensateTable(U32 AxID, F64 OriginPos, F64 Pitch, PF64 OffsetData, U32 OffsetElements, U32 Direction)
```

##### Acm2_Ax2DCompensateTable
Set compensate table 2D.

```cpp
U32 Acm2_Ax2DCompensateTable(U32 AxID, U32 RelAxID, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataX, PF64 OffsetDataY, U32 OffsetElementsX, U32 OffsetElementsY)
```

##### Acm2_AxZAxisCompensateTable
Set compensate table Z axis.

```cpp
U32 Acm2_AxZAxisCompensateTable(U32 AxID, U32 RelAxID, U32 ZAxID, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataZ, U32 OffsetElementsX, U32 OffsetElementsY)
```

##### Acm2_AxGetCompensatePosition
Get compensate position by axis.

```cpp
U32 Acm2_AxGetCompensatePosition(U32 AxID, PF64 Position)
```

##### Acm2_AxGetPreview1DCompensatePosition
```cpp
U32 Acm2_AxGetPreview1DCompensatePosition(U32 AxID, F64 Position, U32 Direction, PF64 PreviewPosition)
```

##### Acm2_AxGetPreview2DCompensatePosition
```cpp
U32 Acm2_AxGetPreview2DCompensatePosition(U32 AxID, U32 RelAxID, F64 Position, F64 RelPosition, U32 Direction, U32 RelDirection, PF64 PreviewPosition, PF64 PreviewRelPosition)
```

##### Acm2_AxGetPreviewZAxisCompensatePosition
```cpp
U32 Acm2_AxGetPreviewZAxisCompensatePosition(U32 AxID, U32 RelAxID, U32 ZAxID, F64 Position, F64 RelPosition, U32 Direction, U32 RelDirection, PF64 PreviewZPosition)
```

##### Acm2_DevMultiTrigInitial
```cpp
U32 Acm2_DevMultiTrigInitial(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Enable, U32 PWM, U32 LTC, U32 MPG)
```

##### Acm2_DevOscChannelDataStart
Start Osc. channel data.

```cpp
U32 Acm2_DevOscChannelDataStart(U32 DevID)
```

##### Acm2_DevOscChannelDataStop
Stop Osc. channel data.

```cpp
U32 Acm2_DevOscChannelDataStop(U32 DevID)
```

##### Acm2_DevGetOscChannelDataConfig
Get config of Osc. channel.

```cpp
U32 Acm2_DevGetOscChannelDataConfig(U32 DevID, U16 ChannelID, POSC_PROFILE_PRM oscflg)
```

##### Acm2_DevSetOscChannelDataConfig
Set config of Osc. channel.

```cpp
U32 Acm2_DevSetOscChannelDataConfig(U32 DevID, U16 ChannelID, OSC_PROFILE_PRM oscflg)
```

##### Acm2_DevGetOscChannelData
Get Osc. channel data.

```cpp
U32 Acm2_DevGetOscChannelData(U32 DevID, U16 ChannelID, U32 DataIndex, PU32 MaxCount, PF64 DataBuffer)
```

##### Acm2_DevGetOscChannelStatus
Get Osc. channel status.

```cpp
U32  Acm2_DevGetOscChannelStatus(U32 DevID, PU32 Status)
```


---

## Log Functions
##### Amc_SetApiLog
Set API Log options

```cpp
U32 Amc_SetApiLog(const char* dir, const char* baseName, const AMCApiLogOptions* opt, U64 bufferSize)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

logOpt = AMC_API_LOG_OPT()
logDir = b'D:\\'
baseName = b'amc_api_log'
bufferSize = 1024
logOpt.sizePerFile = bufferSize
AmcApi.Amc_SetApiLog(logDir, baseName, byref(logOpt), bufferSize)
```

##### Amc_StartApiLog
```cpp
U32 Amc_StartApiLog()
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

Amc_StartApiLog()
```

##### Amc_StopApiLog
```cpp
U32 Amc_StopApiLog()
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

Amc_StopApiLog()
```

##### Amc_OpenApiLogFile
```cpp
U32 Amc_OpenApiLogFile(const char* filePath, FILE** pFile)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

def convert_filetime_to_datetime(self, filetime_int: int):
    """
    將一個 64-bit Windows FILETIME (I64) 轉換為
    人類可讀的 (human-readable) 本地時區 datetime 物件。

    FILETIME 是自 1601-01-01 0000 UTC 起的 100 奈秒間隔數。
    """
    # 1. 定義 FILETIME 的起始時間 (epoch)
    epoch = datetime.datetime(1601, 1, 1, tzinfo=datetime.timezone.utc)
    # 2. 計算總共的微秒數 (microseconds)
    # 1 微秒 = 10 個 (100奈秒) 間隔
    microseconds_delta = filetime_int / 10
    # 3. 建立時間差 (timedelta)
    delta = datetime.timedelta(microseconds=microseconds_delta)
    # 4. 計算出正確的 UTC 時間
    utc_time = epoch + delta
    # 5. 轉換為系統的本地時區 (例如: CST)
    local_time = utc_time.astimezone(None)
    return local_time

pfile = c_void_p()
file_name = b"D:\\TestLog_20251215_195932_443.dat"
api_header = AMC_API_LOG_HEADER()
out_str = create_string_buffer(1024)
stopCnd = 0
cnt = 0
Amc_OpenApiLogFile(file_name, byref(pfile))
while stopCnd != ErrorCode2.NoMoreLogData:
    data_buffer = (c_uint8 * 1024)()
    stopCnd = Amc_GetApiLogData(pfile, data_buffer, 1024, byref(api_header))
    print(f'stopCnd:0x{stopCnd:x}')
    print(f'header.len={api_header.dataLen}')
    print(f"type={'Command' if api_header.type == AMC_API_LOG_DATA_TYPE.LogCommand.value else 'Response'}, functionId={api_header.functionId}")
    if stopCnd == ErrorCode2.SUCCESS:
        Amc_ApiLogToString(byref(api_header), data_buffer, out_str, 1024)
        output = out_str.value.decode('utf-8')
        print(f'{convert_filetime_to_datetime(api_header.timestamp)}|{output}')
        cnt = cnt + 1
        print(f'cnt:{cnt}\n')
Amc_CloseApiLogFile(pfile)
```

##### Amc_GetApiLogData
```cpp
U32 Amc_GetApiLogData(FILE* pFile, U8* pDataBuff, U32 bufferSize, AMCApiLogHeader* pApiLogInfo)
```

##### Amc_CloseApiLogFile
```cpp
U32 Amc_CloseApiLogFile(FILE* pFile);
```

##### Amc_ApiLogToString
```cpp
U32 Amc_ApiLogToString(const AMCApiLogHeader* info, const U8* rawData, I8* outString, U64 outSize)
```

##### Amc_ApiLogGetStatus
```cpp
U32 Amc_ApiLogGetStatus(AMCAPILogStatus* status)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

getStatus = AMC_API_LOG_STATUS()
Amc_ApiLogGetStatus(byref(getStatus))
```

##### Amc_DataLog_SetLog
```cpp
U32 Amc_DataLog_SetLog(U32 DevID, U32 Channel, const LogDataSource* source, U16 index)
```

```python
import time
import unittest
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2, AmcLogAPI
from AcmP.AdvMotErr_CM2 import ErrorCode2
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *

dataLogSource = AMC_DATA_LOG_SOURCE()
dataLogSource.type = c_uint(AMC_DATA_LOG_SOURCE_TYPE.LOG_SOURCE_MOTION_AXIS.value)
dataLogSource.selection[0] = c_uint32(0)
dataLogSource.count = 1
dataLogSource.items.smItems = AMC_DATA_LOG_SM_ITEMS()
dataLogSource.items.smItems.cmd_pos = c_uint8(True)
dataLogSource.items.smItems.act_pos = c_uint8(True)
dataLogSource.items.smItems.cmd_vel = c_uint8(True)
dataLogSource.items.smItems.act_vel = c_uint8(True)
log_ch = c_uint32(1)
log_index = c_uint16(0)
Amc_DataLog_SetLog(devID, log_ch, byref(dataLogSource), log_index)
```

##### Amc_DataLog_GetLog
```cpp
U32 Amc_DataLog_GetLog(U32 DevID, U32 Channel, LogDataSource* source, U16 index)
```

```python
import time
import unittest
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2, AmcLogAPI
from AcmP.AdvMotErr_CM2 import ErrorCode2
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *

getDataLogSource = AMC_DATA_LOG_SOURCE()
log_ch = c_uint32(1)
log_index = c_uint16(0)
Amc_DataLog_GetLog(devID, log_ch, byref(getDataLogSource), log_index)
```

##### Amc_DataLog_SetLogOption
```cpp
U32 Amc_DataLog_SetLogOption(U32 DevID, U32 Channel, const DataLogOptions* options)
```

```python
import time
import unittest
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2, AmcLogAPI
from AcmP.AdvMotErr_CM2 import ErrorCode2
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *

dataLogOption = AMC_DATA_LOG_OPTIONS()
dataLogOption.isRotateFile = c_uint8(False)
dataLogOption.maxLogFileCount = c_uint32(1)
log_ch = c_uint32(1)
Amc_DataLog_SetLogOption(devID, log_ch, byref(dataLogOption))
```

##### Amc_DataLog_GetLogOption
```cpp
U32 Amc_DataLog_GetLogOption(U32 DevID, U32 Channel, DataLogOptions* options)
```

```python
import time
import unittest
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2, AmcLogAPI
from AcmP.AdvMotErr_CM2 import ErrorCode2
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *

log_ch = c_uint32(1)
getDataLogOption = AMC_DATA_LOG_OPTIONS()
Amc_DataLog_GetLogOption(devID, log_ch, byref(getDataLogOption))
```

##### Amc_DataLog_SetLogFilePath
```cpp
U32 Amc_DataLog_SetLogFilePath(U32 DevID, U32 Channel, const char* dirPath, const char* fileName)
```

```python
import time
import unittest
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2, AmcLogAPI
from AcmP.AdvMotErr_CM2 import ErrorCode2
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *

log_ch = c_uint32(1)
dirPath = b'/tmp'
fileName = b'PyTestDataLog'
Amc_DataLog_SetLogFilePath(devID, log_ch, dirPath, fileName)
```

##### Amc_DataLog_GetLogFilePath
```cpp
U32 Amc_DataLog_GetLogFilePath(U32 DevID, U32 Channel, char* dirPath, char* fileName)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
getDirPath = create_string_buffer(256)
getFileName = create_string_buffer(256)
Amc_DataLog_GetLogFilePath(devID, log_ch, getDirPath, getFileName)
```

##### Amc_DataLog_GetRotatedLogFilePaths
```cpp
U32 Amc_DataLog_GetRotatedLogFilePaths(U32 DevID, U32 Channel, char* fileNamesBuffer, U32* bufferSize, PU32 fileCount)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
fileBufferSize = c_uint32(1024)
getFilePath = create_string_buffer(fileBufferSize.value)
getFileCnt = c_uint32(0)
Amc_DataLog_GetRotatedLogFilePaths(devID, log_ch, getFilePath, byref(fileBufferSize), byref(getFileCnt))
```

##### Amc_DataLog_SetLogHeader
```cpp
U32 Amc_DataLog_SetLogHeader(U32 DevID, U32 Channel, const char* header)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
logHeader = b'Data Log Test from python'
Amc_DataLog_SetLogHeader(devID, log_ch, logHeader)
```

##### Amc_DataLog_GetLogHeader
```cpp
U32 Amc_DataLog_GetLogHeader(U32 DevID, U32 Channel, char* header)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
getLogHeader = create_string_buffer(256)
Amc_DataLog_GetLogHeader(devID, log_ch, getLogHeader)
```

##### Amc_DataLog_GetStatus
```cpp
U32 Amc_DataLog_GetStatus(U32 DevID, U32 Channel, LogStatus* outStatus)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
getDataLogStatus = AMC_DATA_LOG_STATUS()
Amc_DataLog_GetStatus(devID, log_ch, byref(getDataLogStatus))
```

##### Amc_DataLog_StartLog
```cpp
U32 Amc_DataLog_StartLog(U32 DevID, U32 Channel)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
Amc_DataLog_StartLog(devID, log_ch)
```

##### Amc_DataLog_StopLog
```cpp
U32 Amc_DataLog_StopLog(U32 DevID, U32 Channel)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
Amc_DataLog_StopLog(devID, log_ch)
```

##### Amc_DataLog_ResetLog
```cpp
U32 Amc_DataLog_ResetLog(U32 DevID, U32 Channel)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
Amc_DataLog_ResetLog(devID, log_ch)
```

##### Amc_DataLog_GetLogFile
```cpp
U32 Amc_DataLog_GetLogFile(U32 DevID, U32 Channel, const char* remoteFilePath, char* outBuffer, U32* bufferSize)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

bufferSize = 1024
currSize = bufferSize
fileBuffer = create_string_buffer(currSize)
log_ch = c_uint32(1)
filePath = b'/tmp/PyTestDataLog'
Amc_DataLog_GetLogFile(devID, log_ch, filePath, fileBuffer, byref(bufferSize))
```

---

