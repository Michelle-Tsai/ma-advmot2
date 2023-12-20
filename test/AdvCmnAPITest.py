import unittest
from maAdvMot2.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from maAdvMot2.AdvMotApi_CM2 import *
from maAdvMot2.MotionInfo import *

class AdvCmnAPI_Test(unittest.TestCase):
    def setUp(self):
        self.maxEnt = 10
        self.devlist = (DEVLIST*self.maxEnt)()
        self.outEnt = c_uint32(0)
        self.errCde = 0
        self.AdvMot = AdvCmnAPI_CM2
    
    def tearDown(self):
        # self.maxEnt = 0
        # self.devlist = None
        # self.AdvMot = None
        self.errCde = 0
    
    def test_GetAvailableDevs(self):
        # your switch number on board as device number
        excepted_dev_hex = '0x63000000'
        excepted_dev = int(excepted_dev_hex, 16)
        self.AdvMot.mAcm2_GetAvailableDevs(self.devlist, self.maxEnt, byref(self.outEnt))
        result_dev = self.devlist[0].dwDeviceNum
        self.assertEqual(excepted_dev, result_dev)
    
    def test_DevOpen(self):
        excepted_dev_hex = '0x63000000'
        excepted_dev = int(excepted_dev_hex, 16)
        device_number = c_uint32(excepted_dev)
        self.device_info = DEVICEINFO()
        excepted_err = 0
        result_err = self.AdvMot.mAcm2_DevOpen(device_number, byref(self.device_info))
        print(result_err)
        self.assertEqual(excepted_err, result_err)


    def test_Initialize(self):
        self.errCde = self.AdvMot.mAcm2_DevInitialize()
        excepted_err = 0
        self.assertEqual(excepted_err, self.errCde)

    # def test_CloseDevice(self):
    #     self.errCde = self.AdvMot.mAcm2_DevClose(self.devlist[0].)
    #     excepted_err = 0
    #     self.assertEqual(excepted_err, self.errCde)

    def test_LoadENI(self):
        ring_no = c_uint32(0)
        # eni file name has device number prefix
        eni_path = b'test/63000000_eni0.xml'
        self.errCde = self.AdvMot.mAcm2_DevLoadENI(ring_no, eni_path)
        excepted_err = 0
        self.assertEqual(excepted_err, self.errCde)
    
    def test_GetMDevice(self):
        ring_no = c_uint32(0)
        MDeviceInfo = ADVAPI_MDEVICE_INFO()
        self.errCde = self.AdvMot.mAcm2_DevGetMDeviceInfo(ring_no, byref(MDeviceInfo))
        excepted_err = 0
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

if __name__ == '__main__':
    # Test all case without order
    # unittest.main()
    # Test case with self-defined order
    runner = unittest.TextTestRunner()
    runner.run(DeviceOpen())
    # runner.run(DownloadENISuite())
    # runner.run(GetMDevice())