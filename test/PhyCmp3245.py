import unittest
import os
import sys
import time

# 強制 Windows 使用 ANSI 支援
os.system('')
# # 強制設定 stdout 編碼為 utf-8
sys.stdout.reconfigure(encoding='utf-8')

from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import *
from AcmP.MotionInfo import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from colorama import init, Fore

global_cmp_ch = 0
global_cmp_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
global_use_buffer_api = False
init(autoreset=True, strip=False)

class PhyCmpTest(unittest.TestCase):
    def setUp(self):
        self.errCde = 0
        self.except_err = c_uint32(ErrorCode2.SUCCESS.value)
    # Call once by test case
    @classmethod
    def setUpClass(cls):
        cls.AdvMot = AdvCmnAPI_CM2
        cls.AdvPpt = PropertyID2
        # cls.AdvGpPpt = PropertyGpID
        cls.maxDevCnt = 10
        cls.maxDevList = (DEVLIST * cls.maxDevCnt)()
        cls.maxDev = c_uint32(0)
        cls.devNum = c_uint32(0)
        cls.gpHandle = c_void_p()
    def tearDown(self):
        self.errCde = 0

    def _PrintResult(self, isPass, message):
        if isPass:
            print(f'{Fore.GREEN}[✓ Pass]{message}')
        else:
            print(f'{Fore.RED}[X Fail]{message}')

    def initial(self):
        self.errCde = self.AdvMot.Acm2_GetAvailableDevs(self.maxDevList, self.maxDevCnt, byref(self.maxDev))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Acm2_GetAvailableDevs failed:0x{self.errCde:x}')
            self.assertSetEqual(self.except_err.value, self.errCde, f'Acm2_GetAvailableDevs failed:0x{self.errCde:x}')
        else:
            self._PrintResult(True, f'Acm2_GetAvailableDevs successed')
            for i in range(self.maxDev.value):
                print(f'{Fore.LIGHTBLUE_EX}Device number:{self.maxDevList[i].dwDeviceNum:x}')
            if self.maxDev.value > 0:
                self.devNum.value = self.maxDevList[0].dwDeviceNum
        self.errCde = self.AdvMot.Acm2_DevInitialize()
        self.assertEqual(self.except_err.value, self.errCde, f'Acm2_DevInitialize failed:0x{self.errCde:x}')

    def _ClearLink(self, cmpCH):
        getLinkCnt = c_uint32(10)
        getLinkArr = (c_uint32 * getLinkCnt.value)()
        getLinkObj = c_uint32(0)
        transArr = (c_uint32 * len(getLinkArr))(*getLinkArr)
        # 清除比較觸發通道綁定的 DO
        self.errCde = self.AdvMot.Acm2_ChLinkCmpObject(cmpCH.value, ADV_OBJ_TYPE.ADV_AXIS.value, transArr, c_uint32(0))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Clear CmpCH:{cmpCH.value} failed, errCde:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Acm2_ChLinkCmpObject failed:0x{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_ChGetLinkedCmpObject(cmpCH.value, byref(getLinkObj), getLinkArr, byref(getLinkCnt))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Get CmpCH:{cmpCH.value} linked failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Acm2_ChGetLinkedCmpObject failed:0x{self.errCde:x}')
        self._PrintResult(True, f'Clear CmpCH:{cmpCH.value} successed')
        for i in range(getLinkCnt.value):
            self._PrintResult(True, f'Clear link {ADV_OBJ_TYPE(getLinkObj.value).name}:{getLinkArr[i]}')

    def _Linked(self, cmpCH, linkedArr):
        getLinkCnt = c_uint32(10)
        getLinkArr = (c_uint32 * getLinkCnt.value)()
        getLinkObj = c_uint32(0)
        transArr = (c_uint32 * len(linkedArr))(*linkedArr)
        # 綁定比較觸發通道的
        for i in range(len(linkedArr)):
            print(f'{Fore.CYAN}Link to {ADV_OBJ_TYPE.ADV_AXIS.name}:{linkedArr[i].value}')
        self.errCde = self.AdvMot.Acm2_ChLinkCmpObject(cmpCH.value, ADV_OBJ_TYPE.ADV_AXIS.value, transArr, len(linkedArr))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'CmpCH:{cmpCH.value} link failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Acm2_ChLinkCmpObject failed:0x{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_ChGetLinkedCmpObject(cmpCH.value, byref(getLinkObj), getLinkArr, byref(getLinkCnt))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Get CmpCH:{cmpCH.value} linked failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Acm2_ChGetLinkedCmpObject failed:0x{self.errCde:x}')
        else:
            self._PrintResult(True, f'Link successed, count:{getLinkCnt.value}')
        for i in range(getLinkCnt.value):
            self._PrintResult(True, f'Link {ADV_OBJ_TYPE(getLinkObj.value).name}:{getLinkArr[i]}')

    def _ResetAxis(self, axid, posType):
        setPos = c_double(0)
        getPos = c_double(0)
        self.errCde = self.AdvMot.Acm2_AxResetError(axid)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Axis:{axid.value} reset error failed')
            self.assertEqual(self.except_err.value, self.errCde, f'Reset axis:{axid.value} error failed:0x{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_AxSetPosition(axid, posType, setPos)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Set axis:{axid.value} position failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Set axis:{axid.value} position failed:0x{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_AxGetPosition(axid, posType, byref(getPos))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Get axid:{axid.value} position failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Get axis:{axid.value} position failed:0x{self.errCde:x}')
        if getPos.value != setPos.value:
            self._PrintResult(False, f'Reset axis:{axid.value} position failed, position is:{getPos.value}')
            self.assertEqual(setPos.value, getPos.value, f'Reset axis:{axid.value} position failed, position is:{getPos.value}')
        self._PrintResult(True, f'Reset axis:{axid.value} successed')

    def _CheckState(self, axid, state, posType):
        getState = c_uint32(16)
        stateType = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
        getPos = c_double(0)
        self.errCde = self.AdvMot.Acm2_AxGetState(axid, stateType, byref(getState))
        while getState.value != state:
            print(f'{Fore.BLUE}Not Ready, state:{AXIS_STATE(getState.value).name}, cur_pos:{getPos.value}', end='\r')
            if self.except_err.value != self.errCde:
                self._PrintResult(False, f'Get axis:{axid.value} state failed')
                self.assertEqual(self.except_err.value, self.errCde, f'Get axid:{axid.type} state failed')
            time.sleep(0.5)
            self.errCde = self.AdvMot.Acm2_AxGetState(axid, posType, byref(getState))
            time.sleep(0.5)
            self.errCde = self.AdvMot.Acm2_AxGetPosition(axid, posType, byref(getPos))
        self._PrintResult(True, f'Axid:{axid.value} state:{AXIS_STATE(getState.value).name}')

    def _SetProperty(self, id, ppt, setVal):
        getVal = c_double(0)
        self.errCde = self.AdvMot.Acm2_SetProperty(id, ppt, setVal)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value} failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value} failed:0x{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_GetProperty(id, ppt, byref(getVal))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Get {self.AdvPpt(ppt.value).name} failed')
            self.assertEqual(self.except_err.value, self.errCde, f'Get {self.AdvPpt(ppt.value).name} failed')
        if getVal.value != setVal.value:
            self._PrintResult(False, f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value} failed, get:{getVal.value}')
            self.assertEqual(getVal.value, setVal.value, f'Set {self.AdvPpt(ppt.value).name} value:{setVal.value}, get:{getVal.value}')
        else:
            self._PrintResult(True, f'Set {self.AdvPpt(ppt.value).name} value:{getVal.value} successed')


    def _AxSetSpeed(self, axid):
        speedProfile = SPEED_PROFILE_PRM()
        speedProfile.FH = c_double(4000)
        speedProfile.FL = c_double(1000)
        speedProfile.Acc = c_double(1000)
        speedProfile.Dec = c_double(1000)
        pptArr = [c_uint32(self.AdvPpt.PAR_AxVelLow.value), c_uint32(self.AdvPpt.PAR_AxVelHigh.value),
                  c_uint32(self.AdvPpt.PAR_AxAcc.value), c_uint32(self.AdvPpt.PAR_AxDec.value)]
        setVal = [c_double(1000), c_double(4000), c_double(1000), c_double(1000)]
        for i in range(len(pptArr)):
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Axis:{axid.value} {self.AdvPpt(pptArr[i].value).name}:{setVal[i].value}]')
            self._SetProperty(axid, pptArr[i], setVal[i])

    def _AxPTP(self, axid, mode, targetPos, posType):
        getPos = c_double(-1)
        state = AXIS_STATE.STA_AX_READY.value
        self._AxSetSpeed(axid)
        self.errCde = self.AdvMot.Acm2_AxPTP(axid, mode, targetPos)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Axis:{axid.value} PTP failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Axis:{axid} PTP failed:0x{self.errCde:x}')
        self._CheckState(axid, state, posType)
        self.errCde = self.AdvMot.Acm2_AxGetPosition(axid, posType, byref(getPos))
        if self.errCde != targetPos.value:
            self._PrintResult(False, f'Get Axis:{axid.value} position failed:0x{self.errCde}')
            self.assertEqual(self.except_err.value, self.errCde, f'Get axis:{axid.value} position failed:{self.errCde}')
        if getPos.value != targetPos.value:
            self._PrintResult(False, f'Axis:{axid.value} PTP target position at:{targetPos.value}, but end at:{getPos.value}')
            self.assertEqual(targetPos.value, getPos.value, f'Axis:{axid.value} PTP target position at:{targetPos.value}, but end at:{getPos.value}')
        self._PrintResult(True, f'Axis:{axid.value} PTP done, end at:{getPos.value}')

    def _GpSetSpeed(self, gpid):
        pptArr = [c_uint32(self.AdvPpt.PAR_GpVelLow.value), c_uint32(self.AdvPpt.PAR_GpVelHigh.value),
                  c_uint32(self.AdvPpt.PAR_GpAcc.value), c_uint32(self.AdvPpt.PAR_GpDec.value)]
        setVal = [c_double(1000), c_double(4000), c_double(1000), c_double(1000)]
        for i in range(len(pptArr)):
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Group:{gpid.value} {self.AdvPpt(pptArr[i].value).name}:{setVal[i].value}]')
            self._SetProperty(gpid, pptArr[i], setVal[i])

    def _GpCheckState(self, gpId, gpArr):
        state = GROUP_STATE.STA_GP_READY
        posType = c_uint(POSITION_TYPE.POSITION_CMD.value)
        getState = c_uint32(12)
        getPos = c_double(0)
        self.errCde = self.AdvMot.Acm2_GpGetState(gpId, byref(getState))
        while getState.value != state.value:
            print(f'{Fore.BLUE}Not Ready, state:{GROUP_STATE(getState.value).name}, ax:{gpArr[0].value} cur_pos:{getPos.value}', end='\r')
            if self.except_err.value != self.errCde:
                self._PrintResult(False, f'Get group:{gpId.value} state failed:{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get group:{gpId.value} state failed:{self.errCde:x}')
            time.sleep(0.5)
            self.errCde = self.AdvMot.Acm2_GpGetState(gpId, byref(getState))
            self.errCde = self.AdvMot.Acm2_AxGetPosition(gpArr[0], posType, byref(getPos))
        self._PrintResult(True, f'Group:{gpId.value} state:{GROUP_STATE(getState.value).name}')

    def _GpMoveLinearRel(self, axesArr, endArr):
        posType = c_uint(POSITION_TYPE.POSITION_CMD.value)
        gpId = c_uint32(0)
        gpArrTrans = (c_uint32 * len(axesArr))(*axesArr)
        gpMoveMode = GP_LINE_MODE.LINE_REL
        endArrTrans = (c_double * len(endArr))(*endArr)
        endArrLen = c_uint32(len(endArr))
        getAxPos = c_double(0)
        # 清除群組綁定的軸
        self.errCde = self.AdvMot.Acm2_GpCreate(gpId, gpArrTrans, 0)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Reset group failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Reset group failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'[Reset][Axes in group]')
        # 創建群組且綁定軸
        self.errCde = self.AdvMot.Acm2_GpCreate(gpId, gpArrTrans, len(axesArr))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Create group failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Create group failed:0x{self.errCde:x}')
        # 確認群組軸數正確
        getGpAxesCnt = c_uint32(64)
        getGpAxes = (c_uint32 * getGpAxesCnt.value)()
        self.errCde = self.AdvMot.Acm2_GpGetAxesInGroup(gpId, getGpAxes, getGpAxesCnt)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Get axes in group failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Get axes in group failed:0x{self.errCde:x}')
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
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Group move line failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Group move line failed:0x{self.errCde:x}')
        time.sleep(0.5)
        self._GpCheckState(gpId, axesArr)
        self.errCde = self.AdvMot.Acm2_AxGetPosition(axesArr[0], posType, byref(getAxPos))
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Get ax:{axesArr[0].value} position failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Get ax:{axesArr[0].value} position failed:0x{self.errCde:x}')
        if getAxPos.value != endArr[0].value:
            self._PrintResult(False, f'Ax:{axesArr[0].value} target position at:{endArr[0].value}, but end at:{getAxPos.value}')
            self.assertEqual(endArr[0].value, getAxPos.value, f'Ax:{axesArr[0].value} target position at:{endArr[0].value}, but end at:{getAxPos.value}')
        else:
            self._PrintResult(True, f'Group:{gpId.value} move {gpMoveMode.name} mode done, end at:{getAxPos.value}')
        # 清除群組綁定的軸
        self.errCde = self.AdvMot.Acm2_GpCreate(gpId, gpArrTrans, 0)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Reset group failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Reset group failed:0x{self.errCde:x}')
        else:
            self._PrintResult(True, f'[Reset][Axes in group]')

    def _OnOffCmp(self, cmpCh, onOff):
        getVal = c_double(-1)
        self.errCde = self.AdvMot.Acm2_ChEnableCmp(cmpCh, onOff)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Enable Cmp failed:0x{self.errCde:x}' if onOff is COMPARE_ENABLE.CMP_ENABLE.value else f'Disable Cmp failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Enable Cmp failed:0x{self.errCde:x}' if onOff is COMPARE_ENABLE.CMP_ENABLE.value else f'Disable Cmp failed:0x{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_SetProperty(cmpCh, self.AdvPpt.CFG_DevMultiCmpAxisEnable.value, onOff)
        if self.errCde != self.except_err.value:
            self._PrintResult(False, f'Set {self.AdvPpt.CFG_DevMultiCmpAxisEnable.name} failed:0x{self.errCde:x}')
            self.assertEqual(self.except_err.value, self.errCde, f'Set {self.AdvPpt.CFG_DevMultiCmpAxisEnable.name} failed:0x{self.errCde:x}')
        # self.errCde = self.AdvMot.Acm2_GetProperty(cmpCh, self.AdvPpt.CFG_CH_DaqCmpDoEnable.value, byref(getVal))
        # if self.errCde != self.except_err.value:
        #     self._PrintResult(False, f'Get {self.AdvPpt.CFG_CH_DaqCmpDoEnable.name} failed:0x{self.errCde:x}')
        #     self.assertEqual(self.except_err.value, self.errCde, f'Get {self.AdvPpt.CFG_CH_DaqCmpDoEnable.name} failed:0x{self.errCde:x}')
        # if int(getVal.value) != onOff:
        #     self._PrintResult(False, f'Set {self.AdvPpt.CFG_CH_DaqCmpDoEnable.name}:{onOff}, get:{getVal.value}')
        #     self.assertEqual(onOff, getVal.value, f'Set {self.AdvPpt.CFG_CH_DaqCmpDoEnable.name}:{onOff}, get:{getVal.value}')
        # else:
        #     self._PrintResult(True, f'{'Enable' if onOff is COMPARE_ENABLE.CMP_ENABLE.value else 'Disable'} cmp successed')

    def CmpRunAxesTable(self):
        global global_cmp_ch, global_cmp_do_mode, global_use_buffer_api
        posType = c_uint(POSITION_TYPE.POSITION_CMD.value)
        if global_cmp_do_mode.value == COMPARE_OUTPUT_MODE.CMP_TOGGLE.value:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqCmpDeviation.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value), c_double(500)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0)]
        else:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqCmpDeviation.value),
                   c_uint32(self.AdvPpt.CFG_CH_DaqCmpDoPulseWidth.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(500), c_double(0.5*1000*1000)]
            defaultPptVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0), c_double(0)]
        setCmpTableArr = [c_double(5000), c_double(10000), c_double(15000), c_double(20000), c_double(25000), c_double(30000),
                          c_double(5000), c_double(10000), c_double(15000), c_double(20000), c_double(25000), c_double(30000)]
        transCmpTableArr = (c_double * len(setCmpTableArr))(*setCmpTableArr)
        endPosArr = [c_double(31000), c_double(31000)]

        for ax in range(global_cmp_ch):
            cmpCh = c_uint32(ax)
            if ax != 63:
                linkedAxes = [c_uint32(ax), c_uint32(ax + 1)]
            else:
                linkedAxes = [c_uint32(ax), c_uint32(0)]
            getCmpBuffer = BUFFER_STATUS()
            print(f'{Fore.YELLOW} --- Start test[Cmp:{cmpCh.value}] 2 axes[ax_0:{linkedAxes[0].value}, ax_1:{linkedAxes[1].value}] with table, ({global_cmp_do_mode.name} mode)')
            # 清除比較觸發通道綁定的 Do
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Compare channel]')
            self._ClearLink(cmpCh)
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Compare channel linked to DO]')
            self._Linked(cmpCh, linkedAxes)
            # 清除軸錯誤, 設置軸位置為 0
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Axis reset error, and reset position]')
            self._ResetAxis(linkedAxes[0], posType)
            self._ResetAxis(linkedAxes[1], posType)
            # 設置比較觸發屬性
            for i in range(len(ppt)):
                if ppt[i].value == self.AdvPpt.CFG_CH_DaqCmpDoOutputMode.value:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Do output mode:{COMPARE_OUTPUT_MODE(pptSetVal[i].value).name}]')
                elif ppt[i].value == self.AdvPpt.CFG_CH_DaqCmpDeviation.value:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[CMP deviation:{pptSetVal[i].value}]')
                else:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[{self.AdvPpt(ppt[i].value).name:{pptSetVal[i].value}}]')
                self._SetProperty(cmpCh, ppt[i], pptSetVal[i])
            # 關閉比較觸發
            # print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Compare]')
            # self._OnOffCmp(cmpCh, COMPARE_ENABLE.CMP_DISABLE.value)
            # 重置比較觸發表格
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Compare data]')
            self.errCde = self.AdvMot.Acm2_ChResetCmpData(cmpCh)
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Reset CMP data failed:0x{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Set CMP data failed:0x{self.errCde:x}')
            else:
                self._PrintResult(True, f'Reset CMP data successed')
            # 獲取比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(cmpCh, byref(getCmpBuffer))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed:0x{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get CMP buffer failed:0x{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getCmpBuffer.CurIndex}, RemainCount:{getCmpBuffer.RemainCount}, FreeSpaceCount:{getCmpBuffer.FreeSpaceCount})')
            getLinkCnt = c_uint32(10)
            getLinkArr = (c_uint32 * getLinkCnt.value)()
            getLinkObj = c_uint32(0)
            self.errCde = self.AdvMot.Acm2_ChGetLinkedCmpObject(cmpCh.value, byref(getLinkObj), getLinkArr, byref(getLinkCnt))
            print(f'{Fore.RED}getLinkCnt:{getLinkCnt.value}')

            # 啟動軟體比較觸發
            print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Compare]')
            self._OnOffCmp(cmpCh, COMPARE_ENABLE.CMP_ENABLE.value)

            getLinkCnt = c_uint32(10)
            getLinkArr = (c_uint32 * getLinkCnt.value)()
            getLinkObj = c_uint32(0)
            self.errCde = self.AdvMot.Acm2_ChGetLinkedCmpObject(cmpCh.value, byref(getLinkObj), getLinkArr, byref(getLinkCnt))
            print(f'{Fore.RED}getLinkCnt:{getLinkCnt.value}')
            # 設置比較觸發表格
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Compare data]')
            for idx in range(len(setCmpTableArr)):
                if idx != len(setCmpTableArr) - 1:
                    print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}', end=' ')
                else:
                    print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}')
            if global_use_buffer_api is True:
                self.errCde = self.AdvMot.Acm2_ChSetMultiCmpBufferData(cmpCh, transCmpTableArr, len(linkedAxes), c_uint32(int(len(setCmpTableArr) / len(linkedAxes))))
            else:
                self.errCde = self.AdvMot.Acm2_ChSetMultiCmpTable(cmpCh, transCmpTableArr, len(linkedAxes), c_uint32(int(len(setCmpTableArr) / len(linkedAxes))))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Set CMP data failed:0x{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Set CMP data failed:0x{self.errCde:x}')
            else:
                self._PrintResult(True, f'Set CMP data successed')
            # 獲取比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(cmpCh, byref(getCmpBuffer))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed:0x{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get CMP buffer failed:0x{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getCmpBuffer.CurIndex}, RemainCount:{getCmpBuffer.RemainCount}, FreeSpaceCount:{getCmpBuffer.FreeSpaceCount})')
            # 啟動軟體比較觸發
            print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Compare]')
            self._OnOffCmp(cmpCh, COMPARE_ENABLE.CMP_ENABLE.value)
            # 使群組運動
            self._GpMoveLinearRel(linkedAxes, endPosArr)
            # 獲取比較數據狀態
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(cmpCh, byref(getCmpBuffer))
            if self.errCde != self.except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed:0x{self.errCde:x}')
                self.assertEqual(self.except_err.value, self.errCde, f'Get CMP buffer failed:0x{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getCmpBuffer.CurIndex}, RemainCount:{getCmpBuffer.RemainCount}, FreeSpaceCount:{getCmpBuffer.FreeSpaceCount})')
            print(f'{Fore.YELLOW}--- End test CMP:{cmpCh.value} ---')
            print(f'{Fore.BLUE}***** Initializing (CMP:{cmpCh.value} 2 axes) *****')
            # 關閉比較觸發
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Axis reset error, and reset position]')
            self._ResetAxis(linkedAxes[0], posType)
            self._ResetAxis(linkedAxes[1], posType)
            # 設置比較觸發輸出模式回初始值
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Reset property back to default value]')
            for i in range(len(ppt)):
                self._SetProperty(cmpCh, ppt[i], defaultPptVal[i])
            # 清除比較觸發通道綁定的 Axis
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Compare channel linked to Axis]')
            self._ClearLink(cmpCh)
            print(f'{Fore.BLUE}***** End (CMP:{cmpCh.value} 2 axes) *****')
            print('\n')



def AdvInitial():
    tests = ['initial']
    suite = unittest.TestSuite(map(PhyCmpTest, tests))
    return suite

def MultiCMPToggleTable():
    global global_cmp_ch, global_cmp_do_mode, global_use_buffer_api
    global_cmp_ch = 1
    global_cmp_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    global_use_buffer_api = False
    tests = ['initial', 'CmpRunAxesTable']
    suite = unittest.TestSuite(map(PhyCmpTest, tests))
    return suite

def MultiCMPToggleTableBuffer():
    global global_cmp_ch, global_cmp_do_mode, global_use_buffer_api
    global_cmp_ch = 1
    global_cmp_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    global_use_buffer_api = True
    tests = ['initial', 'CmpRunAxesTable']
    suite = unittest.TestSuite(map(PhyCmpTest, tests))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    advinit = runner.run(AdvInitial())
    multiToggleTable = runner.run(MultiCMPToggleTable())
    multiToggleTableBuffer = runner.run(MultiCMPToggleTableBuffer())