from ctypes import *
from maAdvMot2.utils import TypeDef
from maAdvMot2.AdvMotDrv import *

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

class LINK_PORT_INFO(Structure):
    _fields_ = [
        ('desc', TypeDef.ULONG),
        ('link_up', TypeDef.UCHAR),
        ('loop_closed', TypeDef.UCHAR),
        ('signal_detected', TypeDef.UCHAR),
        ('receive_time', TypeDef.ULONG),
        ('next_slave', TypeDef.USHORT),
        ('delay_to_next_dc', TypeDef.ULONG)
    ]

class ADVAPI_SUBDEVICE_INFO_CM2(Structure):
    _fields_ = [
        ('Position', TypeDef.USHORT),
        ('VendorID', TypeDef.ULONG),
        ('ProductID', TypeDef.ULONG),
        ('RevisionNo', TypeDef.ULONG),
        ('SerialNo', TypeDef.ULONG),
        ('SubDeviceID', TypeDef.USHORT),
        ('current_on_ebus', TypeDef.SHORT),
        ('ports', LINK_PORT_INFO*4),
        ('al_state', TypeDef.UCHAR),
        ('error_flag', TypeDef.UCHAR),
        ('sync_count', TypeDef.UCHAR),
        ('Reserved', TypeDef.UCHAR),
        ('transmission_delay', TypeDef.ULONG),
        ('dc_configure', TypeDef.USHORT),
        ('DeviceName', c_char*40)
    ]

ADV_USER_CALLBACK_FUNC = CFUNCTYPE(TypeDef.U32, TypeDef.U32, TypeDef.PVOID)
def ADVUSERCALLBACKFUNC(EvtValue, UserParameter):
    pass
PADV_USER_CALLBACK_FUNC = ADV_USER_CALLBACK_FUNC(ADVUSERCALLBACKFUNC)

class PHASE_AXIS_PRM(Structure):
    _fields_ = [
        ('Acc', TypeDef.F64),
        ('Dec', TypeDef.F64),
        ('PhaseVel', TypeDef.F64),
        ('PhaseDistance', TypeDef.F64)
    ]

class SPEED_PROFILE_PRM(Structure):
    _fields_ = [
        ('FH', TypeDef.F64),
        ('FL', TypeDef.F64),
        ('Acc', TypeDef.F64),
        ('Dec', TypeDef.F64),
        ('JerkFac', TypeDef.F64)
    ]

class MOTION_IO(Structure):
    _fields_ = [
        ('RDY', TypeDef.U8),
        ('ALM', TypeDef.U8),
        ('LMT_P', TypeDef.U8),
        ('LMT_N', TypeDef.U8),
        ('ORG', TypeDef.U8),
        ('DIR', TypeDef.U8),
        ('EMG', TypeDef.U8),
        ('PCS', TypeDef.U8),
        ('ERC', TypeDef.U8),
        ('EZ', TypeDef.U8),
        ('CLR', TypeDef.U8),
        ('LTC', TypeDef.U8),
        ('SD', TypeDef.U8),
        ('INP', TypeDef.U8),
        ('SVON', TypeDef.U8),
        ('ALRM', TypeDef.U8),
        ('SLMT_P', TypeDef.U8),
        ('SLMT_N', TypeDef.U8),
        ('CMP', TypeDef.U8),
        ('CAMDO', TypeDef.U8),
        ('RESETREADY', TypeDef.U8)
    ]

class PATH_STATUS(Structure):
    _fields_ = [
        ('CurIndex', TypeDef.U32),
        ('CurCmdFunc', TypeDef.U32),
        ('RemainCount', TypeDef.U32),
        ('FreeSpaceCount', TypeDef.U32)
    ]

class CAM_IN_PRM(Structure):
    _fields_ = [
        ('PrimaryOffset', TypeDef.F64),
        ('FollowingOffset', TypeDef.F64),
        ('PrimaryScaling', TypeDef.F64),
        ('FollowingScaling', TypeDef.F64),
        ('CamTableID', TypeDef.U32),
        ('RefSrc', TypeDef.U32)
    ]

class GEAR_RATIO_RATE(Structure):
    _fields_ = [
        ('Num', TypeDef.F64),
        ('Den', TypeDef.F64)
    ]

class GEAR_IN_PRM(Structure):
    _fields_ = [
        ('RefSrc', c_uint),
        ('GearRatioRate', GEAR_RATIO_RATE),
        ('Mode', TypeDef.U32),
        ('GearPosition', TypeDef.F64)
    ]

class TANGENT_IN_PRM(Structure):
    _fields_ = [
        ('StartVectorArray', TypeDef.I32*3),
        ('Working_plane', TypeDef.U32),
        ('Direction', c_uint)
    ]

class GANTRY_IN_PRM(Structure):
    _fields_ = [
        ('RefSrc', c_uint),
        ('Direction', c_uint),
    ]

class BUFFER_STATUS(Structure):
    _fields_ = [
        ('CurIndex', TypeDef.U32),
        ('RemainCount', TypeDef.U32),
        ('FreeSpaceCount', TypeDef.U32)
    ]

class JOG_SPEED_PROFILE_PRM(Structure):
    _fields_ = [
        ('FH', TypeDef.F64),
        ('FL', TypeDef.F64),
        ('Acc', TypeDef.F64),
        ('Dec', TypeDef.F64),
        ('VLTime', TypeDef.F64)
    ]

class PATH_DO_MODE0(Structure):
    _fields_ = [
        ('DOPort', TypeDef.U32),
        ('DOEnable', TypeDef.U32),
        ('DOValue', TypeDef.U32)
    ]

class PATH_DO_MODE1(Structure):
    _fields_ = [
        ('SubDeviceID', TypeDef.U32),
        ('DOPort', TypeDef.U32),
        ('DOEnable', TypeDef.U32),
        ('DOValue', TypeDef.U32)
    ]

class PATH_DO_MODE2(Structure):
    _fields_ = [
        ('AxID', TypeDef.U32),
        ('DOEnable', TypeDef.U32),
        ('DOValue', TypeDef.U32)
    ]

class PATH_DO_MODE(Union):
    _fields_ = [
        ('Mode0', PATH_DO_MODE0),
        ('Mode1', PATH_DO_MODE1),
        ('Mode2', PATH_DO_MODE2)
    ]

class PATH_DO_PRM(Structure):
    _fields_ = [
        ('MoveMode', TypeDef.U32),
        ('PathDO_Prm', PATH_DO_MODE),
        ('DO_Output_Time', TypeDef.F64)
    ]

class PATH_DI_WAIT_MODE0(Structure):
    _fields_ = [
        ('DIPort', TypeDef.U32),
        ('DIEnable', TypeDef.U32),
        ('DIValue', TypeDef.U32)
    ]

class PATH_DI_WAIT_MODE1(Structure):
    _fields_ = [
        ('SubDeviceID', TypeDef.U32),
        ('DIPort', TypeDef.U32),
        ('DIEnable', TypeDef.U32),
        ('DIValue', TypeDef.U32)
    ]

class PATH_DI_WAIT_MODE2(Structure):
    _fields_ = [
        ('AxID', TypeDef.U32),
        ('DIEnable', TypeDef.U32),
        ('DIValue', TypeDef.U32)
    ]

class PATH_DI_WAIT_MODE(Union):
    _fields_ = [
        ('Mode0', PATH_DI_WAIT_MODE0),
        ('Mode1', PATH_DI_WAIT_MODE1),
        ('Mode2', PATH_DI_WAIT_MODE2)
    ]

class PATH_DI_WAIT_PRM(Structure):
    _fields_ = [
        ('MoveMode', TypeDef.U32),
        ('PathDI_Prm', PATH_DI_WAIT_MODE),
        ('DI_Wait_Time', TypeDef.F64),
    ]

class PATH_AX_WAIT_PRM(Structure):
    _fields_ = [
        ('AxID', TypeDef.U32),
        ('CmpMethod', TypeDef.U32),
        ('CmpValue', TypeDef.F64),
        ('ValueRange', TypeDef.F64),
        ('CmpSrc', c_uint),
        ('Timeout', TypeDef.F64),
    ]

class PWM_TABLE_STATUS(Structure):
    _fields_ = [
        ('Velocity', TypeDef.U32),
        ('PWMValue', TypeDef.U32)
    ]

class OSC_PROFILE_PRM(Structure):
    _fields_ = [
        ('Enable', TypeDef.U32),
        ('Period', TypeDef.U32),
        ('AxidNo', TypeDef.U32),
        ('ChanType', TypeDef.U32),
        ('ChanProperty', TypeDef.U32),
        ('TrigMode', TypeDef.U32),
        ('TimeWidth', TypeDef.U32)
    ]





