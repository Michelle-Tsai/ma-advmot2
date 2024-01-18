import unittest
import time
import os
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.MotionInfo import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

# if os.name == 'nt':
#     from colorama import init as colorama_init, Fore
#     colorama_init(autoreset=True, wrap=True, convert=True)
# else:
#     from AcmP.utils import Color

class AdvCmnAPI_Test(unittest.TestCase):
    def setUp(self):
        self.maxEnt = 10
        self.devlist = (DEVLIST*self.maxEnt)()
        self.outEnt = c_uint32(0)
        self.errCde = 0
        self.state = c_uint32(16)
        self.AdvMot = AdvCmnAPI_CM2
        self.gpid = c_uint32(0)
        gp_arr = [c_uint32(0), c_uint32(1)]
        self.axis_array = (c_uint32 * len(gp_arr))(*gp_arr)
    
    def tearDown(self):
        self.errCde = 0
    
    def test_GetAvailableDevs(self):
        # your switch number on board as device number
        excepted_dev_hex = '0x63003000'
        excepted_dev = int(excepted_dev_hex, 16)
        self.AdvMot.Acm2_GetAvailableDevs(self.devlist, self.maxEnt, byref(self.outEnt))
        result_dev = self.devlist[0].dwDeviceNum
        self.assertEqual(excepted_dev, result_dev)
    
    def test_DevOpen(self):
        excepted_dev_hex = '0x63003000'
        excepted_dev = int(excepted_dev_hex, 16)
        device_number = c_uint32(excepted_dev)
        self.device_info = DEVICEINFO()
        excepted_err = 0
        self.errCde = self.AdvMot.Acm2_DevOpen(device_number, byref(self.device_info))
        self.assertEqual(excepted_err, self.errCde)

    def test_Initialize(self):
        self.errCde = self.AdvMot.Acm2_DevInitialize()
        excepted_err = 0
        self.assertEqual(excepted_err, self.errCde)

    def test_DevClose(self):
        excepted_err = 0
        self.errCde = self.AdvMot.Acm2_DevAllClose()
        self.assertEqual(excepted_err, self.errCde)

    def test_LoadENI(self):
        ring_no = c_uint32(0)
        # eni file name has device number prefix
        if os.name == 'nt':
            eni_path = c_char_p(b'test\\63000000_eni0.xml')
        else:
            eni_path = b'test/63000000_eni0.xml'
        self.errCde = self.AdvMot.Acm2_DevLoadENI(ring_no, eni_path)
        excepted_err = 0
        self.assertEqual(excepted_err, self.errCde)
    
    def test_GetMDevice(self):
        ring_no = c_uint32(0)
        MDeviceInfo = ADVAPI_MDEVICE_INFO()
        self.errCde = self.AdvMot.Acm2_DevGetMDeviceInfo(ring_no, byref(MDeviceInfo))
        excepted_err = 0
        self.assertEqual(excepted_err, self.errCde)
    
    def test_DevExportMappingTable(self):
        # test0.xml will saved under current folder
        if os.name == 'nt':
            file_path = c_char_p(b'test\\test0.xml')
        else:
            file_path = b'test/test0.xml'
        self.errCde = self.AdvMot.Acm2_DevExportMappingTable(file_path)
        excepted_err = 0
        self.assertEqual(excepted_err, self.errCde)
    
    def test_DevImportMappingTable(self):
        if os.name == 'nt':
            file_path = c_char_p(b'test\\test0.xml')
        else:
            file_path = b'test/test0.xml'        
        self.errCde = self.AdvMot.Acm2_DevImportMappingTable(file_path)
        excepted_err = 0
        self.assertEqual(excepted_err, self.errCde)

    def test_AxPTP(self):
        ax_id = c_uint32(0)
        abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
        distance = c_double(1000)
        self.errCde = self.AdvMot.Acm2_AxPTP(ax_id, abs_mode, distance)
        excepted_err = 0
        self.assertEqual(excepted_err, self.errCde)

    def test_GetAxState(self):
        ax_id = c_uint32(0)
        state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
        self.AdvMot.Acm2_AxGetState(ax_id, state_type, byref(self.state))
        if (self.state.value != AXIS_STATE.STA_AX_READY.value):
            print('Not Ready')
    
    def test_ResetAll(self):
        ax_id_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
        excepted_err = 0
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        pos = c_double(0)
        state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
        # Check axis status
        for i in range(len(ax_id_arr)):
            state = c_uint32(16)
            self.AdvMot.Acm2_AxGetState(ax_id_arr[i], state_type, byref(state))
            while state.value != AXIS_STATE.STA_AX_READY.value:
                time.sleep(0.5) # sleep for 0.5 second
                self.AdvMot.Acm2_AxGetState(ax_id_arr[i], state_type, byref(state))
        # Clear all
        self.errCde = self.AdvMot.Acm2_DevResetAllError()
        self.assertEqual(excepted_err, self.errCde)
        # Set axis command position as 0
        for j in range(len(ax_id_arr)):
            self.errCde = self.AdvMot.Acm2_AxSetPosition(ax_id_arr[j], pos_type, pos)
            self.assertEqual(excepted_err, self.errCde)
    
    def test_AxGetPosition(self):
        ax_id = c_uint32(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        pos = c_double(0)
        while self.state.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.test_GetAxState()
        self.errCde = self.AdvMot.Acm2_AxGetPosition(ax_id, pos_type, byref(pos))
        excepted_pos = c_double(1000)
        excepted_err = 0
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(excepted_pos.value, pos.value)

    def test_SetDeviceDIOProperty(self):
        do_ch = c_uint32(0)
        property_id = c_uint(PropertyID2.CFG_CH_DaqDoFuncSelect.value)
        val = c_double(1)
        excepted_err = 0
        self.errCde = self.AdvMot.Acm2_SetProperty(do_ch, property_id, val)
        self.assertEqual(excepted_err, self.errCde)
    
    def test_GetDeviceDIOProperty(self):
        do_ch = c_uint32(0)
        property_id = c_uint(PropertyID2.CFG_CH_DaqDoFuncSelect.value)
        val = c_double(1)
        get_val = c_double(0)
        excepted_err = 0
        self.errCde = self.AdvMot.Acm2_GetProperty(do_ch, property_id, byref(get_val))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(val.value, get_val.value)
    
    def test_SetDeviceDO_ON(self):
        do_ch = c_uint32(0)
        data = c_uint32(1)
        get_data = c_uint32(0)
        excepted_err = 0
        self.errCde = self.AdvMot.Acm2_ChSetDOBit(do_ch, data)
        self.assertEqual(excepted_err, self.errCde)
        self.errCde = self.AdvMot.Acm2_ChGetDOBit(do_ch, byref(get_data))
        self.assertEqual(excepted_err, self.errCde)      
        self.assertEqual(data.value, get_data.value)

    def test_CreatGroup(self):
        # Set axis0, axis1 as group, 0 as group id.
        excepted_err = 0
        self.errCde = self.AdvMot.Acm2_GpCreate(self.gpid, self.axis_array, len(self.axis_array))
        self.assertEqual(excepted_err, self.errCde)
    
    def test_CheckGroupAxes(self):
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        excepted_err = 0
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(self.gpid, get_axes, len_get)
        self.assertEqual(excepted_err, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(self.axis_array[idx], get_axes[idx])
    
    def test_RemoveGroup(self):
        remove_all_axes = c_uint32(0)
        excepted_err = 0
        self.errCde = self.AdvMot.Acm2_GpCreate(self.gpid, self.axis_array, remove_all_axes)
        self.assertEqual(excepted_err, self.errCde)

    def test_GetLastError_Device(self):
        excepted_err = 0
        obj_logicID = c_uint32(0)
        obj_type = c_uint(ADV_OBJ_TYPE.ADV_DEVICE.value)
        self.errCde = self.AdvMot.Acm2_GetLastError(obj_type, obj_logicID)
        self.assertEqual(excepted_err, self.errCde)

    def test_GetLastError_AXIS(self):
        excepted_err = 0
        for i in range(64):
            obj_logicID = c_uint32(i)
            obj_type = c_uint(ADV_OBJ_TYPE.ADV_AXIS.value)
            self.errCde = self.AdvMot.Acm2_GetLastError(obj_type, obj_logicID)
            self.assertEqual(excepted_err, self.errCde)

    def test_GetLastError_Group(self):
        excepted_err = 0
        for i in range(8):
            obj_logicID = c_uint32(i)
            obj_type = c_uint(ADV_OBJ_TYPE.ADV_GROUP.value)
            self.errCde = self.AdvMot.Acm2_GetLastError(obj_type, obj_logicID)
            self.assertEqual(excepted_err, self.errCde)

    def test_SetMultiPropertyAndCheck_AxisSpeed(self):
        excepted_err = 0
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
        self.errCde = self.AdvMot.Acm2_SetMultiProperty(ax_id, trans_ppt_arr, trans_val_arr, data_cnt, err_buffer)
        self.assertEqual(excepted_err, self.errCde)
        # Check value
        get_val = (c_double * data_cnt.value)()
        self.errCde = self.AdvMot.Acm2_GetMultiProperty(ax_id, trans_ppt_arr, get_val, data_cnt, err_buffer)
        self.assertEqual(excepted_err, self.errCde)
        for i in range(data_cnt.value):
            # print('set[{0}]:{1}, get:{2}'.format(i, value_arr[i].value, get_val[i]))
            self.assertEqual(value_arr[i].value, get_val[i])
    
    def test_SetAxSpeedInfoAndCheck(self):
        excepted_err = 0
        ax_id = c_uint32(0)
        speed_info = SPEED_PROFILE_PRM()
        speed_info.FH = c_double(3000)
        speed_info.FL = c_double(1500)
        speed_info.Acc = c_double(11000)
        speed_info.Dec = c_double(9900)
        speed_info.JerkFac = c_double(0)
        # Set speed information
        self.errCde = self.AdvMot.Acm2_AxSetSpeedProfile(ax_id, speed_info)
        self.assertEqual(excepted_err, self.errCde)

    def test_SetAxJogInfo(self):
        excepted_err = 0
        ax_id = c_uint32(0)
        jog_speed_info = JOG_SPEED_PROFILE_PRM()
        jog_speed_info.FH = c_double(8000)
        jog_speed_info.FL = c_double(1000)
        jog_speed_info.Acc = c_double(10000)
        jog_speed_info.Dec = c_double(5000)
        jog_speed_info.VLTime = c_double(2000)
        # Set axis 0 jog speed information
        self.errCde = self.AdvMot.Acm2_AxSetJogSpeedProfile(ax_id, jog_speed_info)
        self.assertEqual(excepted_err, self.errCde)
    
    def test_GetCurrentVelocity(self):
        excepted_err = 0
        ax_id = c_uint32(0)
        get_vel = c_double(0)
        vel_Type = c_uint(VELOCITY_TYPE.VELOCITY_CMD.value)
        # Get axis 0 current velocity
        self.errCde = self.AdvMot.Acm2_AxGetVel(ax_id, vel_Type, byref(get_vel))
        self.assertEqual(excepted_err, self.errCde)
    
    def test_PVTTable(self):
        excepted_err = 0
        ax_id = c_uint32(0)
        # Reset PVT table
        self.errCde = self.AdvMot.Acm2_AxResetPVTTable(ax_id)
        self.assertEqual(excepted_err, self.errCde)
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
        self.errCde = self.AdvMot.Acm2_AxLoadPVTTable(ax_id, posArr, velArr, timeArr, len(pos_arr))
        self.assertEqual(excepted_err, self.errCde)
        # Set PVT
        self.errCde = self.AdvMot.Acm2_AxMovePVT(ax_id)
        self.assertEqual(excepted_err, self.errCde)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        get_pos = c_double(0)
        while self.state.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.test_GetAxState()
        self.errCde = self.AdvMot.Acm2_AxGetPosition(ax_id, pos_type, byref(get_pos))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(c_double(30000).value, get_pos.value)

    def test_PTTable(self):
        excepted_err = 0
        ax_id = c_uint32(0)
        # Reset PT table
        self.errCde = self.AdvMot.Acm2_AxResetPTData(ax_id)
        self.assertEqual(excepted_err, self.errCde)
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
        for i in range(len(pos_arr)):
            self.errCde = self.AdvMot.Acm2_AxAddPTData(ax_id, pos_arr[i], time_arr[i])
            self.assertEqual(excepted_err, self.errCde)
        # Start move PT table
        self.errCde = self.AdvMot.Acm2_AxMovePT(ax_id)
        self.assertEqual(excepted_err, self.errCde)

        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        get_pos = c_double(0)
        # Check status
        while self.state.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.test_GetAxState()
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(ax_id, pos_type, byref(get_pos))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(c_double(30000).value, get_pos.value)

    def test_Gear(self):
        excepted_err = 0
        primary_ax = c_uint32(0)
        follow_ax = c_uint32(1)
        # Reset following axis
        self.errCde = self.AdvMot.Acm2_AxSyncOut(follow_ax)
        self.assertEqual(excepted_err, self.errCde)
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
        self.errCde = self.AdvMot.Acm2_AxGearIn(primary_ax, follow_ax, gear_param)
        self.assertEqual(excepted_err, self.errCde)
        # Move primary axis
        abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
        distance = c_double(10000)
        self.errCde = self.AdvMot.Acm2_AxPTP(primary_ax, abs_mode, distance)
        self.assertEqual(excepted_err, self.errCde)
        # Check status
        while self.state.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.test_GetAxState()
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 (primary) position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(primary_ax, pos_type, byref(get_pos_0))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(distance.value, get_pos_0.value)
        # Get axis 1 (following) position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(follow_ax, pos_type, byref(get_pos_1))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(distance.value, get_pos_1.value)
        # Reset following axis
        self.errCde = self.AdvMot.Acm2_AxSyncOut(follow_ax)
        self.assertEqual(excepted_err, self.errCde)

    def test_Gantry(self):
        excepted_err = 0
        primary_ax = c_uint32(0)
        follow_ax = c_uint32(1)
        # Reset following axis
        self.errCde = self.AdvMot.Acm2_AxSyncOut(follow_ax)
        self.assertEqual(excepted_err, self.errCde)
        # Set gantry parameter
        gantry_param = GANTRY_IN_PRM()
        # Set gantry reference source as command position
        gantry_param.RefSrc = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Set gantry direction as positive
        gantry_param.Direction = c_uint(MOTION_DIRECTION.DIRECTION_POS.value)
        # Set gantry
        self.errCde = self.AdvMot.Acm2_AxGantryIn(primary_ax, follow_ax, gantry_param)
        self.assertEqual(excepted_err, self.errCde)
        # Move primary axis
        abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
        distance = c_double(10000)
        self.errCde = self.AdvMot.Acm2_AxPTP(primary_ax, abs_mode, distance)
        self.assertEqual(excepted_err, self.errCde)
        # Check status
        while self.state.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.test_GetAxState()
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 (primary) position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(primary_ax, pos_type, byref(get_pos_0))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(distance.value, get_pos_0.value)
        # Get axis 1 (following) position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(follow_ax, pos_type, byref(get_pos_1))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(distance.value, get_pos_1.value)
        # Reset following axis
        self.errCde = self.AdvMot.Acm2_AxSyncOut(follow_ax)
        self.assertEqual(excepted_err, self.errCde)

    def test_GpLine(self):
        excepted_err = 0
        gp_ax_arr = [c_uint32(0), c_uint32(1)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(excepted_err, self.errCde)
        # Creat group 0, and set axis 0, 1 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(excepted_err, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(excepted_err, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
        # Set group move as relative
        gp_move_mode = c_uint(GP_LINE_MODE.LINE_REL.value)
        # Set group end position: axis(0) = 10000, axis(1) = 10000
        end_pos_arr = [c_double(10000), c_double(10000)]
        arr_element = c_uint32(len(end_pos_arr))
        end_arr = (c_double * len(end_pos_arr))(*end_pos_arr)
        # Group 0 move line
        self.errCde = self.AdvMot.Acm2_GpLine(gp_id, gp_move_mode, end_arr, byref(arr_element))
        # Check status
        while self.state.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.test_GetAxState()
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 (primary) position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(end_pos_arr[0].value, get_pos_0.value)
        # Get axis 1 (following) position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(end_pos_arr[1].value, get_pos_1.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(excepted_err, self.errCde)

    def test_2DArc(self):
        excepted_err = 0
        gp_ax_arr = [c_uint32(0), c_uint32(1)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(excepted_err, self.errCde)
        # Creat group 0, and set axis 0, 1 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(excepted_err, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(excepted_err, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
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
        self.errCde = self.AdvMot.Acm2_GpArc_Center(gp_id, arc_mode, center_arr, end_arr, byref(arr_element), dir_mode)
        self.assertEqual(excepted_err, self.errCde)
        # Check status
        while self.state.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.test_GetAxState()
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(end_ax_arr[0].value, get_pos_0.value)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(end_ax_arr[1].value, get_pos_1.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(excepted_err, self.errCde)

    def test_2DArc3P(self):
        excepted_err = 0
        gp_ax_arr = [c_uint32(0), c_uint32(1)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(excepted_err, self.errCde)
        # Creat group 0, and set axis 0, 1 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(excepted_err, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(excepted_err, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
        # Set 2D Arc mode
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
        self.errCde = self.AdvMot.Acm2_GpArc_3P(gp_id, arc_mode, refArr, endArr, byref(arr_element), dir_mode)
        self.assertEqual(excepted_err, self.errCde)
        # Check status
        while self.state.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.test_GetAxState()
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(end_arr[0].value, get_pos_0.value)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(end_arr[1].value, get_pos_1.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(excepted_err, self.errCde)


    def test_3DArcCenter(self):
        excepted_err = 0
        gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(excepted_err, self.errCde)
        # Creat group 0, and set axis 0, 1, 2 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(excepted_err, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(excepted_err, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
        # Set 3D Arc mode
        arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
        # Set 3D Arc CW, with 60 degree
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
        # Set direction as CW
        dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
        self.errCde = self.AdvMot.Acm2_Gp3DArc_Center(gp_id, arc_mode, center_arr, end_arr, byref(arr_element), dir_mode)
        self.assertEqual(excepted_err, self.errCde)
        # Check status
        while self.state.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.test_GetAxState()
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        get_pos_2 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(end_ax_arr[0].value, get_pos_0.value)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(end_ax_arr[1].value, get_pos_1.value)
        # Get axis 2 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(end_ax_arr[2].value, get_pos_2.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(excepted_err, self.errCde)

    def test_Gp3DArc3P(self):
        excepted_err = 0
        gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(excepted_err, self.errCde)
        # Creat group 0, and set axis 0, 1, 2 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(excepted_err, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(excepted_err, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
        # Set 3D Arc mode
        arc_mode = c_uint(ABS_MODE.MOVE_REL.value)
        # Set 3D Arc CW, with 60 degree
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
        # Set arc movement with 3 point of circular
        self.errCde = self.AdvMot.Acm2_Gp3DArc_3P(gp_id, arc_mode, refArr, endArr, byref(arr_element), dir_mode, cyc_cnt)
        self.assertEqual(excepted_err, self.errCde)
        # Check status
        while self.state.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.test_GetAxState()
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        get_pos_2 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(end_arr[0].value, get_pos_0.value)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(end_arr[1].value, get_pos_1.value)
        # Get axis 2 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
        self.assertEqual(excepted_err, self.errCde)
        self.assertEqual(end_arr[2].value, get_pos_2.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(excepted_err, self.errCde)

def DownloadENISuite():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_LoadENI']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def GetMDevice():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_GetMDevice']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def DeviceOpen():
    tests = ['test_GetAvailableDevs', 'test_DevOpen']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def DeviceClose():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_DevClose']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def ExportMappingTable():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_DevExportMappingTable']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def ImportMappingTable():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_DevImportMappingTable']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def AxPTP_Check():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_ResetAll', 'test_AxPTP', 'test_AxGetPosition']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def DeviceDO():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_SetDeviceDIOProperty', 'test_GetDeviceDIOProperty', 'test_SetDeviceDO_ON']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def GroupCreateCheck():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_RemoveGroup', 'test_CreatGroup', 'test_CheckGroupAxes']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def GetAllError():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_GetLastError_Device', 'test_GetLastError_AXIS', 'test_GetLastError_Group']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def SetAxis0SpeedLimit():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_SetMultiPropertyAndCheck_AxisSpeed', 'test_GetLastError_AXIS']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def SetAxis0SpeedWithProfile():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_SetAxSpeedInfoAndCheck', 'test_GetLastError_AXIS']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def PVTTable():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_PVTTable']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def PTTable():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_PTTable']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def Gear0And1():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_ResetAll', 'test_Gear', 'test_ResetAll']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def Gantry0And1():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_ResetAll', 'test_Gantry', 'test_ResetAll']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def GpMoveLineRel():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_ResetAll', 'test_GpLine', 'test_ResetAll']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def GpMove2DArcCW():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_ResetAll', 'test_2DArc', 'test_ResetAll']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def GpMove2DArcCW3P():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_ResetAll', 'test_2DArc3P', 'test_ResetAll']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def GpMove3DArcCW():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_ResetAll', 'test_3DArcCenter', 'test_ResetAll']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

def GpMove3DArcCW3P():
    tests = ['test_GetAvailableDevs', 'test_Initialize', 'test_ResetAll', 'test_Gp3DArc3P', 'test_ResetAll']
    suite = unittest.TestSuite(map(AdvCmnAPI_Test, tests))
    return suite

if __name__ == '__main__':
    # Test all case without order
    # unittest.main()
    # Test case with self-defined order
    runner = unittest.TextTestRunner()
    # runner.run(DownloadENISuite())
    # runner.run(GetMDevice())
    # runner.run(ExportMappingTable())
    # runner.run(ImportMappingTable())
    # runner.run(AxPTP_Check())
    # runner.run(DeviceDO())
    # runner.run(GroupCreateCheck())
    # runner.run(GetAllError())
    # runner.run(SetAxis0SpeedLimit())
    # runner.run(SetAxis0SpeedWithProfile())
    # runner.run(PVTTable())
    # runner.run(PTTable())
    # runner.run(Gear0And1())
    # runner.run(Gantry0And1())
    # runner.run(GpMoveLineRel())
    # runner.run(GpMove2DArcCW())
    # runner.run(GpMove2DArcCW3P())
    # runner.run(GpMove3DArcCW())
    runner.run(GpMove3DArcCW3P())
    