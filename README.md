# AcmP SDK
This SDK package allows developers to esaily use Advantech AdvMot api.

# Installation
This SDK supports Python version 3.10 or later
```shell
$ pip install -i pip install -i https://test.pypi.org/simple/ AcmP
```
Before using this package, please ensure the following items are already installed:
## Linux
1. PCIE-1203.ko
2. libadvmot.so
3. libpcie1203.so

You can check the installation using the following commands.
```shell
$ lsmod | grep PCI
$ ls /lib | grep adv
$ ls /lib | grep pci
```
## Windows
1. PCIE1203s.sys
2. ADVMOT.dll
3. PCIE1203.dll

You can check the installation using the following commands.
```shell
ls C:\Windows\System32\ | findstr ADVMOT
ls C:\Windows\System32\ | findstr PCIE1203
```
# Available Devices
* <a href="https://www.advantech.com/en/products/7d3c9775-8c30-4f65-83ec-755bee93b1d4/pcie-1203/mod_bb3ec42a-e9b1-4839-8b26-96551d894bb9">Advantech PCIE-1203</a>
# API
## How to use?
Due to our driver running with admin/root authentication, it's important to execute the project with admin/root privileges.

### AdvCmnAPI_CM2
* Device
    + <a href="#Acm2_DevOpen"><code>Acm2_DevOpen</code></a>
    + <a href="#Acm2_DevInitialize"><code>Acm2_DevInitialize</code></a>
    + <a href="#Acm2_GetAvailableDevs"><code>Acm2_GetAvailableDevs</code></a>
    + <a href="#Acm2_DevExportMappingTable"><code>Acm2_DevExportMappingTable</code></a>
    + <a href="#Acm2_DevImportMappingTable"><code>Acm2_DevImportMappingTable</code></a>
    + <a href="#Acm2_GetMappedLogicalIDList"><code>Acm2_GetMappedLogicalIDList</code></a>
    + <a href="#Acm2_GetMappedObjInfo"><code>Acm2_GetMappedObjInfo</code></a>
    + <a href="#Acm2_DevAllClose"><code>Acm2_DevAllClose</code></a>
    + <a href="#Acm2_GetLastError"><code>Acm2_GetLastError</code></a>
    + <a href="#Acm2_GetMappedPhysicalID"><code>Acm2_GetMappedPhysicalID</code></a>
    + <a href="#Acm2_SetProperty"><code>Acm2_SetProperty</code></a>
    + <a href="#Acm2_GetProperty"><code>Acm2_GetProperty</code></a>
    + <a href="#Acm2_SetMultiProperty"><code>Acm2_SetMultiProperty</code></a>
    + <a href="#Acm2_GetMultiProperty"><code>Acm2_GetMultiProperty</code></a>
    + <a href="#Acm2_GetRawProperty"><code>Acm2_GetRawProperty</code></a>
    + <a href="#Acm2_EnableCallBackFuncForOneEvent"><code>Acm2_EnableCallBackFuncForOneEvent</code></a>
    + <a href="#Acm2_DevLoadAllConfig"><code>Acm2_DevLoadAllConfig</code></a>
    + <a href="#Acm2_DevLoadConfig"><code>Acm2_DevLoadConfig</code></a>
    + <a href="#Acm2_DevReadMailBox"><code>Acm2_DevReadMailBox</code></a>
    + <a href="#Acm2_DevWriteMailBox"><code>Acm2_DevWriteMailBox</code></a>
    + <a href="#Acm2_GetErrors"><code>Acm2_GetErrors</code></a>
    + <a href="#Acm2_ResetErrorRecord"><code>Acm2_ResetErrorRecord</code></a>
    + <a href="#Acm2_DevPreviewMotion"><code>Acm2_DevPreviewMotion</code></a>
* Axis
    + <a href="#Acm2_AxReturnPausePosition"><code>Acm2_AxReturnPausePosition</code></a>
    + <a href="#Acm2_AxSetSvOn"><code>Acm2_AxSetSvOn</code></a>
    + <a href="#Acm2_DevSetAllSvOn"><code>Acm2_DevSetAllSvOn</code></a>
    + <a href="#Acm2_AxSetErcOn"><code>Acm2_AxSetErcOn</code></a>
    + <a href="#Acm2_AxResetAlm"><code>Acm2_AxResetAlm</code></a>
    + <a href="#Acm2_AxPTP"><code>Acm2_AxPTP</code></a>
    + <a href="#Acm2_AxMoveContinue"><code>Acm2_AxMoveContinue</code></a>
    + <a href="#Acm2_AxMotionStop"><code>Acm2_AxMotionStop</code></a>
    + <a href="#Acm2_AxHome"><code>Acm2_AxHome</code></a>
    + <a href="#Acm2_AxMoveGantryHome"><code>Acm2_AxMoveGantryHome</code></a>
    + <a href="#Acm2_AxSetHomeSpeedProfile"><code>Acm2_AxSetHomeSpeedProfile</code></a>
    + <a href="#Acm2_AxChangePos"><code>Acm2_AxChangePos</code></a>
    + <a href="#Acm2_AxChangeVel"><code>Acm2_AxChangeVel</code></a>
    + <a href="#Acm2_AxChangeVelByRate"><code>Acm2_AxChangeVelByRate</code></a>
    + <a href="#Acm2_AxMoveImpose"><code>Acm2_AxMoveImpose</code></a>
    + <a href="#Acm2_AxResetError"><code>Acm2_AxResetError</code></a>
    + <a href="#Acm2_DevResetAllError"><code>Acm2_DevResetAllError</code></a>
    + <a href="#Acm2_AxGetState"><code>Acm2_AxGetState</code></a>
    + <a href="#Acm2_AxGetMotionIO"><code>Acm2_AxGetMotionIO</code></a>
    + <a href="#Acm2_AxSetPosition"><code>Acm2_AxSetPosition</code></a>
    + <a href="#Acm2_AxGetPosition"><code>Acm2_AxGetPosition</code></a>
    + <a href="#Acm2_AxSetSpeedProfile"><code>Acm2_AxSetSpeedProfile</code></a>
    + <a href="#Acm2_AxGetVel"><code>Acm2_AxGetVel</code></a>
    + <a href="#Acm2_AxEnableExternalMode"><code>Acm2_AxEnableExternalMode</code></a>
    + <a href="#Acm2_AxSoftJog"><code>Acm2_AxSoftJog</code></a>
    + <a href="#Acm2_AxSetJogSpeedProfile"><code>Acm2_AxSetJogSpeedProfile</code></a>
    + <a href="#Acm2_AxMotionStart"><code>Acm2_AxMotionStart</code></a>
    + <a href="#Acm2_AxPause"><code>Acm2_AxPause</code></a>
    + <a href="#Acm2_AxResume"><code>Acm2_AxResume</code></a>
    + <a href="#Acm2_AxResetPVTTable"><code>Acm2_AxResetPVTTable</code></a>
    + <a href="#Acm2_AxLoadPVTTable"><code>Acm2_AxLoadPVTTable</code></a>
    + <a href="#Acm2_AxLoadPVTTableContinuous"><code>Acm2_AxLoadPVTTableContinuous</code></a>
    + <a href="#Acm2_AxMovePVT"><code>Acm2_AxMovePVT</code></a>
    + <a href="#Acm2_AxCheckPTBuffer"><code>Acm2_AxCheckPTBuffer</code></a>
    + <a href="#Acm2_AxAddPTData"><code>Acm2_AxAddPTData</code></a>
    + <a href="#Acm2_AxMovePT"><code>Acm2_AxMovePT</code></a>
    + <a href="#Acm2_AxResetPTData"><code>Acm2_AxResetPTData</code></a>
    + <a href="#Acm2_AxGearIn"><code>Acm2_AxGearIn</code></a>
    + <a href="#Acm2_AxGantryIn"><code>Acm2_AxGantryIn</code></a>
    + <a href="#Acm2_AxPhaseAx"><code>Acm2_AxPhaseAx</code></a>
    + <a href="#Acm2_AxSyncOut"><code>Acm2_AxSyncOut</code></a>
* Group
    + <a href="#Acm2_GpGetPausePosition"><code>Acm2_GpGetPausePosition</code></a>
    + <a href="#Acm2_GpCreate"><code>Acm2_GpCreate</code></a>
    + <a href="#Acm2_GpGetAxesInGroup"><code>Acm2_GpGetAxesInGroup</code></a>
    + <a href="#Acm2_GpResetError"><code>Acm2_GpResetError</code></a>
    + <a href="#Acm2_GpLine"><code>Acm2_GpLine</code></a>
    + <a href="#Acm2_GpArc_Center"><code>Acm2_GpArc_Center</code></a>
    + <a href="#Acm2_GpArc_3P"><code>Acm2_GpArc_3P</code></a>
    + <a href="#Acm2_GpArc_Angle"><code>Acm2_GpArc_Angle</code></a>
    + <a href="#Acm2_Gp3DArc_Center"><code>Acm2_Gp3DArc_Center</code></a>
    + <a href="#Acm2_Gp3DArc_NormVec"><code>Acm2_Gp3DArc_NormVec</code></a>
    + <a href="#Acm2_Gp3DArc_3P"><code>Acm2_Gp3DArc_3P</code></a>
    + <a href="#Acm2_Gp3DArc_3PAngle"><code>Acm2_Gp3DArc_3PAngle</code></a>
    + <a href="#Acm2_GpHelix_Center"><code>Acm2_GpHelix_Center</code></a>
    + <a href="#Acm2_GpHelix_3P"><code>Acm2_GpHelix_3P</code></a>
    + <a href="#Acm2_GpHelix_Angle"><code>Acm2_GpHelix_Angle</code></a>
    + <a href="#Acm2_GpResume"><code>Acm2_GpResume</code></a>
    + <a href="#Acm2_GpPause"><code>Acm2_GpPause</code></a>
    + <a href="#Acm2_GpMotionStop"><code>Acm2_GpMotionStop</code></a>
    + <a href="#Acm2_GpChangeVel"><code>Acm2_GpChangeVel</code></a>
    + <a href="Acm2_GpChangeVelByRate"><code>Acm2_GpChangeVelByRate</code></a>
    + <a href="#Acm2_GpGetVel"><code>Acm2_GpGetVel</code></a>
    + <a href="#Acm2_GpSetSpeedProfile"><code>Acm2_GpSetSpeedProfile</code></a>
    + <a href="#Acm2_GpGetState"><code>Acm2_GpGetState</code></a>
    + <a href="#Acm2_GpLoadPath"><code>Acm2_GpLoadPath</code></a>
    + <a href="#Acm2_GpAddPath"><code>Acm2_GpAddPath</code></a>
    + <a href="#Acm2_GpMovePath"><code>Acm2_GpMovePath</code></a>
    + <a href="#Acm2_GpResetPath"><code>Acm2_GpResetPath</code></a>
    + <a href="#Acm2_GpGetPathStatus"><code>Acm2_GpGetPathStatus</code></a>
    + <a href="#Acm2_GpMoveSelPath"><code>Acm2_GpMoveSelPath</code></a>
    + <a href="#Acm2_GpGetPathIndexStatus"><code>Acm2_GpGetPathIndexStatus</code></a>
    + <a href="#Acm2_GpDelay"><code>Acm2_GpDelay</code></a>
    + <a href="#Acm2_GpPathDO"><code>Acm2_GpPathDO</code></a>
    + <a href="#Acm2_GpPathWaitDI"><code>Acm2_GpPathWaitDI</code></a>
    + <a href="#Acm2_GpPathWaitForAxis"><code>Acm2_GpPathWaitForAxis</code></a>
    + <a href="#Acm2_GpLookAheadPath"><code>Acm2_GpLookAheadPath</code></a>
    + <a href="#Acm2_GpLookAheadPathFile"><code>Acm2_GpLookAheadPathFile</code></a>
    + <a href="#Acm2_GpLoadAndMovePath"><code>Acm2_GpLoadAndMovePath</code></a>
* DIO
    + <a href="#Acm2_ChSetDOBit"><code>Acm2_ChSetDOBit</code></a>
    + <a href="#Acm2_ChGetDOBit"><code>Acm2_ChGetDOBit</code></a>
    + <a href="#Acm2_ChGetDIBit"><code>Acm2_ChGetDIBit</code></a>
    + <a href="#Acm2_ChSetDOBitByRingN"><code>Acm2_ChSetDOBitByRingN</code></a>
    + <a href="#Acm2_ChGetDOBitByRingN"><code>Acm2_ChGetDOBitByRingN</code></a>
    + <a href="#Acm2_ChGetDIBitByRingN"><code>Acm2_ChGetDIBitByRingN</code></a>
    + <a href="#Acm2_ChSetDOByte"><code>Acm2_ChSetDOByte</code></a>
    + <a href="#Acm2_ChGetDOByte"><code>Acm2_ChGetDOByte</code></a>
    + <a href="#Acm2_ChGetDIByte"><code>Acm2_ChGetDIByte</code></a>
    + <a href="#Acm2_ChSetDOByteByRingNo"><code>Acm2_ChSetDOByteByRingNo</code></a>
    + <a href="#Acm2_ChGetDOByteByRingNo"><code>Acm2_ChGetDOByteByRingNo</code></a>
    + <a href="#Acm2_ChGetDIByteByRingNo"><code>Acm2_ChGetDIByteByRingNo</code></a>
* AIO
    + <a href="#Acm2_ChSetAOData"><code>Acm2_ChSetAOData</code></a>
    + <a href="#Acm2_ChGetAOData"><code>Acm2_ChGetAOData</code></a>
    + <a href="#Acm2_ChSetAODataByRingNo"><code>Acm2_ChSetAODataByRingNo</code></a>
    + <a href="#Acm2_ChGetAODataByRingNo"><code>Acm2_ChGetAODataByRingNo</code></a>
    + <a href="#Acm2_ChGetAIData"><code>Acm2_ChGetAIData</code></a>
    + <a href="#Acm2_ChGetAIDataByRingNo"><code>Acm2_ChGetAIDataByRingNo</code></a>
    + <a href="#Acm2_ChGetCntData"><code>Acm2_ChGetCntData</code></a>
    + <a href="#Acm2_ChSetCntData"><code>Acm2_ChSetCntData</code></a>
    + <a href="#Acm2_ChLinkCmpFIFO"><code>Acm2_ChLinkCmpFIFO</code></a>
    + <a href="#Acm2_ChLinkCmpObject"><code>Acm2_ChLinkCmpObject</code></a>
    + <a href="#Acm2_ChGetLinkedCmpObject"><code>Acm2_ChGetLinkedCmpObject</code></a>
    + <a href="#Acm2_ChEnableCmp"><code>Acm2_ChEnableCmp</code></a>
    + <a href="#Acm2_ChSetCmpOut"><code>Acm2_ChSetCmpOut</code></a>
    + <a href="#Acm2_ChSetCmpDoOut"><code>Acm2_ChSetCmpDoOut</code></a>
    + <a href="#Acm2_AxGetCmpData"><code>Acm2_AxGetCmpData</code></a>
    + <a href="#Acm2_ChGetCmpData"><code>Acm2_ChGetCmpData</code></a>
    + <a href="#Acm2_AxSetCmpTable"><code>Acm2_AxSetCmpTable</code></a>
    + <a href="#Acm2_AxSetCmpAuto"><code>Acm2_AxSetCmpAuto</code></a>
    + <a href="#Acm2_ChSetCmpAuto"><code>Acm2_ChSetCmpAuto</code></a>
    + <a href="#Acm2_ChSetCmpBufferData"><code>Acm2_ChSetCmpBufferData</code></a>
    + <a href="#Acm2_ChSetMultiCmpTable"><code>Acm2_ChSetMultiCmpTable</code></a>
    + <a href="#Acm2_ChSetMultiCmpBufferData"><code>Acm2_ChSetMultiCmpBufferData</code></a>
    + <a href="#Acm2_ChResetCmpData"><code>Acm2_ChResetCmpData</code></a>
    + <a href="#Acm2_ChGetCmpBufferStatus"><code>Acm2_ChGetCmpBufferStatus</code></a>
    + <a href="#Acm2_ChLinkLatchAxis"><code>Acm2_ChLinkLatchAxis</code></a>
    + <a href="#Acm2_ChLinkLatchObject"><code>Acm2_ChLinkLatchObject</code></a>
    + <a href="#Acm2_ChGetLinkedLatchObject"><code>Acm2_ChGetLinkedLatchObject</code></a>
    + <a href="#Acm2_ChTriggerLatch"><code>Acm2_ChTriggerLatch</code></a>
    + <a href="#Acm2_AxReadLatchBuffer"><code>Acm2_AxReadLatchBuffer</code></a>
    + <a href="#Acm2_ChReadLatchBuffer"><code>Acm2_ChReadLatchBuffer</code></a>
    + <a href="#Acm2_AxGetLatchBufferStatus"><code>Acm2_AxGetLatchBufferStatus</code></a>
    + <a href="#Acm2_ChGetLatchBufferStatus"><code>Acm2_ChGetLatchBufferStatus</code></a>
    + <a href="#Acm2_AxResetLatchBuffer"><code>Acm2_AxResetLatchBuffer</code></a>
    + <a href="#Acm2_ChResetLatchBuffer"><code>Acm2_ChResetLatchBuffer</code></a>
    + <a href="#Acm2_ChLinkPWMTable"><code>Acm2_ChLinkPWMTable</code></a>
    + <a href="#Acm2_ChGetLinkedPWMTable"><code>Acm2_ChGetLinkedPWMTable</code></a>
    + <a href="#Acm2_ChSetPWMTable"><code>Acm2_ChSetPWMTable</code></a>
    + <a href="#Acm2_ChLoadPWMTableFile"><code>Acm2_ChLoadPWMTableFile</code></a>
    + <a href="#Acm2_ChGetPWMTableStatus"><code>Acm2_ChGetPWMTableStatus</code></a>
    + <a href="#Acm2_ChGetExtDriveData"><code>Acm2_ChGetExtDriveData</code></a>
    + <a href="#Acm2_ChSetExtDriveData"><code>Acm2_ChSetExtDriveData</code></a>
    + <a href="#Acm2_ChLinkExtDriveObject"><code>Acm2_ChLinkExtDriveObject</code></a>
    + <a href="#Acm2_ChGetLinkedExtDriveObject"><code>Acm2_ChGetLinkedExtDriveObject</code></a>
    + <a href="#Acm2_DevMDaqConfig"><code>Acm2_DevMDaqConfig</code></a>
    + <a href="#Acm2_DevMDaqGetConfig"><code>Acm2_DevMDaqGetConfig</code></a>
    + <a href="#Acm2_DevMDaqStart"><code>Acm2_DevMDaqStart</code></a>
    + <a href="#Acm2_DevMDaqStop"><code>Acm2_DevMDaqStop</code></a>
    + <a href="#Acm2_DevMDaqReset"><code>Acm2_DevMDaqReset</code></a>
    + <a href="#Acm2_DevMDaqGetStatus"><code>Acm2_DevMDaqGetStatus</code></a>
    + <a href="#Acm2_DevMDaqGetData"><code>Acm2_DevMDaqGetData</code></a>
    + <a href="#Acm2_GetDSPFrmWareDwnLoadRate"><code>Acm2_GetDSPFrmWareDwnLoadRate</code></a>
* EtherCAT
    + <a href="#Acm2_DevLoadENI"><code>Acm2_DevLoadENI</code></a>
    + <a href="#Acm2_DevConnect"><code>Acm2_DevConnect</code></a>
    + <a href="#Acm2_DevDisConnect"><code>Acm2_DevDisConnect</code></a>
    + <a href="#Acm2_DevGetSubDevicesID"><code>Acm2_DevGetSubDevicesID</code></a>
    + <a href="#Acm2_DevGetMDeviceInfo"><code>Acm2_DevGetMDeviceInfo</code></a>
    + <a href="#Acm2_DevGetSubDeviceInfo"><code>Acm2_DevGetSubDeviceInfo</code></a>
    + <a href="#Acm2_DevGetSubDeviceFwVersion"><code>Acm2_DevGetSubDeviceFwVersion</code></a>
    + <a href="#Acm2_DevSetSubDeviceID"><code>Acm2_DevSetSubDeviceID</code></a>
    + <a href="#Acm2_DevSetSubDeviceStates"><code>Acm2_DevSetSubDeviceStates</code></a>
    + <a href="#Acm2_DevGetSubDeviceStates"><code>Acm2_DevGetSubDeviceStates</code></a>
    + <a href="#Acm2_DevWriteSDO"><code>Acm2_DevWriteSDO</code></a>
    + <a href="#Acm2_DevReadSDO"><code>Acm2_DevReadSDO</code></a>
    + <a href="#Acm2_DevWritePDO"><code>Acm2_DevWritePDO</code></a>
    + <a href="#Acm2_DevReadPDO"><code>Acm2_DevReadPDO</code></a>
    + <a href="#Acm2_DevWriteReg"><code>Acm2_DevWriteReg</code></a>
    + <a href="#Acm2_DevReadReg"><code>Acm2_DevReadReg</code></a>
    + <a href="#Acm2_DevReadSubDeviceCommErrCnt"><code>Acm2_DevReadSubDeviceCommErrCnt</code></a>
    + <a href="#Acm2_Ax1DCompensateTable"><code>Acm2_Ax1DCompensateTable</code></a>
    + <a href="#Acm2_Ax2DCompensateTable"><code>Acm2_Ax2DCompensateTable</code></a>
    + <a href="#Acm2_AxZAxisCompensateTable"><code>Acm2_AxZAxisCompensateTable</code></a>
    + <a href="#Acm2_AxGetCompensatePosition"><code>Acm2_AxGetCompensatePosition</code></a>
    + <a href="#Acm2_DevOscChannelDataStart"><code>Acm2_DevOscChannelDataStart</code></a>
    + <a href="#Acm2_DevOscChannelDataStop"><code>Acm2_DevOscChannelDataStop</code></a>
    + <a href="#Acm2_DevGetOscChannelDataConfig"><code>Acm2_DevGetOscChannelDataConfig</code></a>
    + <a href="#Acm2_DevSetOscChannelDataConfig"><code>Acm2_DevSetOscChannelDataConfig</code></a>
    + <a href="#Acm2_DevGetOscChannelData"><code>Acm2_DevGetOscChannelData</code></a>
    + <a href="#Acm2_DevGetOscChannelStatus"><code>Acm2_DevGetOscChannelStatus</code></a>
----
<a name="Acm2_GetAvailableDevs"></a>

### Acm2_GetAvailableDevs
Get all device list.

<a name="Acm2_DevOpen"></a>

#### Acm2_DevOpen
Open device with device number.

<a name="Acm2_DevExportMappingTable"></a>

#### Acm2_DevExportMappingTable
Export mapping table of device.

<a name="Acm2_DevImportMappingTable"></a>

#### Acm2_DevImportMappingTable
Import mapping table of device.

<a name="Acm2_GetMappedPhysicalID"></a>

#### Acm2_GetMappedPhysicalID
Get mapped physical id of device.

<a name="Acm2_GetMappedLogicalIDList"></a>

#### Acm2_GetMappedLogicalIDList
Get mapped list of logical id.

<a name="Acm2_GetMappedObjInfo"></a>

#### Acm2_GetMappedObjInfo
Get mapped object information.

<a name="Acm2_DevAllClose"></a>

#### Acm2_DevAllClose
Close all device at same time.

```python
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.MotionInfo import DEVICEINFO

number_hex = '0x63000000'
number_int = int(number_hex, 16)
device_number = c_uint32(number_int)
dev_list = (DEVLIST*10)()
device_info = DEVICEINFO()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Then open
errCde = AdvMot.Acm2_DevOpen(device_number, byref(device_info))
# Close device
errCde = AdvMot.Acm2_DevAllClose()
```

<a name="Acm2_DevInitialize"></a>

#### Acm2_DevInitialize
Initial the device.

<a name="Acm2_AxGetPosition"></a>

#### Acm2_AxGetPosition
Get axis position by axis number, and position type.

```python
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotDrv import POSITION_TYPE

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()
axid = c_uint32(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
pos = c_double(0)
# Get axis 0 command position
errCde = AdvMot.Acm2_AxGetPosition(axid, pos_type, byref(pos))
```
<a name="Acm2_AxPTP"></a>

#### Acm2_AxPTP
Set axis move with position.

<a name="Acm2_AxGetState"></a>

#### Acm2_AxGetState
Get axis state.

```python
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotDrv import POSITION_TYPE, ABS_MODE, AXIS_STATUS_TYPE

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()
axid = c_uint32(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
pos = c_double(0)
distance = c_double(1000)
abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
state = c_uint32(16)
# Get axis 0 command position
errCde = AdvMot.Acm2_AxGetPosition(axid, pos_type, byref(pos))
# Move axis 0 to position 1000(command position)
errCde = AdvMot.Acm2_AxPTP(axid, abs_mode, distance)
# Check axis 0 status
errCde = AdvMot.Acm2_AxGetState(axid, state_type, byref(state))
```
<a name="Acm2_SetProperty"></a>

#### Acm2_SetProperty
Set device/axis property.

<a name="Acm2_GetProperty"></a>

#### Acm2_GetProperty
Get device/axis property.

```python
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()
do_ch = c_uint32(0)
property_id = c_uint(PropertyID2.CFG_CH_DaqDoFuncSelect.value)
val = c_double(1)
# Set local DO channel 0 as gerneral DO
errCde = AdvMot.Acm2_SetProperty(do_ch, property_id, val)
get_val = c_double(0)
# Get local DO channel 0 property value
errCde = AdvMot.Acm2_GetProperty(do_ch, property_id, byref(get_val))
```
<a name="Acm2_SetMultiProperty"></a>

#### Acm2_SetMultiProperty
Set multiple properties at once.

<a name="Acm2_GetMultiProperty"></a>

#### Acm2_GetMultiProperty
Get multiple properties at once.

```python
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()
# Set axis 0 speed info at once
ax_id = c_uint32(0)
property_arr = [c_uint32(PropertyID2.PAR_AxVelLow.value), c_uint32(PropertyID2.PAR_AxVelHigh.value)]
trans_ppt_arr = (c_uint32 * len(property_arr))(*property_arr)
# Default value of velocity low is 2000, and velocity high is 8000.
value_arr = [c_double(1000), c_double(2000)]
trans_val_arr = (c_double * len(value_arr))(*value_arr)
data_cnt = c_uint32(2)
err_buffer = (c_uint32 * data_cnt.value)()
# Set value
errCde = AdvMot.Acm2_SetMultiProperty(ax_id, trans_ppt_arr, trans_val_arr, data_cnt, err_buffer)
# Check value
get_val = (c_double * data_cnt.value)()
errCde = AdvMot.Acm2_GetMultiProperty(ax_id, trans_ppt_arr, get_val, data_cnt, err_buffer)
for i in range(data_cnt.value):
    print('set[{0}]:{1}, get:{2}'.format(i, value_arr[i].value, get_val[i]))
```
<a name="Acm2_GetRawProperty"></a>

#### Acm2_GetRawProperty
Get raw property value.

<a name="Acm2_EnableCallBackFuncForOneEvent"></a>

#### Acm2_EnableCallBackFuncForOneEvent
Set callback function for event.

<a name="Acm2_DevLoadAllConfig"></a>

#### Acm2_DevLoadAllConfig
Load all configuration at once.

<a name="Acm2_DevLoadConfig"></a>

#### Acm2_DevLoadConfig
Load configuration.

<a name="Acm2_DevReadMailBox"></a>

#### Acm2_DevReadMailBox
Read mailbox of device.

<a name="Acm2_DevWriteMailBox"></a>

#### Acm2_DevWriteMailBox
Write mailbox of device.

<a name="Acm2_GetErrors"></a>

#### Acm2_GetErrors
Get error of device.

<a name="Acm2_ResetErrorRecord"></a>

#### Acm2_ResetErrorRecord
Reset error.

<a name="Acm2_DevPreviewMotion"></a>

#### Acm2_DevPreviewMotion
Preview motion.

<a name="Acm2_ChSetDOBit"></a>

#### Acm2_ChSetDOBit
Set DO bit by channel.

<a name="Acm2_ChGetDOBit"></a>

#### Acm2_ChGetDOBit
Get DO bit by channel.

```python
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()
do_ch = c_uint32(0)
property_id = c_uint(PropertyID2.CFG_CH_DaqDoFuncSelect.value)
val = c_double(1)
# Set local DO channel 0 as gerneral DO
errCde = AdvMot.Acm2_SetProperty(do_ch, property_id, val)
get_val = c_double(0)
# Get local DO channel 0 property value
errCde = AdvMot.Acm2_GetProperty(do_ch, property_id, byref(get_val))
# Set local DO channel 0 ON
data = c_uint32(1)
errCde = AdvMot.Acm2_ChSetDOBit(do_ch, data)
# Get local DO channel 0 value
get_data = c_uint32(0)
errCde = AdvMot.Acm2_ChGetDOBit(do_ch, byref(get_data))
```
<a name="Acm2_GetLastError"></a>

#### Acm2_GetLastError
Get last error of system.

<a name="Acm2_AxReturnPausePosition"></a>

#### Acm2_AxReturnPausePosition
Get axis pause position.

<a name="Acm2_AxSetSvOn"></a>

#### Acm2_AxSetSvOn
Set axis servo on/off.

<a name="Acm2_DevSetAllSvOn"></a>

#### Acm2_DevSetAllSvOn
Set all axes servo on.off.

<a name="Acm2_AxSetErcOn"></a>

#### Acm2_AxSetErcOn
Set axis erc on/off.

<a name="Acm2_AxResetAlm"></a>

#### Acm2_AxResetAlm
Reset axis alarm logic.

<a name="Acm2_AxMoveContinue"></a>

#### Acm2_AxMoveContinue
Set aixs continue move.

<a name="Acm2_AxMotionStop"></a>

#### Acm2_AxMotionStop
Force axis stop motion.

<a name="Acm2_AxHome"></a>

#### Acm2_AxHome
Set axis moving home with direction and home mode.

<a name="Acm2_AxMoveGantryHome"></a>

#### Acm2_AxMoveGantryHome
Set axis moving home with gantry.

<a name="Acm2_AxSetHomeSpeedProfile"></a>

#### Acm2_AxSetHomeSpeedProfile
Set axis home speed config.

<a name="Acm2_AxChangePos"></a>

#### Acm2_AxChangePos
Set axis position.

<a name="Acm2_AxChangeVel"></a>

#### Acm2_AxChangeVel
Set axis velocity.

<a name="Acm2_AxChangeVelByRate"></a>

#### Acm2_AxChangeVelByRate
Set axis velocity by rate.

<a name="Acm2_AxMoveImpose"></a>

#### Acm2_AxMoveImpose
Set axis impose.

<a name="Acm2_AxResetError"></a>

#### Acm2_AxResetError
Reset error of axis.

<a name="Acm2_DevResetAllError"></a>

#### Acm2_DevResetAllError
Reset all device error.

```python
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()
# Clear all error
errCde = AdvMot.Acm2_DevResetAllError()

ax_id = c_uint32(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
pos = c_double(0)
# Set axis 0 command position as 0
errCde = AdvMot.Acm2_AxSetPosition(ax_id, pos_type, pos)
```
<a name="Acm2_AxGetMotionIO"></a>

#### Acm2_AxGetMotionIO
Get axis motion IO status.

<a name="Acm2_AxSetPosition"></a>

#### Acm2_AxSetPosition
Set axis position.

<a name="Acm2_AxSetSpeedProfile"></a>

#### Acm2_AxSetSpeedProfile
Set axis speed information.

<a name="Acm2_AxGetVel"></a>

#### Acm2_AxGetVel
Get axis velocity.

<a name="Acm2_AxEnableExternalMode"></a>

#### Acm2_AxEnableExternalMode
Enable axis external mode.

<a name="Acm2_AxSoftJog"></a>

#### Acm2_AxSoftJog
Set axis jog.

<a name="Acm2_AxSetJogSpeedProfile"></a>

#### Acm2_AxSetJogSpeedProfile
Set axis jog speed information.

<a name="Acm2_AxMotionStart"></a>

#### Acm2_AxMotionStart
Start motion.

<a name="Acm2_AxPause"></a>

#### Acm2_AxPause
Pause motion.

<a name="Acm2_AxResume"></a>

#### Acm2_AxResume
Resume motion.

<a name="Acm2_AxResetPVTTable"></a>

#### Acm2_AxResetPVTTable
Reset axis PVT table.

<a name="Acm2_AxLoadPVTTable"></a>

#### Acm2_AxLoadPVTTable
Load axis PVT table.

<a name="Acm2_AxLoadPVTTableContinuous"></a>

#### Acm2_AxLoadPVTTableContinuous
Continuous loading PVT table.

<a name="Acm2_AxMovePVT"></a>

#### Acm2_AxMovePVT
Move PVT motion.

<a name="Acm2_AxCheckPTBuffer"></a>

#### Acm2_AxCheckPTBuffer
Check axis PT buffer.

<a name="Acm2_AxAddPTData"></a>

#### Acm2_AxAddPTData
Add axis PT data.

<a name="Acm2_AxMovePT"></a>

#### Acm2_AxMovePT
Move PT motion.

<a name="Acm2_AxResetPTData"></a>

#### Acm2_AxResetPTData
Reset axis PT data.

<a name="Acm2_AxGearIn"></a>

#### Acm2_AxGearIn
Set axis gear.

<a name="Acm2_AxGantryIn"></a>

#### Acm2_AxGantryIn
Set axis gantry.

<a name="Acm2_AxPhaseAx"></a>

#### Acm2_AxPhaseAx
Set axis phase.

<a name="Acm2_AxSyncOut"></a>

#### Acm2_AxSyncOut
Lift the gantry.

<a name="Acm2_GpGetPausePosition"></a>

#### Acm2_GpGetPausePosition
Get group pause position.

<a name="Acm2_GpCreate"></a>

#### Acm2_GpCreate
Create group.

<a name="Acm2_GpGetAxesInGroup"></a>

#### Acm2_GpGetAxesInGroup
Check axes in group.

<a name="Acm2_GpResetError"></a>

#### Acm2_GpResetError
Reset error of group.

<a name="Acm2_GpLine"></a>

#### Acm2_GpLine
Move group in line.

<a name="Acm2_GpArc_Center"></a>

#### Acm2_GpArc_Center
Set group arc center.

<a name="Acm2_GpArc_3P"></a>

#### Acm2_GpArc_3P
Set group arc point.

<a name="Acm2_GpArc_Angle"></a>

#### Acm2_GpArc_Angle
Set group arc angle.

<a name="Acm2_Gp3DArc_Center"></a>

#### Acm2_Gp3DArc_Center
Set 3D group arc center.

<a name="Acm2_Gp3DArc_NormVec"></a>

#### Acm2_Gp3DArc_NormVec
Set 3D group arc norm vector.

<a name="Acm2_Gp3DArc_3P"></a>

#### Acm2_Gp3DArc_3P
Set 3D group arc point.

<a name="Acm2_Gp3DArc_3PAngle"></a>

#### Acm2_Gp3DArc_3PAngle
Set 3D group arc points, angle.

<a name="Acm2_GpHelix_Center"></a>

#### Acm2_GpHelix_Center
Set group helix center.

<a name="Acm2_GpHelix_3P"></a>

#### Acm2_GpHelix_3P
Set group helix points.

<a name="Acm2_GpHelix_Angle"></a>

#### Acm2_GpHelix_Angle
Set group helix angle.

<a name="Acm2_GpResume"></a>

#### Acm2_GpResume

<a name="Acm2_GpPause"></a>

#### Acm2_GpPause
Set group pause motion.

<a name="Acm2_GpMotionStop"></a>

#### Acm2_GpMotionStop
Stop group motion.

<a name="Acm2_GpChangeVel"></a>

#### Acm2_GpChangeVel
Change velocity of group.

<a name="Acm2_GpChangeVelByRate"></a>

#### Acm2_GpChangeVelByRate
Change group velocity by rate.

<a name="Acm2_GpGetVel"></a>

#### Acm2_GpGetVel
Get group velocity.

<a name="Acm2_GpSetSpeedProfile"></a>

#### Acm2_GpSetSpeedProfile
Get group speed information.

<a name="Acm2_GpGetState"></a>

#### Acm2_GpGetState
Get group status.

<a name="Acm2_GpLoadPath"></a>

#### Acm2_GpLoadPath
Load path table in group.

<a name="Acm2_GpAddPath"></a>

#### Acm2_GpAddPath
Add path into group.

<a name="Acm2_GpMovePath"></a>

#### Acm2_GpMovePath
Start move group after add path.

<a name="Acm2_GpResetPath"></a>

#### Acm2_GpResetPath
Reset group path table.

<a name="Acm2_GpGetPathStatus"></a>

#### Acm2_GpGetPathStatus
Get group path status.

<a name="Acm2_GpMoveSelPath"></a>

#### Acm2_GpMoveSelPath

<a name="Acm2_GpGetPathIndexStatus"></a>

#### Acm2_GpGetPathIndexStatus
Get group information by the index of path table.

<a name="Acm2_GpDelay"></a>

#### Acm2_GpDelay
Delay group.

<a name="Acm2_GpPathDO"></a>

#### Acm2_GpPathDO
Set device do on/off between path.

<a name="Acm2_GpPathWaitDI"></a>

#### Acm2_GpPathWaitDI
Wait DI status between path.

<a name="Acm2_GpPathWaitForAxis"></a>

#### Acm2_GpPathWaitForAxis
Wait axis between path.

<a name="Acm2_GpLookAheadPath"></a>

#### Acm2_GpLookAheadPath

<a name="Acm2_GpLookAheadPathFile"></a>

#### Acm2_GpLookAheadPathFile

<a name="Acm2_GpLoadAndMovePath"></a>

#### Acm2_GpLoadAndMovePath

<a name="Acm2_ChGetDIBit"></a>

#### Acm2_ChGetDIBit
Get DI bit by channel.

<a name="Acm2_ChSetDOBitByRingN"></a>

#### Acm2_ChSetDOBitByRingN
Set DO bit by channel, and ring number.

<a name="Acm2_ChGetDOBitByRingN"></a>

#### Acm2_ChGetDOBitByRingN
Get DO bit by ring number, and channel.

<a name="Acm2_ChGetDIBitByRingN"></a>

#### Acm2_ChGetDIBitByRingN
Get DI bit by ring number, and channel.

<a name="Acm2_ChSetDOByte"></a>

#### Acm2_ChSetDOByte
Set DO channel byte.

<a name="Acm2_ChGetDOByte"></a>

#### Acm2_ChGetDOByte
Get DO channel byte.

<a name="Acm2_ChGetDIByte"></a>

#### Acm2_ChGetDIByte
Get DI channel byte.

<a name="Acm2_ChSetDOByteByRingNo"></a>

#### Acm2_ChSetDOByteByRingNo
Set DO byte by ring number.

<a name="Acm2_ChGetDOByteByRingNo"></a>

#### Acm2_ChGetDOByteByRingNo
Get DO byte by ring number.

<a name="Acm2_ChGetDIByteByRingNo"></a>

#### Acm2_ChGetDIByteByRingNo
Get DI byte by ring number.

<a name="Acm2_ChSetAOData"></a>

#### Acm2_ChSetAOData
Set AO data.

<a name="Acm2_ChGetAOData"></a>

#### Acm2_ChGetAOData
Get AO data.

<a name="Acm2_ChSetAODataByRingNo"></a>

#### Acm2_ChSetAODataByRingNo
Set AO data by ring number.

<a name="Acm2_ChGetAODataByRingNo"></a>

#### Acm2_ChGetAODataByRingNo
Get AO data by ring number.

<a name="Acm2_ChGetAIData"></a>

#### Acm2_ChGetAIData
Get AI data.

<a name="Acm2_ChGetAIDataByRingNo"></a>

#### Acm2_ChGetAIDataByRingNo
Get AI data by ring number.

<a name="Acm2_ChGetCntData"></a>

#### Acm2_ChGetCntData
Get counter data.

<a name="Acm2_ChSetCntData"></a>

#### Acm2_ChSetCntData
Set counter data.

<a name="Acm2_ChLinkCmpFIFO"></a>

#### Acm2_ChLinkCmpFIFO
Set compare position.

<a name="Acm2_ChLinkCmpObject"></a>

#### Acm2_ChLinkCmpObject
Link compare do with axis/counter.

<a name="Acm2_ChGetLinkedCmpObject"></a>

#### Acm2_ChGetLinkedCmpObject
Get compare do linked object.

<a name="Acm2_ChEnableCmp"></a>

#### Acm2_ChEnableCmp
Enable compare channel.

<a name="Acm2_ChSetCmpOut"></a>

#### Acm2_ChSetCmpOut
Set compare channel on/off.

<a name="Acm2_ChSetCmpDoOut"></a>

#### Acm2_ChSetCmpDoOut
Set compare on/off.

<a name="Acm2_AxGetCmpData"></a>

#### Acm2_AxGetCmpData
Get compared data by axis.

<a name="Acm2_ChGetCmpData"></a>

#### Acm2_ChGetCmpData
Get compared data by channel.

<a name="Acm2_AxSetCmpTable"></a>

#### Acm2_AxSetCmpTable
Set compare table by axis.

<a name="Acm2_AxSetCmpAuto"></a>

#### Acm2_AxSetCmpAuto
Set auto compare by axis.

<a name="Acm2_ChSetCmpAuto"></a>

#### Acm2_ChSetCmpAuto
Set auto compare by channel.

<a name="Acm2_ChSetCmpBufferData"></a>

#### Acm2_ChSetCmpBufferData
Set compare buffer.

<a name="Acm2_ChSetMultiCmpTable"></a>

#### Acm2_ChSetMultiCmpTable
Set compare table.

<a name="Acm2_ChSetMultiCmpBufferData"></a>

#### Acm2_ChSetMultiCmpBufferData
Set multi compare buffer.

<a name="Acm2_ChResetCmpData"></a>

#### Acm2_ChResetCmpData
Reset compare data.

<a name="Acm2_ChGetCmpBufferStatus"></a>

#### Acm2_ChGetCmpBufferStatus
Get compared buffer status.

<a name="Acm2_ChLinkLatchAxis"></a>

#### Acm2_ChLinkLatchAxis
Link latch to axis.

<a name="Acm2_ChLinkLatchObject"></a>

#### Acm2_ChLinkLatchObject
Lift latch to object.

<a name="Acm2_ChGetLinkedLatchObject"></a>

#### Acm2_ChGetLinkedLatchObject
Get linked latch object.

<a name="Acm2_ChTriggerLatch"></a>

#### Acm2_ChTriggerLatch
Trigger latch by channel.

<a name="Acm2_AxReadLatchBuffer"></a>

#### Acm2_AxReadLatchBuffer
Read latch buffer.

<a name="Acm2_ChReadLatchBuffer"></a>

#### Acm2_ChReadLatchBuffer
Read latch buffer by channel.

<a name="Acm2_AxGetLatchBufferStatus"></a>

#### Acm2_AxGetLatchBufferStatus
Get latch buffer status.

<a name="Acm2_ChGetLatchBufferStatus"></a>

#### Acm2_ChGetLatchBufferStatus
Get latch buffer status by channel.

<a name="Acm2_AxResetLatchBuffer"></a>

#### Acm2_AxResetLatchBuffer
Reset latch buffer.

<a name="Acm2_ChResetLatchBuffer"></a>

#### Acm2_ChResetLatchBuffer
Reset latch buffer by channel.

<a name="Acm2_ChLinkPWMTable"></a>

#### Acm2_ChLinkPWMTable
Link PWM with object.

<a name="Acm2_ChGetLinkedPWMTable"></a>

#### Acm2_ChGetLinkedPWMTable
Get linked PWM Acm2_ChSetPWMTabletable by channel.

<a name="Acm2_ChSetPWMTable"></a>

#### Acm2_ChSetPWMTable
Set PWM table by channel.

<a name="Acm2_ChLoadPWMTableFile"></a>

#### Acm2_ChLoadPWMTableFile
Loal PWM table file.

<a name="Acm2_ChGetPWMTableStatus"></a>

#### Acm2_ChGetPWMTableStatus
Get PWM table status.

<a name="Acm2_ChGetExtDriveData"></a>

#### Acm2_ChGetExtDriveData
Get external drive data by channel.

<a name="Acm2_ChSetExtDriveData"></a>

#### Acm2_ChSetExtDriveData
Set external drive data by channel.

<a name="Acm2_ChLinkExtDriveObject"></a>

#### Acm2_ChLinkExtDriveObject
Link external drive object.

<a name="Acm2_ChGetLinkedExtDriveObject"></a>

#### Acm2_ChGetLinkedExtDriveObject
Get linked external drive object.

<a name="Acm2_DevMDaqConfig"></a>

#### Acm2_DevMDaqConfig
Set MDAQ config.

<a name="Acm2_DevMDaqGetConfig"></a>

#### Acm2_DevMDaqGetConfig
Get MDAQ config.

<a name="Acm2_DevMDaqStart"></a>

#### Acm2_DevMDaqStart
Start MDAQ.

<a name="Acm2_DevMDaqStop"></a>

#### Acm2_DevMDaqStop
Stop MDAQ.

<a name="Acm2_DevMDaqReset"></a>

#### Acm2_DevMDaqReset
Reset MDAQ.

<a name="Acm2_DevMDaqGetStatus"></a>

#### Acm2_DevMDaqGetStatus
Get MDAQ status.

<a name="Acm2_DevMDaqGetData"></a>

#### Acm2_DevMDaqGetData
Get MDAQ data.

<a name="Acm2_GetDSPFrmWareDwnLoadRate"></a>

#### Acm2_GetDSPFrmWareDwnLoadRate
Get FW download rate.

<a name="Acm2_DevLoadENI"></a>

#### Acm2_DevLoadENI
Download ENI file.

<a name="Acm2_DevConnect"></a>

#### Acm2_DevConnect
Connect subdevices.

<a name="Acm2_DevDisConnect"></a>

#### Acm2_DevDisConnect
Disconnect subdevices

<a name="Acm2_DevGetSubDevicesID"></a>

#### Acm2_DevGetSubDevicesID
Get subdevices id.

<a name="Acm2_DevGetMDeviceInfo"></a>

#### Acm2_DevGetMDeviceInfo
Get main device information.

<a name="Acm2_DevGetSubDeviceInfo"></a>

#### Acm2_DevGetSubDeviceInfo
Get subdevice information.

<a name="Acm2_DevGetSubDeviceFwVersion"></a>

#### Acm2_DevGetSubDeviceFwVersion
Get subdevice fw information.

<a name="Acm2_DevSetSubDeviceID"></a>

#### Acm2_DevSetSubDeviceID
Set subdevice id.

<a name="Acm2_DevSetSubDeviceStates"></a>

#### Acm2_DevSetSubDeviceStates
Set subdevice status.

<a name="Acm2_DevGetSubDeviceStates"></a>

#### Acm2_DevGetSubDeviceStates
Get subdevice states.

<a name="Acm2_DevWriteSDO"></a>

#### Acm2_DevWriteSDO
Write data by SDO.

<a name="Acm2_DevReadSDO"></a>

#### Acm2_DevReadSDO
Read data by SDO.

<a name="Acm2_DevWritePDO"></a>

#### Acm2_DevWritePDO
Write data by PDO.

<a name="Acm2_DevReadPDO"></a>

#### Acm2_DevReadPDO
Read data by PDO.

<a name="Acm2_DevWriteReg"></a>

#### Acm2_DevWriteReg
Write data by reg.

<a name="Acm2_DevReadReg"></a>

#### Acm2_DevReadReg
Read data by reg.

<a name="Acm2_DevReadSubDeviceCommErrCnt"></a>

#### Acm2_DevReadSubDeviceCommErrCnt
Read subdevice communication error counter.

<a name="Acm2_Ax1DCompensateTable"></a>

#### Acm2_Ax1DCompensateTable
Set compensate table with one axis.

<a name="Acm2_Ax2DCompensateTable"></a>

#### Acm2_Ax2DCompensateTable
Set compensate table in 2D.

<a name="Acm2_AxZAxisCompensateTable"></a>

#### Acm2_AxZAxisCompensateTable
Set compensate table in Z axis.

<a name="Acm2_AxGetCompensatePosition"></a>

#### Acm2_AxGetCompensatePosition
Get compensate position by axis.

<a name="Acm2_DevOscChannelDataStart"></a>

#### Acm2_DevOscChannelDataStart
Start Osc. channel data.

<a name="Acm2_DevOscChannelDataStop"></a>

#### Acm2_DevOscChannelDataStop
Stop Osc. channel data.

<a name="Acm2_DevGetOscChannelDataConfig"></a>

#### Acm2_DevGetOscChannelDataConfig
Get config of Osc. channel.

<a name="Acm2_DevSetOscChannelDataConfig"></a>

#### Acm2_DevSetOscChannelDataConfig
Set config of Osc. channel.

<a name="Acm2_DevGetOscChannelData"></a>

#### Acm2_DevGetOscChannelData
Get Osc. channel data.

<a name="Acm2_DevGetOscChannelStatus"></a>

#### Acm2_DevGetOscChannelStatus
Get Osc. channel status.