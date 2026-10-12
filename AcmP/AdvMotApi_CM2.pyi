"""Type stub for AdvMotApi_CM2 (ctypes structures)。

由 AdvMotApi_CM2.py 以 gen_pyi.py 自動產生，供 VS Code Pylance 自動完成與型別檢查使用。
欄位後的註解為 C 端 ctypes 型別、offset 與大小（x64）。
"""

from collections.abc import Callable, Iterator
from ctypes import Structure, Union, _CFuncPtr
from ctypes import c_char, c_double, c_int16, c_int32, c_int64, c_uint16, c_uint32, c_uint64, c_uint8
from typing import Any, Final, Generic, TypeVar, overload

_T = TypeVar("_T")

class _CArray(Generic[_T]):
    """stub 專用：代表 ctypes 定長陣列 (c_xxx * N)，讓索引結果有正確型別。執行期是 ctypes.Array。"""
    _length_: int
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int, /) -> _T: ...
    @overload
    def __getitem__(self, index: slice, /) -> list[_T]: ...
    def __setitem__(self, index: int, value: _T, /) -> None: ...
    def __iter__(self) -> Iterator[_T]: ...

class _CPtr(Generic[_T]):
    """stub 專用：代表 POINTER(c_xxx)。p[i] / p.contents 有正確型別。執行期是 ctypes._Pointer。"""
    contents: object
    def __getitem__(self, index: int, /) -> _T: ...
    def __setitem__(self, index: int, value: _T, /) -> None: ...
    def __bool__(self) -> bool: ...

class _CCharArray:
    """stub 專用：代表 c_char * N 陣列物件（巢狀陣列的元素）。"""
    value: bytes
    raw: bytes
    def __len__(self) -> int: ...

# callback: U32 (*)(U32 EvtValue, void* UserParameter)
class CALLBACK_FUNC(_CFuncPtr):
    def __init__(self, callable: Callable[[int, int | None], int], /) -> None: ...
    def __call__(self, EvtValue: int, UserParameter: int | None, /) -> int: ...

class ADV_USER_CALLBACK_FUNC(_CFuncPtr):
    def __init__(self, callable: Callable[[int, int | None], int], /) -> None: ...
    def __call__(self, EvtValue: int, UserParameter: int | None, /) -> int: ...

def ADVUSERCALLBACKFUNC(EvtValue: int, UserParameter: int | None) -> None: ...
PADV_USER_CALLBACK_FUNC: ADV_USER_CALLBACK_FUNC

MAX_CONTEXT_LINES: Final[int]
MAX_LINE_STR_LEN: Final[int]

class DEVLIST(Structure):
    """sizeof = 56 bytes"""
    dwDeviceNum: int  # c_uint32, offset 0, size 4
    szDeviceName: bytes  # c_char[50], offset 4, size 50
    nNumOfSubdevices: int  # c_int16, offset 54, size 2
    def __init__(
        self,
        dwDeviceNum: int = ...,
        szDeviceName: bytes = ...,
        nNumOfSubdevices: int = ...,
    ) -> None: ...

class ADVAPI_MDEVICE_INFO(Structure):
    """sizeof = 88 bytes"""
    totalTxLen: int  # c_uint32, offset 0, size 4
    totalRxLen: int  # c_uint32, offset 4, size 4
    cyclicTimeNS: int  # c_uint32, offset 8, size 4
    slave_count: int  # c_uint32, offset 12, size 4
    link_up: int  # c_uint32, offset 16, size 4
    phase: int  # c_uint8, offset 20, size 1
    active: int  # c_uint8, offset 21, size 1
    scan_busy: int  # c_uint8, offset 22, size 1
    ring_type: int  # c_uint8, offset 23, size 1
    num_devices: int  # c_uint32, offset 24, size 4
    tx_count: int  # c_uint64, offset 32, size 8
    rx_count: int  # c_uint64, offset 40, size 8
    tx_bytes: int  # c_uint64, offset 48, size 8
    rx_bytes: int  # c_uint64, offset 56, size 8
    dc_ref_time: int  # c_uint64, offset 64, size 8
    app_time: int  # c_uint64, offset 72, size 8
    ref_clock: int  # c_uint16, offset 80, size 2
    reserved2: int  # c_uint16, offset 82, size 2
    def __init__(
        self,
        totalTxLen: int = ...,
        totalRxLen: int = ...,
        cyclicTimeNS: int = ...,
        slave_count: int = ...,
        link_up: int = ...,
        phase: int = ...,
        active: int = ...,
        scan_busy: int = ...,
        ring_type: int = ...,
        num_devices: int = ...,
        tx_count: int = ...,
        rx_count: int = ...,
        tx_bytes: int = ...,
        rx_bytes: int = ...,
        dc_ref_time: int = ...,
        app_time: int = ...,
        ref_clock: int = ...,
        reserved2: int = ...,
    ) -> None: ...

class DEV_IO_MAP_INFO(Structure):
    """sizeof = 192 bytes"""
    Name: bytes  # c_char[50], offset 0, size 50
    Index: int  # c_uint32, offset 52, size 4
    Offset: int  # c_uint32, offset 56, size 4
    ByteLength: int  # c_uint32, offset 60, size 4
    SlotID: int  # c_uint32, offset 64, size 4
    PortChanID: int  # c_uint32, offset 68, size 4
    ModuleID: int  # c_uint32, offset 72, size 4
    ModuleName: bytes  # c_char[16], offset 76, size 16
    Description: bytes  # c_char[100], offset 92, size 100
    def __init__(
        self,
        Name: bytes = ...,
        Index: int = ...,
        Offset: int = ...,
        ByteLength: int = ...,
        SlotID: int = ...,
        PortChanID: int = ...,
        ModuleID: int = ...,
        ModuleName: bytes = ...,
        Description: bytes = ...,
    ) -> None: ...

class LINK_PORT_INFO(Structure):
    """sizeof = 20 bytes"""
    desc: int  # c_uint32, offset 0, size 4
    link_up: int  # c_uint8, offset 4, size 1
    loop_closed: int  # c_uint8, offset 5, size 1
    signal_detected: int  # c_uint8, offset 6, size 1
    receive_time: int  # c_uint32, offset 8, size 4
    next_slave: int  # c_uint16, offset 12, size 2
    delay_to_next_dc: int  # c_uint32, offset 16, size 4
    def __init__(
        self,
        desc: int = ...,
        link_up: int = ...,
        loop_closed: int = ...,
        signal_detected: int = ...,
        receive_time: int = ...,
        next_slave: int = ...,
        delay_to_next_dc: int = ...,
    ) -> None: ...

class ADVAPI_SUBDEVICE_INFO_CM2(Structure):
    """sizeof = 180 bytes"""
    Position: int  # c_uint16, offset 0, size 2
    VendorID: int  # c_uint32, offset 4, size 4
    ProductID: int  # c_uint32, offset 8, size 4
    RevisionNo: int  # c_uint32, offset 12, size 4
    SerialNo: int  # c_uint32, offset 16, size 4
    SubDeviceID: int  # c_uint16, offset 20, size 2
    current_on_ebus: int  # c_int16, offset 22, size 2
    ports: _CArray[LINK_PORT_INFO]  # LINK_PORT_INFO[4], offset 24, size 80
    al_state: int  # c_uint8, offset 104, size 1
    error_flag: int  # c_uint8, offset 105, size 1
    sync_count: int  # c_uint8, offset 106, size 1
    Reserved: int  # c_uint8, offset 107, size 1
    transmission_delay: int  # c_uint32, offset 108, size 4
    dc_configure: int  # c_uint16, offset 112, size 2
    DeviceName: bytes  # c_char[64], offset 114, size 64
    def __init__(
        self,
        Position: int = ...,
        VendorID: int = ...,
        ProductID: int = ...,
        RevisionNo: int = ...,
        SerialNo: int = ...,
        SubDeviceID: int = ...,
        current_on_ebus: int = ...,
        ports: _CArray[LINK_PORT_INFO] | tuple[LINK_PORT_INFO, ...] = ...,
        al_state: int = ...,
        error_flag: int = ...,
        sync_count: int = ...,
        Reserved: int = ...,
        transmission_delay: int = ...,
        dc_configure: int = ...,
        DeviceName: bytes = ...,
    ) -> None: ...

class PHASE_AXIS_PRM(Structure):
    """sizeof = 32 bytes"""
    Acc: float  # c_double, offset 0, size 8
    Dec: float  # c_double, offset 8, size 8
    PhaseVel: float  # c_double, offset 16, size 8
    PhaseDistance: float  # c_double, offset 24, size 8
    def __init__(
        self,
        Acc: float = ...,
        Dec: float = ...,
        PhaseVel: float = ...,
        PhaseDistance: float = ...,
    ) -> None: ...

class SPEED_PROFILE_PRM(Structure):
    """sizeof = 40 bytes"""
    FH: float  # c_double, offset 0, size 8
    FL: float  # c_double, offset 8, size 8
    Acc: float  # c_double, offset 16, size 8
    Dec: float  # c_double, offset 24, size 8
    JerkFac: float  # c_double, offset 32, size 8
    def __init__(
        self,
        FH: float = ...,
        FL: float = ...,
        Acc: float = ...,
        Dec: float = ...,
        JerkFac: float = ...,
    ) -> None: ...

class MOTION_IO(Structure):
    """sizeof = 21 bytes"""
    RDY: int  # c_uint8, offset 0, size 1
    ALM: int  # c_uint8, offset 1, size 1
    LMT_P: int  # c_uint8, offset 2, size 1
    LMT_N: int  # c_uint8, offset 3, size 1
    ORG: int  # c_uint8, offset 4, size 1
    DIR: int  # c_uint8, offset 5, size 1
    EMG: int  # c_uint8, offset 6, size 1
    PCS: int  # c_uint8, offset 7, size 1
    ERC: int  # c_uint8, offset 8, size 1
    EZ: int  # c_uint8, offset 9, size 1
    CLR: int  # c_uint8, offset 10, size 1
    LTC: int  # c_uint8, offset 11, size 1
    SD: int  # c_uint8, offset 12, size 1
    INP: int  # c_uint8, offset 13, size 1
    SVON: int  # c_uint8, offset 14, size 1
    ALRM: int  # c_uint8, offset 15, size 1
    SLMT_P: int  # c_uint8, offset 16, size 1
    SLMT_N: int  # c_uint8, offset 17, size 1
    CMP: int  # c_uint8, offset 18, size 1
    CAMDO: int  # c_uint8, offset 19, size 1
    RESETREADY: int  # c_uint8, offset 20, size 1
    def __init__(
        self,
        RDY: int = ...,
        ALM: int = ...,
        LMT_P: int = ...,
        LMT_N: int = ...,
        ORG: int = ...,
        DIR: int = ...,
        EMG: int = ...,
        PCS: int = ...,
        ERC: int = ...,
        EZ: int = ...,
        CLR: int = ...,
        LTC: int = ...,
        SD: int = ...,
        INP: int = ...,
        SVON: int = ...,
        ALRM: int = ...,
        SLMT_P: int = ...,
        SLMT_N: int = ...,
        CMP: int = ...,
        CAMDO: int = ...,
        RESETREADY: int = ...,
    ) -> None: ...

class VALIDATE_RESULT(Structure):
    """sizeof = 332 bytes"""
    index: int  # c_int32, offset 0, size 4
    context: _CArray[_CCharArray]  # c_char[5][64], offset 4, size 320
    context_count: int  # c_int32, offset 324, size 4
    context_error_line: int  # c_int32, offset 328, size 4
    def __init__(
        self,
        index: int = ...,
        context: _CArray[_CCharArray] | tuple[bytes, ...] = ...,
        context_count: int = ...,
        context_error_line: int = ...,
    ) -> None: ...

class PATH_STATUS(Structure):
    """sizeof = 16 bytes"""
    CurIndex: int  # c_uint32, offset 0, size 4
    CurCmdFunc: int  # c_uint32, offset 4, size 4
    RemainCount: int  # c_uint32, offset 8, size 4
    FreeSpaceCount: int  # c_uint32, offset 12, size 4
    def __init__(
        self,
        CurIndex: int = ...,
        CurCmdFunc: int = ...,
        RemainCount: int = ...,
        FreeSpaceCount: int = ...,
    ) -> None: ...

class CAM_IN_PRM(Structure):
    """sizeof = 40 bytes"""
    PrimaryOffset: float  # c_double, offset 0, size 8
    FollowingOffset: float  # c_double, offset 8, size 8
    PrimaryScaling: float  # c_double, offset 16, size 8
    FollowingScaling: float  # c_double, offset 24, size 8
    CamTableID: int  # c_uint32, offset 32, size 4
    RefSrc: int  # c_uint32, offset 36, size 4
    def __init__(
        self,
        PrimaryOffset: float = ...,
        FollowingOffset: float = ...,
        PrimaryScaling: float = ...,
        FollowingScaling: float = ...,
        CamTableID: int = ...,
        RefSrc: int = ...,
    ) -> None: ...

class GEAR_RATIO_RATE(Structure):
    """sizeof = 16 bytes, _pack_ = 1"""
    Num: float  # c_double, offset 0, size 8
    Den: float  # c_double, offset 8, size 8
    def __init__(
        self,
        Num: float = ...,
        Den: float = ...,
    ) -> None: ...

class GEAR_IN_PRM(Structure):
    """sizeof = 32 bytes"""
    RefSrc: int  # c_uint32, offset 0, size 4
    GearRatioRate: GEAR_RATIO_RATE  # GEAR_RATIO_RATE, offset 4, size 16
    Mode: int  # c_uint32, offset 20, size 4
    GearPosition: float  # c_double, offset 24, size 8
    def __init__(
        self,
        RefSrc: int = ...,
        GearRatioRate: GEAR_RATIO_RATE = ...,
        Mode: int = ...,
        GearPosition: float = ...,
    ) -> None: ...

class TANGENT_IN_PRM(Structure):
    """sizeof = 20 bytes"""
    StartVectorArray: _CArray[int]  # c_int32[3], offset 0, size 12
    Working_plane: int  # c_uint32, offset 12, size 4
    Direction: int  # c_uint32, offset 16, size 4
    def __init__(
        self,
        StartVectorArray: _CArray[int] | tuple[int, ...] = ...,
        Working_plane: int = ...,
        Direction: int = ...,
    ) -> None: ...

class GANTRY_IN_PRM(Structure):
    """sizeof = 4 bytes"""
    RefSrc: int  # c_int16, offset 0, size 2
    Direction: int  # c_int16, offset 2, size 2
    def __init__(
        self,
        RefSrc: int = ...,
        Direction: int = ...,
    ) -> None: ...

class BUFFER_STATUS(Structure):
    """sizeof = 12 bytes"""
    CurIndex: int  # c_uint32, offset 0, size 4
    RemainCount: int  # c_uint32, offset 4, size 4
    FreeSpaceCount: int  # c_uint32, offset 8, size 4
    def __init__(
        self,
        CurIndex: int = ...,
        RemainCount: int = ...,
        FreeSpaceCount: int = ...,
    ) -> None: ...

class JOG_SPEED_PROFILE_PRM(Structure):
    """sizeof = 40 bytes"""
    FH: float  # c_double, offset 0, size 8
    FL: float  # c_double, offset 8, size 8
    Acc: float  # c_double, offset 16, size 8
    Dec: float  # c_double, offset 24, size 8
    VLTime: float  # c_double, offset 32, size 8
    def __init__(
        self,
        FH: float = ...,
        FL: float = ...,
        Acc: float = ...,
        Dec: float = ...,
        VLTime: float = ...,
    ) -> None: ...

class PATH_DO_MODE0(Structure):
    """sizeof = 12 bytes"""
    DOPort: int  # c_uint32, offset 0, size 4
    DOEnable: int  # c_uint32, offset 4, size 4
    DOValue: int  # c_uint32, offset 8, size 4
    def __init__(
        self,
        DOPort: int = ...,
        DOEnable: int = ...,
        DOValue: int = ...,
    ) -> None: ...

class PATH_DO_MODE1(Structure):
    """sizeof = 16 bytes"""
    SubDeviceID: int  # c_uint32, offset 0, size 4
    DOPort: int  # c_uint32, offset 4, size 4
    DOEnable: int  # c_uint32, offset 8, size 4
    DOValue: int  # c_uint32, offset 12, size 4
    def __init__(
        self,
        SubDeviceID: int = ...,
        DOPort: int = ...,
        DOEnable: int = ...,
        DOValue: int = ...,
    ) -> None: ...

class PATH_DO_MODE2(Structure):
    """sizeof = 12 bytes"""
    AxID: int  # c_uint32, offset 0, size 4
    DOEnable: int  # c_uint32, offset 4, size 4
    DOValue: int  # c_uint32, offset 8, size 4
    def __init__(
        self,
        AxID: int = ...,
        DOEnable: int = ...,
        DOValue: int = ...,
    ) -> None: ...

class PATH_DO_MODE(Structure):
    """sizeof = 40 bytes"""
    Mode0: PATH_DO_MODE0  # PATH_DO_MODE0, offset 0, size 12
    Mode1: PATH_DO_MODE1  # PATH_DO_MODE1, offset 12, size 16
    Mode2: PATH_DO_MODE2  # PATH_DO_MODE2, offset 28, size 12
    def __init__(
        self,
        Mode0: PATH_DO_MODE0 = ...,
        Mode1: PATH_DO_MODE1 = ...,
        Mode2: PATH_DO_MODE2 = ...,
    ) -> None: ...

class PATH_DO_PRM(Structure):
    """sizeof = 56 bytes"""
    MoveMode: int  # c_uint32, offset 0, size 4
    PathDO_Prm: PATH_DO_MODE  # PATH_DO_MODE, offset 4, size 40
    DO_Output_Time: float  # c_double, offset 48, size 8
    def __init__(
        self,
        MoveMode: int = ...,
        PathDO_Prm: PATH_DO_MODE = ...,
        DO_Output_Time: float = ...,
    ) -> None: ...

class TRIG_PRM(Structure):
    """sizeof = 48 bytes"""
    TriggerType: int  # c_uint32, offset 0, size 4
    CompareMethod: int  # c_int32, offset 4, size 4
    TriggerValue: float  # c_double, offset 8, size 8
    Range: float  # c_double, offset 16, size 8
    TriggerAxis: int  # c_uint32, offset 24, size 4
    Index: int  # c_uint32, offset 28, size 4
    SubIndex: int  # c_uint32, offset 32, size 4
    RingNo: int  # c_uint32, offset 36, size 4
    SubDeviceID: int  # c_uint32, offset 40, size 4
    def __init__(
        self,
        TriggerType: int = ...,
        CompareMethod: int = ...,
        TriggerValue: float = ...,
        Range: float = ...,
        TriggerAxis: int = ...,
        Index: int = ...,
        SubIndex: int = ...,
        RingNo: int = ...,
        SubDeviceID: int = ...,
    ) -> None: ...

class PATH_DI_WAIT_MODE0(Structure):
    """sizeof = 12 bytes"""
    DIPort: int  # c_uint32, offset 0, size 4
    DIEnable: int  # c_uint32, offset 4, size 4
    DIValue: int  # c_uint32, offset 8, size 4
    def __init__(
        self,
        DIPort: int = ...,
        DIEnable: int = ...,
        DIValue: int = ...,
    ) -> None: ...

class PATH_DI_WAIT_MODE1(Structure):
    """sizeof = 16 bytes"""
    SubDeviceID: int  # c_uint32, offset 0, size 4
    DIPort: int  # c_uint32, offset 4, size 4
    DIEnable: int  # c_uint32, offset 8, size 4
    DIValue: int  # c_uint32, offset 12, size 4
    def __init__(
        self,
        SubDeviceID: int = ...,
        DIPort: int = ...,
        DIEnable: int = ...,
        DIValue: int = ...,
    ) -> None: ...

class PATH_DI_WAIT_MODE2(Structure):
    """sizeof = 12 bytes"""
    AxID: int  # c_uint32, offset 0, size 4
    DIEnable: int  # c_uint32, offset 4, size 4
    DIValue: int  # c_uint32, offset 8, size 4
    def __init__(
        self,
        AxID: int = ...,
        DIEnable: int = ...,
        DIValue: int = ...,
    ) -> None: ...

class PATH_DI_WAIT_MODE(Structure):
    """sizeof = 40 bytes"""
    Mode0: PATH_DI_WAIT_MODE0  # PATH_DI_WAIT_MODE0, offset 0, size 12
    Mode1: PATH_DI_WAIT_MODE1  # PATH_DI_WAIT_MODE1, offset 12, size 16
    Mode2: PATH_DI_WAIT_MODE2  # PATH_DI_WAIT_MODE2, offset 28, size 12
    def __init__(
        self,
        Mode0: PATH_DI_WAIT_MODE0 = ...,
        Mode1: PATH_DI_WAIT_MODE1 = ...,
        Mode2: PATH_DI_WAIT_MODE2 = ...,
    ) -> None: ...

class PATH_DI_WAIT_PRM(Structure):
    """sizeof = 56 bytes"""
    MoveMode: int  # c_uint32, offset 0, size 4
    PathDI_Prm: PATH_DI_WAIT_MODE  # PATH_DI_WAIT_MODE, offset 4, size 40
    DI_Wait_Time: float  # c_double, offset 48, size 8
    def __init__(
        self,
        MoveMode: int = ...,
        PathDI_Prm: PATH_DI_WAIT_MODE = ...,
        DI_Wait_Time: float = ...,
    ) -> None: ...

class PATH_AX_WAIT_PRM(Structure):
    """sizeof = 40 bytes"""
    AxID: int  # c_uint32, offset 0, size 4
    CmpMethod: int  # c_uint32, offset 4, size 4
    CmpValue: float  # c_double, offset 8, size 8
    ValueRange: float  # c_double, offset 16, size 8
    CmpSrc: int  # c_uint32, offset 24, size 4
    Timeout: float  # c_double, offset 32, size 8
    def __init__(
        self,
        AxID: int = ...,
        CmpMethod: int = ...,
        CmpValue: float = ...,
        ValueRange: float = ...,
        CmpSrc: int = ...,
        Timeout: float = ...,
    ) -> None: ...

class PWM_TABLE_STATUS(Structure):
    """sizeof = 8 bytes"""
    Velocity: int  # c_uint32, offset 0, size 4
    PWMValue: int  # c_uint32, offset 4, size 4
    def __init__(
        self,
        Velocity: int = ...,
        PWMValue: int = ...,
    ) -> None: ...

class OSC_PROFILE_PRM(Structure):
    """sizeof = 28 bytes"""
    Enable: int  # c_uint32, offset 0, size 4
    Period: int  # c_uint32, offset 4, size 4
    AxidNo: int  # c_uint32, offset 8, size 4
    ChanType: int  # c_uint32, offset 12, size 4
    ChanProperty: int  # c_uint32, offset 16, size 4
    TrigMode: int  # c_uint32, offset 20, size 4
    TimeWidth: int  # c_uint32, offset 24, size 4
    def __init__(
        self,
        Enable: int = ...,
        Period: int = ...,
        AxidNo: int = ...,
        ChanType: int = ...,
        ChanProperty: int = ...,
        TrigMode: int = ...,
        TimeWidth: int = ...,
    ) -> None: ...

class ADVAPI_IO_LINK_INFO(Structure):
    """sizeof = 216 bytes"""
    DeviceName: bytes  # c_char[48], offset 0, size 48
    SubDeviceID: int  # c_uint32, offset 48, size 4
    Position: int  # c_uint32, offset 52, size 4
    VendorID: int  # c_uint32, offset 56, size 4
    ProductID: int  # c_uint32, offset 60, size 4
    SubDeviceName: bytes  # c_char[64], offset 64, size 64
    PhysicRingNo: int  # c_uint32, offset 128, size 4
    PortType: int  # c_int32, offset 132, size 4
    PhysicNo: int  # c_uint32, offset 136, size 4
    EntryName: bytes  # c_char[64], offset 140, size 64
    EntryIndex: int  # c_uint32, offset 204, size 4
    EntrySubIndex: int  # c_uint32, offset 208, size 4
    BitLength: int  # c_uint32, offset 212, size 4
    def __init__(
        self,
        DeviceName: bytes = ...,
        SubDeviceID: int = ...,
        Position: int = ...,
        VendorID: int = ...,
        ProductID: int = ...,
        SubDeviceName: bytes = ...,
        PhysicRingNo: int = ...,
        PortType: int = ...,
        PhysicNo: int = ...,
        EntryName: bytes = ...,
        EntryIndex: int = ...,
        EntrySubIndex: int = ...,
        BitLength: int = ...,
    ) -> None: ...

class PATH_VAR_PRM(Structure):
    """sizeof = 24 bytes"""
    VarID: int  # c_uint32, offset 0, size 4
    CmpMethod: int  # c_uint32, offset 4, size 4
    CmpValue: float  # c_double, offset 8, size 8
    ValueRange: float  # c_double, offset 16, size 8
    def __init__(
        self,
        VarID: int = ...,
        CmpMethod: int = ...,
        CmpValue: float = ...,
        ValueRange: float = ...,
    ) -> None: ...

class MULTI_SDO_REQ(Structure):
    """sizeof = 16 bytes"""
    SubDeviceID: int  # c_uint16, offset 0, size 2
    Index: int  # c_uint16, offset 2, size 2
    SubIndex: int  # c_uint16, offset 4, size 2
    Type: int  # c_uint16, offset 6, size 2
    Data: int  # c_uint32, offset 8, size 4
    ErrorCode: int  # c_uint32, offset 12, size 4
    def __init__(
        self,
        SubDeviceID: int = ...,
        Index: int = ...,
        SubIndex: int = ...,
        Type: int = ...,
        Data: int = ...,
        ErrorCode: int = ...,
    ) -> None: ...

class PATH_OPERATOR_PRM(Structure):
    """sizeof = 12 bytes"""
    VarID: int  # c_uint32, offset 0, size 4
    Operator: int  # c_uint32, offset 4, size 4
    Value: int  # c_int32, offset 8, size 4
    def __init__(
        self,
        VarID: int = ...,
        Operator: int = ...,
        Value: int = ...,
    ) -> None: ...

class AMC_API_LOG_OPT(Structure):
    """sizeof = 8 bytes"""
    sizePerFile: int  # c_uint32, offset 0, size 4
    excludePolling: int  # c_uint8, offset 4, size 1
    def __init__(
        self,
        sizePerFile: int = ...,
        excludePolling: int = ...,
    ) -> None: ...

class AMC_API_LOG_HEADER(Structure):
    """sizeof = 21 bytes, _pack_ = 1"""
    timestamp: int  # c_int64, offset 0, size 8
    logId: int  # c_uint16, offset 8, size 2
    type: int  # c_uint8, offset 10, size 1
    functionId: int  # c_uint16, offset 11, size 2
    dataLen: int  # c_uint32, offset 13, size 4
    threadId: int  # c_uint32, offset 17, size 4
    def __init__(
        self,
        timestamp: int = ...,
        logId: int = ...,
        type: int = ...,
        functionId: int = ...,
        dataLen: int = ...,
        threadId: int = ...,
    ) -> None: ...

class AMC_API_LOG_STATUS(Structure):
    """sizeof = 12 bytes"""
    state: int  # c_uint8, offset 0, size 1
    totalQueueSize: int  # c_int32, offset 4, size 4
    usedQueueSize: int  # c_uint32, offset 8, size 4
    def __init__(
        self,
        state: int = ...,
        totalQueueSize: int = ...,
        usedQueueSize: int = ...,
    ) -> None: ...

class AMC_DATA_LOG_OPTIONS(Structure):
    """sizeof = 28 bytes"""
    samplingTimeMilliseconds: int  # c_int32, offset 0, size 4
    samplingPeriodInCycles: int  # c_uint32, offset 4, size 4
    isRotateFile: int  # c_uint8, offset 8, size 1
    maxLogFileCount: int  # c_uint32, offset 12, size 4
    maxLogFileSize: int  # c_int32, offset 16, size 4
    stopLoggingOnBufferOverflow: int  # c_uint8, offset 20, size 1
    delimiter: bytes  # c_char, offset 21, size 1
    triggerOnCondition: int  # c_uint8, offset 22, size 1
    triggerOnEvent: int  # c_uint8, offset 23, size 1
    triggerEventID: int  # c_uint32, offset 24, size 4
    def __init__(
        self,
        samplingTimeMilliseconds: int = ...,
        samplingPeriodInCycles: int = ...,
        isRotateFile: int = ...,
        maxLogFileCount: int = ...,
        maxLogFileSize: int = ...,
        stopLoggingOnBufferOverflow: int = ...,
        delimiter: bytes = ...,
        triggerOnCondition: int = ...,
        triggerOnEvent: int = ...,
        triggerEventID: int = ...,
    ) -> None: ...

class AMC_DATA_LOG_SM_ITEMS(Structure):
    """sizeof = 4 bytes"""
    cmd_pos: int  # c_uint8, offset 0, size 1
    act_pos: int  # c_uint8, offset 1, size 1
    cmd_vel: int  # c_uint8, offset 2, size 1
    act_vel: int  # c_uint8, offset 3, size 1
    def __init__(
        self,
        cmd_pos: int = ...,
        act_pos: int = ...,
        cmd_vel: int = ...,
        act_vel: int = ...,
    ) -> None: ...

class AMC_DATA_LOG_SOURCE_ITEMS(Union):
    """sizeof = 4 bytes"""
    smItems: AMC_DATA_LOG_SM_ITEMS  # AMC_DATA_LOG_SM_ITEMS, offset 0, size 4
    def __init__(
        self,
        smItems: AMC_DATA_LOG_SM_ITEMS = ...,
    ) -> None: ...

class AMC_DATA_LOG_SOURCE(Structure):
    """sizeof = 268 bytes"""
    selection: _CArray[int]  # c_uint32[64], offset 0, size 256
    count: int  # c_uint32, offset 256, size 4
    type: int  # c_uint32, offset 260, size 4
    items: AMC_DATA_LOG_SOURCE_ITEMS  # AMC_DATA_LOG_SOURCE_ITEMS, offset 264, size 4
    def __init__(
        self,
        selection: _CArray[int] | tuple[int, ...] = ...,
        count: int = ...,
        type: int = ...,
        items: AMC_DATA_LOG_SOURCE_ITEMS = ...,
    ) -> None: ...

class AMC_DATA_LOG_STATUS(Structure):
    """sizeof = 56 bytes"""
    state: int  # c_uint32, offset 0, size 4
    samplesToCollect: int  # c_uint64, offset 8, size 8
    millisecondsToCollect: int  # c_int64, offset 16, size 8
    samplesCollected: int  # c_uint64, offset 24, size 8
    samplesWritten: int  # c_uint64, offset 32, size 8
    currentFileIndex: int  # c_uint32, offset 40, size 4
    currentFileSize: int  # c_int32, offset 44, size 4
    stopRequest: int  # c_uint8, offset 48, size 1
    def __init__(
        self,
        state: int = ...,
        samplesToCollect: int = ...,
        millisecondsToCollect: int = ...,
        samplesCollected: int = ...,
        samplesWritten: int = ...,
        currentFileIndex: int = ...,
        currentFileSize: int = ...,
        stopRequest: int = ...,
    ) -> None: ...
