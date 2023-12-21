from ctypes import *
from maAdvMot2.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from maAdvMot2.AdvMotApi_CM2 import DEVLIST
from maAdvMot2.MotionInfo import DEVICEINFO

number_hex = '0x63000000'
number_int = int(number_hex, 16)
device_number = c_uint32(number_int)
dev_list = (DEVLIST*10)()
device_info = DEVICEINFO()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.mAcm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Then open
errCde = AdvMot.mAcm2_DevOpen(device_number, byref(device_info))
# Close device
errCde = AdvMot.mAcm2_DevAllClose()