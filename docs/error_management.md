
```
form pyvium import Pyvium
from pyvium.errors import DeviceNotConnectedToIviumSoftError, IviumSoftNotRunningError

try:
    Pyvium.open_driver()
    Pyvium.get_potential()
except IviumSoftNotRunningError:
    print('Tell the user the software is not running')
except DeviceNotConnectedToIviumSoftError:
    raise

```


| Available errors                      |
| ------------------------------------- |
| DeviceBusyError                       |
| DeviceNotConnectedToIviumSoftError    |
| DriverNotOpenError                    |
| NoDeviceDetectedError                 |
| IviumSoftNotRunningError              |
| CellOffError                          |