from ctypes import *
from utils import TypeDef

class DEVLIST(Structure):
    _fields_ = [
        ("dwDeviceNum", TypeDef.U32),
        ("szDeviceName", c_char*50),
        ("nNumOfSubdevices", TypeDef.I16)
    ]

class ADVAPI_MDEVICE_INFO(Structure):
    _fields_ = [
        ('totalTxLen', TypeDef.U32),
        ('totalRxLen', TypeDef.U32),
        ('cyclicTimeNS', TypeDef.U32),
        ('slave_count', TypeDef.U32),
        ('link_up', TypeDef.U32),
        ('phase', TypeDef.U8),
        ('active', TypeDef.U8),
        ('scan_busy', TypeDef.U8),
        ('ring_type', TypeDef.U8),
        ('num_devices', TypeDef.U32),
        ('tx_count', TypeDef.U64),
        ('rx_count', TypeDef.U64),
        ('tx_bytes', TypeDef.U64),
        ('rx_bytes', TypeDef.U64),
        ('dc_ref_time', TypeDef.U64),
        ('app_time', TypeDef.U64),
        ('ref_clock', TypeDef.U16),
        ('reserved2', TypeDef.U16)
    ]

class DEV_IO_MAP_INFO(Structure):
    _fields_ = [
        ('Name', c_char*50),
        ('Index', TypeDef.ULONG),
        ('Offset', TypeDef.ULONG),
        ('ByteLength', TypeDef.ULONG),
        ('SlotID', TypeDef.ULONG),
        ('PortChanID', TypeDef.ULONG),
        ('ModuleID', TypeDef.ULONG),
        ('ModuleName', c_char*16),
        ('Description', c_char*100),
    ]
