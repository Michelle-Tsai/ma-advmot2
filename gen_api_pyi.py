"""從 AdvCmnAPI_CM2.py（_bind 寫法）靜態產生 Pylance 用的 .pyi stub。

不會 import 目標檔，也不會載入 ADVMOT.dll / libadvmot.so。

用法:
    python gen_api_pyi.py AcmP/AdvCmnAPI_CM2.py
    python gen_api_pyi.py AcmP/AdvCmnAPI_CM2.py --headers path/to/include -o out.pyi

--enums：AdvMotDrv.py 路徑（選用，預設找 src 同資料夾），用來列出 enum 成員與數值。
--headers：放 C header 的資料夾（選用）。有提供時，會從 AdvMotApi.h、AdvMotApi_CM2.h、
AmcDataLog.h、AmcApiLogManager.h 抓參數名稱與 C 原型放進 docstring，並從
AdvCmnAPI_CM2.h 的 typedef 找出 Acm2_* 的 enum 參數（例如 POSITION_TYPE）；參數數量
和 argtypes 不一致時不採用名稱，並在 docstring 標註警告。
"""
import argparse, ast, os, re

ap = argparse.ArgumentParser()
ap.add_argument("src")
ap.add_argument("--headers")
ap.add_argument("-o", "--out")
ap.add_argument("--enums", help="AdvMotDrv.py 路徑（預設：與 src 同資料夾的 AdvMotDrv.py）")
args = ap.parse_args()
SRC = os.path.abspath(args.src)
OUT = args.out or os.path.splitext(SRC)[0] + ".pyi"
src = open(SRC, encoding="utf-8").read()
tree = ast.parse(src)

# ---------------- C header 原型（取參數名稱） ----------------
PROTO = {}
def _strip(s):
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.S)
    return re.sub(r"//[^\n]*", "", s)
if args.headers:
    for fn in ["AdvMotApi.h", "AdvMotApi_CM2.h", "AmcDataLog.h", "AmcApiLogManager.h"]:
        p = os.path.join(args.headers, fn)
        if not os.path.exists(p):
            continue
        s = _strip(open(p, encoding="utf-8-sig", errors="replace").read())
        for m in re.finditer(r"\b(\w+)\s+ADVCMNAPI\s+(\w+)\s*\((.*?)\)\s*;", s, flags=re.S):
            ret, name, body = m.group(1), m.group(2), " ".join(m.group(3).split())
            params = [] if body in ("", "void", "VOID") else [x.strip() for x in body.split(",")]
            names, ctys = [], []
            for x in params:
                arr = bool(re.search(r"\[\s*\w*\s*\]$", x))
                x = re.sub(r"\[\s*\w*\s*\]$", "", x).strip()
                mm = re.search(r"(\w+)\s*$", x)
                has_name = bool(mm and re.search(r"[\s\*&]", x))
                names.append(mm.group(1) if has_name else None)
                ct = x[:mm.start()].strip() if has_name else x
                ct = re.sub(r"\b(const|IN|OUT|OPTIONAL|struct)\b", "", ct)
                ct = " ".join(ct.split()).replace(" *", "*").replace("&", "*")
                ctys.append(ct + ("*" if arr else ""))
            PROTO[name] = (f"{ret} {name}({', '.join(params)})", names, ctys, ret)

# ---------------- CM2 typedef（AdvCmnAPI_CM2.h，只有型別沒有參數名稱） ----------------
CM2_TYPES = {}   # "Acm2_AxSetPosition" -> ["HAND", "POSITION_TYPE", "F64"]
if args.headers and os.path.exists(os.path.join(args.headers, "AdvCmnAPI_CM2.h")):
    s2 = _strip(open(os.path.join(args.headers, "AdvCmnAPI_CM2.h"), encoding="utf-8-sig", errors="replace").read())
    macros = {m.group(1): m.group(2) for m in re.finditer(r'#define\s+(Adv2?_\w+)\s+"(\w+)"', s2)}
    tds = {}
    for m in re.finditer(r"typedef\s+\w+\s*\(\s*(?:ADVCMNAPI\s*)?\*\s*(LP\w+)\s*\)\s*\((.*?)\)\s*;", s2, flags=re.S):
        body = " ".join(m.group(2).split())
        tds[m.group(1).lower().removesuffix("_cm2")] = [] if body in ("", "void") else [
            " ".join(re.sub(r"/\*.*?\*/", "", x).split()).replace(" *", "*") for x in body.split(",")]
    for mac, fn in macros.items():
        for key in (mac.split("_", 1)[1], fn.split("_", 1)[-1]):
            t = tds.get("lp" + key.lower())
            if t is not None:
                CM2_TYPES[fn] = t
                break

# ---------------- Python enum（AdvMotDrv.py） ----------------
ENUMS = {}       # "POSITION_TYPE" -> [("POSITION_CMD", 0), ...]
ENUM_INT = set() # int-based enum（IntEnum / _CEnum）：可直接傳成員，不需 .value
_ep = args.enums or os.path.join(os.path.dirname(SRC), "AdvMotDrv.py")
if os.path.exists(_ep):
    import enum, importlib.util
    _spec = importlib.util.spec_from_file_location("_stub_enums", _ep)
    _em = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_em)          # AdvMotDrv.py 只有 enum 定義，不會載入 DLL
    for _n, _o in vars(_em).items():
        if isinstance(_o, type) and issubclass(_o, enum.Enum) and _o not in (enum.Enum, enum.IntEnum):
            ENUMS[_n] = [(k, v.value) for k, v in _o.__members__.items()]
            if issubclass(_o, int):
                ENUM_INT.add(_n)
ENUM_ALIAS = {"PATH_MOVE_MODE_CM2": "PATH_MOVE_MODE_CM2"}

def enum_doc(cname):
    """C enum 名稱 -> docstring 說明；不是已知 enum 回傳 None"""
    py = ENUM_ALIAS.get(cname, cname)
    if py not in ENUMS:
        return None
    mem = ENUMS[py]
    show = ", ".join(f"{k}={v}" for k, v in mem[:8])
    more = f", …共 {len(mem)} 個" if len(mem) > 8 else ""
    how = f"可直接傳 {py}.<成員>" if py in ENUM_INT else f"請傳 {py}.<成員>.value"
    return f"enum {py}，{how}；{show}{more}"

# ---------------- ctypes 型別 → Python 型別 ----------------
INT = {"c_uint8","c_int8","c_ubyte","c_byte","c_uint16","c_int16","c_ushort","c_short","c_uint32","c_int32",
       "c_uint","c_int","c_ulong","c_long","c_uint64","c_int64","c_ulonglong","c_longlong","c_size_t","c_ssize_t"}
FLT = {"c_double","c_float","c_longdouble"}
STRUCTS_USED = set()

def node_src(n):
    return ast.get_source_segment(src, n)

def arg_type(n):
    """argtypes 的一個元素 -> 呼叫時可傳入的 Python 型別"""
    if isinstance(n, ast.Name):
        t = n.id
        if t in INT: return "int"
        if t in FLT: return "float"
        if t == "c_bool": return "bool"
        if t == "c_char_p": return "bytes | Array[c_char] | None"   # 輸出 buffer 用 create_string_buffer(n)
        if t == "c_wchar_p": return "str | None"
        if t == "c_void_p": return "_VoidPtrArg"
        if t == "c_char": return "bytes"
        STRUCTS_USED.add(t)
        return t                     # 傳值的 struct 或 callback 型別
    if isinstance(n, ast.Call) and getattr(n.func, "id", "") == "POINTER" and len(n.args) == 1:
        inner = n.args[0]
        it = node_src(inner)
        if isinstance(inner, ast.Name) and inner.id not in INT | FLT | {"c_bool","c_char","c_void_p"}:
            STRUCTS_USED.add(inner.id)
        if it == "c_void_p":
            return "_PtrArg[c_void_p]"
        return f"_PtrArg[{it}]"
    return "Any"

def ret_type(n):
    if n is None: return "int"
    t = node_src(n)
    if t in INT: return "int"
    if t in FLT: return "float"
    if t == "c_bool": return "bool"
    if t == "None": return "None"
    if t == "c_char_p": return "bytes | None"
    if t == "c_void_p": return "int | None"
    return "Any"


# ---------------- C 型別資訊（顯示在 docstring） ----------------
# ctypes 名稱 -> (C 型別, 大小 bytes, 範圍)
CT_INFO = {
    "c_uint8": ("U8", 1, "0 ~ 255"), "c_ubyte": ("U8", 1, "0 ~ 255"),
    "c_int8": ("I8", 1, "-128 ~ 127"), "c_byte": ("I8", 1, "-128 ~ 127"),
    "c_uint16": ("U16", 2, "0 ~ 65535"), "c_ushort": ("U16", 2, "0 ~ 65535"),
    "c_int16": ("I16", 2, "-32768 ~ 32767"), "c_short": ("I16", 2, "-32768 ~ 32767"),
    "c_uint32": ("U32", 4, "0 ~ 4294967295"), "c_ulong": ("U32", 4, "0 ~ 4294967295"),
    "c_uint": ("U32", 4, "0 ~ 4294967295"),
    "c_int32": ("I32", 4, "-2147483648 ~ 2147483647"), "c_long": ("I32", 4, "-2147483648 ~ 2147483647"),
    "c_int": ("I32", 4, "-2147483648 ~ 2147483647"),
    "c_uint64": ("U64", 8, "0 ~ 2^64-1"), "c_ulonglong": ("U64", 8, "0 ~ 2^64-1"),
    "c_int64": ("I64", 8, "-2^63 ~ 2^63-1"), "c_longlong": ("I64", 8, "-2^63 ~ 2^63-1"),
    "c_float": ("F32", 4, "float"), "c_double": ("F64", 8, "double"),
    "c_bool": ("bool", 1, "True / False"), "c_char": ("I8", 1, "char"),
    "c_char_p": ("PI8", 8, "char*，字串或輸出 buffer"),
    "c_void_p": ("HAND / PVOID", 8, "void*，handle 或位址"),
}
PTR_NAME = {"U8": "PU8", "I8": "PI8", "U16": "PU16", "I16": "PI16", "U32": "PU32", "I32": "PI32",
            "U64": "PU64", "I64": "PI64", "F32": "PF32", "F64": "PF64", "HAND / PVOID": "PHAND"}
# C header 型別別名 -> 正規化 (kind, size, is_ptr)
C_NORM = {"U8": ("i", 1), "I8": ("i", 1), "BYTE": ("i", 1), "UCHAR": ("i", 1), "char": ("i", 1), "CHAR": ("i", 1),
          "U16": ("i", 2), "I16": ("i", 2), "USHORT": ("i", 2), "WORD": ("i", 2), "short": ("i", 2),
          "U32": ("i", 4), "I32": ("i", 4), "ULONG": ("i", 4), "LONG": ("i", 4), "DWORD": ("i", 4), "int": ("i", 4),
          "UINT": ("i", 4), "BOOL": ("i", 4), "U64": ("i", 8), "I64": ("i", 8),
          "F32": ("f", 4), "float": ("f", 4), "F64": ("f", 8), "double": ("f", 8), "bool": ("b", 1),
          "HAND": ("p", 8), "HANDLE": ("p", 8), "PVOID": ("p", 8), "void*": ("p", 8), "FILE*": ("p", 8)}
C_PTR = {"PU8": "U8", "PI8": "I8", "PU16": "U16", "PI16": "I16", "PU32": "U32", "PI32": "I32", "PULONG": "U32",
         "PUSHORT": "U16", "PF32": "F32", "PF64": "F64", "PHAND": "HAND", "PI64": "I64", "PU64": "U64"}

def ctype_info(n):
    """argtypes 元素 -> (C 型別, 說明, 正規化)"""
    if isinstance(n, ast.Name):
        t = n.id
        if t in CT_INFO:
            c, sz, rng = CT_INFO[t]
            note = f"{sz} bytes, {rng}"
            if t == "c_uint": note += "（常用於 enum）"
            k = "p" if t in ("c_void_p", "c_char_p") else ("f" if c.startswith("F") else ("b" if c == "bool" else "i"))
            return c, f"{t}, {note}", (k, sz, t == "c_char_p")
        if t in ("CALLBACK_FUNC", "ADV_USER_CALLBACK_FUNC"):
            return "callback", f"{t}，函式指標 U32 (*)(U32, void*)", ("p", 8, False)
        return t, f"{t} struct，以值傳遞", ("s", t, False)
    if isinstance(n, ast.Call) and getattr(n.func, "id", "") == "POINTER" and n.args:
        inner = n.args[0]
        it = node_src(inner)
        if it in CT_INFO:
            c = CT_INFO[it][0]
            pc = PTR_NAME.get(c, c + "*")
            kind = "p" if it in ("c_void_p", "c_char_p") else ("i" if c[0] in "UI" else c[0].lower())
            return pc, f"POINTER({it})，指向 {c}，可用 byref() / 陣列", ("p", 8, True, kind, CT_INFO[it][1])
        return f"{it}*", f"POINTER({it})，可用 byref(struct) / 陣列", ("p", 8, True, "s", it)
    return node_src(n), "", None

def c_norm(ct):
    """C header 型別字串 -> 與 ctype_info 第三項可比較的形式；無法判斷回傳 None"""
    if ct in C_NORM:
        k, sz = C_NORM[ct]; return (k, sz, ct in ("char*",))
    if ct in C_PTR:
        b = C_PTR[ct]
        k, sz = C_NORM.get(b, ("p", 8))
        return ("p", 8, True, k, sz)
    if ct.endswith("*"):
        b = ct[:-1]
        if b in C_NORM: k, sz = C_NORM[b]; return ("p", 8, True, k, sz)
        if b in ("void",): return ("p", 8, False)
        if b.endswith("*"): return ("p", 8, True, "p", 8)                       # FILE** 等
        return ("p", 8, True, "?", b)
    if re.search(r"CALLBACK|_FUNC$", ct): return ("p", 8, False)                 # callback 函式指標
    if re.fullmatch(r"P[A-Z][A-Z0-9_]*", ct) and ct not in C_PTR:              # PBUFFER_STATUS 這類 struct 指標 typedef
        return ("p", 8, True, "?", ct[1:])
    if re.fullmatch(r"[A-Z][A-Z0-9_]*", ct): return ("enum_or_struct", ct)
    return None

def mismatch(cn, pn):
    """C header 正規化 vs ctypes 正規化，只標出明確不相容的情況"""
    if cn is None or pn is None: return False
    if cn[0] == "enum_or_struct":
        return pn[0] not in ("i", "s")            # enum -> 4-byte int；或同名 struct
    if cn[0] == "p" and pn[0] == "p":
        if len(cn) == 5 and len(pn) == 5:
            if cn[3] == "?" or pn[3] == "s": return False
            return cn[3] != pn[3] or cn[4] != pn[4]
        return False
    if cn[0] != pn[0]: return not ({cn[0], pn[0]} <= {"i", "b"})
    return cn[1] != pn[1]

# ---------------- 收集 _bind ----------------
classes = []   # (cls_name, [(attr, dllname, argnodes|None, restnode|None, lineno, comment)])
for c in tree.body:
    if not isinstance(c, ast.ClassDef):
        continue
    items = []
    for st in c.body:
        if not (isinstance(st, ast.Assign) and isinstance(st.value, ast.Call)
                and getattr(st.value.func, "id", "") == "_bind"):
            continue
        call = st.value
        attr = st.targets[0].id
        dll = call.args[0].value if call.args and isinstance(call.args[0], ast.Constant) else attr
        argn = call.args[1] if len(call.args) > 1 else None
        resn = call.args[2] if len(call.args) > 2 else None
        for kw in call.keywords:
            if kw.arg == "argtypes": argn = kw.value
            if kw.arg == "restype": resn = kw.value
        if isinstance(argn, ast.Constant) and argn.value is None:
            argn = None
        items.append((attr, dll, argn, resn))
    classes.append((c.name, items))

# ---------------- 輸出 ----------------
mod = os.path.splitext(os.path.basename(SRC))[0]
pkg_imports = [l for l in src.splitlines() if re.match(r"\s*from\s+\S+\s+import\s+\*", l)]
L = [f'"""Type stub for {mod}（由 gen_api_pyi.py 從 {os.path.basename(SRC)} 自動產生）。',
     "",
     "所有函式都是 class 上的 staticmethod，直接以 Class.Func(...) 呼叫。",
     "enum 參數 (ABS_MODE 等)：AdvMotDrv 的 enum 若為 int-based 可直接傳成員，否則請用 .value。",
     '"""',
     "",
     *[l.strip() for l in pkg_imports],
     "from ctypes import _CArgObject, _CData, _Pointer",
     "from ctypes import CDLL as CDLL, Array as Array, c_char as c_char, c_void_p as c_void_p",
     "from typing import Any, TypeAlias, TypeVar",
     "",
     '_T = TypeVar("_T", bound=_CData)',
     "# POINTER(X) 參數可傳：byref(x)、pointer(x)、(X * n)() 陣列、或 None",
     "_PtrArg: TypeAlias = _Pointer[_T] | Array[_T] | _CArgObject | None",
     "# c_void_p 參數可傳：整數位址 / handle、c_void_p、byref(...)、任何 ctypes 物件、None",
     "_VoidPtrArg: TypeAlias = int | c_void_p | _CArgObject | _CData | None",
     "",
     "lib: CDLL",
     ""]
stats = {"funcs": 0, "named": 0, "noargtypes": [], "mismatch": [], "typediff": [], "enum": 0, "enum_guess": 0, "enum_unknown": []}
RET_C = {"int": "U32", "bool": "BOOL", "float": "F64", "None": "void"}
for cname, items in classes:
    L.append(f"class {cname}:")
    if not items:
        L.append("    ...")
    for attr, dll, argn, resn in items:
        stats["funcs"] += 1
        rt = ret_type(resn)
        proto = PROTO.get(dll)
        head, warn, args_doc = [], [], []
        if proto:
            head.append(proto[0])
        if argn is None:
            sig = "*args: Any"
            stats["noargtypes"].append(attr)
            warn.append("⚠ Python 端未設定 argtypes，ctypes 不會檢查參數")
        else:
            elts = argn.elts if isinstance(argn, (ast.List, ast.Tuple)) else []
            types = [arg_type(e) for e in elts]
            infos = [ctype_info(e) for e in elts]
            names, hdr_ct = None, None
            if proto:
                pn, pct = proto[1], proto[2]
                if len(pn) == len(types):
                    hdr_ct = pct
                    if all(pn) and len(set(pn)) == len(pn):
                        names = pn
                else:
                    stats["mismatch"].append(f"{attr}: C {len(pn)} 個參數, Python {len(types)} 個")
                    warn.append(f"⚠ 參數數量與 C 原型不符（C {len(pn)} / Python {len(types)}）")
            if names:
                stats["named"] += 1
            else:
                names = [f"arg{i}" for i in range(len(types))]
            # CM2：從 driver typedef 找 enum。driver 參數順序可能與 DLL 不同，所以
            #   (1) 逐位置型別都相容 -> 照位置對應
            #   (2) 否則把 typedef 中的 enum 依序對到 Python 端的 c_uint 參數（數量需相同）
            cm2_enum = {}                        # 參數 index -> (enum 名稱, 是否為推定)
            cm2 = CM2_TYPES.get(dll)
            if cm2 is not None and not hdr_ct:
                def _ok(i, ct):
                    if i == 0: return True       # driver 第一個是 HAND，DLL 是 ID
                    if enum_doc(ct): return infos[i][2] is not None and infos[i][2][0] == "i" and infos[i][2][1] == 4
                    cn = c_norm(ct)
                    return cn is None or ct == node_src(elts[i]) or not mismatch(cn, infos[i][2])
                if len(cm2) == len(types) and all(_ok(i, ct) for i, ct in enumerate(cm2)):
                    cm2_enum = {i: (ct, False) for i, ct in enumerate(cm2) if i and enum_doc(ct)}
                else:
                    ens = [ct for ct in cm2 if enum_doc(ct)]
                    slots = [i for i, e in enumerate(elts) if isinstance(e, ast.Name) and e.id == "c_uint"]
                    if ens and len(ens) == len(slots):
                        cm2_enum = {i: (ct, True) for i, ct in zip(slots, ens)}
                        stats["enum_guess"] += len(ens)
            for i, (n, (c, note, pnorm)) in enumerate(zip(names, infos)):
                ct = c
                en, guess = None, False
                if hdr_ct and enum_doc(hdr_ct[i]):
                    en = hdr_ct[i]
                elif i in cm2_enum:
                    en, guess = cm2_enum[i]
                if en and pnorm and pnorm[0] == "i" and pnorm[1] == 4:
                    py_en = ENUM_ALIAS.get(en, en)
                    if py_en in ENUM_INT:
                        types[i] = f"{py_en} | int"   # 簽章直接接受 enum 成員
                    args_doc.append(f"    {n} ({en}): {enum_doc(en)}" + ("（依 driver typedef 順序推定）" if guess else ""))
                    stats["enum"] += 1
                    continue
                if isinstance(elts[i], ast.Name) and elts[i].id == "c_uint" and not hdr_ct:
                    stats["enum_unknown"].append(f"{attr}.{n}")
                if hdr_ct:
                    ct = hdr_ct[i]                       # 以 C header 的型別名稱為準（例如 ABS_MODE、HAND）
                    if ct != node_src(elts[i]) and mismatch(c_norm(ct), pnorm):
                        warn.append(f"⚠ {n}: C 是 {ct}，Python 綁定為 {node_src(elts[i])}")
                        stats["typediff"].append(f"{attr}.{n}: C {ct} / Python {node_src(elts[i])}")
                    elif ct != c and c not in ("HAND / PVOID",) and not ct.startswith(c):
                        note = f"{c}；" + note           # header 名稱與 ctypes 推得的不同時兩者都列
                args_doc.append(f"    {n} ({ct}): {note}")
            sig = ", ".join(f"{n}: {t}" for n, t in zip(names, types))
            if types:
                sig += ", /"
        rc = proto[3] if proto else RET_C.get(rt, rt)
        # docstring 只放 C 原型：有 header 原型就原樣使用；
        # 沒有（例如 Acm2_*）則用推得的 C 型別組出原型，參數名稱沿用 argN
        if head:
            cproto = head[0]
        else:
            cts = []
            for a in args_doc:
                m_ = re.match(r"\s*(\w+) \((.+?)\):", a)
                ct_ = m_.group(2).replace("HAND / PVOID", "HAND")
                cts.append(f"{ct_} {m_.group(1)}")
            cproto = f"{rc} {dll}({', '.join(cts)})"
        L.append("    @staticmethod")
        L.append(f"    def {attr}({sig}) -> {rt}:")
        L.append(f'        """{cproto}"""')
    L.append("")
open(OUT, "w", encoding="utf-8").write("\n".join(L).rstrip() + "\n")
print(f"wrote {OUT}: {stats['funcs']} functions, {stats['named']} with C parameter names, "
      f"{stats['enum']} enum parameters ({stats['enum_guess']} 依順序推定)")
if stats["enum_unknown"]:
    print(f"  c_uint 參數但找不到對應 enum {len(stats['enum_unknown'])} 個（可能是 enum，docstring 只標 U32）")
    print("   ", ", ".join(stats["enum_unknown"]))
if stats["noargtypes"]:
    print("  未設定 argtypes:", ", ".join(stats["noargtypes"]))
if stats["typediff"]:
    print(f"  與 C 原型型別不符 {len(stats['typediff'])} 個:")
    for x in stats["typediff"]:
        print("   ", x)
if stats["mismatch"]:
    print(f"  與 C 原型參數數量不符 {len(stats['mismatch'])} 個:")
    for x in stats["mismatch"]:
        print("   ", x)
