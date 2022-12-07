## Pyvium and Core methods
:white_check_mark: ready
:small_orange_diamond: under development
:no_entry_sign: not working

| Pyvium Methods  | Core Methods |
| ------------- | ------- |
| :small_orange_diamond: open_driver() |   :white_check_mark: IV_open()| 
| :small_orange_diamond: close_driver()  | :white_check_mark: IV_close()|
| :small_orange_diamond: get_max_device_number()   | :white_check_mark: IV_MaxDevices()|
| :small_orange_diamond: select_iviumsoft_instance(int)   | :white_check_mark: IV_selectdevice(int)|
| :small_orange_diamond: get_device_status() | :white_check_mark: IV_getdevicestatus()|
| :small_orange_diamond: get_device_serial_number()  | :white_check_mark: IV_readSN()|
| :small_orange_diamond: connect_device()  | :white_check_mark: IV_connect(int)|
| :small_orange_diamond: disconnect_device() | ^ |
|   |  :white_check_mark: IV_VersionHost(version)|
| :small_orange_diamond: get_dll_version() |  :white_check_mark: IV_VersionDll()|
| :small_orange_diamond:  is_iviumsoft_running() |  :white_check_mark: IV_VersionCheck()|
|   |  :white_check_mark: IV_HostHandle()|
|   |  :white_check_mark: IV_VersionDllFile()|
|   |  :white_check_mark: IV_VersionDllFileStr()|
| :small_orange_diamond: select_channel(int) |  :white_check_mark: IV_SelectChannel(int)|
| :small_orange_diamond: get_cell_status()  |  :white_check_mark: IV_getcellstatus()|
| :small_orange_diamond: set_connection_mode() |  :white_check_mark: IV_setconnectionmode(value)|
|   |  :white_check_mark: IV_setcellon(cellon)|
|   |  :white_check_mark: IV_setpotential(value)|
|   |  :white_check_mark: IV_setpotentialWE2(value)|
|  |  :white_check_mark: IV_setcurrent(value)|
|  |  :white_check_mark: IV_getpotential(value)|
|   |  :white_check_mark: IV_setcurrentrange(value)|
|  |  :white_check_mark: IV_setcurrentrangeWE2(value)|
|      |  :white_check_mark: IV_getcurrent(value)|
|      |  :white_check_mark: IV_getcurrentWE2(value)|
|      |  :white_check_mark: IV_setfilter(value)|
|      |  :white_check_mark: IV_setstability(value)|
|      |  :white_check_mark: IV_setbistatmode(value)|
|      |  :white_check_mark: IV_setdac(channr, value)|
|      |  :white_check_mark: IV_getadc(channr, value)|
|      |  :white_check_mark: IV_setmuxchannel(value)|
|      |  :white_check_mark: IV_setdigout(value)|
|      |  :white_check_mark: IV_getdigin(value)|
|      |  :white_check_mark: IV_setfrequency(value)|
|      |  :white_check_mark: IV_setamplitude(value)|
|      |  :white_check_mark: IV_getcurrenttrace(npoints, rate, values)|
|      |  :white_check_mark: IV_getcurrentWE2trace(npoints, rate, values)|
|      |  :white_check_mark: IV_getpotentialtrace(npoints, rate, values)|
|      |  :white_check_mark: IV_we32setchannel(index)|
|      |  :white_check_mark: IV_we32setoffset(index, value)|
|      |  :white_check_mark: IV_we32setoffsets(nval, values)|
|      |  :white_check_mark: IV_we32getoffsets(nval, values)|
|      |  :white_check_mark: IV_we32readcurrents(values)|
|      |  :white_check_mark: IV_readmethod(fname)|
|      |  :white_check_mark: IV_savemethod(fname)|
|      |  :white_check_mark: IV_startmethod(fname)|
|      |  :white_check_mark: IV_abort()|
|      |  :white_check_mark: IV_savedata(fname)|
|      |  :white_check_mark: IV_setmethodparameter(parname, parvalue)|
|      |  :white_check_mark: IV_Ndatapoints(value)|
|      |  :white_check_mark: IV_getdata(pointnr, x, y, z)|
|      |  :white_check_mark: IV_getdatafromline(pointnr, scannr, x, y, z)|
|      |  :small_orange_diamond: IV_getDbFileName(fname)|