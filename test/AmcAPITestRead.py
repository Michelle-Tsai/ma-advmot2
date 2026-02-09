import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.MotionInfo import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import create_string_buffer

class AmcLogAPI_Test(unittest.TestCase):
    def setUp(self):
        self.maxEnt = 10
        self.devlist = (DEVLIST*self.maxEnt)()
        self.outEnt = c_uint32(0)
        self.errCde = 0
        self.AdvMot = AdvCmnAPI_CM2
        self.AmcApi = AmcLogAPI
        self.bufferSize = 1024
        self.cnt = 0
        if os.name == 'nt':
            self.logDir = b'D:\\'
        else:
            self.logDir = b'd:/'
        self.baseName = b'amc_api_log'
    def tearDown(self):
        self.errCde = 0

    def initial(self):
        except_err = 0
        self.errCde = self.AdvMot.Acm2_GetAvailableDevs(self.devlist, self.maxEnt, byref(self.outEnt))
        self.assertEqual(except_err, self.errCde, '{0} failed'.format(self._testMethodName))
        for i in range(self.outEnt.value):
            print('Dev number:{0:x}'.format(self.devlist[i].dwDeviceNum))
        self.errCde = self.AdvMot.Acm2_DevInitialize()
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))

    def convert_filetime_to_datetime(self, filetime_int: int):
        """
        將一個 64-bit Windows FILETIME (I64) 轉換為
        人類可讀的 (human-readable) 本地時區 datetime 物件。

        FILETIME 是自 1601-01-01 00:00:00 UTC 起的 100 奈秒間隔數。
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

    def axPTP(self):
        except_err = 0
        ax_id = c_uint32(0)
        state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
        abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
        distance = c_double(1000)
        get_state = c_uint32(0)
        speed_profile = SPEED_PROFILE_PRM()
        speed_profile.FH = c_double(3000)
        speed_profile.FL = c_double(1000)
        speed_profile.Acc = c_double(10000)
        speed_profile.Dec = c_double(1000)
        self.errCde = self.AdvMot.Acm2_AxSetSpeedProfile(ax_id, speed_profile)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        self.errCde = self.AdvMot.Acm2_AxPTP(ax_id, abs_mode, distance)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        self.errCde = self.AdvMot.Acm2_AxGetState(ax_id, state_type, byref(get_state))
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        while get_state.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.AdvMot.Acm2_AxGetState(ax_id, state_type, byref(get_state))

    def setLog(self):
        except_err = 0
        logOpt = AMC_API_LOG_OPT()
        logOpt.sizePerFile = self.bufferSize
        self.errCde = self.AmcApi.Amc_SetApiLog(self.logDir, self.baseName, byref(logOpt), self.bufferSize)
        self.assertEqual(except_err, self.errCde, '{0} failed. err={1:x}'.format(self._testMethodName, self.errCde))
    
    def startLog(self):
        except_err = 0
        self.errCde = self.AmcApi.Amc_StartApiLog()
        self.assertEqual(except_err, self.errCde, '{0} failed. err={1:x}'.format(self._testMethodName, self.errCde))
        # time.sleep(5)

    def stopLog(self):
        except_err = 0
        self.errCde = self.AmcApi.Amc_StopApiLog()
        self.assertEqual(except_err, self.errCde, '{0} failed. err={1:x}'.format(self._testMethodName, self.errCde))

    def readFile(self):
        except_err = 0
        pfile = c_void_p()
        # file_name = b"D:\\amc_api_log_20251111_132212_897.dat"
        # file_name = b'D:\\log.txt'
        # file_name = "D:\\設中文1211_20251211_085241_604.dat".encode('cp950')
        file_name = b"D:\\TestLog_20251215_195932_443.dat"
        # file_name = b"D:\\11_20251120_164126_046.dat"
        api_header = AMC_API_LOG_HEADER()
        out_str = create_string_buffer(1024)
        stopCnd = 0
        self.cnt = 0
        self.errCde = self.AmcApi.Amc_OpenApiLogFile(file_name, byref(pfile))
        self.assertEqual(except_err, self.errCde, '{0} failed. err={1:x}'.format(self._testMethodName, self.errCde))
        while stopCnd != ErrorCode2.NoMoreLogData:
            data_buffer = (c_uint8 * self.bufferSize)()
            stopCnd = self.AmcApi.Amc_GetApiLogData(pfile, data_buffer, self.bufferSize, byref(api_header))
            print(f'stopCnd:0x{stopCnd:x}')
            print(f'header.len={api_header.dataLen}')
            print(f"type={'Command' if api_header.type == AMC_API_LOG_DATA_TYPE.LogCommand.value else 'Response'}, functionId={api_header.functionId}")
            if stopCnd == ErrorCode2.SUCCESS:
                self.errCde = self.AmcApi.Amc_ApiLogToString(byref(api_header), data_buffer, out_str, 1024)
                output = out_str.value.decode('utf-8')
                print(f'{self.convert_filetime_to_datetime(api_header.timestamp)}|{output}')
                self.cnt = self.cnt + 1
                print(f'cnt:{self.cnt}\n')
        self.errCde = self.AmcApi.Amc_CloseApiLogFile(pfile)
        self.assertEqual(except_err, self.errCde, '{0} failed. err={1:x}'.format(self._testMethodName, self.errCde))

    def getLogStatus(self):
        except_err = 0
        getStatus = AMC_API_LOG_STATUS()
        self.errCde = self.AmcApi.Amc_ApiLogGetStatus(byref(getStatus))
        self.assertEqual(except_err, self.errCde, '{0} failed. err={1:x}'.format(self._testMethodName, self.errCde))
        print(f'state:{getStatus.state}')
        while getStatus.state != AMC_API_LOG_STATE.API_LOG_STOPPED.value :
            self.errCde = self.AmcApi.Amc_ApiLogGetStatus(byref(getStatus))
            self.assertEqual(except_err, self.errCde, '{0} failed. err={1:x}'.format(self._testMethodName, self.errCde))
            print(f'state:{AMC_API_LOG_STATE(getStatus.state).name}')
            print(f'totalQueueSize:{getStatus.totalQueueSize}, usedQueueSize:{getStatus.usedQueueSize}')

def SetOpt():
    tests = ['setLog', 'startLog']
    suite = unittest.TestSuite(map(AmcLogAPI_Test, tests))
    return suite

def StopLog():
    tests = ['initial', 'stopLog']
    suite = unittest.TestSuite(map(AmcLogAPI_Test, tests))
    return suite

def Run():
    tests = ['initial', 'axPTP']
    suite = unittest.TestSuite(map(AmcLogAPI_Test, tests))
    return suite

def GetStatus():
    tests = ['getLogStatus']
    suite = unittest.TestSuite(map(AmcLogAPI_Test, tests))
    return suite

def ReadLog():
    tests = ['readFile']
    suite = unittest.TestSuite(map(AmcLogAPI_Test, tests))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # get_state = runner.run(GetStatus())
    read_log = runner.run(ReadLog())    # 需更改 file_name