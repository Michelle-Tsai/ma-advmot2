# -*- coding: utf-8 -*-
"""
AMC Data Log 完整測試

測試分類
  TestBoundary        參數邊界：Channel / index / count / 軸號 / 選項 / NULL 指標
  TestStateMachine    狀態機：各狀態下 API 是否允許、Start/Stop/Reset 轉換
  TestSingleChannel   單通道：單軸、多軸、重複軸、跨資料源、採樣週期、最大軸數
  TestMultiChannel    多通道：多通道多軸、多通道最大軸數、不同採樣週期同時記錄
  TestFileFeatures    檔案：自訂標頭、分隔字元、檔案輪替、取檔緩衝區不足
  TestStress          壓力測試（預設略過，加 --stress 才執行）

執行方式
  python AmcDataLogFullTest.py                        # 全部（不含壓力測試）
  python AmcDataLogFullTest.py --axes 8               # 實際只有 8 軸的機台
  python AmcDataLogFullTest.py TestBoundary           # 只跑某一類
  python AmcDataLogFullTest.py TestSingleChannel.test_single_channel_max_axes
  python AmcDataLogFullTest.py --stress -v            # 含壓力測試

注意
  * 本程式依 Data Log 規格撰寫，部分測試會揭露尚未修正的 DLL / RT 問題
    （例如 StopLog 未處理 STOP 狀態、多通道共用 writerThread），失敗訊息會說明原因。
  * 記錄檔會下載到 --out 指定的目錄（預設 ./datalog_test_out），方便事後檢查。
"""
import argparse
import os
import sys
import time
import unittest
from ctypes import (byref, c_char, c_uint8, c_uint16, c_uint32, c_int32,
                    create_string_buffer, sizeof)

from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2, AmcLogAPI
from AcmP.AdvMotErr_CM2 import ErrorCode2
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *

# =============================================================================
# 設定（可由命令列覆寫）
# =============================================================================
class Cfg:
    DEV_ID = 0
    AXES = 128              # 機台實際可用的軸數（gPort.MaxAxisNum）
    RT_FREQ = 1000          # RT 每秒 cycle 數（1 ms cycle = 1000）
    REMOTE_DIR = b'/tmp'
    OUT_DIR = 'datalog_test_out'
    STRESS = False
    VERBOSE = False

# 與 amc_log.h / AmcDataLog.h 一致的常數
MAX_LOG_CHANNELS = 4
MAX_DATASOURCES = 4
MAX_SELECTIONS = 64
LOG_MAX_AXES = 128
MAX_PATH = 256
RING_CAPACITY = 2000        # 每通道封包數（實際可用 1999）

# LogState
ST_IDLE, ST_WAIT, ST_RUNNING, ST_STOP, ST_FINISHED, ST_WRITE_FAIL, ST_OVERFLOW, ST_ERROR = range(8)
STATE_NAME = ['IDLE', 'WAITING_FOR_TRIGGER', 'RUNNING', 'STOP', 'FINISHED',
              'WRITE_FAIL', 'BUFFER_OVERFLOW', 'ERROR']
DONE_STATES = (ST_STOP, ST_FINISHED, ST_WRITE_FAIL, ST_OVERFLOW, ST_ERROR)

# LogSourceType
SRC_NONE, SRC_AXIS, SRC_IO = 0, 1, 2

# LogError（amc_log.h）
SUCCESS = 0
E_PARAM = 0xFF
E_STATE = 0x100
E_DS_LIMIT = 0x102
E_THREAD = 0x105
E_SHM = 0x106
E_BUF_SMALL = ErrorCode2.BufferTooSmall
E_MEM = int(ErrorCode2.MemAllocateFailed) if hasattr(ErrorCode2, 'MemAllocateFailed') else None


def hx(v):
    return f'0x{int(v):X}'


def state_name(s):
    return STATE_NAME[s] if 0 <= s < len(STATE_NAME) else f'?({s})'


# =============================================================================
# API 包裝：統一函式名稱（Python 模組中有 Amc_DataLogXxx 與 Amc_DataLog_Xxx 兩種寫法）
# =============================================================================
class DataLog:
    def __init__(self, api):
        self.api = api

    def _fn(self, name):
        for cand in (f'Amc_DataLog{name}', f'Amc_DataLog_{name}'):
            f = getattr(self.api, cand, None)
            if f is not None:
                return f
        raise AttributeError(f'AmcLogAPI 找不到 Amc_DataLog{name} / Amc_DataLog_{name}')

    def set_log(self, ch, src, index):
        return self._fn('SetLog')(Cfg.DEV_ID, c_uint32(ch), byref(src) if src is not None else None, c_uint16(index))

    def get_log(self, ch, index):
        src = AMC_DATA_LOG_SOURCE()
        err = self._fn('GetLog')(Cfg.DEV_ID, c_uint32(ch), byref(src), c_uint16(index))
        return err, src

    def set_option(self, ch, opt):
        return self._fn('SetLogOption')(Cfg.DEV_ID, c_uint32(ch), byref(opt) if opt is not None else None)

    def get_option(self, ch):
        opt = AMC_DATA_LOG_OPTIONS()
        err = self._fn('GetLogOption')(Cfg.DEV_ID, c_uint32(ch), byref(opt))
        return err, opt

    def set_path(self, ch, d, f):
        return self._fn('SetLogFilePath')(Cfg.DEV_ID, c_uint32(ch), d, f)

    def get_path(self, ch):
        d, f = create_string_buffer(MAX_PATH), create_string_buffer(MAX_PATH)
        err = self._fn('GetLogFilePath')(Cfg.DEV_ID, c_uint32(ch), d, f)
        return err, d.value, f.value

    def set_header(self, ch, h):
        return self._fn('SetLogHeader')(Cfg.DEV_ID, c_uint32(ch), h)

    def get_header(self, ch):
        h = create_string_buffer(MAX_PATH)
        err = self._fn('GetLogHeader')(Cfg.DEV_ID, c_uint32(ch), h)
        return err, h.value

    def status(self, ch):
        st = AMC_DATA_LOG_STATUS()
        err = self._fn('GetStatus')(Cfg.DEV_ID, c_uint32(ch), byref(st))
        return err, st

    def start(self, ch):
        return self._fn('StartLog')(Cfg.DEV_ID, c_uint32(ch))

    def stop(self, ch):
        return self._fn('StopLog')(Cfg.DEV_ID, c_uint32(ch))

    def reset(self, ch):
        return self._fn('ResetLog')(Cfg.DEV_ID, c_uint32(ch))

    def rotated_paths(self, ch, buf_size=4096):
        size = c_uint32(buf_size)
        buf = create_string_buffer(max(buf_size, 1))
        cnt = c_uint32(0)
        err = self._fn('GetRotatedLogFilePaths')(Cfg.DEV_ID, c_uint32(ch), buf, byref(size), byref(cnt))
        names = []
        if err == SUCCESS:
            raw = buf.raw[:size.value]
            names = [n for n in raw.split(b'\0') if n][:cnt.value]
        return err, names, size.value, cnt.value

    def get_file_raw(self, path, buf_size):
        size = c_uint32(buf_size)
        buf = create_string_buffer(max(buf_size, 1))
        err = self._fn('GetLogFile')(Cfg.DEV_ID, c_uint32(0), path, buf, byref(size))
        return err, buf, size.value

    def get_file(self, path):
        """先用 1 byte 查詢大小，再配置足夠的緩衝區讀取"""
        err, buf, size = self.get_file_raw(path, 1)
        if err == SUCCESS:
            return err, buf.raw[:size]
        if E_MEM is not None and err == E_MEM:
            err, buf, got = self.get_file_raw(path, size + 1)
            return err, buf.raw[:got] if err == SUCCESS else b''
        return err, b''


# =============================================================================
# 建立結構的輔助函式
# =============================================================================
def make_axis_source(axes, cmd_pos=1, act_pos=1, cmd_vel=0, act_vel=0, count=None):
    src = AMC_DATA_LOG_SOURCE()
    src.type = SRC_AXIS
    for i, a in enumerate(axes):
        src.selection[i] = a
    src.count = len(axes) if count is None else count
    src.items.smItems.cmd_pos = cmd_pos
    src.items.smItems.act_pos = act_pos
    src.items.smItems.cmd_vel = cmd_vel
    src.items.smItems.act_vel = act_vel
    return src


def make_none_source():
    src = AMC_DATA_LOG_SOURCE()
    src.type = SRC_NONE
    src.count = 0
    return src


def make_option(ms=0, period=1, rotate=False, file_cnt=1, file_size=0,
                stop_on_overflow=1, delimiter=b' ', trig_event=0, event_id=0):
    opt = AMC_DATA_LOG_OPTIONS()
    opt.samplingTimeMilliseconds = ms
    opt.samplingPeriodInCycles = period
    opt.isRotateFile = 1 if rotate else 0
    opt.maxLogFileCount = file_cnt
    opt.maxLogFileSize = file_size
    opt.stopLoggingOnBufferOverflow = stop_on_overflow
    opt.delimiter = delimiter
    opt.triggerOnCondition = 0
    opt.triggerOnEvent = trig_event
    opt.triggerEventID = event_id
    return opt


def chunks(seq, n):
    return [seq[i:i + n] for i in range(0, len(seq), n)]


# =============================================================================
# 記錄檔解析
# =============================================================================
class ParsedLog:
    def __init__(self, raw, delimiter=' ', custom_header=None):
        text = raw.decode('utf-8', errors='replace')
        lines = [l for l in text.splitlines() if l != '']
        self.custom_header = None
        if custom_header:
            self.custom_header = lines.pop(0) if lines else None
        self.axis_header = None
        self.io_header = None
        self.rows = []          # (type, id, [values])
        self.bad_lines = []
        d = delimiter
        for ln in lines:
            if ln.startswith('EventType'):
                cols = ln.split(d)
                if self.axis_header is None and 'Value' not in cols:
                    self.axis_header = cols
                else:
                    self.io_header = cols
                continue
            parts = ln.split(d)
            if len(parts) < 2 or parts[0] not in ('AXIS', 'IO'):
                self.bad_lines.append(ln)
                continue
            try:
                self.rows.append((parts[0], int(parts[1]), [int(v) for v in parts[2:]]))
            except ValueError:
                self.bad_lines.append(ln)

    def axis_rows(self):
        return [r for r in self.rows if r[0] == 'AXIS']

    def count_by_axis(self):
        c = {}
        for _, a, _v in self.axis_rows():
            c[a] = c.get(a, 0) + 1
        return c


# =============================================================================
# 共用基底類別
# =============================================================================
dl = DataLog(AmcLogAPI)
_device_ready = False


def setUpModule():
    global _device_ready
    devlist = (DEVLIST * 10)()
    out = c_uint32(0)
    err = AdvCmnAPI_CM2.Acm2_GetAvailableDevs(devlist, 10, byref(out))
    if err != 0 or out.value == 0:
        raise unittest.SkipTest(f'找不到設備 err={hx(err)}')
    err = AdvCmnAPI_CM2.Acm2_DevInitialize()
    if err != 0:
        raise unittest.SkipTest(f'Acm2_DevInitialize 失敗 err={hx(err)}')
    os.makedirs(Cfg.OUT_DIR, exist_ok=True)
    _device_ready = True


class DataLogTestBase(unittest.TestCase):
    """每個測試前後都把 4 個通道恢復為 IDLE"""

    def setUp(self):
        self.reset_all()

    def tearDown(self):
        self.reset_all()

    # ---------- 通用動作 ----------
    def reset_all(self):
        for ch in range(MAX_LOG_CHANNELS):
            dl.stop(ch)
            err = dl.reset(ch)
            if err != SUCCESS:
                # 可能仍在 RUNNING（例如 StopLog 失敗），再試一次
                time.sleep(0.2)
                dl.stop(ch)
                dl.reset(ch)

    def ok(self, err, what):
        self.assertEqual(SUCCESS, err, f'{what} 失敗 err={hx(err)}')

    def err_is(self, err, expect, what):
        self.assertEqual(expect, err, f'{what}：預期 {hx(expect)}，實際 {hx(err)}')

    def err_not_ok(self, err, what):
        self.assertNotEqual(SUCCESS, err, f'{what}：預期失敗，實際回傳成功')

    def log(self, msg):
        if Cfg.VERBOSE:
            print(f'    {msg}')

    def remote_name(self, ch, tag):
        return f'pyDL_{self._testMethodName}_ch{ch}_{tag}'.encode()

    def configure(self, ch, sources, opt, name=None, header=b''):
        """設定一個通道：sources 為 [(index, LogDataSource)]"""
        for idx, src in sources:
            self.ok(dl.set_log(ch, src, idx), f'SetLog ch{ch} idx{idx}')
        self.ok(dl.set_option(ch, opt), f'SetLogOption ch{ch}')
        name = name or self.remote_name(ch, 'log')
        self.ok(dl.set_path(ch, Cfg.REMOTE_DIR, name), f'SetLogFilePath ch{ch}')
        self.ok(dl.set_header(ch, header), f'SetLogHeader ch{ch}')
        return Cfg.REMOTE_DIR + b'/' + name + b'.txt'

    def wait_state(self, ch, states, timeout):
        t0 = time.time()
        while True:
            err, st = dl.status(ch)
            self.ok(err, f'GetStatus ch{ch}')
            if st.state in states:
                return st
            if time.time() - t0 > timeout:
                return st
            time.sleep(0.05)

    def finish(self, ch, timeout=10.0):
        """StopLog 並等到寫完：回傳最終狀態"""
        self.ok(dl.stop(ch), f'StopLog ch{ch}')
        t0 = time.time()
        while True:
            err, st = dl.status(ch)
            self.ok(err, f'GetStatus ch{ch}')
            # STOP 也接受：DLL 的 StopLog 若未處理 STOP 狀態，狀態會停在 STOP（由 test_auto_stop_and_stop 專門檢查）
            if st.state in (ST_STOP, ST_FINISHED, ST_OVERFLOW, ST_WRITE_FAIL, ST_ERROR) and \
                    st.samplesWritten >= st.samplesCollected:
                return st
            if time.time() - t0 > timeout:
                return st
            time.sleep(0.05)

    def run_timed(self, chs, ms, extra_wait=3.0):
        """同時啟動多個通道，等待自動停止（STOP）後 StopLog"""
        for ch in chs:
            self.ok(dl.start(ch), f'StartLog ch{ch}')
        result = {}
        for ch in chs:
            st = self.wait_state(ch, DONE_STATES, ms / 1000.0 + extra_wait)
            self.assertIn(st.state, DONE_STATES,
                          f'ch{ch} 超時仍未停止，state={state_name(st.state)} collected={st.samplesCollected}/{st.samplesToCollect}')
            self.assertNotEqual(ST_OVERFLOW, st.state, f'ch{ch} Ring Buffer 溢位')
        for ch in chs:
            st = self.finish(ch)
            if st.state == ST_STOP:
                _warn_once('StopLog 後狀態仍為 STOP（DLL StopLog 未處理 LOG_STATE_STOP），'
                           '內容檢查照常進行；同一測試內再次 StartLog 會失敗')
            else:
                self.assertEqual(ST_FINISHED, st.state, f'ch{ch} StopLog 後狀態為 {state_name(st.state)}，預期 FINISHED')
            self.assertEqual(st.samplesCollected, st.samplesWritten,
                             f'ch{ch} 寫入數 {st.samplesWritten} ≠ 收集數 {st.samplesCollected}')
            result[ch] = st
        return result

    def download(self, remote_path, delimiter=' ', custom_header=None):
        err, raw = dl.get_file(remote_path)
        self.ok(err, f'GetLogFile {remote_path}')
        local = os.path.join(Cfg.OUT_DIR, os.path.basename(remote_path.decode()))
        with open(local, 'wb') as f:
            f.write(raw)
        p = ParsedLog(raw, delimiter, custom_header)
        self.assertEqual([], p.bad_lines[:5], f'{remote_path} 有無法解析的資料行')
        return p

    # ---------- 內容檢查 ----------
    def check_content(self, p, axes, samples=None, cols=None, tolerance=0):
        """axes：預期出現的軸；samples：每軸預期筆數；cols：每行預期數值欄位數"""
        axes = sorted(set(axes))
        self.assertIsNotNone(p.axis_header, '缺少軸的欄位標頭')
        counts = p.count_by_axis()
        self.assertEqual(axes, sorted(counts), '記錄到的軸與設定不符')
        if samples is not None:
            for a in axes:
                self.assertLessEqual(abs(counts[a] - samples), tolerance,
                                     f'軸 {a} 筆數 {counts[a]}，預期 {samples}')
        else:
            vals = set(counts.values())
            self.assertLessEqual(max(vals) - min(vals), 1, f'各軸筆數不一致：{counts}')
        hdr_vals = len(p.axis_header) - 2
        for t, a, v in p.axis_rows():
            self.assertEqual(hdr_vals, len(v), f'軸 {a} 欄位數 {len(v)} 與標頭 {hdr_vals} 不符')
        if cols is not None:
            self.assertEqual(cols, hdr_vals, f'欄位數 {hdr_vals}，預期 {cols}')
        # 同一次採樣內軸號必須遞增
        rows = [a for _, a, _ in p.axis_rows()]
        n = len(axes)
        for i in range(0, len(rows) - n + 1, n):
            self.assertEqual(axes, rows[i:i + n], f'第 {i // n} 次採樣的軸順序錯誤')


_warned = set()
def _warn_once(msg):
    if msg not in _warned:
        _warned.add(msg)
        print(f'\n  [WARN] {msg}')


def usable_axes(n=None):
    """可用的軸號（不超過機台軸數與 LOG_MAX_AXES）"""
    m = min(Cfg.AXES, LOG_MAX_AXES)
    return list(range(m if n is None else min(n, m)))


def expected_samples(ms, period):
    ticks = ms * Cfg.RT_FREQ // 1000
    return max(ticks // max(period, 1), 1)


# =============================================================================
# 1. 參數邊界
# =============================================================================
class TestBoundary(DataLogTestBase):

    def test_channel_range(self):
        src = make_axis_source([0])
        for ch in (0, MAX_LOG_CHANNELS - 1):
            self.ok(dl.set_log(ch, src, 0), f'SetLog ch{ch}')
            err, _ = dl.status(ch)
            self.ok(err, f'GetStatus ch{ch}')
        for ch in (MAX_LOG_CHANNELS, MAX_LOG_CHANNELS + 1, 0xFFFFFFFF):
            self.err_is(dl.set_log(ch, src, 0), E_PARAM, f'SetLog ch{ch}')
            self.err_is(dl.set_option(ch, make_option()), E_PARAM, f'SetLogOption ch{ch}')
            self.err_is(dl.start(ch), E_PARAM, f'StartLog ch{ch}')
            self.err_is(dl.stop(ch), E_PARAM, f'StopLog ch{ch}')
            self.err_is(dl.reset(ch), E_PARAM, f'ResetLog ch{ch}')
            err, _ = dl.status(ch)
            self.err_is(err, E_PARAM, f'GetStatus ch{ch}')

    def test_datasource_index_range(self):
        src = make_axis_source([0])
        for idx in range(MAX_DATASOURCES):
            self.ok(dl.set_log(0, src, idx), f'SetLog idx{idx}')
        for idx in (MAX_DATASOURCES, MAX_DATASOURCES + 1, 0xFFFF):
            self.err_is(dl.set_log(0, src, idx), E_DS_LIMIT, f'SetLog idx{idx}')

    def test_selection_count_range(self):
        self.ok(dl.set_log(0, make_axis_source([]), 0), 'count=0')
        self.ok(dl.set_log(0, make_axis_source([0] * MAX_SELECTIONS), 0), f'count={MAX_SELECTIONS}')
        bad = make_axis_source([0] * MAX_SELECTIONS, count=MAX_SELECTIONS + 1)
        self.err_is(dl.set_log(0, bad, 0), E_PARAM, f'count={MAX_SELECTIONS + 1}')
        bad = make_axis_source([0], count=0xFFFFFFFF)
        self.err_is(dl.set_log(0, bad, 0), E_PARAM, 'count=0xFFFFFFFF')

    def test_axis_id_range(self):
        self.ok(dl.set_log(0, make_axis_source([0]), 0), '軸 0')
        self.ok(dl.set_log(0, make_axis_source([LOG_MAX_AXES - 1]), 0), f'軸 {LOG_MAX_AXES - 1}')
        for a in (LOG_MAX_AXES, LOG_MAX_AXES + 1, 0xFFFFFFFF):
            self.err_is(dl.set_log(0, make_axis_source([a]), 0), E_PARAM, f'軸 {a}')
        # 只要清單中有一個非法軸號就整組拒絕，且原設定不變
        self.ok(dl.set_log(0, make_axis_source([1, 2]), 0), '合法設定')
        self.err_is(dl.set_log(0, make_axis_source([1, LOG_MAX_AXES]), 0), E_PARAM, '混合非法軸號')
        err, got = dl.get_log(0, 0)
        self.ok(err, 'GetLog')
        self.assertEqual((2, 1, 2), (got.count, got.selection[0], got.selection[1]), '失敗的 SetLog 不應改變原設定')

    def test_null_pointer(self):
        self.err_not_ok(dl.set_log(0, None, 0), 'SetLog source=NULL')
        self.err_not_ok(dl.set_option(0, None), 'SetLogOption options=NULL')

    def test_set_get_roundtrip(self):
        src = make_axis_source([3, 0, 127 if Cfg.AXES >= 128 else 1], 1, 0, 1, 0)
        self.ok(dl.set_log(2, src, 3), 'SetLog')
        err, got = dl.get_log(2, 3)
        self.ok(err, 'GetLog')
        self.assertEqual(src.count, got.count)
        self.assertEqual(list(src.selection[:src.count]), list(got.selection[:got.count]))
        self.assertEqual((1, 0, 1, 0), (got.items.smItems.cmd_pos, got.items.smItems.act_pos,
                                        got.items.smItems.cmd_vel, got.items.smItems.act_vel))

    def test_option_sampling_time(self):
        self.ok(dl.set_option(0, make_option(ms=0)), 'samplingTime=0（不限時間）')
        self.ok(dl.set_option(0, make_option(ms=1)), 'samplingTime=1')
        self.ok(dl.set_option(0, make_option(ms=0x7FFFFFFF)), 'samplingTime=INT_MAX')
        self.err_is(dl.set_option(0, make_option(ms=-1)), E_PARAM, 'samplingTime=-1')

    def test_option_period_zero_default(self):
        self.ok(dl.set_option(0, make_option(period=0)), 'period=0')
        err, opt = dl.get_option(0)
        self.ok(err, 'GetLogOption')
        self.assertGreaterEqual(opt.samplingPeriodInCycles, 1, 'period=0 應被設為預設值')
        self.ok(dl.set_option(0, make_option(period=0xFFFFFFFF)), 'period=0xFFFFFFFF')

    def test_option_rotate(self):
        self.err_is(dl.set_option(0, make_option(rotate=True, file_cnt=1, file_size=4096)), E_PARAM,
                    '輪替且 maxLogFileCount=1')
        self.err_is(dl.set_option(0, make_option(rotate=True, file_cnt=0, file_size=4096)), E_PARAM,
                    '輪替且 maxLogFileCount=0')
        self.ok(dl.set_option(0, make_option(rotate=True, file_cnt=2, file_size=4096)), '輪替 2 個檔案')
        self.err_is(dl.set_option(0, make_option(rotate=False, file_size=4096)), E_PARAM,
                    '未輪替但 maxLogFileSize>0')
        self.ok(dl.set_option(0, make_option(rotate=False, file_cnt=5)), '未輪替 maxLogFileCount=5')
        err, opt = dl.get_option(0)
        self.ok(err, 'GetLogOption')
        self.assertEqual(1, opt.maxLogFileCount, '未輪替時 maxLogFileCount 應固定為 1')

    def test_option_delimiter_zero(self):
        self.ok(dl.set_option(0, make_option(delimiter=b'\0')), 'delimiter=0')
        err, opt = dl.get_option(0)
        self.ok(err, 'GetLogOption')
        self.assertEqual(b' ', opt.delimiter, 'delimiter=0 應改為空白')

    def test_path_and_header(self):
        self.ok(dl.set_path(0, b'/tmp', b'abc'), 'SetLogFilePath')
        err, d, f = dl.get_path(0)
        self.ok(err, 'GetLogFilePath')
        self.assertEqual((b'/tmp', b'abc.txt'), (d, f), '檔名應自動加上 .txt')
        long_dir = b'/tmp/' + b'd' * 250            # 255 字元
        self.ok(dl.set_path(0, long_dir, b'x'), '255 字元目錄')
        err, d, _ = dl.get_path(0)
        self.ok(err, 'GetLogFilePath')
        self.assertEqual(long_dir, d)
        too_long = b'/tmp/' + b'd' * 400
        err = dl.set_path(0, too_long, b'x')
        if err == SUCCESS:
            _, d, _ = dl.get_path(0)
            self.assertLess(len(d), MAX_PATH, '過長路徑必須被截斷或拒絕，不可溢位')
        hdr = b'H' * 255
        self.ok(dl.set_header(0, hdr), '255 字元標頭')
        err, got = dl.get_header(0)
        self.ok(err, 'GetLogHeader')
        self.assertEqual(hdr, got)
        err = dl.set_header(0, b'H' * 400)
        if err == SUCCESS:
            _, got = dl.get_header(0)
            self.assertLess(len(got), MAX_PATH, '過長標頭必須被截斷或拒絕，不可溢位')

    def test_get_file_errors(self):
        err, _ = dl.get_file(b'/tmp/__file_not_exist__.txt')
        self.err_not_ok(err, '讀取不存在的檔案')


# =============================================================================
# 2. 狀態機
# =============================================================================
class TestStateMachine(DataLogTestBase):

    def start_running(self, ch=0):
        self.configure(ch, [(0, make_axis_source([0]))], make_option(ms=0, period=10))
        self.ok(dl.start(ch), 'StartLog')
        st = self.wait_state(ch, (ST_RUNNING,), 1.0)
        self.assertEqual(ST_RUNNING, st.state, f'StartLog 後狀態為 {state_name(st.state)}')

    def test_initial_idle(self):
        for ch in range(MAX_LOG_CHANNELS):
            err, st = dl.status(ch)
            self.ok(err, 'GetStatus')
            self.assertEqual(ST_IDLE, st.state, f'ch{ch} Reset 後應為 IDLE')

    def test_api_rejected_while_running(self):
        self.start_running()
        self.err_is(dl.set_log(0, make_axis_source([1]), 0), E_STATE, 'RUNNING 時 SetLog')
        self.err_is(dl.set_path(0, b'/tmp', b'x'), E_STATE, 'RUNNING 時 SetLogFilePath')
        self.err_is(dl.set_header(0, b'x'), E_STATE, 'RUNNING 時 SetLogHeader')
        self.err_is(dl.set_option(0, make_option()), E_STATE, 'RUNNING 時 SetLogOption')
        self.err_is(dl.start(0), E_STATE, 'RUNNING 時再次 StartLog')
        self.err_is(dl.reset(0), E_STATE, 'RUNNING 時 ResetLog')
        err, _ = dl.status(0)
        self.ok(err, 'RUNNING 時 GetStatus')
        err, _ = dl.get_log(0, 0)
        self.ok(err, 'RUNNING 時 GetLog')
        st = self.finish(0)
        self.assertEqual(ST_FINISHED, st.state)

    def test_stop_when_idle(self):
        self.ok(dl.stop(0), 'IDLE 時 StopLog 應直接成功')
        err, st = dl.status(0)
        self.assertEqual(ST_IDLE, st.state)

    def test_restart_after_finished(self):
        path = self.configure(0, [(0, make_axis_source([0]))], make_option(ms=200, period=1))
        self.run_timed([0], 200)
        # FINISHED 後可直接修改設定並再次啟動
        self.ok(dl.set_log(0, make_axis_source([1]), 0), 'FINISHED 後 SetLog')
        self.run_timed([0], 200)
        p = self.download(path)
        self.check_content(p, [1], expected_samples(200, 1))

    def test_auto_stop_and_stop(self):
        self.configure(0, [(0, make_axis_source([0]))], make_option(ms=300, period=1))
        self.ok(dl.start(0), 'StartLog')
        st = self.wait_state(0, DONE_STATES, 3.0)
        self.assertEqual(ST_STOP, st.state, f'時間到應自動進入 STOP，實際 {state_name(st.state)}')
        self.assertEqual(st.samplesToCollect, st.samplesCollected)
        st = self.finish(0)
        self.assertEqual(ST_FINISHED, st.state,
                         f'STOP 狀態下 StopLog 後應為 FINISHED，實際 {state_name(st.state)}'
                         '（DLL StopLog 需處理 LOG_STATE_STOP）')

    def test_wait_for_trigger_then_stop(self):
        path = self.configure(0, [(0, make_axis_source([0]))], make_option(ms=0, period=1, trig_event=1, event_id=10))
        self.ok(dl.start(0), 'StartLog（事件觸發）')
        time.sleep(0.5)
        err, st = dl.status(0)
        self.assertEqual(ST_WAIT, st.state, f'應為 WAITING_FOR_TRIGGER，實際 {state_name(st.state)}')
        self.assertEqual(0, st.samplesCollected, '未觸發前不應收集資料')
        self.ok(dl.set_option(0, make_option(ms=0, period=2, trig_event=1, event_id=10)),
                'WAITING_FOR_TRIGGER 時允許 SetLogOption')
        st = self.finish(0)
        self.assertEqual(ST_FINISHED, st.state,
                         f'WAITING 狀態下 StopLog 後應為 FINISHED，實際 {state_name(st.state)}')
        p = self.download(path)
        self.assertEqual(0, len(p.rows), '未觸發的記錄檔不應有資料行')

    def test_reset_clears_settings(self):
        self.configure(1, [(0, make_axis_source([5]))], make_option(ms=123, period=7), header=b'hdr')
        self.ok(dl.reset(1), 'ResetLog')
        err, src = dl.get_log(1, 0)
        self.assertEqual(0, src.count, 'Reset 後資料源應清除')
        err, opt = dl.get_option(1)
        self.assertEqual(0, opt.samplingTimeMilliseconds)
        err, h = dl.get_header(1)
        self.assertEqual(b'', h)

    def test_start_without_selection(self):
        path = self.configure(0, [], make_option(ms=200, period=1))
        self.ok(dl.start(0), '未選任何軸也允許 StartLog')
        time.sleep(0.4)
        self.finish(0)
        p = self.download(path)
        self.assertIsNotNone(p.axis_header, '仍應輸出欄位標頭')
        self.assertEqual(0, len(p.rows))


# =============================================================================
# 3. 單通道
# =============================================================================
class TestSingleChannel(DataLogTestBase):

    def test_single_axis_all_items(self):
        path = self.configure(0, [(0, make_axis_source([0], 1, 1, 1, 1))], make_option(ms=500, period=1))
        self.run_timed([0], 500)
        p = self.download(path)
        self.assertEqual(['EventType', 'SourceID', 'CmdPos', 'ActPos', 'CmdVel', 'ActVel'], p.axis_header)
        self.check_content(p, [0], expected_samples(500, 1), cols=4)

    def test_item_combinations(self):
        combos = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 1, 0), (0, 0, 0, 0)]
        for i, c in enumerate(combos):
            with self.subTest(items=c):
                self.reset_all()
                path = self.configure(0, [(0, make_axis_source([0], *c))], make_option(ms=100, period=1),
                                      name=self.remote_name(0, f'c{i}'))
                self.run_timed([0], 100)
                p = self.download(path)
                self.check_content(p, [0], expected_samples(100, 1), cols=sum(c))

    def test_multi_axes(self):
        for n in (2, 8, 16, 32, 64):
            axes = usable_axes(n)
            if len(axes) < n:
                continue
            with self.subTest(axes=n):
                self.reset_all()
                path = self.configure(0, [(0, make_axis_source(axes))], make_option(ms=300, period=2),
                                      name=self.remote_name(0, f'n{n}'))
                res = self.run_timed([0], 300)
                self.assertEqual(expected_samples(300, 2) * n, res[0].samplesToCollect, 'samplesToCollect 應乘上軸數')
                p = self.download(path)
                self.check_content(p, axes, expected_samples(300, 2))

    def test_non_contiguous_axes(self):
        axes = [a for a in (0, 3, 31, 32, 63, 64, 100, 127) if a < min(Cfg.AXES, LOG_MAX_AXES)]
        path = self.configure(0, [(0, make_axis_source(list(reversed(axes))))], make_option(ms=200, period=1))
        self.run_timed([0], 200)
        p = self.download(path)
        self.check_content(p, axes, expected_samples(200, 1))     # 輸出依軸號遞增，與設定順序無關

    def test_duplicate_axes_recorded_once(self):
        src0 = make_axis_source([1, 1, 2, 1])
        src1 = make_axis_source([2, 3])
        path = self.configure(0, [(0, src0), (1, src1)], make_option(ms=200, period=1))
        res = self.run_timed([0], 200)
        p = self.download(path)
        self.check_content(p, [1, 2, 3], expected_samples(200, 1))
        self.assertEqual(expected_samples(200, 1) * 3, res[0].samplesToCollect)

    def test_disabled_datasource_ignored(self):
        path = self.configure(0, [(0, make_axis_source([0])), (1, make_none_source()), (2, make_axis_source([1]))],
                              make_option(ms=200, period=1))
        self.run_timed([0], 200)
        p = self.download(path)
        self.check_content(p, [0, 1], expected_samples(200, 1))

    def test_sampling_period(self):
        for period in (1, 2, 5, 10, 100):
            with self.subTest(period=period):
                self.reset_all()
                path = self.configure(0, [(0, make_axis_source([0]))], make_option(ms=1000, period=period),
                                      name=self.remote_name(0, f'p{period}'))
                self.run_timed([0], 1000)
                p = self.download(path)
                self.check_content(p, [0], expected_samples(1000, period))

    def test_period_longer_than_time(self):
        path = self.configure(0, [(0, make_axis_source([0]))], make_option(ms=10, period=100))
        self.run_timed([0], 100)
        p = self.download(path)
        self.check_content(p, [0], 1)       # 至少記一筆

    def test_axis_beyond_machine_ignored(self):
        if Cfg.AXES >= LOG_MAX_AXES:
            self.skipTest('機台軸數 >= LOG_MAX_AXES，無超出範圍的軸可測')
        path = self.configure(0, [(0, make_axis_source([0, Cfg.AXES, LOG_MAX_AXES - 1]))], make_option(ms=200))
        self.run_timed([0], 200)
        p = self.download(path)
        self.assertEqual([0], sorted(p.count_by_axis()), '超出機台軸數的軸應被忽略')

    def test_unlimited_time_manual_stop(self):
        path = self.configure(0, [(0, make_axis_source(usable_axes(4)))], make_option(ms=0, period=5))
        self.ok(dl.start(0), 'StartLog')
        time.sleep(1.0)
        err, st = dl.status(0)
        self.assertEqual(ST_RUNNING, st.state, '不限時間應持續 RUNNING')
        st = self.finish(0)
        self.assertEqual(ST_FINISHED, st.state)
        p = self.download(path)
        self.check_content(p, usable_axes(4))
        n = p.count_by_axis()[0]
        self.assertGreater(n, 0)
        self.log(f'1 秒記錄 {n} 筆（period=5）')

    def test_single_channel_max_axes(self):
        axes = usable_axes()
        sources = [(i, make_axis_source(part)) for i, part in enumerate(chunks(axes, MAX_SELECTIONS))]
        self.assertLessEqual(len(sources), MAX_DATASOURCES)
        path = self.configure(0, sources, make_option(ms=500, period=5))
        res = self.run_timed([0], 500)
        self.assertEqual(expected_samples(500, 5) * len(axes), res[0].samplesToCollect)
        p = self.download(path)
        self.check_content(p, axes, expected_samples(500, 5))

    def test_single_channel_max_selections(self):
        """4 組資料源各 64 個編號（共 256 個，含重複）"""
        axes = usable_axes()
        sel = (axes * ((MAX_SELECTIONS * MAX_DATASOURCES) // len(axes) + 1))[:MAX_SELECTIONS * MAX_DATASOURCES]
        sources = [(i, make_axis_source(part)) for i, part in enumerate(chunks(sel, MAX_SELECTIONS))]
        path = self.configure(0, sources, make_option(ms=300, period=10))
        self.run_timed([0], 300)
        p = self.download(path)
        self.check_content(p, axes, expected_samples(300, 10))


# =============================================================================
# 4. 多通道
# =============================================================================
class TestMultiChannel(DataLogTestBase):

    def test_multi_channel_multi_axes(self):
        axes = usable_axes()
        plan = {0: axes[0:4], 1: axes[4:12], 2: axes[0:16], 3: axes[-8:]}
        paths = {}
        for ch, ax in plan.items():
            paths[ch] = self.configure(ch, [(0, make_axis_source(ax))], make_option(ms=500, period=2))
        self.run_timed(list(plan), 500)
        for ch, ax in plan.items():
            with self.subTest(ch=ch):
                p = self.download(paths[ch])
                self.check_content(p, ax, expected_samples(500, 2))

    def test_multi_channel_different_periods(self):
        periods = {0: 1, 1: 3, 2: 7, 3: 20}
        paths = {ch: self.configure(ch, [(0, make_axis_source(usable_axes(4)))], make_option(ms=600, period=pd))
                 for ch, pd in periods.items()}
        self.run_timed(list(periods), 600)
        for ch, pd in periods.items():
            with self.subTest(ch=ch, period=pd):
                p = self.download(paths[ch])
                self.check_content(p, usable_axes(4), expected_samples(600, pd))

    def test_multi_channel_different_durations(self):
        dur = {0: 200, 1: 500, 2: 1000, 3: 1500}
        paths = {ch: self.configure(ch, [(0, make_axis_source([ch % len(usable_axes())]))], make_option(ms=ms))
                 for ch, ms in dur.items()}
        self.run_timed(list(dur), max(dur.values()))
        for ch, ms in dur.items():
            with self.subTest(ch=ch, ms=ms):
                p = self.download(paths[ch])
                self.check_content(p, [ch % len(usable_axes())], expected_samples(ms, 1))

    def test_same_axes_on_all_channels(self):
        axes = usable_axes(8)
        paths = {ch: self.configure(ch, [(0, make_axis_source(axes, 1, ch % 2, 0, 0))], make_option(ms=400, period=2))
                 for ch in range(MAX_LOG_CHANNELS)}
        self.run_timed(list(range(MAX_LOG_CHANNELS)), 400)
        for ch in range(MAX_LOG_CHANNELS):
            with self.subTest(ch=ch):
                p = self.download(paths[ch])
                self.check_content(p, axes, expected_samples(400, 2), cols=1 + ch % 2)

    def test_multi_channel_max_axes(self):
        axes = usable_axes()
        paths = {}
        for ch in range(MAX_LOG_CHANNELS):
            sources = [(i, make_axis_source(part)) for i, part in enumerate(chunks(axes, MAX_SELECTIONS))]
            paths[ch] = self.configure(ch, sources, make_option(ms=500, period=10))
        self.run_timed(list(range(MAX_LOG_CHANNELS)), 500)
        for ch in range(MAX_LOG_CHANNELS):
            with self.subTest(ch=ch):
                p = self.download(paths[ch])
                self.check_content(p, axes, expected_samples(500, 10))

    def test_stop_one_channel_others_continue(self):
        paths = {ch: self.configure(ch, [(0, make_axis_source([ch]))], make_option(ms=0, period=5))
                 for ch in range(MAX_LOG_CHANNELS)}
        for ch in range(MAX_LOG_CHANNELS):
            self.ok(dl.start(ch), f'StartLog ch{ch}')
        time.sleep(0.5)
        st = self.finish(1, timeout=5.0)
        self.assertEqual(ST_FINISHED, st.state, f'ch1 StopLog 後為 {state_name(st.state)}（可能 join 到其他通道的 writer）')
        err, st0 = dl.status(0)
        before = st0.samplesCollected
        time.sleep(0.5)
        err, st0 = dl.status(0)
        self.assertEqual(ST_RUNNING, st0.state, '停止 ch1 不應影響 ch0')
        self.assertGreater(st0.samplesCollected, before, 'ch0 應持續收集')
        for ch in (0, 2, 3):
            self.assertEqual(ST_FINISHED, self.finish(ch).state)
        for ch in range(MAX_LOG_CHANNELS):
            with self.subTest(ch=ch):
                self.check_content(self.download(paths[ch]), [ch])

    def test_start_channels_staggered(self):
        paths = {ch: self.configure(ch, [(0, make_axis_source([0]))], make_option(ms=400, period=1))
                 for ch in range(MAX_LOG_CHANNELS)}
        for ch in range(MAX_LOG_CHANNELS):
            self.ok(dl.start(ch), f'StartLog ch{ch}')
            time.sleep(0.1)
        for ch in range(MAX_LOG_CHANNELS):
            self.assertIn(self.wait_state(ch, DONE_STATES, 3.0).state, DONE_STATES)
            self.assertEqual(ST_FINISHED, self.finish(ch).state)
        for ch in range(MAX_LOG_CHANNELS):
            with self.subTest(ch=ch):
                self.check_content(self.download(paths[ch]), [0], expected_samples(400, 1))


# =============================================================================
# 5. 檔案功能
# =============================================================================
class TestFileFeatures(DataLogTestBase):

    def test_custom_header(self):
        hdr = b'PyTest custom header 123'
        path = self.configure(0, [(0, make_axis_source([0]))], make_option(ms=100), header=hdr)
        self.run_timed([0], 100)
        p = self.download(path, custom_header=hdr)
        self.assertEqual(hdr.decode(), p.custom_header)
        self.check_content(p, [0], expected_samples(100, 1))

    def test_delimiter(self):
        for d in (b',', b'\t', b';'):
            with self.subTest(delimiter=d):
                self.reset_all()
                path = self.configure(0, [(0, make_axis_source([0, 1][:len(usable_axes())], 1, 1))],
                                      make_option(ms=100, delimiter=d), name=self.remote_name(0, f'd{ord(d)}'))
                self.run_timed([0], 100)
                p = self.download(path, delimiter=d.decode())
                self.assertEqual(['EventType', 'SourceID', 'CmdPos', 'ActPos'], p.axis_header)
                self.check_content(p, usable_axes(2), expected_samples(100, 1))

    def test_rotate_files(self):
        file_cnt, file_size = 3, 8 * 1024
        name = self.remote_name(0, 'rot')
        self.configure(0, [(0, make_axis_source(usable_axes(4), 1, 1, 1, 1))],
                       make_option(ms=2000, period=1, rotate=True, file_cnt=file_cnt, file_size=file_size), name=name)
        self.run_timed([0], 2000)
        err, names, _, cnt = dl.rotated_paths(0)
        self.ok(err, 'GetRotatedLogFilePaths')
        self.assertEqual(file_cnt, cnt)
        expect = [Cfg.REMOTE_DIR + b'/' + name + f'_{i}.txt'.encode() for i in range(file_cnt)]
        self.assertEqual(expect, names)
        total = 0
        for n in names:
            err, raw = dl.get_file(n)
            self.ok(err, f'GetLogFile {n}')
            self.assertLessEqual(len(raw), file_size + 256, f'{n} 大小 {len(raw)} 超過上限 {file_size}')
            p = ParsedLog(raw)
            self.assertIsNotNone(p.axis_header, f'{n} 缺少欄位標頭')
            total += len(p.rows)
            with open(os.path.join(Cfg.OUT_DIR, os.path.basename(n.decode())), 'wb') as f:
                f.write(raw)
        self.assertGreater(total, 0)

    def test_rotated_paths_buffer_too_small(self):
        self.configure(0, [(0, make_axis_source([0]))], make_option(rotate=True, file_cnt=4, file_size=4096))
        err, _, need, _ = dl.rotated_paths(0, buf_size=8)
        self.err_is(err, E_BUF_SMALL, 'GetRotatedLogFilePaths 緩衝區不足')
        self.assertGreater(need, 8, '應回傳所需大小')
        err, names, _, cnt = dl.rotated_paths(0, buf_size=need)
        self.ok(err, '以回傳的大小重試')
        self.assertEqual(4, cnt)

    def test_rotated_paths_not_rotate(self):
        name = self.remote_name(0, 'single')
        self.configure(0, [(0, make_axis_source([0]))], make_option(), name=name)
        err, names, _, cnt = dl.rotated_paths(0)
        self.ok(err, 'GetRotatedLogFilePaths')
        self.assertEqual([Cfg.REMOTE_DIR + b'/' + name + b'.txt'], names)

    def test_get_file_buffer_size(self):
        path = self.configure(0, [(0, make_axis_source([0]))], make_option(ms=300))
        self.run_timed([0], 300)
        if E_MEM is None:
            self.skipTest('ErrorCode2 沒有 MemAllocateFailed')
        err, _, size = dl.get_file_raw(path, 1)
        self.err_is(err, E_MEM, '緩衝區 1 byte')
        self.assertGreater(size, 1, '應回傳檔案大小')
        err, buf, got = dl.get_file_raw(path, size)
        self.ok(err, '剛好等於檔案大小')
        self.assertEqual(size, got)
        err, buf, got = dl.get_file_raw(path, size + 4096)
        self.ok(err, '大於檔案大小')
        self.assertEqual(size, got)

    def test_get_file_large(self):
        """跨多個 4 KB 區塊、且大小不是 4 KB 倍數的檔案"""
        path = self.configure(0, [(0, make_axis_source(usable_axes(8), 1, 1, 1, 1))], make_option(ms=1500, period=1))
        self.run_timed([0], 1500)
        err, raw = dl.get_file(path)
        self.ok(err, 'GetLogFile')
        self.assertGreater(len(raw), 4096 * 3, '測試檔案應跨多個區塊')
        p = ParsedLog(raw)
        self.assertEqual([], p.bad_lines[:5], '跨區塊傳輸後資料行不應損壞')
        self.check_content(p, usable_axes(8), expected_samples(1500, 1))


# =============================================================================
# 6. 壓力測試（--stress）
# =============================================================================
@unittest.skipUnless(Cfg.STRESS or '--stress' in sys.argv, '加上 --stress 才執行')
class TestStress(DataLogTestBase):

    def test_overflow_policy_continue(self):
        """4 通道最大軸數、每 cycle 採樣，不因溢位停止：檢查狀態與資料一致性"""
        axes = usable_axes()
        paths = {}
        for ch in range(MAX_LOG_CHANNELS):
            sources = [(i, make_axis_source(part, 1, 1, 1, 1)) for i, part in enumerate(chunks(axes, MAX_SELECTIONS))]
            paths[ch] = self.configure(ch, sources, make_option(ms=3000, period=1, stop_on_overflow=0))
        for ch in range(MAX_LOG_CHANNELS):
            self.ok(dl.start(ch), f'StartLog ch{ch}')
        for ch in range(MAX_LOG_CHANNELS):
            self.wait_state(ch, DONE_STATES, 15.0)
        for ch in range(MAX_LOG_CHANNELS):
            st = self.finish(ch, timeout=30.0)
            print(f'    ch{ch}: state={state_name(st.state)} collected={st.samplesCollected} '
                  f'written={st.samplesWritten} toCollect={st.samplesToCollect}')
            self.assertEqual(st.samplesCollected, st.samplesWritten)
            p = self.download(paths[ch])
            self.assertEqual(st.samplesWritten, len(p.rows), f'ch{ch} 檔案行數與 samplesWritten 不符')

    def test_overflow_policy_stop(self):
        axes = usable_axes()
        sources = [(i, make_axis_source(part, 1, 1, 1, 1)) for i, part in enumerate(chunks(axes, MAX_SELECTIONS))]
        self.configure(0, sources, make_option(ms=0, period=1, stop_on_overflow=1))
        self.ok(dl.start(0), 'StartLog')
        st = self.wait_state(0, (ST_OVERFLOW,), 10.0)
        print(f'    state={state_name(st.state)} collected={st.samplesCollected}')
        st = self.finish(0, timeout=30.0)
        self.assertIn(st.state, (ST_FINISHED, ST_OVERFLOW))

    def test_repeat_start_stop(self):
        path = self.configure(0, [(0, make_axis_source(usable_axes(4)))], make_option(ms=50, period=1))
        for i in range(50):
            self.run_timed([0], 50)
        self.check_content(self.download(path), usable_axes(4), expected_samples(50, 1))


# =============================================================================
# 主程式
# =============================================================================
def main():
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument('--dev', type=int, default=Cfg.DEV_ID)
    ap.add_argument('--axes', type=int, default=Cfg.AXES, help='機台實際軸數')
    ap.add_argument('--rt-freq', type=int, default=Cfg.RT_FREQ, help='RT 每秒 cycle 數')
    ap.add_argument('--dir', default=Cfg.REMOTE_DIR.decode(), help='RT 端記錄檔目錄')
    ap.add_argument('--out', default=Cfg.OUT_DIR, help='下載記錄檔的本機目錄')
    ap.add_argument('--stress', action='store_true')
    args, rest = ap.parse_known_args()
    Cfg.DEV_ID, Cfg.AXES, Cfg.RT_FREQ = args.dev, args.axes, args.rt_freq
    Cfg.REMOTE_DIR, Cfg.OUT_DIR, Cfg.STRESS = args.dir.encode(), args.out, args.stress
    Cfg.VERBOSE = '-v' in rest or '--verbose' in rest
    print(f'Data Log 測試：dev={Cfg.DEV_ID} axes={Cfg.AXES} rt_freq={Cfg.RT_FREQ} '
          f'dir={Cfg.REMOTE_DIR.decode()} out={Cfg.OUT_DIR} stress={Cfg.STRESS}')
    unittest.main(argv=[sys.argv[0]] + rest, verbosity=2)


if __name__ == '__main__':
    main()