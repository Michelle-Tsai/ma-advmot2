import unittest
import os
import sys
import time

# 強制 Windows 使用 ANSI 支援
os.system('')
# # 強制設定 stdout 編碼為 utf-8
sys.stdout.reconfigure(encoding='utf-8')

from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.MotionInfo import *
from AcmP.AdvMotPropID_CM2 import PropertyID, PropertyGpID
from AcmP.AdvMotErr_CM2 import ErrorCode
from colorama import init, Fore

global_link_type = 0
global_run_swcmpch = 1
global_open_axcnt = 1
global_use_buffer_api = False
global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
init(autoreset=True, strip=False)

class SWCmp_TestCM1(unittest.TestCase):
    def setUp(self):
        self.errCde = 0
        self.except_err = c_uint32(ErrorCode.SUCCESS.value)
    # Call once by test case
    @classmethod
    def setUpClass(cls):
        global global_open_axcnt
        cls.AdvMot = AdvCmnAPI
        cls.AdvPpt = PropertyID
        cls.AdvGpPpt = PropertyGpID
        cls.maxDevCnt = 10
        cls.maxDevList = (DEVLIST * cls.maxDevCnt)()
        cls.maxDev = c_uint32(0)
        cls.devNum = c_uint32(0)
        cls.devHandle = c_void_p()
        cls.axHandArr = [c_void_p() for _ in range(64)]
        cls.openAxCnt = global_open_axcnt
        cls.gpHandle = c_void_p()
    def tearDown(self):
        self.errCde = 0

    def _PrintResult(self, isPass, message):
        if isPass:
            print(f'{Fore.GREEN}[✓ Pass]{message}')
        else:
            print(f'{Fore.RED}[X Fail]{message}')

    def initial(self):
        self.errCde = self.AdvMot.Acm_GetAvailableDevs(self.maxDevList, self.maxDevCnt, byref(self.maxDev))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Acm_GetAvailableDevs failed:{self.errCde:x}')
            self.assertSetEqual(self.except_err.value, self.errCde, f'Acm_GetAvailableDevs failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Acm_GetAvailableDevs successed')
            for i in range(self.maxDev.value):
                print(f'{Fore.LIGHTBLUE_EX}Device number:{self.maxDevList[i].dwDeviceNum:x}')
            if self.maxDev.value > 0:
                self.devNum.value = self.maxDevList[0].dwDeviceNum
        self.errCde = self.AdvMot.Acm_DevOpen(self.devNum, byref(self.devHandle))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Device open failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Device open failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Device open successed')
        for axid in range(self.openAxCnt):
            self.errCde = self.AdvMot.Acm_AxOpen(self.devHandle, axid, byref(self.axHandArr[axid]))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Axis:{axid} open failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Axis:{axid} open failed:{self.errCde:x}')
            # else:
            #     self._PrintResult(True, f'Axis:{axid} open successed')

    def closeAll(self):
        for axid in range(self.openAxCnt):
            self.errCde = self.AdvMot.Acm_AxClose(self.axHandArr[axid])
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Axis:{axid} close failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Axis:{axid} close failed:{self.errCde:x}')
            # else:
            #     self._PrintResult(True, f'Close axis:{axid} successed')
        self.errCde = self.AdvMot.Acm_DevClose(byref(self.devHandle))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Device close failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Device close failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Device close successed')

    def _ClearLinkedDo(self, SWCmpChId):
        clearVal = c_uint32(0xFFFFFFFF)
        getLinkedDo = c_uint32(0)
        # 清除軟體比較觸發通道綁定的Do
        self.errCde = self.AdvMot.Acm_DaqDoLinkSWCmpObject(self.devHandle, clearVal, SWCmpChId)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Clear SWCmp:{SWCmpChId.value}, Acm_DaqDoLinkSWCmpObject failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Clear SWCmp:{SWCmpChId.value}, Acm_DaqDoLinkSWCmpObject failed:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm_DaqDoGetLinkedSWCmpObject(self.devHandle, byref(getLinkedDo), SWCmpChId)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'SWCmpCh:{SWCmpChId.value} Acm_DaqDoGetLinkedSWCmpObject failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'SWCmpCh:{SWCmpChId.value} Acm_DaqDoGetLinkedSWCmpObject failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Clear SWCmpCh:{SWCmpChId.value} linked DoCh:{getLinkedDo.value} successed')

    def _LinkedDo(self, SWCmpChId, DoChId):
        getLinkedDo = c_uint32(0)
        self.errCde = self.AdvMot.Acm_DaqDoLinkSWCmpObject(self.devHandle, DoChId, SWCmpChId)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Set SWCmpCh:{SWCmpChId.value} failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Set SWCmpCh:{SWCmpChId.value} failed:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm_DaqDoGetLinkedSWCmpObject(self.devHandle, byref(getLinkedDo), SWCmpChId)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Get SWCmpCh:{SWCmpChId.value} failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Get SWCmpCh:{SWCmpChId.value} failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'SWCmpCh:{SWCmpChId.value} linked DoCh:{getLinkedDo.value} successed')

    def _ClearLinkedObj(self, SWCmpChId, objType, linkedArr):
        getLinkedCnt = c_uint32(10)
        getLinkedArr = (c_uint32 * getLinkedCnt.value)()
        getLinkedObj = c_uint(0)
        transArr = (c_uint32 * len(linkedArr))(*linkedArr)
        # 清除軟體比較觸發通道綁定的 Axis/Counter
        self.errCde = self.AdvMot.Acm_ChLinkSWCmpObject(self.devHandle, SWCmpChId, objType.value, transArr, c_uint32(0))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Clear SWCmpCh:{SWCmpChId.value} link {objType.name} failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Clear SWCmpCh:{SWCmpChId.value} link {objType.name} failed:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm_ChGetLinkedSWCmpObject(self.devHandle, SWCmpChId, byref(getLinkedObj), getLinkedArr, byref(getLinkedCnt))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Get SWCmpCh:{SWCmpChId.value} linked failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Get SWCmpCh:{SWCmpChId.value} linked failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Clear SWCmpCh:{SWCmpChId.value} linked {ADV_OBJ_TYPE(getLinkedObj.value).name} successed')

    def _LinkedObj(self, SWCmpChId, objType, linkedArr):
        getLinkedCnt = c_uint32(10)
        getLinkedArr = (c_uint32 * getLinkedCnt.value)()
        getLinkedObj = c_uint(0)
        transArr = (c_uint32 * len(linkedArr))(*linkedArr)
        # 綁定軟體比較觸發通道的 Axis/Counter
        self.errCde = self.AdvMot.Acm_ChLinkSWCmpObject(self.devHandle, SWCmpChId, objType.value, transArr, len(linkedArr))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'SWCmpCh:{SWCmpChId.value} link {objType.name} failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'SWCmpCh:{SWCmpChId.value} link {objType.name} failed:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm_ChGetLinkedSWCmpObject(self.devHandle, SWCmpChId, byref(getLinkedObj), getLinkedArr, byref(getLinkedCnt))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Get SWCmpCh:{SWCmpChId.value} linked failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Get SWCmpCh:{SWCmpChId.value} linked failed:{self.errCde:x}')
        else:
            for i in range(getLinkedCnt.value):
                self._PrintResult(True, f'SWCmpCh:{SWCmpChId.value} linked {ADV_OBJ_TYPE(getLinkedObj.value).name}:{getLinkedArr[i]} successed')

    def _SetPropertyBound(self, SWCmpChId, ppt, setVal, errorCode):
        getVal = c_double(0)
        swcmp = c_uint32(SWCmpChId.value)
        self.errCde = self.AdvMot.Acm_SetChannelProperty(self.devHandle, swcmp, ppt, setVal)
        if self.errCde != errorCode:
            self._PrintResult(False, f'Set {self.AdvPpt(ppt.value).name} value:{self.errCde:x}')
            self.assertEqual(errorCode, self.errCde, f'Set {self.AdvPpt(ppt.value).name} value:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm_GetChannelProperty(self.devHandle, swcmp, ppt, byref(getVal))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Get {self.AdvPpt(ppt.value).name} failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Get {self.AdvPpt(ppt.value).name} failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value}, get:{getVal.value}')

    def _SetChProperty(self, SWCmpChId, ppt, setVal):
        getVal = c_double(0)
        swcmp = c_uint32(SWCmpChId.value)
        self.errCde = self.AdvMot.Acm_SetChannelProperty(self.devHandle, swcmp, ppt, setVal)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Set {self.AdvPpt(ppt.value).name} failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Set {self.AdvPpt(ppt.value).name} failed:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm_GetChannelProperty(self.devHandle, swcmp, ppt, byref(getVal))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Get {self.AdvPpt(ppt.value).name} failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Get {self.AdvPpt(ppt.value).name} failed:{self.errCde:x}')
        if getVal.value != setVal.value:
            self._PrintResult(False, f'Set {self.AdvPpt(ppt.value).name} failed, set:{setVal.value} get:{getVal.value}')
            self.assertEqual(setVal.value, getVal.value, f'Set {self.AdvPpt(ppt.value).name} failed, set:{setVal.value} get:{getVal.value}')
        else:
            self._PrintResult(True, f'Set {self.AdvPpt(ppt.value).name} value:{getVal.value} successed')

    def _SetProperty(self, ppt, setVal, id, hType):
        getVal = c_uint32(0)
        if hType == ADV_HANDLE_TYPE.HdType_Axis.value:
            self.errCde = self.AdvMot.Acm_SetU32Property(self.axHandArr[id.value], ppt, setVal)
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Set {self.AdvPpt(ppt.value).name} failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Set {self.AdvPpt(ppt.value).name} failed:{self.errCde:x}')
            self.errCde = self.AdvMot.Acm_GetU32Property(self.axHandArr[id.value], ppt, byref(getVal))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get {self.AdvPpt(ppt.value).name} failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get {self.AdvPpt(ppt.value).name} failed:{self.errCde:x}')
            if getVal.value != setVal.value:
                self._PrintResult(False, f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value}, but get:{getVal.value}')
                self.assertEqual(setVal.value, getVal.value, f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value}, but get:{getVal.value}')
            else:
                self._PrintResult(True, f'Set {self.AdvPpt(ppt.value).name} value:{getVal.value}successed')

    def _ResetAxis(self, axid, posType):
        setPos = c_double(0)
        getPos = c_double(0)
        self.errCde = self.AdvMot.Acm_AxResetError(self.axHandArr[axid.value])
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Ax:{axid.value} reset error failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Ax:{axid.value} reset error failed:{self.errCde:x}')
        if posType.value == POSITION_TYPE.POSITION_CMD.value:
            self.errCde = self.AdvMot.Acm_AxSetCmdPosition(self.axHandArr[axid.value], setPos)
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Reset ax:{axid.value} {POSITION_TYPE(posType.value).name} position failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Reset ax:{axid.value} {POSITION_TYPE(posType.value).name} position failed:{self.errCde:x}')
            self.errCde = self.AdvMot.Acm_AxGetCmdPosition(self.axHandArr[axid.value], byref(getPos))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get ax:{axid.value} position failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get ax:{axid.value} {POSITION_TYPE(posType.value).name} position failed:{self.errCde:x}')
            if getPos.value != setPos.value:
                self._PrintResult(False, f'Reset ax:{axid.value} position failed:{self.errCde:x}')
                self.assertEqual(setPos.value, getPos.value, f'Reset ax:{axid.value} {POSITION_TYPE(posType.value).name} position failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Reset ax:{axid.value} successed')
        elif posType.value == POSITION_TYPE.POSITION_ACT.value:
            self.errCde = self.AdvMot.Acm_AxSetActualPosition(self.axHandArr[axid.value], setPos)
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Reset ax:{axid.value} {POSITION_TYPE(posType.value).name} position failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Reset ax:{axid.value} {POSITION_TYPE(posType.value).name} position failed:{self.errCde:x}')
            self.errCde = self.AdvMot.Acm_AxGetActualPosition(self.axHandArr[axid.value], byref(getPos))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get ax:{axid.value} position failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get ax:{axid.value} {POSITION_TYPE(posType.value).name} position failed:{self.errCde:x}')
            if getPos.value != setPos.value:
                self._PrintResult(False, f'Reset ax:{axid.value} position failed:{self.errCde:x}')
                self.assertEqual(setPos.value, getPos.value, f'Reset ax:{axid.value} {POSITION_TYPE(posType.value).name} position failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Reset ax:{axid.value} {POSITION_TYPE(posType.value).name} successed')

    def _AxCheckState(self, axid, state, posType):
        getState = c_uint16(16)
        getPos = c_double(0)
        self.errCde = self.AdvMot.Acm_AxGetState(self.axHandArr[axid.value], byref(getState))
        while getState.value != state:
            print(f'{Fore.BLUE}Not Ready, state:{AXIS_STATE(getState.value).name}, cur_pos:{getPos.value}', end='\r')
            if self.except_err.value != self.errCde:
                self._PrintResult(False, f'Get ax:{axid.value} state failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get ax:{axid.value} state failed:{self.errCde:x}')
            time.sleep(0.5)
            self.errCde = self.AdvMot.Acm_AxGetState(self.axHandArr[axid.value], byref(getState))
            time.sleep(0.5)
            if posType.value == POSITION_TYPE.POSITION_CMD.value:
                self.errCde = self.AdvMot.Acm_AxGetCmdPosition(self.axHandArr[axid.value], byref(getPos))
            elif posType.value == POSITION_TYPE.POSITION_ACT.value:
                self.errCde = self.AdvMot.Acm_AxGetActualPosition(self.axHandArr[axid.value], byref(getPos))
        self._PrintResult(True, f'Ax:{axid.value} state:{AXIS_STATE(getState.value).name}')

    def _AxSetSpeed(self, axid):
        pptArr = [c_uint32(self.AdvPpt.PAR_AxVelLow.value), c_uint32(self.AdvPpt.PAR_AxVelHigh.value),
                  c_uint32(self.AdvPpt.PAR_AxAcc.value), c_uint32(self.AdvPpt.PAR_AxDec.value)]
        setVal = [c_double(1000), c_double(4000), c_double(5000), c_double(1000)]
        for i in range(len(pptArr)):
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Ax:{axid.value} {self.AdvPpt(pptArr[i].value).name}:{setVal[i].value}]')
            self._SetProperty(pptArr[i], setVal[i], axid, ADV_HANDLE_TYPE.HdType_Axis)

    def _AxPTP(self, axid, mode, targetPos, posType):
        getPos = c_double(-1)
        state = AXIS_STATE.STA_AX_READY.value
        self._AxSetSpeed(axid)
        if mode == ABS_MODE.MOVE_REL.value:
            self.errCde = self.AdvMot.Acm_AxMoveRel(self.axHandArr[axid.value], targetPos)
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Ax:{axid.value} PTP failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Ax:{axid.value} PTP failed:{self.errCde:x}')
            self._AxCheckState(axid, state, posType)
            self.errCde = self.AdvMot.Acm_AxGetCmdPosition(self.axHandArr[axid.value], byref(getPos))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get ax:{axid.value} position failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get ax:{axid.value} position failed:{self.errCde:x}')
            if getPos.value != targetPos.value:
                self._PrintResult(False, f'Ax:{axid.value} PTP target position at:{targetPos.value}, but end at:{getPos.value}')
                self.assertEqual(targetPos.value, getPos.value, f'Ax:{axid.value} PTP target position at:{targetPos.value}, but end at:{getPos.value}')
            else:
                self._PrintResult(True, f'Ax:{axid.value} PTP done, end at:{getPos.value}')

    def _OnOffCmp(self, SWCmpChId, onOff):
        getVal = c_double(-1)
        swcmp = c_uint32(SWCmpChId.value)
        self.errCde = self.AdvMot.Acm_SetChannelProperty(self.devHandle, swcmp, self.AdvPpt.CFG_CH_DaqSWCmpDoEnable.value, onOff)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'{'Enable' if onOff is COMPARE_ENABLE.CMP_ENABLE.value else 'Disable'}  SWCmp:{SWCmpChId.value} failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'{'Enable' if onOff is COMPARE_ENABLE.CMP_ENABLE.value else 'Disable'}  SWCmp:{SWCmpChId.value} failed:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm_GetChannelProperty(self.devHandle, swcmp, self.AdvPpt.CFG_CH_DaqSWCmpDoEnable.value, byref(getVal))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Get {self.AdvPpt.CFG_CH_DaqSWCmpDoEnable.name} failed:{self.errCde}')
            self.assertEqual(self.except_err.value, self.errCde, f'Get {self.AdvPpt.CFG_CH_DaqSWCmpDoEnable.name} failed:{self.errCde}')
        if int(getVal.value) != onOff:
            self._PrintResult(False, f'Set {self.AdvPpt.CFG_CH_DaqSWCmpDoEnable.name} failed')
            self.assertEqual(onOff, getVal.value, f'Set {self.AdvPpt.CFG_CH_DaqSWCmpDoEnable.name} failed')
        else:
            self._PrintResult(True, f'{'Enable' if onOff is COMPARE_ENABLE.CMP_ENABLE.value else 'Disable'} SWCmp:{SWCmpChId.value} successed')

    def _AddAxIntoGroup(self, axid):
        self.errCde = self.AdvMot.Acm_GpAddAxis(byref(self.gpHandle), self.axHandArr[axid.value])
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Add ax:{axid.value} failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Add ax:{axid.value} failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Add ax:{axid.value} into group successed')

    def _CloseGroup(self):
        self.errCde = self.AdvMot.Acm_GpClose(self.gpHandle)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Close group failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Close group failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Close group successed')

    def _GpSetSpeed(self):
        pptArr = [c_uint32(self.AdvGpPpt.CFG_GpMaxVel.value), c_uint32(self.AdvGpPpt.CFG_GpMaxAcc.value),
                  c_uint32(self.AdvGpPpt.CFG_GpMaxDec.value),
                  c_uint32(self.AdvGpPpt.PAR_GpVelLow.value), c_uint32(self.AdvGpPpt.PAR_GpVelHigh.value),
                  c_uint32(self.AdvGpPpt.PAR_GpAcc.value), c_uint32(self.AdvGpPpt.PAR_GpDec.value)]
        setVal = [c_double(10000), c_double(10000), c_double(10000),
                  c_double(1000), c_double(4000), c_double(5000), c_double(1000)]
        getVal = c_double(0)
        for i in range(len(pptArr)):
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Group {self.AdvGpPpt(pptArr[i].value).name}:{setVal[i].value}]')
            self.errCde = self.AdvMot.Acm_SetF64Property(self.gpHandle, pptArr[i], setVal[i])
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Set {self.AdvGpPpt(pptArr[i].value).name} failed:{self.errCde:x}')
                self.assertEqual(self.errCde, self.except_err.value, f'Set {self.AdvGpPpt(pptArr[i].value).name} failed:{self.errCde:x}')
            self.errCde = self.AdvMot.Acm_GetF64Property(self.gpHandle, pptArr[i], byref(getVal))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Acm_GetF64Property failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Acm_GetF64Property failed:{self.errCde:x}')
            if getVal.value != setVal[i].value:
                self._PrintResult(False, f'Set {self.AdvGpPpt(pptArr[i].value).name}:{setVal[i].value}, but get:{getVal.value}')
                self.assertEqual(setVal[i].value, getVal.value, f'Set {self.AdvGpPpt(pptArr[i].value).name}:{setVal[i].value}, but get:{getVal.value}')
            else:
                self._PrintResult(True, f'Set {self.AdvGpPpt(pptArr[i].value).name}:{getVal.value} successed')

    def _GpCheckState(self, gpArr):
        state = GROUP_STATE.STA_GP_READY
        getState = c_uint16(12)
        getPos = c_double(0)
        self.errCde = self.AdvMot.Acm_GpGetState(self.gpHandle, byref(getState))
        while getState.value != state.value:
            print(f'{Fore.BLUE}Not Ready, state:{GROUP_STATE(getState.value).name}, ax:{gpArr[0].value} cur_pos:{getPos.value}', end='\r')
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get group state failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get group state failed:{self.errCde:x}')
            time.sleep(0.5)
            self.errCde = self.AdvMot.Acm_GpGetState(self.gpHandle, byref(getState))
            self.errCde = self.AdvMot.Acm_AxGetCmdPosition(self.axHandArr[gpArr[0].value], byref(getPos))
        self._PrintResult(True, f'Group state:{GROUP_STATE(getState.value).name}')

    def _GpMoveLinearRel(self, axesArr, endArr):
        endArrTrans = (c_double * len(endArr))(*endArr)
        endArrLen = c_uint32(len(endArr))
        getPos = c_double(0)
        if self.gpHandle.value is not None:
            self._CloseGroup()
        # 創立群組
        for i in range(len(axesArr)):
            self._AddAxIntoGroup(axesArr[i])
        # 設定群組速度
        self._GpSetSpeed()
        # 群組移動
        print(f'{Fore.CYAN}[Start move group in LINE_REL mode, end at:{endArr[0].value}]')
        self.errCde = self.AdvMot.Acm_GpMoveLinearRel(self.gpHandle, endArrTrans, byref(endArrLen))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Group move line failed:{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Group move line failed:{self.errCde:x}')
        time.sleep(0.5)
        self._GpCheckState(axesArr)
        for i in range(len(axesArr)):
            self.errCde = self.AdvMot.Acm_AxGetCmdPosition(self.axHandArr[axesArr[i].value], byref(getPos))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get ax:{axesArr[i].value} position failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get ax:{axesArr[i].value} position failed:{self.errCde:x}')
            if getPos.value != endArr[0].value:
                self._PrintResult(False, f'Ax:{axesArr[i].value} target position at:{endArr[i].value}, but end at:{getPos.value}')
                self.assertEqual(endArr[i].value, getPos.value, f'Ax:{axesArr[i].value} target position at:{endArr[i].value}, but end at:{getPos.value}')
            else:
                self._PrintResult(True, f'Group move done, end at:{getPos.value}')
        # 清除群組
        self._CloseGroup()

    def swCmpBoundTestSingle(self):
        global global_link_type
        global global_run_swcmpch
        linkedDo = c_uint32(0)
        pptArr = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value),
                    c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoEnable.value),
                    c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value),
                    c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoLogic.value),
                    c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoPulseWidth.value),
                    c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoDelay.value),
                    c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpMethod.value)]
        upperBound = [c_double(65536), c_double(2), c_double(2), c_double(2),
                            c_double(0x100000000), c_double(1000001), c_double(3)]
        errorCode = [ErrorCode.EC_InvalidCntMultiCmpDeviation.value, ErrorCode.EC_InvalidCmpDoEnable.value, ErrorCode.EC_InvalidCmpDoOutputMode.value, ErrorCode.EC_InvalidCmpDoLogic.value, ErrorCode.EC_InvalidCmpDoPulseWidth.value, ErrorCode.InvalidInputParam.value, ErrorCode.EC_InvalidCntCmpMethod.value]
        lowerBound = c_double(-1)
        for i in range(global_run_swcmpch):
            swCmpCh = c_uint16(i)
            print(f'{Fore.YELLOW}--- SWCmpCh:{i} test start ---')
            link_axis = [c_uint32(i)]
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            # 綁定軟體比較觸發通道與 Do
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._LinkedDo(swCmpCh, linkedDo)
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to {global_link_type.name}]')
            self._ClearLinkedObj(swCmpCh, global_link_type, link_axis)
            # 綁定軟體比較觸發通道與 Axis
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to {global_link_type.name}]')
            self._LinkedObj(swCmpCh, global_link_type, link_axis)
            # 確認屬性邊界錯誤
            for idx, ppt in enumerate(pptArr):
                print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[UpperBound][{self.AdvPpt(ppt.value).name}]')
                self._SetPropertyBound(swCmpCh, ppt, upperBound[idx], errorCode[idx])
                print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[LowerBound][{self.AdvPpt(ppt.value).name}]')
                self._SetPropertyBound(swCmpCh, ppt, lowerBound, errorCode[idx])
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to {global_link_type.name}]')
            self._ClearLinkedObj(swCmpCh, global_link_type, link_axis)
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            print(f'{Fore.YELLOW}--- SWCmpCh:{i} test end ---')
            print('\n')

    def swCmpRunAxisSingleData(self):
        global global_run_swcmpch, global_run_do_mode
        linkType = ADV_OBJ_TYPE.ADV_AXIS
        linkedDoCh = c_uint32(0)
        posType = c_uint(POSITION_TYPE.POSITION_CMD.value)
        if global_run_do_mode.value == COMPARE_OUTPUT_MODE.CMP_TOGGLE.value:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value), c_double(500)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0)]
        else:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value),
                c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoPulseWidth.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(500), c_double(0.5*1000*1000)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0), c_double(0)]
        # SW Cmp behavior:  --- ON ---      --- Off ---
        setCmpTableArr = [c_double(5000)]
        endPos = c_double(5200)
        axMoveMode = ABS_MODE.MOVE_REL.value
        for ax in range(global_run_swcmpch):
            swCmpCh = c_uint16(ax)
            linkAxId = c_uint32(ax)
            linkedAxis = [linkAxId]
            getSWCmpIndex = c_uint32(0)
            getSWCmpRemainCnt = c_uint32(0)
            getSWCmpSpaceCnt = c_uint32(0)
            print(f'{Fore.YELLOW}--- Start test [SWCmp:{swCmpCh.value}] single [axis:{linkAxId.value}] with table, ({global_run_do_mode.name} mode) ---')
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            # 綁定軟體比較觸發通道與 Do
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._LinkedDo(swCmpCh, linkedDoCh)
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._ClearLinkedObj(swCmpCh, linkType, linkedAxis)
            # 綁定軟體比較觸發通道與 Axis
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._LinkedObj(swCmpCh, linkType, linkedAxis)
            # 清除軸錯誤, 設置軸位置為 0
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Axis reset error, and reset position]')
            self._ResetAxis(linkAxId, posType)
            # 設置軟體比較觸發屬性
            for i in range(len(ppt)):
                if ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Do output mode:{COMPARE_OUTPUT_MODE(pptSetVal[i].value).name}]')
                elif ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[CMP deviation:{pptSetVal[i].value}]')
                else:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[{self.AdvPpt(ppt[i].value).name}:{pptSetVal[i].value}]')
                self._SetChProperty(swCmpCh, ppt[i], pptSetVal[i])
            # 設置軟體比較觸發數據, 一次一個, 跑完再設下一組
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Software compare data]')
            for idx in range(len(setCmpTableArr)):
                # 關閉軟體比較觸發
                print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
                self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
                # 重置軟體比較觸發表格
                print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Software compare data]')
                self.errCde = self.AdvMot.Acm_AxResetCmpData(self.axHandArr[ax])
                if self.errCde != self.except_err.value:
                    self._PrintResult(False, f'Reset CMP data failed:{self.errCde:x}')
                    self.assertEqual(self.except_err.value, self.errCde, f'Reset CMP data failed:{self.errCde:x}')
                else:
                    self._PrintResult(True, f'Reset CMP data successed')
                # 獲取軟體比較數據狀態
                self.errCde = self.AdvMot.Acm_AxGetCmpBufferStatus(self.axHandArr[ax], byref(getSWCmpIndex), byref(getSWCmpRemainCnt), byref(getSWCmpSpaceCnt))
                if self.errCde != self.except_err.value:
                    self._PrintResult(False, f'Get CMP status failed:{self.errCde:x}')
                    self.assertEqual(self.except_err.value, self.errCde, f'Get CMP status failed:{self.errCde:x}')
                else:
                    self._PrintResult(True, f'Get CMP status successed (Index:{getSWCmpIndex.value}, RemainCnt:{getSWCmpRemainCnt.value}, FreeSpaceCnt:{getSWCmpSpaceCnt.value})')
                # 設置軟體比較觸發數據
                self.errCde = self.AdvMot.Acm_AxSetCmpData(self.axHandArr[ax], setCmpTableArr[idx])
                if self.errCde != self.except_err.value:
                    self._PrintResult(False, f'Set CMP data failed:{self.errCde:x}')
                    self.assertEqual(self.except_err.value, self.errCde, f'Set CMP data failed:{self.errCde:x}')
                else:
                    self._PrintResult(True, f'Set CMP data:{setCmpTableArr[idx].value} successed')
                # 獲取軟體比較數據狀態
                self.errCde = self.AdvMot.Acm_AxGetCmpBufferStatus(self.axHandArr[ax], byref(getSWCmpIndex), byref(getSWCmpRemainCnt), byref(getSWCmpSpaceCnt))
                if self.errCde != self.except_err.value:
                    self._PrintResult(False, f'Get CMP status failed:{self.errCde:x}')
                    self.assertEqual(self.except_err.value, self.errCde, f'Get CMP status failed:{self.errCde:x}')
                else:
                    self._PrintResult(True, f'Get CMP status successed (Index:{getSWCmpIndex.value}, RemainCnt:{getSWCmpRemainCnt.value}, FreeSpaceCnt:{getSWCmpSpaceCnt.value})')
                # 啟動軟體比較觸發
                print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Software compare]')
                self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_ENABLE.value)
                # 讀取軟體比較數據數值
                getCmpData = c_double(0)
                self.errCde = self.AdvMot.Acm_AxGetCmpData(self.axHandArr[ax], byref(getCmpData))
                if self.errCde != self.except_err.value:
                    self._PrintResult(False, f'Acm_AxGetCmpData failed:{self.errCde:x}')
                    self.assertEqual(self.except_err.value, self.errCde, f'Acm_AxGetCmpData failed:{self.errCde:x}')
                else:
                    self._PrintResult(True, f'Acm_AxGetCmpData successed:{getCmpData.value}')
                # 使軸運動
                print(f'{Fore.CYAN}[Move]{Fore.LIGHTBLUE_EX}[Axis:{linkAxId.value} move {ABS_MODE(axMoveMode).name} to {endPos.value}]')
                self._AxPTP(linkAxId, axMoveMode, endPos, posType)
                # 獲取軟體比較數據狀態
                self.errCde = self.AdvMot.Acm_AxGetCmpBufferStatus(self.axHandArr[ax], byref(getSWCmpIndex), byref(getSWCmpRemainCnt), byref(getSWCmpSpaceCnt))
                if self.errCde != self.except_err.value:
                    self._PrintResult(False, f'Get CMP status failed:{self.errCde:x}')
                    self.assertEqual(self.except_err.value, self.errCde, f'Get CMP status failed:{self.errCde:x}')
                else:
                    self._PrintResult(True, f'Get CMP status successed (Index:{getSWCmpIndex.value}, RemainCnt:{getSWCmpRemainCnt.value}, FreeSpaceCnt:{getSWCmpSpaceCnt.value})')
                # 關閉軟體比較觸發
                print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
                self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            print(f'{Fore.YELLOW}--- End test SWCmp:{swCmpCh.value} ---')
            print(f'{Fore.BLUE}***** Initializing (SWCmp:{swCmpCh.value} single axis:{linkAxId.value}) *****')
            # 清除軸錯誤, 設置軸位置為 0
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Axis reset error, and reset position]')
            self._ResetAxis(linkAxId, posType)
            # 設置軟體比較觸發輸出模式回初始值
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Reset property back to default value]')
            for i in range(len(ppt)):
                self._SetChProperty(swCmpCh, ppt[i], defaultPptVal[i])
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._ClearLinkedObj(swCmpCh, linkType, linkedAxis)
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            print(f'{Fore.BLUE}***** End (SWCmp:{swCmpCh.value} single axis:{linkAxId.value}) *****')
            print('\n')

    def swCmpRunAxisSingleTable(self):
        global global_run_swcmpch, global_use_buffer_api, global_run_do_mode
        linkType = ADV_OBJ_TYPE.ADV_AXIS
        linkedDoCh = c_uint32(0)
        posType = c_uint(POSITION_TYPE.POSITION_CMD.value)
        if global_run_do_mode.value == COMPARE_OUTPUT_MODE.CMP_TOGGLE.value:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value), c_double(500)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0)]
        else:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value),
                c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoPulseWidth.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(500), c_double(0.5*1000*1000)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0), c_double(0)]
         # SW Cmp behavior:  --- ON ---      --- Off ---
        setCmpTableArr = [c_double(5000), c_double(10000), c_double(15000), c_double(20000), c_double(25000), c_double(30000)]
        transCmpTableArr = (c_double * len(setCmpTableArr))(*setCmpTableArr)
        endPos = c_double(31000)
        axMoveMode = ABS_MODE.MOVE_REL.value
        for ax in range(global_run_swcmpch):
            swCmpCh = c_uint16(ax)
            linkAxId = c_uint32(ax)
            linkedAxis = [linkAxId]
            getSWCmpIndex = c_uint32(0)
            getSWCmpRemainCnt = c_uint32(0)
            getSWCmpSpaceCnt = c_uint32(0)
            print(f'{Fore.YELLOW}--- Start test [SWCmp:{swCmpCh.value}] single [axis:{linkAxId.value}] with table, ({global_run_do_mode.name} mode) ---')
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            # 綁定軟體比較觸發通道與 Do
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._LinkedDo(swCmpCh, linkedDoCh)
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._ClearLinkedObj(swCmpCh, linkType, linkedAxis)
            # 綁定軟體比較觸發通道與 Axis
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._LinkedObj(swCmpCh, linkType, linkedAxis)
            # 清除軸錯誤, 設置軸位置為 0
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Axis reset error, and reset position]')
            self._ResetAxis(linkAxId, posType)
            # 設置軟體比較觸發屬性
            for i in range(len(ppt)):
                if ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Do output mode:{COMPARE_OUTPUT_MODE(pptSetVal[i].value).name}]')
                elif ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[CMP deviation:{pptSetVal[i].value}]')
                else:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[{self.AdvPpt(ppt[i].value).name}:{pptSetVal[i].value}]')
                self._SetChProperty(swCmpCh, ppt[i], pptSetVal[i])
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            # 重置軟體比較觸發表格
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Software compare data]')
            self.errCde = self.AdvMot.Acm_AxResetCmpData(self.axHandArr[ax])
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Reset CMP data failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Reset CMP data failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Reset CMP data successed')
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm_AxGetCmpBufferStatus(self.axHandArr[ax], byref(getSWCmpIndex), byref(getSWCmpRemainCnt), byref(getSWCmpSpaceCnt))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get CMP status failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get CMP status failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP status successed (Index:{getSWCmpIndex.value}, RemainCnt:{getSWCmpRemainCnt.value}, FreeSpaceCnt:{getSWCmpSpaceCnt.value})')
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Software compare data]')
            for idx in range(len(setCmpTableArr)):
                if idx != len(setCmpTableArr) - 1:
                    print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}', end= ' ')
                else:
                    print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}')
            # 設置軟體比較觸發數據
            if global_use_buffer_api is True:
                self.errCde = self.AdvMot.Acm_AxSetCmpBufferData(self.axHandArr[ax], transCmpTableArr, len(setCmpTableArr))
            else:
                self.errCde = self.AdvMot.Acm_AxSetCmpTable(self.axHandArr[ax], transCmpTableArr, len(setCmpTableArr))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'{'Acm_AxSetCmpBufferData' if global_use_buffer_api is True else 'Acm_AxSetCmpTable'}:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'{'Acm_AxSetCmpBufferData' if global_use_buffer_api is True else 'Acm_AxSetCmpTable'}:{self.errCde:x}')
            else:
                self._PrintResult(True, f'{'Acm_AxSetCmpBufferData' if global_use_buffer_api is True else 'Acm_AxSetCmpTable'} successed')
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm_AxGetCmpBufferStatus(self.axHandArr[ax], byref(getSWCmpIndex), byref(getSWCmpRemainCnt), byref(getSWCmpSpaceCnt))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get CMP status failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get CMP status failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP status successed (Index:{getSWCmpIndex.value}, RemainCnt:{getSWCmpRemainCnt.value}, FreeSpaceCnt:{getSWCmpSpaceCnt.value})')
            # 讀取軟體比較數據數值
            getCmpData = c_double(0)
            self.errCde = self.AdvMot.Acm_AxGetCmpData(self.axHandArr[ax], byref(getCmpData))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Acm_AxGetCmpData failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Acm_AxGetCmpData failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Acm_AxGetCmpData successed:{getCmpData.value}')
            # 啟動軟體比較觸發
            print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_ENABLE.value)
            # 使軸運動
            print(f'{Fore.CYAN}[Move]{Fore.LIGHTBLUE_EX}[Axis:{linkAxId.value} move {ABS_MODE(axMoveMode).name} to {endPos.value}]')
            self._AxPTP(linkAxId, axMoveMode, endPos, posType)
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm_AxGetCmpBufferStatus(self.axHandArr[ax], byref(getSWCmpIndex), byref(getSWCmpRemainCnt), byref(getSWCmpSpaceCnt))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get CMP status failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get CMP status failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP status successed (Index:{getSWCmpIndex.value}, RemainCnt:{getSWCmpRemainCnt.value}, FreeSpaceCnt:{getSWCmpSpaceCnt.value})')
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            print(f'{Fore.YELLOW}--- End test SWCmp:{swCmpCh.value} ---')
            print(f'{Fore.BLUE}***** Initializing (SWCmp:{swCmpCh.value} single axis:{linkAxId.value}) *****')
            # 清除軸錯誤, 設置軸位置為 0
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Axis reset error, and reset position]')
            self._ResetAxis(linkAxId, posType)
            # 設置軟體比較觸發輸出模式回初始值
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Reset property back to default value]')
            for i in range(len(ppt)):
                self._SetChProperty(swCmpCh, ppt[i], defaultPptVal[i])
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._ClearLinkedObj(swCmpCh, linkType, linkedAxis)
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            print(f'{Fore.BLUE}***** End (SWCmp:{swCmpCh.value} single axis:{linkAxId.value}) *****')
            print('\n')

    def swCmpRunAxisSingleAuto(self):
        global global_run_swcmpch, global_run_do_mode
        linkType = ADV_OBJ_TYPE.ADV_AXIS
        linkedDoCh = c_uint32(0)
        posType = c_uint(POSITION_TYPE.POSITION_CMD.value)
        if global_run_do_mode.value == COMPARE_OUTPUT_MODE.CMP_TOGGLE.value:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value), c_double(500)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0)]
        else:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value),
                c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoPulseWidth.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(500), c_double(0.5*1000*1000)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0), c_double(0)]
        endPos = c_double(31000)
        axMoveMode = ABS_MODE.MOVE_REL.value
        startPos = c_double(5000)
        autoEndPos = c_double(30000)
        interval = c_double(5000)
        for ax in range(global_run_swcmpch):
            swCmpCh = c_uint16(ax)
            linkAxId = c_uint32(ax)
            linkedAxis = [linkAxId]
            getSWCmpIndex = c_uint32(0)
            getSWCmpRemainCnt = c_uint32(0)
            getSWCmpSpaceCnt = c_uint32(0)
            print(f'{Fore.YELLOW}--- Start test [SWCmp:{swCmpCh.value}] single [axis:{linkAxId.value}] with table, ({global_run_do_mode.name} mode) ---')
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            # 綁定軟體比較觸發通道與 Do
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._LinkedDo(swCmpCh, linkedDoCh)
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._ClearLinkedObj(swCmpCh, linkType, linkedAxis)
            # 綁定軟體比較觸發通道與 Axis
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._LinkedObj(swCmpCh, linkType, linkedAxis)
            # 清除軸錯誤, 設置軸位置為 0
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Axis reset error, and reset position]')
            self._ResetAxis(linkAxId, posType)
            # 設置軟體比較觸發屬性
            for i in range(len(ppt)):
                if ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Do output mode:{COMPARE_OUTPUT_MODE(pptSetVal[i].value).name}]')
                elif ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[CMP deviation:{pptSetVal[i].value}]')
                else:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[{self.AdvPpt(ppt[i].value).name}:{pptSetVal[i].value}]')
                self._SetChProperty(swCmpCh, ppt[i], pptSetVal[i])
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            # 重置軟體比較觸發表格
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Software compare data]')
            self.errCde = self.AdvMot.Acm_AxResetCmpData(self.axHandArr[ax])
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Reset CMP data failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Reset CMP data failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Reset CMP data successed')
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm_AxGetCmpBufferStatus(self.axHandArr[ax], byref(getSWCmpIndex), byref(getSWCmpRemainCnt), byref(getSWCmpSpaceCnt))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get CMP status failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get CMP status failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP status successed (Index:{getSWCmpIndex.value}, RemainCnt:{getSWCmpRemainCnt.value}, FreeSpaceCnt:{getSWCmpSpaceCnt.value})')
            # 設置軟體比較觸發自動觸發
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Software compare data]')
            print(f'{Fore.LIGHTBLUE_EX}Start pos:{startPos.value}, interval:{interval.value}, end pos:{autoEndPos.value}')
            self.errCde = self.AdvMot.Acm_AxSetCmpAuto(self.axHandArr[ax], startPos, endPos, interval)
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Acm_AxSetCmpAuto failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Acm_AxSetCmpAuto failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Acm_AxSetCmpAuto successed')
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm_AxGetCmpBufferStatus(self.axHandArr[ax], byref(getSWCmpIndex), byref(getSWCmpRemainCnt), byref(getSWCmpSpaceCnt))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get CMP status failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get CMP status failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP status successed (Index:{getSWCmpIndex.value}, RemainCnt:{getSWCmpRemainCnt.value}, FreeSpaceCnt:{getSWCmpSpaceCnt.value})')
            # 讀取軟體比較數據數值
            getCmpData = c_double(0)
            self.errCde = self.AdvMot.Acm_AxGetCmpData(self.axHandArr[ax], byref(getCmpData))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Acm_AxGetCmpData failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Acm_AxGetCmpData failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Acm_AxGetCmpData successed:{getCmpData.value}')
            # 啟動軟體比較觸發
            print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_ENABLE.value)
            # 使軸運動
            print(f'{Fore.CYAN}[Move]{Fore.LIGHTBLUE_EX}[Axis:{linkAxId.value} move {ABS_MODE(axMoveMode).name} to {endPos.value}]')
            self._AxPTP(linkAxId, axMoveMode, endPos, posType)
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm_AxGetCmpBufferStatus(self.axHandArr[ax], byref(getSWCmpIndex), byref(getSWCmpRemainCnt), byref(getSWCmpSpaceCnt))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get CMP status failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get CMP status failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP status successed (Index:{getSWCmpIndex.value}, RemainCnt:{getSWCmpRemainCnt.value}, FreeSpaceCnt:{getSWCmpSpaceCnt.value})')
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            print(f'{Fore.YELLOW}--- End test SWCmp:{swCmpCh.value} ---')
            print(f'{Fore.BLUE}***** Initializing (SWCmp:{swCmpCh.value} single axis:{linkAxId.value}) *****')
            # 清除軸錯誤, 設置軸位置為 0
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Axis reset error, and reset position]')
            self._ResetAxis(linkAxId, posType)
            # 設置軟體比較觸發輸出模式回初始值
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Reset property back to default value]')
            for i in range(len(ppt)):
                self._SetChProperty(swCmpCh, ppt[i], defaultPptVal[i])
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._ClearLinkedObj(swCmpCh, linkType, linkedAxis)
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            print(f'{Fore.BLUE}***** End (SWCmp:{swCmpCh.value} single axis:{linkAxId.value}) *****')
            print('\n')

    def swCmpRunAxesTable(self):
        global global_run_swcmpch, global_use_buffer_api, global_run_do_mode
        linkType = ADV_OBJ_TYPE.ADV_AXIS
        linkedDoCh = c_uint32(0)
        posType = c_uint(POSITION_TYPE.POSITION_CMD.value)
        if global_run_do_mode.value == COMPARE_OUTPUT_MODE.CMP_TOGGLE.value:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value), c_double(500)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0)]
        else:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value),
                c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoPulseWidth.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(500), c_double(0.5*1000*1000)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0), c_double(0)]
         # SW Cmp behavior:  --- ON ---      --- Off ---
        setCmpTableArr = [c_double(5000), c_double(10000), c_double(15000), c_double(20000), c_double(25000), c_double(30000)]
        transCmpTableArr = (c_double * len(setCmpTableArr))(*setCmpTableArr)
        endPosArr = [c_double(31000), c_double(31000)]
        axMoveMode = ABS_MODE.MOVE_REL.value
        for ax in range(global_run_swcmpch):
            swCmpCh = c_uint16(ax)
            if ax != 63:
                linkedAxes = [c_uint32(ax), c_uint32(ax + 1)]
            else:
                linkedAxes = [c_uint32(ax), c_uint32(0)]
            getSWCmpIndex = c_uint32(0)
            getSWCmpRemainCnt = c_uint32(0)
            getSWCmpSpaceCnt = c_uint32(0)
            print(f'{Fore.YELLOW}--- Start test [SWCmp:{swCmpCh.value}] 2 axes:[{linkedAxes[0].value, linkedAxes[1].value}] with table, ({global_run_do_mode.name} mode) ---')
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            # 綁定軟體比較觸發通道與 Do
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._LinkedDo(swCmpCh, linkedDoCh)
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._ClearLinkedObj(swCmpCh, linkType, linkedAxes)
            # 綁定軟體比較觸發通道與 Axis
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._LinkedObj(swCmpCh, linkType, linkedAxes)
            # 清除軸錯誤, 設置軸位置為 0
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Axis reset error, and reset position]')
            self._ResetAxis(linkedAxes[0], posType)
            self._ResetAxis(linkedAxes[1], posType)
            # 設置軟體比較觸發屬性
            for i in range(len(ppt)):
                if ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Do output mode:{COMPARE_OUTPUT_MODE(pptSetVal[i].value).name}]')
                elif ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[CMP deviation:{pptSetVal[i].value}]')
                else:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[{self.AdvPpt(ppt[i].value).name}:{pptSetVal[i].value}]')
                self._SetChProperty(swCmpCh, ppt[i], pptSetVal[i])
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            for i in range(len(linkedAxes)):
                # 重置軟體比較觸發表格
                print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Software compare data, ax:{linkedAxes[i].value}]')
                self.errCde = self.AdvMot.Acm_AxResetCmpData(self.axHandArr[linkedAxes[i].value])
                if self.errCde != self.except_err.value:
                    self._PrintResult(False, f'Reset CMP data failed:{self.errCde:x}')
                    self.assertEqual(self.except_err.value, self.errCde, f'Reset CMP data failed:{self.errCde:x}')
                else:
                    self._PrintResult(True, f'Reset CMP data successed')
                # 獲取軟體比較數據狀態
                self.errCde = self.AdvMot.Acm_AxGetCmpBufferStatus(self.axHandArr[linkedAxes[i].value], byref(getSWCmpIndex), byref(getSWCmpRemainCnt), byref(getSWCmpSpaceCnt))
                if self.errCde != self.except_err.value:
                    self._PrintResult(False, f'Get CMP status failed:{self.errCde:x}')
                    self.assertEqual(self.except_err.value, self.errCde, f'Get CMP status failed:{self.errCde:x}')
                else:
                    self._PrintResult(True, f'Get CMP status successed (Index:{getSWCmpIndex.value}, RemainCnt:{getSWCmpRemainCnt.value}, FreeSpaceCnt:{getSWCmpSpaceCnt.value})')
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Software compare data]')
            for idx in range(len(setCmpTableArr)):
                if idx != len(setCmpTableArr) - 1:
                    print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}', end= ' ')
                else:
                    print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}')
            for i in range(len(linkedAxes)):
                # 設置軟體比較觸發數據
                if global_use_buffer_api is True:
                    self.errCde = self.AdvMot.Acm_AxSetCmpBufferData(self.axHandArr[linkedAxes[i].value], transCmpTableArr, len(setCmpTableArr))
                else:
                    self.errCde = self.AdvMot.Acm_AxSetCmpTable(self.axHandArr[linkedAxes[i].value], transCmpTableArr, len(setCmpTableArr))
                if self.errCde != self.except_err.value:
                    self._PrintResult(False, f'{'Acm_AxSetCmpBufferData' if global_use_buffer_api is True else 'Acm_AxSetCmpTable'}:{self.errCde:x}')
                    self.assertEqual(self.except_err.value, self.errCde, f'{'Acm_AxSetCmpBufferData' if global_use_buffer_api is True else 'Acm_AxSetCmpTable'}:{self.errCde:x}')
                else:
                    self._PrintResult(True, f'{'Acm_AxSetCmpBufferData' if global_use_buffer_api is True else 'Acm_AxSetCmpTable'} successed')
                # 獲取軟體比較數據狀態
                self.errCde = self.AdvMot.Acm_AxGetCmpBufferStatus(self.axHandArr[linkedAxes[i].value], byref(getSWCmpIndex), byref(getSWCmpRemainCnt), byref(getSWCmpSpaceCnt))
                if self.errCde != self.except_err.value:
                    self._PrintResult(False, f'Get CMP status failed:{self.errCde:x}')
                    self.assertEqual(self.except_err.value, self.errCde, f'Get CMP status failed:{self.errCde:x}')
                else:
                    self._PrintResult(True, f'Get CMP status successed (Index:{getSWCmpIndex.value}, RemainCnt:{getSWCmpRemainCnt.value}, FreeSpaceCnt:{getSWCmpSpaceCnt.value})')
                # 讀取軟體比較數據數值
                getCmpData = c_double(0)
                self.errCde = self.AdvMot.Acm_AxGetCmpData(self.axHandArr[linkedAxes[i].value], byref(getCmpData))
                if self.errCde != self.except_err.value:
                    self._PrintResult(False, f'Acm_AxGetCmpData failed:{self.errCde:x}')
                    self.assertEqual(self.except_err.value, self.errCde, f'Acm_AxGetCmpData failed:{self.errCde:x}')
                else:
                    self._PrintResult(True, f'Acm_AxGetCmpData ax:{linkedAxes[i].value} successed:{getCmpData.value}')
            # 啟動軟體比較觸發
            print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_ENABLE.value)
            # 使群組運動
            print(f'{Fore.CYAN}[Move]{Fore.LIGHTBLUE_EX}Ax:{linkedAxes[0].value, linkedAxes[1].value} move to {endPosArr[0].value, endPosArr[1].value}')
            self._GpMoveLinearRel(linkedAxes, endPosArr)
            for i in range(len(linkedAxes)):
                # 獲取軟體比較數據狀態
                self.errCde = self.AdvMot.Acm_AxGetCmpBufferStatus(self.axHandArr[linkedAxes[i].value], byref(getSWCmpIndex), byref(getSWCmpRemainCnt), byref(getSWCmpSpaceCnt))
                if self.errCde != self.except_err.value:
                    self._PrintResult(False, f'Get CMP status failed:{self.errCde:x}')
                    self.assertEqual(self.except_err.value, self.errCde, f'Get CMP status failed:{self.errCde:x}')
                else:
                    self._PrintResult(True, f'Get CMP status successed (Index:{getSWCmpIndex.value}, RemainCnt:{getSWCmpRemainCnt.value}, FreeSpaceCnt:{getSWCmpSpaceCnt.value})')
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            print(f'{Fore.YELLOW}--- End test SWCmp:{swCmpCh.value} ---')
            print(f'{Fore.BLUE}***** Initializing (SWCmp:{swCmpCh.value} 2 axes:[{linkedAxes[0].value, linkedAxes[1].value}]) *****')
            # 清除軸錯誤, 設置軸位置為 0
            for i in range(len(linkedAxes)):
                print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Ax:{linkedAxes[i].value} reset error, and reset position]')
                self._ResetAxis(linkedAxes[i], posType)
            # 設置軟體比較觸發輸出模式回初始值
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Reset property back to default value]')
            for i in range(len(ppt)):
                self._SetChProperty(swCmpCh, ppt[i], defaultPptVal[i])
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._ClearLinkedObj(swCmpCh, linkType, linkedAxes)
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            print(f'{Fore.BLUE}***** End (SWCmp:{swCmpCh.value} 2 axes:[{linkedAxes[0].value, linkedAxes[1].value}]) *****')
            print('\n')


def AdvCM1Initial():
    global global_open_axcnt
    global_open_axcnt = 64
    tests = ['initial', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTestBoundAxis():
    global global_link_type, global_run_swcmpch, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 1
    global_link_type = ADV_OBJ_TYPE.ADV_AXIS
    tests = ['initial', 'swCmpBoundTestSingle', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTestBoundCounter():
    global global_link_type, global_run_swcmpch, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 1
    global_link_type = ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL
    tests = ['initial', 'swCmpBoundTestSingle', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTestSingleAxisDataToggle():
    global global_run_swcmpch, global_run_do_mode, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 1
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    tests = ['initial', 'swCmpRunAxisSingleData', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTestSingleAxisTableToggle():
    global global_run_swcmpch, global_use_buffer_api, global_run_do_mode, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 1
    global_use_buffer_api = False
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    tests = ['initial', 'swCmpRunAxisSingleTable', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTestSingleAxisBufferToggle():
    global global_run_swcmpch, global_use_buffer_api, global_run_do_mode, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 1
    global_use_buffer_api = True
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    tests = ['initial', 'swCmpRunAxisSingleTable', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTestSingleAutoToggle():
    global global_run_swcmpch, global_run_do_mode, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 1
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    tests = ['initial', 'swCmpRunAxisSingleAuto', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTestSingleAxisDataPulse():
    global global_run_swcmpch, global_run_do_mode, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 1
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    tests = ['initial', 'swCmpRunAxisSingleData', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTestSingleAxisTablePulse():
    global global_run_swcmpch, global_use_buffer_api, global_run_do_mode, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 1
    global_use_buffer_api = False
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    tests = ['initial', 'swCmpRunAxisSingleTable', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTestSingleAxisBufferPulse():
    global global_run_swcmpch, global_use_buffer_api, global_run_do_mode, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 1
    global_use_buffer_api = True
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    tests = ['initial', 'swCmpRunAxisSingleTable', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTestSingleAutoPulse():
    global global_run_swcmpch, global_run_do_mode, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 1
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    tests = ['initial', 'swCmpRunAxisSingleAuto', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTest2AxesTableToggle():
    global global_run_swcmpch, global_use_buffer_api, global_run_do_mode, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 2
    global_use_buffer_api = False
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    tests = ['initial', 'swCmpRunAxesTable', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTest2AxesTablePulse():
    global global_run_swcmpch, global_use_buffer_api, global_run_do_mode, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 2
    global_use_buffer_api = False
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    tests = ['initial', 'swCmpRunAxesTable', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTest2AxesBufferToggle():
    global global_run_swcmpch, global_use_buffer_api, global_run_do_mode, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 2
    global_use_buffer_api = True
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    tests = ['initial', 'swCmpRunAxesTable', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite

def SWCmpTest2AxesBufferPulse():
    global global_run_swcmpch, global_use_buffer_api, global_run_do_mode, global_open_axcnt
    global_run_swcmpch = 1
    global_open_axcnt = 2
    global_use_buffer_api = True
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    tests = ['initial', 'swCmpRunAxesTable', 'closeAll']
    suite = unittest.TestSuite(map(SWCmp_TestCM1, tests))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # initital = runner.run(AdvCM1Initial())
    # bound_test_axis = runner.run(SWCmpTestBoundAxis())
    # bound_test_counter = runner.run(SWCmpTestBoundCounter())
    # run_ax_single_data_toggle = runner.run(SWCmpTestSingleAxisDataToggle())
    # run_ax_single_table_toggle = runner.run(SWCmpTestSingleAxisTableToggle())
    # run_ax_single_buffer_toggle = runner.run(SWCmpTestSingleAxisBufferToggle())
    # run_ax_single_auto_toggle = runner.run(SWCmpTestSingleAutoToggle())
    # run_ax_single_data_pulse = runner.run(SWCmpTestSingleAxisDataPulse())
    # run_ax_single_table_pulse = runner.run(SWCmpTestSingleAxisTablePulse())
    # run_ax_single_buffer_pulse = runner.run(SWCmpTestSingleAxisBufferPulse())
    # run_ax_single_auto_pulse = runner.run(SWCmpTestSingleAutoPulse())
    run_axes_table_toggle = runner.run(SWCmpTest2AxesTableToggle())
    run_axes_table_pulse = runner.run(SWCmpTest2AxesTablePulse())
    run_axes_buffer_toggle = runner.run(SWCmpTest2AxesBufferToggle())
    run_axes_buffer_pulse = runner.run(SWCmpTest2AxesBufferPulse())