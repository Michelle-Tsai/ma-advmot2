# AcmP SDK
This SDK package allows developers to esaily use Advantech AdvMot api.

# Installation
This SDK supports Python version 3.10 or later
```shell
$ pip install AcmP
```
Before using this package, please ensure the following items are already installed:
## Linux
### Shared driver:
* libadvmot.so
### For PCIE-1203M:
1. pcie1203m.ko
2. libpcie1203.so
### For PCIE-1245
1. pcie1245.ko
2. libpcie1245.so

You can check the installation using the following commands.
```shell
$ lsmod | grep PCI
$ ls /lib | grep adv
$ ls /lib | grep pcie
```
## Windows
### Shared driver:
* ADVMOT.dll
### For PCIE-1203M:
1. PCIE1203Ms.sys
2. PCIE1203M.dll
### For PCIE-1245:
1. PCIE1245s.sys
2. PCIE1245.dll

You can check the installation using the following commands.
```shell
ls C:\Windows\System32\ | findstr ADVMOT
ls C:\Windows\System32\ | findstr PCIE1203
```
# Available Devices
* <a href="https://www.advantech.com/en/products/7d3c9775-8c30-4f65-83ec-755bee93b1d4/pcie-1203/mod_bb3ec42a-e9b1-4839-8b26-96551d894bb9">Advantech PCIE-1203M</a>
* <a href="https://www.advantech.com/zh-tw/products/e37baca6-8e5d-40f4-83c6-6bf379307dcf/pcie-1245/mod_212c4df1-455d-4153-8293-e0a216690702">Advantech PCIE-1245</>
# API
## How to use?
Due to our driver running with admin/root authentication, it's important to execute the project with admin/root privileges.

### AdvCmnAPI_CM2 (Common Motion API 2.0)
* Device
    <!-- + <a href="#Acm2_DevOpen"><code>Acm2_DevOpen</code></a> -->
    + <a href="#Acm2_DevInitialize"><code>Acm2_DevInitialize</code></a>
    + <a href="#Acm2_GetAvailableDevs"><code>Acm2_GetAvailableDevs</code></a>
    <!-- + <a href="#Acm2_DevExportMappingTable"><code>Acm2_DevExportMappingTable</code></a> -->
    <!-- + <a href="#Acm2_DevImportMappingTable"><code>Acm2_DevImportMappingTable</code></a> -->
    + <a href="#Acm2_DevSaveAllMapFile"><code>Acm2_DevSaveAllMapFile</code></a>
    + <a href="#Acm2_DevLoadAllMapFile"><code>Acm2_DevLoadAllMapFile</code></a>
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
    <!-- + <a href="#Acm2_GpLoadAndMovePath"><code>Acm2_GpLoadAndMovePath</code></a> -->
* DIO
    + <a href="#Acm2_ChSetDOBit"><code>Acm2_ChSetDOBit</code></a>
    + <a href="#Acm2_ChGetDOBit"><code>Acm2_ChGetDOBit</code></a>
    + <a href="#Acm2_ChGetDIBit"><code>Acm2_ChGetDIBit</code></a>
    + <a href="#Acm2_ChSetDOBitByRingNo"><code>Acm2_ChSetDOBitByRingNo</code></a>
    + <a href="#Acm2_ChGetDOBitByRingNo"><code>Acm2_ChGetDOBitByRingNo</code></a>
    + <a href="#Acm2_ChGetDIBitByRingNo"><code>Acm2_ChGetDIBitByRingNo</code></a>
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

#### Acm2_GetAvailableDevs
Get all device list.

```cpp
U32 Acm2_GetAvailableDevs(DEVLIST *DeviceList, U32 MaxEntries, PU32 OutEntries)
```
<!-- <a name="Acm2_DevOpen"></a>

#### Acm2_DevOpen
Open device with device number.

```cpp
U32 Acm2_DevOpen(U32 DeviceNumber, DEVICEINFO *DeviceHandle)
``` -->
<!-- <a name="Acm2_DevExportMappingTable"></a>

#### Acm2_DevExportMappingTable
Export mapping table of device.

```cpp
U32 Acm2_DevExportMappingTable(PI8 FilePath)
```
<a name="Acm2_DevImportMappingTable"></a>

#### Acm2_DevImportMappingTable
Import mapping table of device.

```cpp
U32 Acm2_DevImportMappingTable(PI8 FilePath)
``` -->
<a name="Acm2_DevSaveAllMapFile"></a>

#### Acm2_DevSaveAllMapFile
Upload input/output mapping table from device.

```cpp
U32 Acm2_DevSaveAllMapFile(PI8 FilePath)
```
<a name="Acm2_DevLoadAllMapFile"></a>

#### Acm2_DevLoadAllMapFile
Download input/output mapping table to device.

```cpp
U32 Acm2_DevLoadAllMapFile(PI8 FilePath)
```
<a name="Acm2_GetMappedPhysicalID"></a>

#### Acm2_GetMappedPhysicalID
Get mapped physical id of device.

```cpp
U32 Acm2_GetMappedPhysicalID(ADV_OBJ_TYPE ObjType, U32 ObjLogicalID, PU32 DeviceNumber, PU32 ObjPhysicalID)
```
<a name="Acm2_GetMappedLogicalIDList"></a>

#### Acm2_GetMappedLogicalIDList
Get mapped list of logical id.

```cpp
U32 Acm2_GetMappedLogicalIDList(ADV_OBJ_TYPE ObjType, U32 DeviceLogicalID, PU32 LogicallIDList, PU32 ObjCnt)
```
<a name="Acm2_GetMappedObjInfo"></a>

#### Acm2_GetMappedObjInfo
Get mapped object information.

```cpp
U32 Acm2_GetMappedObjInfo(ADV_OBJ_TYPE ObjType, U32 ObjLogicalID, VOID *pObjInfo)
```
<a name="Acm2_DevAllClose"></a>

#### Acm2_DevAllClose
Close all device at same time.

```cpp
U32 Acm2_DevAllClose()
```
```python
# Example code
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

```cpp
U32 Acm2_DevInitialize()
```
<a name="Acm2_AxGetPosition"></a>

#### Acm2_AxGetPosition
Get axis position by axis number, and position type.

```cpp
U32 Acm2_AxGetPosition(U32 AxID, POSITION_TYPE PosType, PF64 Position)
```
```python
# Example code
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

```cpp
U32 Acm2_AxPTP(U32 AxID, ABS_MODE ptpMode, F64 Distance)
```
<a name="Acm2_AxGetState"></a>

#### Acm2_AxGetState
Get axis state.

```cpp
U32 Acm2_AxGetState(U32 AxID, AXIS_STATUS_TYPE StatusType, PU32 State)
```
```python
# Example code
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

```cpp
U32 Acm2_SetProperty(U32 ObjID, U32 PropertyID, F64 Value)
```
<a name="Acm2_GetProperty"></a>

#### Acm2_GetProperty
Get device/axis property.

```cpp
U32 Acm2_GetProperty(U32 ObjID, U32 PropertyID, PF64 Value)
```
```python
# Example code
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

```cpp
U32 Acm2_SetMultiProperty(U32 ObjID, PU32 PropertyID, PF64 Value, U32 Data_Cnt, PU32 ErrorBuffer)
```
<a name="Acm2_GetMultiProperty"></a>

#### Acm2_GetMultiProperty
Get multiple properties at once.

```cpp
U32 Acm2_GetMultiProperty(U32 ObjID, PU32 PropertyID, PF64 Value, U32 Data_Cnt, PU32 ErrorBuffer)
```
```python
# Example code
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
for i range(data_cnt.value):
    print('set[{0}]:{1}, get:{2}'.format(i, value_arr[i].value, get_val[i]))
```
<a name="Acm2_GetRawProperty"></a>

#### Acm2_GetRawProperty
Get raw property value.

```cpp
U32 Acm2_GetRawProperty(U32 ObjID, U32 PropertyID, PVOID Value, PU32 BufferLength)
```
<a name="Acm2_EnableCallBackFuncForOneEvent"></a>

#### Acm2_EnableCallBackFuncForOneEvent
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

ax_id = c_uint32(0)
abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
distance = c_double(1000)
ax_motion_cnt.value = 0
# Set callback function, enable event
errCde = AdvMot.Acm2_EnableCallBackFuncForOneEvent(ax_id, c_int(ADV_EVENT_SUBSCRIBE.AXIS_MOTION_DONE.value), EvtAxMotionDone)
# Move
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
# Remove callback function, disable event
errCde = AdvMot.Acm2_EnableCallBackFuncForOneEvent(ax_id, c_int(ADV_EVENT_SUBSCRIBE.EVENT_DISABLE.value), EmptyFunction)
```

<a name="Acm2_DevLoadAllConfig"></a>

#### Acm2_DevLoadAllConfig
Load all configuration at once.

```cpp
U32 Acm2_DevLoadAllConfig(PI8 ConfigPath)
```
<a name="Acm2_DevLoadConfig"></a>

#### Acm2_DevLoadConfig
Load configuration.

```cpp
U32 Acm2_DevLoadConfig(U32 DevID, PI8 ConfigPath)
```
<a name="Acm2_DevReadMailBox"></a>

#### Acm2_DevReadMailBox
Read mailbox of device.

```cpp
U32 Acm2_DevReadMailBox(ADV_OBJ_TYPE ObjType, U32 ObjID, U32 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```
<a name="Acm2_DevWriteMailBox"></a>

#### Acm2_DevWriteMailBox
Write mailbox of device.

```cpp
U32 Acm2_DevWriteMailBox(ADV_OBJ_TYPE ObjType, U32 ObjID, U32 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```
<a name="Acm2_GetErrors"></a>

#### Acm2_GetErrors
Get error of device.

```cpp
U32 Acm2_GetErrors(U32 DevID, PVOID Error, PU32 ErrorCount)
```
<a name="Acm2_ResetErrorRecord"></a>

#### Acm2_ResetErrorRecord
Reset error.

```cpp
U32 Acm2_ResetErrorRecord(U32 DevID)
```
<a name="Acm2_DevPreviewMotion"></a>

#### Acm2_DevPreviewMotion
Preview motion.

```cpp
U32 Acm2_DevPreviewMotion(U32 DevID, PI8 InputFile, PI8 OutputFile, U16 NumberOfAxes)
```
<a name="Acm2_ChSetDOBit"></a>

#### Acm2_ChSetDOBit
Set DO bit by channel.

```cpp
U32 Acm2_ChSetDOBit(U32 DoChannel, U32 BitData)
```
```python
# Example code
# Using the example code after LoadENI & Connect
import time
import os
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

# Set DO channel, local DO on PCIE-1203 is 0~1, rest of device will set from channel 8~
do_channel8 = c_uint32(8)
do_channel14 = c_uint32(14)
bit_data = c_uint32(DO_ONOFF.DO_ON.value)
# Set DO(8) on
errCde = AdvMot.Acm2_ChSetDOBit(do_channel8, bit_data)
# Set DO(14) on
errCde = AdvMot.Acm2_ChSetDOBit(do_channel14, bit_data)
time.sleep(0.5)
get_data8 = c_uint32(0)
get_data14 = c_uint32(0)
# Get DO(8) value
errCde = AdvMot.Acm2_ChGetDOBit(do_channel8, byref(get_data8))
# Get DO(14) value
errCde = AdvMot.Acm2_ChGetDOBit(do_channel8, byref(get_data14))
```
<a name="Acm2_ChGetDOBit"></a>

#### Acm2_ChGetDOBit
Get DO bit by channel.

```cpp
U32 Acm2_ChGetDOBit(U32 DoChannel, PU32 BitData)
```
```python
# Example code
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

```cpp
U32 Acm2_GetLastError(ADV_OBJ_TYPE ObjType, U32 ObjLogicalID)
```
<a name="Acm2_AxReturnPausePosition"></a>

#### Acm2_AxReturnPausePosition
Get axis pause position.

```cpp
U32 Acm2_AxReturnPausePosition(U32 AxID)
```
<a name="Acm2_AxSetSvOn"></a>

#### Acm2_AxSetSvOn
Set axis servo on/off.

```cpp
U32 Acm2_AxSetSvOn(U32 AxID, DO_ONOFF OnOff)
```
<a name="Acm2_DevSetAllSvOn"></a>

#### Acm2_DevSetAllSvOn
Set all axes servo on.off.

```cpp
U32 Acm2_DevSetAllSvOn(DO_ONOFF OnOff)
```
<a name="Acm2_AxSetErcOn"></a>

#### Acm2_AxSetErcOn
Set axis erc on/off.

```cpp
U32 Acm2_AxSetErcOn(U32 AxID, DO_ONOFF OnOff)
```
<a name="Acm2_AxResetAlm"></a>

#### Acm2_AxResetAlm
Reset axis alarm logic.

```cpp
U32 Acm2_AxResetAlm(U32 AxID, DO_ONOFF OnOff)
```
<a name="Acm2_AxMoveContinue"></a>

#### Acm2_AxMoveContinue
Set aixs continue move.

```cpp
U32 Acm2_AxMoveContinue(U32 AxID, MOTION_DIRECTION Direction)
```
<a name="Acm2_AxMotionStop"></a>

#### Acm2_AxMotionStop
Force axis stop motion.

```cpp
U32 Acm2_AxMotionStop(PU32 AxisArray, U32 ArrayElements, MOTION_STOP_MODE StopMode, F64 NewDec)
```
```python
# Example code
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
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
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis position
starting_pos = c_double(0)
pos = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
errCde = AdvMot.Acm2_AxGetPosition(ax_id, pos_type, byref(pos))
```
<a name="Acm2_AxHome"></a>

#### Acm2_AxHome
Set axis moving home with direction and home mode.

```cpp
U32 Acm2_AxHomeEx(U32 AxID, U32 DirMode)
```
<a name="Acm2_AxMoveGantryHome"></a>

#### Acm2_AxMoveGantryHome
Set axis moving home with gantry.

```cpp
U32 Acm2_AxMoveGantryHome(U32 AxID, HOME_MODE HomeMode, MOTION_DIRECTION Direction)
```
<a name="Acm2_AxSetHomeSpeedProfile"></a>

#### Acm2_AxSetHomeSpeedProfile
Set axis home speed config.

```cpp
U32 Acm2_AxSetHomeSpeedProfile(U32 AxID, SPEED_PROFILE_PRM ProfileVel)
```
<a name="Acm2_AxChangePos"></a>

#### Acm2_AxChangePos
Set axis position.

```cpp
U32 Acm2_AxChangePos(U32 AxID, F64 NewPosition)
```
<a name="Acm2_AxChangeVel"></a>

#### Acm2_AxChangeVel
Set axis velocity.

```cpp
U32 Acm2_AxChangeVel(U32 AxID, F64 NewVelocity, F64 NewAcc, F64 NewDec)
```
<a name="Acm2_AxChangeVelByRate"></a>

#### Acm2_AxChangeVelByRate
Set axis velocity by rate.

```cpp
U32 Acm2_AxChangeVelByRate(U32 AxID, U32 Rate, F64 NewAcc, F64 NewDec)
```
<a name="Acm2_AxMoveImpose"></a>

#### Acm2_AxMoveImpose
Set axis impose.

```cpp
U32 Acm2_AxMoveImpose(U32 AxID, F64 Position, F64 NewVelocity)
```
<a name="Acm2_AxResetError"></a>

#### Acm2_AxResetError
Reset error of axis.

```cpp
U32 Acm2_AxResetError(U32 AxID)
```
<a name="Acm2_DevResetAllError"></a>

#### Acm2_DevResetAllError
Reset all device error.

```cpp
U32 Acm2_DevResetAllError()
```
```python
# Example code
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

```cpp
U32 Acm2_AxGetMotionIO(U32 AxID, MOTION_IO *Status)
```
<a name="Acm2_AxSetPosition"></a>

#### Acm2_AxSetPosition
Set axis position.

```cpp
U32 Acm2_AxSetPosition(U32 AxID, POSITION_TYPE PosType, F64 Position)
```
<a name="Acm2_AxSetSpeedProfile"></a>

#### Acm2_AxSetSpeedProfile
Set axis speed information.

```cpp
U32 Acm2_AxSetSpeedProfile(U32 AxID, SPEED_PROFILE_PRM ProfileVel)
```
```python
# Example code
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

ax_id = c_uint32(0)
speed_info = SPEED_PROFILE_PRM()
speed_info.FH = c_double(3000)
speed_info.FL = c_double(1500)
speed_info.Acc = c_double(11000)
speed_info.Dec = c_double(9900)
speed_info.JerkFac = c_double(0)
# Set speed information
errCde = AdvMot.Acm2_AxSetSpeedProfile(ax_id, speed_info)
```
<a name="Acm2_AxGetVel"></a>

#### Acm2_AxGetVel
Get axis current velocity.

```cpp
U32 Acm2_AxGetVel(U32 AxID, VELOCITY_TYPE VelType, PF64 Velocity)
```
```python
# Example code
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotDrv import VELOCITY_TYPE

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

ax_id = c_uint32(0)
get_vel = c_double(0)
vel_Type = c_uint(VELOCITY_TYPE.VELOCITY_CMD.value)
# Get axis 0 current velocity
errCde = AdvMot.Acm2_AxGetVel(ax_id, vel_Type, byref(get_vel))
```
<a name="Acm2_AxEnableExternalMode"></a>

#### Acm2_AxEnableExternalMode
Enable axis external mode.

```cpp
U32 Acm2_AxEnableExternalMode(U32 AxID, EXT_DRIVE_MODE ExtDrvMode)
```
<a name="Acm2_AxSoftJog"></a>

#### Acm2_AxSoftJog
Set axis jog.

```cpp
U32 Acm2_AxSoftJog(U32 AxID, MOTION_DIRECTION Direction)
```
<a name="Acm2_AxSetJogSpeedProfile"></a>

#### Acm2_AxSetJogSpeedProfile
Set axis jog speed information.

```cpp
U32 Acm2_AxSetJogSpeedProfile(U32 AxID, JOG_SPEED_PROFILE_PRM ProfileVel)
```
```python
# Example code
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

ax_id = c_uint32(0)
jog_speed_info = JOG_SPEED_PROFILE_PRM()
jog_speed_info.FH = c_double(8000)
jog_speed_info.FL = c_double(1000)
jog_speed_info.Acc = c_double(10000)
jog_speed_info.Dec = c_double(5000)
jog_speed_info.VLTime = c_double(2000)
# Set axis 0 jog speed information
errCde = AdvMot.Acm2_AxSetJogSpeedProfile(ax_id, jog_speed_info)
```
<a name="Acm2_AxMotionStart"></a>

#### Acm2_AxMotionStart
Start motion.

```cpp
U32 Acm2_AxMotionStart(PU32 AxisArray, U32 ArrayElements)
```
<a name="Acm2_AxPause"></a>

#### Acm2_AxPause
Pause motion.

```cpp
U32 Acm2_AxPause(U32 AxID)
```
<a name="Acm2_AxResume"></a>

#### Acm2_AxResume
Resume motion.

```cpp
U32 Acm2_AxResume(U32 AxID)
```
<a name="Acm2_AxResetPVTTable"></a>

#### Acm2_AxResetPVTTable
Reset axis PVT table.

```cpp
U32 Acm2_AxResetPVTTable(U32 AxID)
```
<a name="Acm2_AxLoadPVTTable"></a>

#### Acm2_AxLoadPVTTable
Load axis PVT table.

```cpp
U32 Acm2_AxLoadPVTTable(U32 AxID, PF64 Position, PF64 Velocity, PF64 Time, U32 ArrayElements)
```
<a name="Acm2_AxLoadPVTTableContinuous"></a>

#### Acm2_AxLoadPVTTableContinuous
Continuous loading PVT table.

```cpp
U32 Acm2_AxLoadPVTTableContinuous(U32 AxID, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, F64 TimeDelay, U32 ArrayElements)
```
<a name="Acm2_AxMovePVT"></a>

#### Acm2_AxMovePVT
Move PVT motion.

```cpp
U32 Acm2_AxMovePVT(U32 AxID)
```
```python
# Example code
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

ax_id = c_uint32(0)
# Reset PVT table
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
# Set table of PVT
errCde = AdvMot.Acm2_AxLoadPVTTable(ax_id, posArr, velArr, timeArr, len(pos_arr))
# Set PVT
errCde = AdvMot.Acm2_AxMovePVT(ax_id)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
get_pos = c_double(0)
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
# Get axis 0 state
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Check axis 0 is ready
if (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(ax_id, pos_type, byref(get_pos))
```
<a name="Acm2_AxCheckPTBuffer"></a>

#### Acm2_AxCheckPTBuffer
Check axis PT buffer.

```cpp
U32 Acm2_AxCheckPTBuffer(U32 AxID, PU32 Freespace)
```
<a name="Acm2_AxAddPTData"></a>

#### Acm2_AxAddPTData
Add axis PT data.

```cpp
U32 Acm2_AxAddPTData(U32 AxID, F64 Position, F64 Time)
```
<a name="Acm2_AxMovePT"></a>

#### Acm2_AxMovePT
Move PT motion.

```cpp
U32 Acm2_AxMovePT(U32 AxID)
```
<a name="Acm2_AxResetPTData"></a>

#### Acm2_AxResetPTData
Reset axis PT data.

```cpp
U32 Acm2_AxResetPTData(U32 AxID)
```
```python
# Example code
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

ax_id = c_uint32(0)
# Reset PT table
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
# Set PT table
for i range(len(pos_arr)):
    errCde = AdvMot.Acm2_AxAddPTData(ax_id, pos_arr[i], time_arr[i])
# Start move PT table
errCde = AdvMot.Acm2_AxMovePT(ax_id)

pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
get_pos = c_double(0)
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(ax_id, pos_type, byref(get_pos))
```
<a name="Acm2_AxGearIn"></a>

#### Acm2_AxGearIn
Set axis gear.

```cpp
U32 Acm2_AxGearIn(U32 PrimaryAxisID, U32 FollowingAxisID, GEAR_IN_PRM GearInParameter)
```
<a name="Acm2_AxGantryIn"></a>

#### Acm2_AxGantryIn
Set axis gantry.

```cpp
U32	Acm2_AxGantryIn(U32	PrimaryAxisID, U32 FollowingAxisID, GANTRY_IN_PRM GantryInParameter)
```
```python
# Example code
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

primary_ax = c_uint32(0)
follow_ax = c_uint32(1)
# Reset following axis
errCde = AdvMot.Acm2_AxSyncOut(follow_ax)
# Set gantry parameter
gantry_param = GANTRY_IN_PRM()
# Set gantry reference source as command position
gantry_param.RefSrc = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Set gantry direction as positive
gantry_param.Direction = c_uint(MOTION_DIRECTION.DIRECTION_POS.value)
# Set gantry
errCde = AdvMot.Acm2_AxGantryIn(primary_ax, follow_ax, gantry_param)
# Move primary axis
abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
distance = c_double(10000)
errCde = AdvMot.Acm2_AxPTP(primary_ax, abs_mode, distance)
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 (primary) position
errCde = AdvMot.Acm2_AxGetPosition(primary_ax, pos_type, byref(get_pos_0))
# Get axis 1 (following) position
errCde = AdvMot.Acm2_AxGetPosition(follow_ax, pos_type, byref(get_pos_1))
# Reset following axis
errCde = AdvMot.Acm2_AxSyncOut(follow_ax)
```
<a name="Acm2_AxPhaseAx"></a>

#### Acm2_AxPhaseAx
Set axis phase.

```cpp
U32 Acm2_AxPhaseAx(U32 AxID, PHASE_AXIS_PRM PhaseAxParameter)
```
<a name="Acm2_AxSyncOut"></a>

#### Acm2_AxSyncOut
Lift the gantry.

```cpp
U32 Acm2_AxSyncOut(U32 FollowingAxisID)
```
```python
# Example code
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

primary_ax = c_uint32(0)
follow_ax = c_uint32(1)
# Reset following axis
errCde = AdvMot.Acm2_AxSyncOut(follow_ax)
gear_param = GEAR_IN_PRM()
# Position type as command position
gear_param.RefSrc = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Mode as relative mode
gear_param.Mode = c_uint32(0)
# Set gear ratio
gear_param.GearPosition = c_double(0)
gear_param.GearRatioRate.Num = c_double(1)
gear_param.GearRatioRate.Den = c_double(1)
# Set gear
errCde = AdvMot.Acm2_AxGearIn(primary_ax, follow_ax, gear_param)
# Move primary axis
abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
distance = c_double(10000)
errCde = AdvMot.Acm2_AxPTP(primary_ax, abs_mode, distance)
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 (primary) position
errCde = AdvMot.Acm2_AxGetPosition(primary_ax, pos_type, byref(get_pos_0))
# Get axis 1 (following) position
errCde = AdvMot.Acm2_AxGetPosition(follow_ax, pos_type, byref(get_pos_1))
# Reset following axis
errCde = AdvMot.Acm2_AxSyncOut(follow_ax)
```
<a name="Acm2_GpGetPausePosition"></a>

#### Acm2_GpGetPausePosition
Get group pause position.

```cpp
U32 Acm2_GpGetPausePosition(U32 GpID, PF64 PosArray)
```
<a name="Acm2_GpCreate"></a>

#### Acm2_GpCreate
Create group.

```cpp
U32 Acm2_GpCreate(U32 GpID, PU32 AxisArray, U32 ArrayElements)
```
<a name="Acm2_GpGetAxesInGroup"></a>

#### Acm2_GpGetAxesInGroup
Check axes group.

```cpp
U32 Acm2_GpGetAxesInGroup(U32 GpID, PU32 AxisArray, PU32 ArrayElements)
```
<a name="Acm2_GpResetError"></a>

#### Acm2_GpResetError
Reset error of group.

```cpp
U32 Acm2_GpResetError(U32 GpID)
```
<a name="Acm2_GpLine"></a>

#### Acm2_GpLine
Move group line.

```cpp
U32 Acm2_GpLine(U32 GpID, GP_LINE_MODE LineMode, PF64 EndArray, PU32 ArrayElements)
```
```python
# Example code
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
# Set group move as relative
gp_move_mode = c_uint(GP_LINE_MODE.LINE_REL.value)
# Set group end position: axis(0) = 10000, axis(1) = 10000
end_pos_arr = [c_double(10000), c_double(10000)]
arr_element = c_uint32(len(end_pos_arr))
end_arr = (c_double * len(end_pos_arr))(*end_pos_arr)
# Group 0 move line
errCde = AdvMot.Acm2_GpLine(gp_id, gp_move_mode, end_arr, byref(arr_element))
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 (primary) position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 (following) position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_GpArc_Center"></a>

#### Acm2_GpArc_Center
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
# Set 2D Arc mode
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
# Set 2D Arc CW center, end position
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
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_GpArc_3P"></a>

#### Acm2_GpArc_3P
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
# # Set 2D Arc mode as relative, which the starting point of circular is (0, 0)
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
# Set 2D Arc CW center, end position
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
# Set arc movement as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
errCde = AdvMot.Acm2_GpArc_3P(gp_id, arc_mode, refArr, endArr, byref(arr_element), dir_mode)
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_GpArc_Angle"></a>

#### Acm2_GpArc_Angle
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
# Set 2D Arc mode as relative, which the starting point of circular is (0, 0)
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
# Set center as (20000, 20000)
center_arr = [c_double(20000), c_double(20000)]
centerArr = (c_double * len(center_arr))(*center_arr)
arr_element = c_uint32(len(center_arr))
# Set degree as 45
degree = c_double(45)
# Set arc movement as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
errCde = AdvMot.Acm2_GpArc_Angle(gp_id, arc_mode, centerArr, byref(arr_element), degree, dir_mode)
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_Gp3DArc_Center"></a>

#### Acm2_Gp3DArc_Center
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
# Set 3D Arc mode
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
# Set 3D Arc CW, with 120 degree
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
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_Gp3DArc_NormVec"></a>

#### Acm2_Gp3DArc_NormVec
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
# Set 3D Arc mode
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
# Set direction as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
# Set 3D Arc CW, with 120 degree
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
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_Gp3DArc_3P"></a>

#### Acm2_Gp3DArc_3P
Set arc movement with 3 points of circular.

```cpp
U32 Acm2_Gp3DArc_3P(U32 GpID, ABS_MODE ArcMode, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION  Direction, U32 cycCount)
```
```python
# Example code
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
# # Set 3D Arc mode as relative, which the starting point of circular is (0, 0, 0)
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
# Set 3D Arc CW, with 120 degree
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
# Set direction as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
cyc_cnt = c_uint32(0)
# Set arc movement with 3 points of circular
errCde = AdvMot.Acm2_Gp3DArc_3P(gp_id, arc_mode, refArr, endArr, byref(arr_element), dir_mode, cyc_cnt)
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_Gp3DArc_3PAngle"></a>

#### Acm2_Gp3DArc_3PAngle
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
# # Set 3D Arc mode as relative, which the starting point of circular is (0, 0, 0)
arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
# Set direction as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
# Set 3D Arc CW, with 120 degree
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
# Set arc movement with 3 point of circular
errCde = AdvMot.Acm2_Gp3DArc_3PAngle(gp_id, arc_mode, refArr, endArr, byref(arr_element), degree, dir_mode)
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
# Check value
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_GpHelix_Center"></a>

#### Acm2_GpHelix_Center
Set group helix center.

```cpp
U32 Acm2_GpHelix_Center(U32 GpID, ABS_MODE HelixMode, PF64 CenterArray, PF64 EndArray, PU32	pArrayElements, ARC_DIRECTION Direction)
```
```python
# Example code
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
# Set mode as relative
helix_mode = c_uint(ABS_MODE.MOVE_REL.value)
# Set center as (10000, 0, 0)
center_arr = [c_double(10000), c_double(0), c_double(0)]
centerArr = (c_double * len(center_arr))(*center_arr)
# Set end position as (20000, 0, 20000)
end_arr = [c_double(20000), c_double(0), c_double(20000)]
endArr = (c_double * len(end_arr))(*end_arr)
arr_element = c_uint32(len(end_arr))
# Set direction as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
# Set Helix movement
errCde = AdvMot.Acm2_GpHelix_Center(gp_id, helix_mode, centerArr, endArr, byref(arr_element), dir_mode)
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
# Check value
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_GpHelix_3P"></a>

#### Acm2_GpHelix_3P
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
# Set mode as relative
helix_mode = c_uint(ABS_MODE.MOVE_REL.value)
# Set center as (8000, 0, 0)
center_arr = [c_double(8000), c_double(0), c_double(0)]
centerArr = (c_double * len(center_arr))(*center_arr)
# Set end position as (16000, 16000, 10000)
end_arr = [c_double(16000), c_double(16000), c_double(10000)]
endArr = (c_double * len(end_arr))(*end_arr)
arr_element = c_uint32(len(center_arr))
# Set direction as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
# Set Helix movement
errCde = AdvMot.Acm2_GpHelix_3P(gp_id, helix_mode, centerArr, endArr, byref(arr_element), dir_mode)
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
# Check value
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_GpHelix_Angle"></a>

#### Acm2_GpHelix_Angle
Set group helix angle.

```cpp
U32 Acm2_GpHelix_Angle(U32 GpID, ABS_MODE HelixMode, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, ARC_DIRECTION Direction)
```
```python
# Example code
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
# Set mode as relative
helix_mode = c_uint(ABS_MODE.MOVE_REL.value)
# Set center as (200, 0)
center_arr = [c_double(200), c_double(0), c_double(0)]
centerArr = (c_double * len(center_arr))(*center_arr)
# Set 120 as degree
end_arr = [c_double(4000), c_double(4000), c_double(120)]
endArr = (c_double * len(end_arr))(*end_arr)
arr_element = c_uint32(len(center_arr))
# Set direction as CW
dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
# Set Helix movement
errCde = AdvMot.Acm2_GpHelix_Angle(gp_id, helix_mode, centerArr, endArr, byref(arr_element), dir_mode)
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
# Check value
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_GpResume"></a>

#### Acm2_GpResume

```cpp
U32 Acm2_GpResume(U32 GpID)
```
<a name="Acm2_GpPause"></a>

#### Acm2_GpPause
Set group pause motion.

```cpp
U32 Acm2_GpPause(U32 GpID)
```
```python
# Example code
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
for idx range(len_get.value):
# Set mode as relative
move_mode = c_uint(GP_LINE_MODE.LINE_REL.value)
end_arr = [c_double(20000), c_double(20000), c_double(20000)]
endArr = (c_double * len(end_arr))(*end_arr)
arr_element = c_uint32(len(end_arr))
errCde = AdvMot.Acm2_GpLine(gp_id, move_mode, endArr, arr_element)
# Pause movement
errCde = AdvMot.Acm2_GpPause(gp_id)
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
# Check value: Not equal to target position
# Resume movement
errCde = AdvMot.Acm2_GpResume(gp_id)
# Check status
while state.value != AXIS_STATE.STA_AX_READY.value:
    time.sleep(1)
    test_GetAxState()
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
# Check value: Equal to target position
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_GpMotionStop"></a>

#### Acm2_GpMotionStop
Stop group motion.

```cpp
U32 Acm2_GpMotionStop(U32 GpID, MOTION_STOP_MODE StopMode, F64 NewDec)
```
<a name="Acm2_GpChangeVel"></a>

#### Acm2_GpChangeVel
Change velocity of group.

```cpp
U32 Acm2_GpChangeVel(U32 GpID, F64 NewVelocity, F64 NewAcc, F64 NewDec)
```
<a name="Acm2_GpChangeVelByRate"></a>

#### Acm2_GpChangeVelByRate
Change group velocity by rate.

```cpp
U32 Acm2_GpChangeVelByRate(U32 GpID, U32 Rate, F64 NewAcc, F64 NewDec)
```
<a name="Acm2_GpGetVel"></a>

#### Acm2_GpGetVel
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1, 2 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
for idx range(len_get.value):
# Set mode as relative
move_mode = c_uint(GP_LINE_MODE.LINE_REL.value)
end_arr = [c_double(200000), c_double(200000), c_double(200000)]
endArr = (c_double * len(end_arr))(*end_arr)
arr_element = c_uint32(len(end_arr))
errCde = AdvMot.Acm2_GpLine(gp_id, move_mode, endArr, arr_element)
# Check group status
time.sleep(2)
gp_state = c_uint32(0)
errCde = AdvMot.Acm2_GpGetState(gp_id, byref(gp_state))
print('gp_state:0x{0:x}'.format(gp_state.value))
# Change velocity
new_vel = c_double(5000)
new_acc = c_double(9000)
new_dec = c_double(4000)
errCde = AdvMot.Acm2_GpChangeVel(gp_id, new_vel, new_acc, new_dec)
vel_type = c_uint(VELOCITY_TYPE.VELOCITY_CMD.value)
get_gp_vel = c_double(0)
time.sleep(2)
errCde = AdvMot.Acm2_GpGetVel(gp_id, vel_type, byref(get_gp_vel))
print('gp vel:{0}'.format(get_gp_vel.value))
# Set stop mode as deceleration to stop
stop_mode = c_uint(MOTION_STOP_MODE.MOTION_STOP_MODE_DEC.value)
errCde = AdvMot.Acm2_GpMotionStop(gp_id, stop_mode, new_dec)
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
get_pos_2 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Get axis 2 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
# Check value: Not equal to target position
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_GpSetSpeedProfile"></a>

#### Acm2_GpSetSpeedProfile
Get group speed information.

```cpp
U32 Acm2_GpSetSpeedProfile(U32 GpID, SPEED_PROFILE_PRM ProfileVel)
```
<a name="Acm2_GpGetState"></a>

#### Acm2_GpGetState
Get group status.

```cpp
U32 Acm2_GpGetState(U32 GpID, PU32 State)
```
<a name="Acm2_GpLoadPath"></a>

#### Acm2_GpLoadPath
Load path table group.

```cpp
U32 Acm2_GpLoadPath(U32 GpID, PI8 FilePath, PU32 TotalCount)
```
<a name="Acm2_GpAddPath"></a>

#### Acm2_GpAddPath
Add path into group.

```cpp
U32 Acm2_GpAddPath(U32 GpID, U32 MoveCmd, PATH_MOVE_MODE_CM2 MoveMode, F64 FH, F64 FL, F64 Acc, F64 Dec, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)
```
<a name="Acm2_GpMovePath"></a>

#### Acm2_GpMovePath
Start move group after add path.

```cpp
U32 Acm2_GpMovePath(U32 GpID)
```
<a name="Acm2_GpResetPath"></a>

#### Acm2_GpResetPath
Reset group path table.

```cpp
U32 Acm2_GpResetPath(U32 GpID)
```
```python
# Example code
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
for idx range(len_get.value):
# Reset group path
errCde = AdvMot.Acm2_GpResetPath(gp_id)
# Set 2D Arc CW center, end position
'''
| axis | Arc center | Arc end |
|------|------------|---------|
|   0  |    8000    |  16000  |
|   1  |      0     |    0    |
'''
# Set path table
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
# Start move path
errCde = AdvMot.Acm2_GpMovePath(gp_id)
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Check value: Equal to target position
# Reset group path
errCde = AdvMot.Acm2_GpResetPath(gp_id)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_GpGetPathStatus"></a>

#### Acm2_GpGetPathStatus
Get group path status.

```cpp
U32 Acm2_GpGetPathStatus(U32 GpID, PATH_STATUS *pathStatus)
```
```python
# Example code
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

gp_ax_arr = [c_uint32(0), c_uint32(1)]
gp_id = c_uint32(0)
gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
# Creat group 0, and set axis 0, 1 into group
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
# get_axes size must be same as len_get
len_get = c_uint32(64)
get_axes = (c_uint32 * len_get.value)()
# Get axes group 0 and check
errCde = AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
for idx range(len_get.value):
# Reset group path
errCde = AdvMot.Acm2_GpResetPath(gp_id)
# Create path file by path editor inside the Utility
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
# Start move path
errCde = AdvMot.Acm2_GpMovePath(gp_id)
path_status = c_uint(0)
errCde = AdvMot.Acm2_GpGetPathStatus(gp_id, byref(path_status))
# Check status
state = c_uint32(0)
state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
while (state.value != AXIS_STATE.STA_AX_READY.value):
    time.sleep(1)
    AdvMot.Acm2_AxGetState(ax_id, state_type, byref(state))
# Get axis 0 position
get_pos_0 = c_double(0)
get_pos_1 = c_double(0)
pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
# Get axis 0 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
# Get axis 1 position
errCde = AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
# Check value: Equal to target position
# Reset group path
errCde = AdvMot.Acm2_GpResetPath(gp_id)
# Reset all axes from group 0
errCde = AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
```
<a name="Acm2_GpMoveSelPath"></a>

#### Acm2_GpMoveSelPath

```cpp
U32 Acm2_GpMoveSelPath(U32 GpID, U32 StartIndex, U32 EndIndex, U32 Repeat)
```
<a name="Acm2_GpGetPathIndexStatus"></a>

#### Acm2_GpGetPathIndexStatus
Get group information by the index of path table.

```cpp
U32 Acm2_GpGetPathIndexStatus(U32 GpID, U32 Index, PU32 CmdFunc, PU32 MoveMode, PF64 FH, PF64 FL, PF64 Acc, PF64 Dec, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)
```
<a name="Acm2_GpDelay"></a>

#### Acm2_GpDelay
Delay group.

```cpp
U32 Acm2_GpDelay(U32 GpID, U32 DelayTime)
```
<a name="Acm2_GpPathDO"></a>

#### Acm2_GpPathDO
Set device do on/off between path.

```cpp
U32 Acm2_GpPathDO(U32 GpID, PATH_DO_PRM  PathDOPrm)
```
<a name="Acm2_GpPathWaitDI"></a>

#### Acm2_GpPathWaitDI
Wait DI status between path.

```cpp
U32 Acm2_GpPathWaitDI(U32 GpID, PATH_DI_WAIT_PRM DIWaitPrm)
```
<a name="Acm2_GpPathWaitForAxis"></a>

#### Acm2_GpPathWaitForAxis
Wait axis between path.

```cpp
U32 Acm2_GpPathWaitForAxis(U32 GpID, PATH_AX_WAIT_PRM AxWaitPrm)
```
<a name="Acm2_GpLookAheadPath"></a>

#### Acm2_GpLookAheadPath

```cpp
U32 Acm2_GpLookAheadPath(U32 GpID, U16 BufferSize, PI8 OutputFile)
```
<a name="Acm2_GpLookAheadPathFile"></a>

#### Acm2_GpLookAheadPathFile

```cpp
U32 Acm2_GpLookAheadPathFile(U32 GpID, U16 BufferSize, PI8 InputPathFile, PI8 OutputFile, PU32 PathCount)
```
<!-- <a name="Acm2_GpLoadAndMovePath"></a>

#### Acm2_GpLoadAndMovePath -->

<a name="Acm2_ChGetDIBit"></a>

#### Acm2_ChGetDIBit
Get DI bit by channel.

```cpp
U32 Acm2_ChGetDIBit(U32 DiChannel, PU32 BitData)
```
<a name="Acm2_ChSetDOBitByRingNo"></a>

#### Acm2_ChSetDOBitByRingNo
Set DO bit by channel, and ring number.

```cpp
U32 Acm2_ChSetDOBitByRingNo(U32 RingNo, U32 SlaveID, U32 DoChannel, U32 BitData)
```
<a name="Acm2_ChGetDOBitByRingNo"></a>

#### Acm2_ChGetDOBitByRingNo
Get DO bit by ring number, and channel.

```cpp
U32 Acm2_ChGetDOBitByRingNo(U32 RingNo, U32 SlaveID, U32 DoChannel, PU32 BitData)
```
<a name="Acm2_ChGetDIBitByRingNo"></a>

#### Acm2_ChGetDIBitByRingNo
Get DI bit by ring number, and channel.

```cpp
U32 Acm2_ChGetDIBitByRingNo(U32 RingNo, U32 SlaveID, U32 DiChannel, PU32 BitData)
```
<a name="Acm2_ChSetDOByte"></a>

#### Acm2_ChSetDOByte
Set DO channel byte.

```cpp
U32 Acm2_ChSetDOByte(U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```
<a name="Acm2_ChGetDOByte"></a>

#### Acm2_ChGetDOByte
Get DO channel byte.

```cpp
U32 Acm2_ChGetDOByte(U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```
```python
# Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

# Using this example code after connect AMAX-5057SO
# Check how to start a EtherCAT subdevice by Acm2_DevConnect

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

# Local DO of PCIE1203 is port 0
port_num = c_uint32(1)
start_ch = c_uint32(0)
get_byte_value = [c_uint32(0)] * 8
time.sleep(0.5)
# Get DO byte of 5057SO (0~7)
errCde = AdvMot.Acm2_ChGetDOByte(start_ch, port_num, byref(get_byte_value[0]))
set_byte_value_on = [c_uint32(DO_ONOFF.DO_ON.value)] * 8
set_byte_value_off = [c_uint32(DO_ONOFF.DO_OFF.value)] * 8
set_value_arr_on = (c_uint32 * len(set_byte_value_on))(*set_byte_value_on)
set_value_arr_off = (c_uint32 * len(set_byte_value_off))(*set_byte_value_off)
time.sleep(0.5)
# Set DO byte of 5057SO (0~7)
errCde = AdvMot.Acm2_ChSetDOByte(start_ch, port_num, set_value_arr_on)
time.sleep(1)
# Get DO byte of 5057SO (0~7)
errCde = AdvMot.Acm2_ChGetDOByte(start_ch, port_num, byref(get_byte_value[0]))
time.sleep(0.5)
# Set DO byte of 5057SO (0~7)
errCde = AdvMot.Acm2_ChSetDOByte(start_ch, port_num, set_value_arr_off)
```
<a name="Acm2_ChGetDIByte"></a>

#### Acm2_ChGetDIByte
Get DI channel byte.

```cpp
U32 Acm2_ChGetDIByte(U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```
<a name="Acm2_ChSetDOByteByRingNo"></a>

#### Acm2_ChSetDOByteByRingNo
Set DO byte by ring number.

```cpp
U32 Acm2_ChSetDOByteByRingNo(U32 RingNo, U32 SlaveID, U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```
<a name="Acm2_ChGetDOByteByRingNo"></a>

#### Acm2_ChGetDOByteByRingNo
Get DO byte by ring number.

```cpp
U32 Acm2_ChGetDOByteByRingNo(U32 RingNo, U32 SlaveID, U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```
<a name="Acm2_ChGetDIByteByRingNo"></a>

#### Acm2_ChGetDIByteByRingNo
Get DI byte by ring number.

```cpp
U32 Acm2_ChGetDIByteByRingNo(U32 RingNo, U32 SlaveID, U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```
<a name="Acm2_ChSetAOData"></a>

#### Acm2_ChSetAOData
Set AO data.

```cpp
U32 Acm2_ChSetAOData(U32 AoChannel, DAQ_DATA_TYPE Type, F64 AoData)
```
```python
# Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

# Using this example code after connect AMAX-4820, AMAX-4817
# Check how to start a EtherCAT subdevice by Acm2_DevConnect

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

# Ring as IO Ring
ring_no = c_uint32(1)
# set by position
id_type = c_uint(ECAT_ID_TYPE.SUBDEVICE_POS.value)
# Sort AMAX-4820 second posiotn
sub_dev_pos = c_uint32(2)
# Set AO(0) output range as -10V ~ 10V
pdo_type = c_uint32(ECAT_TYPE.ECAT_TYPE_U16.value)
pdo_data_size = c_uint32(sizeof(c_uint16))
pdo_index = c_uint32(0x2180)
val_range = c_uint16(3)
pdo_range_sub_index = c_uint32(0x02)
errCde = AdvMot.Acm2_DevWriteSDO(ring_no, id_type, sub_dev_pos, pdo_index, pdo_range_sub_index, pdo_type, pdo_data_size, byref(val_range))
# Set AO(0) output enable
pdo_enable_sub_index = c_uint32(0x01)
val_enable = c_uint16(1)
errCde = AdvMot.Acm2_DevWriteSDO(ring_no, id_type, sub_dev_pos, pdo_index, pdo_enable_sub_index, pdo_type, pdo_data_size, byref(val_enable))
# AMAX-4820 default AO(0) ~ AO(3)
ao_ch = c_uint32(0)
# Set AO(0) as 10V
data_type = c_uint(DAQ_DATA_TYPE.SCALED_DATA.value)
ao_data = c_double(10)
errCde = AdvMot.Acm2_ChSetAOData(ao_ch, data_type, ao_data)
# Get AO(0) data
get_data_ao = c_double(0)
errCde = AdvMot.Acm2_ChGetAOData(ao_ch, data_type, byref(get_data_ao))
assertAlmostEqual(ao_data.value, get_data_ao.value, delta=1.0)
# Get AI(0) data
get_data_ai = c_double(0)
errCde = AdvMot.Acm2_ChGetAIData(ao_ch, data_type, byref(get_data_ai))
```
<a name="Acm2_ChGetAOData"></a>

#### Acm2_ChGetAOData
Get AO data.

```cpp
U32 Acm2_ChGetAOData(U32 AoChannel, DAQ_DATA_TYPE Type, PF64 AoData)
```
<a name="Acm2_ChSetAODataByRingNo"></a>

#### Acm2_ChSetAODataByRingNo
Set AO data by ring number.

```cpp
U32 Acm2_ChSetAODataByRingNo(U32 RingNo, U32 SlaveID, U32 AoChannel, DAQ_DATA_TYPE Type, F64 AoData)
```
<a name="Acm2_ChGetAODataByRingNo"></a>

#### Acm2_ChGetAODataByRingNo
Get AO data by ring number.

```cpp
U32 Acm2_ChGetAODataByRingNo(U32 RingNo, U32 SlaveID, U32 AoChannel, DAQ_DATA_TYPE Type, PF64 AoData)
```
<a name="Acm2_ChGetAIData"></a>

#### Acm2_ChGetAIData
Get AI data.

```cpp
U32 Acm2_ChGetAIData(U32 AiChannel, DAQ_DATA_TYPE Type, PF64 AiData)
```
<a name="Acm2_ChGetAIDataByRingNo"></a>

#### Acm2_ChGetAIDataByRingNo
Get AI data by ring number.

```cpp
U32 Acm2_ChGetAIDataByRingNo(U32 RingNo, U32 SlaveID, U32 AiChannel, DAQ_DATA_TYPE Type, PF64 AiData)
```
<a name="Acm2_ChGetCntData"></a>

#### Acm2_ChGetCntData
Get counter data.

```cpp
U32 Acm2_ChGetCntData(U32 CntChannel, PF64 CounterData)
```
<a name="Acm2_ChSetCntData"></a>

#### Acm2_ChSetCntData
Set counter data.

```cpp
U32 Acm2_ChSetCntData(U32 CntChannel, F64 CounterData)
```
<a name="Acm2_ChLinkCmpFIFO"></a>

#### Acm2_ChLinkCmpFIFO
Set compare position.

```cpp
U32 Acm2_ChLinkCmpFIFO(U32 ChID, PU32 AxisArray, U32 ArrayElement)
```
<a name="Acm2_ChLinkCmpObject"></a>

#### Acm2_ChLinkCmpObject
Link compare do with axis/counter.

```cpp
U32 Acm2_ChLinkCmpObject(U32 ChID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)
```
```python
# Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

# Using this example code after connect AMAX-4820, AMAX-4817
# Check how to start a EtherCAT subdevice by Acm2_DevConnect

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

cnt_ch = c_uint32(1)
# Local CMP Diff channel is 2
cmp_ch = c_uint32(2)
# Set encoder(0) pulse mode as CW/CCW.
ppt_arr = c_uint32(PropertyID2.CFG_CH_DaqCntPulseInMode.value)
val_arr = c_double(PULSE_IN_MODE.I_CW_CCW.value)
get_val = c_double(0)
get_cnt_data = c_double(0)
errCde = AdvMot.Acm2_SetProperty(cnt_ch, ppt_arr, val_arr)
errCde = AdvMot.Acm2_GetProperty(cnt_ch, ppt_arr, byref(get_val))
errCde = AdvMot.Acm2_ChGetCntData(cnt_ch, byref(get_cnt_data))
# Link local encoder/counter to compare
cnt_arr = [cnt_ch]
trans_cnt_arr = (c_uint32 * len(cnt_arr))(*cnt_arr)
axis_type = c_uint(ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL.value)
# Reset Link connection
errCde = AdvMot.Acm2_ChLinkCmpObject(cmp_ch, axis_type, trans_cnt_arr, 0)
errCde = AdvMot.Acm2_ChLinkCmpObject(cmp_ch, axis_type, trans_cnt_arr, len(cnt_arr))
# Set compare property, disable compare before setting.
cmp_set_arr = [c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoOutputMode.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoLogic.value)]
val_arr = [c_double(COMPARE_ENABLE.CMP_DISABLE.value),
            c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value),
            c_double(COMPARE_LOGIC.CP_ACT_LOW.value)]
for i range(len(cmp_set_arr)):
    errCde = AdvMot.Acm2_SetProperty(cmp_ch, cmp_set_arr[i].value, val_arr[i])
# Get value
get_val = c_double(0)
for i range(len(val_arr)):
    errCde = AdvMot.Acm2_GetProperty(cmp_ch, cmp_set_arr[i], byref(get_val))
end_pos = c_double(2500)
# Enable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_ENABLE.value).value)
# Set compare data table
# Compare DO behavior: ---ON---        ---OFF---        ---ON---       ---OFF---
set_cmp_data_arr = [c_double(500), c_double(1000), c_double(1500), c_double(2000)]
trans_cmp_data_arr = (c_double * len(set_cmp_data_arr))(*set_cmp_data_arr)
errCde = AdvMot.Acm2_ChSetCmpBufferData(cmp_ch, trans_cmp_data_arr, len(set_cmp_data_arr))
# Reset encoder data as 0
reset_cnt_data = c_double(0)
errCde = AdvMot.Acm2_ChSetCntData(cnt_ch, reset_cnt_data)
# Get encoder data
get_cnt_data = c_double(0)
while get_cnt_data.value <= end_pos.value:
    time.sleep(0.1)
    errCde = AdvMot.Acm2_ChGetCntData(cnt_ch, byref(get_cnt_data))
# Disable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
```
<a name="Acm2_ChGetLinkedCmpObject"></a>

#### Acm2_ChGetLinkedCmpObject
Get compare do linked object.

```cpp
U32 Acm2_ChGetLinkedCmpObject(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```
<a name="Acm2_ChEnableCmp"></a>

#### Acm2_ChEnableCmp
Enable compare channel.

```cpp
U32 Acm2_ChEnableCmp(U32 ChID, U32 Enable)
```
<a name="Acm2_ChSetCmpOut"></a>

#### Acm2_ChSetCmpOut
Set compare channel on/off.

```cpp
U32 Acm2_ChSetCmpOut(U32 ChID, DO_ONOFF OnOff)
```
<a name="Acm2_ChSetCmpDoOut"></a>

#### Acm2_ChSetCmpDoOut
Set compare on/off.

```cpp
U32 Acm2_ChSetCmpDoOut(U32 ChID, DO_ONOFF OnOff)
```
<a name="Acm2_AxGetCmpData"></a>

#### Acm2_AxGetCmpData
Get compared data by axis.

```cpp
U32 Acm2_AxGetCmpData(U32 AxID, PF64 CmpData)
```
<a name="Acm2_ChGetCmpData"></a>

#### Acm2_ChGetCmpData
Get compared data by channel.

```cpp
U32 Acm2_ChGetCmpData(U32 CmpChannel, PF64 CmpData, U32 ObjectArrayCount)
```
<a name="Acm2_AxSetCmpTable"></a>

#### Acm2_AxSetCmpTable
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

# Pulse mode
cnt_ch = c_uint32(0)
cmp_ch = c_uint32(0)
# Set encoder(0) pulse mode as CW/CCW.
ppt_arr = c_uint32(PropertyID2.CFG_CH_DaqCntPulseInMode.value)
val_arr = c_double(PULSE_IN_MODE.I_CW_CCW.value)
get_val = c_double(0)
errCde = AdvMot.Acm2_SetProperty(cnt_ch, ppt_arr, val_arr)
errCde = AdvMot.Acm2_GetProperty(cnt_ch, ppt_arr, byref(get_val))
# Set compare property, disable compare before setting.
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
# Get value
get_val = c_double(0)
for i range(len(val_arr)):
    errCde = AdvMot.Acm2_GetProperty(cmp_ch, cmp_set_arr[i], byref(get_val))
# Link local encoder/counter to compare
cnt_arr = [cnt_ch]
trans_cnt_arr = (c_uint32 * len(cnt_arr))(*cnt_arr)
axis_type = c_uint(ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL.value)
errCde = AdvMot.Acm2_ChLinkCmpObject(cmp_ch, axis_type, trans_cnt_arr, len(cnt_arr))
end_pos = c_double(2500)
# Set compare data table
# Compare DO behavior: ---ON---        ---OFF---        ---ON---       ---OFF---
set_cmp_data_arr = [c_double(500), c_double(1000), c_double(1500), c_double(2000)]
trans_cmp_data_arr = (c_double * len(set_cmp_data_arr))(*set_cmp_data_arr)
errCde = AdvMot.Acm2_ChSetCmpBufferData(cmp_ch, trans_cmp_data_arr, len(set_cmp_data_arr))
# Reset encoder data as 0
reset_cnt_data = c_double(0)
errCde = AdvMot.Acm2_ChSetCntData(cnt_ch, reset_cnt_data)
# Enable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_ENABLE.value).value)
# Get encoder data
get_cnt_data = c_double(0)
while get_cnt_data.value < end_pos.value:
    time.sleep(0.1)
    errCde = AdvMot.Acm2_ChGetCntData(cnt_ch, byref(get_cnt_data))
# Disable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
```

<a name="Acm2_AxSetCmpAuto"></a>

#### Acm2_AxSetCmpAuto
Set auto compare by axis.

```cpp
U32 Acm2_AxSetCmpAuto(U32 AxID, F64 StartPosition, F64 EndPosition, F64 Interval)
```
<a name="Acm2_ChSetCmpAuto"></a>

#### Acm2_ChSetCmpAuto
Set auto compare by channel.

```cpp
U32 Acm2_ChSetCmpAuto(U32 CmpChannel, F64 StartPosition, F64 EndPosition, F64 Interval)
```
<a name="Acm2_ChSetCmpBufferData"></a>

#### Acm2_ChSetCmpBufferData
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

# Toggle Mode
cnt_ch = c_uint32(0)
cmp_ch = c_uint32(0)
# Set encoder(0) pulse mode as CW/CCW.
ppt_arr = c_uint32(PropertyID2.CFG_CH_DaqCntPulseInMode.value)
val_arr = c_double(PULSE_IN_MODE.I_CW_CCW.value)
get_val = c_double(0)
errCde = AdvMot.Acm2_SetProperty(cnt_ch, ppt_arr, val_arr)
errCde = AdvMot.Acm2_GetProperty(cnt_ch, ppt_arr, byref(get_val))
# Set compare property, disable compare before setting.
cmp_set_arr = [c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoOutputMode.value),
                c_uint32(PropertyID2.CFG_CH_DaqCmpDoLogic.value)]
val_arr = [c_double(COMPARE_ENABLE.CMP_DISABLE.value),
            c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value),
            c_double(COMPARE_LOGIC.CP_ACT_LOW.value)]
for i range(len(cmp_set_arr)):
    errCde = AdvMot.Acm2_SetProperty(cmp_ch, cmp_set_arr[i].value, val_arr[i])
# Get value
get_val = c_double(0)
for i range(len(val_arr)):
    errCde = AdvMot.Acm2_GetProperty(cmp_ch, cmp_set_arr[i], byref(get_val))
# Link local encoder/counter to compare
cnt_arr = [cnt_ch]
trans_cnt_arr = (c_uint32 * len(cnt_arr))(*cnt_arr)
axis_type = c_uint(ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL.value)
errCde = AdvMot.Acm2_ChLinkCmpObject(cmp_ch, axis_type, trans_cnt_arr, len(cnt_arr))
end_pos = c_double(2500)
# Set compare data table
# Compare DO behavior: ---ON---        ---OFF---        ---ON---       ---OFF---
set_cmp_data_arr = [c_double(500), c_double(1000), c_double(1500), c_double(2000)]
trans_cmp_data_arr = (c_double * len(set_cmp_data_arr))(*set_cmp_data_arr)
errCde = AdvMot.Acm2_ChSetCmpBufferData(cmp_ch, trans_cmp_data_arr, len(set_cmp_data_arr))
# Reset encoder data as 0
reset_cnt_data = c_double(0)
errCde = AdvMot.Acm2_ChSetCntData(cnt_ch, reset_cnt_data)
# Enable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_ENABLE.value).value)
# Get encoder data
get_cnt_data = c_double(0)
while get_cnt_data.value < end_pos.value:
    time.sleep(0.1)
    errCde = AdvMot.Acm2_ChGetCntData(cnt_ch, byref(get_cnt_data))
# Disable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
```

<a name="Acm2_ChSetMultiCmpTable"></a>

#### Acm2_ChSetMultiCmpTable
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

cnt_ch = [c_uint32(0), c_uint32(1)]
cmp_ch = c_uint32(0)
ltc_ch = c_uint32(0)
# Set encoder(0) pulse mode as CW/CCW.
ppt_arr = c_uint32(PropertyID2.CFG_CH_DaqCntPulseInMode.value)
val_arr = c_double(PULSE_IN_MODE.I_CW_CCW.value)
get_val = c_double(0)
for i range(len(cnt_ch)):
    errCde = AdvMot.Acm2_SetProperty(cnt_ch[i], ppt_arr, val_arr)
    errCde = AdvMot.Acm2_GetProperty(cnt_ch[i], ppt_arr, byref(get_val))
# Link local encoder/counter to compare
cnt_arr = cnt_ch
trans_cnt_arr = (c_uint32 * len(cnt_arr))(*cnt_arr)
axis_type = c_uint(ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL.value)
errCde = AdvMot.Acm2_ChLinkCmpObject(cmp_ch, axis_type, trans_cnt_arr, len(cnt_arr))
get_obj_type = c_uint(0)
get_linked_arr = (c_uint32 * 2)()
get_linked_cnt = c_uint32(2)
# Get linked local encoder/counter to compare
errCde = AdvMot.Acm2_ChGetLinkedCmpObject(cmp_ch, byref(get_obj_type), get_linked_arr, byref(get_linked_cnt))
print('[CMP] Linked type:{0}, linked count:{1}'.format(get_obj_type.value, get_linked_cnt.value))
for i range(get_linked_cnt.value):
    print('Linked channel:{0}'.format(get_linked_arr[i]))
# Set compare property, disable compare before setting.
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
# Get CMP proerty
get_val = c_double(0)
for i range(len(val_arr)):
    errCde = AdvMot.Acm2_GetProperty(cmp_ch, cmp_set_arr[i], byref(get_val))
# Get linked local encoder/counter to latch
errCde = AdvMot.Acm2_ChGetLinkedLatchObject(ltc_ch, byref(get_obj_type), get_linked_arr, byref(get_linked_cnt))
print('[LTC] Linked type:{0}, linked count:{1}'.format(get_obj_type.value, get_linked_cnt.value))
for i range(get_linked_cnt.value):
    print('Linked channel:{0}'.format(get_linked_arr[i]))
# Reset LTC buffer
errCde = AdvMot.Acm2_ChResetLatchBuffer(ltc_ch)
# Set LTC property
ltc_set_ppt_arr = [c_uint32(PropertyID2.CFG_CH_DaqLtcMinDist.value),
                c_uint32(PropertyID2.CFG_CH_DaqLtcLogic.value),
                c_uint32(PropertyID2.CFG_CH_DaqLtcEnable.value)]
ltc_val_arr = [c_double(10), c_double(COMPARE_LOGIC.CP_ACT_LOW.value), c_double(COMPARE_ENABLE.CMP_ENABLE.value)]
for i range(len(ltc_set_ppt_arr)):
    errCde = AdvMot.Acm2_SetProperty(ltc_ch, ltc_set_ppt_arr[i].value, ltc_val_arr[i])
# Get LTC property
get_val_ltc = c_double(0)
for i range(len(ltc_val_arr)):
    errCde = AdvMot.Acm2_GetProperty(ltc_ch, ltc_set_ppt_arr[i], byref(get_val_ltc))

# Set compare data
set_cmp_data_arr = [c_double(500), c_double(1000), c_double(1500), c_double(2000), c_double(2500), c_double(3000),
                    c_double(550), c_double(1050), c_double(1550), c_double(2050), c_double(2550), c_double(3050)]
trans_cmp_data_arr = (c_double * len(set_cmp_data_arr))(*set_cmp_data_arr)
errCde = AdvMot.Acm2_ChSetMultiCmpBufferData(cmp_ch, trans_cmp_data_arr, len(cnt_ch), c_uint32(int(len(set_cmp_data_arr) / len(cnt_ch))))
# Reset encoder data as 0
reset_cnt_data = c_double(0)
for i range(len(cnt_ch)):
    errCde = AdvMot.Acm2_ChSetCntData(cnt_ch[i], reset_cnt_data)
# Enable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_ENABLE.value).value)
# Get encoder data
get_cnt_data = c_double(0)
end_pos = c_double(3500)
while get_cnt_data.value <= end_pos.value:
    time.sleep(0.1)
    for i range(len(cnt_ch)):
        tmp_ch = c_uint32(i)
        errCde = AdvMot.Acm2_ChGetCntData(tmp_ch, byref(get_cnt_data))
# Get LTC data
get_ltc_buf_status = BUFFER_STATUS()
act_data_cnt = c_uint32(128)
get_ltc_data_arr = (c_double * act_data_cnt.value)()
errCde = AdvMot.Acm2_ChGetLatchBufferStatus(ltc_ch, byref(get_ltc_buf_status))
print('RemainCount:{0}, FreeSpaceCount:{1}'.format(get_ltc_buf_status.RemainCount, get_ltc_buf_status.FreeSpaceCount))
errCde = AdvMot.Acm2_ChReadLatchBuffer(ltc_ch, get_ltc_data_arr, act_data_cnt, byref(act_data_cnt))
print('act_data_cnt:{0}'.format(act_data_cnt.value))
for i range(act_data_cnt.value):
    print('get_ltc_data_arr[{0}]:{1}'.format(i, get_ltc_data_arr[i]))
# Disable compare and latch
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqLtcEnable.value).value,
                                        c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
errCde = AdvMot.Acm2_SetProperty(ltc_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value,
                                        c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
```
<a name="Acm2_ChSetMultiCmpBufferData"></a>

#### Acm2_ChSetMultiCmpBufferData
Set multi compare buffer.

```cpp
U32 Acm2_ChSetMultiCmpBufferData(U32 ChID, PF64 MultiCmpTable, U32 ObjectArrayCount, U32 DataArrayCount)
```
<a name="Acm2_ChResetCmpData"></a>

#### Acm2_ChResetCmpData
Reset compare data.

```cpp
U32 Acm2_ChResetCmpData(U32 CmpChannel)
```
<a name="Acm2_ChGetCmpBufferStatus"></a>

#### Acm2_ChGetCmpBufferStatus
Get compared buffer status.

```cpp
U32	Acm2_ChGetCmpBufferStatus(U32 CmpChannel, PBUFFER_STATUS bufferstatus)
```
<a name="Acm2_ChLinkLatchAxis"></a>

#### Acm2_ChLinkLatchAxis
Link latch to axis.
```cpp
U32 Acm2_ChLinkLatchAxis(U32 ChID, PU32 AxisArray, U32 AxisCount)
```
<a name="Acm2_ChLinkLatchObject"></a>

#### Acm2_ChLinkLatchObject
Lift latch to object.
```cpp
U32 Acm2_ChLinkLatchObject(U32 ChID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)
```
<a name="Acm2_ChGetLinkedLatchObject"></a>

#### Acm2_ChGetLinkedLatchObject
Get linked latch object.
```cpp
U32 Acm2_ChGetLinkedLatchObject(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```
<a name="Acm2_ChTriggerLatch"></a>

#### Acm2_ChTriggerLatch
Trigger latch by channel.

```cpp
U32 Acm2_ChTriggerLatch(U32 ChID)
```
<a name="Acm2_AxReadLatchBuffer"></a>

#### Acm2_AxReadLatchBuffer
Read latch buffer.

```cpp
U32	Acm2_AxReadLatchBuffer(U32 AxID, PF64 LatchDataArray, PU32 DataCnt)
```
<a name="Acm2_ChReadLatchBuffer"></a>

#### Acm2_ChReadLatchBuffer
Read latch buffer by channel.

```cpp
U32	Acm2_ChReadLatchBuffer(U32 LtcChannel, PF64 LatchDataArray, U32 ObjectArrayCount, PU32 DataArrayCount)
```
<a name="Acm2_AxGetLatchBufferStatus"></a>

#### Acm2_AxGetLatchBufferStatus
Get latch buffer status.

```cpp
U32	Acm2_AxGetLatchBufferStatus(U32 AxID, PU32 RemainCnt, PU32 SpaceCnt)
```
<a name="Acm2_ChGetLatchBufferStatus"></a>

#### Acm2_ChGetLatchBufferStatus
Get latch buffer status by channel.

```cpp
U32	Acm2_ChGetLatchBufferStatus(U32 LtcChannel, BUFFER_STATUS *bufferstatus)
```
```python
# Example code
import time
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

# Using this example code after connect AMAX-4820, AMAX-4817
# Check how to start a EtherCAT subdevice by Acm2_DevConnect

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

cnt_ch = c_uint32(0)
cmp_ch = c_uint32(0)
ltc_ch = c_uint32(0)
# Set encoder(0) pulse mode as CW/CCW.
ppt_arr = c_uint32(PropertyID2.CFG_CH_DaqCntPulseInMode.value)
val_arr = c_double(PULSE_IN_MODE.I_CW_CCW.value)
get_val = c_double(0)
errCde = AdvMot.Acm2_SetProperty(cnt_ch, ppt_arr, val_arr)
errCde = AdvMot.Acm2_GetProperty(cnt_ch, ppt_arr, byref(get_val))
# Link local encoder/counter to compare
cnt_arr = [cnt_ch]
trans_cnt_arr = (c_uint32 * len(cnt_arr))(*cnt_arr)
axis_type = c_uint(ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL.value)
errCde = AdvMot.Acm2_ChLinkCmpObject(cmp_ch, axis_type, trans_cnt_arr, len(cnt_arr))
# Set compare property, disable compare before setting.
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
# Get CMP proerty
get_val = c_double(0)
for i range(len(val_arr)):
    errCde = AdvMot.Acm2_GetProperty(cmp_ch, cmp_set_arr[i], byref(get_val))

# Get linked local encoder/counter to latch
get_obj_type = c_uint(0)
get_linked_arr = (c_uint32 * 2)()
get_linked_cnt = c_uint32(2)
errCde = AdvMot.Acm2_ChGetLinkedLatchObject(ltc_ch, byref(get_obj_type), get_linked_arr, byref(get_linked_cnt))
print('Linked type:{0}, linked count:{1}'.format(get_obj_type.value, get_linked_cnt.value))
for i range(get_linked_cnt.value):
    print('Linked channel:{0}'.format(get_linked_arr[i]))
# Reset LTC buffer
errCde = AdvMot.Acm2_ChResetLatchBuffer(ltc_ch)
# Set LTC property
ltc_set_ppt_arr = [c_uint32(PropertyID2.CFG_CH_DaqLtcMinDist.value),
                    c_uint32(PropertyID2.CFG_CH_DaqLtcLogic.value),
                    c_uint32(PropertyID2.CFG_CH_DaqLtcEnable.value)]
ltc_val_arr = [c_double(10), c_double(COMPARE_LOGIC.CP_ACT_LOW.value), c_double(COMPARE_ENABLE.CMP_ENABLE.value)]
for i range(len(ltc_set_ppt_arr)):
    errCde = AdvMot.Acm2_SetProperty(ltc_ch, ltc_set_ppt_arr[i].value, ltc_val_arr[i])
# Get LTC property
get_val_ltc = c_double(0)
for i range(len(ltc_val_arr)):
    errCde = AdvMot.Acm2_GetProperty(ltc_ch, ltc_set_ppt_arr[i], byref(get_val_ltc))

# Set compare data
set_cmp_data_arr = [c_double(500), c_double(1000), c_double(1500), c_double(2000)]
trans_cmp_data_arr = (c_double * len(set_cmp_data_arr))(*set_cmp_data_arr)
errCde = AdvMot.Acm2_ChSetCmpBufferData(cmp_ch, trans_cmp_data_arr, len(set_cmp_data_arr))
# Reset encoder data as 0
reset_cnt_data = c_double(0)
errCde = AdvMot.Acm2_ChSetCntData(cnt_ch, reset_cnt_data)
# Enable compare
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value, c_double(COMPARE_ENABLE.CMP_ENABLE.value).value)
# Get encoder data
get_cnt_data = c_double(0)
end_pos = c_double(2500)
while get_cnt_data.value <= end_pos.value:
    time.sleep(0.1)
    for i range(2):
        tmp_ch = c_uint32(i)
        errCde = AdvMot.Acm2_ChGetCntData(tmp_ch, byref(get_cnt_data))
        print('[{0}]get_cnt_data:{1}'.format(i, get_cnt_data.value))
    errCde = AdvMot.Acm2_ChGetCntData(cnt_ch, byref(get_cnt_data))
# Get LTC data
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
# Disable compare and latch
errCde = AdvMot.Acm2_SetProperty(cmp_ch, c_uint32(PropertyID2.CFG_CH_DaqLtcEnable.value).value,
                                            c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
errCde = AdvMot.Acm2_SetProperty(ltc_ch, c_uint32(PropertyID2.CFG_CH_DaqCmpDoEnable.value).value,
                                            c_double(COMPARE_ENABLE.CMP_DISABLE.value).value)
```
<a name="Acm2_AxResetLatchBuffer"></a>

#### Acm2_AxResetLatchBuffer
Reset latch buffer.

```cpp
U32	Acm2_AxResetLatchBuffer(U32 AxID)
```
<a name="Acm2_ChResetLatchBuffer"></a>

#### Acm2_ChResetLatchBuffer
Reset latch buffer by channel.

```cpp
U32	Acm2_ChResetLatchBuffer(U32 LtcChannel)
```
<a name="Acm2_ChLinkPWMTable"></a>

#### Acm2_ChLinkPWMTable
Link PWM with object.

```cpp
U32 Acm2_ChLinkPWMTable(U32 ChID, ADV_OBJ_TYPE ObjType, U32 ObjectID)
```
<a name="Acm2_ChGetLinkedPWMTable"></a>

#### Acm2_ChGetLinkedPWMTable
Get linked PWM Acm2_ChSetPWMTabletable by channel.

```cpp
U32 Acm2_ChGetLinkedPWMTable(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```
<a name="Acm2_ChSetPWMTable"></a>

#### Acm2_ChSetPWMTable
Set PWM table by channel.

```cpp
U32 Acm2_ChSetPWMTable(U32 ChID, PF64 VelocityArray, PF64 PWMArray, U32 ArrayElements)
```
<a name="Acm2_ChLoadPWMTableFile"></a>

#### Acm2_ChLoadPWMTableFile
Loal PWM table file.

```cpp
U32 Acm2_ChLoadPWMTableFile(U32 ChID, PI8 FilePath, PU32 PointsCount)
```
<a name="Acm2_ChGetPWMTableStatus"></a>

#### Acm2_ChGetPWMTableStatus
Get PWM table status.

```cpp
U32	Acm2_ChGetPWMTableStatus(U32 ChID, PWM_TABLE_STATUS *PWMStatus)
```
<a name="Acm2_ChGetExtDriveData"></a>

#### Acm2_ChGetExtDriveData
Get external drive data by channel.

```cpp
U32 Acm2_ChGetExtDriveData(U32 ExtChannel, PF64 CounterData)
```
<a name="Acm2_ChSetExtDriveData"></a>

#### Acm2_ChSetExtDriveData
Set external drive data by channel.

```cpp
U32 Acm2_ChSetExtDriveData(U32 ExtChannel, F64 CounterData)
```
<a name="Acm2_ChLinkExtDriveObject"></a>

#### Acm2_ChLinkExtDriveObject
Link external drive object.

```cpp
U32 Acm2_ChLinkExtDriveObject(U32 ChID, ADV_OBJ_TYPE ObjType, U32 ObjectID)
```
<a name="Acm2_ChGetLinkedExtDriveObject"></a>

#### Acm2_ChGetLinkedExtDriveObject
Get linked external drive object.

```cpp
U32 Acm2_ChGetLinkedExtDriveObject(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```
<a name="Acm2_DevMDaqConfig"></a>

#### Acm2_DevMDaqConfig
Set MDAQ config.

```cpp
U32 Acm2_DevMDaqConfig(U32 ChannelID, U32 Period, U32 AxisNo, U32 Method, U32 ChanType, U32 Count)
```
<a name="Acm2_DevMDaqGetConfig"></a>

#### Acm2_DevMDaqGetConfig
Get MDAQ config.

```cpp
U32 Acm2_DevMDaqGetConfig(U32 ChannelID, PU32 Period, PU32 AxisNo, PU32 Method, PU32 ChanType, PU32 Count)
```
<a name="Acm2_DevMDaqStart"></a>

#### Acm2_DevMDaqStart
Start MDAQ.

```cpp
U32 Acm2_DevMDaqStart(U32 DevID)
```
<a name="Acm2_DevMDaqStop"></a>

#### Acm2_DevMDaqStop
Stop MDAQ.

```cpp
U32 Acm2_DevMDaqStop(U32 DevID)
```
<a name="Acm2_DevMDaqReset"></a>

#### Acm2_DevMDaqReset
Reset MDAQ.

```cpp
U32 Acm2_DevMDaqReset(U32 ChannelID)
```
<a name="Acm2_DevMDaqGetStatus"></a>

#### Acm2_DevMDaqGetStatus
Get MDAQ status.

```cpp
U32 Acm2_DevMDaqGetStatus(U32 ChannelID, PU32 CurrentCnt, PU32 Status)
```
<a name="Acm2_DevMDaqGetData"></a>

#### Acm2_DevMDaqGetData
Get MDAQ data.

```cpp
U32 Acm2_DevMDaqGetData(U32 ChannelID, U32 StartIndex, U32 MaxCount, PF64 DataBuffer)
```
<a name="Acm2_GetDSPFrmWareDwnLoadRate"></a>

#### Acm2_GetDSPFrmWareDwnLoadRate
Get FW download rate.

```cpp
U32 Acm2_GetDSPFrmWareDwnLoadRate(U32 DevID, PF64 Percentage)
```
<a name="Acm2_DevLoadENI"></a>

#### Acm2_DevLoadENI
Download ENI file.

```cpp
U32 Acm2_DevLoadENI(U32 RingNo, PI8 ENIFile)
```
<a name="Acm2_DevConnect"></a>

#### Acm2_DevConnect
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

# eni file can be create by the Utility
eni_path = b'test\\63000000_eni1.xml'
# Motion ring number:0, IO Ring number:1, IORing is SM mode only
ring_no = c_uint32(1)
errCde = AdvMot.Acm2_DevLoadENI(ring_no, eni_path)
# After load eni file, StartFieldbus/Connect to subdevices.
errCde = AdvMot.Acm2_DevConnect(ring_no)
# Set EtherCAT type as position
ecat_type = c_uint(ECAT_ID_TYPE.SUBDEVICE_POS.value)
# SubDevice position 0 is AMAX-5074
sub_dev0 = c_uint32(0)
# SubDevice position 1 is AMAX-5057SO
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
<a name="Acm2_DevDisConnect"></a>

#### Acm2_DevDisConnect
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

# Motion ring number:0, IO Ring number:1, IORing is SM mode only
ring_no0 = c_uint32(0)
ring_no1 = c_uint32(1)
# Disconnect devices
errCde = AdvMot.Acm2_DevDisConnect(ring_no0)
errCde = AdvMot.Acm2_DevDisConnect(ring_no1)
```
<a name="Acm2_DevGetSubDevicesID"></a>

#### Acm2_DevGetSubDevicesID
Get subdevices id.

```cpp
U32 Acm2_DevGetSubDevicesID(U32 RingNo, ECAT_ID_TYPE IDType, PU32 SubDeviceIDArray, PU32 SubDeviceCnt)
```
<a name="Acm2_DevGetMDeviceInfo"></a>

#### Acm2_DevGetMDeviceInfo
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

ring_no = c_uint32(1)
main_dev_info = ADVAPI_MDEVICE_INFO()
errCde = AdvMot.Acm2_DevGetMDeviceInfo(ring_no, byref(main_dev_info))
print('slave_count:{0}'.format(main_dev_info.slave_count))
```
<a name="Acm2_DevGetSubDeviceInfo"></a>

#### Acm2_DevGetSubDeviceInfo
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

ring_no = c_uint32(1)
# Get subdevice ID
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
# Check value from xml
for subdev tree.findall('.//Slave'):
    phys_addr = int(subdev.find('Info/PhysAddr').text)
    phys_addr_arr[idx] = phys_addr
    idx += 1
for i range(id_cnt.value):
    sub_dev_info = ADVAPI_SUBDEVICE_INFO_CM2()
    errCde = AdvMot.Acm2_DevGetSubDeviceInfo(ring_no, c_uint(ECAT_ID_TYPE.SUBDEVICE_POS.value), i, byref(sub_dev_info))
```
<a name="Acm2_DevGetSubDeviceFwVersion"></a>

#### Acm2_DevGetSubDeviceFwVersion
Get subdevice fw information.

```cpp
U32 Acm2_DevGetSubDeviceFwVersion(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, char *VersionInfo)
```
<a name="Acm2_DevSetSubDeviceID"></a>

#### Acm2_DevSetSubDeviceID
Set subdevice id.

```cpp
U32 Acm2_DevSetSubDeviceID(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 SubDeviceNewID)
```
<a name="Acm2_DevSetSubDeviceStates"></a>

#### Acm2_DevSetSubDeviceStates
Set subdevice status.

```cpp
U32 Acm2_DevSetSubDeviceStates(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 SubDeviceState)
```
<a name="Acm2_DevGetSubDeviceStates"></a>

#### Acm2_DevGetSubDeviceStates
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

# eni file can be create by the Utility
if os.name == 'nt':
    eni_path = b'test\\eni1.xml'
else:
    eni_path = b'test/eni1.xml'
# Motion ring number:0, IO Ring number:1, IORing is SM mode only
ring_no = c_uint32(1)
errCde = AdvMot.Acm2_DevLoadENI(ring_no, eni_path)
# After load eni file, StartFieldbus/Connect to subdevices.
errCde = AdvMot.Acm2_DevConnect(ring_no)
# Set EtherCAT type as position
ecat_type = c_uint(ECAT_ID_TYPE.SUBDEVICE_POS.value)
# SubDevice position 0 is AMAX-5074
sub_dev0 = c_uint32(0)
# SubDevice position 1 is AMAX-5057SO
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
<a name="Acm2_DevWriteSDO"></a>

#### Acm2_DevWriteSDO
Write data by SDO.

```cpp
U32 Acm2_DevWriteSDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, VOID *pValue)
```
<a name="Acm2_DevReadSDO"></a>

#### Acm2_DevReadSDO
Read data by SDO.

```cpp
U32 Acm2_DevReadSDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, VOID *pValue)
```
<a name="Acm2_DevWritePDO"></a>

#### Acm2_DevWritePDO
Write data by PDO.

```cpp
U32 Acm2_DevWritePDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, VOID *pValue)
```
<a name="Acm2_DevReadPDO"></a>

#### Acm2_DevReadPDO
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
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()

# Ring as IO Ring
ring_no = c_uint32(1)
# set by position
id_type = c_uint(ECAT_ID_TYPE.SUBDEVICE_POS.value)
sub_dev_pos = c_uint32(1)
# AMAX-5057SO 0x3101:01 is DO(0)
pdo_idx = c_uint32(0x3101)
pdo_sub_idx = c_uint32(0x01)
# DO(0) data type is boolean
pdo_type = c_uint32(ECAT_TYPE.ECAT_TYPE_BOOL.value)
pdo_data_size = c_uint32(sizeof(c_bool))
val_on = c_bool(1)
val_off = c_bool(0)
get_value = c_bool(0)
# Set DO(0) on by PDO
errCde = AdvMot.Acm2_DevWritePDO(ring_no, id_type, sub_dev_pos, pdo_idx, pdo_sub_idx, pdo_type, pdo_data_size, byref(val_on))
# Get DO(0) value by PDO
errCde = AdvMot.Acm2_DevReadPDO(ring_no, id_type, sub_dev_pos, pdo_idx, pdo_sub_idx, pdo_type, pdo_data_size, byref(get_value))
# Set DO(0) off by PDO
errCde = AdvMot.Acm2_DevWritePDO(ring_no, id_type, sub_dev_pos, pdo_idx, pdo_sub_idx, pdo_type, pdo_data_size, byref(val_off))
# Get DO(0) value by PDO
errCde = AdvMot.Acm2_DevReadPDO(ring_no, id_type, sub_dev_pos, pdo_idx, pdo_sub_idx, pdo_type, pdo_data_size, byref(get_value))
```
<a name="Acm2_DevWriteReg"></a>

#### Acm2_DevWriteReg
Write data by reg.

```cpp
U32 Acm2_DevWriteReg(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Address, U32 Type, U32 DataSize, VOID *pValue)
```
<a name="Acm2_DevReadReg"></a>

#### Acm2_DevReadReg
Read data by reg.

```cpp
U32 Acm2_DevReadReg(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Address, U32 Type, U32 DataSize, VOID *pValue)
```
<a name="Acm2_DevReadSubDeviceCommErrCnt"></a>

#### Acm2_DevReadSubDeviceCommErrCnt
Read subdevice communication error counter.

```cpp
U32 Acm2_DevReadSubDeviceCommErrCnt(U32 RingNo, PU32 ErrCntArray, PU32 ArrayElements)
```
<a name="Acm2_Ax1DCompensateTable"></a>

#### Acm2_Ax1DCompensateTable
Set compensate table with one axis.

```cpp
U32 Acm2_Ax1DCompensateTable(U32 AxID, F64 OriginPos, F64 Pitch, PF64 OffsetData, U32 OffsetElements, U32 Direction)
```
<a name="Acm2_Ax2DCompensateTable"></a>

#### Acm2_Ax2DCompensateTable
Set compensate table 2D.

```cpp
U32 Acm2_Ax2DCompensateTable(U32 AxID, U32 RelAxID, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataX, PF64 OffsetDataY, U32 OffsetElementsX, U32 OffsetElementsY)
```
<a name="Acm2_AxZAxisCompensateTable"></a>

#### Acm2_AxZAxisCompensateTable
Set compensate table Z axis.

```cpp
U32 Acm2_AxZAxisCompensateTable(U32 AxID, U32 RelAxID, U32 ZAxID, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataZ, U32 OffsetElementsX, U32 OffsetElementsY)
```
<a name="Acm2_AxGetCompensatePosition"></a>

#### Acm2_AxGetCompensatePosition
Get compensate position by axis.

```cpp
U32 Acm2_AxGetCompensatePosition(U32 AxID, PF64 Position)
```
<a name="Acm2_DevOscChannelDataStart"></a>

#### Acm2_DevOscChannelDataStart
Start Osc. channel data.

```cpp
U32 Acm2_DevOscChannelDataStart(U32 DevID)
```
<a name="Acm2_DevOscChannelDataStop"></a>

#### Acm2_DevOscChannelDataStop
Stop Osc. channel data.

```cpp
U32 Acm2_DevOscChannelDataStop(U32 DevID)
```
<a name="Acm2_DevGetOscChannelDataConfig"></a>

#### Acm2_DevGetOscChannelDataConfig
Get config of Osc. channel.

```cpp
U32 Acm2_DevGetOscChannelDataConfig(U32 DevID, U16 ChannelID, POSC_PROFILE_PRM oscflg)
```
<a name="Acm2_DevSetOscChannelDataConfig"></a>

#### Acm2_DevSetOscChannelDataConfig
Set config of Osc. channel.

```cpp
U32 Acm2_DevSetOscChannelDataConfig(U32 DevID, U16 ChannelID, OSC_PROFILE_PRM oscflg)
```
<a name="Acm2_DevGetOscChannelData"></a>

#### Acm2_DevGetOscChannelData
Get Osc. channel data.

```cpp
U32 Acm2_DevGetOscChannelData(U32 DevID, U16 ChannelID, U32 DataIndex, PU32 MaxCount, PF64 DataBuffer)
```
<a name="Acm2_DevGetOscChannelStatus"></a>

#### Acm2_DevGetOscChannelStatus
Get Osc. channel status.

```cpp
U32  Acm2_DevGetOscChannelStatus(U32 DevID, PU32 Status)
```

### AdvCmnAPI_CM (Common Motion API 1.0)
* Device
    + <a href="#Acm_GetAvailableDevs"><code>Acm_GetAvailableDevs</code></a>
    + <a href="#Acm_GetErrorMessage"><code>Acm_GetErrorMessage</code></a>
    + <a href="#Acm_DevOpen"><code>Acm_DevOpen</code></a>
    + <a href="#Acm_DevReOpen"><code>Acm_DevReOpen</code></a>
    + <a href="#Acm_DevClose"><code>Acm_DevClose</code></a>
    + <a href="#Acm_GetLastError"><code>Acm_GetLastError</code></a>
    + <a href="#Acm_GetProperty"><code>Acm_GetProperty</code></a>
    + <a href="#Acm_SetProperty"><code>Acm_SetProperty</code></a>
    + <a href="#Acm_GetU32Property"><code>Acm_GetU32Property</code></a>
    + <a href="#Acm_GetI32Property"><code>Acm_GetI32Property</code></a>
    + <a href="#Acm_GetF64Property"><code>Acm_GetF64Property</code></a>
    + <a href="#Acm_GetStringProperty"><code>Acm_GetStringProperty</code></a>
    + <a href="#Acm_SetU32Property"><code>Acm_SetU32Property</code></a>
    + <a href="#Acm_SetI32Property"><code>Acm_SetI32Property</code></a>
    + <a href="#Acm_SetF64Property"><code>Acm_SetF64Property</code></a>
    + <a href="#Acm_SetStringProperty"><code>Acm_SetStringProperty</code></a>
    + <a href="#Acm_GetMultiProperty"><code>Acm_GetMultiProperty</code></a>
    + <a href="#Acm_SetMultiU32Property"><code>Acm_SetMultiU32Property</code></a>
    + <a href="#Acm_SetMultiI32Property"><code>Acm_SetMultiI32Property</code></a>
    + <a href="#Acm_SetMultiF64Property"><code>Acm_SetMultiF64Property</code></a>
    + <a href="#Acm_GetChannelProperty"><code>Acm_GetChannelProperty</code></a>
    + <a href="#Acm_SetChannelProperty"><code>Acm_SetChannelProperty</code></a>
    + <a href="#Acm_GetMultiChannelProperty"><code>Acm_GetMultiChannelProperty</code></a>
    + <a href="#Acm_SetMultiChannelProperty"><code>Acm_SetMultiChannelProperty</code></a>
    + <a href="#Acm_DevEnableEvent"><code>Acm_DevEnableEvent</code></a>
    + <a href="#Acm_DevCheckEvent"><code>Acm_DevCheckEvent</code></a>
    + <a href="#Acm_EnableMotionEvent"><code>Acm_EnableMotionEvent</code></a>
    + <a href="#Acm_CheckMotionEvent"><code>Acm_CheckMotionEvent</code></a>
    + <a href="#Acm_CancelCheckEvent"><code>Acm_CancelCheckEvent</code></a>
    + <a href="#Acm_DevEnableEvent_All"><code>Acm_DevEnableEvent_All</code></a>
    + <a href="#Acm_DevCheckEvent_All"><code>Acm_DevCheckEvent_All</code></a>
    + <a href="#Acm_DevLoadConfig"><code><Acm_DevLoadConfig/code></a>
    + <a href="#Acm_DevSlaveFwDownload"><code>Acm_DevSlaveFwDownload</code></a>
    + <a href="#Acm_DevWriteDPMData"><code>Acm_DevWriteDPMData</code></a>
    + <a href="#Acm_DevWriteMultiMailBox"><code>Acm_DevWriteMultiMailBox</code></a>
    + <a href="#Acm_WriteRingBuffer"><code>Acm_WriteRingBuffer</code></a>
    + <a href="#Acm_ReadRingBuffer"><code>Acm_ReadRingBuffer</code></a>
    + <a href="#Acm_DevGetComStatus"><code>Acm_DevGetComStatus</code></a>
    + <a href="#Acm_DevGetErrorTable"><code>Acm_DevGetErrorTable</code></a>
    + <a href="#Acm_DevGetIOInfo"><code>Acm_DevGetIOInfo</code></a>
    + <a href="#Acm_CheckVersion"><code>Acm_CheckVersion</code></a>
    + <a href="#Acm_DevMultiTrigSetPWMTableOnTime"><code>Acm_DevMultiTrigSetPWMTableOnTime</code></a>
    + <a href="#Acm_DevMultiTrigSetCmpDO"><code>Acm_DevMultiTrigSetCmpDO</code></a>
    + <a href="#Acm_DevMultiTrigForceCmpOut"><code>Acm_DevMultiTrigForceCmpOut</code></a>
    + <a href="#Acm_DevMutiTrigSetCmpDO"><code>Acm_DevMutiTrigSetCmpDO</code></a>
    + <a href="#Acm_DevMutiTrigForceCmpOut"><code>Acm_DevMutiTrigForceCmpOut</code></a>
    + <a href="#Acm_MasStartRing"><code>Acm_MasStartRing</code></a>
    + <a href="#Acm_MasStopRing"><code>Acm_MasStopRing</code></a>
    + <a href="#Acm_MasGetComStatus"><code>Acm_MasGetComStatus</code></a>
    + <a href="#Acm_MasGetComCyclicTime"><code>Acm_MasGetComCyclicTime</code></a>
    + <a href="#Acm_MasGetDataCyclicTime"><code>Acm_MasGetDataCyclicTime</code></a>
    + <a href="#Acm_MasGetActiveTable"><code>Acm_MasGetActiveTable</code></a>
    + <a href="#Acm_MasGetErrorTable"><code>Acm_MasGetErrorTable</code></a>
    + <a href="#Acm_MasGetSlaveInfo"><code>Acm_MasGetSlaveInfo</code></a>
    + <a href="#Acm_MasLogComStatus"><code>Acm_MasLogComStatus</code></a>
    + <a href="#Acm_DevDownloadScanData"><code>Acm_DevDownloadScanData</code></a>
        + <a href="#Acm_DevMDaqConfig"><code>Acm_DevMDaqConfig</code></a>
    + <a href="#Acm_DevMDaqStart"><code>Acm_DevMDaqStart</code></a>
    + <a href="#Acm_DevMDaqStop"><code>Acm_DevMDaqStop</code></a>
    + <a href="#Acm_DevMDaqReset"><code>Acm_DevMDaqReset</code></a>
    + <a href="#Acm_DevMDaqGetStatus"><code>Acm_DevMDaqGetStatus</code></a>
    + <a href="#Acm_DevMDaqGetData"><code>Acm_DevMDaqGetData</code></a>
    + <a href="#Acm_DevMDaqGetConfig"><code>Acm_DevMDaqGetConfig</code></a>
    + <a href="#Acm_RegCallBackFunc"><code>Acm_RegCallBackFunc</code></a>
    + <a href="#Acm_EnableEventCallBack"><code>Acm_EnableEventCallBack</code></a>
    + <a href="#Acm_RegCallBackFuncForOneEvent"><code>Acm_RegCallBackFuncForOneEvent</code></a>
    + <a href="#Acm_DevEnableMotionEvent"><code>Acm_DevEnableMotionEvent</code></a>
    + <a href="#Acm_ServoSetCom"><code>Acm_ServoSetCom</code></a>
    + <a href="#Acm_ServoGetAbsPosition"><code>Acm_ServoGetAbsPosition</code></a>
    + <a href="#Acm_AxSetCmdPosi_Pulse"><code>Acm_AxSetCmdPosi_Pulse</code></a>
    + <a href="#Acm_AxSpecialDiSetBit"><code>Acm_AxSpecialDiSetBit</code></a>
    + <a href="#Acm_DevEnableLTC"><code>Acm_DevEnableLTC</code></a>
    + <a href="#Acm_DevLTCSaftyDist"><code>Acm_DevLTCSaftyDist</code></a>
    + <a href="#Acm_DevEnableCmp"><code>Acm_DevEnableCmp</code></a>
    + <a href="#Acm_DevLtcLinkCmp"><code>Acm_DevLtcLinkCmp</code></a>
    + <a href="#Acm_DevSetCmp"><code>Acm_DevSetCmp</code></a>
    + <a href="#Acm_DevSetCmpDO"><code>Acm_DevSetCmpDO</code></a>
    + <a href="#Acm_DevSetCmpData"><code>Acm_DevSetCmpData</code></a>
    + <a href="#Acm_DevSetCmpAuto"><code>Acm_DevSetCmpAuto</code></a>
    + <a href="#Acm_DevGetCmpData"><code>Acm_DevGetCmpData</code></a>
    + <a href="#Acm_DevEnableCmpFIFO"><code>Acm_DevEnableCmpFIFO</code></a>
    + <a href="#Acm_DevGetCmpFIFOCount"><code>Acm_DevGetCmpFIFOCount</code></a>
    + <a href="#Acm_DevGetCmpCounter"><code>Acm_DevGetCmpCounter</code></a>
    + <a href="#Acm_DevResetCmpFIFO"><code>Acm_DevResetCmpFIFO</code></a>
    + <a href="#Acm_DevSetLTCInEdge"><code>Acm_DevSetLTCInEdge</code></a>
    + <a href="#Acm_DevGetLTCData"><code>Acm_DevGetLTCData</code></a>
    + <a href="#Acm_DevGetLTCFlag"><code>Acm_DevGetLTCFlag</code></a>
    + <a href="#Acm_DevResetLTC"><code>Acm_DevResetLTC</code></a>
    + <a href="#Acm_DevGetCmpFlag"><code>Acm_DevGetCmpFlag</code></a>
    + <a href="#Acm_DevResetCmpFlag"><code>Acm_DevResetCmpFlag</code></a>
    + <a href="#Acm_DevGetLtcLinkCmpStatus"><code>Acm_DevGetLtcLinkCmpStatus</code></a>
    + <a href="#Acm_DevResetCmpData"><code>Acm_DevResetCmpData</code></a>
    + <a href="#Acm_DevGetLTCInEdge"><code>Acm_DevGetLTCInEdge</code></a>
    + <a href="#Acm_DevGetLTCInPol"><code>Acm_DevGetLTCInPol</code></a>
    + <a href="#Acm_DevGetLTCSaftyDist"><code>Acm_DevGetLTCSaftyDist</code></a>
    + <a href="#Acm_DevGetLTCInSource"><code>Acm_DevGetLTCInSource</code></a>
    + <a href="#Acm_DevSetLTCInSource"><code>Acm_DevSetLTCInSource</code></a>
    + <a href="#Acm_DevGetCmp"><code>Acm_DevGetCmp</code></a>
    + <a href="#Acm_DevReadLatchBuffer"><code>Acm_DevReadLatchBuffer</code></a>
    + <a href="#Acm_DevGetLatchBufferStatus"><code>Acm_DevGetLatchBufferStatus</code></a>
    + <a href="#Acm_DevResetLatchBuffer"><code>Acm_DevResetLatchBuffer</code></a>
    + <a href="#Acm_DevSetLTCInAxisID"><code>Acm_DevSetLTCInAxisID</code></a>
    + <a href="#Acm_DevGetLTCInAxisID"><code>Acm_DevGetLTCInAxisID</code></a>
    + <a href="#Acm_DevSetCmpAxisID"><code>Acm_DevSetCmpAxisID</code></a>
    + <a href="#Acm_DevGetCmpAxisID"><code>Acm_DevGetCmpAxisID</code></a>
    + <a href="#Acm_GetDevNum"><code>Acm_GetDevNum</code></a>
    + <a href="#Acm_DevSaveMapFile"><code>Acm_DevSaveMapFile</code></a>
    + <a href="#Acm_DevLoadMapFile"><code>Acm_DevLoadMapFile</code></a>
    + <a href="#Acm_DevUpLoadMapInfo"><code>Acm_DevUpLoadMapInfo</code></a>
    + <a href="#Acm_DevDownLoadMapInfo"><code>Acm_DevDownLoadMapInfo</code></a>
    + <a href="#Acm_DevSetSlaveStates"><code>Acm_DevSetSlaveStates</code></a>
    + <a href="#Acm_DevGetSlaveStates"><code>Acm_DevGetSlaveStates</code></a>
    + <a href="#Acm_DevGetSlaveTxPDO"><code>Acm_DevGetSlaveTxPDO</code></a>
    + <a href="#Acm_DevGetSlaveRxPDO"><code>Acm_DevGetSlaveRxPDO</code></a>
    + <a href="#Acm_DevWriteSDOComplete"><code>Acm_DevWriteSDOComplete</code></a>
    + <a href="#Acm_DevWriteSDOData"><code>Acm_DevWriteSDOData</code></a>
    + <a href="#Acm_DevReadSDOData"><code>Acm_DevReadSDOData</code></a>
    + <a href="#Acm_DevWriteRegData"><code>Acm_DevWriteRegData</code></a>
    + <a href="#Acm_DevReadRegData"><code>Acm_DevReadRegData</code></a>
    + <a href="#Acm_DevReadEmgMessage"><code>Acm_DevReadEmgMessage</code></a>
    + <a href="#Acm_DevReadSlvCommErrCnt"><code>Acm_DevReadSlvCommErrCnt</code></a>
    + <a href="#Acm_DaqLinkPDO"><code>Acm_DaqLinkPDO</code></a>
    + <a href="#Acm_AxMoveTorque"><code>Acm_AxMoveTorque</code></a>
    + <a href="#Acm_AxGetActTorque"><code>Acm_AxGetActTorque</code></a>
    + <a href="#Acm_Ax2DCompensateInAx"><code>Acm_Ax2DCompensateInAx</code></a>
    + <a href="#Acm_Ax1DCompensateTable"><code>Acm_Ax1DCompensateTable</code></a>
    + <a href="#Acm_DevZAxisCompensateTable"><code>Acm_DevZAxisCompensateTable</code></a>
    + <a href="#Acm_Dev2DCompensateTable"><code>Acm_Dev2DCompensateTable</code></a>
    + <a href="#Acm_DevZAxisCompensateTableEx"><code>Acm_DevZAxisCompensateTableEx</code></a>
    + <a href="#Acm_Dev2DCompensateTableEx"><code>Acm_Dev2DCompensateTableEx</code></a>
    + <a href="#Acm_AxGetCompensatePosition"><code>Acm_AxGetCompensatePosition</code></a>
    + <a href="#Acm_DevMultiTrigInitial"><code>Acm_DevMultiTrigInitial</code></a>
    + <a href="#Acm_EnableOneDevEventCallBack"><code>Acm_EnableOneDevEventCallBack</code></a>
    + <a href="#Acm_AxGetRawData"><code>Acm_AxGetRawData</code></a>
    + <a href="#Acm_AxSetRawData"><code>Acm_AxSetRawData</code></a>
    + <a href="#Acm_AxReturnPausePosition"><code>Acm_AxReturnPausePosition</code></a>
    + <a href="#Acm_AxAddOnAx"><code>Acm_AxAddOnAx</code></a>
    + <a href="#Acm_AxAddRemove"><code>Acm_AxAddRemove</code></a>
    + <a href="#Acm_AxGetAddOnNum"><code>Acm_AxGetAddOnNum</code></a>
    + <a href="#Acm_AxSetCompensateDistance"><code>Acm_AxSetCompensateDistance</code></a>
    + <a href="#Acm_AxGetCompensateDistance"><code>Acm_AxGetCompensateDistance</code></a>
* Axis
    + <a href="#Acm_AxOpen"><code>Acm_AxOpen</code></a>
    + <a href="#Acm_AxOpenbyID"><code>Acm_AxOpenbyID</code></a>
    + <a href="#Acm_AxClose"><code>Acm_AxClose</code></a>
    + <a href="#Acm_AxSetSvOn"><code>Acm_AxSetSvOn</code></a>
    + <a href="#Acm_AxResetAlm"><code>Acm_AxResetAlm</code></a>
    + <a href="#Acm_AxMoveRel"><code>Acm_AxMoveRel</code></a>
    + <a href="#Acm_AxMoveRel_T"><code>Acm_AxMoveRel_T</code></a>
    + <a href="#Acm_AxMoveRel_SD"><code>Acm_AxMoveRel_SD</code></a>
    + <a href="#Acm_AxMoveRel_EC"><code>Acm_AxMoveRel_EC</code></a>
    + <a href="#Acm_AxMoveAbs"><code>Acm_AxMoveAbs</code></a>
    + <a href="#Acm_AxMoveAbs_T"><code>Acm_AxMoveAbs_T</code></a>
    + <a href="#Acm_AxMoveAbs_SD"><code>Acm_AxMoveAbs_SD</code></a>
    + <a href="#Acm_AxMoveAbs_EC"><code>Acm_AxMoveAbs_EC</code></a>
    + <a href="#Acm_AxMoveVel"><code>Acm_AxMoveVel</code></a>
    + <a href="#Acm_AxStopDec"><code>Acm_AxStopDec</code></a>
    + <a href="#Acm_AxStopDecEx"><code>Acm_AxStopDecEx</code></a>
    + <a href="#Acm_AxStopEmg"><code>Acm_AxStopEmg</code></a>
    + <a href="#Acm_AxMoveImpose"><code>Acm_AxMoveImpose</code></a>
    + <a href="#Acm_AxHomeEx"><code>Acm_AxHomeEx</code></a>
    + <a href="#Acm_AxHome"><code>Acm_AxHome</code></a>
    + <a href="#Acm_AxMoveHome"><code>Acm_AxMoveHome</code></a>
    + <a href="#Acm_AxMoveGantryHome"><code>Acm_AxMoveGantryHome</code></a>
    + <a href="#Acm_AxChangeVel"><code>Acm_AxChangeVel</code></a>
    + <a href="#Acm_AxChangePos"><code>Acm_AxChangePos</code></a>
    + <a href="#Acm_AxChangeVelByRate"><code>Acm_AxChangeVelByRate</code></a>
    + <a href="#Acm_AxChangeVelExByRate"><code>Acm_AxChangeVelExByRate</code></a>
    + <a href="#Acm_AxResetError"><code>Acm_AxResetError</code></a>
    + <a href="#Acm_AxGetState"><code>Acm_AxGetState</code></a>
    + <a href="#Acm_AxGetMotionIO"><code>Acm_AxGetMotionIO</code></a>
    + <a href="#Acm_AxGetMotionStatus"><code>Acm_AxGetMotionStatus</code></a>
    + <a href="#Acm_AxGetCmdPosition"><code>Acm_AxGetCmdPosition</code></a>
    + <a href="#Acm_AxGetMachPosition"><code>Acm_AxGetMachPosition</code></a>
    + <a href="#Acm_AxSetCmdPosition"><code>Acm_AxSetCmdPosition</code></a>
    + <a href="#Acm_AxGetActualPosition"><code>Acm_AxGetActualPosition</code></a>
    + <a href="#Acm_AxSetActualPosition"><code>Acm_AxSetActualPosition</code></a>
    + <a href="#Acm_AxGetCmdVelocity"><code>Acm_AxGetCmdVelocity</code></a>
    + <a href="#Acm_AxGetActVelocity"><code>Acm_AxGetActVelocity</code></a>
    + <a href="#Acm_AxGetLagCounter"><code>Acm_AxGetLagCounter</code></a>
    + <a href="#Acm_AxSetExtDrive"><code>Acm_AxSetExtDrive</code></a>
    + <a href="#Acm_AxDoSetBit"><code>Acm_AxDoSetBit</code></a>
    + <a href="#Acm_AxDiSetBit"><code>Acm_AxDiSetBit</code></a>
    + <a href="#Acm_AxDoGetBit"><code>Acm_AxDoGetBit</code></a>
    + <a href="#Acm_AxDiGetBit"><code>Acm_AxDiGetBit</code></a>
    + <a href="#Acm_AxDoSetByte"><code>Acm_AxDoSetByte</code></a>
    + <a href="#Acm_AxDoGetByte"><code>Acm_AxDoGetByte</code></a>
    + <a href="#Acm_AxDiGetByte"><code>Acm_AxDiGetByte</code></a>
    + <a href="#Acm_AxSimStartSuspendVel"><code>Acm_AxSimStartSuspendVel</code></a>
    + <a href="#Acm_AxSimStartSuspendRel"><code>Acm_AxSimStartSuspendRel</code></a>
    + <a href="#Acm_AxSimStartSuspendAbs"><code>Acm_AxSimStartSuspendAbs</code></a>
    + <a href="#Acm_AxSimStart"><code>Acm_AxSimStart</code></a>
    + <a href="#Acm_AxSimStop"><code>Acm_AxSimStop</code></a>
    + <a href="#Acm_AxGetLatchData"><code>Acm_AxGetLatchData</code></a>
    + <a href="#Acm_AxStartSoftLatch"><code>Acm_AxStartSoftLatch</code></a>
    + <a href="#Acm_AxResetLatch"><code>Acm_AxResetLatch</code></a>
    + <a href="#Acm_AxGetLatchFlag"><code>Acm_AxGetLatchFlag</code></a>
    + <a href="#Acm_AxTriggerLatch"><code>Acm_AxTriggerLatch</code></a>
    + <a href="#Acm_AxReadLatchBuffer"><code>Acm_AxReadLatchBuffer</code></a>
    + <a href="#Acm_AxResetLatchBuffer"><code>Acm_AxResetLatchBuffer</code></a>
    + <a href="#Acm_AxGetLatchBufferStatus"><code>Acm_AxGetLatchBufferStatus</code></a>
    + <a href="#Acm_AxGearInAx"><code>Acm_AxGearInAx</code></a>
    + <a href="#Acm_AxTangentInGp"><code>Acm_AxTangentInGp</code></a>
    + <a href="#Acm_AxGantryInAx"><code>Acm_AxGantryInAx</code></a>
    + <a href="#Acm_AxPhaseAx"><code>Acm_AxPhaseAx</code></a>
    + <a href="#Acm_AxSetChannelCmpSetting"><code>Acm_AxSetChannelCmpSetting</code></a>
    + <a href="#Acm_AxGetChannelCmpSetting"><code>Acm_AxGetChannelCmpSetting</code></a>
    + <a href="#Acm_AxResetChannelCmp"><code>Acm_AxResetChannelCmp</code></a>
    + <a href="#Acm_AxAddChannelCmpDatas"><code>Acm_AxAddChannelCmpDatas</code></a>
    + <a href="#Acm_AxGetChannelCmpData"><code>Acm_AxGetChannelCmpData</code></a>
    + <a href="#Acm_AxLoadChannelNextData"><code>Acm_AxLoadChannelNextData</code></a>
    + <a href="#Acm_AxGetCmpbufferRemainCount"><code>Acm_AxGetCmpbufferRemainCount</code></a>
    + <a href="#Acm_AxSetCmpAuto"><code>Acm_AxSetCmpAuto</code></a>
    + <a href="#Acm_AxGetCmpData"><code>Acm_AxGetCmpData</code></a>
    + <a href="#Acm_AxSetCmpData"><code>Acm_AxSetCmpData</code></a>
    + <a href="#Acm_AxChangeCmpIndex"><code>Acm_AxChangeCmpIndex</code></a>
    + <a href="#Acm_AxSetCmpBufferData"><code>Acm_AxSetCmpBufferData</code></a>
    + <a href="#Acm_AxResetCmpData"><code>Acm_AxResetCmpData</code></a>
    + <a href="#Acm_AxGetCmpBufferStatus"><code>Acm_AxGetCmpBufferStatus</code></a>
    + <a href="#Acm_AxResetMPGOffset"><code>Acm_AxResetMPGOffset</code></a>
    + <a href="#Acm_AxMovePTPBufferRel"><code>Acm_AxMovePTPBufferRel</code></a>
    + <a href="#Acm_AxMovePTPBufferAbs"><code>Acm_AxMovePTPBufferAbs</code></a>
    + <a href="#Acm_AxEnableCompensation"><code>Acm_AxEnableCompensation</code></a>
    + <a href="#Acm_AxGetCompensationValue"><code>Acm_AxGetCompensationValue</code></a>
    + <a href="#Acm_AxSetCompenPara"><code>Acm_AxSetCompenPara</code></a>
    + <a href="#Acm_AxDIStartMoveAbs"><code>Acm_AxDIStartMoveAbs</code></a>
    + <a href="#Acm_AxDIStartMoveRel"><code>Acm_AxDIStartMoveRel</code></a>
    + <a href="#Acm_AxDIStartMoveVel"><code>Acm_AxDIStartMoveVel</code></a>
    + <a href="#Acm_AxDisableDIStart"><code>Acm_AxDisableDIStart</code></a>
    + <a href="#Acm_AxSetPWMTableOnTime"><code>Acm_AxSetPWMTableOnTime</code></a>
    + <a href="#Acm_AxGetINxStopStatus"><code>Acm_AxGetINxStopStatus</code></a>
    + <a href="#Acm_AxResetINxStopStatus"><code>Acm_AxResetINxStopStatus</code></a>
    + <a href="#Acm_AxJog"><code>Acm_AxJog</code></a>
    + <a href="#Acm_AxSetCmpDO"><code>Acm_AxSetCmpDO</code></a>
    + <a href="#Acm_AxDownloadTorqueTable"><code>Acm_AxDownloadTorqueTable</code></a>
    + <a href="#Acm_AxLoadTorqueTableFile"><code>Acm_AxLoadTorqueTableFile</code></a>
    + <a href="#Acm_AxResetPVTTable"><code>Acm_AxResetPVTTable</code></a>
    + <a href="#Acm_AxLoadPVTTable"><code>Acm_AxLoadPVTTable</code></a>
    + <a href="#Acm_AxCalculatePVTTableContinuous"><code>Acm_AxCalculatePVTTableContinuous</code></a>
    + <a href="#Acm_AxLoadPVTTableContinuous"><code>Acm_AxLoadPVTTableContinuous</code></a>
    + <a href="#Acm_AxStartPVT"><code>Acm_AxStartPVT</code></a>
    + <a href="#Acm_AxStartAllPVT"><code>Acm_AxStartAllPVT</code></a>
    + <a href="#Acm_AxCheckPTBuffer"><code>Acm_AxCheckPTBuffer</code></a>
    + <a href="#Acm_AxAddPTData"><code>Acm_AxAddPTData</code></a>
    + <a href="#Acm_AxStartPT"><code>Acm_AxStartPT</code></a>
    + <a href="#Acm_AxStartAllPT"><code>Acm_AxStartAllPT</code></a>
    + <a href="#Acm_AxResetPTData"><code>Acm_AxResetPTData</code></a>
    + <a href="#Acm_AxAddPVAData"><code>Acm_AxAddPVAData</code></a>
* Group
    + <a href="#Acm_GpOpen"><code>Acm_GpOpen</code></a>
    + <a href="#Acm_GpAddAxis"><code>Acm_GpAddAxis</code></a>
    + <a href="#Acm_GpRemAxis"><code>Acm_GpRemAxis</code></a>
    + <a href="#Acm_GpClose"><code>Acm_GpClose</code></a>
    + <a href="#Acm_GpGetState"><code>Acm_GpGetState</code></a>
    + <a href="#Acm_GpResetError"><code>Acm_GpResetError</code></a>
    + <a href="#Acm_GpIpoMask"><code>Acm_GpIpoMask</code></a>
    + <a href="#Acm_GpMoveLinearRel"><code>Acm_GpMoveLinearRel</code></a>
    + <a href="#Acm_GpMoveLinearAbs"><code>Acm_GpMoveLinearAbs</code></a>
    + <a href="#Acm_GpMoveDirectRel"><code>Acm_GpMoveDirectRel</code></a>
    + <a href="#Acm_GpMoveDirectAbs"><code>Acm_GpMoveDirectAbs</code></a>
    + <a href="#Acm_GpMoveCircularRel"><code>Acm_GpMoveCircularRel</code></a>
    + <a href="#Acm_GpMoveCircularAbs"><code>Acm_GpMoveCircularAbs</code></a>
    + <a href="#Acm_GpMoveCircularRel_3P"><code>Acm_GpMoveCircularRel_3P</code></a>
    + <a href="#Acm_GpMoveCircularAbs_3P"><code>Acm_GpMoveCircularAbs_3P</code></a>
    + <a href="#Acm_GpMoveCircularRel_Angle"><code>Acm_GpMoveCircularRel_Angle</code></a>
    + <a href="#Acm_GpMoveCircularAbs_Angle"><code>Acm_GpMoveCircularAbs_Angle</code></a>
    + <a href="#Acm_GpMoveArcRel_Angle"><code>Acm_GpMoveArcRel_Angle</code></a>
    + <a href="#Acm_GpMoveArcAbs_Angle"><code>Acm_GpMoveArcAbs_Angle</code></a>
    + <a href="#Acm_GpMove3DArcAbs"><code>Acm_GpMove3DArcAbs</code></a>
    + <a href="#Acm_GpMove3DArcRel"><code>Acm_GpMove3DArcRel</code></a>
    + <a href="#Acm_GpMove3DArcAbs_V"><code>Acm_GpMove3DArcAbs_V</code></a>
    + <a href="#Acm_GpMove3DArcRel_V"><code>Acm_GpMove3DArcRel_V</code></a>
    + <a href="#Acm_GpMove3DArcAbs_3P"><code>Acm_GpMove3DArcAbs_3P</code></a>
    + <a href="#Acm_GpMove3DArcRel_3P"><code>Acm_GpMove3DArcRel_3P</code></a>
    + <a href="#Acm_GpMove3DArcAbs_3PAngle"><code>Acm_GpMove3DArcAbs_3PAngle</code></a>
    + <a href="#Acm_GpMove3DArcRel_3PAngle"><code>Acm_GpMove3DArcRel_3PAngle</code></a>
    + <a href="#Acm_GpMoveHelixAbs"><code>Acm_GpMoveHelixAbs</code></a>
    + <a href="#Acm_GpMoveHelixRel"><code>Acm_GpMoveHelixRel</code></a>
    + <a href="#Acm_GpMoveHelixAbs_3P"><code>Acm_GpMoveHelixAbs_3P</code></a>
    + <a href="#Acm_GpMove3DArcRel_3PAngle"><code>Acm_GpMove3DArcRel_3PAngle</code></a>
    + <a href="#Acm_GpMoveHelixAbs"><code>Acm_GpMoveHelixAbs</code></a>
    + <a href="#Acm_GpMoveHelixRel"><code>Acm_GpMoveHelixRel</code></a>
    + <a href="#Acm_GpMoveHelixAbs_3P"><code>Acm_GpMoveHelixAbs_3P</code></a>
    + <a href="#Acm_GpMoveHelixRel_3P"><code>Acm_GpMoveHelixRel_3P</code></a>
    + <a href="#Acm_GpMoveHelixRel_Angle"><code>Acm_GpMoveHelixRel_Angle</code></a>
    + <a href="#Acm_GpMoveHelixAbs_Angle"><code>Acm_GpMoveHelixAbs_Angle</code></a>
    + <a href="#Acm_GpMoveEllipticalRel"><code>Acm_GpMoveEllipticalRel</code></a>
    + <a href="#Acm_GpMoveEllipticalAbs"><code>Acm_GpMoveEllipticalAbs</code></a>
    + <a href="#Acm_GpLoadPath"><code>Acm_GpLoadPath</code></a>
    + <a href="#Acm_GpUnloadPath"><code>Acm_GpUnloadPath</code></a>
    + <a href="#Acm_GpMovePath"><code>Acm_GpMovePath</code></a>
    + <a href="#Acm_GpMoveAllPath"><code>Acm_GpMoveAllPath</code></a>
    + <a href="#Acm_GpAddPath"><code>Acm_GpAddPath</code></a>
    + <a href="#Acm_GpAddPath2"><code>Acm_GpAddPath2</code></a>
    + <a href="#Acm_GpLookAheadPath"><code>Acm_GpLookAheadPath</code></a>
    + <a href="#Acm_GpResetPath"><code>Acm_GpResetPath</code></a>
    + <a href="#Acm_GpGetPathStatus"><code>Acm_GpGetPathStatus</code></a>
    + <a href="#Acm_GpMoveSelPath"><code>Acm_GpMoveSelPath</code></a>
    + <a href="#Acm_GpGetPathIndexStatus"><code>Acm_GpGetPathIndexStatus</code></a>
    + <a href="#Acm_GpAddBSplinePath"><code>Acm_GpAddBSplinePath</code></a>
    + <a href="#Acm_GpAddCSplinePath"><code>Acm_GpAddCSplinePath</code></a>
    + <a href="#Acm_GpResumeMotion"><code>Acm_GpResumeMotion</code></a>
    + <a href="#Acm_GpPauseMotion"><code>Acm_GpPauseMotion</code></a>
    + <a href="#Acm_GpStopDec"><code>Acm_GpStopDec</code></a>
    + <a href="#Acm_GpStopDecEx"><code>Acm_GpStopDecEx</code></a>
    + <a href="#Acm_GpStopEmg"><code>Acm_GpStopEmg</code></a>
    + <a href="#Acm_GpChangeVel"><code>Acm_GpChangeVel</code></a>
    + <a href="#Acm_GpChangeVelByRate"><code>Acm_GpChangeVelByRate</code></a>
    + <a href="#Acm_GpGetCmdVel"><code>Acm_GpGetCmdVel</code></a>
    + <a href="#Acm_GpGetINxStopStatus"><code>Acm_GpGetINxStopStatus</code></a>
    + <a href="#Acm_GpResetINxStopStatus"><code>Acm_GpResetINxStopStatus</code></a>
    + <a href="#Acm_GpGetPausePosition"><code>Acm_GpGetPausePosition</code></a>
    + <a href="#Acm_GpSetRawData"><code>Acm_GpSetRawData</code></a>
    + <a href="#Acm_GpGetRawData"><code>Acm_GpGetRawData</code></a>
* DIO
    + <a href="#Acm_DaqDiGetByte"><code>Acm_DaqDiGetByte</code></a>
    + <a href="#Acm_DaqDiGetBit"><code>Acm_DaqDiGetBit</code></a>
    + <a href="#Acm_DaqDoSetByte"><code>Acm_DaqDoSetByte</code></a>
    + <a href="#Acm_DaqDoSetBit"><code>Acm_DaqDoSetBit</code></a>
    + <a href="#Acm_DaqDiSetBit"><code>Acm_DaqDiSetBit</code></a>
    + <a href="#Acm_DaqDoGetByte"><code>Acm_DaqDoGetByte</code></a>
    + <a href="#Acm_DaqDoGetBit"><code>Acm_DaqDoGetBit</code></a>
    + <a href="#Acm_DaqDiGetBytes"><code>Acm_DaqDiGetBytes</code></a>
    + <a href="#Acm_DaqDoSetBytes"><code>Acm_DaqDoSetBytes</code></a>
    + <a href="#Acm_DaqDoGetBytes"><code>Acm_DaqDoGetBytes</code></a>
    + <a href="#Acm_DaqDiGetByteEx"><code>Acm_DaqDiGetByteEx</code></a>
    + <a href="#Acm_DaqDiGetBitEx"><code>Acm_DaqDiGetBitEx</code></a>
    + <a href="#Acm_DaqDoSetByteEx"><code></code></a>
    + <a href="#Acm_DaqDoGetByteEx"><code>Acm_DaqDoGetByteEx</code></a>
    + <a href="#Acm_DaqDoGetBitEx"><code>Acm_DaqDoGetBitEx</code></a>
* AIO
    + <a href="#Acm_DaqAiGetRawData"><code>Acm_DaqAiGetRawData</code></a>
    + <a href="#Acm_DaqAiGetEngData"><code>Acm_DaqAiGetEngData</code></a>
    + <a href="#Acm_DaqAiGetVoltData"><code>Acm_DaqAiGetVoltData</code></a>
    + <a href="#Acm_DaqAiGetCurrData"><code>Acm_DaqAiGetCurrData</code></a>
    + <a href="#Acm_DaqAiZeroCalibration"><code>Acm_DaqAiZeroCalibration</code></a>
    + <a href="#Acm_DaqAiSpanCalibration"><code>Acm_DaqAiSpanCalibration</code></a>
    + <a href="#Acm_DaqAiGetChannelStatus"><code>Acm_DaqAiGetChannelStatus</code></a>
    + <a href="#Acm_DaqAoSetRawData"><code>Acm_DaqAoSetRawData</code></a>
    + <a href="#Acm_DaqAoSetEngData"><code>Acm_DaqAoSetEngData</code></a>
    + <a href="#Acm_DaqAoSetVoltData"><code>Acm_DaqAoSetVoltData</code></a>
    + <a href="#Acm_DaqAoSetCurrData"><code>Acm_DaqAoSetCurrData</code></a>
    + <a href="#Acm_DaqAoGetRawData"><code>Acm_DaqAoGetRawData</code></a>
    + <a href="#Acm_DaqAoGetEngData"><code>Acm_DaqAoGetEngData</code></a>
    + <a href="#Acm_DaqAoGetVoltData"><code>Acm_DaqAoGetVoltData</code></a>
    + <a href="#Acm_DaqAoGetCurrData"><code>Acm_DaqAoGetCurrData</code></a>
    + <a href="#Acm_DaqAoSetCaliType"><code>Acm_DaqAoSetCaliType</code></a>
    + <a href="#Acm_DaqAoSetCaliValue"><code>Acm_DaqAoSetCaliValue</code></a>
    + <a href="#Acm_DaqAoCaliDone"><code>Acm_DaqAoCaliDone</code></a>
    + <a href="#Acm_DaqAoCaliDefault"><code>Acm_DaqAoCaliDefault</code></a>
    + <a href="#Acm_DaqAoGetChannelStatus"><code>Acm_DaqAoGetChannelStatus</code></a>
    + <a href="#Acm_DaqSetScaledProperty"><code>Acm_DaqSetScaledProperty</code></a>
    + <a href="#Acm_DaqAiGetRawDataEx"><code>Acm_DaqAiGetRawDataEx</code></a>
    + <a href="#Acm_DaqAiGetEngDataEx"><code>Acm_DaqAiGetEngDataEx</code></a>
    + <a href="#Acm_DaqAiGetVoltDataEx"><code>Acm_DaqAiGetVoltDataEx</code></a>
    + <a href="#Acm_DaqAiGetCurrDataEx"><code>Acm_DaqAiGetCurrDataEx</code></a>
    + <a href="#Acm_DaqAiGetChannelStatusEx"><code>Acm_DaqAiGetChannelStatusEx</code></a>
    + <a href="#Acm_DaqAoSetRawDataEx"><code>Acm_DaqAoSetRawDataEx</code></a>
    + <a href="#Acm_DaqAoSetEngDataEx"><code>Acm_DaqAoSetEngDataEx</code></a>
    + <a href="#Acm_DaqAoSetVoltDataEx"><code>Acm_DaqAoSetVoltDataEx</code></a>
    + <a href="#Acm_DaqAoSetCurrDataEx"><code>Acm_DaqAoSetCurrDataEx</code></a>
    + <a href="#Acm_DaqAoGetRawDataEx"><code>Acm_DaqAoGetRawDataEx</code></a>
    + <a href="#Acm_DaqAoGetEngDataEx"><code>Acm_DaqAoGetEngDataEx</code></a>
    + <a href="#Acm_DaqAoGetVoltDataEx"><code>Acm_DaqAoGetVoltDataEx</code></a>
    + <a href="#Acm_DaqAoGetCurrDataEx"><code>Acm_DaqAoGetCurrDataEx</code></a>
    + <a href="#Acm_DaqGetIOLinkStatus"><code>Acm_DaqGetIOLinkStatus</code></a>
    + <a href="#Acm_DaqCntTriggerCmp"><code>Acm_DaqCntTriggerCmp</code></a>
    + <a href="#Acm_DaqCntResetLatch"><code>Acm_DaqCntResetLatch</code></a>
    + <a href="#Acm_DaqCntResetCmp"><code>Acm_DaqCntResetCmp</code></a>
    + <a href="#Acm_DaqCntResetCnt"><code>Acm_DaqCntResetCnt</code></a>
    + <a href="#Acm_DaqCntGetCounterData"><code>Acm_DaqCntGetCounterData</code></a>
    + <a href="#Acm_DaqCntSetCounterData"><code>Acm_DaqCntSetCounterData</code></a>
    + <a href="#Acm_DaqCntGetCounterFrequency"><code>Acm_DaqCntGetCounterFrequency</code></a>
    + <a href="#Acm_DaqCntGetExtDriveData"><code>Acm_DaqCntGetExtDriveData</code></a>
    + <a href="#Acm_DaqCntSetExtDriveData"><code>Acm_DaqCntSetExtDriveData</code></a>
    + <a href="#Acm_DaqCntGetLatchData"><code>Acm_DaqCntGetLatchData</code></a>
    + <a href="#Acm_DaqCntGetCmpData"><code>Acm_DaqCntGetCmpData</code></a>
    + <a href="#Acm_DaqCntSetCmpData"><code>Acm_DaqCntSetCmpData</code></a>
    + <a href="#Acm_DaqCntSetCmpTable"><code>Acm_DaqCntSetCmpTable</code></a>
    + <a href="#Acm_DaqCntSetCmpAuto"><code>Acm_DaqCntSetCmpAuto</code></a>
    + <a href="#Acm_DaqCntGetLatchBufferStatus"><code>Acm_DaqCntGetLatchBufferStatus</code></a>
    + <a href="#Acm_DaqCntReadLatchBuffer"><code>Acm_DaqCntReadLatchBuffer</code></a>
    + <a href="#Acm_DaqCntTriggerCmpEx"><code>Acm_DaqCntTriggerCmpEx</code></a>
    + <a href="#Acm_DaqCntTriggerLatchEx"><code>Acm_DaqCntTriggerLatchEx</code></a>
    + <a href="#Acm_DaqCntResetLatchEx"><code>Acm_DaqCntResetLatchEx</code></a>
    + <a href="#Acm_DaqCntResetCmpEx"><code>Acm_DaqCntResetCmpEx</code></a>
    + <a href="#Acm_DaqCntResetCntEx"><code>Acm_DaqCntResetCntEx</code></a>
    + <a href="#Acm_DaqCntGetCounterDataEx"><code>Acm_DaqCntGetCounterDataEx</code></a>
    + <a href="#Acm_DaqCntSetCounterDataEx"><code>Acm_DaqCntSetCounterDataEx</code></a>
    + <a href="#Acm_DaqCntGetCounterFrequencyEx"><code>Acm_DaqCntGetCounterFrequencyEx</code></a>
    + <a href="#Acm_DaqCntGetExtDriveDataEx"><code>Acm_DaqCntGetExtDriveDataEx</code></a>
    + <a href="#Acm_DaqCntSetExtDriveDataEx"><code>Acm_DaqCntSetExtDriveDataEx</code></a>
    + <a href="#Acm_DaqCntGetLatchDataEx"><code>Acm_DaqCntGetLatchDataEx</code></a>
    + <a href="#Acm_DaqCntGetCmpDataEx"><code>Acm_DaqCntGetCmpDataEx</code></a>
    + <a href="#Acm_DaqCntSetCmpDataEx"><code>Acm_DaqCntSetCmpDataEx</code></a>
    + <a href="#Acm_DaqCntSetCmpTableEx"><code>Acm_DaqCntSetCmpTableEx</code></a>
    + <a href="#Acm_DaqCntSetCmpAutoEx"><code>Acm_DaqCntSetCmpAutoEx</code></a>
    + <a href="#Acm_DaqCntGetLatchBufferStatusEx"><code>Acm_DaqCntGetLatchBufferStatusEx</code></a>
    + <a href="#Acm_DaqCntReadLatchBufferEx"><code>Acm_DaqCntReadLatchBufferEx</code></a>
    + <a href="#Acm_AxPWMOut"><code>Acm_AxPWMOut</code></a>
    + <a href="#Acm_AxGetPWMOutState"><code>Acm_AxGetPWMOutState</code></a>
* EtherCAT
    + <a href="#Acm_DevECATOpen"><code>Acm_DevECATOpen</code></a>
    + <a href="#Acm_DevReadMailBox"><code>Acm_DevReadMailBox</code></a>
    + <a href="#Acm_DevReadMultiMailBox"><code>Acm_DevReadMultiMailBox</code></a>
    + <a href="#Acm_DevWriteMailBox"><code>Acm_DevWriteMailBox</code></a>
    + <a href="#Acm_LoadENI"><code>Acm_LoadENI</code></a>
    + <a href="#Acm_DevGetMasInfo"><code>Acm_DevGetMasInfo</code></a>
    + <a href="#Acm_DevGetMasStates"><code>Acm_DevGetMasStates</code></a>
    + <a href="#Acm_DevGetSlaveInfo"><code>Acm_DevGetSlaveInfo</code></a>
    + <a href="#Acm_DevGetModuleInfo"><code>Acm_DevGetModuleInfo</code></a>
    + <a href="#Acm_DevGetSlaveDataCnt"><code>Acm_DevGetSlaveDataCnt</code></a>
    + <a href="#Acm_DevGetSlaveFwVersion"><code>Acm_DevGetSlaveFwVersion</code></a>
    + <a href="#Acm_DevSetSlaveID"><code>Acm_DevSetSlaveID</code></a>
---
#### Acm_GetAvailableDevs
<a name="Acm_GetAvailableDevs" />

```cpp
U32 Acm_GetAvailableDevs(DEVLIST *DeviceList, U32 MaxEntries, PU32 OutEntries)
```

#### Acm_GetErrorMessage
<a name="Acm_GetErrorMessage" />

```cpp
BOOL Acm_GetErrorMessage(U32 ErrorCode, PI8 lpszError,  U32 nMaxError)
```

#### Acm_DevOpen
<a name="Acm_DevOpen" />

```cpp
U32 Acm_DevOpen(U32 DeviceNumber, PHAND DeviceHandle)
```

#### Acm_DevReOpen
<a name="Acm_DevReOpen" />

```cpp
U32 Acm_DevOpen(U32 DeviceNumber, PHAND DeviceHandle)
```

#### Acm_DevClose
<a name="Acm_DevClose" />

```cpp
U32 Acm_DevClose(PHAND DeviceHandle)
```

#### Acm_GetLastError
<a name="Acm_GetLastError" />

```cpp
U32 Acm_GetLastError(HAND Handle)
```
#### Acm_GetProperty
<a name="Acm_GetProperty" />

```cpp
U32 Acm_GetProperty(HAND Handle, U32 PropertyID, PVOID Buffer, PU32 BufferLength)
```

#### Acm_SetProperty
<a name="Acm_SetProperty" />

```cpp
U32 Acm_SetProperty(HAND Handle, U32 PropertyID, PVOID Buffer, U32 BufferLength)
```

#### Acm_GetU32Property
<a name="Acm_GetU32Property" />

```cpp
U32 Acm_GetU32Property(HAND Handle, U32 PropertyID, PU32 Value)
```

#### Acm_GetI32Property
<a name="Acm_GetI32Property" />

```cpp
U32 Acm_GetI32Property(HAND Handle, U32 PropertyID, PI32 Value)
```

#### Acm_GetF64Property
<a name="Acm_GetF64Property" />

```cpp
U32 Acm_GetF64Property(HAND Handle, U32 PropertyID, PF64 Value)
```

#### Acm_GetStringProperty
<a name="Acm_GetStringProperty" />

```cpp
U32 Acm_GetStringProperty(HAND Handle, U32 PropertyID, PU8 Value);
```

#### Acm_SetU32Property
<a name="Acm_SetU32Property" />

```cpp
U32 Acm_SetU32Property(HAND Handle, U32 PropertyID, U32 Value)
```

#### Acm_SetI32Property
<a name="Acm_SetI32Property" />

```cpp
U32 Acm_SetI32Property(HAND Handle, U32 PropertyID, I32 Value)
```

#### Acm_SetF64Property
<a name="Acm_SetF64Property" />

```cpp
U32 Acm_SetF64Property(HAND Handle, U32 PropertyID, F64 Value)
```

#### Acm_SetStringProperty
<a name="Acm_SetStringProperty" />

```cpp
U32 Acm_SetStringProperty(HAND Handle, U32 PropertyID, PU8 Value)
```

#### Acm_GetMultiProperty
<a name="Acm_GetMultiProperty" />

```cpp
U32 Acm_GetMultiProperty (HAND Handle, PU32 PropertyIDArray, PF64 ValueArray, U32 PropertyCnt, PU32 ErrorBuffer)
```

#### Acm_SetMultiU32Property
<a name="Acm_SetMultiU32Property" />

```cpp
U32 Acm_SetMultiU32Property(HAND Handle, PU32 PropertyIDArray, PU32 ValueArray, U32 PropertyCnt)
```

#### Acm_SetMultiI32Property
<a name="Acm_SetMultiI32Property" />

```cpp
U32 Acm_SetMultiI32Property(HAND Handle, PU32 PropertyIDArray, PI32 ValueArray, U32 PropertyCnt)
```

#### Acm_SetMultiF64Property
<a name="Acm_SetMultiF64Property" />

```cpp
U32 Acm_SetMultiF64Property(HAND Handle, PU32 PropertyIDArray, PF64 ValueArray, U32 PropertyCnt)
```

#### Acm_GetChannelProperty
<a name="Acm_GetChannelProperty" />

```cpp
U32 Acm_GetChannelProperty(HAND Handle, U32 ChannelID, U32 PropertyID,  PF64 Value)
```

#### Acm_SetChannelProperty
<a name="Acm_SetChannelProperty" />

```cpp
U32 Acm_SetChannelProperty(HAND Handle, U32 ChannelID, U32 PropertyID,  F64 Value)
```

#### Acm_GetMultiChannelProperty
<a name="Acm_GetMultiChannelProperty" />

```cpp
U32 Acm_GetMultiChannelProperty(HAND Handle, U32 PropertyID, U32 StartChID, U32 ChCount, PF64 ValueArray)
```

#### Acm_SetMultiChannelProperty
<a name="Acm_SetMultiChannelProperty" />

```cpp
U32 Acm_SetMultiChannelProperty(HAND Handle, U32 PropertyID, U32 StartChID, U32 ChCount, PF64 ValueArray)
```

#### Acm_DevEnableEvent
<a name="Acm_DevEnableEvent" />

```cpp
U32 Acm_DevEnableEvent(HAND DeviceHandle, U32 DevEnableEvt)
```

#### Acm_DevCheckEvent
<a name="Acm_DevCheckEvent" />

```cpp
U32 Acm_DevCheckEvent(HAND DeviceHandle, PU32 DevCheckEvt, U32 Millisecond);
```

#### Acm_EnableMotionEvent
<a name="Acm_EnableMotionEvent" />

```cpp
U32 Acm_EnableMotionEvent(HAND DeviceHandle, PU32 AxEnableEvtArray, PU32 GpEnableEvtArray, U32 AxArrayElements, U32 GpArrayElements)
```

#### Acm_CheckMotionEvent
<a name="Acm_CheckMotionEvent" />

```cpp
U32 Acm_CheckMotionEvent(HAND DeviceHandle, PU32 AxEvtStatusArray, PU32 GpEvtStatusArray, U32 AxArrayElements, U32 GpArrayElements, U32 Millisecond)
```

#### Acm_CancelCheckEvent
<a name="Acm_CancelCheckEvent" />

```cpp
U32 Acm_CancelCheckEvent(HAND ObjectHandle)
```

#### Acm_DevEnableEvent_All
<a name="Acm_DevEnableEvent_All" />

```cpp
U32 Acm_DevEnableEvent_All(HAND DeviceHandle, PU32 DevEnableEvtArray, PU32 AxEnableEvtArray, PU32 GpEnableEvtArray, U32 AxArrayElements,U32 GpArrayElements)
```

#### Acm_DevCheckEvent_All
<a name="Acm_DevCheckEvent_All" />

```cpp
U32 Acm_DevCheckEvent_All(HAND DeviceHandle, PU32 DevEvtStatusArray, PU32 AxEvtStatusArray, PU32 GpEvtStatusArray, U32 AxArrayElements, U32 GpArrayElements, U32 Millisecond);
```

#### Acm_DevLoadConfig
<a name="Acm_DevLoadConfig" />

```cpp
U32 Acm_DevLoadConfig(HAND DeviceHandle, PI8 ConfigPath)
```

#### Acm_DevSlaveFwDownload
<a name="Acm_DevSlaveFwDownload" />

```cpp
U32 Acm_DevSlaveFwDownload(HAND DeviceHandle, U16 RingNo, U16 Position, PI8 FileName, PI8 FilePath, U32 Password)
```

#### Acm_DevWriteDPMData
<a name="Acm_DevWriteDPMData" />

```cpp
U32 Acm_DevWriteDPMData(HAND Handle, U16 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```

#### Acm_DevWriteMultiMailBox
<a name="Acm_DevWriteMultiMailBox" />

```cpp
U32 Acm_DevWriteMultiMailBox(HAND Handle, U8 object_id, PU16 par_id, PU32 DataBuffer, PU32 ErrorBuffer, U32 ArrayElements)
```

#### Acm_WriteRingBuffer
<a name="Acm_WriteRingBuffer" />

```cpp
U32 Acm_WriteRingBuffer(HAND Handle, U32 cmd_id, U32 data_index, U32 data_cnt, PU32 dataBuffer)
```

#### Acm_ReadRingBuffer
<a name="Acm_ReadRingBuffer" />

```cpp
U32 Acm_ReadRingBuffer(HAND Handle, PU32 cmd_id, PU32 data_index, U32 data_cnt, PU32 dataBuffer)
```

#### Acm_DevGetComStatus
<a name="Acm_DevGetComStatus" />

```cpp
U32 Acm_DevGetComStatus(HAND DeviceHandle, U16 RingNo, PU16 pStatus)
```

#### Acm_DevGetErrorTable
<a name="Acm_DevGetErrorTable" />

```cpp
U32 Acm_DevGetErrorTable(HAND DeviceHandle, U16 RingNo, PU32 ErrorTableArray, PU32 ArrayElements)
```

#### Acm_DevGetIOInfo
<a name="Acm_DevGetIOInfo" />

```cpp
U32 Acm_DevGetIOInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Slot, U8 DataType, PVOID pInfo)
```

#### Acm_CheckVersion
<a name="Acm_CheckVersion" />

```cpp
U32 Acm_CheckVersion(HAND DeviceHandle, U32 VersionID, PU32 Result)
```

#### Acm_DevMultiTrigSetPWMTableOnTime
<a name="Acm_DevMultiTrigSetPWMTableOnTime" />

```cpp
U32 Acm_DevMultiTrigSetPWMTableOnTime(HAND DeviceHandle, PU32 TimeTableArray, U32 ArrayCount)
```

#### Acm_DevMultiTrigSetCmpDO
<a name="Acm_DevMultiTrigSetCmpDO" />

```cpp
U32 Acm_DevMultiTrigSetCmpDO(HAND DeviceHandle,U32 OFForON)
```

#### Acm_DevMultiTrigForceCmpOut
<a name="Acm_DevMultiTrigForceCmpOut" />

```cpp
U32 Acm_DevMultiTrigForceCmpOut(HAND DeviceHandle, U32 OFForON)
```

#### Acm_DevMutiTrigSetCmpDO
<a name="Acm_DevMutiTrigSetCmpDO" />

```cpp
U32 Acm_DevMutiTrigSetCmpDO(HAND DeviceHandle,U32 OFForON)
```

#### Acm_DevMutiTrigForceCmpOut
<a name="Acm_DevMutiTrigForceCmpOut" />

```cpp
U32 Acm_DevMutiTrigForceCmpOut(HAND DeviceHandle, U32 OFForON)
```

#### Acm_MasStartRing
<a name="Acm_MasStartRing" />

```cpp
U32 Acm_MasStartRing(HAND DeviceHandle, U16 RingNo)
```

#### Acm_MasStopRing
<a name="Acm_MasStopRing" />

```cpp
U32 Acm_MasStopRing(HAND DeviceHandle, U16 RingNo)
```

#### Acm_MasGetComStatus
<a name="Acm_MasGetComStatus" />

```cpp
U32 Acm_MasGetComStatus(HAND DeviceHandle, U16 RingNo, PU16 pStatus)
```

#### Acm_MasGetComCyclicTime
<a name="Acm_MasGetComCyclicTime" />

```cpp
U32 Acm_MasGetComCyclicTime(HAND DeviceHandle, U16 RingNo, PF64 pTime)
```

#### Acm_MasGetDataCyclicTime
<a name="Acm_MasGetDataCyclicTime" />

```cpp
U32 Acm_MasGetDataCyclicTime(HAND DeviceHandle, U16 RingNo, PF64 DataCyclicTime)
```

#### Acm_MasGetActiveTable
<a name="Acm_MasGetActiveTable" />

```cpp
U32 Acm_MasGetActiveTable(HAND DeviceHandle, U16 RingNo, PU32 ActiveTableArray, PU32 ArrayElements)
```

#### Acm_MasGetErrorTable
<a name="Acm_MasGetErrorTable" />

```cpp
U32 Acm_MasGetErrorTable(HAND DeviceHandle, U16 RingNo, PU32 ErrorTableArray, PU32 ArrayElements)
```

#### Acm_MasGetSlaveInfo
<a name="Acm_MasGetSlaveInfo" />

```cpp
U32 Acm_MasGetSlaveInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PU32 pInfo)
```

#### Acm_MasLogComStatus
<a name="Acm_MasLogComStatus" />

```cpp
U32 Acm_MasLogComStatus(HAND DeviceHandle, U16 RingNo)
```

#### Acm_DevDownloadScanData
<a name="Acm_DevDownloadScanData" />

```cpp
U32 Acm_DevDownloadScanData(HAND DeviceHandle, PDEV_PRE_SCAN_DATA pScanDataArray, U32 ArrayLength)
```

#### Acm_DevMDaqConfig
<a name="Acm_DevMDaqConfig" />

```cpp
U32 Acm_DevMDaqConfig(HAND DeviceHandle, U16 ChannelID, U32 Period, U32 AxisNo, U32 Method, U32 ChanType, U32 Count)
```

#### Acm_DevMDaqStart
<a name="Acm_DevMDaqStart" />

```cpp
U32 Acm_DevMDaqStart(HAND DeviceHandle)
```

#### Acm_DevMDaqStop
<a name="Acm_DevMDaqStop" />

```cpp
U32 Acm_DevMDaqStop(HAND DeviceHandle)
```

#### Acm_DevMDaqReset
<a name="Acm_DevMDaqReset" />

```cpp
U32 Acm_DevMDaqReset(HAND DeviceHandle, U16 ChannelID)
```

#### Acm_DevMDaqGetStatus
<a name="Acm_DevMDaqGetStatus" />

```cpp
U32 Acm_DevMDaqGetStatus(HAND DeviceHandle, U16 ChannelID, PU16 CurrentCnt, PU8 Status)
```

#### Acm_DevMDaqGetData
<a name="Acm_DevMDaqGetData" />

```cpp
U32 Acm_DevMDaqGetData(HAND DeviceHandle, U16 ChannelID, U16 StartIndex, U16 MaxCount, PI32 DataBuffer)
```

#### Acm_DevMDaqGetConfig
<a name="Acm_DevMDaqGetConfig" />

```cpp
U32 Acm_DevMDaqGetConfig(HAND DeviceHandle, U16 ChannelID, PU32 Period, PU32 AxisNo, PU32 Method, PU32 ChanType, PU32 Count)
```

#### Acm_RegCallBackFunc
<a name="Acm_RegCallBackFunc" />

```cpp
U32 Acm_RegCallBackFunc(HAND Handle, ADV_USER_CALLBACK_FUNC CallBackFun, PVOID UserParamter)
```

#### Acm_EnableEventCallBack
<a name="Acm_EnableEventCallBack" />

```cpp
U32 Acm_EnableEventCallBack(HAND DeviceHandle)
```

#### Acm_RegCallBackFuncForOneEvent
<a name="Acm_RegCallBackFuncForOneEvent" />

```cpp
U32 Acm_RegCallBackFuncForOneEvent(HAND Handle, U32 EvtChannel, ADV_USER_CALLBACK_FUNC CallBackFun, PVOID UserParamter)
```

#### Acm_DevEnableMotionEvent
<a name="Acm_DevEnableMotionEvent" />

```cpp
U32 Acm_DevEnableMotionEvent(HAND DeviceHandle, PU32 AxEnableEvtArray, PU32 GpEnableEvtArray, U32 AxArrayElements, U32 GpArrayElements)
```

#### Acm_ServoSetCom
<a name="Acm_ServoSetCom" />

```cpp
U32 Acm_ServoSetCom(U32 ComPortID, U32 Baudrate, U32 Timeout)
```

#### Acm_ServoGetAbsPosition
<a name="Acm_ServoGetAbsPosition" />

```cpp
U32 Acm_ServoGetAbsPosition(U32 ComPortID, U32 ServoType, U32 ServoID, U32 ServoAbsResolution, U32 ServoCmdResolution, U32 EncoderDir, PF64 AbsPosition)
```

#### Acm_AxSetCmdPosi_Pulse
<a name="Acm_AxSetCmdPosi_Pulse" />

```cpp
U32 Acm_AxSetCmdPosi_Pulse(HAND AxisHandle,F64 Position)
```

#### Acm_AxSpecialDiSetBit
<a name="Acm_AxSpecialDiSetBit" />

```cpp
U32 Acm_AxSpecialDiSetBit(HAND AxisHandle,U16 DiType,U8 BitData)
```

#### Acm_DevEnableLTC
<a name="Acm_DevEnableLTC" />

```cpp
U32 Acm_DevEnableLTC(HAND DeviceHandle, U16 LtcID, U16 EnableMode)
```

#### Acm_DevLTCSaftyDist
<a name="Acm_DevLTCSaftyDist" />

```cpp
U32 Acm_DevLTCSaftyDist(HAND DeviceHandle, U16 LtcID, F64 SaftyDist)
```

#### Acm_DevEnableCmp
<a name="Acm_DevEnableCmp" />

```cpp
U32 Acm_DevEnableCmp(HAND DeviceHandle, U16 CmpID, U16 EnableMode)
```

#### Acm_DevLtcLinkCmp
<a name="Acm_DevLtcLinkCmp" />

```cpp
U32 Acm_DevLtcLinkCmp(HAND DeviceHandle, HAND AxisHandle, U16 EnableLink, U16 LtcID, U16 CmpID, F64 Offset)
```

#### Acm_DevSetCmp
<a name="Acm_DevSetCmp" />

```cpp
U32 Acm_DevSetCmp(HAND DeviceHandle, U16 CmpID, U32 CmpLogic, U32 CmpSrc, U32 CmpMethod, U32 DOMode, U32 DOWidth)
```

#### Acm_DevSetCmpDO
<a name="Acm_DevSetCmpDO" />

```cpp
U32 Acm_DevSetCmpDO(HAND DeviceHandle, U16 CmpID, U16 OnOff)
```

#### Acm_DevSetCmpData
<a name="Acm_DevSetCmpData" />

```cpp
U32 Acm_DevSetCmpData(HAND DeviceHandle, U16 CmpID, F64 Data)
```

#### Acm_DevSetCmpAuto
<a name="Acm_DevSetCmpAuto" />

```cpp
U32 Acm_DevSetCmpAuto(HAND DeviceHandle, U16 CmpID, F64 Start, F64 End, F64 Interval)
```

#### Acm_DevGetCmpData
<a name="Acm_DevGetCmpData" />

```cpp
U32 Acm_DevGetCmpData(HAND DeviceHandle, U16 CmpID, PF64 Data)
```

#### Acm_DevEnableCmpFIFO
<a name="Acm_DevEnableCmpFIFO" />

```cpp
U32 Acm_DevEnableCmpFIFO(HAND DeviceHandle, U16 CmpID, U16 Enable)
```

#### Acm_DevGetCmpFIFOCount
<a name="Acm_DevGetCmpFIFOCount" />

```cpp
U32 Acm_DevGetCmpFIFOCount(HAND DeviceHandle, U16 CmpID, PU16 DataCount)
```

#### Acm_DevGetCmpCounter
<a name="Acm_DevGetCmpCounter" />

```cpp
U32 Acm_DevGetCmpCounter(HAND DeviceHandle, U16 CmpID, PU32 DataCount)
```

#### Acm_DevResetCmpFIFO
<a name="Acm_DevResetCmpFIFO" />

```cpp
U32 Acm_DevResetCmpFIFO(HAND DeviceHandle, U16 CmpID)
```

#### Acm_DevSetLTCInEdge
<a name="Acm_DevSetLTCInEdge" />

```cpp
U32 Acm_DevSetLTCInEdge(HAND DeviceHandle, U16 LtcID, U16 Edge)
```

#### Acm_DevGetLTCData
<a name="Acm_DevGetLTCData" />

```cpp
U32 Acm_DevGetLTCData(HAND DeviceHandle, U16 LtcID, PF64 CommandPosition, PF64 Actualposition)
```

#### Acm_DevGetLTCFlag
<a name="Acm_DevGetLTCFlag" />

```cpp
U32 Acm_DevGetLTCFlag(HAND DeviceHandle, U16 LtcID, PU8 LtcFlag)
```

#### Acm_DevResetLTC
<a name="Acm_DevResetLTC" />

```cpp
U32 Acm_DevResetLTC(HAND DeviceHandle, U16 LtcID)
```

#### Acm_DevGetCmpFlag
<a name="Acm_DevGetCmpFlag" />

```cpp
U32 Acm_DevGetCmpFlag(HAND DeviceHandle, U16 CmpID, PU8 CmpFlag)
```

#### Acm_DevResetCmpFlag
<a name="Acm_DevResetCmpFlag" />

```cpp
U32 Acm_DevResetCmpFlag(HAND DeviceHandle, U16 CmpID)
```

#### Acm_DevGetLtcLinkCmpStatus
<a name="Acm_DevGetLtcLinkCmpStatus" />

```cpp
U32 Acm_DevGetLtcLinkCmpStatus(HAND DeviceHandle, U16 LtcID, PU16 LinkStatus)
```

#### Acm_DevResetCmpData
<a name="Acm_DevResetCmpData" />

```cpp
U32 Acm_DevResetCmpData(HAND DeviceHandle, U16 CmpID)
```

#### Acm_DevGetLTCInEdge
<a name="Acm_DevGetLTCInEdge" />

```cpp
U32 Acm_DevGetLTCInEdge(HAND DeviceHandle, U16 LtcID, PU16 Edge)
```

#### Acm_DevGetLTCInPol
<a name="Acm_DevGetLTCInPol" />

```cpp
U32 Acm_DevGetLTCInPol(HAND DeviceHandle, U16 LtcID, PU16 Logic)
```

#### Acm_DevGetLTCSaftyDist
<a name="Acm_DevGetLTCSaftyDist" />

```cpp
U32 Acm_DevGetLTCSaftyDist(HAND DeviceHandle, U16 LtcID, PF64 SaftyDist)
```

#### Acm_DevGetLTCInSource
<a name="Acm_DevGetLTCInSource" />

```cpp
U32 Acm_DevGetLTCInSource(HAND DeviceHandle, U16 LtcID, PU16 Source)
```

#### Acm_DevSetLTCInSource
<a name="Acm_DevSetLTCInSource" />

```cpp
U32 Acm_DevSetLTCInSource(HAND DeviceHandle, U16 LtcID, U16 Source)
```

#### Acm_DevGetCmp
<a name="Acm_DevGetCmp" />

```cpp
U32 Acm_DevGetCmp(HAND DeviceHandle, U16 CmpID, PU32 CmpLogic, PU32 CmpSrc, PU32 CmpMethod, PU32 DOMode, PU32 DOWidth)
```

#### Acm_DevReadLatchBuffer
<a name="Acm_DevReadLatchBuffer" />

```cpp
U32 Acm_DevReadLatchBuffer(HAND DeviceHandle, U16 LtcID, PF64 CommandPositionArray, PF64 ActualPositionArray, PU32 DataCnt)
```

#### Acm_DevGetLatchBufferStatus
<a name="Acm_DevGetLatchBufferStatus" />

```cpp
U32 Acm_DevGetLatchBufferStatus(HAND DeviceHandle, U16 LtcID, PU32 RemainCnt, PU32 SpaceCnt, PU32 LtcCounter)
```

#### Acm_DevResetLatchBuffer
<a name="Acm_DevResetLatchBuffer" />

```cpp
U32 Acm_DevResetLatchBuffer(HAND DeviceHandle, U16 LtcID)
```

#### Acm_DevSetLTCInAxisID
<a name="Acm_DevSetLTCInAxisID" />

```cpp
U32 Acm_DevSetLTCInAxisID(HAND DeviceHandle, U16 LtcID, U32 AxisID)
```

#### Acm_DevGetLTCInAxisID
<a name="Acm_DevGetLTCInAxisID" />

```cpp
U32 Acm_DevGetLTCInAxisID(HAND DeviceHandle, U16 LtcID, PU32 AxisID)
```

#### Acm_DevSetCmpAxisID
<a name="Acm_DevSetCmpAxisID" />

```cpp
U32 Acm_DevSetCmpAxisID(HAND DeviceHandle, U16 CmpID, U32 AxisID)
```

#### Acm_DevGetCmpAxisID
<a name="Acm_DevGetCmpAxisID" />

```cpp
U32 Acm_DevGetCmpAxisID(HAND DeviceHandle, U16 CmpID, PU32 AxisID)
```

#### Acm_GetDevNum
<a name="Acm_GetDevNum" />

```cpp
U32 Acm_GetDevNum(U32 DevType,U32 BoardID,PU32 DeviceNumber)
```

#### Acm_DevSaveMapFile
<a name="Acm_DevSaveMapFile" />

```cpp
U32 Acm_DevSaveMapFile(HAND DeviceHandle, PI8 FilePath)
```

#### Acm_DevLoadMapFile
<a name="Acm_DevLoadMapFile" />

```cpp
U32 Acm_DevLoadMapFile(HAND DeviceHandle, PI8 FilePath)
```

#### Acm_DevUpLoadMapInfo
<a name="Acm_DevUpLoadMapInfo" />

```cpp
U32 Acm_DevUpLoadMapInfo(HAND DeviceHandle, U16 MapType, PDEV_IO_MAP_INFO MapInfoArray, PU32 ArrayLength)
```

#### Acm_DevDownLoadMapInfo
<a name="Acm_DevDownLoadMapInfo" />

```cpp
U32 Acm_DevDownLoadMapInfo(HAND DeviceHandle, U16 MapType, PDEV_IO_MAP_INFO MapInfoArray, U32 ArrayLength)
```

#### Acm_DevSetSlaveStates
<a name="Acm_DevSetSlaveStates" />

```cpp
U32 Acm_DevSetSlaveStates(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 SlvState)
```

#### Acm_DevGetSlaveStates
<a name="Acm_DevGetSlaveStates" />

```cpp
U32 Acm_DevGetSlaveStates(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PU16 SlvState)
```

#### Acm_DevGetSlaveTxPDO
<a name="Acm_DevGetSlaveTxPDO" />

```cpp
U32 Acm_DevGetSlaveTxPDO(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 StartOffset, U16 Length, PU8 DataArray)
```

#### Acm_DevGetSlaveRxPDO
<a name="Acm_DevGetSlaveRxPDO" />

```cpp
U32 Acm_DevGetSlaveRxPDO(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 StartOffset, U16 Length, PU8 DataArray)
```

#### Acm_DevWriteSDOComplete
<a name="Acm_DevWriteSDOComplete" />

```cpp
U32 Acm_DevWriteSDOComplete(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Index, U16 DataSize, PVOID pValue)
```

#### Acm_DevWriteSDOData
<a name="Acm_DevWriteSDOData" />

```cpp
U32 Acm_DevWriteSDOData(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Index, U16 SubIndex, U16 Type, U16 DataSize, PVOID pValue)
```

#### Acm_DevReadSDOData
<a name="Acm_DevReadSDOData" />

```cpp
U32 Acm_DevReadSDOData(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Index, U16 SubIndex, U16 Type, U16 DataSize, PVOID pValue)
```

#### Acm_DevWriteRegData
<a name="Acm_DevWriteRegData" />

```cpp
U32 Acm_DevWriteRegData(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Address, U16 Type, U16 DataSize, PVOID pValue)
```

#### Acm_DevReadRegData
<a name="Acm_DevReadRegData" />

```cpp
U32 Acm_DevReadRegData(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Address, U16 Type, U16 DataSize, PVOID pValue);
```

#### Acm_DevReadEmgMessage
<a name="Acm_DevReadEmgMessage" />

```cpp
U32 Acm_DevReadEmgMessage(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 DataSize, PU8 EmgMessage);
```

#### Acm_DevReadSlvCommErrCnt
<a name="Acm_DevReadSlvCommErrCnt" />

```cpp
U32 Acm_DevReadSlvCommErrCnt(HAND DeviceHandle, U16 RingNo, PU32 ErrCntArray, PU32 ArrayElements)
```

#### Acm_DaqLinkPDO
<a name="Acm_DaqLinkPDO" />

```cpp
U32 Acm_DaqLinkPDO(HAND DeviceHandle, PORT_TYPE Type, U16 Channel, U32 RingNo, U32 SlaveID, U32 EntryIndex, U32 EntrySubIndex);
```

#### Acm_AxMoveTorque
<a name="Acm_AxMoveTorque" />

```cpp
U32 Acm_AxMoveTorque(HAND AxisHandle, F64 Distance, F64 Torque, F64 Velocity, F64 PressTime, U8 Mode)
```

#### Acm_AxGetActTorque
<a name="Acm_AxGetActTorque" />

```cpp
U32 Acm_AxGetActTorque(HAND AxisHandle, PI32 Torque)
```

#### Acm_Ax2DCompensateInAx
<a name="Acm_Ax2DCompensateInAx" />

```cpp
U32 Acm_Ax2DCompensateInAx(HAND AxisHandle, HAND RelAxisHandle, PF64 Coefficient, PF64 RelCoefficient, U32 ArrayElements)
```

#### Acm_Ax1DCompensateTable
<a name="Acm_Ax1DCompensateTable" />

```cpp
U32 Acm_Ax1DCompensateTable (HAND AxisHandle, F64 OriginPos, F64 Pitch, PF64 OffsetData, U32 OffsetElements, U32 Direction)
```

#### Acm_DevZAxisCompensateTable
<a name="Acm_DevZAxisCompensateTable" />

```cpp
U32 Acm_DevZAxisCompensateTable(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, HAND ZAxisHandle, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataZ, U32 OffsetElementsX, U32 OffsetElementsY)
```

#### Acm_Dev2DCompensateTable
<a name="Acm_Dev2DCompensateTable" />

```cpp
U32 Acm_Dev2DCompensateTable(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataX, PF64 OffsetDataY, U32 OffsetElementsX, U32 OffsetElementsY)
```

#### Acm_DevZAxisCompensateTableEx
<a name="Acm_DevZAxisCompensateTableEx" />

```cpp
U32 Acm_DevZAxisCompensateTableEx(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, HAND ZAxisHandle, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataZ, U32 OffsetElementsX, U32 OffsetElementsY, U32 Direction)
```

#### Acm_Dev2DCompensateTableEx
<a name="Acm_Dev2DCompensateTableEx" />

```cpp
U32 Acm_Dev2DCompensateTableEx(HAND DeviceHandle, HAND AxisHandle, HAND RelAxisHandle, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataX, PF64 OffsetDataY, U32 OffsetElementsX, U32 OffsetElementsY, U32 Direction)
```

#### Acm_AxGetCompensatePosition
<a name="Acm_AxGetCompensatePosition" />

```cpp
U32 Acm_AxGetCompensatePosition(HAND AxisHandle, PF64 Position)
```

#### Acm_DevMultiTrigInitial
<a name="Acm_DevMultiTrigInitial" />

```cpp
U32 Acm_DevMultiTrigInitial(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 Enable, U8 PWM, U8 LTC, U8 MPG)
```

#### Acm_EnableOneDevEventCallBack
<a name="Acm_EnableOneDevEventCallBack" />

```cpp
U32 Acm_EnableOneDevEventCallBack(HANDLE DeviceHandle, ULONG EventID)
```

#### Acm_AxGetRawData
<a name="Acm_AxGetRawData" />

```cpp
U32 Acm_AxGetRawData(HAND AxisHandle, U8 index, PF64 RawData)
```

#### Acm_AxSetRawData
<a name="Acm_AxSetRawData" />

```cpp
U32 Acm_AxSetRawData(HAND AxisHandle, U8 index, F64 RawData)
```

#### Acm_AxReturnPausePosition
<a name="Acm_AxReturnPausePosition" />

```cpp
U32 Acm_AxReturnPausePosition(HAND AxHandle)
```

#### Acm_AxAddOnAx
<a name="Acm_AxAddOnAx" />

```cpp
U32 Acm_AxAddOnAx(HAND AxisHandle, HAND MasAxisHandle)
```

#### Acm_AxAddRemove
<a name="Acm_AxAddRemove" />

```cpp
U32 Acm_AxAddRemove(HAND AxisHandle, HAND MasAxisHandle)
```

#### Acm_AxGetAddOnNum
<a name="Acm_AxGetAddOnNum" />

```cpp
U32 Acm_AxGetAddOnNum(HAND AxisHandle, PI32 num)
```

#### Acm_AxSetCompensateDistance
<a name="Acm_AxSetCompensateDistance" />

```cpp
U32 Acm_AxSetCompensateDistance(HAND AxisHandle, F64 Distance)
```

#### Acm_AxGetCompensateDistance
<a name="Acm_AxGetCompensateDistance" />

```cpp
U32 Acm_AxGetCompensateDistance(HAND AxisHandle, PF64 Distance)
```

#### Acm_AxOpen
<a name="Acm_AxOpen" />

```cpp
U32 Acm_AxOpen(HAND DeviceHandle, U16 PhyAxis, PHAND AxisHandle)
```

#### Acm_AxOpenbyID
<a name="Acm_AxOpenbyID" />

```cpp
U32 Acm_AxOpenbyID(HAND DeviceHandle, U16 SlaveID, U8 SubID, PHAND AxisHandle)
```

#### Acm_AxClose
<a name="Acm_AxClose" />

```cpp
U32 Acm_AxClose(PHAND AxisHandle)
```

#### Acm_AxSetSvOn
<a name="Acm_AxSetSvOn" />

```cpp
U32 Acm_AxSetSvOn(HAND AxisHandle, U32 OnOff)
```

#### Acm_AxResetAlm
<a name="Acm_AxResetAlm" />

```cpp
U32 Acm_AxResetAlm(HAND AxisHandle, U32 OnOff)
```

#### Acm_AxMoveRel
<a name="Acm_AxMoveRel  " />

```cpp
U32 Acm_AxMoveRel(HAND AxisHandle, F64 Distance)
```

#### Acm_AxMoveRel_T
<a name="Acm_AxMoveRel_T" />

```cpp
U32 Acm_AxMoveRel_T(HAND AxisHandle, F64 Distance, F64 Time, F64 Factor)
```

#### Acm_AxMoveRel_SD
<a name="Acm_AxMoveRel_SD" />

```cpp
U32 Acm_AxMoveRel_SD(HAND AxisHandle, F64 Distance, F64 SDDistance)
```

#### Acm_AxMoveRel_EC
<a name="Acm_AxMoveRel_EC" />

```cpp
U32 Acm_AxMoveRel_EC(HAND AxisHandle, F64 Position)
```

#### Acm_AxMoveAbs
<a name="Acm_AxMoveAbs" />

```cpp
U32 Acm_AxMoveAbs(HAND AxisHandle, F64 Position)
```

#### Acm_AxMoveAbs_T
<a name="Acm_AxMoveAbs_T" />

```cpp
U32 Acm_AxMoveAbs_T(HAND AxisHandle, F64 Position, F64 Time, F64 Factor)
```

#### Acm_AxMoveAbs_SD
<a name="Acm_AxMoveAbs_SD" />

```cpp
U32 Acm_AxMoveAbs_SD(HAND AxisHandle, F64 Position, F64 SDPosition)
```

#### Acm_AxMoveAbs_EC
<a name="Acm_AxMoveAbs_EC" />

```cpp
U32 Acm_AxMoveAbs_EC(HAND AxisHandle, F64 Position)
```

#### Acm_AxMoveVel
<a name="Acm_AxMoveVel" />

```cpp
U32 Acm_AxMoveVel(HAND AxisHandle, U16 Direction)
```

#### Acm_AxStopDec
<a name="Acm_AxStopDec" />

```cpp
U32 Acm_AxStopDec(HAND AxisHandle)
```

#### Acm_AxStopDecEx
<a name="Acm_AxStopDecEx" />

```cpp
U32 Acm_AxStopDecEx(HAND AxisHandle, F64 NewDec)
```

#### Acm_AxStopEmg
<a name="Acm_AxStopEmg" />

```cpp
U32 Acm_AxStopEmg(HAND AxisHandle)
```

#### Acm_AxMoveImpose
<a name="Acm_AxMoveImpose" />

```cpp
U32 Acm_AxMoveImpose(HAND AxisHandle, F64 Position, F64 NewVel)
```

#### Acm_AxHomeEx
<a name="Acm_AxHomeEx" />

```cpp
U32 Acm_AxHomeEx(HAND AxisHandle, U32 DirMode)
```

#### Acm_AxHome
<a name="Acm_AxHome" />

```cpp
U32 Acm_AxHome(HAND AxisHandle, U32 HomeMode, U32 DirMode)
```

#### Acm_AxMoveHome
<a name="Acm_AxMoveHome" />

```cpp
U32 Acm_AxMoveHome(HAND AxisHandle, U32 HomeMode, U32 Dir)
```

#### Acm_AxMoveGantryHome
<a name="Acm_AxMoveGantryHome" />

```cpp
U32 Acm_AxMoveGantryHome(HAND AxisHandle, U32 HomeMode, U32 Dir)
```

#### Acm_AxChangeVel
<a name="Acm_AxChangeVel" />

```cpp
U32 Acm_AxChangeVel(HAND AxisHandle, F64 NewVel)
```

#### Acm_AxChangePos
<a name="Acm_AxChangePos" />

```cpp
U32 Acm_AxChangePos(HAND AxisHandle, F64 NewPos)
```

#### Acm_AxChangeVelByRate
<a name="Acm_AxChangeVelByRate" />

```cpp
U32 Acm_AxChangeVelByRate(HAND AxisHandle, U32 Rate)
```

#### Acm_AxChangeVelExByRate
<a name="Acm_AxChangeVelExByRate" />

```cpp
U32 Acm_AxChangeVelExByRate(HAND AxisHandle, U32 Rate, F64 NewAcc, F64 NewDec);
```

#### Acm_AxResetError
<a name="Acm_AxResetError" />

```cpp
U32 Acm_AxResetError(HAND AxisHandle)
```

#### Acm_AxGetState
<a name="Acm_AxGetState" />

```cpp
U32 Acm_AxGetState(HAND AxisHandle, PU16 State)
```

#### Acm_AxGetMotionIO
<a name="Acm_AxGetMotionIO" />

```cpp
U32 Acm_AxGetMotionIO(HAND AxisHandle, PU32 Status)
```

#### Acm_AxGetMotionStatus
<a name="Acm_AxGetMotionStatus" />

```cpp
U32 Acm_AxGetMotionStatus(HAND AxisHandle, PU32 Status)
```

#### Acm_AxGetCmdPosition
<a name="Acm_AxGetCmdPosition" />

```cpp
U32 Acm_AxGetCmdPosition(HAND AxisHandle, PF64 Position)
```

#### Acm_AxGetMachPosition
<a name="Acm_AxGetMachPosition" />

```cpp
U32 Acm_AxGetMachPosition(HAND AxisHandle, PF64 Position)
```

#### Acm_AxSetCmdPosition
<a name="Acm_AxSetCmdPosition" />

```cpp
U32 Acm_AxSetCmdPosition(HAND AxisHandle, F64 Position)
```

#### Acm_AxGetActualPosition
<a name="Acm_AxGetActualPosition" />

```cpp
U32 Acm_AxGetActualPosition(HAND AxisHandle, PF64 Position)
```

#### Acm_AxSetActualPosition
<a name="Acm_AxSetActualPosition" />

```cpp
U32 Acm_AxSetActualPosition(HAND AxisHandle, F64 Position)
```

#### Acm_AxGetCmdVelocity
<a name="Acm_AxGetCmdVelocity" />

```cpp
U32 Acm_AxGetCmdVelocity(HAND AxisHandle, PF64 Velocity)
```

#### Acm_AxGetActVelocity
<a name="Acm_AxGetActVelocity" />

```cpp
U32 Acm_AxGetActVelocity(HAND AxisHandle, PF64 Velocity)
```

#### Acm_AxGetLagCounter
<a name="Acm_AxGetLagCounter" />

```cpp
U32 Acm_AxGetLagCounter(HAND AxisHandle, PF64 Position)
```

#### Acm_AxSetExtDrive
<a name="Acm_AxSetExtDrive" />

```cpp
U32 Acm_AxSetExtDrive(HAND AxisHandle, U16 ExtDrvMode)
```

#### Acm_AxDoSetBit
<a name="Acm_AxDoSetBit" />

```cpp
U32 Acm_AxDoSetBit(HAND AxisHandle, U16	DoChannel, U8 BitData)
```

#### Acm_AxDiSetBit
<a name="Acm_AxDiSetBit" />

```cpp
U32 Acm_AxDiSetBit(HAND AxisHandle, U16	DiChannel, U8 BitData)
```

#### Acm_AxDoGetBit
<a name="Acm_AxDoGetBit" />

```cpp
U32 Acm_AxDoGetBit(HAND AxisHandle, U16	DoChannel, PU8 BitData)
```

#### Acm_AxDiGetBit
<a name="Acm_AxDiGetBit" />

```cpp
U32 Acm_AxDiGetBit(HAND AxisHandle, U16	DiChannel, PU8 BitData)
```

#### Acm_AxDoSetByte
<a name="Acm_AxDoSetByte" />

```cpp
U32 Acm_AxDoSetByte(HAND AxisHandle, U16 DoPort, U8 ByteData)
```

#### Acm_AxDoGetByte
<a name="Acm_AxDoGetByte" />

```cpp
U32 Acm_AxDoGetByte(HAND AxisHandle, U16 DoPort, PU8 ByteData)
```

#### Acm_AxDiGetByte
<a name="Acm_AxDiGetByte" />

```cpp
U32 Acm_AxDiGetByte(HAND AxisHandle, U16 DiPort, PU8 ByteData)
```

#### Acm_AxSimStartSuspendVel
<a name="Acm_AxSimStartSuspendVel" />

```cpp
U32 Acm_AxSimStartSuspendVel(HAND AxisHandle, U16 DriDir)
```

#### Acm_AxSimStartSuspendRel
<a name="Acm_AxSimStartSuspendRel" />

```cpp
U32 Acm_AxSimStartSuspendRel(HAND AxisHandle,F64 Distance)
```

#### Acm_AxSimStartSuspendAbs
<a name="Acm_AxSimStartSuspendAbs" />

```cpp
U32 Acm_AxSimStartSuspendAbs(HAND AxisHandle,F64 EndPoint)
```

#### Acm_AxSimStart
<a name="Acm_AxSimStart" />

```cpp
U32 Acm_AxSimStart(HAND AxisHandle)
```

#### Acm_AxSimStop
<a name="Acm_AxSimStop" />

```cpp
U32 Acm_AxSimStop(HAND AxisHandle)
```

#### Acm_AxGetLatchData
<a name="Acm_AxGetLatchData" />

```cpp
U32 Acm_AxGetLatchData(HAND AxisHandle, U32 PositionNo, PF64 Position)
```

#### Acm_AxStartSoftLatch
<a name="Acm_AxStartSoftLatch" />

```cpp
U32 Acm_AxStartSoftLatch(U32 AxisHandle)
```

#### Acm_AxResetLatch
<a name="Acm_AxResetLatch" />

```cpp
U32 Acm_AxResetLatch(HAND AxisHandle)
```

#### Acm_AxGetLatchFlag
<a name="Acm_AxGetLatchFlag" />

```cpp
U32 Acm_AxGetLatchFlag(HAND AxisHandle, PU8 LatchFlag)
```

#### Acm_AxTriggerLatch
<a name="Acm_AxTriggerLatch" />

```cpp
U32 Acm_AxTriggerLatch(HAND AxisHandle)
```

#### Acm_AxReadLatchBuffer
<a name="Acm_AxReadLatchBuffer" />

```cpp
U32 Acm_AxReadLatchBuffer(HAND AxisHandle, PF64 LatchDataArray, PU32 DataCnt)
```

#### Acm_AxResetLatchBuffer
<a name="Acm_AxResetLatchBuffer" />

```cpp
U32 Acm_AxResetLatchBuffer(HAND AxisHandle)
```

#### Acm_AxGetLatchBufferStatus
<a name="Acm_AxGetLatchBufferStatus" />

```cpp
U32 Acm_AxGetLatchBufferStatus(HAND AxisHandle, PU32 RemainCnt, PU32 SpaceCnt)
```

#### Acm_AxGearInAx
<a name="Acm_AxGearInAx" />

```cpp
U32 Acm_AxGearInAx(HAND AxisHandle, HAND MasAxisHandle, I32 Numerator, I32 Denominator, U32 RefSrc, U32 Absolute)
```

#### Acm_AxTangentInGp
<a name="Acm_AxTangentInGp" />

```cpp
U32 Acm_AxTangentInGp(HAND AxisHandle, HAND MasGroupHandle, PI16 StartVectorArray, U8 Working_plane, I16 Direction)
```

#### Acm_AxGantryInAx
<a name="Acm_AxGantryInAx" />

```cpp
U32	Acm_AxGantryInAx(HAND AxisHandle, HAND MasAxisHandle, I16 RefMasterSrc, I16 direction)
```

#### Acm_AxPhaseAx
<a name="Acm_AxPhaseAx" />

```cpp
U32 Acm_AxPhaseAx(HAND AxisHandle, F64 Acc, F64 Dec, F64 PhaseSpeed, F64 PhaseDist)
```

#### Acm_AxSetChannelCmpSetting
<a name="Acm_AxSetChannelCmpSetting" />

```cpp
U32 Acm_AxSetChannelCmpSetting(HAND AxisHandle, U16 ChannelID, U32 CmpSrc, U32 CmpMethod, U32 CmpPulseMode, U32 CmpPulseWidth)
```

#### Acm_AxGetChannelCmpSetting
<a name="Acm_AxGetChannelCmpSetting" />

```cpp
U32 Acm_AxGetChannelCmpSetting(HAND AxisHandle, U16 ChannelID, PU32 CmpSrc, PU32 CmpMethod, PU32 CmpPulseMode, PU32 CmpPulseWidth)
```

#### Acm_AxResetChannelCmp
<a name="Acm_AxResetChannelCmp" />

```cpp
U32 Acm_AxResetChannelCmp(HAND AxisHandle, U16 ChannelID)
```

#### Acm_AxAddChannelCmpDatas
<a name="Acm_AxAddChannelCmpDatas" />

```cpp
U32 Acm_AxAddChannelCmpDatas(HAND AxisHandle, U16 ChannelID, PF64 TableArray, U32 ArrayCount)
```

#### Acm_AxGetChannelCmpData
<a name="Acm_AxGetChannelCmpData" />

```cpp
U32 Acm_AxGetChannelCmpData(HAND AxisHandle, U16 ChannelID, PF64 CmpData)
```

#### Acm_AxLoadChannelNextData
<a name="Acm_AxLoadChannelNextData" />

```cpp
U32 Acm_AxLoadChannelNextData(HAND AxisHandle, U16 ChannelID)
```

#### Acm_AxGetCmpbufferRemainCount
<a name="Acm_AxGetCmpbufferRemainCount" />

```cpp
U32 Acm_AxGetCmpbufferRemainCount(HAND AxisHandle, U16 ChannelID,PU32 DataCount)
```

#### Acm_AxSetCmpAuto
<a name="Acm_AxSetCmpAuto" />

```cpp
U32 Acm_AxSetCmpAuto(HAND AxisHandle, F64 Start, F64 End, F64 Interval)
```

#### Acm_AxGetCmpData
<a name="Acm_AxGetCmpData" />

```cpp
U32 Acm_AxGetCmpData(HAND AxisHandle, PF64 CmpPosition)
```

#### Acm_AxSetCmpData
<a name="Acm_AxSetCmpData" />

```cpp
U32 Acm_AxSetCmpData(HAND AxisHandle, F64 CmpPosition)
```

#### Acm_AxChangeCmpIndex
<a name="Acm_AxChangeCmpIndex" />

```cpp
U32 Acm_AxChangeCmpIndex(HAND AxisHandle, U32 CmpIndex)
```

#### Acm_AxSetCmpBufferData
<a name="Acm_AxSetCmpBufferData" />

```cpp
U32 Acm_AxSetCmpBufferData(HAND AxisHandle, PF64 TableArray, I32 ArrayCount)
```

#### Acm_AxResetCmpData
<a name="Acm_AxResetCmpData" />

```cpp
U32 Acm_AxResetCmpData(HAND AxisHandle)
```

#### Acm_AxGetCmpBufferStatus
<a name="Acm_AxGetCmpBufferStatus" />

```cpp
U32 Acm_AxGetCmpBufferStatus(HAND AxisHandle, PU32 CurIndex, PU32 RemainCnt, PU32 SpaceCnt)
```

#### Acm_AxResetMPGOffset
<a name="Acm_AxResetMPGOffset" />

```cpp
U32 Acm_AxResetMPGOffset(HAND AxisHandle)
```

#### Acm_AxMovePTPBufferRel
<a name="Acm_AxMovePTPBufferRel" />

```cpp
U32 Acm_AxMovePTPBufferRel(HAND AxisHandle, U16 MotionMode, PF64 PositionArray, PF64 FLArray, PF64 FHArray, PU16 TSArray, U32 ArrayLength)
```

#### Acm_AxMovePTPBufferAbs
<a name="Acm_AxMovePTPBufferAbs" />

```cpp
U32 Acm_AxMovePTPBufferAbs(HAND AxisHandle, U16 MotionMode, PF64 PositionArray, PF64 FLArray, PF64 FHArray, PU16 TSArray, U32 ArrayLength)
```

#### Acm_AxEnableCompensation
<a name="Acm_AxEnableCompensation" />

```cpp
U32 Acm_AxEnableCompensation(HAND AxisHandle,F64 ZStartPos)
```

#### Acm_AxGetCompensationValue
<a name="Acm_AxGetCompensationValue" />

```cpp
U32 Acm_AxGetCompensationValue(HAND AxisHandle, F64 XData, F64 YData, PF64 PCompensationValue)
```

#### Acm_AxSetCompenPara
<a name="Acm_AxSetCompenPara" />

```cpp
U32 Acm_AxSetCompenPara(HAND AxisHandle, HAND GroupHandle, U32 XScanDataCnt, U32 YScanDataCnt, U32 CompMode)
```

#### Acm_AxDIStartMoveAbs
<a name="Acm_AxDIStartMoveAbs" />

```cpp
U32 Acm_AxDIStartMoveAbs(HAND AxisHandle, U16 DIChannel, F64 Position)
```

#### Acm_AxDIStartMoveRel
<a name="Acm_AxDIStartMoveRel" />

```cpp
U32 Acm_AxDIStartMoveRel(HAND AxisHandle, U16 DIChannel, F64 Distance)
```

#### Acm_AxDIStartMoveVel
<a name="Acm_AxDIStartMoveVel" />

```cpp
U32 Acm_AxDIStartMoveVel(HAND AxisHandle, U16 DIChannel, U16 Direction)
```

#### Acm_AxDisableDIStart
<a name="Acm_AxDisableDIStart" />

```cpp
U32 Acm_AxDisableDIStart(HAND AxisHandle)
```

#### Acm_AxSetPWMTableOnTime
<a name="Acm_AxSetPWMTableOnTime" />

```cpp
U32 Acm_AxSetPWMTableOnTime(HAND AxisHandle, PU32 TimeTableArray, I32 ArrayCount)
```

#### Acm_AxGetINxStopStatus
<a name="Acm_AxGetINxStopStatus" />

```cpp
U32 Acm_AxGetINxStopStatus(HAND AxisHandle,PU32 Stop_Flag)
```

#### Acm_AxResetINxStopStatus
<a name="Acm_AxResetINxStopStatus" />

```cpp
U32 Acm_AxResetINxStopStatus(HAND AxisHandle)
```

#### Acm_AxJog
<a name="Acm_AxJog" />

```cpp
U32 Acm_AxJog(HAND AxisHandle,U16 Direction)
```

#### Acm_AxSetCmpDO
<a name="Acm_AxSetCmpDO" />

```cpp
U32 Acm_AxSetCmpDO(HAND AxisHandle,U32 OFForON)
```

#### Acm_AxDownloadTorqueTable
<a name="Acm_AxDownloadTorqueTable" />

```cpp
U32 Acm_AxDownloadTorqueTable(HAND AxisHandle, PF64 PositionArray, PF64 TorqueArray, U32 ArrayElements)
```

#### Acm_AxLoadTorqueTableFile
<a name="Acm_AxLoadTorqueTableFile" />

```cpp
U32 Acm_AxLoadTorqueTableFile(HAND AxisHandle, PI8 FilePath, PU32 PointsCount)
```

#### Acm_AxResetPVTTable
<a name="Acm_AxResetPVTTable" />

```cpp
U32 Acm_AxResetPVTTable(HAND AxisHandle)
```

#### Acm_AxLoadPVTTable
<a name="Acm_AxLoadPVTTable" />

```cpp
U32 Acm_AxLoadPVTTable(HAND AxisHandle, PF64 Position, PF64 Velocity, PF64 Time, U32 ArrayElements)
```

#### Acm_AxCalculatePVTTableContinuous
<a name="Acm_AxCalculatePVTTableContinuous" />

```cpp
U32 Acm_AxCalculatePVTTableContinuous(HAND AxisHandle, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, U32 ArrayElements, PF64 Time)
```

#### Acm_AxLoadPVTTableContinuous
<a name="Acm_AxLoadPVTTableContinuous" />

```cpp
U32 Acm_AxLoadPVTTableContinuous(HAND AxisHandle, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, F64 TimeDelay, U32 ArrayElements)
```

#### Acm_AxStartPVT
<a name="Acm_AxStartPVT" />

```cpp
U32 Acm_AxStartPVT(HAND AxisHandle, U8 Repeat)
```

#### Acm_AxStartAllPVT
<a name="Acm_AxStartAllPVT" />

```cpp
U32 Acm_AxStartAllPVT(PHAND AxisHandle, U8 Repeat, U32 ArrayElements)
```

#### Acm_AxCheckPTBuffer
<a name="Acm_AxCheckPTBuffer" />

```cpp
U32 Acm_AxCheckPTBuffer(HAND AxisHandle, PU16 Freespace)
```

#### Acm_AxAddPTData
<a name="Acm_AxAddPTData" />

```cpp
U32 Acm_AxAddPTData(HAND AxisHandle, F64 Position, F64 Time)
```

#### Acm_AxStartPT
<a name="Acm_AxStartPT" />

```cpp
U32 Acm_AxStartPT(HAND AxisHandle, U8 Repeat)
```

#### Acm_AxStartAllPT
<a name="Acm_AxStartAllPT" />

```cpp
U32 Acm_AxStartAllPT(PHAND AxisHandle, U8 Repeat, U32 ArrayElements)
```

#### Acm_AxResetPTData
<a name="Acm_AxResetPTData" />

```cpp
U32 Acm_AxResetPTData(HAND AxisHandle)
```

#### Acm_AxAddPVAData
<a name="Acm_AxAddPVAData" />

```cpp
U32 Acm_AxAddPVAData(HAND AxisHandle, F64 Position, PF64 VelArray, PF64 AccArray, PF64 DecArray, U32 ArrayElements)
```

#### Acm_GpOpen
<a name="Acm_GpOpen" />

```cpp
U32 Acm_GpOpen(HAND DevHandle,PHAND GpHandle,USHORT GpID)
```

#### Acm_GpAddAxis
<a name="Acm_GpAddAxis" />

```cpp
U32 Acm_GpAddAxis(PHAND GpHandle,HAND AxHandle)
```

#### Acm_GpRemAxis
<a name="Acm_GpRemAxis" />

```cpp
U32 Acm_GpRemAxis(HAND GroupHandle, HAND AxisHandle)
```

#### Acm_GpClose
<a name="Acm_GpClose" />

```cpp
U32 Acm_GpClose(PHAND GroupHandle)
```

#### Acm_GpGetState
<a name="Acm_GpGetState" />

```cpp
U32 Acm_GpGetState(HAND GroupHandle, PU16 State)
```

#### Acm_GpResetError
<a name="Acm_GpResetError" />

```cpp
U32 Acm_GpResetError(HAND GroupHandle)
```

#### Acm_GpIpoMask
<a name="Acm_GpIpoMask" />

```cpp
U32 Acm_GpIpoMask(HAND GroupHandle, HAND AxHandle, U32 Mask)
```

#### Acm_GpMoveLinearRel
<a name="Acm_GpMoveLinearRel" />

```cpp
U32 Acm_GpMoveLinearRel(HAND GroupHandle, PF64 DistanceArray, PU32 ArrayElements)
```

#### Acm_GpMoveLinearAbs
<a name="Acm_GpMoveLinearAbs" />

```cpp
U32 Acm_GpMoveLinearAbs(HAND GroupHandle, PF64 PositionArray, PU32 ArrayElements)
```

#### Acm_GpMoveDirectRel
<a name="Acm_GpMoveDirectRel" />

```cpp
U32 Acm_GpMoveDirectRel(HAND GroupHandle, PF64 DistanceArray, PU32 ArrayElements)
```

#### Acm_GpMoveDirectAbs
<a name="Acm_GpMoveDirectAbs" />

```cpp
U32 Acm_GpMoveDirectAbs(HAND GroupHandle, PF64 PositionArray, PU32 ArrayElements)
```

#### Acm_GpMoveCircularRel
<a name="Acm_GpMoveCircularRel" />

```cpp
U32 Acm_GpMoveCircularRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 ArrayElements, I16 Direction)
```

#### Acm_GpMoveCircularAbs
<a name="Acm_GpMoveCircularAbs" />

```cpp
U32 Acm_GpMoveCircularAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 ArrayElements, I16 Direction)
```

#### Acm_GpMoveCircularRel_3P
<a name="Acm_GpMoveCircularRel_3P" />

```cpp
U32 Acm_GpMoveCircularRel_3P(HAND GroupHandle, PF64	RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)

```

#### Acm_GpMoveCircularAbs_3P
<a name="Acm_GpMoveCircularAbs_3P" />

```cpp
U32 Acm_GpMoveCircularAbs_3P(HAND GroupHandle, PF64	RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveCircularRel_Angle
<a name="Acm_GpMoveCircularRel_Angle" />

```cpp
U32 Acm_GpMoveCircularRel_Angle(HAND GroupHandle, PF64 CenterArray, U16 Degree, PU32 ArrayElements, I16 Direction)

```

#### Acm_GpMoveCircularAbs_Angle
<a name="Acm_GpMoveCircularAbs_Angle" />

```cpp
U32 Acm_GpMoveCircularAbs_Angle(HAND GroupHandle, PF64 CenterArray, U16 Degree, PU32 ArrayElements, I16 Direction)
```

#### Acm_GpMoveArcRel_Angle
<a name="Acm_GpMoveArcRel_Angle" />

```cpp
U32 Acm_GpMoveArcRel_Angle(HAND GroupHandle, PF64 CenterArray, F64 Degree, PU32 ArrayElements, I16 Direction)
```

#### Acm_GpMoveArcAbs_Angle
<a name="Acm_GpMoveArcAbs_Angle" />

```cpp
U32 Acm_GpMoveArcAbs_Angle(HAND GroupHandle, PF64 CenterArray, F64 Degree, PU32 ArrayElements, I16 Direction)
```

#### Acm_GpMove3DArcAbs
<a name="Acm_GpMove3DArcAbs" />

```cpp
U32 Acm_GpMove3DArcAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMove3DArcRel
<a name="Acm_GpMove3DArcRel" />

```cpp
U32 Acm_GpMove3DArcRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)

```

#### Acm_GpMove3DArcAbs_V
<a name="Acm_GpMove3DArcAbs_V" />

```cpp
U32 Acm_GpMove3DArcAbs_V(HAND GroupHandle, PF64 CenterArray, PF64 NVectorArray, F64 Degree, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMove3DArcRel_V
<a name="Acm_GpMove3DArcRel_V" />

```cpp
U32 Acm_GpMove3DArcRel_V(HAND GroupHandle, PF64 CenterArray, PF64 NVectorArray, F64 Degree, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMove3DArcAbs_3P
<a name="Acm_GpMove3DArcAbs_3P" />

```cpp
U32 Acm_GpMove3DArcAbs_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, U16 cycCount)
```

#### Acm_GpMove3DArcRel_3P
<a name="Acm_GpMove3DArcRel_3P" />

```cpp
U32 Acm_GpMove3DArcRel_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, U16 cycCount)
```

#### Acm_GpMove3DArcAbs_3PAngle
<a name="Acm_GpMove3DArcAbs_3PAngle" />

```cpp
U32 Acm_GpMove3DArcAbs_3PAngle(HAND GroupHandle, PF64 RefPoint_1, PF64 RefPoint_2, PU32 pArrayElements, I16 Direction, F64 Degree)
```

#### Acm_GpMove3DArcRel_3PAngle
<a name="Acm_GpMove3DArcRel_3PAngle" />

```cpp
U32 Acm_GpMove3DArcRel_3PAngle(HAND GroupHandle, PF64 RefPoint_1, PF64 RefPoint_2, PU32 pArrayElements, I16 Direction, F64 Degree)

```

#### Acm_GpMoveHelixAbs
<a name="Acm_GpMoveHelixAbs" />

```cpp
U32 Acm_GpMoveHelixAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveHelixRel
<a name="Acm_GpMoveHelixRel" />

```cpp
U32 Acm_GpMoveHelixRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)

```

#### Acm_GpMoveHelixAbs_3P
<a name="Acm_GpMoveHelixAbs_3P" />

```cpp
U32 Acm_GpMoveHelixAbs_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMove3DArcRel_3PAngle
<a name="Acm_GpMove3DArcRel_3PAngle" />

```cpp
U32 Acm_GpMove3DArcRel_3PAngle(HAND GroupHandle, PF64 RefPoint_1, PF64 RefPoint_2, PU32 pArrayElements, I16 Direction, F64 Degree)
```

#### Acm_GpMoveHelixAbs
<a name="Acm_GpMoveHelixAbs" />

```cpp
U32 Acm_GpMoveHelixAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveHelixRel
<a name="Acm_GpMoveHelixRel" />

```cpp
U32 Acm_GpMoveHelixRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveHelixAbs_3P
<a name="Acm_GpMoveHelixAbs_3P" />

```cpp
U32 Acm_GpMoveHelixAbs_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveHelixRel_3P
<a name="Acm_GpMoveHelixRel_3P" />

```cpp
U32 Acm_GpMoveHelixRel_3P(HAND GroupHandle, PF64 RefArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveHelixRel_Angle
<a name="Acm_GpMoveHelixRel_Angle" />

```cpp
U32 Acm_GpMoveHelixRel_Angle(HAND GroupHandle, PF64	CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveHelixAbs_Angle
<a name="Acm_GpMoveHelixAbs_Angle" />

```cpp
U32 Acm_GpMoveHelixAbs_Angle(HAND GroupHandle, PF64	CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction)
```

#### Acm_GpMoveEllipticalRel
<a name="Acm_GpMoveEllipticalRel" />

```cpp
U32 Acm_GpMoveEllipticalRel(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, F64 RatioSemiAxes)
```

#### Acm_GpMoveEllipticalAbs
<a name="Acm_GpMoveEllipticalAbs" />

```cpp
U32 Acm_GpMoveEllipticalAbs(HAND GroupHandle, PF64 CenterArray, PF64 EndArray, PU32 pArrayElements, I16 Direction, F64 RatioSemiAxes)
```

#### Acm_GpLoadPath
<a name="Acm_GpLoadPath" />

```cpp
U32 Acm_GpLoadPath(HAND GroupHandle, PI8 FilePath, PHAND PathHandle, PU32 pTotalCount)
```

#### Acm_GpUnloadPath
<a name="Acm_GpUnloadPath" />

```cpp
U32 Acm_GpUnloadPath(HAND GroupHandle, PHAND PathHandle)
```

#### Acm_GpMovePath
<a name="Acm_GpMovePath" />

```cpp
U32 Acm_GpMovePath(HAND GroupHandle, HAND PathHandle)
```

#### Acm_GpMoveAllPath
<a name="Acm_GpMoveAllPath" />

```cpp
U32 Acm_GpMoveAllPath(PHAND GroupHandle, U32 ArrayElements)
```

#### Acm_GpAddPath
<a name="Acm_GpAddPath" />

```cpp
U32 Acm_GpAddPath(HAND GroupHandle, U16 MoveCmd, U16 MoveMode, F64 FH, F64 FL, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)
```

#### Acm_GpAddPath2
<a name="Acm_GpAddPath2" />

```cpp
U32 Acm_GpAddPath2(HAND GroupHandle, U16 MoveCmd, U16 MoveMode, F64 FH, F64 FL, F64 ACC, F64 DEC, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)
```

#### Acm_GpLookAheadPath
<a name="Acm_GpLookAheadPath" />

```cpp
U32 Acm_GpLookAheadPath(HAND GroupHandle, U16 BufferSize, PI8 OutputFile)
```

#### Acm_GpResetPath
<a name="Acm_GpResetPath" />

```cpp
U32 Acm_GpResetPath (PHAND GroupHandle)
```

#### Acm_GpGetPathStatus
<a name="Acm_GpGetPathStatus" />

```cpp
U32 Acm_GpGetPathStatus(HAND GroupHandle, PU32 pCurIndex, PU32 pCurCmdFunc, PU32 pRemainCount, PU32 pFreeSpaceCount)
```

#### Acm_GpMoveSelPath
<a name="Acm_GpMoveSelPath" />

```cpp
U32 Acm_GpMoveSelPath(HAND GroupHandle, HAND PathHandle, U32 StartIndex, U32 EndIndex, U8 Repeat)
```

#### Acm_GpGetPathIndexStatus
<a name="Acm_GpGetPathIndexStatus" />

```cpp
U32 Acm_GpGetPathIndexStatus(HAND GroupHandle, U32 Index, PU16 CmdFunc, PU16 MoveMode, PF64 FH, PF64 FL, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements);

```

#### Acm_GpAddBSplinePath
<a name="Acm_GpAddBSplinePath" />

```cpp
U32 Acm_GpAddBSplinePath(HAND GroupHandle, F64 FH, F64 FL, F64 *CtrlP0List, F64 *CtrlP1List, U32 CtrlPCount, F64 *NodeList, U32 NodeCount, U32 Degree, U32 CutPointCount)
```

#### Acm_GpAddCSplinePath
<a name="Acm_GpAddCSplinePath" />

```cpp
U32 Acm_GpAddCSplinePath(HAND GroupHandle, F64 FH, F64 FL, F64 *CtrlP0List, F64 *CtrlP1List, F64 *Tightness, U32 CtrlPCount, U32 CutPointCount)

```

#### Acm_GpResumeMotion
<a name="Acm_GpResumeMotion" />

```cpp
U32 Acm_GpResumeMotion(HAND GroupHandle)
```

#### Acm_GpPauseMotion
<a name="Acm_GpPauseMotion" />

```cpp
U32 Acm_GpPauseMotion(HAND GroupHandle)
```

#### Acm_GpStopDec
<a name="Acm_GpStopDec" />

```cpp
U32 Acm_GpStopDec(HAND GroupHandle)
```

#### Acm_GpStopDecEx
<a name="Acm_GpStopDecEx" />

```cpp
U32 Acm_GpStopDecEx(HAND GroupHandle, F64 NewDec)
```

#### Acm_GpStopEmg
<a name="Acm_GpStopEmg" />

```cpp
U32 Acm_GpStopEmg(HAND GroupHandle)
```

#### Acm_GpChangeVel
<a name="Acm_GpChangeVel" />

```cpp
U32 Acm_GpChangeVel(HAND GroupHandle, F64 NewVelocity)
```

#### Acm_GpChangeVelByRate
<a name="Acm_GpChangeVelByRate" />

```cpp
U32 Acm_GpChangeVelByRate(HAND GroupHandle, U32 Rate)
```

#### Acm_GpGetCmdVel
<a name="Acm_GpGetCmdVel" />

```cpp
U32 Acm_GpGetCmdVel(HAND GroupHandle, PF64 CmdVel)
```

#### Acm_GpGetINxStopStatus
<a name="Acm_GpGetINxStopStatus" />

```cpp
U32 Acm_GpGetINxStopStatus(HAND GroupHandle,PU32 Stop_Flag)
```

#### Acm_GpResetINxStopStatus
<a name="Acm_GpResetINxStopStatus" />

```cpp
U32 Acm_GpResetINxStopStatus(HAND GroupHandle)
```

#### Acm_GpGetPausePosition
<a name="Acm_GpGetPausePosition" />

```cpp
U32 Acm_GpGetPausePosition(HAND GroupHandle, PF64 RefPausePosition)
```

#### Acm_GpSetRawData
<a name="Acm_GpSetRawData" />

```cpp
U32 Acm_GpSetRawData(HAND GroupHandle, U8 index, F64 RawData)
```

#### Acm_GpGetRawData
<a name="Acm_GpGetRawData" />

```cpp
U32 Acm_GpGetRawData(HAND GroupHandle, U8 index, PF64 RawData)
```

#### Acm_DaqDiGetByte
<a name="Acm_DaqDiGetByte" />

```cpp
U32 Acm_DaqDiGetByte(HAND DeviceHandle, U16 DiPort, PU8 ByteData)
```

#### Acm_DaqDiGetBit
<a name="Acm_DaqDiGetBit" />

```cpp
U32 Acm_DaqDiGetBit(HAND DeviceHandle, U16 DiChannel, PU8 BitData)
```

#### Acm_DaqDoSetByte
<a name="Acm_DaqDoSetByte" />

```cpp
U32 Acm_DaqDoSetByte(HAND DeviceHandle, U16 DoPort, U8	ByteData)
```

#### Acm_DaqDoSetBit
<a name="Acm_DaqDoSetBit" />

```cpp
U32 Acm_DaqDoSetBit(HAND DeviceHandle, U16 DoChannel, U8 BitData)
```

#### Acm_DaqDiSetBit
<a name="Acm_DaqDiSetBit" />

```cpp
U32 Acm_DaqDiSetBit(HAND DeviceHandle, U16 DiChannel, U8 BitData)
```

#### Acm_DaqDoGetByte
<a name="Acm_DaqDoGetByte" />

```cpp
U32 Acm_DaqDoGetByte(HAND DeviceHandle, U16 DoPort, PU8 ByteData)
```

#### Acm_DaqDoGetBit
<a name="Acm_DaqDoGetBit" />

```cpp
U32 Acm_DaqDoGetBit(HAND DeviceHandle, U16 DoChannel, PU8 BitData)
```

#### Acm_DaqDiGetBytes
<a name="Acm_DaqDiGetBytes" />

```cpp
U32 Acm_DaqDiGetBytes(HAND DeviceHandle, U16 StartPort, U16 NumPort, PU8 ByteDataArray)
```

#### Acm_DaqDoSetBytes
<a name="Acm_DaqDoSetBytes" />

```cpp
U32 Acm_DaqDoSetBytes(HAND DeviceHandle, U16 StartPort, U16 NumPort, PU8 ByteDataArray)
```

#### Acm_DaqDoGetBytes
<a name="Acm_DaqDoGetBytes" />

```cpp
U32 Acm_DaqDoGetBytes(HAND DeviceHandle, U16 StartPort, U16 NumPort, PU8 ByteDataArray)
```

#### Acm_DaqDiGetByteEx
<a name="Acm_DaqDiGetByteEx" />

```cpp
U32 Acm_DaqDiGetByteEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 DiPort, PU8 ByteData)
```

#### Acm_DaqDoSetByteEx
<a name="Acm_DaqDoSetByteEx" />

```cpp
U32 Acm_DaqDoSetByteEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 DoPort, U8 ByteData)
```

#### Acm_DaqDoGetByteEx
<a name="Acm_DaqDoGetByteEx" />

```cpp
U32 Acm_DaqDoGetByteEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 DoPort, PU8 ByteData)
```

#### Acm_DaqDoGetBitEx
<a name="Acm_DaqDoGetBitEx" />

```cpp
U32 Acm_DaqDoGetBitEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 DoChannel, PU8 BitData)
```

#### Acm_DaqAiGetRawData
<a name="Acm_DaqAiGetRawData" />

```cpp
U32 Acm_DaqAiGetRawData(HAND DeviceHandle, U16 AiChannel, PU16 AiData)
```

#### Acm_DaqAiGetEngData
<a name="Acm_DaqAiGetEngData" />

```cpp
U32 Acm_DaqAiGetEngData(HAND DeviceHandle, U16 AiChannel, PF32 AiData)
```

#### Acm_DaqAiGetVoltData
<a name="Acm_DaqAiGetVoltData" />

```cpp
U32 Acm_DaqAiGetVoltData(HAND DeviceHandle, U16	AiChannel, PF32	AiData)
```

#### Acm_DaqAiGetCurrData
<a name="Acm_DaqAiGetCurrData" />

```cpp
U32 Acm_DaqAiGetCurrData(HAND DeviceHandle, U16	AiChannel, PF32	AiData)
```

#### Acm_DaqAiZeroCalibration
<a name="Acm_DaqAiZeroCalibration" />

```cpp
U32 Acm_DaqAiZeroCalibration(HAND DeviceHandle, U16	AiChannel)
```

#### Acm_DaqAiSpanCalibration
<a name="Acm_DaqAiSpanCalibration" />

```cpp
U32 Acm_DaqAiSpanCalibration(HAND DeviceHandle, U16	AiChannel)
```

#### Acm_DaqAiGetChannelStatus
<a name="Acm_DaqAiGetChannelStatus" />

```cpp
U32 Acm_DaqAiGetChannelStatus(HAND DeviceHandle, U16 AiChannel, PU32 ChanStatus)
```

#### Acm_DaqAoSetRawData
<a name="Acm_DaqAoSetRawData" />

```cpp
U32 Acm_DaqAoSetRawData(HAND DeviceHandle, U16 AoChannel, U16 AoData)
```

#### Acm_DaqAoSetEngData
<a name="Acm_DaqAoSetEngData" />

```cpp
U32 Acm_DaqAoSetEngData(HAND DeviceHandle, U16 AoChannel, F32 AoData)
```

#### Acm_DaqAoSetVoltData
<a name="Acm_DaqAoSetVoltData" />

```cpp
U32 Acm_DaqAoSetVoltData(HAND DeviceHandle, U16	AoChannel, F32 AoData)
```

#### Acm_DaqAoSetCurrData
<a name="Acm_DaqAoSetCurrData" />

```cpp
U32 Acm_DaqAoSetCurrData(HAND DeviceHandle, U16	AoChannel, F32 AoData)
```

#### Acm_DaqAoGetRawData
<a name="Acm_DaqAoGetRawData" />

```cpp
U32 Acm_DaqAoGetRawData(HAND DeviceHandle, U16 AoChannel, PU16 AoData)
```

#### Acm_DaqAoGetEngData
<a name="Acm_DaqAoGetEngData" />

```cpp
U32 Acm_DaqAoGetEngData(HAND DeviceHandle, U16 AoChannel, PF32 AoData)
```

#### Acm_DaqAoGetVoltData
<a name="Acm_DaqAoGetVoltData" />

```cpp
U32 Acm_DaqAoGetVoltData(HAND DeviceHandle, U16	AoChannel, PF32 AoData)
```

#### Acm_DaqAoGetCurrData
<a name="Acm_DaqAoGetCurrData" />

```cpp
U32 Acm_DaqAoGetCurrData(HAND DeviceHandle, U16	AoChannel, PF32 AoData)
```

#### Acm_DaqAoSetCaliType
<a name="Acm_DaqAoSetCaliType" />

```cpp
U32 Acm_DaqAoSetCaliType(HAND DeviceHandle, U16	AoChannel, U16 TrimType)
```

#### Acm_DaqAoSetCaliValue
<a name="Acm_DaqAoSetCaliValue" />

```cpp
U32 Acm_DaqAoSetCaliValue(HAND DeviceHandle, U16 AoChannel, U16 CaliData)
```

#### Acm_DaqAoCaliDone
<a name="Acm_DaqAoCaliDone" />

```cpp
U32 Acm_DaqAoCaliDone(HAND DeviceHandle, U16 AoChannel, bool done)
```

#### Acm_DaqAoCaliDefault
<a name="Acm_DaqAoCaliDefault" />

```cpp
U32 Acm_DaqAoCaliDefault(HAND DeviceHandle, U16	AoChannel)
```

#### Acm_DaqAoGetChannelStatus
<a name="Acm_DaqAoGetChannelStatus" />

```cpp
U32 Acm_DaqAoGetChannelStatus(HAND DeviceHandle, U16 AoChannel, PU32 ChanStatus)
```

#### Acm_DaqSetScaledProperty
<a name="Acm_DaqSetScaledProperty" />

```cpp
U32 Acm_DaqSetScaledProperty(HAND DeviceHandle, PORT_TYPE Type, U16 Channel, F32 UpperBound, F32 LowerBound, U16 Resolution, I16 TransType)
```

#### Acm_DaqAiGetRawDataEx
<a name="Acm_DaqAiGetRawDataEx" />

```cpp
U32 Acm_DaqAiGetRawDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AiChannel, PU16 AiData)
```

#### Acm_DaqAiGetEngDataEx
<a name="Acm_DaqAiGetEngDataEx" />

```cpp
U32 Acm_DaqAiGetEngDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AiChannel, PF32 AiData)
```

#### Acm_DaqAiGetVoltDataEx
<a name="Acm_DaqAiGetVoltDataEx" />

```cpp
U32 Acm_DaqAiGetVoltDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AiChannel, PF32 AiData)
```

#### Acm_DaqAiGetCurrDataEx
<a name="Acm_DaqAiGetCurrDataEx" />

```cpp
U32 Acm_DaqAiGetCurrDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AiChannel, PF32 AiData)
```

#### Acm_DaqAiGetChannelStatusEx
<a name="Acm_DaqAiGetChannelStatusEx" />

```cpp
U32 Acm_DaqAiGetChannelStatusEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AiChannel, PU32 ChanStatus)
```

#### Acm_DaqAoSetRawDataEx
<a name="Acm_DaqAoSetRawDataEx" />

```cpp
U32 Acm_DaqAoSetRawDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, U16 AoData)
```

#### Acm_DaqAoSetEngDataEx
<a name="Acm_DaqAoSetEngDataEx" />

```cpp
U32 Acm_DaqAoSetEngDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, F32 AoData)
```

#### Acm_DaqAoSetVoltDataEx
<a name="Acm_DaqAoSetVoltDataEx" />

```cpp
U32 Acm_DaqAoSetVoltDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, F32 AoData)
```

#### Acm_DaqAoSetCurrDataEx
<a name="Acm_DaqAoSetCurrDataEx" />

```cpp
U32 Acm_DaqAoSetCurrDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, F32 AoData)
```

#### Acm_DaqAoGetRawDataEx
<a name="Acm_DaqAoGetRawDataEx" />

```cpp
U32 Acm_DaqAoGetRawDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, PU16 AoData)
```

#### Acm_DaqAoGetEngDataEx
<a name="Acm_DaqAoGetEngDataEx" />

```cpp
U32 Acm_DaqAoGetEngDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, PF32 AoData)
```

#### Acm_DaqAoGetVoltDataEx
<a name="Acm_DaqAoGetVoltDataEx" />

```cpp
U32 Acm_DaqAoGetVoltDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, PF32 AoData)
```

#### Acm_DaqAoGetCurrDataEx
<a name="Acm_DaqAoGetCurrDataEx" />

```cpp
U32 Acm_DaqAoGetCurrDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 AoChannel, PF32 AoData)
```

#### Acm_DaqGetIOLinkStatus
<a name="Acm_DaqGetIOLinkStatus" />

```cpp
U32 Acm_DaqGetIOLinkStatus(HAND DeviceHandle, PU32 pStatus)
```

#### Acm_DaqCntTriggerCmp
<a name="Acm_DaqCntTriggerCmp" />

```cpp
U32 Acm_DaqCntTriggerCmp(HAND DeviceHandle, U16 CntChannel)
```

#### Acm_DaqCntResetLatch
<a name="Acm_DaqCntResetLatch" />

```cpp
U32 Acm_DaqCntResetLatch(HAND DeviceHandle, U16 CntChannel)
```

#### Acm_DaqCntResetCmp
<a name="Acm_DaqCntResetCmp" />

```cpp
U32 Acm_DaqCntResetCmp(HAND DeviceHandle, U16 CntChannel)
```

#### Acm_DaqCntResetCnt
<a name="Acm_DaqCntResetCnt" />

```cpp
U32 Acm_DaqCntResetCnt(HAND DeviceHandle, U16 CntChannel)
```

#### Acm_DaqCntGetCounterData
<a name="Acm_DaqCntGetCounterData" />

```cpp
U32 Acm_DaqCntGetCounterData(HAND DeviceHandle, U16 CntChannel, PF64 CounterData)
```

#### Acm_DaqCntSetCounterData
<a name="Acm_DaqCntSetCounterData" />

```cpp
U32 Acm_DaqCntSetCounterData(HAND DeviceHandle, U16 CntChannel, F64 CounterData)
```

#### Acm_DaqCntGetCounterFrequency
<a name="Acm_DaqCntGetCounterFrequency" />

```cpp
U32 Acm_DaqCntGetCounterFrequency(HAND DeviceHandle, U16 CntChannel, PF64 Frequency)
```

#### Acm_DaqCntGetExtDriveData
<a name="Acm_DaqCntGetExtDriveData" />

```cpp
U32 Acm_DaqCntGetExtDriveData(HAND DeviceHandle, U16 CntChannel, PF64 CounterData)
```

#### Acm_DaqCntSetExtDriveData
<a name="Acm_DaqCntSetExtDriveData" />

```cpp
U32 Acm_DaqCntSetExtDriveData(HAND DeviceHandle, U16 CntChannel, F64 CounterData)
```

#### Acm_DaqCntGetLatchData
<a name="Acm_DaqCntGetLatchData" />

```cpp
U32 Acm_DaqCntGetLatchData(HAND DeviceHandle, U16 CntChannel, PF64 LatchData)
```

#### Acm_DaqCntGetCmpData
<a name="Acm_DaqCntGetCmpData" />

```cpp
U32 Acm_DaqCntGetCmpData(HAND DeviceHandle, U16 CntChannel, PF64 CmpData)
```

#### Acm_DaqCntSetCmpData
<a name="Acm_DaqCntSetCmpData" />

```cpp
U32 Acm_DaqCntSetCmpData(HAND DeviceHandle, U16 CntChannel, F64 CmpData)
```

#### Acm_DaqCntSetCmpTable
<a name="Acm_DaqCntSetCmpTable" />

```cpp
U32 Acm_DaqCntSetCmpTable(HAND DeviceHandle, U16 CntChannel, PF64 TableArray, I32 ArrayCount)
```

#### Acm_DaqCntSetCmpAuto
<a name="Acm_DaqCntSetCmpAuto" />

```cpp
U32 Acm_DaqCntSetCmpAuto(HAND DeviceHandle, U16 CntChannel, F64 Start, F64 End, F64 Interval)
```

#### Acm_DaqCntGetLatchBufferStatus
<a name="Acm_DaqCntGetLatchBufferStatus" />

```cpp
U32 Acm_DaqCntGetLatchBufferStatus(HAND DeviceHandle, U16 CntChannel, PU32 RemainCnt, PU32 SpaceCnt)
```

#### Acm_DaqCntReadLatchBuffer
<a name="Acm_DaqCntReadLatchBuffer" />

```cpp
U32 Acm_DaqCntReadLatchBuffer(HAND DeviceHandle, U16 CntChannel, PF64 LatchDataArray, PU32 DataCnt)
```

#### Acm_DaqCntTriggerCmpEx
<a name="Acm_DaqCntTriggerCmpEx" />

```cpp
U32 Acm_DaqCntTriggerCmpEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel)
```

#### Acm_DaqCntTriggerLatchEx
<a name="Acm_DaqCntTriggerLatchEx" />

```cpp
U32 Acm_DaqCntTriggerLatchEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel)
```

#### Acm_DaqCntResetLatchEx
<a name="Acm_DaqCntResetLatchEx" />

```cpp
U32 Acm_DaqCntResetLatchEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel)
```

#### Acm_DaqCntResetCmpEx
<a name="Acm_DaqCntResetCmpEx" />

```cpp
U32 Acm_DaqCntResetCmpEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel)
```

#### Acm_DaqCntResetCntEx
<a name="Acm_DaqCntResetCntEx" />

```cpp
U32 Acm_DaqCntResetCntEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel)
```

#### Acm_DaqCntGetCounterDataEx
<a name="Acm_DaqCntGetCounterDataEx" />

```cpp
U32 Acm_DaqCntGetCounterDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 CounterData)
```

#### Acm_DaqCntSetCounterDataEx
<a name="Acm_DaqCntSetCounterDataEx" />

```cpp
U32 Acm_DaqCntSetCounterDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, F64 CounterData)
```

#### Acm_DaqCntGetCounterFrequencyEx
<a name="Acm_DaqCntGetCounterFrequencyEx" />

```cpp
U32 Acm_DaqCntGetCounterFrequencyEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 Frequency)
```

#### Acm_DaqCntGetExtDriveDataEx
<a name="Acm_DaqCntGetExtDriveDataEx" />

```cpp
U32 Acm_DaqCntGetExtDriveDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 CounterData)
```

#### Acm_DaqCntSetExtDriveDataEx
<a name="Acm_DaqCntSetExtDriveDataEx" />

```cpp
U32 Acm_DaqCntSetExtDriveDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, F64 CounterData)
```

#### Acm_DaqCntGetLatchDataEx
<a name="Acm_DaqCntGetLatchDataEx" />

```cpp
U32 Acm_DaqCntGetLatchDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 LatchData)
```

#### Acm_DaqCntGetCmpDataEx
<a name="Acm_DaqCntGetCmpDataEx" />

```cpp
U32 Acm_DaqCntGetCmpDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 CmpData)
```

#### Acm_DaqCntSetCmpDataEx
<a name="Acm_DaqCntSetCmpDataEx" />

```cpp
U32 Acm_DaqCntSetCmpDataEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, F64 CmpData)
```

#### Acm_DaqCntSetCmpTableEx
<a name="Acm_DaqCntSetCmpTableEx" />

```cpp
U32 Acm_DaqCntSetCmpTableEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 TableArray, I32 ArrayCount)
```

#### Acm_DaqCntSetCmpAutoEx
<a name="Acm_DaqCntSetCmpAutoEx" />

```cpp
U32 Acm_DaqCntSetCmpAutoEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, F64 Start, F64 End, F64 Interval)
```

#### Acm_DaqCntGetLatchBufferStatusEx
<a name="Acm_DaqCntGetLatchBufferStatusEx" />

```cpp
U32 Acm_DaqCntGetLatchBufferStatusEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PU32 RemainCnt, PU32 SpaceCnt)
```

#### Acm_DaqCntReadLatchBufferEx
<a name="Acm_DaqCntReadLatchBufferEx" />

```cpp
U32 Acm_DaqCntReadLatchBufferEx(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 CntChannel, PF64 LatchDataArray, PU32 DataCnt)
```

#### Acm_AxPWMOut
<a name="Acm_AxPWMOut" />

```cpp
U32 Acm_AxPWMOut(HAND AxisHandle,U32 OFForON,U32 PulseCount)
```

#### Acm_AxGetPWMOutState
<a name="Acm_AxGetPWMOutState" />

```cpp
U32 Acm_AxGetPWMOutState(HAND AxisHandle,PU32 OFForON)
```

#### Acm_DevECATOpen
<a name="Acm_DevECATOpen" />

```cpp
U32 Acm_DevECATOpen(U32 DeviceNumber, U16 Ring0SlaveCount, U16 Ring1SlaveCount, U16 Timeout, PHAND DeviceHandle)
```

#### Acm_DevReadMailBox
<a name="Acm_DevReadMailBox" />

```cpp
U32 Acm_DevReadMailBox(HAND Handle, U16 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```

#### Acm_DevReadMultiMailBox
<a name="Acm_DevReadMultiMailBox" />

```cpp
U32 Acm_DevReadMultiMailBox(HAND Handle, U8 object_id, PU16 par_id, PU32 DataBuffer, PU32 ErrorBuffer, U32 ArrayElements)
```

#### Acm_DevWriteMailBox
<a name="Acm_DevWriteMailBox" />

```cpp
U32 Acm_DevWriteMailBox(HAND Handle, U16 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```

#### Acm_LoadENI
<a name="Acm_LoadENI" />

```cpp
U32 Acm_LoadENI(HAND DeviceHandle, PI8 FilePath)
```

#### Acm_DevGetMasInfo
<a name="Acm_DevGetMasInfo" />

```cpp
U32 Acm_DevGetMasInfo(HAND DeviceHandle, PVOID pMasInfo, PU16 SlaveIPArray, PU32 SlvCnt)
```

#### Acm_DevGetMasStates
<a name="Acm_DevGetMasStates" />

```cpp
U32 Acm_DevGetMasStates(HAND DeviceHandle, U16 RingNo, PU16 SlvCounters, PU16 SlvStates)
```

#### Acm_DevGetSlaveInfo
<a name="Acm_DevGetSlaveInfo" />

```cpp
U32 Acm_DevGetSlaveInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PVOID pInfo)
```

#### Acm_DevGetModuleInfo
<a name="Acm_DevGetModuleInfo" />

```cpp
U32 Acm_DevGetModuleInfo(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, PU32 ModIDArray, PU32 ModCnt)
```

#### Acm_DevGetSlaveDataCnt
<a name="Acm_DevGetSlaveDataCnt" />

```cpp
U32 Acm_DevGetSlaveDataCnt(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U8 DataType, PU32 DataCnt)
```

#### Acm_DevGetSlaveFwVersion
<a name="Acm_DevGetSlaveFwVersion" />

```cpp
U32 Acm_DevGetSlaveFwVersion(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, OUT PI8 VersionInfo)
```

#### Acm_DevSetSlaveID
<a name="Acm_DevSetSlaveID" />

```cpp
U32 Acm_DevSetSlaveID(HAND DeviceHandle, U16 RingNo, U16 SlaveIP, U16 SlaveNewIP)
```