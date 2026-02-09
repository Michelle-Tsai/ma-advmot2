import time
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2 as AdvMot
from AcmP.AdvMotErr_CM2 import ErrorCode2 as err2
from AcmP.AdvMotPropID_CM2 import PropertyID2 as AdvPpt
from AcmP.AdvMotApi_CM2 import *
from colorama import init, Fore, Style

init(autoreset=True, strip=False)

def _PrintResult(isPass, message):
    if isPass:
        print(f'{Fore.GREEN}[✓ Pass]{message}')
    else:
        print(f'{Fore.RED}[X Fail]{message}')

def AdvInitial():
    errCde = 0
    maxEnt = 10
    outEnt = c_uint32(0)
    devlist = (DEVLIST*maxEnt)()
    errCde = AdvMot.Acm2_GetAvailableDevs(devlist, maxEnt, byref(outEnt))
    for i in range(outEnt.value):
        print(f'{Fore.LIGHTBLUE_EX}Device number:{devlist[i].dwDeviceNum:x}')
    errCde = AdvMot.Acm2_DevInitialize()
    if errCde != err2.SUCCESS.value:
        _PrintResult(False, f'Device initialize failed, errCde:{errCde:x}')

def AdvResetDo():
    errCde = 0
    doCh = c_uint32(0)
    setVal = c_uint32(0)
    errCde = AdvMot.Acm2_ChSetDOByte(doCh, 1, setVal)
    if errCde != err2.SUCCESS.value:
        _PrintResult(False, f'Reset Do:{doCh.value} value failed, errCde:{errCde:x}')
    # else:
        _PrintResult(True, f'Reset Do:{doCh.value} value:{setVal.value} successed')

def _visualizeBits(number, width: int = 8) -> str:
    """
    將整數轉換為視覺化的 bit 符號
    :param number: 要轉換的數字 (例如 245)
    :param width: 顯示位元的寬度 (預設 8 bit, 不足自動補齊)
    """
    bitStr = f'{number:0{width}b}'
    transToSymbol = str.maketrans('01', '○●')
    return bitStr.translate(transToSymbol)

def AdvGetDoStatus():
    errCde = 0
    doCh = c_uint32(0)
    getVal = c_uint32(0)
    errCde = AdvMot.Acm2_ChGetDOByte(doCh, 1, byref(getVal))
    if errCde != err2.SUCCESS.value:
        _PrintResult(False, f'Get Do:{doCh.value} value failed, errCde:{errCde:x}')
    else:
        _PrintResult(True, f'Get Do:{doCh.value} value successed')
    while errCde == err2.SUCCESS.value:
        getStr = _visualizeBits(getVal.value, 8)
        print(f'{Fore.LIGHTYELLOW_EX}{getStr}', end='\r', flush=True)
        time.sleep(1) # 每 1s 獲取一次狀態
        errCde = AdvMot.Acm2_ChGetDOByte(doCh, 1, byref(getVal))

if __name__ == '__main__':
    AdvInitial()
    AdvResetDo()
    AdvGetDoStatus()