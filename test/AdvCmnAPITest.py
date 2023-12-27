import unittest
import time
import os
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotDrv import ABS_MODE, POSITION_TYPE, AXIS_STATUS_TYPE, AXIS_STATE
from AcmP.MotionInfo import *
from AcmP.AdvMotPropID_CM2 import PropertyID2

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
        # self.state = c_uint32(16)
        self.AdvMot.Acm2_AxGetState(ax_id, state_type, byref(self.state))
        if (self.state.value != AXIS_STATE.STA_AX_READY.value):
            print('Not Ready')
    
    def test_ResetAll(self):
        ax_id = c_uint32(0)
        excepted_err = 0
        pos_type = c_uint(POSITION_TYPE.POSITION_CMD.value)
        pos = c_double(0)
        self.errCde = self.AdvMot.Acm2_DevResetAllError()
        self.assertEqual(excepted_err, self.errCde)
        self.errCde = self.AdvMot.Acm2_AxSetPosition(ax_id, pos_type, pos)
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
    runner.run(DeviceDO())
    # runner.run(GroupCreateCheck())