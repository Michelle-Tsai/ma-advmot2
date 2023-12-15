from maAdvMot2.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from maAdvMot2.AdvMotApi_CM2 import DEVLIST, ADVAPI_MDEVICE_INFO
from maAdvMot2.utils import *

# GetAvailableDevs
maxEnt = 10
dev_list = (DEVLIST*maxEnt)()
outEnt = c_uint32(0)
err_cde = c_uint32(0)
print(Color.GREEN + "GetAvailableDevs:0x{0:x}".format(dev_list[0].dwDeviceNum) + Color.END)
err_cde = AdvCmnAPI_CM2.mAcm2_GetAvailableDevs(dev_list, maxEnt, byref(outEnt))
print(Color.RED + "GetAvailableDevs:0x{0:x}, err:0x{1:x}".format(dev_list[0].dwDeviceNum, err_cde) + Color.END)

AdvCmnAPI_CM2.mAcm2_DevInitialize()

ringNo = c_uint32(0)
MDevice_info = ADVAPI_MDEVICE_INFO()
AdvCmnAPI_CM2.mAcm2_DevGetMDeviceInfo(ringNo, byref(MDevice_info))

