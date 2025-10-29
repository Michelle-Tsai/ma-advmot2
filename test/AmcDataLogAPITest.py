import time
import unittest
import os
import ctypes
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2, AmcLogAPI
from AcmP.AdvMotErr_CM2 import ErrorCode2
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.MotionInfo import *

global_isRotate = False
global_maxFileCnt = 1

class AmcDataLogAPI_Test(unittest.TestCase):
    def setUp(self):
        self.maxEnt = 10
        self.devlist = (DEVLIST * self.maxEnt)()
        self.outEnt = c_uint32(0)
        self.errCde = 0
        self.AdvMot = AdvCmnAPI_CM2
        self.AdvAmc = AmcLogAPI
        self.log_ch = c_uint32(1)
        self.ax_id = c_uint32(1)
        self.log_index = c_uint16(0)
        self.dirPath = b'/tmp'
        self.fileName = b'PyTestDataLog'
        self.saveLocalFile = "download_amclog.txt"
    def tearDown(self):
        self.errCde = 0

    def initial(self):
        except_err = 0
        self.errCde = self.AdvMot.Acm2_GetAvailableDevs(self.devlist, self.maxEnt, byref(self.outEnt))
        self.assertEqual(except_err, self.errCde, '{0} failed'.format(self._testMethodName))
        for i in range(self.outEnt.value):
            print('Dev number:{0:x}'.format(self.devlist[i].dwDeviceNum))
        self.errCde = self.AdvMot.Acm2_DevInitialize()
        self.assertEqual(except_err, self.errCde, '{0} failed'.format(self._testMethodName))
        
    def axPTP(self):
        except_err = 0
        state_type = c_uint(AXIS_STATUS_TYPE.AXIS_STATE.value)
        abs_mode = c_uint(ABS_MODE.MOVE_REL.value)
        distance = c_double(100000)
        get_state = c_uint32(0)
        speed_profile = SPEED_PROFILE_PRM()
        speed_profile.FH = c_double(3000)
        speed_profile.FL = c_double(1000)
        speed_profile.Acc = c_double(10000)
        speed_profile.Dec = c_double(1000)
        get_distance = c_double(0)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        self.errCde = self.AdvMot.Acm2_AxSetSpeedProfile(self.ax_id, speed_profile)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        self.errCde = self.AdvMot.Acm2_AxPTP(self.ax_id, abs_mode, distance)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        self.errCde = self.AdvMot.Acm2_AxGetState(self.ax_id, state_type, byref(get_state))
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        while get_state.value != AXIS_STATE.STA_AX_READY.value:
            time.sleep(1)
            self.errCde = self.AdvMot.Acm2_AxGetState(self.ax_id, state_type, byref(get_state))
        self.errCde = self.AdvMot.Acm2_AxGetPosition(self.ax_id, pos_type, byref(get_distance))
        print(f'Get ax:{self.ax_id.value}, pos:{get_distance.value}')

    def setLog(self):
        global global_isRotate, global_maxFileCnt
        except_err = 0
        dataLogSource = AMC_DATA_LOG_SOURCE()
        dataLogSource.type = c_uint(AMC_DATA_LOG_SOURCE_TYPE.LOG_SOURCE_MOTION_AXIS.value)
        dataLogSource.selection[0] = c_uint32(self.ax_id.value)
        dataLogSource.count = 1
        dataLogSource.items.smItems = AMC_DATA_LOG_SM_ITEMS()
        dataLogSource.items.smItems.cmd_pos = c_uint8(True)
        dataLogSource.items.smItems.act_pos = c_uint8(True)
        dataLogSource.items.smItems.cmd_vel = c_uint8(True)
        dataLogSource.items.smItems.act_vel = c_uint8(True)
        getDataLogSource = AMC_DATA_LOG_SOURCE()
        
        dataLogOption = AMC_DATA_LOG_OPTIONS()
        dataLogOption.isRotateFile = c_uint8(global_isRotate)
        dataLogOption.maxLogFileCount = c_uint32(global_maxFileCnt)
        dataLogOption.maxLogFileSize = c_int32(0)
        dataLogOption.samplingTimeMilliseconds = c_int32(0)
        getDataLogOption = AMC_DATA_LOG_OPTIONS()

        getDirPath = create_string_buffer(256)
        getFileName = create_string_buffer(256)

        logHeader = b'Data Log Test from python'
        getLogHeader = create_string_buffer(256)

        self.errCde = self.AdvAmc.Amc_DataLogSetLog(self.log_ch, byref(dataLogSource), self.log_index)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        self.errCde = self.AdvAmc.Amc_DataLogGetLog(self.log_ch, byref(getDataLogSource), self.log_index)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        print(f'count:{getDataLogSource.count}, type:{getDataLogSource.type}, cmd_pos:{getDataLogSource.items.smItems.cmd_pos}')
        
        self.errCde = self.AdvAmc.Amc_DataLogSetLogOption(self.log_ch, byref(dataLogOption))
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        self.errCde = self.AdvAmc.Amc_DataLogGetLogOption(self.log_ch, byref(getDataLogOption))
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        print(f'isRotateFile:{getDataLogOption.isRotateFile}, maxLogFileCount:{getDataLogOption.maxLogFileCount}, samplingTimeMilliseconds:{getDataLogOption.samplingTimeMilliseconds}')

        self.errCde = self.AdvAmc.Amc_DataLogSetLogFilePath(self.log_ch, self.dirPath, self.fileName)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        self.errCde = self.AdvAmc.Amc_DataLogGetLogFilePath(self.log_ch, getDirPath, getFileName)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        print(f'dirPath:{getDirPath.value.decode('utf-8', errors='ignore')}, fileName:{getFileName.value.decode('utf-8', errors='ignore')}')
        fileNames = []
        if (global_isRotate is True):
            fileBufferSize = c_uint32(1024)
            getFilePath = create_string_buffer(fileBufferSize.value)
            getFileCnt = c_uint32(0)
            self.errCde = self.AdvAmc.Amc_DataLog_GetRotatedLogFilePaths(self.log_ch, getFilePath, POINTER(fileBufferSize), POINTER(getFileCnt))
            self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
            print(f'getFileCnt:{getFileCnt.value}')
            if getFileCnt.value > 0:
                startIdx = 0
                content = getFilePath.raw[:fileBufferSize.value]
                for _ in range(getFileCnt.value):
                    nullPos = content.find(b'\0', startIdx)
                    if nullPos == -1:
                        print("Cann't find")
                        break
                    try:
                        fileName = content[startIdx:nullPos].decode('utf-8', errors='replace')
                    except UnicodeDecodeError:
                        try:
                            import locale
                            fileName = content[startIdx:nullPos].decode(locale.getpreferredencoding, errors='replace')
                        except Exception:
                            print("Failed to decode")
                    fileNames.append(fileName)
                    startIdx = nullPos + 1
                    if startIdx >= len(fileBufferSize.value):
                        if len(fileNames) < getFileCnt.value:
                            print(f"End decode, still has:{getFileCnt.value}")
                            break
                if len(fileNames) != getFileCnt.value:
                    print(f"fileNames:{len(fileNames)} != getFileCnt:{getFileCnt.value}")
            for fname in fileNames:
                print(f"{fname}")

        self.errCde = self.AdvAmc.Amc_DataLog_SetLogHeader(self.log_ch, logHeader)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        self.errCde = self.AdvAmc.Amc_DataLogGetLogHeader(self.log_ch, getLogHeader)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        print(f'logHeader:{getLogHeader.value.decode('utf-8', errors='ignore')}')

    def getLogStatus(self):
        except_err = 0
        getDataLogStatus = AMC_DATA_LOG_STATUS()
        self.errCde = self.AdvAmc.Amc_DataLogGetStatus(self.log_ch, byref(getDataLogStatus))
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        print(f'state:{getDataLogStatus.state}, stopRequest:{getDataLogStatus.stopRequest}')

    def startLog(self):
        except_err = 0
        self.errCde = self.AdvAmc.Amc_DataLogStartLog(self.log_ch)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))

    def stopLog(self):
        except_err = 0
        self.errCde = self.AdvAmc.Amc_DataLogStopLog(self.log_ch)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))

    def getLogFile(self):
        except_err = 0
        filePath = self.dirPath + b'/' + self.fileName + b'.txt'
        bufferSize = c_uint32(5 * 1024 * 1024) # 5MB
        currSize = bufferSize
        fileBuffer = create_string_buffer(bufferSize.value)
        self.errCde = self.AdvAmc.Amc_DataLogGetLogFile(filePath, fileBuffer, byref(bufferSize))
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        if self.errCde == ErrorCode2.MemAllocateFailed:
            print(f'Initial buffer too small. Required: {bufferSize} bytes')
            if bufferSize <= currSize:
                print(f'Error!currSize:{currSize.value}, bufferSize:{bufferSize.value}')
            currSize = bufferSize
            fileBuffer = create_string_buffer(currSize)
            self.errCde = self.AdvAmc.Amc_DataLogGetLogFile(filePath, fileBuffer, byref(bufferSize))
            self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        if self.errCde == ErrorCode2.SUCCESS:
            with open(self.saveLocalFile, "wb") as f:
                f.write(fileBuffer.raw[:bufferSize.value])

    def stopAll(self):
        except_err = 0
        ax_arr = [self.ax_id]
        axArr = (c_uint32 * len(ax_arr))(*ax_arr)
        stop_mode = c_uint(MOTION_STOP_MODE.MOTION_STOP_MODE_DEC.value)
        new_dec = c_double(3000)
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        pos = c_double(0)
        self.errCde = self.AdvMot.Acm2_AxMotionStop(axArr, len(ax_arr), stop_mode, new_dec)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))
        self.errCde = self.AdvMot.Acm2_AxSetPosition(self.ax_id, pos_type, pos)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))

    def resetLog(self):
        except_err = 0
        self.errCde = self.AdvAmc.Amc_DataLogResetLog(self.log_ch)
        self.assertEqual(except_err, self.errCde, '{0} failed.'.format(self._testMethodName))

    def sleep(self):
        time.sleep(5)

def SetLog():
    global global_isRotate, global_maxFileCnt
    global_isRotate = False
    global_maxFileCnt = 1
    tests = ['initial', 'setLog']
    suite = unittest.TestSuite(map(AmcDataLogAPI_Test, tests))
    return suite

def SetLogWithRotate():
    global global_isRotate, global_maxFileCnt
    global_isRotate = True
    global_maxFileCnt = 2
    tests = ['initial', 'setLog']
    suite = unittest.TestSuite(map(AmcDataLogAPI_Test, tests))
    return suite

def Run():
    tests = ['initial', 'startLog', 'axPTP', 'sleep','stopLog', 'getLogStatus']
    suite = unittest.TestSuite(map(AmcDataLogAPI_Test, tests))
    return suite

def StopAllAndReset():
    tests = ['initial', 'stopAll', 'getLogStatus', 'resetLog']
    suite = unittest.TestSuite(map(AmcDataLogAPI_Test, tests))
    return suite

def GetLogFile():
    tests = ['initial', 'getLogFile']
    suite = unittest.TestSuite(map(AmcDataLogAPI_Test, tests))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    stop_reset = runner.run(StopAllAndReset())
    # set_log = runner.run(SetLog())
    set_log = runner.run(SetLogWithRotate())
    run = runner.run(Run())
    logFile = runner.run(GetLogFile())