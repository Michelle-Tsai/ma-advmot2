# Log Functions
#### Amc_SetApiLog
Set API Log options

```cpp
U32 Amc_SetApiLog(const char* dir, const char* baseName, const AMCApiLogOptions* opt, U64 bufferSize)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

logOpt = AMC_API_LOG_OPT()
logDir = b'D:\\'
baseName = b'amc_api_log'
bufferSize = 1024
logOpt.sizePerFile = bufferSize
AmcApi.Amc_SetApiLog(logDir, baseName, byref(logOpt), bufferSize)
```

#### Amc_StartApiLog
```cpp
U32 Amc_StartApiLog()
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

Amc_StartApiLog()
```

#### Amc_StopApiLog
```cpp
U32 Amc_StopApiLog()
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

Amc_StopApiLog()
```

#### Amc_OpenApiLogFile
```cpp
U32 Amc_OpenApiLogFile(const char* filePath, FILE** pFile)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

def convert_filetime_to_datetime(self, filetime_int: int):
    """
    將一個 64-bit Windows FILETIME (I64) 轉換為
    人類可讀的 (human-readable) 本地時區 datetime 物件。

    FILETIME 是自 1601-01-01 00:00:00 UTC 起的 100 奈秒間隔數。
    """
    # 1. 定義 FILETIME 的起始時間 (epoch)
    epoch = datetime.datetime(1601, 1, 1, tzinfo=datetime.timezone.utc)
    # 2. 計算總共的微秒數 (microseconds)
    # 1 微秒 = 10 個 (100奈秒) 間隔
    microseconds_delta = filetime_int / 10
    # 3. 建立時間差 (timedelta)
    delta = datetime.timedelta(microseconds=microseconds_delta)
    # 4. 計算出正確的 UTC 時間
    utc_time = epoch + delta
    # 5. 轉換為系統的本地時區 (例如: CST)
    local_time = utc_time.astimezone(None)
    return local_time

pfile = c_void_p()
file_name = b"D:\\TestLog_20251215_195932_443.dat"
api_header = AMC_API_LOG_HEADER()
out_str = create_string_buffer(1024)
stopCnd = 0
cnt = 0
Amc_OpenApiLogFile(file_name, byref(pfile))
while stopCnd != ErrorCode2.NoMoreLogData:
    data_buffer = (c_uint8 * 1024)()
    stopCnd = Amc_GetApiLogData(pfile, data_buffer, 1024, byref(api_header))
    print(f'stopCnd:0x{stopCnd:x}')
    print(f'header.len={api_header.dataLen}')
    print(f"type={'Command' if api_header.type == AMC_API_LOG_DATA_TYPE.LogCommand.value else 'Response'}, functionId={api_header.functionId}")
    if stopCnd == ErrorCode2.SUCCESS:
        Amc_ApiLogToString(byref(api_header), data_buffer, out_str, 1024)
        output = out_str.value.decode('utf-8')
        print(f'{convert_filetime_to_datetime(api_header.timestamp)}|{output}')
        cnt = cnt + 1
        print(f'cnt:{cnt}\n')
Amc_CloseApiLogFile(pfile)
```

#### Amc_GetApiLogData
```cpp
U32 Amc_GetApiLogData(FILE* pFile, U8* pDataBuff, U32 bufferSize, AMCApiLogHeader* pApiLogInfo)
```

#### Amc_CloseApiLogFile
```cpp
U32 Amc_CloseApiLogFile(FILE* pFile);
```

#### Amc_ApiLogToString
```cpp
U32 Amc_ApiLogToString(const AMCApiLogHeader* info, const U8* rawData, I8* outString, U64 outSize)
```

#### Amc_ApiLogGetStatus
```cpp
U32 Amc_ApiLogGetStatus(AMCAPILogStatus* status)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

getStatus = AMC_API_LOG_STATUS()
Amc_ApiLogGetStatus(byref(getStatus))
```

#### Amc_DataLog_SetLog
```cpp
U32 Amc_DataLog_SetLog(U32 DevID, U32 Channel, const LogDataSource* source, U16 index)
```

```python
import time
import unittest
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2, AmcLogAPI
from AcmP.AdvMotErr_CM2 import ErrorCode2
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *

dataLogSource = AMC_DATA_LOG_SOURCE()
dataLogSource.type = c_uint(AMC_DATA_LOG_SOURCE_TYPE.LOG_SOURCE_MOTION_AXIS.value)
dataLogSource.selection[0] = c_uint32(0)
dataLogSource.count = 1
dataLogSource.items.smItems = AMC_DATA_LOG_SM_ITEMS()
dataLogSource.items.smItems.cmd_pos = c_uint8(True)
dataLogSource.items.smItems.act_pos = c_uint8(True)
dataLogSource.items.smItems.cmd_vel = c_uint8(True)
dataLogSource.items.smItems.act_vel = c_uint8(True)
log_ch = c_uint32(1)
log_index = c_uint16(0)
Amc_DataLog_SetLog(devID, log_ch, byref(dataLogSource), log_index)
```

#### Amc_DataLog_GetLog
```cpp
U32 Amc_DataLog_GetLog(U32 DevID, U32 Channel, LogDataSource* source, U16 index)
```

```python
import time
import unittest
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2, AmcLogAPI
from AcmP.AdvMotErr_CM2 import ErrorCode2
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *

getDataLogSource = AMC_DATA_LOG_SOURCE()
log_ch = c_uint32(1)
log_index = c_uint16(0)
Amc_DataLog_GetLog(devID, log_ch, byref(getDataLogSource), log_index)
```

#### Amc_DataLog_SetLogOption
```cpp
U32 Amc_DataLog_SetLogOption(U32 DevID, U32 Channel, const DataLogOptions* options)
```

```python
import time
import unittest
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2, AmcLogAPI
from AcmP.AdvMotErr_CM2 import ErrorCode2
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *

dataLogOption = AMC_DATA_LOG_OPTIONS()
dataLogOption.isRotateFile = c_uint8(False)
dataLogOption.maxLogFileCount = c_uint32(1)
log_ch = c_uint32(1)
Amc_DataLog_SetLogOption(devID, log_ch, byref(dataLogOption))
```

#### Amc_DataLog_GetLogOption
```cpp
U32 Amc_DataLog_GetLogOption(U32 DevID, U32 Channel, DataLogOptions* options)
```

```python
import time
import unittest
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2, AmcLogAPI
from AcmP.AdvMotErr_CM2 import ErrorCode2
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *

log_ch = c_uint32(1)
getDataLogOption = AMC_DATA_LOG_OPTIONS()
Amc_DataLog_GetLogOption(devID, log_ch, byref(getDataLogOption))
```

#### Amc_DataLog_SetLogFilePath
```cpp
U32 Amc_DataLog_SetLogFilePath(U32 DevID, U32 Channel, const char* dirPath, const char* fileName)
```

```python
import time
import unittest
import os
from ctypes import *
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2, AmcLogAPI
from AcmP.AdvMotErr_CM2 import ErrorCode2
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *

log_ch = c_uint32(1)
dirPath = b'/tmp'
fileName = b'PyTestDataLog'
Amc_DataLog_SetLogFilePath(devID, log_ch, dirPath, fileName)
```

#### Amc_DataLog_GetLogFilePath
```cpp
U32 Amc_DataLog_GetLogFilePath(U32 DevID, U32 Channel, char* dirPath, char* fileName)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
getDirPath = create_string_buffer(256)
getFileName = create_string_buffer(256)
Amc_DataLog_GetLogFilePath(devID, log_ch, getDirPath, getFileName)
```

#### Amc_DataLog_GetRotatedLogFilePaths
```cpp
U32 Amc_DataLog_GetRotatedLogFilePaths(U32 DevID, U32 Channel, char* fileNamesBuffer, U32* bufferSize, PU32 fileCount)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
fileBufferSize = c_uint32(1024)
getFilePath = create_string_buffer(fileBufferSize.value)
getFileCnt = c_uint32(0)
Amc_DataLog_GetRotatedLogFilePaths(devID, log_ch, getFilePath, byref(fileBufferSize), byref(getFileCnt))
```

#### Amc_DataLog_SetLogHeader
```cpp
U32 Amc_DataLog_SetLogHeader(U32 DevID, U32 Channel, const char* header)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
logHeader = b'Data Log Test from python'
Amc_DataLog_SetLogHeader(devID, log_ch, logHeader)
```

#### Amc_DataLog_GetLogHeader
```cpp
U32 Amc_DataLog_GetLogHeader(U32 DevID, U32 Channel, char* header)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
getLogHeader = create_string_buffer(256)
Amc_DataLog_GetLogHeader(devID, log_ch, getLogHeader)
```

#### Amc_DataLog_GetStatus
```cpp
U32 Amc_DataLog_GetStatus(U32 DevID, U32 Channel, LogStatus* outStatus)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
getDataLogStatus = AMC_DATA_LOG_STATUS()
Amc_DataLog_GetStatus(devID, log_ch, byref(getDataLogStatus))
```

#### Amc_DataLog_StartLog
```cpp
U32 Amc_DataLog_StartLog(U32 DevID, U32 Channel)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
Amc_DataLog_StartLog(devID, log_ch)
```

#### Amc_DataLog_StopLog
```cpp
U32 Amc_DataLog_StopLog(U32 DevID, U32 Channel)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
Amc_DataLog_StopLog(devID, log_ch)
```

#### Amc_DataLog_ResetLog
```cpp
U32 Amc_DataLog_ResetLog(U32 DevID, U32 Channel)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

log_ch = c_uint32(1)
Amc_DataLog_ResetLog(devID, log_ch)
```

#### Amc_DataLog_GetLogFile
```cpp
U32 Amc_DataLog_GetLogFile(U32 DevID, U32 Channel, const char* remoteFilePath, char* outBuffer, U32* bufferSize)
```

```python
import unittest
import os
import time
import datetime
from AcmP.AdvCmnAPI_CM2 import AdvCmnAPI_CM2
from AcmP.AdvCmnAPI_CM2 import AmcLogAPI
from AcmP.AdvMotDrv import *
from AcmP.AdvMotApi_CM2 import *
from AcmP.AdvMotPropID_CM2 import PropertyID2
from AcmP.AdvMotErr_CM2 import ErrorCode2
from ctypes import *

bufferSize = 1024
currSize = bufferSize
fileBuffer = create_string_buffer(currSize)
log_ch = c_uint32(1)
filePath = b'/tmp/PyTestDataLog'
Amc_DataLog_GetLogFile(devID, log_ch, filePath, fileBuffer, byref(bufferSize))
```