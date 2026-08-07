# Common Motion API 2.0 (AdvCmnAPI_CM2)
#### Acm2_GetAvailableDevs
Get all device list.
```cpp
U32 Acm2_GetAvailableDevs(DEVLIST *DeviceList, U32 MaxEntries, PU32 OutEntries)
```

#### Acm2_DevSaveAllMapFile
Upload input/output mapping table from device.

```cpp
U32 Acm2_DevSaveAllMapFile(PI8 FilePath)
```

#### Acm2_DevLoadAllMapFile
Download input/output mapping table to device.

```cpp
U32 Acm2_DevLoadAllMapFile(PI8 FilePath)
```

#### Acm2_GetMappedPhysicalID
Get mapped physical id of device.

```cpp
U32 Acm2_GetMappedPhysicalID(ADV_OBJ_TYPE ObjType, U32 ObjLogicalID, PU32 DeviceNumber, PU32 ObjPhysicalID)
```

#### Acm2_GetMappedLogicalIDList
Get mapped list of logical id.

```cpp
U32 Acm2_GetMappedLogicalIDList(ADV_OBJ_TYPE ObjType, U32 DeviceLogicalID, PU32 LogicallIDList, PU32 ObjCnt)
```

#### Acm2_GetMappedObjInfo
Get mapped object information.

```cpp
U32 Acm2_GetMappedObjInfo(ADV_OBJ_TYPE ObjType, U32 ObjLogicalID, VOID *pObjInfo)
```

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

#### Acm2_DevInitialize
Initial the device.

```cpp
U32 Acm2_DevInitialize()
```

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

#### Acm2_AxPTP
Set axis move with position.

```cpp
U32 Acm2_AxPTP(U32 AxID, ABS_MODE ptpMode, F64 Distance)
```

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

#### Acm2_SetProperty
Set device/axis property.

```cpp
U32 Acm2_SetProperty(U32 ObjID, U32 PropertyID, F64 Value)
```

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

#### Acm2_SetMultiProperty
Set multiple properties at once.

```cpp
U32 Acm2_SetMultiProperty(U32 ObjID, PU32 PropertyID, PF64 Value, U32 Data_Cnt, PU32 ErrorBuffer)
```

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
for i in range(data_cnt.value):
    print('set[{0}]:{1}, get:{2}'.format(i, value_arr[i].value, get_val[i]))
```

#### Acm2_GetRawProperty
Get raw property value.

```cpp
U32 Acm2_GetRawProperty(U32 ObjID, U32 PropertyID, PVOID Value, PU32 BufferLength)
```

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


#### Acm2_DevLoadAllConfig
Load all configuration at once.

```cpp
U32 Acm2_DevLoadAllConfig(PI8 ConfigPath)
```

#### Acm2_DevLoadConfig
Load configuration.

```cpp
U32 Acm2_DevLoadConfig(U32 DevID, PI8 ConfigPath)
```

#### Acm2_DevReadMailBox
Read mailbox of device.

```cpp
U32 Acm2_DevReadMailBox(ADV_OBJ_TYPE ObjType, U32 ObjID, U32 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```

#### Acm2_DevWriteMailBox
Write mailbox of device.

```cpp
U32 Acm2_DevWriteMailBox(ADV_OBJ_TYPE ObjType, U32 ObjID, U32 par_id, U32 data_index, U32 data_count, PU32 DataBuffer)
```

#### Acm2_GetErrors
Get error of device.

```cpp
U32 Acm2_GetErrors(U32 DevID, PVOID Error, PU32 ErrorCount)
```

#### Acm2_ResetErrorRecord
Reset error.

```cpp
U32 Acm2_ResetErrorRecord(U32 DevID)
```

#### Acm2_DevPreviewMotion
Preview motion.

```cpp
U32 Acm2_DevPreviewMotion(U32 DevID, PI8 InputFile, PI8 OutputFile, U16 NumberOfAxes)
```

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

#### Acm2_GetLastError
Get last error of system.

```cpp
U32 Acm2_GetLastError(ADV_OBJ_TYPE ObjType, U32 ObjLogicalID)
```

#### Acm2_AxReturnPausePosition
Get axis pause position.

```cpp
U32 Acm2_AxReturnPausePosition(U32 AxID)
```

#### Acm2_AxSetSvOn
Set axis servo on/off.

```cpp
U32 Acm2_AxSetSvOn(U32 AxID, DO_ONOFF OnOff)
```

#### Acm2_DevSetAllSvOn
Set all axes servo on.off.

```cpp
U32 Acm2_DevSetAllSvOn(DO_ONOFF OnOff)
```

#### Acm2_AxSetErcOn
Set axis erc on/off.

```cpp
U32 Acm2_AxSetErcOn(U32 AxID, DO_ONOFF OnOff)
```

#### Acm2_AxResetAlm
Reset axis alarm logic.

```cpp
U32 Acm2_AxResetAlm(U32 AxID, DO_ONOFF OnOff)
```

#### Acm2_AxMoveContinue
Set aixs continue move.

```cpp
U32 Acm2_AxMoveContinue(U32 AxID, MOTION_DIRECTION Direction)
```

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

#### Acm2_AxHome
Set axis moving home with direction and home mode.

```cpp
U32 Acm2_AxHomeEx(U32 AxID, U32 DirMode)
```

#### Acm2_AxMoveGantryHome
Set axis moving home with gantry.

```cpp
U32 Acm2_AxMoveGantryHome(U32 AxID, HOME_MODE HomeMode, MOTION_DIRECTION Direction)
```

#### Acm2_AxSetHomeSpeedProfile
Set axis home speed config.

```cpp
U32 Acm2_AxSetHomeSpeedProfile(U32 AxID, SPEED_PROFILE_PRM ProfileVel)
```

#### Acm2_AxChangePos
Set axis position.

```cpp
U32 Acm2_AxChangePos(U32 AxID, F64 NewPosition)
```

#### Acm2_AxChangeVel
Set axis velocity.

```cpp
U32 Acm2_AxChangeVel(U32 AxID, F64 NewVelocity, F64 NewAcc, F64 NewDec)
```

#### Acm2_AxChangeVelByRate
Set axis velocity by rate.

```cpp
U32 Acm2_AxChangeVelByRate(U32 AxID, U32 Rate, F64 NewAcc, F64 NewDec)
```

#### Acm2_AxMoveImpose
Set axis impose.

```cpp
U32 Acm2_AxMoveImpose(U32 AxID, F64 Position, F64 NewVelocity)
```

#### Acm2_AxResetError
Reset error of axis.

```cpp
U32 Acm2_AxResetError(U32 AxID)
```

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

#### Acm2_AxGetMotionIO
Get axis motion IO status.

```cpp
U32 Acm2_AxGetMotionIO(U32 AxID, MOTION_IO *Status)
```

#### Acm2_AxSetPosition
Set axis position.

```cpp
U32 Acm2_AxSetPosition(U32 AxID, POSITION_TYPE PosType, F64 Position)
```

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

#### Acm2_AxEnableExternalMode
Enable axis external mode.

```cpp
U32 Acm2_AxEnableExternalMode(U32 AxID, EXT_DRIVE_MODE ExtDrvMode)
```

#### Acm2_AxSoftJog
Set axis jog.

```cpp
U32 Acm2_AxSoftJog(U32 AxID, MOTION_DIRECTION Direction)
```

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

#### Acm2_AxMotionStart
Start motion.

```cpp
U32 Acm2_AxMotionStart(PU32 AxisArray, U32 ArrayElements)
```

#### Acm2_AxPause
Pause motion.

```cpp
U32 Acm2_AxPause(U32 AxID)
```

#### Acm2_AxResume
Resume motion.

```cpp
U32 Acm2_AxResume(U32 AxID)
```

#### Acm2_AxResetPVTTable
Reset axis PVT table.

```cpp
U32 Acm2_AxResetPVTTable(U32 AxID)
```

#### Acm2_AxLoadPVTTable
Load axis PVT table.

```cpp
U32 Acm2_AxLoadPVTTable(U32 AxID, PF64 Position, PF64 Velocity, PF64 Time, U32 ArrayElements)
```

#### Acm2_AxLoadPVTTableContinuous
Continuous loading PVT table.

```cpp
U32 Acm2_AxLoadPVTTableContinuous(U32 AxID, PF64 Position, PF64 Velocity, PF64 JerkFactor, PF64 MaxVel, PF64 Acc, PF64 Dec, F64 TimeDelay, U32 ArrayElements)
```

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

#### Acm2_AxCheckPTBuffer
Check axis PT buffer.

```cpp
U32 Acm2_AxCheckPTBuffer(U32 AxID, PU32 Freespace)
```

#### Acm2_AxAddPTData
Add axis PT data.

```cpp
U32 Acm2_AxAddPTData(U32 AxID, F64 Position, F64 Time)
```

#### Acm2_AxMovePT
Move PT motion.

```cpp
U32 Acm2_AxMovePT(U32 AxID)
```

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

#### Acm2_AxGearIn
Set axis gear.

```cpp
U32 Acm2_AxGearIn(U32 PrimaryAxisID, U32 FollowingAxisID, GEAR_IN_PRM GearInParameter)
```

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

#### Acm2_AxPhaseAx
Set axis phase.

```cpp
U32 Acm2_AxPhaseAx(U32 AxID, PHASE_AXIS_PRM PhaseAxParameter)
```

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

#### Acm2_GpGetPausePosition
Get group pause position.

```cpp
U32 Acm2_GpGetPausePosition(U32 GpID, PF64 PosArray)
```

#### Acm2_GpCreate
Create group.

```cpp
U32 Acm2_GpCreate(U32 GpID, PU32 AxisArray, U32 ArrayElements)
```

#### Acm2_GpGetAxesInGroup
Check axes group.

```cpp
U32 Acm2_GpGetAxesInGroup(U32 GpID, PU32 AxisArray, PU32 ArrayElements)
```

#### Acm2_GpResetError
Reset error of group.

```cpp
U32 Acm2_GpResetError(U32 GpID)
```

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

#### Acm2_GpResume

```cpp
U32 Acm2_GpResume(U32 GpID)
```

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

#### Acm2_GpMotionStop
Stop group motion.

```cpp
U32 Acm2_GpMotionStop(U32 GpID, MOTION_STOP_MODE StopMode, F64 NewDec)
```

#### Acm2_GpChangeVel
Change velocity of group.

```cpp
U32 Acm2_GpChangeVel(U32 GpID, F64 NewVelocity, F64 NewAcc, F64 NewDec)
```

#### Acm2_GpChangeVelByRate
Change group velocity by rate.

```cpp
U32 Acm2_GpChangeVelByRate(U32 GpID, U32 Rate, F64 NewAcc, F64 NewDec)
```

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

#### Acm2_GpSetSpeedProfile
Get group speed information.

```cpp
U32 Acm2_GpSetSpeedProfile(U32 GpID, SPEED_PROFILE_PRM ProfileVel)
```

#### Acm2_GpGetState
Get group status.

```cpp
U32 Acm2_GpGetState(U32 GpID, PU32 State)
```

#### Acm2_GpLoadPath
Load path table group.

```cpp
U32 Acm2_GpLoadPath(U32 GpID, PI8 FilePath, PU32 TotalCount)
```

#### Acm2_GpAddPath
Add path into group.

```cpp
U32 Acm2_GpAddPath(U32 GpID, U32 MoveCmd, PATH_MOVE_MODE_CM2 MoveMode, F64 FH, F64 FL, F64 Acc, F64 Dec, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)
```

#### Acm2_GpMovePath
Start move group after add path.

```cpp
U32 Acm2_GpMovePath(U32 GpID)
```

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

#### Acm2_GpMoveSelPath

```cpp
U32 Acm2_GpMoveSelPath(U32 GpID, U32 StartIndex, U32 EndIndex, U32 Repeat)
```

#### Acm2_GpGetPathIndexStatus
Get group information by the index of path table.

```cpp
U32 Acm2_GpGetPathIndexStatus(U32 GpID, U32 Index, PU32 CmdFunc, PU32 MoveMode, PF64 FH, PF64 FL, PF64 Acc, PF64 Dec, PF64 EndPoint_DataArray, PF64 CenPoint_DataArray, PU32 ArrayElements)
```

#### Acm2_GpDelay
Delay group.

```cpp
U32 Acm2_GpDelay(U32 GpID, U32 DelayTime)
```

#### Acm2_GpPathDO
Set device do on/off between path.

```cpp
U32 Acm2_GpPathDO(U32 GpID, PATH_DO_PRM  PathDOPrm)
```

#### Acm2_GpPathWaitDI
Wait DI status between path.

```cpp
U32 Acm2_GpPathWaitDI(U32 GpID, PATH_DI_WAIT_PRM DIWaitPrm)
```

#### Acm2_GpPathWaitForAxis
Wait axis between path.

```cpp
U32 Acm2_GpPathWaitForAxis(U32 GpID, PATH_AX_WAIT_PRM AxWaitPrm)
```

#### Acm2_GpLookAheadPath

```cpp
U32 Acm2_GpLookAheadPath(U32 GpID, U16 BufferSize, PI8 OutputFile)
```

#### Acm2_GpLookAheadPathFile

```cpp
U32 Acm2_GpLookAheadPathFile(U32 GpID, U16 BufferSize, PI8 InputPathFile, PI8 OutputFile, PU32 PathCount)
```

#### Acm2_GpLoadAndMovePath -->


#### Acm2_ChGetDIBit
Get DI bit by channel.

```cpp
U32 Acm2_ChGetDIBit(U32 DiChannel, PU32 BitData)
```

#### Acm2_ChSetDOBitByRingNo
Set DO bit by channel, and ring number.

```cpp
U32 Acm2_ChSetDOBitByRingNo(U32 RingNo, U32 SlaveID, U32 DoChannel, U32 BitData)
```

#### Acm2_ChGetDOBitByRingNo
Get DO bit by ring number, and channel.

```cpp
U32 Acm2_ChGetDOBitByRingNo(U32 RingNo, U32 SlaveID, U32 DoChannel, PU32 BitData)
```

#### Acm2_ChGetDIBitByRingNo
Get DI bit by ring number, and channel.

```cpp
U32 Acm2_ChGetDIBitByRingNo(U32 RingNo, U32 SlaveID, U32 DiChannel, PU32 BitData)
```

#### Acm2_ChSetDOByte
Set DO channel byte.

```cpp
U32 Acm2_ChSetDOByte(U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```

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

#### Acm2_ChGetDIByte
Get DI channel byte.

```cpp
U32 Acm2_ChGetDIByte(U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```

#### Acm2_ChSetDOByteByRingNo
Set DO byte by ring number.

```cpp
U32 Acm2_ChSetDOByteByRingNo(U32 RingNo, U32 SlaveID, U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```

#### Acm2_ChGetDOByteByRingNo
Get DO byte by ring number.

```cpp
U32 Acm2_ChGetDOByteByRingNo(U32 RingNo, U32 SlaveID, U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```

#### Acm2_ChGetDIByteByRingNo
Get DI byte by ring number.

```cpp
U32 Acm2_ChGetDIByteByRingNo(U32 RingNo, U32 SlaveID, U32 StartPort, U32 NumPort, PU32 ByteDataArray)
```

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

#### Acm2_ChGetAOData
Get AO data.

```cpp
U32 Acm2_ChGetAOData(U32 AoChannel, DAQ_DATA_TYPE Type, PF64 AoData)
```

#### Acm2_ChSetAODataByRingNo
Set AO data by ring number.

```cpp
U32 Acm2_ChSetAODataByRingNo(U32 RingNo, U32 SlaveID, U32 AoChannel, DAQ_DATA_TYPE Type, F64 AoData)
```

#### Acm2_ChGetAODataByRingNo
Get AO data by ring number.

```cpp
U32 Acm2_ChGetAODataByRingNo(U32 RingNo, U32 SlaveID, U32 AoChannel, DAQ_DATA_TYPE Type, PF64 AoData)
```

#### Acm2_ChGetAIData
Get AI data.

```cpp
U32 Acm2_ChGetAIData(U32 AiChannel, DAQ_DATA_TYPE Type, PF64 AiData)
```

#### Acm2_ChGetAIDataByRingNo
Get AI data by ring number.

```cpp
U32 Acm2_ChGetAIDataByRingNo(U32 RingNo, U32 SlaveID, U32 AiChannel, DAQ_DATA_TYPE Type, PF64 AiData)
```

#### Acm2_ChGetCntData
Get counter data.

```cpp
U32 Acm2_ChGetCntData(U32 CntChannel, PF64 CounterData)
```

#### Acm2_ChSetCntData
Set counter data.

```cpp
U32 Acm2_ChSetCntData(U32 CntChannel, F64 CounterData)
```

#### Acm2_ChLinkCmpFIFO
Set compare position.

```cpp
U32 Acm2_ChLinkCmpFIFO(U32 ChID, PU32 AxisArray, U32 ArrayElement)
```

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

#### Acm2_ChGetLinkedCmpObject
Get compare do linked object.

```cpp
U32 Acm2_ChGetLinkedCmpObject(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```

#### Acm2_ChEnableCmp
Enable compare channel.

```cpp
U32 Acm2_ChEnableCmp(U32 ChID, U32 Enable)
```

#### Acm2_ChSetCmpOut
Set compare channel on/off.

```cpp
U32 Acm2_ChSetCmpOut(U32 ChID, DO_ONOFF OnOff)
```

#### Acm2_ChSetCmpDoOut
Set compare on/off.

```cpp
U32 Acm2_ChSetCmpDoOut(U32 ChID, DO_ONOFF OnOff)
```

#### Acm2_AxGetCmpData
Get compared data by axis.

```cpp
U32 Acm2_AxGetCmpData(U32 AxID, PF64 CmpData)
```

#### Acm2_ChGetCmpData
Get compared data by channel.

```cpp
U32 Acm2_ChGetCmpData(U32 CmpChannel, PF64 CmpData, U32 ObjectArrayCount)
```

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


#### Acm2_AxSetCmpAuto
Set auto compare by axis.

```cpp
U32 Acm2_AxSetCmpAuto(U32 AxID, F64 StartPosition, F64 EndPosition, F64 Interval)
```

#### Acm2_ChSetCmpAuto
Set auto compare by channel.

```cpp
U32 Acm2_ChSetCmpAuto(U32 CmpChannel, F64 StartPosition, F64 EndPosition, F64 Interval)
```

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

#### Acm2_ChSetMultiCmpBufferData
Set multi compare buffer.

```cpp
U32 Acm2_ChSetMultiCmpBufferData(U32 ChID, PF64 MultiCmpTable, U32 ObjectArrayCount, U32 DataArrayCount)
```

#### Acm2_ChResetCmpData
Reset compare data.

```cpp
U32 Acm2_ChResetCmpData(U32 CmpChannel)
```

#### Acm2_ChGetCmpBufferStatus
Get compared buffer status.

```cpp
U32	Acm2_ChGetCmpBufferStatus(U32 CmpChannel, PBUFFER_STATUS bufferstatus)
```

#### Acm2_ChLinkLatchAxis
Link latch to axis.
```cpp
U32 Acm2_ChLinkLatchAxis(U32 ChID, PU32 AxisArray, U32 AxisCount)
```

#### Acm2_ChLinkLatchObject
Lift latch to object.
```cpp
U32 Acm2_ChLinkLatchObject(U32 ChID, ADV_OBJ_TYPE ObjType, PU32 ObjArray, U32 ArrayElement)
```

#### Acm2_ChGetLinkedLatchObject
Get linked latch object.
```cpp
U32 Acm2_ChGetLinkedLatchObject(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```

#### Acm2_ChTriggerLatch
Trigger latch by channel.

```cpp
U32 Acm2_ChTriggerLatch(U32 ChID)
```

#### Acm2_AxReadLatchBuffer
Read latch buffer.

```cpp
U32	Acm2_AxReadLatchBuffer(U32 AxID, PF64 LatchDataArray, PU32 DataCnt)
```

#### Acm2_ChReadLatchBuffer
Read latch buffer by channel.

```cpp
U32	Acm2_ChReadLatchBuffer(U32 LtcChannel, PF64 LatchDataArray, U32 ObjectArrayCount, PU32 DataArrayCount)
```

#### Acm2_AxGetLatchBufferStatus
Get latch buffer status.

```cpp
U32	Acm2_AxGetLatchBufferStatus(U32 AxID, PU32 RemainCnt, PU32 SpaceCnt)
```

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

#### Acm2_AxResetLatchBuffer
Reset latch buffer.

```cpp
U32	Acm2_AxResetLatchBuffer(U32 AxID)
```

#### Acm2_ChResetLatchBuffer
Reset latch buffer by channel.

```cpp
U32	Acm2_ChResetLatchBuffer(U32 LtcChannel)
```

#### Acm2_ChLinkPWMTable
Link PWM with object.

```cpp
U32 Acm2_ChLinkPWMTable(U32 ChID, ADV_OBJ_TYPE ObjType, U32 ObjectID)
```

#### Acm2_ChGetLinkedPWMTable
Get linked PWM Acm2_ChSetPWMTabletable by channel.

```cpp
U32 Acm2_ChGetLinkedPWMTable(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```

#### Acm2_ChSetPWMTable
Set PWM table by channel.

```cpp
U32 Acm2_ChSetPWMTable(U32 ChID, PF64 VelocityArray, PF64 PWMArray, U32 ArrayElements)
```

#### Acm2_ChLoadPWMTableFile
Loal PWM table file.

```cpp
U32 Acm2_ChLoadPWMTableFile(U32 ChID, PI8 FilePath, PU32 PointsCount)
```

#### Acm2_ChGetPWMTableStatus
Get PWM table status.

```cpp
U32	Acm2_ChGetPWMTableStatus(U32 ChID, PWM_TABLE_STATUS *PWMStatus)
```

#### Acm2_ChGetExtDriveData
Get external drive data by channel.

```cpp
U32 Acm2_ChGetExtDriveData(U32 ExtChannel, PF64 CounterData)
```

#### Acm2_ChSetExtDriveData
Set external drive data by channel.

```cpp
U32 Acm2_ChSetExtDriveData(U32 ExtChannel, F64 CounterData)
```

#### Acm2_ChLinkExtDriveObject
Link external drive object.

```cpp
U32 Acm2_ChLinkExtDriveObject(U32 ChID, ADV_OBJ_TYPE ObjType, U32 ObjectID)
```

#### Acm2_ChGetLinkedExtDriveObject
Get linked external drive object.

```cpp
U32 Acm2_ChGetLinkedExtDriveObject(U32 ChID, ADV_OBJ_TYPE *ObjType, PU32 ObjArray, PU32 ArrayElement)
```

#### Acm2_DevMDaqConfig
Set MDAQ config.

```cpp
U32 Acm2_DevMDaqConfig(U32 ChannelID, U32 Period, U32 AxisNo, U32 Method, U32 ChanType, U32 Count)
```

#### Acm2_DevMDaqGetConfig
Get MDAQ config.

```cpp
U32 Acm2_DevMDaqGetConfig(U32 ChannelID, PU32 Period, PU32 AxisNo, PU32 Method, PU32 ChanType, PU32 Count)
```

#### Acm2_DevMDaqStart
Start MDAQ.

```cpp
U32 Acm2_DevMDaqStart(U32 DevID)
```

#### Acm2_DevMDaqStop
Stop MDAQ.

```cpp
U32 Acm2_DevMDaqStop(U32 DevID)
```

#### Acm2_DevMDaqReset
Reset MDAQ.

```cpp
U32 Acm2_DevMDaqReset(U32 ChannelID)
```

#### Acm2_DevMDaqGetStatus
Get MDAQ status.

```cpp
U32 Acm2_DevMDaqGetStatus(U32 ChannelID, PU32 CurrentCnt, PU32 Status)
```

#### Acm2_DevMDaqGetData
Get MDAQ data.

```cpp
U32 Acm2_DevMDaqGetData(U32 ChannelID, U32 StartIndex, U32 MaxCount, PF64 DataBuffer)
```

#### Acm2_GetDSPFrmWareDwnLoadRate
Get FW download rate.

```cpp
U32 Acm2_GetDSPFrmWareDwnLoadRate(U32 DevID, PF64 Percentage)
```

#### Acm2_DevLoadENI
Download ENI file.

```cpp
U32 Acm2_DevLoadENI(U32 RingNo, PI8 ENIFile)
```

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

#### Acm2_DevGetSubDevicesID
Get subdevices id.

```cpp
U32 Acm2_DevGetSubDevicesID(U32 RingNo, ECAT_ID_TYPE IDType, PU32 SubDeviceIDArray, PU32 SubDeviceCnt)
```

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

#### Acm2_DevGetSubDeviceFwVersion
Get subdevice fw information.

```cpp
U32 Acm2_DevGetSubDeviceFwVersion(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, char *VersionInfo)
```

#### Acm2_DevSetSubDeviceID
Set subdevice id.

```cpp
U32 Acm2_DevSetSubDeviceID(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 SubDeviceNewID)
```

#### Acm2_DevSetSubDeviceStates
Set subdevice status.

```cpp
U32 Acm2_DevSetSubDeviceStates(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 SubDeviceState)
```

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

#### Acm2_DevWriteSDO
Write data by SDO.

```cpp
U32 Acm2_DevWriteSDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, VOID *pValue)
```

#### Acm2_DevReadSDO
Read data by SDO.

```cpp
U32 Acm2_DevReadSDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, VOID *pValue)
```

#### Acm2_DevWritePDO
Write data by PDO.

```cpp
U32 Acm2_DevWritePDO(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Index, U32 SubIndex, U32 Type, U32 DataSize, VOID *pValue)
```

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

#### Acm2_DevWriteReg
Write data by reg.

```cpp
U32 Acm2_DevWriteReg(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Address, U32 Type, U32 DataSize, VOID *pValue)
```

#### Acm2_DevReadReg
Read data by reg.

```cpp
U32 Acm2_DevReadReg(U32 RingNo, ECAT_ID_TYPE IDType, U32 SubDeviceID, U32 Address, U32 Type, U32 DataSize, VOID *pValue)
```

#### Acm2_DevReadSubDeviceCommErrCnt
Read subdevice communication error counter.

```cpp
U32 Acm2_DevReadSubDeviceCommErrCnt(U32 RingNo, PU32 ErrCntArray, PU32 ArrayElements)
```

#### Acm2_Ax1DCompensateTable
Set compensate table with one axis.

```cpp
U32 Acm2_Ax1DCompensateTable(U32 AxID, F64 OriginPos, F64 Pitch, PF64 OffsetData, U32 OffsetElements, U32 Direction)
```

#### Acm2_Ax2DCompensateTable
Set compensate table 2D.

```cpp
U32 Acm2_Ax2DCompensateTable(U32 AxID, U32 RelAxID, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataX, PF64 OffsetDataY, U32 OffsetElementsX, U32 OffsetElementsY)
```

#### Acm2_AxZAxisCompensateTable
Set compensate table Z axis.

```cpp
U32 Acm2_AxZAxisCompensateTable(U32 AxID, U32 RelAxID, U32 ZAxID, F64 OriginPosX, F64 OriginPosY, F64 PitchX, F64 PitchY, PF64 OffsetDataZ, U32 OffsetElementsX, U32 OffsetElementsY)
```

#### Acm2_AxGetCompensatePosition
Get compensate position by axis.

```cpp
U32 Acm2_AxGetCompensatePosition(U32 AxID, PF64 Position)
```

#### Acm2_DevOscChannelDataStart
Start Osc. channel data.

```cpp
U32 Acm2_DevOscChannelDataStart(U32 DevID)
```

#### Acm2_DevOscChannelDataStop
Stop Osc. channel data.

```cpp
U32 Acm2_DevOscChannelDataStop(U32 DevID)
```

#### Acm2_DevGetOscChannelDataConfig
Get config of Osc. channel.

```cpp
U32 Acm2_DevGetOscChannelDataConfig(U32 DevID, U16 ChannelID, POSC_PROFILE_PRM oscflg)
```

#### Acm2_DevSetOscChannelDataConfig
Set config of Osc. channel.

```cpp
U32 Acm2_DevSetOscChannelDataConfig(U32 DevID, U16 ChannelID, OSC_PROFILE_PRM oscflg)
```

#### Acm2_DevGetOscChannelData
Get Osc. channel data.

```cpp
U32 Acm2_DevGetOscChannelData(U32 DevID, U16 ChannelID, U32 DataIndex, PU32 MaxCount, PF64 DataBuffer)
```

#### Acm2_DevGetOscChannelStatus
Get Osc. channel status.

```cpp
U32  Acm2_DevGetOscChannelStatus(U32 DevID, PU32 Status)
```
