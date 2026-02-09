import unittest
import os
import sys
import time

# 強制 Windows 使用 ANSI 支援
os.system('')
# # 強制設定 stdout 編碼為 utf-8
sys.stdout.reconfigure(encoding='utf-8')

from datetime import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.MotionInfo import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from colorama import init, Fore, Style

global_link_type = 0
global_run_swcmpch = 1
global_use_buffer_api = False
global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
init(autoreset=True, strip=False)

class SWCmp_Test(unittest.TestCase):
    def setUp(self):
        self.maxEnt = 10
        self.devlist = (DEVLIST*self.maxEnt)()
        self.outEnt = c_uint32(0)
        self.errCde = 0
        self.AdvMot = AdvCmnAPI_CM2
        self.AdvPpt = PropertyID2
        self.AdvErr = ErrorCode2
        self.AmcApi = AmcLogAPI
        self.bufferSize = 10 * 1024 * 1024
    def tearDown(self):
        self.errCde = 0

    def _PrintResult(self, isPass, message):
        if isPass:
            print(f'{Fore.GREEN}[✓ Pass]{message}')
        else:
            print(f'{Fore.RED}[X Fail]{message}')

    def initial(self):
        except_err = 0
        self.errCde = self.AdvMot.Acm2_GetAvailableDevs(self.devlist, self.maxEnt, byref(self.outEnt))
        self.assertEqual(except_err, self.errCde, '{0} failed'.format(self._testMethodName))
        for i in range(self.outEnt.value):
            print(f'{Fore.LIGHTBLUE_EX}Device number:{self.devlist[i].dwDeviceNum:x}')
        self.errCde = self.AdvMot.Acm2_DevInitialize()
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))

    def _ClearLinkedDo(self, SWCmpChId):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        clearVal = c_uint32(0xFFFFFFFF)
        getLinkedDo = c_uint32(0)
        # 清除軟體比較觸發通道綁定的 Do
        self.errCde = self.AdvMot.Acm2_ChLinkSWCmp(SWCmpChId, clearVal)
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Clear SWCmp:{SWCmpChId.value}, Acm2_ChLinkSWCmp failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Acm2_ChLinkSWCmp failed, errCde:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_ChGetLinkedSWCmp(SWCmpChId, byref(getLinkedDo))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Acm2_ChGetLinkedSWCmp failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Acm2_ChGetLinkedSWCmp failed, errCde:{self.errCde:x}')
        self._PrintResult(True, f'Clear SWCmpCh:{SWCmpChId.value} linked DoCh successed')

    def _LinkedDo(self, SWCmpChId, DoChId):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        getLinkedDo = c_uint32(0)
        self.errCde = self.AdvMot.Acm2_ChLinkSWCmp(SWCmpChId, DoChId)
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Set SWCmpChId:{SWCmpChId.value} link DoChId:{DoChId} failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde,
                            f'SWCmpChId:{SWCmpChId.value} linked DoChId:{DoChId} failed, errCde:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_ChGetLinkedSWCmp(SWCmpChId, byref(getLinkedDo))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get SWCmpChId:{SWCmpChId.value} failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde,
                            f'SWCmpChId:{SWCmpChId.value} get linked DoChId:{getLinkedDo.value} failed, errCde:{self.errCde:x}')
        self._PrintResult(True, f'SWCmpCh:{SWCmpChId.value} linked DoCh:{getLinkedDo.value} successed')

    def _ClearLinkedObj(self, SWCmpChId, objType, linkedArr):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        getLinkedCnt = c_uint32(10)
        getLinkedArr = (c_uint32 * getLinkedCnt.value)()
        getLinkedObj = c_uint(0)
        transArr = (c_uint32 * len(linkedArr))(*linkedArr)
        # 清除軟體比較觸發通道綁定的 Axis/Counter
        self.errCde = self.AdvMot.Acm2_ChLinkCmpObject(SWCmpChId, objType.value, transArr, c_uint32(0))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Clear SWCmpCh:{SWCmpChId.value} link {objType.name} failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Acm2_ChLinkCmpObject failed, errCde:{self.errCde}')
        self.errCde = self.AdvMot.Acm2_ChGetLinkedCmpObject(SWCmpChId, byref(getLinkedObj), getLinkedArr, byref(getLinkedCnt))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get SWCmpCh:{SWCmpChId.value} linked failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Acm2_ChGetLinkedCmpObject failed, errCde:{self.errCde}')
        self._PrintResult(True, f'Clear SWCmpCh:{SWCmpChId.value} linked {objType.name}')
        for i in range(getLinkedCnt.value):
            self._PrintResult(True, f'Clear Link {objType.name}:{getLinkedArr[i].value}')

    def _LinkedObj(self, SWCmpChId, objType, linkedArr):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        getLinkedCnt = c_uint32(10)
        getLinkedArr = (c_uint32 * getLinkedCnt.value)()
        getLinkedObj = c_uint(0)
        transArr = (c_uint32 * len(linkedArr))(*linkedArr)
        # 綁定軟體比較觸發通道的 Axis/Counter
        for i in range(len(linkedArr)):
            print(f'{Fore.CYAN}Link to {objType.name}:{linkedArr[i].value}')
        self.errCde = self.AdvMot.Acm2_ChLinkCmpObject(SWCmpChId, objType.value, transArr, len(linkedArr))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'SWCmpCh:{SWCmpChId.value} link {objType.name} failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Acm2_ChLinkCmpObject failed, errCde:{self.errCde}')
        self.errCde = self.AdvMot.Acm2_ChGetLinkedCmpObject(SWCmpChId, byref(getLinkedObj), getLinkedArr, byref(getLinkedCnt))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get SWCmpCh:{SWCmpChId.value} linked failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Acm2_ChGetLinkedCmpObject failed, errCde:{self.errCde}')
        for i in range(getLinkedCnt.value):
            self._PrintResult(True, f'SWCmpCh:{SWCmpChId.value} linked {objType.name}:{getLinkedArr[i]} successed')

    def _SetPropertyBound(self, SWCmpChId, ppt, setVal, errorCode):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        getVal = c_double(0)
        self.errCde = self.AdvMot.Acm2_SetProperty(SWCmpChId, ppt, setVal)
        if self.errCde != errorCode:
            self._PrintResult(False,
                              f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value} failed, errCde:{self.errCde:x}')
            self.assertNotEqual(errorCode, self.errCde,
                             f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value} failed, errCde:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_GetProperty(SWCmpChId, ppt, byref(getVal))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get {self.AdvPpt(ppt.value).name} failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde,
                             f'Get {self.AdvPpt(ppt.value).name} failed, errCde:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value}, get:{getVal.value}')

    def _SetProperty(self, id, ppt, setVal):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        getVal = c_double(0)
        self.errCde = self.AdvMot.Acm2_SetProperty(id, ppt, setVal)
        if self.errCde != except_err.value:
            self._PrintResult(False,
                        f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value} failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde,
                        f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value} failed, errCde:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_GetProperty(id, ppt, byref(getVal))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get {self.AdvPpt(ppt.value).name} failed')
            self.assertEqual(except_err.value, self.errCde, f'Get {self.AdvPpt(ppt.value).name} failed')
        if getVal.value != setVal.value:
            self._PrintResult(False,
                            f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value} failed, get:{getVal.value}')
            self.assertEqual(getVal.value, setVal.value,
                             f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value} failed, get:{getVal.value}')
        else:
            self._PrintResult(True, f'Set {self.AdvPpt(ppt.value).name} value:{getVal.value} successed')

    def _ResetAxis(self, axid, posType):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        setPos = c_double(0)
        getPos = c_double(0)
        self.errCde = self.AdvMot.Acm2_AxResetError(axid)
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Axis:{axid.value} reset error failed')
            self.assertEqual(except_err.value, self.errCde, f'Reset axis:{axid.value} error failed, errCde:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_AxSetPosition(axid, posType, setPos)
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Reset axis:{axid.value} {POSITION_TYPE(posType.value).name} position failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Reset axis:{axid.value} position failed, errCde:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_AxGetPosition(axid, posType, byref(getPos))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get axis:{axid.value} position failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Get axis:{axid.value} position failed, errCde:{self.errCde:x}')
        if getPos.value != setPos.value:
            self._PrintResult(False, f'Reset axis:{axid.value} position failed, position is:{getPos.value}')
            self.assertEqual(setPos.value, getPos.value, f'Reset axis:{axid.value} position failed, position is:{getPos.value}')
        self._PrintResult(True, f'Reset axis:{axid.value} successed')

    def _AxCheckState(self, axid, state, posType):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        getState = c_uint32(16)
        stateType = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
        getPos = c_double(0)
        self.errCde = self.AdvMot.Acm2_AxGetState(axid, stateType, byref(getState))
        while getState.value != state:
            print(f'{Fore.BLUE}Not Ready, state:{AXIS_STATE(getState.value).name}, cur_pos:{getPos.value}', end='\r')
            if except_err.value != self.errCde:
                self._PrintResult(False, f'Get axis:{axid.value} state failed')
                self.assertEqual(except_err.value, self.errCde, f'Get axis:{axid.value} state failed')
            time.sleep(0.5)
            self.errCde = self.AdvMot.Acm2_AxGetState(axid, stateType, byref(getState))
            time.sleep(0.5)
            self.errCde = self.AdvMot.Acm2_AxGetPosition(axid, posType, byref(getPos))
        self._PrintResult(True, f'Axis:{axid.value} state:{AXIS_STATE(getState.value).name}')

    def _AxSetSpeed(self, axid):
        speed_profile = SPEED_PROFILE_PRM()
        speed_profile.FH = c_double(4000)
        speed_profile.FL = c_double(1000)
        speed_profile.Acc = c_double(5000)
        speed_profile.Dec = c_double(1000)
        pptArr = [c_uint32(self.AdvPpt.PAR_AxVelLow.value), c_uint32(self.AdvPpt.PAR_AxVelHigh.value),
                  c_uint32(self.AdvPpt.PAR_AxAcc.value), c_uint32(self.AdvPpt.PAR_AxDec.value)]
        setVal = [c_double(1000), c_double(4000), c_double(5000), c_double(1000)]
        for i in range(len(pptArr)):
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Axis:{axid.value} {self.AdvPpt(pptArr[i].value).name}:{setVal[i].value}]')
            self._SetProperty(axid, pptArr[i], setVal[i])

    def _AxPTP(self, axid, mode, targetPos, posType):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        getPos = c_double(-1)
        state = AXIS_STATE.STA_AX_READY.value
        self._AxSetSpeed(axid)
        self.errCde = self.AdvMot.Acm2_AxPTP(axid, mode, targetPos)
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Axis:{axid.value} PTP failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Axis:{axid} PTP failed, errCde:{self.errCde:x}')
        self._AxCheckState(axid, state, posType)
        self.errCde = self.AdvMot.Acm2_AxGetPosition(axid, posType, byref(getPos))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get axis:{axid.value} position failed, errCde:{self.errCde}')
            self.assertEqual(except_err.value, self.errCde, f'Get axis:{axid.value} position failed, errCde:{self.errCde}')
        if getPos.value != targetPos.value:
            self._PrintResult(False, f'Axis:{axid.value} PTP target position at:{targetPos.value}, but end at:{getPos.value}')
            self.assertEqual(targetPos.value, getPos.value,
                             f'Axis:{axid.value} PTP target position at:{targetPos.value}, but end at:{getPos.value}')
        self._PrintResult(True, f'Axis:{axid.value} PTP done, end at:{getPos.value}')

    def _GpSetSpeed(self, gpid):
        pptArr = [c_uint32(self.AdvPpt.PAR_GpVelLow.value), c_uint32(self.AdvPpt.PAR_GpVelHigh.value),
                  c_uint32(self.AdvPpt.PAR_GpAcc.value), c_uint32(self.AdvPpt.PAR_GpDec.value)]
        setVal = [c_double(1000), c_double(4000), c_double(5000), c_double(1000)]
        for i in range(len(pptArr)):
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Group:{gpid.value} {self.AdvPpt(pptArr[i].value).name}:{setVal[i].value}]')
            self._SetProperty(gpid, pptArr[i], setVal[i])

    def _GpCheckState(self, gpId, gpArr):
        state = GROUP_STATE.STA_GP_READY
        posType = c_uint(POSITION_TYPE.POSITION_CMD.value)
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        getState = c_uint32(12)
        getPos = c_double(0)
        self.errCde = self.AdvMot.Acm2_GpGetState(gpId, byref(getState))
        while getState.value != state.value:
            print(f'{Fore.BLUE}Not Ready, state:{GROUP_STATE(getState.value).name}, ax:{gpArr[0].value} cur_pos:{getPos.value}', end='\r')
            if except_err.value != self.errCde:
                self._PrintResult(False, f'Get group:{gpId.value} state failed:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get group:{gpId.value} state failed:{self.errCde:x}')
            time.sleep(0.5)
            self.errCde = self.AdvMot.Acm2_GpGetState(gpId, byref(getState))
            self.errCde = self.AdvMot.Acm2_AxGetPosition(gpArr[0], posType, byref(getPos))
        self._PrintResult(True, f'Group:{gpId.value} state:{GROUP_STATE(getState.value).name}')

    def _GpMoveLinearRel(self, axesArr, endArr):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        posType = c_uint(POSITION_TYPE.POSITION_CMD.value)
        gpId = c_uint32(0)
        gpArrTrans = (c_uint32 * len(axesArr))(*axesArr)
        gpMoveMode = GP_LINE_MODE.LINE_REL
        endArrTrans = (c_double * len(endArr))(*endArr)
        endArrLen = c_uint32(len(endArr))
        getAxPos = c_double(0)
        # 清除群組綁定的軸
        self.errCde = self.AdvMot.Acm2_GpCreate(gpId, gpArrTrans, 0)
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Reset group failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Reset group failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'[Reset][Axes in group]')
        # 創建群組且綁定軸
        self.errCde = self.AdvMot.Acm2_GpCreate(gpId, gpArrTrans, len(axesArr))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Create group failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Create group failed:{self.errCde:x}')
        # 確認群組軸數正確
        getGpAxesCnt = c_uint32(64)
        getGpAxes = (c_uint32 * getGpAxesCnt.value)()
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gpId, getGpAxes, getGpAxesCnt)
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get axes in group failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Get axes in group failed:{self.errCde:x}')
        else:
            for i in range(getGpAxesCnt.value):
                if axesArr[i].value != getGpAxes[i]:
                    self._PrintResult(False, f'Set ax:{axesArr[i].value}, but get:{getGpAxes[i]}')
                    self.assertEqual(axesArr[i].value, getGpAxes[i], f'Set ax:{axesArr[i]}, but get:{getGpAxes[i]}')
            self._PrintResult(True, f'[Create][Axes:{axesArr[0].value}, {axesArr[1].value} in group:{gpId.value}]')
        # 設定群組速度
        self._GpSetSpeed(gpId)
        # 群組移動
        print(f'{Fore.CYAN}[Start move group in {gpMoveMode.name} mode, end at:{endArr[0].value}]')
        self.errCde = self.AdvMot.Acm2_GpLine(gpId, gpMoveMode.value, endArrTrans, byref(endArrLen))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Group move line failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Group move line failed:{self.errCde:x}')
        time.sleep(0.5)
        self._GpCheckState(gpId, axesArr)
        self.errCde = self.AdvMot.Acm2_AxGetPosition(axesArr[0], posType, byref(getAxPos))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get ax:{axesArr[0].value} position failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Get ax:{axesArr[0].value} position failed:{self.errCde:x}')
        if getAxPos.value != endArr[0].value:
            self._PrintResult(False, f'Ax:{axesArr[0].value} target position at:{endArr[0].value}, but end at:{getAxPos.value}')
            self.assertEqual(endArr[0].value, getAxPos.value, f'Ax:{axesArr[0].value} target position at:{endArr[0].value}, but end at:{getAxPos.value}')
        else:
            self._PrintResult(True, f'Group:{gpId.value} move {gpMoveMode.name} mode done, end at:{getAxPos.value}')
        # 清除群組綁定的軸
        self.errCde = self.AdvMot.Acm2_GpCreate(gpId, gpArrTrans, 0)
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Reset group failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Reset group failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'[Reset][Axes in group]')

    def _OnOffCmp(self, SWCmpChId, onOff):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        getVal = c_double(-1)
        self.errCde = self.AdvMot.Acm2_ChEnableCmp(SWCmpChId, onOff)
        if self.errCde != except_err.value:
            self._PrintResult(False,
                f'Enable SWCmp failed:{self.errCde:x}' if onOff is COMPARE_ENABLE.CMP_ENABLE.value else f'Disable SWCmp failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde,
                f'Enable SWCmp failed:{self.errCde:x}' if onOff is COMPARE_ENABLE.CMP_ENABLE.value else f'Disable SWCmp failed:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_GetProperty(SWCmpChId, self.AdvPpt.CFG_CH_DaqSWCmpDoEnable.value, byref(getVal))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get {self.AdvPpt.CFG_CH_DaqSWCmpDoEnable.name} failed, errCde:{self.errCde}')
            self.assertEqual(except_err.value, self.errCde,
                             f'Get {self.AdvPpt.CFG_CH_DaqSWCmpDoEnable.name} failed, errCde:{self.errCde}')
        if  int(getVal.value) != onOff:
            self._PrintResult(False, f'Set {self.AdvPpt.CFG_CH_DaqSWCmpDoEnable.name}:{onOff}, get:{getVal.value}')
            self.assertEqual(onOff, getVal.value,
                             f'Set {self.AdvPpt.CFG_CH_DaqSWCmpDoEnable.name}:{onOff}, get:{getVal.value}')
        else:
            self._PrintResult(True,
                f'{'Enable' if onOff is COMPARE_ENABLE.CMP_ENABLE.value else 'Disable'} SWCmp successed')

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
        errorCode = [ErrorCode2.EC_InvalidCntMultiCmpDeviation.value,
                     ErrorCode2.EC_InvalidCmpDoEnable.value,
                     ErrorCode2.EC_InvalidCmpDoOutputMode.value,
                     ErrorCode2.EC_InvalidCmpDoLogic.value,
                     ErrorCode2.EC_InvalidCmpDoPulseWidth.value,
                     ErrorCode2.InvalidInputParam.value,
                     ErrorCode2.EC_InvalidCntCmpMethod.value]
        lowerBound = c_double(-1)
        for i in range(global_run_swcmpch):
            swCmpCh = c_uint32(i)
            print(f'{Fore.YELLOW}--- SWCmpCh:{i} test start ---')
            link_axis = [c_uint32(i)]
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            # 綁定軟體比較觸發通道與 Do
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._LinkedDo(swCmpCh, linkedDo.value)
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

    def swCmpRunAxisSingleTable(self):
        global global_run_swcmpch, global_run_do_mode
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        posType = c_uint(POSITION_TYPE.POSITION_CMD.value)
        linkType = ADV_OBJ_TYPE.ADV_AXIS
        linkedDoCh = c_uint32(0)
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
            swCmpCh = c_uint32(ax)
            linkAxId = c_uint32(ax)
            linkedAxis = [linkAxId]
            getSWCmpBuffer = BUFFER_STATUS()
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
                self._SetProperty(swCmpCh, ppt[i], pptSetVal[i])
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            # 重置軟體比較觸發表格
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Software compare data]')
            self.errCde = self.AdvMot.Acm2_ChResetCmpData(swCmpCh)
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Reset CMP data failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Set CMP data failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Reset CMP data successed')
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(swCmpCh, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            # 設置軟體比較觸發表格
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Software compare data]')
            for idx in range(len(setCmpTableArr)):
                if idx != len(setCmpTableArr) - 1:
                    print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}', end= ' ')
                else:
                    print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}')
            self.errCde = self.AdvMot.Acm2_ChSetCmpBufferData(swCmpCh, transCmpTableArr, len(setCmpTableArr))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Set CMP data failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Set CMP data failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Set CMP data successed')
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(swCmpCh, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            # 啟動軟體比較觸發
            print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_ENABLE.value)
            # 使軸運動
            print(f'{Fore.CYAN}[Move]{Fore.LIGHTBLUE_EX}[Axis:{linkAxId.value} move {ABS_MODE(axMoveMode).name} to {endPos.value}]')
            self._AxPTP(linkAxId, axMoveMode, endPos, posType)
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(swCmpCh, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            print(f'{Fore.YELLOW}--- End test SWCmp:{swCmpCh.value} ---')
            print(f'{Fore.BLUE}***** Initializing (SWCmp:{swCmpCh.value} single axis:{linkAxId.value}) *****')
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            # 清除軸錯誤, 設置軸位置為 0
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Axis reset error, and reset position]')
            self._ResetAxis(linkAxId, posType)
            # 設置軟體比較觸發輸出模式回初始值
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Reset property back to default value]')
            for i in range(len(ppt)):
                self._SetProperty(swCmpCh, ppt[i], defaultPptVal[i])
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
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        posType = c_uint(POSITION_TYPE.POSITION_CMD.value)
        linkType = ADV_OBJ_TYPE.ADV_AXIS
        endPos = c_double(31000)
        axMoveMode = ABS_MODE.MOVE_REL.value
        linkedDoCh = c_uint32(0)
        if global_run_do_mode.value == COMPARE_OUTPUT_MODE.CMP_TOGGLE.value:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value), c_double(500)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0)]
        else:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value),
                c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoPulseWidth.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(500), c_double(0.5*1000*1000)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0), c_double(0)]
        startPos = c_double(5000)
        autoEndPos = c_double(30000)
        interval = c_double(5000)

        for ax in range(global_run_swcmpch):
            swCmpCh = c_uint32(ax)
            linkAxId = c_uint32(ax)
            linkedAxis = [linkAxId]
            getSWCmpBuffer = BUFFER_STATUS()
            print(f'{Fore.YELLOW}--- Start test [SWCmp:{swCmpCh.value}] single [axis:{linkAxId.value}] with auto, ({global_run_do_mode.name} mode) ---')
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
                self._SetProperty(swCmpCh, ppt[i], pptSetVal[i])
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            # 重置軟體比較觸發表格
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Software compare data]')
            self.errCde = self.AdvMot.Acm2_ChResetCmpData(swCmpCh)
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Reset CMP data failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Set CMP data failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Reset CMP data successed')
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(swCmpCh, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            # 設置軟體比較觸發自動觸發
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Software compare data]')
            print(f'{Fore.LIGHTBLUE_EX}Start pos:{startPos.value}, interval:{interval.value}, end pos:{autoEndPos.value}')
            self.errCde = self.AdvMot.Acm2_ChSetCmpAuto(swCmpCh, startPos, autoEndPos, interval)
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Set CMP data failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Set CMP data failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Set CMP data successed')
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(swCmpCh, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            # 讀取軟體比較數值
            getCmpDataCnt = c_uint32(10)
            getCmpDataArr = (c_double * getCmpDataCnt.value)()
            self.errCde = self.AdvMot.Acm2_ChGetCmpData(swCmpCh, getCmpDataArr, getCmpDataCnt)
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Acm2_ChGetCmpData failed:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Acm2_ChGetCmpData failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP data successed')
                for j in range(getCmpDataCnt.value):
                    if getCmpDataArr[j] != 0:
                        if j != getCmpDataCnt.value - 1:
                            print(f'{Fore.LIGHTBLUE_EX}{getCmpDataArr[j]}', end=' ')
                        else:
                            print(f'{Fore.LIGHTBLUE_EX}{getCmpDataArr[j]}')
            # 啟動軟體比較觸發
            print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_ENABLE.value)
            # 使軸運動
            print(f'{Fore.CYAN}[Move]{Fore.LIGHTBLUE_EX}[Axis:{linkAxId.value} move {ABS_MODE(axMoveMode).name} to {endPos.value}]')
            self._AxPTP(linkAxId, axMoveMode, endPos, posType)
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(swCmpCh, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            print(f'{Fore.YELLOW}--- End test SWCmp:{swCmpCh.value} ---')
            print(f'{Fore.BLUE}***** Initializing *****')
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            # 清除軸錯誤, 設置軸位置為 0
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Axis reset error, and reset position]')
            self._ResetAxis(linkAxId, posType)
            # 設置軟體比較觸發輸出模式回初始值
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Reset property back to default value]')
            for i in range(len(ppt)):
                self._SetProperty(swCmpCh, ppt[i], defaultPptVal[i])
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._ClearLinkedObj(swCmpCh, linkType, linkedAxis)
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            print(f'{Fore.BLUE}***** End (SWCmp:{swCmpCh.value} single axis:{linkAxId.value}) *****')
            print('\n')

    def swCmpRunAxesTable(self):
        global global_run_swcmpch, global_run_do_mode, global_use_buffer_api
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        posType = c_uint(POSITION_TYPE.POSITION_CMD.value)
        linkType = ADV_OBJ_TYPE.ADV_AXIS
        linkedDoCh = c_uint32(0)
        if global_run_do_mode.value == COMPARE_OUTPUT_MODE.CMP_TOGGLE.value:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value), c_double(500)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0)]
        else:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value),
                c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoPulseWidth.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(500), c_double(0.5*1000*1000)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0), c_double(0)]
        setCmpTableArr = [c_double(5000), c_double(10000), c_double(15000), c_double(20000), c_double(25000), c_double(30000),
                          c_double(5000), c_double(10000), c_double(15000), c_double(20000), c_double(25000), c_double(30000)]
        transCmpTableArr = (c_double * len(setCmpTableArr))(*setCmpTableArr)
        endPosArr = [c_double(31000), c_double(31000)]

        for ax in range(global_run_swcmpch):
            swCmpCh = c_uint32(ax)
            if ax != 63:
                linkedAxes = [c_uint32(ax), c_uint32(ax + 1)]
            else:
                linkedAxes = [c_uint32(ax), c_uint32(0)]
            getSWCmpBuffer = BUFFER_STATUS()
            print(f'{Fore.YELLOW}--- Start test[SWCmp:{swCmpCh.value}] 2 axes[ax_0:{linkedAxes[0].value}, ax_1:{linkedAxes[1].value}] with table, ({global_run_do_mode.name} mode) ---')
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            # 綁定軟體比較觸發通道與 Do
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._LinkedDo(swCmpCh, linkedDoCh)
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to axes]')
            self._ClearLinkedObj(swCmpCh, linkType, linkedAxes)
            # 綁定軟體比較觸發通道與 Axis
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to axes]')
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
                self._SetProperty(swCmpCh, ppt[i], pptSetVal[i])
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            # 重置軟體比較觸發表格
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Software compare data]')
            self.errCde = self.AdvMot.Acm2_ChResetCmpData(swCmpCh)
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Reset CMP data failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Set CMP data failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Reset CMP data successed')
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(swCmpCh, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            # 設置軟體比較觸發表格
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Software compare data]')
            for idx in range(len(setCmpTableArr)):
                if idx != len(setCmpTableArr) - 1:
                    print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}', end= ' ')
                else:
                    print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}')
            if global_use_buffer_api is True:
                self.errCde = self.AdvMot.Acm2_ChSetMultiCmpBufferData(swCmpCh, transCmpTableArr, len(linkedAxes), c_uint32(int(len(setCmpTableArr) / len(linkedAxes))))
            else:
                self.errCde = self.AdvMot.Acm2_ChSetMultiCmpTable(swCmpCh, transCmpTableArr, len(linkedAxes), c_uint32(int(len(setCmpTableArr) / len(linkedAxes))))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Set CMP data failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Set CMP data failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Set CMP data successed')
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(swCmpCh, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            # 啟動軟體比較觸發
            print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_ENABLE.value)
            # 使群組運動
            self._GpMoveLinearRel(linkedAxes, endPosArr)
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(swCmpCh, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            print(f'{Fore.YELLOW}--- End test SWCmp:{swCmpCh.value} ---')
            print(f'{Fore.BLUE}***** Initializing (SWCmp:{swCmpCh.value} 2 axes ax_0:{linkedAxes[0].value}, ax_1:{linkedAxes[1].value}) *****')
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            # 清除軸錯誤, 設置軸位置為 0
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Axis reset error, and reset position]')
            self._ResetAxis(linkedAxes[0], posType)
            self._ResetAxis(linkedAxes[1], posType)
            # 設置軟體比較觸發輸出模式回初始值
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Reset property back to default value]')
            for i in range(len(ppt)):
                self._SetProperty(swCmpCh, ppt[i], defaultPptVal[i])
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._ClearLinkedObj(swCmpCh, linkType, linkedAxes)
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            print(f'{Fore.BLUE}***** End (SWCmp:{swCmpCh.value} 2 axes ax_0:{linkedAxes[0].value}, ax_1:{linkedAxes[1].value}) *****')
            print('\n')

    def swCmpRunAxesAuto(self):
        global global_run_swcmpch, global_run_do_mode
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        posType = c_uint(POSITION_TYPE.POSITION_CMD.value)
        linkType = ADV_OBJ_TYPE.ADV_AXIS
        linkedDoCh = c_uint32(0)
        if global_run_do_mode.value == COMPARE_OUTPUT_MODE.CMP_TOGGLE.value:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value), c_double(500)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0)]
        else:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value),
                c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoPulseWidth.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(500), c_double(0.5*1000*1000)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0), c_double(0)]
        startPos = c_double(5000)
        autoEndPos = c_double(30000)
        interval = c_double(5000)
        endPosArr = [c_double(31000), c_double(31000)]

        for ax in range(global_run_swcmpch):
            swCmpCh = c_uint32(ax)
            if ax != 63:
                linkedAxes = [c_uint32(ax), c_uint32(ax + 1)]
            else:
                linkedAxes = [c_uint32(ax), c_uint32(0)]
            getSWCmpBuffer = BUFFER_STATUS()
            print(f'{Fore.YELLOW}--- Start test[SWCmp:{swCmpCh.value}] 2 axes[ax_0:{linkedAxes[0].value}, ax_1:{linkedAxes[1].value}] with auto, ({global_run_do_mode.name} mode) ---')
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            # 綁定軟體比較觸發通道與 Do
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._LinkedDo(swCmpCh, linkedDoCh)
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to axes]')
            self._ClearLinkedObj(swCmpCh, linkType, linkedAxes)
            # 綁定軟體比較觸發通道與 Axis
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to axes]')
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
                self._SetProperty(swCmpCh, ppt[i], pptSetVal[i])
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            # 重置軟體比較觸發表格
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Software compare data]')
            self.errCde = self.AdvMot.Acm2_ChResetCmpData(swCmpCh)
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Reset CMP data failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Set CMP data failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Reset CMP data successed')
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(swCmpCh, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            # 設置軟體比較觸發自動觸發
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Software compare data]')
            print(f'{Fore.LIGHTBLUE_EX}Start pos:{startPos.value}, interval:{interval.value}, end pos:{autoEndPos.value}')
            self.errCde = self.AdvMot.Acm2_ChSetCmpAuto(swCmpCh, startPos, autoEndPos, interval)
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Set CMP data failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Set CMP data failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Set CMP data successed')
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(swCmpCh, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            # 啟動軟體比較觸發
            print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_ENABLE.value)
            # 使群組運動
            self._GpMoveLinearRel(linkedAxes, endPosArr)
            # 獲取軟體比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(swCmpCh, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            print(f'{Fore.YELLOW}--- End test SWCmp:{swCmpCh.value} ---')
            print(f'{Fore.BLUE}***** Initializing (SWCmp:{swCmpCh.value} 2 axes ax_0:{linkedAxes[0].value}, ax_1:{linkedAxes[1].value}) *****')
            # 關閉軟體比較觸發
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(swCmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            # 清除軸錯誤, 設置軸位置為 0
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Axis reset error, and reset position]')
            self._ResetAxis(linkedAxes[0], posType)
            self._ResetAxis(linkedAxes[1], posType)
            # 設置軟體比較觸發輸出模式回初始值
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Reset property back to default value]')
            for i in range(len(ppt)):
                self._SetProperty(swCmpCh, ppt[i], defaultPptVal[i])
            # 清除軟體比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Axis]')
            self._ClearLinkedObj(swCmpCh, linkType, linkedAxes)
            # 清除軟體比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(swCmpCh)
            print(f'{Fore.BLUE}***** End (SWCmp:{swCmpCh.value} 2 axes ax_0:{linkedAxes[0].value}, ax_1:{linkedAxes[1].value}) *****')
            print('\n')


def AdvInitial():
    tests = ['initial']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpTestBoundAxis():
    global global_link_type
    global global_run_swcmpch
    global_run_swcmpch = 1
    global_link_type = ADV_OBJ_TYPE.ADV_AXIS
    tests = ['initial', 'swCmpBoundTestSingle']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpTestBoundCounter():
    global global_link_type
    global global_run_swcmpch
    global_run_swcmpch = 1
    global_link_type = ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL
    tests = ['initial', 'swCmpBoundTestSingle']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRunAxisSingleTableToggle():
    global global_run_swcmpch, global_run_do_mode
    global_run_swcmpch = 1
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    tests = ['initial', 'swCmpRunAxisSingleTable']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRunAxisSingleAutoToggle():
    global global_run_swcmpch, global_run_do_mode
    global_run_swcmpch = 1
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    tests = ['initial', 'swCmpRunAxisSingleAuto']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRunAxisSingleTablePulse():
    global global_run_swcmpch, global_run_do_mode
    global_run_swcmpch = 1
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    tests = ['initial', 'swCmpRunAxisSingleTable']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRunAxisSingleAutoPulse():
    global global_run_swcmpch, global_run_do_mode
    global_run_swcmpch = 1
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    tests = ['initial', 'swCmpRunAxisSingleAuto']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRun2AxesTableToggle():
    global global_run_swcmpch, global_run_do_mode, global_use_buffer_api
    global_run_swcmpch = 1
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    global_use_buffer_api = False
    tests = ['initial', 'swCmpRunAxesTable']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRun2AxesTablePulse():
    global global_run_swcmpch, global_run_do_mode, global_use_buffer_api
    global_run_swcmpch = 1
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    global_use_buffer_api = False
    tests = ['initial', 'swCmpRunAxesTable']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRun2AxesAutoToggle():
    global global_run_swcmpch, global_run_do_mode
    global_run_swcmpch = 1
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    tests = ['initial', 'swCmpRunAxesAuto']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRun2AxesAutoPulse():
    global global_run_swcmpch, global_run_do_mode
    global_run_swcmpch = 1
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    tests = ['initial', 'swCmpRunAxesAuto']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # initial = runner.run(AdvInitial())
    # bound_test_axis = runner.run(SWCmpTestBoundAxis())
    # bound_test_counter = runner.run(SWCmpTestBoundCounter())
    # run_axis_single_table_toggle = runner.run(SWCmpRunAxisSingleTableToggle())
    # run_axis_single_auto_toggle = runner.run(SWCmpRunAxisSingleAutoToggle())
    # run_axis_single_table_pulse = runner.run(SWCmpRunAxisSingleTablePulse())
    # run_axis_single_auto_pulse = runner.run(SWCmpRunAxisSingleAutoPulse())
    # run_axes_table_toggle = runner.run(SWCmpRun2AxesTableToggle())
    # run_axes_table_pulse = runner.run(SWCmpRun2AxesTablePulse())
    # run_axes_auto_toggle = runner.run(SWCmpRun2AxesAutoToggle())
    run_axes_auto_pulse = runner.run(SWCmpRun2AxesAutoPulse())