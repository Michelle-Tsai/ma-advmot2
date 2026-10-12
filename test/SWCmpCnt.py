import unittest
import os
import sys
import time
import threading

# 強制 Windows 使用 ANSI 支援
os.system('')
# # 強制設定 stdout 編碼為 utf-8
sys.stdout.reconfigure(encoding='utf-8')

from datetime import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from colorama import init, Fore, Style

global_link_type = 0
global_open_axcnt = 1
global_run_swcmpch = 0
global_use_buffer_api = False
global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
global_run_cnt_cnt = 1
global_cnt_arr = [-1, -1]
global_eni_path = b'only4270.xml'
# global_eni_path = b'amax5081.xml'
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
            self._PrintResult(False, f'Clear SWCmp:{SWCmpChId}, Acm2_ChLinkSWCmp failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Acm2_ChLinkSWCmp failed, errCde:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_ChGetLinkedSWCmp(SWCmpChId, byref(getLinkedDo))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Acm2_ChGetLinkedSWCmp failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Acm2_ChGetLinkedSWCmp failed, errCde:{self.errCde:x}')
        self._PrintResult(True, f'Clear SWCmpCh:{SWCmpChId} linked DoCh successed')

    def _LinkedDo(self, SWCmpChId, DoChId):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        getLinkedDo = c_uint32(0)
        self.errCde = self.AdvMot.Acm2_ChLinkSWCmp(SWCmpChId, DoChId)
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Set SWCmpChId:{SWCmpChId} link DoChId:{DoChId} failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde,
                            f'SWCmpChId:{SWCmpChId} linked DoChId:{DoChId} failed, errCde:{self.errCde:x}')
        self.errCde = self.AdvMot.Acm2_ChGetLinkedSWCmp(SWCmpChId, byref(getLinkedDo))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get SWCmpChId:{SWCmpChId} failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde,
                            f'SWCmpChId:{SWCmpChId} get linked DoChId:{getLinkedDo.value} failed, errCde:{self.errCde:x}')
        if getLinkedDo.value == DoChId.value:
            self._PrintResult(True, f'SWCmpCh:{SWCmpChId} linked DoCh:{getLinkedDo.value} successed')
        else:
            self._PrintResult(False, f'SWCmpCh:{SWCmpChId} linked DoCh:{getLinkedDo.value} failed')
            self._PrintResult(False, f'Excepted:{DoChId.value} but get:{getLinkedDo.value}')
            self.assertEqual(DoChId.value, getLinkedDo.value, f'Excepted:{DoChId.value} but get:{getLinkedDo.value}')

    def _ClearLinkedObj(self, SWCmpChId, objType, linkedArr):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        getLinkedCnt = c_uint32(10)
        getLinkedArr = (c_uint32 * getLinkedCnt.value)()
        getLinkedObj = c_uint(0)
        transArr = (c_uint32 * len(linkedArr))(*linkedArr)
        # 清除軟體比較觸發通道綁定的 Axis/Counter
        self.errCde = self.AdvMot.Acm2_ChLinkCmpObject(SWCmpChId, objType.value, transArr, c_uint32(0))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Clear SWCmpCh:{SWCmpChId} link {objType.name} failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Acm2_ChLinkCmpObject failed, errCde:{self.errCde}')
        self.errCde = self.AdvMot.Acm2_ChGetLinkedCmpObject(SWCmpChId, byref(getLinkedObj), getLinkedArr, byref(getLinkedCnt))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get SWCmpCh:{SWCmpChId} linked failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Acm2_ChGetLinkedCmpObject failed, errCde:{self.errCde}')
        self._PrintResult(True, f'Clear SWCmpCh:{SWCmpChId} linked {objType.name}')
        for i in range(getLinkedCnt.value):
            self._PrintResult(True, f'Clear Link {objType.name}:{getLinkedArr[i]}')

    def _LinkedObj(self, SWCmpChId, objType, linkedArr):
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        getLinkedCnt = c_uint32(10)
        getLinkedArr = (c_uint32 * getLinkedCnt.value)()
        getLinkedObj = c_uint(0)
        transArr = (c_uint32 * len(linkedArr))(*linkedArr)
        # 綁定軟體比較觸發通道的 Axis/Counter
        for i in range(len(linkedArr)):
            print(f'{Fore.CYAN}Link to {objType.name}:{linkedArr[i]}')
        self.errCde = self.AdvMot.Acm2_ChLinkCmpObject(SWCmpChId, objType.value, transArr, len(linkedArr))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'SWCmpCh:{SWCmpChId} link {objType.name} failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Acm2_ChLinkCmpObject failed, errCde:{self.errCde}')
        self.errCde = self.AdvMot.Acm2_ChGetLinkedCmpObject(SWCmpChId, byref(getLinkedObj), getLinkedArr, byref(getLinkedCnt))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get SWCmpCh:{SWCmpChId} linked failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Acm2_ChGetLinkedCmpObject failed, errCde:{self.errCde}')
        for i in range(getLinkedCnt.value):
            self._PrintResult(True, f'SWCmpCh:{SWCmpChId} linked {objType.name}:{getLinkedArr[i]} successed')

    def EtherCATInit(self):
        global global_eni_path
        except_err = 0
        self.errCde = self.AdvMot.Acm2_DevLoadENI(0, global_eni_path)
        print(f'{Fore.LIGHTBLUE_EX} ENI Path:{global_eni_path}')
        self.assertEqual(except_err, self.errCde, f'Acm2_DevLoadENI failed:{self.errCde:x}')
        getState = c_uint32(SUB_DEV_STATE.EC_SLAVE_STATE_INIT.value)
        self.errCde = self.AdvMot.Acm2_DevConnect(0)
        self.assertEqual(except_err, self.errCde, f'Failed to StartFieldbus:{self.errCde:x}')
        time.sleep(2)
        self.errCde = self.AdvMot.Acm2_DevGetSubDeviceStates(0, ECAT_ID_TYPE.SUBDEVICE_POS.value, 0, byref(getState))
        self.assertEqual(except_err, self.errCde, f'Acm2_DevGetSubDeviceStates failed:{self.errCde:x}')
        self.assertEqual(SUB_DEV_STATE.EC_SLAVE_STATE_OP.value, getState.value, f'Device state is wrong, get:{SUB_DEV_STATE(getState.value).name}')

    def EtherCATDisConnect(self):
        except_err = 0
        self.errCde = self.AdvMot.Acm2_DevDisConnect(0)
        self.assertEqual(except_err, self.errCde, f'Acm2_DevDisConnect failed:{self.errCde:x}')

    def Reset508xCntValue(self, cnt):
        reset = c_double(0)
        except_err = 0
        for idx in range(cnt):
            print(f'--- {Fore.LIGHTBLUE_EX} Reset counter:{idx} as 0 ---')
            self.errCde = self.AdvMot.Acm2_ChSetCntData(idx, reset)
            self.assertEqual(except_err, self.errCde, f'Acm2_ChSetCntData failed:{self.errCde:x}')

    def SetCntValue(self, cntCh, value):
        except_err = 0
        getVal = c_double(0)
        print(f'--- {Fore.LIGHTBLUE_EX} Set counter:{cntCh} value:{value}')
        self.errCde = self.AdvMot.Acm2_ChSetCntData(cntCh, value)
        self.assertEqual(except_err, self.errCde, f'Acm2_ChSetCntData failed:{self.errCde:x}')
        time.sleep(1)
        self.errCde = self.AdvMot.Acm2_ChGetCntData(cntCh, byref(getVal))
        self.assertEqual(value, getVal.value, f'Set:{value}, but get:{getVal.value}')
        self.assertEqual(except_err, self.errCde, f'Acm2_ChGetCntData failed:{self.errCde:x}')

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

    def TestCmpSingleCntTable(self):
        global global_run_swcmpch, global_run_do_mode, global_use_buffer_api, global_run_cnt_cnt, global_cnt_arr
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        linkedDo = c_uint32(0)
        linkType = ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL
        if global_run_do_mode.value == COMPARE_OUTPUT_MODE.CMP_TOGGLE.value:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value), c_double(500)]
            defaultVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0)]
        else:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoPulseWidth.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(500), c_double(0.5*1000*1000)]
            defaultVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0), c_double(0)]
        setCmpTableArr = [c_double(5000), c_double(10000), c_double(15000), c_double(20000), c_double(25000), c_double(30000)]
        transCmpTable = (c_double * len(setCmpTableArr))(*setCmpTableArr)
        setCntValueArr = [c_double(4000), c_double(5000), c_double(9000), c_double(10000), c_double(14000), c_double(15000), c_double(19000), c_double(20000), c_double(24000), c_double(25000), c_double(29000), c_double(30000), c_double(31000)]
        # setCntValueArr = [c_double(5010), c_double(10010), c_double(15010), c_double(20010), c_double(25010), c_double(30010)]
        print(f'{Fore.YELLOW} --- Start test SWCmp:{global_run_swcmpch} single counter:{global_cnt_arr[0]} with table, {global_run_do_mode.name} mode ---')
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
        self._ClearLinkedDo(global_run_swcmpch)
        print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
        self._LinkedDo(global_run_swcmpch, linkedDo)
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Counter]')
        self._ClearLinkedObj(global_run_swcmpch, linkType, global_cnt_arr)
        print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Counter]')
        self._LinkedObj(global_run_swcmpch, linkType, global_cnt_arr)
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Counter reset error, and reset value]')
        self.Reset508xCntValue(global_cnt_arr[0])
        for i in range(len(ppt)):
            if ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value:
                print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Do output mode:{COMPARE_OUTPUT_MODE(pptSetVal[i].value).name}]')
            elif ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value:
                print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[CMP Deviation:{pptSetVal[i].value}]')
            else:
                print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[{self.AdvPpt(ppt[i].value).name}:{pptSetVal[i].value}]')
            self._SetProperty(global_run_swcmpch, ppt[i], pptSetVal[i])
        print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
        self._OnOffCmp(global_run_swcmpch, COMPARE_ENABLE.CMP_DISABLE.value)
        print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Software compare data]')
        self.errCde = self.AdvMot.Acm2_ChResetCmpData(global_run_swcmpch)
        getSWCmpBuffer = BUFFER_STATUS()
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Reset CMP data failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Reset CMP data failed, errCde:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Reset CMP data successed')
        self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(global_run_swcmpch, byref(getSWCmpBuffer))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get CMP buffer failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
        print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Software compare data]')
        for idx in range(len(setCmpTableArr)):
            if idx != len(setCmpTableArr) - 1:
                print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}', end=' ')
            else:
                print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}')
        self.errCde = self.AdvMot.Acm2_ChSetCmpBufferData(global_run_swcmpch, transCmpTable, len(setCmpTableArr))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Set CMP data failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Set CMP data failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Set CMP data successed')
        self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(global_run_swcmpch, byref(getSWCmpBuffer))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get CMP buffer failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
        print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Software compare]')
        self._OnOffCmp(global_run_swcmpch, COMPARE_ENABLE.CMP_ENABLE.value)
        # 設置 Counter 數值
        for idx in range(len(setCntValueArr)):
            print(f'{Fore.CYAN}[Move]{Fore.LIGHTBLUE_EX}[Counter value set to {setCntValueArr[idx].value}]')
            self.SetCntValue(global_cnt_arr[0], setCntValueArr[idx].value)
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(global_run_swcmpch, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
        print(f'{Fore.YELLOW} --- End test SWCMP:{global_run_swcmpch} ---')
        print(f'{Fore.BLUE}***** Initializing (SWCMP:{global_run_swcmpch} single counter:{global_cnt_arr[0]}) *****')
        print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
        self._OnOffCmp(global_run_swcmpch, COMPARE_ENABLE.CMP_DISABLE.value)
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Counter reset error, and reset counter]')
        self.Reset508xCntValue(global_cnt_arr[0])
        print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Reset property back to default value]')
        for i in range(len(ppt)):
            self._SetProperty(global_run_swcmpch, ppt[i], defaultVal[i])
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Counter]')
        self._ClearLinkedObj(global_run_swcmpch, linkType, global_cnt_arr)

    def TestCmpSingleCntAuto(self):
        global global_run_swcmpch, global_run_do_mode, global_use_buffer_api, global_run_cnt_cnt, global_cnt_arr
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        linkedDo = c_uint32(0)
        linkType = ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL
        if global_run_do_mode.value == COMPARE_OUTPUT_MODE.CMP_TOGGLE.value:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value), c_double(500)]
            defaultVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0)]
        else:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoPulseWidth.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(500), c_double(0.5*1000*1000)]
            defaultVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0), c_double(0)]
        startPos = c_double(5000)
        autoEndPos = c_double(30000)
        interval = c_double(5000)
        setCntValueArr = [c_double(4000), c_double(5000), c_double(9000), c_double(10000), c_double(14000), c_double(15000), c_double(19000), c_double(20000), c_double(24000), c_double(25000), c_double(29000), c_double(30000), c_double(31000), c_double(35000)]
        print(f'{Fore.YELLOW} --- Start test SWCmp:{global_run_swcmpch} single counter:{global_cnt_arr[0]} with auto, {global_run_do_mode.name} mode ---')
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
        self._ClearLinkedDo(global_run_swcmpch)
        print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
        self._LinkedDo(global_run_swcmpch, linkedDo)
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Counter]')
        self._ClearLinkedObj(global_run_swcmpch, linkType, global_cnt_arr)
        print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Counter]')
        self._LinkedObj(global_run_swcmpch, linkType, global_cnt_arr)
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Counter reset error, and reset value]')
        self.Reset508xCntValue(global_cnt_arr[0])
        for i in range(len(ppt)):
            if ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value:
                print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Do output mode:{COMPARE_OUTPUT_MODE(pptSetVal[i].value).name}]')
            elif ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value:
                print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[CMP Deviation:{pptSetVal[i].value}]')
            else:
                print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[{self.AdvPpt(ppt[i].value).name}:{pptSetVal[i].value}]')
            self._SetProperty(global_run_swcmpch, ppt[i], pptSetVal[i])
        print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
        self._OnOffCmp(global_run_swcmpch, COMPARE_ENABLE.CMP_DISABLE.value)
        print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Software compare data]')
        self.errCde = self.AdvMot.Acm2_ChResetCmpData(global_run_swcmpch)
        getSWCmpBuffer = BUFFER_STATUS()
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Reset CMP data failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Reset CMP data failed, errCde:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Reset CMP data successed')
        self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(global_run_swcmpch, byref(getSWCmpBuffer))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get CMP buffer failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
        print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Software compare data]')
        print(f'{Fore.LIGHTBLUE_EX}Start pos:{startPos.value}, interval:{interval.value}, end pos:{autoEndPos.value}')
        self.errCde = self.AdvMot.Acm2_ChSetCmpAuto(global_run_swcmpch, startPos, autoEndPos, interval)
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Set CMP data failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Set CMP data failed, errCde:{self.AdvErr(self.errCde).name}')
        else:
            self._PrintResult(True, f'Set CMP data successed')
        self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(global_run_swcmpch, byref(getSWCmpBuffer))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get CMP buffer failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
        print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Software compare]')
        self._OnOffCmp(global_run_swcmpch, COMPARE_ENABLE.CMP_ENABLE.value)
        # 設置 Counter 數值
        for idx in range(len(setCntValueArr)):
            print(f'{Fore.CYAN}[Move]{Fore.LIGHTBLUE_EX}[Counter value set to {setCntValueArr[idx].value}]')
            self.SetCntValue(global_cnt_arr[0], setCntValueArr[idx].value)
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(global_run_swcmpch, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
        print(f'{Fore.YELLOW} --- End test SWCMP:{global_run_swcmpch} ---')
        print(f'{Fore.BLUE}***** Initializing (SWCMP:{global_run_swcmpch} single counter:{global_cnt_arr[0]}) *****')
        print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
        self._OnOffCmp(global_run_swcmpch, COMPARE_ENABLE.CMP_DISABLE.value)
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Counter reset error, and reset counter]')
        self.Reset508xCntValue(global_cnt_arr[0])
        print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Reset property back to default value]')
        for i in range(len(ppt)):
            self._SetProperty(global_run_swcmpch, ppt[i], defaultVal[i])
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Counter]')
        self._ClearLinkedObj(global_run_swcmpch, linkType, global_cnt_arr)

    def TestCmp2CntsAuto(self):
        global global_run_swcmpch, global_run_do_mode, global_use_buffer_api, global_run_cnt_cnt, global_cnt_arr
        except_err = c_uint32(ErrorCode2.SUCCESS.value)
        linkedDo = c_uint32(0)
        linkType = ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL
        if global_run_do_mode.value == COMPARE_OUTPUT_MODE.CMP_TOGGLE.value:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value), c_double(2000)]
            defaultVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0)]
        else:
            ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoPulseWidth.value)]
            pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(2000), c_double(0.5*1000*1000)]
            defaultVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0), c_double(0)]
        startPos = c_double(5000)
        autoEndPos = c_double(30000)
        interval = c_double(5000)
        setCntValueArr = [c_double(4000), c_double(5000), c_double(6000), c_double(9000), c_double(10000), c_double(14000), c_double(15000), c_double(19000), c_double(20000), c_double(24000), c_double(25000), c_double(29000), c_double(30000), c_double(34000), c_double(35000)]
        print(f'{Fore.YELLOW} --- Start test SWCmp:{global_run_swcmpch} single counter:{global_cnt_arr[0]} with auto, {global_run_do_mode.name} mode ---')
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
        self._ClearLinkedDo(global_run_swcmpch)
        print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
        self._LinkedDo(global_run_swcmpch, linkedDo)
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Counter]')
        self._ClearLinkedObj(global_run_swcmpch, linkType, global_cnt_arr)
        print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Counter]')
        self._LinkedObj(global_run_swcmpch, linkType, global_cnt_arr)
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Counter reset error, and reset value]')
        self.Reset508xCntValue(global_cnt_arr[0])
        for i in range(len(ppt)):
            if ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value:
                print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Do output mode:{COMPARE_OUTPUT_MODE(pptSetVal[i].value).name}]')
            elif ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value:
                print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[CMP Deviation:{pptSetVal[i].value}]')
            else:
                print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[{self.AdvPpt(ppt[i].value).name}:{pptSetVal[i].value}]')
            self._SetProperty(global_run_swcmpch, ppt[i], pptSetVal[i])
        print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
        self._OnOffCmp(global_run_swcmpch, COMPARE_ENABLE.CMP_DISABLE.value)
        print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Software compare data]')
        self.errCde = self.AdvMot.Acm2_ChResetCmpData(global_run_swcmpch)
        getSWCmpBuffer = BUFFER_STATUS()
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Reset CMP data failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Reset CMP data failed, errCde:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Reset CMP data successed')
        self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(global_run_swcmpch, byref(getSWCmpBuffer))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get CMP buffer failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
        print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Software compare data]')
        print(f'{Fore.LIGHTBLUE_EX}Start pos:{startPos.value}, interval:{interval.value}, end pos:{autoEndPos.value}')
        self.errCde = self.AdvMot.Acm2_ChSetCmpAuto(global_run_swcmpch, startPos, autoEndPos, interval)
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Set CMP data failed, errCde:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Set CMP data failed, errCde:{self.AdvErr(self.errCde).name}')
        else:
            self._PrintResult(True, f'Set CMP data successed')
        self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(global_run_swcmpch, byref(getSWCmpBuffer))
        if self.errCde != except_err.value:
            self._PrintResult(False, f'Get CMP buffer failed:{self.errCde:x}')
            self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed:{self.errCde:x}')
        else:
            self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
        print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Software compare]')
        self._OnOffCmp(global_run_swcmpch, COMPARE_ENABLE.CMP_ENABLE.value)
        # 設置 Counter 數值
        for idx in range(len(setCntValueArr)):
            print(f'{Fore.CYAN}[Move]{Fore.LIGHTBLUE_EX}[Counter ch:{global_cnt_arr[0]} value set to {setCntValueArr[idx].value}]')
            self.SetCntValue(global_cnt_arr[0], setCntValueArr[idx].value)
            print(f'{Fore.CYAN}[Move]{Fore.LIGHTBLUE_EX}[Counter ch:{global_cnt_arr[1]} value set to {setCntValueArr[idx].value}]')
            self.SetCntValue(global_cnt_arr[1], setCntValueArr[idx].value)
            time.sleep(1.5)
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(global_run_swcmpch, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
        print(f'{Fore.YELLOW} --- End test SWCMP:{global_run_swcmpch} ---')
        print(f'{Fore.BLUE}***** Initializing (SWCMP:{global_run_swcmpch} 2 counter:{global_cnt_arr[0], global_cnt_arr[1]}) *****')
        print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
        self._OnOffCmp(global_run_swcmpch, COMPARE_ENABLE.CMP_DISABLE.value)
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Counter reset error, and reset counter]')
        self.Reset508xCntValue(global_cnt_arr[0])
        print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Reset property back to default value]')
        for i in range(len(ppt)):
            self._SetProperty(global_run_swcmpch, ppt[i], defaultVal[i])
        print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Counter]')
        self._ClearLinkedObj(global_run_swcmpch, linkType, global_cnt_arr)

    def TestCmp2CntsTable(self):
            global global_run_swcmpch, global_run_do_mode, global_use_buffer_api, global_run_cnt_cnt, global_cnt_arr
            except_err = c_uint32(ErrorCode2.SUCCESS.value)
            linkedDo = c_uint32(0)
            linkType = ADV_OBJ_TYPE.ADV_COUNTER_CHANNEL
            if global_run_do_mode.value == COMPARE_OUTPUT_MODE.CMP_TOGGLE.value:
                ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value)]
                pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_TOGGLE.value), c_double(2000)]
                defaultVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0)]
            else:
                ppt = [c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value), c_uint32(self.AdvPpt.CFG_CH_DaqSWCmpDoPulseWidth.value)]
                pptSetVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(500), c_double(0.5*1000*1000)]
                defaultVal = [c_double(COMPARE_OUTPUT_MODE.CMP_PULSE.value), c_double(0), c_double(0)]
            setCntValueArr = [c_double(4000), c_double(5000), c_double(9000), c_double(10000), c_double(14000), c_double(15000), c_double(19000), c_double(20000), c_double(24000), c_double(25000), c_double(29000), c_double(30000), c_double(31000)]
            setCmpTableArr = [c_double(5000), c_double(10000), c_double(15000), c_double(20000), c_double(25000), c_double(30000),
                              c_double(5000), c_double(10000), c_double(15000), c_double(20000), c_double(25000), c_double(30000)]
            transCmpTable = (c_double * len(setCmpTableArr))(*setCmpTableArr)
            print(f'{Fore.YELLOW} --- Start test SWCmp:{global_run_swcmpch} single counter:{global_cnt_arr[0]} with auto, {global_run_do_mode.name} mode ---')
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._ClearLinkedDo(global_run_swcmpch)
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Do]')
            self._LinkedDo(global_run_swcmpch, linkedDo)
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Counter]')
            self._ClearLinkedObj(global_run_swcmpch, linkType, global_cnt_arr)
            print(f'{Fore.CYAN}[Link]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Counter]')
            self._LinkedObj(global_run_swcmpch, linkType, global_cnt_arr)
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Counter reset error, and reset value]')
            self.Reset508xCntValue(global_cnt_arr[0])
            for i in range(len(ppt)):
                if ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDoOutputMode.value:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Do output mode:{COMPARE_OUTPUT_MODE(pptSetVal[i].value).name}]')
                elif ppt[i].value == self.AdvPpt.CFG_CH_DaqSWCmpDeviation.value:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[CMP Deviation:{pptSetVal[i].value}]')
                else:
                    print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[{self.AdvPpt(ppt[i].value).name}:{pptSetVal[i].value}]')
                self._SetProperty(global_run_swcmpch, ppt[i], pptSetVal[i])
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(global_run_swcmpch, COMPARE_ENABLE.CMP_DISABLE.value)
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Software compare data]')
            self.errCde = self.AdvMot.Acm2_ChResetCmpData(global_run_swcmpch)
            getSWCmpBuffer = BUFFER_STATUS()
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Reset CMP data failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Reset CMP data failed, errCde:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Reset CMP data successed')
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(global_run_swcmpch, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            print(f'{Fore.CYAN}[Set]{Fore.LIGHTBLUE_EX}[Software compare data]')
            for idx in range(len(setCmpTableArr)):
                if idx != len(setCmpTableArr) - 1:
                    print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}', end=' ')
                else:
                    print(f'{Fore.LIGHTBLUE_EX}{setCmpTableArr[idx].value}')
            self.errCde = self.AdvMot.Acm2_ChSetMultiCmpBufferData(global_run_swcmpch, transCmpTable, len(global_cnt_arr), c_uint32(int(len(setCmpTableArr)/len(global_cnt_arr))))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Set CMP data failed, errCde:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Set CMP data failed, errCde:{self.AdvErr(self.errCde).name}')
            else:
                self._PrintResult(True, f'Set CMP data successed')
            self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(global_run_swcmpch, byref(getSWCmpBuffer))
            if self.errCde != except_err.value:
                self._PrintResult(False, f'Get CMP buffer failed:{self.errCde:x}')
                self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed:{self.errCde:x}')
            else:
                self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            print(f'{Fore.CYAN}[Enable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(global_run_swcmpch, COMPARE_ENABLE.CMP_ENABLE.value)
            # 設置 Counter 數值
            for idx in range(len(setCntValueArr)):
                print(f'{Fore.CYAN}[Move]{Fore.LIGHTBLUE_EX}[Counter ch:{global_cnt_arr[0]} value set to {setCntValueArr[idx].value}]')
                self.SetCntValue(global_cnt_arr[0], setCntValueArr[idx].value)
                print(f'{Fore.CYAN}[Move]{Fore.LIGHTBLUE_EX}[Counter ch:{global_cnt_arr[1]} value set to {setCntValueArr[idx].value}]')
                self.SetCntValue(global_cnt_arr[1], setCntValueArr[idx].value)
                time.sleep(3)
                self.errCde = self.AdvMot.Acm2_ChGetCmpBufferStatus(global_run_swcmpch, byref(getSWCmpBuffer))
                if self.errCde != except_err.value:
                    self._PrintResult(False, f'Get CMP buffer failed:{self.errCde:x}')
                    self.assertEqual(except_err.value, self.errCde, f'Get CMP buffer failed:{self.errCde:x}')
                else:
                    self._PrintResult(True, f'Get CMP buffer successed (CurIndex:{getSWCmpBuffer.CurIndex}, RemainCount:{getSWCmpBuffer.RemainCount}, FreeSpaceCount:{getSWCmpBuffer.FreeSpaceCount})')
            print(f'{Fore.YELLOW} --- End test SWCMP:{global_run_swcmpch} ---')
            print(f'{Fore.BLUE}***** Initializing (SWCMP:{global_run_swcmpch} 2 counter:{global_cnt_arr[0], global_cnt_arr[1]}) *****')
            print(f'{Fore.CYAN}[Disable]{Fore.LIGHTBLUE_EX}[Software compare]')
            self._OnOffCmp(global_run_swcmpch, COMPARE_ENABLE.CMP_DISABLE.value)
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Counter reset error, and reset counter]')
            self.Reset508xCntValue(global_cnt_arr[0])
            print(f'{Fore.CYAN}[Reset]{Fore.LIGHTBLUE_EX}[Reset property back to default value]')
            for i in range(len(ppt)):
                self._SetProperty(global_run_swcmpch, ppt[i], defaultVal[i])
            print(f'{Fore.CYAN}[Clear]{Fore.LIGHTBLUE_EX}[Software compare channel linked to Counter]')
            self._ClearLinkedObj(global_run_swcmpch, linkType, global_cnt_arr)

def SWCmpRunSingleCounterTableToggle():
    global global_run_swcmpch, global_run_do_mode, global_use_buffer_api, global_run_cnt_cnt, global_cnt_arr
    global_run_swcmpch = 0
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    global_use_buffer_api = False
    global_run_cnt_cnt = 1
    global_cnt_arr = [0]
    tests = ['initial', 'EtherCATInit', 'TestCmpSingleCntTable', 'EtherCATDisConnect']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRunSingleCounterTablePulse():
    global global_run_swcmpch, global_run_do_mode, global_use_buffer_api, global_run_cnt_cnt, global_cnt_arr
    global_run_swcmpch = 0
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    global_use_buffer_api = False
    global_run_cnt_cnt = 1
    global_cnt_arr = [0]
    tests = ['initial', 'EtherCATInit', 'TestCmpSingleCntTable', 'EtherCATDisConnect']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRunSingleCounterAutoToggle():
    global global_run_swcmpch, global_run_do_mode, global_use_buffer_api, global_run_cnt_cnt, global_cnt_arr
    global_run_swcmpch = 0
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    global_use_buffer_api = False
    global_run_cnt_cnt = 1
    global_cnt_arr = [0]
    tests = ['initial', 'EtherCATInit', 'TestCmpSingleCntAuto', 'EtherCATDisConnect']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRunSingleCounterAutoPulse():
    global global_run_swcmpch, global_run_do_mode, global_use_buffer_api, global_run_cnt_cnt, global_cnt_arr
    global_run_swcmpch = 0
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    global_use_buffer_api = False
    global_run_cnt_cnt = 1
    global_cnt_arr = [0]
    tests = ['initial', 'EtherCATInit', 'TestCmpSingleCntAuto', 'EtherCATDisConnect']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRun2CountersAutoToggle():
    global global_run_swcmpch, global_run_do_mode, global_use_buffer_api, global_run_cnt_cnt, global_cnt_arr
    global_run_swcmpch = 0
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    global_use_buffer_api = False
    global_run_cnt_cnt = 2
    global_cnt_arr = [0, 1]
    tests = ['initial', 'EtherCATInit', 'TestCmp2CntsAuto', 'EtherCATDisConnect']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRun2CountersAutoPulse():
    global global_run_swcmpch, global_run_do_mode, global_use_buffer_api, global_run_cnt_cnt, global_cnt_arr
    global_run_swcmpch = 0
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    global_use_buffer_api = False
    global_run_cnt_cnt = 2
    global_cnt_arr = [0, 1]
    tests = ['initial', 'EtherCATInit', 'TestCmp2CntsAuto', 'EtherCATDisConnect']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRun2CountersTableToggle():
    global global_run_swcmpch, global_run_do_mode, global_use_buffer_api, global_run_cnt_cnt, global_cnt_arr
    global_run_swcmpch = 0
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_TOGGLE
    global_use_buffer_api = False
    global_run_cnt_cnt = 2
    global_cnt_arr = [0, 1]
    tests = ['initial', 'EtherCATInit', 'TestCmp2CntsTable', 'EtherCATDisConnect']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite

def SWCmpRun2CountersTablePulse():
    global global_run_swcmpch, global_run_do_mode, global_use_buffer_api, global_run_cnt_cnt, global_cnt_arr
    global_run_swcmpch = 0
    global_run_do_mode = COMPARE_OUTPUT_MODE.CMP_PULSE
    global_use_buffer_api = False
    global_run_cnt_cnt = 2
    global_cnt_arr = [0, 1]
    tests = ['initial', 'EtherCATInit', 'TestCmp2CntsTable', 'EtherCATDisConnect']
    suite = unittest.TestSuite(map(SWCmp_Test, tests))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # run_single_cnt_table_toggle = runner.run(SWCmpRunSingleCounterTableToggle())
    # run_single_cnt_table_pulse = runner.run(SWCmpRunSingleCounterTablePulse())
    run_single_cnt_auto_toggle = runner.run(SWCmpRunSingleCounterAutoToggle())
    # run_single_cnt_auto_pulse = runner.run(SWCmpRunSingleCounterAutoPulse())
    # run_2_cnts_auto_toggle = runner.run(SWCmpRun2CountersAutoToggle())
    # run_2_cnts_auto_pulse = runner.run(SWCmpRun2CountersAutoPulse())
    # run_2_cnts_table_toggle = runner.run(SWCmpRun2CountersTableToggle())
    # run_2_cnts_table_pulse = runner.run(SWCmpRun2CountersTablePulse())