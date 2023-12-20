# MA-AdvMot SDK
This SDK package allows developers to esaily use Advantech AdvMot api.
<div style="background-color:#fcf8e3;color:#8a6d3b;padding:15px;border-radius:4px">
<span style="font-weight:bold;font-size:16px">
This SDK is for Linux Only.
</span>
</div>

# Installation
This SDK supports Python version 3.10 or later
```shell
$ pip install -i https://test.pypi.org/simple/ maAdvMot2
```
Before using this package, please ensure the following items are already installed:
1. PCIE-1203.ko
2. libadvmot.so
3. libpcie1203.so
You can check the installation using the following commands.
```shell
$ lsmod | grep PCI
$ ls /lib | grep adv
$ ls /lib | grep pci
```
## Available Devices
* <a href="https://www.advantech.com/en/products/7d3c9775-8c30-4f65-83ec-755bee93b1d4/pcie-1203/mod_bb3ec42a-e9b1-4839-8b26-96551d894bb9">Advantech PCIE-1203</a>
## API
### AdvCmnAPI_CM2
+ <a href="#Acm2_DevOpen">mAcm2_DevOpen</a>
+ <a href="#Acm2_DevClose">mAcm2_DevClose</a>
----
<a name="Acm2_DevOpen"></a>
#### mAcm2_DevOpen
##### Open device with device number.
<a name="Acm2_DevClose"></a>
#### mAcm2_DevClose
##### Close device with device handle.

```python
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
handle = c_uint64(device_info.DeviceHandle)
# Close device
errCde = AdvMot.mAcm2_DevClose(byref(handle))
```