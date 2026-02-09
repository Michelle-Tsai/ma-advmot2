import unittest
import os
import time
from datetime import datetime
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
        self.bufferSize = 10 * 1024 * 1024
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
        self.assertEqual(except_err, self.errCde, '{0} failed. err={1:x}'.format(self._testMethodName, self.errCde))
        self.assertEqual(except_err, self.errCde, '{0} failed. err={1:x}'.format(self._testMethodName, self.errCde))
        self.errCde = self.AdvMot.Acm2_AxPTP(ax_id, abs_mode, distance)
        self.assertEqual(except_err, self.errCde, '{0} failed. err={1:x}'.format(self._testMethodName, self.errCde))
        self.errCde = self.AdvMot.Acm2_AxGetState(ax_id, state_type, byref(get_state))
        self.assertEqual(except_err, self.errCde, '{0} failed. err={1:x}'.format(self._testMethodName, self.errCde))
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

    def stopLog(self):
        except_err = 0
        self.errCde = self.AmcApi.Amc_StopApiLog()
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))

    def readFile(self):
        except_err = 0
        pfile = c_void_p()
        file_name = b"D:\\amc_api_log_20250908_151026_400.dat"
        data_buffer = (c_uint8 * self.bufferSize)()
        api_header = AMC_API_LOG_HEADER()
        out_str = create_string_buffer(self.bufferSize)
        stopCnd = 0
        self.errCde = self.AmcApi.Amc_OpenApiLogFile(file_name, byref(pfile))
        self.assertEqual(except_err, self.errCde, '{0} failed. err={1:x}'.format(self._testMethodName, self.errCde))
        while stopCnd != ErrorCode2.NoMoreLogData:
            stopCnd = self.AmcApi.Amc_GetApiLogData(pfile, data_buffer, self.bufferSize, byref(api_header))
            print(f"type={'Command' if api_header.type == AMC_API_LOG_DATA_TYPE.LogCommand.value else 'Response'}, functionId={api_header.functionId}")
            self.errCde = self.AmcApi.Amc_ApiLogToString(byref(api_header), data_buffer, out_str, self.bufferSize)
            output = out_str.value.decode('utf-8')
            print('{0}'.format(output))
        self.errCde = self.AmcApi.Amc_CloseApiLogFile(pfile)
        self.assertEqual(except_err, self.errCde, '{0} failed. err={1:x}'.format(self._testMethodName, self.errCde))

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

def ReadLog():
    tests = ['readFile']
    suite = unittest.TestSuite(map(AmcLogAPI_Test, tests))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # set_start = runner.run(SetOpt())
    stop_log = runner.run(Run())
    # stop_log = runner.run(StopLog())
    # read_log = runner.run(ReadLog())