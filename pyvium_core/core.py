'''This module is a simple wrapper around the "Software development driver DLL" for IviumSoft.'''
from dataclasses import dataclass
from os import path
from sys import maxsize, modules
from cffi import FFI

ffi = FFI()
ffi.cdef("""
    long __stdcall IV_open();
    long __stdcall IV_close();
    long __stdcall IV_MaxDevices();
    long __stdcall IV_selectdevice(long *devnr);
    long __stdcall IV_getdevicestatus();
    long __stdcall IV_readSN(char *sntext);
    long __stdcall IV_connect(long* devconnect);
    long __stdcall IV_VersionHost(long *version);
    long __stdcall IV_VersionDll();
    long __stdcall IV_VersionCheck();
    long __stdcall IV_HostHandle();
    long __stdcall IV_VersionDllFile();
    long __stdcall IV_VersionDllFileStr();
    long __stdcall IV_SelectChannel(long *channel);
    
    long __stdcall IV_getcellstatus(long *devcellstatus);
    long __stdcall IV_setconnectionmode(long *value);
    long __stdcall IV_setcellon(long *cellon);
    long __stdcall IV_setpotential(double *value);
    long __stdcall IV_setpotentialWE2(double *value);
    long __stdcall IV_setcurrent(double *value);
    long __stdcall IV_getpotential(double *value);
    long __stdcall IV_setcurrentrange(long *value);
    long __stdcall IV_setcurrentrangeWE2(long *value);
    long __stdcall IV_getcurrent(double *value);
    long __stdcall IV_getcurrentWE2(double *value);
    long __stdcall IV_setfilter(long *value);
    long __stdcall IV_setstability(long *value);
    long __stdcall IV_setbistatmode(long *value);
    long __stdcall IV_setdac(long *channr, double *value);
    long __stdcall IV_getadc(long *channr, double *value);
    long __stdcall IV_setmuxchannel(long *value);
    long __stdcall IV_setdigout(long *value);
    long __stdcall IV_getdigin(long *value);
    long __stdcall IV_setfrequency(double *value);
    long __stdcall IV_setamplitude(double *value);
    long __stdcall IV_getcurrenttrace(long* npoints, double *rate, double *values);
    long __stdcall IV_getcurrentWE2trace(long* npoints, double *rate, double *values);
    long __stdcall IV_getpotentialtrace(long* npoints, double *rate, double *values);

    long __stdcall IV_we32setchannel(long *index);
    long __stdcall IV_we32setoffset(long *index, double *value);
    long __stdcall IV_we32setoffsets(long *nval, double *values);
    long __stdcall IV_we32getoffsets(long *nval, double *values);
    long __stdcall IV_we32readcurrents(double *values);

    long __stdcall IV_readmethod(char *fname);
    long __stdcall IV_savemethod(char *fname);
    long __stdcall IV_startmethod(char *fname);
    long __stdcall IV_abort();
    long __stdcall IV_savedata(char *fname);
    long __stdcall IV_setmethodparameter(char *parname, char *parvalue);
    long __stdcall IV_Ndatapoints(long *value);
    long __stdcall IV_getdata(long *pointnr, double *x, double *y, double *z);
    long __stdcall IV_getdatafromline(long *pointnr, long *scannr, double *x, double *y, double *z);

    long __stdcall IV_getDbFileName(char *fname);
""")

MODULE_DIRECTORY = path.dirname(modules["pyvium_core"].__file__)

IVIUM_DLL_PATH = path.join(MODULE_DIRECTORY, "Ivium_remdriver64.dll")

if maxsize <= 2**32:
    IVIUM_DLL_PATH = path.join(MODULE_DIRECTORY, "Ivium_remdriver.dll")


@dataclass
class Core:
    '''Represents an execution of the Pyvium module'''
    _lib = ffi.dlopen(IVIUM_DLL_PATH)

    # Deleting (Calling destructor)
    def __del__(self):
        ffi.dlclose(self._lib)

    def IV_open(self):
        '''Open the driver to manipulate the Ivium software'''
        return self._lib.IV_open()

    def IV_close(self):
        '''Closes the iviumSoft driver'''
        return self._lib.IV_close()

    def IV_MaxDevices(self):
        '''Returns the maximum number of devices that can be managed by IviumSoft'''
        return self._lib.IV_MaxDevices()

    def IV_readSN(self):
        '''Returns the serial number of the currently selected device'''
        device_serial_number_ptr = ffi.new("char[]", 16)
        result_code = self._lib.IV_readSN(device_serial_number_ptr)

        return result_code, ffi.string(device_serial_number_ptr).decode("utf-8")

    def IV_selectdevice(self, iviumsoft_instance_number):
        '''It allows to select one instance of the currently running IviumSoft instances'''
        instance_number_ptr = ffi.new("long *", iviumsoft_instance_number)
        result_code = self._lib.IV_selectdevice(instance_number_ptr)

        return result_code,instance_number_ptr[0]

    def IV_connect(self,connection_status):
        '''It connects the currently selected device'''
        connection_status_ptr = ffi.new("long *", connection_status)
        result_code=self._lib.IV_connect(connection_status_ptr)
        return result_code, connection_status_ptr[0]


    def IV_VersionDll(self):
        '''Returns the version of the IviumSoft dll'''
        return self._lib.IV_VersionDll()

    def IV_VersionCheck(self):
        '''It returns 1 if, at least, one instance of IviumSoft is running'''
        return self._lib.IV_VersionCheck()

    def IV_getdevicestatus(self):
        '''It returns -1 (no IviumSoft), 0 (not connected), 1 (available_idle), 2 (available_busy),
        3 (no device available)'''
        return self._lib.IV_getdevicestatus()

    def IV_Ndatapoints(self):
        '''Returns actual available number of datapoints: indicates the progress during a run'''
        data_point_ptr = ffi.new("long *")
        result_code = self._lib.IV_Ndatapoints(data_point_ptr)
        return result_code, data_point_ptr[0]

    def IV_getdata(self, data_point_index):
        '''Get the data from a datapoint with index int, returns 3 values that depend on
        the used technique. For example LSV/CV methods return (E/I/0) Transient methods
        return (time/I,E/0), Impedance methods return (Z1,Z2,freq) etc.'''
        selected_data_point_index_ptr = ffi.new("long *", data_point_index)
        measured_value1_ptr = ffi.new("double *")
        measured_value2_ptr = ffi.new("double *")
        measured_value3_ptr = ffi.new("double *")

        result_code = self._lib.IV_getdata(
            selected_data_point_index_ptr, measured_value1_ptr, measured_value2_ptr, measured_value3_ptr)

        return result_code, measured_value1_ptr[0], measured_value2_ptr[0], measured_value3_ptr[0]

    def IV_getdatafromline(self, data_point_index, scan_index):
        '''Same as get_data_point, but with the additional scan_index parameter.
        This function will allow reading data from non-selected (previous) scans.'''
        selected_data_point_index_ptr = ffi.new("long *", data_point_index)
        selected_line_index_ptr = ffi.new("long *", scan_index)
        measured_value1_ptr = ffi.new("double *")
        measured_value2_ptr = ffi.new("double *")
        measured_value3_ptr = ffi.new("double *")

        result_code = self._lib.IV_getdatafromline(
            selected_data_point_index_ptr,
            selected_line_index_ptr,
            measured_value1_ptr,
            measured_value2_ptr,
            measured_value3_ptr)

        return result_code, measured_value1_ptr[0], measured_value2_ptr[0], measured_value3_ptr[0]

    def IV_getcellstatus(self):
        '''Returns cell status labels
        ["I_ovl", "Anin1_ovl","E_ovl", "CellOff_button pressed", "Cell on"]'''
        cell_status_ptr = ffi.new("long *")
        result_code = self._lib.IV_getcellstatus(cell_status_ptr)
        return result_code,cell_status_ptr[0]

    def IV_readmethod(self, method_file_path):
        '''Loads method procedure previously saved to a file.
        method_file_path represents the full path to the file.'''
        method_file_path_ptr = ffi.new(
            "char []", method_file_path.encode("utf-8"))
        result_code = self._lib.IV_readmethod(method_file_path_ptr)

        return result_code, ffi.string(method_file_path_ptr).decode("utf-8")

    def IV_savemethod(self, method_file_path):
        '''Saves currently loaded method procedure to a file.
        method_file_path represents the full path to the new file.'''
        method_file_path_ptr = ffi.new(
            "char []", method_file_path.encode("utf-8"))

        result_code = self._lib.IV_savemethod(method_file_path_ptr)

        return result_code, ffi.string(method_file_path_ptr).decode("utf-8")

    def IV_startmethod(self, method_file_path=''):
        '''Starts a method procedure.
        If method_file_path is an empty string then the presently loaded procedure is started.
        If the full path to a previously saved method is provided
        then the procedure is loaded from the file and started.'''
        method_file_path_ptr = ffi.new(
            "char []", method_file_path.encode("utf-8"))

        result_code = self._lib.IV_startmethod(method_file_path_ptr)

        return result_code, ffi.string(method_file_path_ptr).decode("utf-8")

    def IV_savedata(self, method_data_file_path):
        '''Saves the results of the last method execution into a file.
        method_file_path represents the full path to the new file.'''
        method_data_file_path_ptr = ffi.new(
            "char []", method_data_file_path.encode("utf-8"))

        result_code = self._lib.IV_savedata(method_data_file_path_ptr)

        return result_code, ffi.string(method_data_file_path_ptr).decode("utf-8")

    def IV_abort(self):
        '''Aborts the ongoing method procedure'''
        return self._lib.IV_abort()


    def IV_setmethodparameter(self, parameter_name, parameter_value):
        '''Allows updating the parameter values for the currently loaded method procedrue.
        It only works for text based parameters and dropdowns (multiple option selectors).'''
        parameter_name_ptr = ffi.new("char []", parameter_name.encode("utf-8"))
        parameter_value_ptr = ffi.new(
            "char []", parameter_value.encode("utf-8"))

        result_code = self._lib.IV_setmethodparameter(
            parameter_name_ptr, parameter_value_ptr)

        return result_code

    def IV_setconnectionmode(self, connection_mode_number):
        ''' Select the connection mode for the currently connected device.
        The available modes depend on the connected device.
        These are all the supported connection modes: 0=off; 1=EStat4EL(default), 2=EStat2EL,
        3=EstatDummy1,4=EStatDummy2,5=EstatDummy3,6=EstatDummy4
        7=Istat4EL, 8=Istat2EL, 9=IstatDummy, 10=BiStat4EL, 11=BiStat2EL'''
        connection_mode_number_ptr = ffi.new("long *", connection_mode_number)
        result_code = self._lib.IV_setconnectionmode(
            connection_mode_number_ptr)

        return result_code
    
    def IV_setcellon(self,cell_on_mode_number):
        '''Set cell on off to close cell relais (0=off;1=on), same as IV_setconnectionmode'''
        cell_on_mode_number_ptr = ffi.new("long *", cell_on_mode_number)
        result_code = self._lib.IV_setconnectionmode(
            cell_on_mode_number_ptr)

        return result_code

    def IV_getcurrenttrace(self, points_quantity, interval_rate):
        '''Returns a sequence of measured currents at defined samplingrate
        (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        points_quantity_ptr = ffi.new("long *", points_quantity)
        interval_rate_ptr = ffi.new("double *", interval_rate)
        result_ptr = ffi.new("double *")
        result_code = self._lib.IV_getcurrenttrace(
            points_quantity_ptr, interval_rate_ptr, result_ptr)

        return result_code, result_ptr[0]

    def IV_getcurrentWE2trace(self, points_quantity, interval_rate):
        '''Returns a sequence of measured WE2 currents at defined samplingrate
        (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        points_quantity_ptr = ffi.new("long *", points_quantity)
        interval_rate_ptr = ffi.new("double *", interval_rate)
        result_ptr = ffi.new("double *")

        result_code = self._lib.IV_getcurrentWE2trace(
            points_quantity_ptr, interval_rate_ptr, result_ptr)

        return result_code, result_ptr[0]

    def IV_getpotentialtrace(self, points_quantity, interval_rate):
        '''Returns a sequence of measured potentials at defined samplingrate
        (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        points_quantity_ptr = ffi.new("long *", points_quantity)
        interval_rate_ptr = ffi.new("double *", interval_rate)
        result_ptr = ffi.new("double *")

        result_code = self._lib.IV_getpotentialtrace(
            points_quantity_ptr, interval_rate_ptr, result_ptr)

        return result_code, result_ptr[0]
