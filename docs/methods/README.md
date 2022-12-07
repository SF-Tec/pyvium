## Pyvium and Core methods
:white_check_mark: working method
:small_orange_diamond: under development
:no_entry_sign: not working

| Pyvium Methods  | Core Methods |
| ------------- | ------- |
| :small_orange_diamond: open_driver() | :small_orange_diamond:  |  :white_check_mark: IV_open()| 
| :small_orange_diamond: close_driver()  | :white_check_mark: IV_close()|
| :small_orange_diamond: get_max_device_number()   | :white_check_mark: IV_MaxDevices()|
| :small_orange_diamond: select_iviumsoft_instance(int)   | :white_check_mark: IV_selectdevice(int)|
| :small_orange_diamond: get_device_status() | :white_check_mark: IV_getdevicestatus()|
| :small_orange_diamond: get_device_serial_number()  | :white_check_mark: IV_readSN()|
|  :small_orange_diamond: connect_device()  | :white_check_mark: IV_connect(int)|
| :small_orange_diamond: disconnect_device() | ^ |
| :small_orange_diamond:  |  :white_check_mark: IV_VersionHost(version)|
| :small_orange_diamond:  |  :white_check_mark: IV_VersionDll()|
| :small_orange_diamond:  |  :white_check_mark: IV_VersionCheck()|
| :small_orange_diamond:  |  :white_check_mark: IV_HostHandle()|
| :small_orange_diamond:  |  :white_check_mark: IV_VersionDllFile()|
| :small_orange_diamond:  |  :white_check_mark: IV_VersionDllFileStr()|
| :small_orange_diamond:  |  :white_check_mark: IV_SelectChannel(channel)|
| :small_orange_diamond:  |  :white_check_mark: IV_getcellstatus(devcellstatus)|
| :small_orange_diamond:  |  :white_check_mark: IV_setconnectionmode(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_setcellon(cellon)|
| :small_orange_diamond:  |  :white_check_mark: IV_setpotential(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_setpotentialWE2(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_setcurrent(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_getpotential(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_setcurrentrange(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_setcurrentrangeWE2(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_getcurrent(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_getcurrentWE2(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_setfilter(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_setstability(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_setbistatmode(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_setdac(channr, value)|
| :small_orange_diamond:  |  :white_check_mark: IV_getadc(channr, value)|
| :small_orange_diamond:  |  :white_check_mark: IV_setmuxchannel(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_setdigout(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_getdigin(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_setfrequency(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_setamplitude(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_getcurrenttrace(npoints, rate, values)|
| :small_orange_diamond:  |  :white_check_mark: IV_getcurrentWE2trace(npoints, rate, values)|
| :small_orange_diamond:  |  :white_check_mark: IV_getpotentialtrace(npoints, rate, values)|
| :small_orange_diamond:  |  :white_check_mark: IV_we32setchannel(index)|
| :small_orange_diamond:  |  :white_check_mark: IV_we32setoffset(index, value)|
| :small_orange_diamond:  |  :white_check_mark: IV_we32setoffsets(nval, values)|
| :small_orange_diamond:  |  :white_check_mark: IV_we32getoffsets(nval, values)|
| :small_orange_diamond:  |  :white_check_mark: IV_we32readcurrents(values)|
| :small_orange_diamond:  |  :white_check_mark: IV_readmethod(fname)|
| :small_orange_diamond:  |  :white_check_mark: IV_savemethod(fname)|
| :small_orange_diamond:  |  :white_check_mark: IV_startmethod(fname)|
| :small_orange_diamond:  |  :white_check_mark: IV_abort()|
| :small_orange_diamond:  |  :white_check_mark: IV_savedata(fname)|
| :small_orange_diamond:  |  :white_check_mark: IV_setmethodparameter(parname, parvalue)|
| :small_orange_diamond:  |  :white_check_mark: IV_Ndatapoints(value)|
| :small_orange_diamond:  |  :white_check_mark: IV_getdata(pointnr, x, y, z)|
| :small_orange_diamond:  |  :white_check_mark: IV_getdatafromline(pointnr, scannr, x, y, z)|
| :small_orange_diamond:  |  :white_check_mark: IV_getDbFileName(fname)|