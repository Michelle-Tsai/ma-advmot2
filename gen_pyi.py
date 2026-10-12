"""從 ctypes 定義檔產生 Pylance 用的 .pyi stub。

用法:
    python gen_pyi.py AcmP/AdvMotApi_CM2.py            # 輸出到 AcmP/AdvMotApi_CM2.pyi
    python gen_pyi.py AcmP/AdvMotApi_CM2.py -o out.pyi

會實際 import 該檔以取得 ctypes 的 offset / sizeof，所以 .py 必須能正常 import。
offset 與 sizeof 依執行此腳本的 Python 平台計算（請用 64-bit Python）。
"""
import sys, ctypes, ast, argparse, importlib.util, os
from ctypes import *

ap = argparse.ArgumentParser()
ap.add_argument("src")
ap.add_argument("-o", "--out")
args = ap.parse_args()
SRC = os.path.abspath(args.src)
OUT = args.out or os.path.splitext(SRC)[0] + ".pyi"
spec = importlib.util.spec_from_file_location("_stub_src", SRC)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

SCALAR = {c_uint8:'int',c_int8:'int',c_uint16:'int',c_int16:'int',c_uint32:'int',c_int32:'int',
          c_uint64:'int',c_int64:'int',c_long:'int',c_ulong:'int',c_bool:'bool',
          c_float:'float',c_double:'float',c_char:'bytes'}
CNAME = {}
for n in ['c_uint8','c_int8','c_uint16','c_int16','c_uint32','c_int32','c_uint64','c_int64',
          'c_float','c_double','c_char','c_bool','c_long','c_ulong']:
    CNAME.setdefault(getattr(ctypes,n), n)

USED_CT = set()      # ctypes names referenced in annotations
EXTERNAL = {}        # struct types from other modules: name -> module

def cname(t):
    if t in CNAME: USED_CT.add(CNAME[t]); return CNAME[t]
    if issubclass(t, Array): return f'Array[{cname(t._type_)}]'
    if issubclass(t, ctypes._Pointer): return f'_CPtr[{elem_type(t._type_)}]'
    if t in (c_void_p, c_char_p): USED_CT.add(t.__name__); return t.__name__
    if getattr(t, '__module__', None) not in (m.__name__, 'ctypes', '_ctypes'):
        EXTERNAL[t.__name__] = t.__module__
    return t.__name__

def get_type(t):
    """type pylance shows on attribute read"""
    if t in SCALAR: return SCALAR[t]
    if issubclass(t, Array):
        if t._type_ is c_char: return 'bytes'      # c_char*N reads as bytes
        return f'_CArray[{elem_type(t._type_)}]'
    return cname(t)

def elem_type(t):
    """type of arr[i]: nested c_char arrays come back as array objects, not bytes"""
    if issubclass(t, Array) and t._type_ is c_char: return '_CCharArray'
    return get_type(t)

def set_type(t):
    g = get_type(t)
    if g.startswith('_CPtr['):
        USED_CT.add('_Pointer')
        return f'{g} | _Pointer[Any] | None'   # 可直接指定 POINTER(...)/cast(...) 的結果
    if g.startswith('_CArray['):
        e=g[8:-1]
        return f"{g} | tuple[{'bytes' if e=='_CCharArray' else e}, ...]"
    return g

def cdesc(t):
    if issubclass(t, ctypes._Pointer): return f'POINTER({cdesc(t._type_)})'
    if issubclass(t, Array):
        dims=[]; x=t
        while issubclass(x, Array): dims.append(x._length_); x=x._type_
        return cname(x)+''.join(f'[{d}]' for d in dims)
    return cname(t)

# preserve source order & docstring comments
src = open(SRC, encoding='utf-8').read()
tree = ast.parse(src)
order = [n.name for n in tree.body if isinstance(n, ast.ClassDef)]

out = [f'"""Type stub for {os.path.splitext(os.path.basename(SRC))[0]} (ctypes structures)。',
       '',
       f'由 {os.path.basename(SRC)} 以 gen_pyi.py 自動產生，供 VS Code Pylance 自動完成與型別檢查使用。',
       '欄位後的註解為 C 端 ctypes 型別、offset 與大小（x64）。',
       '"""',
       '',
       'from collections.abc import Callable, Iterator',
       'from ctypes import Structure, Union, _CFuncPtr',
       '@@EXTRA_IMPORTS@@',
       'from typing import Any, Final, Generic, TypeVar, overload',
       '',
       '_T = TypeVar("_T")',
       '',
       'class _CArray(Generic[_T]):',
       '    """stub 專用：代表 ctypes 定長陣列 (c_xxx * N)，讓索引結果有正確型別。執行期是 ctypes.Array。"""',
       '    _length_: int',
       '    def __len__(self) -> int: ...',
       '    @overload',
       '    def __getitem__(self, index: int, /) -> _T: ...',
       '    @overload',
       '    def __getitem__(self, index: slice, /) -> list[_T]: ...',
       '    def __setitem__(self, index: int, value: _T, /) -> None: ...',
       '    def __iter__(self) -> Iterator[_T]: ...',
       '',
       'class _CPtr(Generic[_T]):',
       '    """stub 專用：代表 POINTER(c_xxx)。p[i] / p.contents 有正確型別。執行期是 ctypes._Pointer。"""',
       '    contents: object',
       '    def __getitem__(self, index: int, /) -> _T: ...',
       '    def __setitem__(self, index: int, value: _T, /) -> None: ...',
       '    def __bool__(self) -> bool: ...',
       '',
       'class _CCharArray:',
       '    """stub 專用：代表 c_char * N 陣列物件（巢狀陣列的元素）。"""',
       '    value: bytes',
       '    raw: bytes',
       '    def __len__(self) -> int: ...',
       '',
       '# callback: U32 (*)(U32 EvtValue, void* UserParameter)',
       'class CALLBACK_FUNC(_CFuncPtr):',
       '    def __init__(self, callable: Callable[[int, int | None], int], /) -> None: ...',
       '    def __call__(self, EvtValue: int, UserParameter: int | None, /) -> int: ...',
       '',
       'class ADV_USER_CALLBACK_FUNC(_CFuncPtr):',
       '    def __init__(self, callable: Callable[[int, int | None], int], /) -> None: ...',
       '    def __call__(self, EvtValue: int, UserParameter: int | None, /) -> int: ...',
       '',
       'def ADVUSERCALLBACKFUNC(EvtValue: int, UserParameter: int | None) -> None: ...',
       'PADV_USER_CALLBACK_FUNC: ADV_USER_CALLBACK_FUNC',
       '',
       'MAX_CONTEXT_LINES: Final[int]',
       'MAX_LINE_STR_LEN: Final[int]',
       '']

for name in order:
    cls = getattr(m, name)
    base = 'Union' if issubclass(cls, Union) else 'Structure'
    pack = getattr(cls, '_pack_', None)
    out.append(f'class {name}({base}):')
    out.append(f'    """sizeof = {sizeof(cls)} bytes' + (f', _pack_ = {pack}' if pack else '') + '"""')
    params=[]
    for fname, ft in cls._fields_:
        off = getattr(cls, fname).offset
        g = get_type(ft)
        if g.startswith('_CPtr['):
            out.append('    @property')
            out.append(f'    def {fname}(self) -> {g}:')
            out.append(f'        """{cdesc(ft)}, offset {off}, size {sizeof(ft)}"""')
            out.append(f'    @{fname}.setter')
            out.append(f'    def {fname}(self, value: {set_type(ft)}) -> None: ...')
        else:
            out.append(f'    {fname}: {g}  # {cdesc(ft)}, offset {off}, size {sizeof(ft)}')
        params.append(f'{fname}: {set_type(ft)} = ...')
    out.append('    def __init__(')
    out.append('        self,')
    for p in params: out.append(f'        {p},')
    out.append('    ) -> None: ...')
    out.append('')

extra = []
if USED_CT: extra.append('from ctypes import ' + ', '.join(sorted(USED_CT)))
for name, mod in sorted(EXTERNAL.items()):
    extra.append(f'from {mod} import {name}  # 外部模組型別，請確認 import 路徑')
out = [x for l in out for x in ([*extra] if l == '@@EXTRA_IMPORTS@@' else [l])]
open(OUT,'w',encoding='utf-8').write('\n'.join(out).rstrip()+'\n')
print(f'wrote {OUT}  ({len(order)} classes)')
