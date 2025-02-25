## Pyvium and Core methods

:heavy_check_mark: ready
:small_orange_diamond: under development
:x: not working

| Pyvium Methods                                         | Core Methods                                                    |
| ------------------------------------------------------ | --------------------------------------------------------------- |
| :heavy_check_mark: open_driver()                       | :heavy_check_mark: IV_open()                                    |
| :heavy_check_mark: close_driver()                      | :heavy_check_mark: IV_close()                                   |
| :heavy_check_mark: get_max_device_number()             | :heavy_check_mark: IV_MaxDevices()                              |
| :heavy_check_mark: get_active_iviumsoft_instances(int) |                                                                 |
| :heavy_check_mark: select_iviumsoft_instance(int)      | :heavy_check_mark: IV_selectdevice(int)                         |
| :heavy_check_mark: get_device_status()                 | :heavy_check_mark: IV_getdevicestatus()                         |
| :heavy_check_mark: is_iviumsoft_running()              |                                                                 |
| :heavy_check_mark: get_device_serial_number()          | :heavy_check_mark: IV_readSN()                                  |
| :small_orange_diamond: select_device(str)              | :heavy_check_mark: IV_SelectSn(str)                             |
| :heavy_check_mark: connect_device()                    | :heavy_check_mark: IV_connect(int)                              |
| :heavy_check_mark: disconnect_device()                 | :heavy_check_mark: IV_connect(int)                              |
|                                                        | :heavy_check_mark: IV_VersionHost(version)                      |
| :heavy_check_mark: get_dll_version()                   | :heavy_check_mark: IV_VersionDll()                              |
|                                                        | :heavy_check_mark: IV_VersionCheck()                            |
|                                                        | :heavy_check_mark: IV_HostHandle()                              |
| :heavy_check_mark: get_iviumsoft_version()             | :heavy_check_mark: IV_VersionDllFile()                          |
|                                                        | :heavy_check_mark: IV_VersionDllFileStr()                       |
| :heavy_check_mark: select_channel(int)                 | :heavy_check_mark: IV_SelectChannel(int)                        |
| :heavy_check_mark: get_cell_status()                   | :heavy_check_mark: IV_getcellstatus()                           |
| :heavy_check_mark: set_connection_mode(int)            | :heavy_check_mark: IV_setconnectionmode(int)                    |
| :heavy_check_mark: set_cell_on()                       | :heavy_check_mark: IV_setcellon(int)                            |
| :heavy_check_mark: set_cell_off()                      |                                                                 |
| :heavy_check_mark: set_potential(float)                | :heavy_check_mark: IV_setpotential(float)                       |
| :heavy_check_mark: set_we2_potential(float)            | :heavy_check_mark: IV_setpotentialWE2(float)                    |
| :heavy_check_mark: set_curretn(float)                  | :heavy_check_mark: IV_setcurrent(float)                         |
| :heavy_check_mark: get_potential()                     | :heavy_check_mark: IV_getpotential()                            |
| :heavy_check_mark: set_current_range(int)              | :heavy_check_mark: IV_setcurrentrange(int)                      |
| :heavy_check_mark: set_we2_current_range(int)          | :heavy_check_mark: IV_setcurrentrangeWE2(int)                   |
| :heavy_check_mark: get_current()                       | :heavy_check_mark: IV_getcurrent()                              |
| :heavy_check_mark: get_we2_current()                   | :heavy_check_mark: IV_getcurrentWE2()                           |
| :heavy_check_mark: set_filter(int)                     | :heavy_check_mark: IV_setfilter(int)                            |
| :heavy_check_mark: set_stability(int)                  | :heavy_check_mark: IV_setstability(int)                         |
| :heavy_check_mark: set_bistat_mode(int)                | :heavy_check_mark: IV_setbistatmode(int)                        |
| :heavy_check_mark: set_dac(int, float)                 | :heavy_check_mark: IV_setdac(int, float)                        |
| :heavy_check_mark: set_adc(int)                        | :heavy_check_mark: IV_getadc(int)                               |
| :heavy_check_mark: set_mux_channel(int)                | :heavy_check_mark: IV_setmuxchannel(int)                        |
|                                                        | :heavy_check_mark: IV_setdigout(value)                          |
|                                                        | :heavy_check_mark: IV_getdigin(value)                           |
| :heavy_check_mark: set_ac_frequency(float)             | :heavy_check_mark: IV_setfrequency(value)                       |
| :heavy_check_mark: set_ac_amplitude(float)             | :heavy_check_mark: IV_setamplitude(value)                       |
|                                                        | :heavy_check_mark: IV_getcurrenttrace(npoints, rate, values)    |
|                                                        | :heavy_check_mark: IV_getcurrentWE2trace(npoints, rate, values) |
|                                                        | :heavy_check_mark: IV_getpotentialtrace(npoints, rate, values)  |
|                                                        | :heavy_check_mark: IV_we32setchannel(index)                     |
|                                                        | :heavy_check_mark: IV_we32setoffset(index, value)               |
|                                                        | :heavy_check_mark: IV_we32setoffsets(nval, values)              |
|                                                        | :heavy_check_mark: IV_we32getoffsets(nval, values)              |
|                                                        | :heavy_check_mark: IV_we32readcurrents(values)                  |
| :heavy_check_mark: load_method(str)                    | :heavy_check_mark: IV_readmethod(fname)                         |
| :heavy_check_mark: save_method(str)                    | :heavy_check_mark: IV_savemethod(fname)                         |
| :heavy_check_mark: start_method(str)                   | :heavy_check_mark: IV_startmethod(fname)                        |
| :heavy_check_mark: abort_method()                      | :heavy_check_mark: IV_abort()                                   |
| :heavy_check_mark: save_data(str)                      | :heavy_check_mark: IV_savedata(fname)                           |
| :heavy_check_mark: set_method_parameter(str, str)      | :heavy_check_mark: IV_setmethodparameter(parname, parvalue)     |
| :heavy_check_mark: get_available_data_points_number()  | :heavy_check_mark: IV_Ndatapoints(value)                        |
| :heavy_check_mark: get_data_point(int)                 | :heavy_check_mark: IV_getdata(pointnr, x, y, z)                 |
| :heavy_check_mark: get_data_point_from_scan(int, int)  | :heavy_check_mark: IV_getdatafromline(pointnr, scannr, x, y, z) |
|                                                        | :heavy_check_mark: IV_getDbFileName(fname)                      |
|                                                        | :small_orange_diamond: IV_StatusParGet(value)                   |
|                                                        | :small_orange_diamond: IV_StatusParSet(value)                   |
|                                                        | :small_orange_diamond: IV_UpdateTemperature(value)              |

## Tools Methods
| Tools Methods (DataProcessing)                   | Description                                                     |
| ------------------------------------------------ | --------------------------------------------------------------- |
| :heavy_check_mark: export_to_csv(data,file_path) |Saves data on a .csv file                                            |
| :heavy_check_mark: get_idf_data(idf_path)        |Extracts the primary data from a ivium .idf file and returns a lits of points (data matrix) |
| :heavy_check_mark: get_all_idf_data(idf_path)    |Extracts all data (primary and extra data) from a ivium .idf file and returns a data dictionary |
| :heavy_check_mark: convert_idf_to_csv(idf_path)  |Extracts the data from a ivium .idf file and saves the data to a .csv file |
| :heavy_check_mark: convert_idf_dir_to_csv(idf_dir_path='.')  |Extracts the data of all .idf files on a directory and saves the data to .csv files |