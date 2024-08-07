import unittest
import time
import os
import numpy as np
import xml.etree.ElementTree as xml
import threading
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.MotionInfo import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2

ax_motion_cnt = c_uint32(0)
@CFUNCTYPE(c_uint32, c_uint32, c_void_p)
def EvtAxMotionDone(axid, reservedParam):
    ax_motion_cnt.value = ax_motion_cnt.value + 1;
    print('[EvtAxMotionDone] AX:{0}, counter:{1}'.format(axid, ax_motion_cnt.value))
    return 0;
@CFUNCTYPE(c_uint32, c_uint32, c_void_p)
def EmptyFunction(val, res):
    return 0;

class TestPCIE1245(unittest.TestCase):
    def setUp(self):
        self.maxAccDev = 10
        self.maxDevList = (DEVLIST*self.maxAccDev)()
        self.maxDev = c_uint32(0)
        self.errCde = c_uint32(ErrorCode2.SUCCESS.value)
        self.exceptedErr = c_uint32(ErrorCode2.SUCCESS.value)
        self.AdvMot = AdvCmnAPI_CM2
        self.axCnt = c_uint32(4)
        self.stateArr = [c_uint32(16) for v in range(self.axCnt.value)]
        self.axisStart = 0
        self.devId = c_uint32(0)
        self.gpid = c_uint32(0)
        self.gpArr = [c_uint32(self.axisStart), c_uint32(self.axisStart + 1)]
        self.transGpArr = (c_uint32 * len(self.gpArr))(*self.gpArr)
    
    def tearDown(self):
        self.errCde = c_uint32(ErrorCode2.SUCCESS.value)
        self.exceptedErr = c_uint32(ErrorCode2.SUCCESS.value)
# Device
    def GetAvailableDevs(self):
        self.errCde = self.AdvMot.Acm2_GetAvailableDevs(self.maxDevList, self.maxAccDev, byref(self.maxDev))
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        print('---Device counts:{0}---'.format(self.maxDev.value))
        for i in range(self.maxDev.value):
            print('[{index}] devNum={devNum:x} devName={devName}'.format(index=i, devNum=self.maxDevList[i].dwDeviceNum,
                                                                          devName=self.maxDevList[i].szDeviceName)) 

    def DevInitialize(self):
        self.errCde = self.AdvMot.Acm2_DevInitialize()
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def ResetAllError(self):
        # Reset axis error
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.errCde = self.AdvMot.Acm2_AxResetError(i)
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Reset All error
        self.errCde = self.AdvMot.Acm2_DevResetAllError()
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
# Axis
    def AxGetMotionState(self):
        axIOStatus = MOTION_IO()
        axState = c_uint32(AXIS_STATE.STA_AX_DISABLE.value)
        axStatusType = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
        print('\naxid state {:11} RDY ALM LMTP LMTN ERC ALRM EMG'.format(''))
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.errCde = self.AdvMot.Acm2_AxGetMotionIO(i, byref(axIOStatus))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
            self.errCde = self.AdvMot.Acm2_AxGetState(i, axStatusType, byref(axState))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
            print('{axid:<4} {ax_state:<17} {RDY:<3} {ALM:<3} {LMTP:<4} {LMTN:<4} {ERC:<3} {ALRM:<4} {EMG:<3}'.format(
                    axid=i, ax_state=AXIS_STATE(axState.value).name, RDY=axIOStatus.RDY, ALM=axIOStatus.ALM, 
                    LMTP=axIOStatus.LMT_P, LMTN=axIOStatus.LMT_N, ERC=axIOStatus.ERC, ALRM=axIOStatus.ALRM, EMG=axIOStatus.EMG))

    def ResetAxIO(self):
        # Set enable
        enablePropertyArr = [PropertyID2.CFG_AxAlmEnable.value, PropertyID2.CFG_AxErcEnableMode.value, PropertyID2.CFG_AxPelEnable.value,
                             PropertyID2.CFG_AxMelEnable.value, PropertyID2.CFG_AxElEnable.value]
        enablePropertyArrU32 = [c_uint32(val) for val in enablePropertyArr]
        transEnableProperty = (c_uint32 * len(enablePropertyArrU32))(*enablePropertyArrU32)
        setEnableArr = [c_double(1) for __ in range(len(enablePropertyArr))]
        transSetEnable = (c_double * len(enablePropertyArr))(*setEnableArr)
        errBuffer = (c_uint32 * len(enablePropertyArr))()
        getValueBuffer = (c_double * len(enablePropertyArr))()
        print('\nSet axis enable:')
        print('axid ALMEN ERCEN PELEN MELEN ELEN')
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.errCde = self.AdvMot.Acm2_SetMultiProperty(i, transEnableProperty, transSetEnable, len(enablePropertyArr), errBuffer)
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
            self.errCde = self.AdvMot.Acm2_GetMultiProperty(i, transEnableProperty, getValueBuffer, len(enablePropertyArr), errBuffer)
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
            print('{axid:<4} {ALMEN:<5} {ERCEN:<5} {PELEN:<5} {MELEN:<5} {ELEN:<4}'.format(
                    axid=i, ALMEN=getValueBuffer[0], ERCEN=getValueBuffer[1],
                    PELEN=getValueBuffer[2], MELEN=getValueBuffer[3], ELEN=getValueBuffer[4]))
        # Set logic
        propertyIDArr = [PropertyID2.CFG_AxAlmLogic.value, PropertyID2.CFG_AxErcLogic.value,
                         PropertyID2.CFG_AxPelLogic.value, PropertyID2.CFG_AxMelLogic.value]
        propertyIDArrInU32 = [c_uint32(val) for val in propertyIDArr]
        transProperty = (c_uint32 * len(propertyIDArrInU32))(*propertyIDArrInU32)
        setValueArr = [c_double(0) for _ in range(len(propertyIDArr))]
        transSetValue = (c_double * len(propertyIDArrInU32))(*setValueArr)
        errBuffer = (c_uint32 * len(propertyIDArrInU32))()
        getValueBuffer = (c_double * len(propertyIDArrInU32))()
        print('\nSet axis logic:')
        print('axid ALM ERC PEL MEL')
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.errCde = self.AdvMot.Acm2_SetMultiProperty(i, transProperty, transSetValue, len(setValueArr), errBuffer)
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
            self.errCde = self.AdvMot.Acm2_GetMultiProperty(i, transProperty, getValueBuffer, len(setValueArr), errBuffer)
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
            print('{axid:<4} {ALM:<3} {ERC:<3} {PEL:<3} {MEL:<3}'.format(
                    axid=i, ALM=getValueBuffer[0], ERC=getValueBuffer[1],
                    PEL=getValueBuffer[2], MEL=getValueBuffer[3]))
        emgLogicArr = [PropertyID2.CFG_DevEmgLogic.value]
        emgLogicArrInU32 = [c_uint32(va) for va in emgLogicArr]
        transEMGLogic = (c_uint32 * len(emgLogicArr))(*emgLogicArrInU32)
        setEMGLogicArr = [c_double(0) for x in range(len(emgLogicArrInU32))]
        transSetEMGLogic = (c_double * len(emgLogicArr))(*setEMGLogicArr)
        errBuffer = (c_uint32 * len(setEMGLogicArr))()
        getValueBuffer = (c_double * len(setEMGLogicArr))()
        self.errCde = self.AdvMot.Acm2_SetMultiProperty(self.devId, transEMGLogic, transSetEMGLogic, len(emgLogicArr), errBuffer)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        self.errCde = self.AdvMot.Acm2_GetMultiProperty(self.devId, transEMGLogic, getValueBuffer, len(emgLogicArr), errBuffer)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        print('EMG:{EMG:<3}'.format(EMG=getValueBuffer[0]))
    
    def ResetStatusAndCounter(self):
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        pos = c_double(0)
        state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
        # Check axis status
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            state = c_uint32(16)
            self.AdvMot.Acm2_AxGetState(i, state_type, byref(state))
            while state.value != AXIS_STATE.STA_AX_READY.value:
                if (state.value == AXIS_STATE.STA_AX_ERROR_STOP.value):
                    break
                time.sleep(0.5) # sleep for 0.5 second
                self.AdvMot.Acm2_AxGetState(i, state_type, byref(state))
        # Clear all
        self.errCde = self.AdvMot.Acm2_DevResetAllError()
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Set axis command position as 0
        for j in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.errCde = self.AdvMot.Acm2_AxSetPosition(j, pos_type, pos)
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def test_AxPTP(self):
        abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
        distance = c_double(1000)
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.errCde = self.AdvMot.Acm2_AxPTP(i, abs_mode, distance)
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def AxMoveContinue(self):
        axDir = c_uint(MOTION_DIRECTION.DIRECTION_POS.value)
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.errCde = self.AdvMot.Acm2_AxMoveContinue(i, axDir)
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        time.sleep(2)
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            axArr = [i]
            transAxArr = (c_uint32 * len(axArr))(*axArr)
            stopMode = c_uint(MOTION_STOP_MODE.MOTION_STOP_MODE_DEC.value)
            newDec = c_double(8000)
            self.errCde = self.AdvMot.Acm2_AxMotionStop(transAxArr, len(axArr), stopMode, newDec)
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def test_GetAxState(self):
        state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.AdvMot.Acm2_AxGetState(i, state_type, byref(self.stateArr[i]))
            if (self.stateArr[i].value != AXIS_STATE.STA_AX_READY.value):
                print('axis[{0}]Not Ready'.format(i))

    def test_AxGetPosition(self):
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        pos = c_double(0)
        # Check status
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            while self.state.value != AXIS_STATE.STA_AX_READY.value:
                time.sleep(1)
                self.test_GetAxState()
            self.errCde = self.AdvMot.Acm2_AxGetPosition(i, pos_type, byref(pos))
            excepted_pos = c_double(1000)
            self.assertEqual(self.exceptedErr.value, self.errCde)
            self.assertEqual(excepted_pos.value, pos.value, '{0} failed.'.format(self._testMethodName))

    def test_SetAxSpeedInfoAndCheck(self):
        speed_info = SPEED_PROFILE_PRM()
        speed_info.FH = c_double(3000)
        speed_info.FL = c_double(1500)
        speed_info.Acc = c_double(11000)
        speed_info.Dec = c_double(9900)
        speed_info.JerkFac = c_double(0)
        # Set speed information
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.errCde = self.AdvMot.Acm2_AxSetSpeedProfile(i, speed_info)
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get speed information
        speedArr = [PropertyID2.PAR_AxVelHigh.value, PropertyID2.PAR_AxVelLow.value,
                    PropertyID2.PAR_AxAcc.value, PropertyID2.PAR_AxDec.value]
        speedArrInU32 = [c_uint32(val) for val in speedArr]
        tranSpeedArr = (c_uint32 * len(speedArr))(*speedArrInU32)
        getValArr = (c_double * len(speedArrInU32))()
        errBuffer = (c_uint32 * len(speedArrInU32))()
        print('\naxid FH{:4} FL{:4} Acc{:4} Dec{:4}'.format('','','',''))
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.errCde = self.AdvMot.Acm2_GetMultiProperty(i, tranSpeedArr, getValArr, len(speedArrInU32), errBuffer)
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
            print('{axid:<4} {FH:<6} {FL:<6} {Acc:<7} {Dec:<6}'.format(axid=i, FH=getValArr[0], FL=getValArr[1],
                                                                       Acc=getValArr[2], Dec=getValArr[3]))

    def test_PVTTable(self):
        # Reset PVT table
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.errCde = self.AdvMot.Acm2_AxResetPVTTable(i)
            self.assertEqual(self.exceptedErr.value, self.errCde)
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
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.errCde = self.AdvMot.Acm2_AxLoadPVTTable(i, posArr, velArr, timeArr, len(pos_arr))
            self.assertEqual(self.exceptedErr.value, self.errCde)
            # Set PVT
            self.errCde = self.AdvMot.Acm2_AxMovePVT(i)
            self.assertEqual(self.exceptedErr.value, self.errCde)
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
            get_pos = c_double(0)
            while self.stateArr[i].value != AXIS_STATE.STA_AX_READY.value:
                time.sleep(1)
                self.test_GetAxState()
            self.errCde = self.AdvMot.Acm2_AxGetPosition(i, pos_type, byref(get_pos))
            self.assertEqual(self.exceptedErr.value, self.errCde)
            self.assertEqual(c_double(30000).value, get_pos.value, '{0} failed.'.format(self._testMethodName))

    def test_PTTable(self):
        # Reset PT table
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.errCde = self.AdvMot.Acm2_AxResetPTData(i)
            self.assertEqual(self.exceptedErr.value, self.errCde)
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
            for j in range(self.axisStart, (self.axisStart + self.axCnt.value)):
                self.errCde = self.AdvMot.Acm2_AxAddPTData(j, pos_arr[i], time_arr[i])
                self.assertEqual(self.exceptedErr.value, self.errCde)
        # Start move PT table
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            self.errCde = self.AdvMot.Acm2_AxMovePT(i)
            self.assertEqual(self.exceptedErr.value, self.errCde)

        # Check status
        for i in range(self.axisStart, (self.axisStart + self.axCnt.value)):
            pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
            get_pos = c_double(0)
            while self.stateArr[i].value != AXIS_STATE.STA_AX_READY.value:
                time.sleep(1)
                self.test_GetAxState()
            # Get axis 0 position
            self.errCde = self.AdvMot.Acm2_AxGetPosition(i, pos_type, byref(get_pos))
            self.assertEqual(self.exceptedErr.value, self.errCde)
            self.assertEqual(c_double(30000).value, get_pos.value, '{0} failed.'.format(self._testMethodName))

    def Gear(self):
        primary_ax = c_uint32(self.axisStart)
        follow_ax = c_uint32(self.axisStart + 1)
        primartAxState = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Reset following axis
        self.errCde = self.AdvMot.Acm2_AxSyncOut(follow_ax)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        gear_param = GEAR_IN_PRM()
        # Position type as command position
        gear_param.RefSrc = c_uint32(POSITION_TYPE.POSITION_CMD.value)
        # Mode as relative mode
        gear_param.Mode = c_uint32(ABS_MODE.MOVE_REL.value)
        # Set gear ratio
        gear_param.GearPosition = c_double(0)
        gear_param.GearRatioRate.Num = c_double(1)
        gear_param.GearRatioRate.Den = c_double(1)
        # Set gear
        self.errCde = self.AdvMot.Acm2_AxGearIn(primary_ax, follow_ax, gear_param)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Move primary axis
        abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
        distance = c_double(10000)
        self.errCde = self.AdvMot.Acm2_AxPTP(primary_ax, abs_mode, distance)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Check status
        while primartAxState.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(primary_ax, c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(primartAxState))
            self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 (primary) position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(primary_ax, pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(distance.value, get_pos_0.value)
        # Get axis 1 (following) position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(follow_ax, pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(distance.value, get_pos_1.value)
        # Reset following axis
        self.errCde = self.AdvMot.Acm2_AxSyncOut(follow_ax)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def Gantry(self):
        primary_ax = c_uint32(0)
        primartAxState = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        follow_ax = c_uint32(1)
        # Reset following axis
        self.errCde = self.AdvMot.Acm2_AxSyncOut(follow_ax)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Set gantry parameter
        gantry_param = GANTRY_IN_PRM()
        # Set gantry reference source as command position
        gantry_param.RefSrc = c_int16(POSITION_TYPE.POSITION_CMD.value)
        # Set gantry direction as positive
        gantry_param.Direction = c_int16(MOTION_DIRECTION.DIRECTION_POS.value)
        # Set gantry
        self.errCde = self.AdvMot.Acm2_AxGantryIn(primary_ax, follow_ax, gantry_param)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Move primary axis
        abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
        distance = c_double(10000)
        self.errCde = self.AdvMot.Acm2_AxPTP(primary_ax, abs_mode, distance)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Check status
        while primartAxState.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(primary_ax, c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(primartAxState))
            self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 (primary) position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(primary_ax, pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(distance.value, get_pos_0.value)
        # Get axis 1 (following) position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(follow_ax, pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(distance.value, get_pos_1.value)
        # Reset following axis
        self.errCde = self.AdvMot.Acm2_AxSyncOut(follow_ax)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
# Group
    def CreateGroupAndCheck(self):
        self.errCde = self.AdvMot.Acm2_GpCreate(self.gpid, self.transGpArr, len(self.transGpArr))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(self.gpid, get_axes, len_get)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(self.transGpArr[idx], get_axes[idx], '{0} failed.'.format(self._testMethodName))

    def ResetGroup(self):
        remove_all_axes = c_uint32(0)
        self.errCde = self.AdvMot.Acm2_GpCreate(self.gpid, self.transGpArr, remove_all_axes)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def GpLine(self):
        # Set group move as relative
        gp_move_mode = c_uint(GP_LINE_MODE.LINE_REL.value)
        # Set group end position: axis(0) = 10000, axis(1) = 10000
        end_pos_arr = [c_double(10000), c_double(10000)]
        arr_element = c_uint32(len(end_pos_arr))
        end_arr = (c_double * len(end_pos_arr))(*end_pos_arr)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Group 0 move line
        self.errCde = self.AdvMot.Acm2_GpLine(self.gpid, gp_move_mode, end_arr, byref(arr_element))
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 (primary) position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(self.gpArr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(end_pos_arr[0].value, get_pos_0.value)
        # Get axis 1 (following) position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(self.gpArr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(end_pos_arr[1].value, get_pos_1.value)

    def Gp2DArc(self):
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
        self.errCde = self.AdvMot.Acm2_GpArc_Center(self.gpid, arc_mode, center_arr, end_arr, byref(arr_element), dir_mode)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(self.gpArr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(end_ax_arr[0].value, get_pos_0.value)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(self.gpArr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(end_ax_arr[1].value, get_pos_1.value)

    def Gp2DArc3P(self):
        # Set 2D Arc mode as relative, which the starting point of circular is (0, 0)
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
        self.errCde = self.AdvMot.Acm2_GpArc_3P(self.gpid, arc_mode, refArr, endArr, byref(arr_element), dir_mode)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(self.gpArr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(end_arr[0].value, get_pos_0.value)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(self.gpArr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(end_arr[1].value, get_pos_1.value)
    
    def Gp2DArcAngle(self):
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
        self.errCde = self.AdvMot.Acm2_GpArc_Angle(self.gpid, arc_mode, centerArr, byref(arr_element), degree, dir_mode)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(self.gpArr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual((round(center_arr[0].value - (center_arr[0].value * (2 ** 0.5)))), get_pos_0.value)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(self.gpArr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(center_arr[1].value, get_pos_1.value)

    def Gp3DArcCenter(self):
        gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Creat group 0, and set axis 0, 1, 2 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
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
        # Set direction as CW
        dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
        self.errCde = self.AdvMot.Acm2_Gp3DArc_Center(gp_id, arc_mode, center_arr, end_arr, byref(arr_element), dir_mode)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        get_pos_2 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(end_ax_arr[0].value, get_pos_0.value)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(end_ax_arr[1].value, get_pos_1.value)
        # Get axis 2 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(end_ax_arr[2].value, get_pos_2.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def Gp3DArcNormVec(self):
        gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Creat group 0, and set axis 0, 1, 2 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
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
        self.errCde = self.AdvMot.Acm2_Gp3DArc_NormVec(gp_id, arc_mode, centerArr, normVecArr, byref(arr_element), angle, dir_mode)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        get_pos_2 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 2 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(arc_end_arr[0].value, get_pos_0.value)
        self.assertEqual(arc_end_arr[1].value, get_pos_1.value)
        self.assertEqual(arc_end_arr[2].value, get_pos_2.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def Gp3DArc3P(self):
        gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Creat group 0, and set axis 0, 1, 2 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
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
        # Set arc movement with 3 point of circular
        self.errCde = self.AdvMot.Acm2_Gp3DArc_3P(gp_id, arc_mode, refArr, endArr, byref(arr_element), dir_mode, cyc_cnt)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        get_pos_2 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(end_arr[0].value, get_pos_0.value)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(end_arr[1].value, get_pos_1.value)
        # Get axis 2 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(end_arr[2].value, get_pos_2.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def Gp3DArcAngle(self):
        gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Creat group 0, and set axis 0, 1, 2 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
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
        self.errCde = self.AdvMot.Acm2_Gp3DArc_3PAngle(gp_id, arc_mode, refArr, endArr, byref(arr_element), degree, dir_mode)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        get_pos_2 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 2 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Check value
        self.assertEqual(end_arr[0].value, get_pos_0.value)
        self.assertEqual(end_arr[1].value, get_pos_1.value)
        self.assertEqual(end_arr[2].value, get_pos_2.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def GpHelixCenter(self):
        gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Creat group 0, and set axis 0, 1, 2 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
        # Set mode as relative
        helix_mode = c_uint(ABS_MODE.MOVE_REL.value)
        # Set center as (10000, 0, 0)
        center_arr = [c_double(8000), c_double(0), c_double(0)]
        centerArr = (c_double * len(center_arr))(*center_arr)
        # Set end position as (20000, 0, 20000)
        end_arr = [c_double(16000), c_double(0), c_double(10000)]
        endArr = (c_double * len(end_arr))(*end_arr)
        arr_element = c_uint32(len(end_arr))
        # Set direction as CW
        dir_mode = c_uint(ARC_DIRECTION.ARC_CW.value)
        # Set Helix movement
        self.errCde = self.AdvMot.Acm2_GpHelix_Center(gp_id, helix_mode, centerArr, endArr, byref(arr_element), dir_mode)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        get_pos_2 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 2 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Check value
        self.assertEqual(end_arr[0].value, get_pos_0.value)
        self.assertEqual(end_arr[1].value, get_pos_1.value)
        self.assertEqual(end_arr[2].value, get_pos_2.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def GpHelix3P(self):
        gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Creat group 0, and set axis 0, 1, 2 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
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
        self.errCde = self.AdvMot.Acm2_GpHelix_3P(gp_id, helix_mode, centerArr, endArr, byref(arr_element), dir_mode)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        get_pos_2 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 2 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Check value
        self.assertEqual(end_arr[0].value, get_pos_0.value)
        self.assertEqual(end_arr[1].value, get_pos_1.value)
        self.assertEqual(end_arr[2].value, get_pos_2.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def GpHelixAngle(self):
        gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Creat group 0, and set axis 0, 1, 2 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
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
        self.errCde = self.AdvMot.Acm2_GpHelix_Angle(gp_id, helix_mode, centerArr, endArr, byref(arr_element), dir_mode)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        get_pos_2 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 2 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Check value
        self.assertEqual(end_arr[2].value, get_pos_2.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def GpLineStopAndResume(self):
        gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Creat group 0, and set axis 0, 1, 2 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
        # Set mode as relative
        move_mode = c_uint(GP_LINE_MODE.LINE_REL.value)
        end_arr = [c_double(20000), c_double(20000), c_double(20000)]
        endArr = (c_double * len(end_arr))(*end_arr)
        arr_element = c_uint32(len(end_arr))
        self.errCde = self.AdvMot.Acm2_GpLine(gp_id, move_mode, endArr, arr_element)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Pause movement
        self.errCde = self.AdvMot.Acm2_GpPause(gp_id)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        get_pos_2 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 2 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Check value: Not equal to target position
        self.assertNotEqual(end_arr[0].value, get_pos_0.value)
        self.assertNotEqual(end_arr[1].value, get_pos_1.value)
        self.assertNotEqual(end_arr[2].value, get_pos_2.value)
        # Resume movement
        self.errCde = self.AdvMot.Acm2_GpResume(gp_id)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        get_pos_2 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 2 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Check value: Equal to target position
        self.assertEqual(end_arr[0].value, get_pos_0.value)
        self.assertEqual(end_arr[1].value, get_pos_1.value)
        self.assertEqual(end_arr[2].value, get_pos_2.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def GpStop(self):
        gp_ax_arr = [c_uint32(0), c_uint32(1), c_uint32(2)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Creat group 0, and set axis 0, 1, 2 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
        # Set mode as relative
        move_mode = c_uint(GP_LINE_MODE.LINE_REL.value)
        end_arr = [c_double(200000), c_double(200000), c_double(200000)]
        endArr = (c_double * len(end_arr))(*end_arr)
        arr_element = c_uint32(len(end_arr))
        self.errCde = self.AdvMot.Acm2_GpLine(gp_id, move_mode, endArr, arr_element)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Check group status
        time.sleep(2)
        gp_state = c_uint32(0)
        self.errCde = self.AdvMot.Acm2_GpGetState(gp_id, byref(gp_state))
        print('gp_state:0x{0:x}'.format(gp_state.value))
        # Change velocity
        new_vel = c_double(5000)
        new_acc = c_double(9000)
        new_dec = c_double(4000)
        self.errCde = self.AdvMot.Acm2_GpChangeVel(gp_id, new_vel, new_acc, new_dec)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        vel_type = c_uint(VELOCITY_TYPE.VELOCITY_CMD.value)
        get_gp_vel = c_double(0)
        time.sleep(2)
        self.errCde = self.AdvMot.Acm2_GpGetVel(gp_id, vel_type, byref(get_gp_vel))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        self.assertEqual(new_vel.value, get_gp_vel.value)
        print('gp vel:{0}'.format(get_gp_vel.value))
        # Set stop mode as deceleration to stop
        stop_mode = c_uint(MOTION_STOP_MODE.MOTION_STOP_MODE_DEC.value)
        self.errCde = self.AdvMot.Acm2_GpMotionStop(gp_id, stop_mode, new_dec)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        get_pos_2 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 2 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[2], pos_type, byref(get_pos_2))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Check value: Not equal to target position
        self.assertNotEqual(end_arr[0].value, get_pos_0.value)
        self.assertNotEqual(end_arr[1].value, get_pos_1.value)
        self.assertNotEqual(end_arr[2].value, get_pos_2.value)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def GpAddPath(self):
        gp_ax_arr = [c_uint32(0), c_uint32(1)]
        gp_id = c_uint32(0)
        gp_arr = (c_uint32 * len(gp_ax_arr))(*gp_ax_arr)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Creat group 0, and set axis 0, 1 into group
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, len(gp_arr))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # get_axes size must be same as len_get
        len_get = c_uint32(64)
        get_axes = (c_uint32 * len_get.value)()
        # Get axes in group 0 and check
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gp_id, get_axes, len_get)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        for idx in range(len_get.value):
            self.assertEqual(gp_arr[idx], get_axes[idx])
        # Reset group path
        self.errCde = self.AdvMot.Acm2_GpResetPath(gp_id)
        self.assertEqual(self.exceptedErr.value, self.errCde)
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
        for i in range(1):
            endArr = (c_double * len(end_arr[i]))(*end_arr[i])
            centerArr = (c_double * len(center_arr[i]))(*center_arr[i])
            self.errCde = self.AdvMot.Acm2_GpAddPath(gp_id, move_cmd_arr[i], move_mode, fh[i], fl[i], acc[i], dec[i], endArr, centerArr, arr_element)
            self.assertEqual(gp_arr[idx], get_axes[idx])
        # Start move path
        self.errCde = self.AdvMot.Acm2_GpMovePath(gp_id)
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(c_uint32(self.axisStart), c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        # Get axis 0 position
        get_pos_0 = c_double(0)
        get_pos_1 = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        # Get axis 0 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[0], pos_type, byref(get_pos_0))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Get axis 1 position
        self.errCde = self.AdvMot.Acm2_AxGetPosition(gp_ax_arr[1], pos_type, byref(get_pos_1))
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Check value: Equal to target position
        self.assertEqual(end_arr[0][0].value, get_pos_0.value)
        self.assertEqual(end_arr[0][1].value, get_pos_1.value)
        # Reset group path
        self.errCde = self.AdvMot.Acm2_GpResetPath(gp_id)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Reset all axes from group 0
        self.errCde = self.AdvMot.Acm2_GpCreate(gp_id, gp_arr, 0)
        self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))

    def AxMotionDoneEvent(self):
        ax_id = c_uint32(0)
        ax_motion_cnt.value = 0
        # Set callback function, enable event
        self.errCde = self.AdvMot.Acm2_EnableCallBackFuncForOneEvent(ax_id, c_int(ADV_EVENT_SUBSCRIBE.AXIS_MOTION_DONE.value), EvtAxMotionDone)
        self.assertEqual(self.exceptedErr.value, self.errCde)
        # Move
        self.test_AxPTP()
        ax0State = c_uint32(AXIS_STATE.STA_AX_EXT_JOG_READY.value + 1)
        # Check status
        while ax0State.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(ax_id, c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value), byref(ax0State))
            self.assertEqual(self.exceptedErr.value, self.errCde, '{0} failed.'.format(self._testMethodName))
        print('AX:{0} is done, event cnt is:{1}'.format(ax_id.value, ax_motion_cnt.value))
        # Remove callback function, disable event
        self.errCde = self.AdvMot.Acm2_EnableCallBackFuncForOneEvent(ax_id, c_int(ADV_EVENT_SUBSCRIBE.EVENT_DISABLE.value), EmptyFunction)
        self.assertEqual(self.exceptedErr.value, self.errCde)

def JustGetAvailableDevices():
    tests = ['GetAvailableDevs']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def InitialDevice():
    tests = ['GetAvailableDevs', 'DevInitialize']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def GetAllAxesStatus():
    tests = ['GetAvailableDevs', 'DevInitialize', 'AxGetMotionState']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def ResetAllAxesALMLogic():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetAxIO', 'AxGetMotionState', 'ResetStatusAndCounter']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def AxisPTPAndCheck():
    tests = ['GetAvailableDevs', 'DevInitialize', 'test_AxPTP', 'test_AxGetPosition', 'ResetStatusAndCounter']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def AxisSetSpeedAndCheck():
    tests = ['GetAvailableDevs', 'DevInitialize', 'test_SetAxSpeedInfoAndCheck']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def AxisPVTTable():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'test_PVTTable']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def AxisPTTable():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'test_PTTable']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def AxisContiMoveAndStop():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'AxMoveContinue', 'ResetStatusAndCounter', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def AxisGear0And1():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'Gear', 'ResetStatusAndCounter', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def AxisGantry0And1():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'Gantry', 'ResetStatusAndCounter', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def AxisMotionDoneEvent():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'AxMotionDoneEvent', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def CreateGroupAndCheck():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'CreateGroupAndCheck', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def GroupLine():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'CreateGroupAndCheck', 'GpLine', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def Group2DArc():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'CreateGroupAndCheck', 'Gp2DArc', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def Group2DArc3P():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'CreateGroupAndCheck', 'Gp2DArc3P', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def Group2DArcAngle():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'CreateGroupAndCheck', 'Gp2DArcAngle', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def Group3DArcCenter():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'Gp3DArcCenter', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def Group3DArcNormVec():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'Gp3DArcNormVec', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def Group3DArc3P():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'Gp3DArc3P', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def Group3DArcAngle():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'Gp3DArcAngle', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def GroupHelixCenter():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'GpHelixCenter', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def GroupHelix3P():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'GpHelix3P', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def GroupHelixAngle():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'GpHelixAngle', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def GroupLineStopAndResume():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'GpLineStopAndResume', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def GroupStop():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'GpStop', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite
def GroupAddPathAndMove():
    tests = ['GetAvailableDevs', 'DevInitialize', 'ResetStatusAndCounter', 'ResetAllError',
             'GpAddPath', 'ResetGroup', 'ResetAllError']
    suite = unittest.TestSuite(map(TestPCIE1245, tests))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    get_available_devs = runner.run(JustGetAvailableDevices())
    initialize = runner.run(InitialDevice())
    get_all_axes_status = runner.run(GetAllAxesStatus())
    reset_all_axes_alm_logic = runner.run(ResetAllAxesALMLogic())
    axis_set_speed_and_check = runner.run(AxisSetSpeedAndCheck())
    axis_ptp_and_check = runner.run(AxisPTPAndCheck())
    axis_pvt_table = runner.run(AxisPVTTable())
    axis_pt_table = runner.run(AxisPTTable())
    axis_conti_move = runner.run(AxisContiMoveAndStop())
    axis_gear_0_1 = runner.run(AxisGear0And1())
    axis_gantry_0_1 = runner.run(AxisGantry0And1())
    axis_motion_done_event = runner.run(AxisMotionDoneEvent())
    create_gp_and_check = runner.run(CreateGroupAndCheck())
    group_line = runner.run(GroupLine())
    group_2DArc = runner.run(Group2DArc())
    group_2DArc3P = runner.run(Group2DArc3P())
    group_2DArcAndgle = runner.run(Group2DArcAngle())
    group_3DArcCenter = runner.run(Group3DArcCenter())
    group_3DArcNormVec = runner.run(Group3DArcNormVec())
    group_3DArc3P = runner.run(Group3DArc3P())
    group_3DArcAngle = runner.run(Group3DArcAngle())
    group_helixCenter = runner.run(GroupHelixCenter())
    group_helix3P = runner.run(GroupHelix3P())
    group_helixAngle = runner.run(GroupHelixAngle())
    group_lineStopAndResume = runner.run(GroupLineStopAndResume())
    group_stop = runner.run(GroupStop())
    group_add_path_move = runner.run(GroupAddPathAndMove())
