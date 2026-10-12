from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotApi_CM2 import DEVLIST
from AcmP.AdvMotPropID_CM2 import PropertyID2

dev_list = (DEVLIST*10)()
out_ent = c_uint32(0)
errCde = c_uint32(0)
# Get Available
errCde = AdvMot.Acm2_GetAvailableDevs(dev_list, 10, byref(out_ent))
# Initial device
errCde = AdvMot.Acm2_DevInitialize()
do_ch = c_uint32(0)
property_id = c_uint(PropertyID2.CFG_CH_DaqDoFuncSelect.value)
val = c_double(1)
# Set local DO channel 0 as gerneral DO
errCde = AdvMot.Acm2_SetProperty(do_ch, property_id, val)
get_val = c_double(0)
# Get local DO channel 0 property value
errCde = AdvMot.Acm2_GetProperty(do_ch, property_id, byref(get_val))
# Set local DO channel 0 ON
data = c_uint32(1)
errCde = AdvMot.Acm2_ChSetDOBit(do_ch, data)
# Get local DO channel 0 value
get_data = c_uint32(0)
errCde = AdvMot.Acm2_ChGetDOBit(do_ch, byref(get_data))