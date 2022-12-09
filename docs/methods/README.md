## Pyvium and Core methods
:heavy_check_mark: ready
:small_orange_diamond: under development
:x: not working

| Pyvium Methods                                        | Core Methods                              |
| ----------------------------------------------------- | ----------------------------------------- |
| :heavy_check_mark: open_driver()                      | :heavy_check_mark: IV_open()              |  
| :heavy_check_mark: close_driver()                     | :heavy_check_mark: IV_close()             |
| :heavy_check_mark: get_max_device_number()            | :heavy_check_mark: IV_MaxDevices()        |
| :heavy_check_mark: get_active_iviumsoft_instances(int)|                                           |
| :heavy_check_mark: select_iviumsoft_instance(int)     | :heavy_check_mark: IV_selectdevice(int)   |
| :heavy_check_mark: get_device_status()                | :heavy_check_mark: IV_getdevicestatus()   |
| :heavy_check_mark: is_iviumsoft_running()             |                                           |
| :heavy_check_mark: get_device_serial_number()         | :heavy_check_mark: IV_readSN()            |
| :heavy_check_mark: connect_device()                   | :heavy_check_mark: IV_connect(int)        |
| :heavy_check_mark: disconnect_device()                |^                                          |
|                                                       | :heavy_check_mark: IV_VersionHost(version)|
| :heavy_check_mark: get_dll_version()                  | :heavy_check_mark: IV_VersionDll()        |
|                                                       | :heavy_check_mark: IV_VersionCheck()      |
|                                                       | :heavy_check_mark: IV_HostHandle()                |
|                                                       | :heavy_check_mark: IV_VersionDllFile()            |
|                                                       | :heavy_check_mark: IV_VersionDllFileStr()         |
| :heavy_check_mark: select_channel(int)                | :heavy_check_mark: IV_SelectChannel(int)          |
| :heavy_check_mark: get_cell_status()                  |  :heavy_check_mark: IV_getcellstatus()            |
| :heavy_check_mark: set_connection_mode()              |  :heavy_check_mark: IV_setconnectionmode(value)   |
|                                                       |  :heavy_check_mark: IV_setcellon(cellon)          |
|                                                       |  :heavy_check_mark: IV_setpotential(value)|
|                                                       |  :heavy_check_mark: IV_setpotentialWE2(value)|
|                                                       |  :heavy_check_mark: IV_setcurrent(value)|
|                                                       |  :heavy_check_mark: IV_getpotential(value)|
|                                                       |  :heavy_check_mark: IV_setcurrentrange(value)|
|                                                       |  :heavy_check_mark: IV_setcurrentrangeWE2(value)|
|                                                       |  :heavy_check_mark: IV_getcurrent(value)|
|                                                       |  :heavy_check_mark: IV_getcurrentWE2(value)|
|                                                       |  :heavy_check_mark: IV_setfilter(value)|
|                                                       |  :heavy_check_mark: IV_setstability(value)|
|                                                       |  :heavy_check_mark: IV_setbistatmode(value)|
|                                                       |  :heavy_check_mark: IV_setdac(channr, value)|
|                                                       |  :heavy_check_mark: IV_getadc(channr, value)|
|                                                       |  :heavy_check_mark: IV_setmuxchannel(value)|
|                                                       |  :heavy_check_mark: IV_setdigout(value)|
|                                                       |  :heavy_check_mark: IV_getdigin(value)|
|  :heavy_check_mark: set_ac_frequency()                |  :heavy_check_mark: IV_setfrequency(value)|
|  :heavy_check_mark: set_ac_amplitude()                |  :heavy_check_mark: IV_setamplitude(value)|
|                                                       |  :heavy_check_mark: IV_getcurrenttrace(npoints, rate, values)|
|                                                       |  :heavy_check_mark: IV_getcurrentWE2trace(npoints, rate, values)|
|      |  :heavy_check_mark: IV_getpotentialtrace(npoints, rate, values)|
|      |  :heavy_check_mark: IV_we32setchannel(index)|
|      |  :heavy_check_mark: IV_we32setoffset(index, value)|
|      |  :heavy_check_mark: IV_we32setoffsets(nval, values)|
|      |  :heavy_check_mark: IV_we32getoffsets(nval, values)|
|      |  :heavy_check_mark: IV_we32readcurrents(values)|
|      |  :heavy_check_mark: IV_readmethod(fname)|
|      |  :heavy_check_mark: IV_savemethod(fname)|
|      |  :heavy_check_mark: IV_startmethod(fname)|
|      |  :heavy_check_mark: IV_abort()|
|      |  :heavy_check_mark: IV_savedata(fname)|
|      |  :heavy_check_mark: IV_setmethodparameter(parname, parvalue)|
|      |  :heavy_check_mark: IV_Ndatapoints(value)|
|      |  :heavy_check_mark: IV_getdata(pointnr, x, y, z)|
|      |  :heavy_check_mark: IV_getdatafromline(pointnr, scannr, x, y, z)|
|      |  :small_orange_diamond: IV_getDbFileName(fname)|