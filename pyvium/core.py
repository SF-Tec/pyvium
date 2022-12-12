'''This module is a simple wrapper around the "Software development driver DLL" for IviumSoft.'''
from cffi import FFI
from .util import get_ivium_dll_path

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

IVIUM_DLL_PATH = get_ivium_dll_path()


class Core:
    '''Represents an execution of the Pyvium module'''
    __is_driver_open = False
    __lib = ffi.dlopen(IVIUM_DLL_PATH)

    ###########################
    #### GENERIC FUNCTIONS ####
    ###########################

    @staticmethod
    def IV_open() -> int:
        '''Open the driver to manipulate the Ivium software'''
        Core.__is_driver_open = True
        return Core.__lib.IV_open()

    @staticmethod
    def IV_close() -> int:
        '''Closes the iviumSoft driver'''
        Core.__is_driver_open = False
        return Core.__lib.IV_close()

    @staticmethod
    def is_driver_open() -> int:
        return Core.__is_driver_open

    @staticmethod
    def IV_MaxDevices() -> int:
        '''Returns the maximum number of devices that can be managed by IviumSoft'''
        return Core.__lib.IV_MaxDevices()

    @staticmethod
    def IV_selectdevice(iviumsoft_instance_number: int = 1) -> tuple[int, int]:
        '''It allows to select one instance of the currently running IviumSoft instances'''
        instance_number_ptr = ffi.new("long *", iviumsoft_instance_number)
        result_code = Core.__lib.IV_selectdevice(instance_number_ptr)
        return result_code, instance_number_ptr[0]

    @staticmethod
    def IV_getdevicestatus() -> int:
        '''It returns -1 (no IviumSoft), 0 (not connected), 1 (available_idle), 2 (available_busy),
            3 (no device available)'''
        return Core.__lib.IV_getdevicestatus()

    @staticmethod
    def IV_readSN() -> tuple[int, str]:
        '''Returns the serial number of the currently selected device'''
        device_serial_number_ptr = ffi.new("char[]", 16)
        result_code = Core.__lib.IV_readSN(device_serial_number_ptr)
        return result_code, ffi.string(device_serial_number_ptr).decode("utf-8")

    @staticmethod
    def IV_connect(connection_status: int) -> tuple[int, int]:
        '''It connects the currently selected device'''
        connection_status_ptr = ffi.new("long *", connection_status)
        result_code = Core.__lib.IV_connect(connection_status_ptr)
        return result_code, connection_status_ptr[0]

    @staticmethod
    def IV_VersionHost(version_host: int) -> tuple[int, int]:
        '''REVISE!!! Returns the version Host'''
        version_host_ptr = ffi.new("long *", version_host)
        result_code = Core.__lib.IV_VersionHost(version_host_ptr)
        return result_code, version_host_ptr[0]

    @staticmethod
    def IV_VersionDll() -> int:
        '''Returns the version of the IviumSoft dll'''
        return Core.__lib.IV_VersionDll()

    @staticmethod
    def IV_VersionCheck() -> int:
        '''It returns 1 if the selected instance of IviumSoft is running'''
        return Core.__lib.IV_VersionCheck()

    @staticmethod
    def IV_HostHandle() -> int:
        '''REVISE!!! Returns Host Handle'''
        return Core.__lib.IV_HostHandle()

    @staticmethod
    def IV_VersionDllFile() -> int:
        '''REVISE!!! Returns DLL file version'''
        return Core.__lib.IV_VersionDllFile()

    @staticmethod
    def IV_VersionDllFileStr() -> str:
        '''REVISE!!! Returns DLL file version str'''
        return Core.__lib.IV_VersionDllFileStr()

    @staticmethod
    def IV_SelectChannel(chanel_number: int) -> int:
        '''Sending the integer value communicates with Multichannel control:
            if not yet active, the [int] number of tabs is automatically opened and the [int] tab becomes active;
            if Ivium-n-Soft is active already, the [int] tab becomes active. 
            Now the channel/instrument that is connected to this tab can be controlled. 
            If no instrument is connected, the next available instrument in the list can be connected (IV_connect) and controlled.'''
        chanel_number_ptr = ffi.new("long *", chanel_number)
        result_code = Core.__lib.IV_SelectChannel(chanel_number_ptr)
        return result_code

    ###############################
    #### DIRECT MODE FUNCTIONS ####
    ###############################

    @staticmethod
    def IV_getcellstatus() -> tuple[int, int]:
        '''Returns cell status labels
            ["I_ovl", "Anin1_ovl","E_ovl", "CellOff_button pressed", "Cell on"]'''
        cell_status_ptr = ffi.new("long *")
        result_code = Core.__lib.IV_getcellstatus(cell_status_ptr)
        return result_code, cell_status_ptr[0]

    @staticmethod
    def IV_setconnectionmode(connection_mode_number: int) -> int:
        ''' Select the connection mode for the currently connected device.
            The available modes depend on the connected device.
            These are all the supported connection modes: 0=off; 1=EStat4EL(default), 2=EStat2EL,
            3=EstatDummy1,4=EStatDummy2,5=EstatDummy3,6=EstatDummy4
            7=Istat4EL, 8=Istat2EL, 9=IstatDummy, 10=BiStat4EL, 11=BiStat2EL'''
        connection_mode_number_ptr = ffi.new("long *", connection_mode_number)
        result_code = Core.__lib.IV_setconnectionmode(
            connection_mode_number_ptr)
        return result_code

    @staticmethod
    def IV_setcellon(cell_on_mode_number: int) -> int:
        '''Set cell on off to close cell relais (0=off;1=on)'''
        cell_on_mode_number_ptr = ffi.new("long *", cell_on_mode_number)
        result_code = Core.__lib.IV_setcellon(
            cell_on_mode_number_ptr)
        return result_code

    @staticmethod
    def IV_setpotential(potential_value: float) -> int:
        '''Set cell potential'''
        potential_value_ptr = ffi.new("double *", potential_value)
        result_code = Core.__lib.IV_setpotential(potential_value_ptr)
        return result_code

    @staticmethod
    def IV_setpotentialWE2(potential_we2_value: float) -> int:
        '''Set BiStat offset potential'''
        potential_we2_value_ptr = ffi.new("double *", potential_we2_value)
        result_code = Core.__lib.IV_setpotentialWE2(potential_we2_value_ptr)
        return result_code

    @staticmethod
    def IV_setcurrent(current_value: float) -> int:
        '''Set cell current (galvanostatic mode)'''
        current_value_ptr = ffi.new("double *", current_value)
        result_code = Core.__lib.IV_setpotentialWE2(current_value_ptr)
        return result_code

    @staticmethod
    def IV_getpotential() -> tuple[int, float]:
        '''Returns measured potential'''
        potential_value_ptr = ffi.new("double *")
        result_code = Core.__lib.IV_getpotential(potential_value_ptr)
        return result_code, potential_value_ptr[0]

    @staticmethod
    def IV_setcurrentrange(current_range_number: int) -> int:
        '''Set current range, 0=10A, 1=1A, etc,'''
        current_range_number_ptr = ffi.new("long *", current_range_number)
        result_code = Core.__lib.IV_setcurrentrange(current_range_number_ptr)
        return result_code

    @staticmethod
    def IV_setcurrentrangeWE2(current_range_number: int) -> int:
        '''Set current range for BiStat, 0=10mA, 1=1mA, etc,'''
        current_range_number_ptr = ffi.new("long *", current_range_number)
        result_code = Core.__lib.IV_setcurrentrangeWE2(
            current_range_number_ptr)
        return result_code

    @staticmethod
    def IV_getcurrent() -> tuple[int, float]:
        '''Returns measured current'''
        current_value_ptr = ffi.new("double *")
        result_code = Core.__lib.IV_getcurrent(current_value_ptr)
        return result_code, current_value_ptr[0]

    @staticmethod
    def IV_getcurrentWE2() -> tuple[int, float]:
        '''Returns measured current from WE2 (bipotentiostat)'''
        current_value_ptr = ffi.new("double *")
        result_code = Core.__lib.IV_getcurrentWE2(current_value_ptr)
        return result_code, current_value_ptr[0]

    @staticmethod
    def IV_setfilter(filter_number: int) -> int:
        '''Set filter, for int :0=1MHz, 1=100kHz, 2=10kHz, 3=1kHz, 4=10Hz'''
        filter_number_ptr = ffi.new("long *", filter_number)
        result_code = Core.__lib.IV_setfilter(filter_number_ptr)
        return result_code

    @staticmethod
    def IV_setstability(stability_number: int) -> int:
        '''Set stability, for int 0=HighSpeed, 1=Standard, 2=HighStability'''
        stability_number_ptr = ffi.new("long *", stability_number)
        result_code = Core.__lib.IV_setstability(stability_number_ptr)
        return result_code

    @staticmethod
    def IV_setbistatmode(value: int) -> int:
        '''REVISE! --> IV_bistat_mode(int) in documentation
            Select mode for BiStat, for int 0=standard, 1=scanning
            This bistat_mode function also can be used to control the Automatic E-ranging function of the instrument;
            0=AutoEranging off; 1=AutoEranging on'''
        value_ptr = ffi.new("long *", value)
        result_code = Core.__lib.IV_setstability(value_ptr)
        return result_code

    @staticmethod
    def IV_setdac(channel_number: int, value: float) -> int:
        '''Set dac on external port, int=0 for dac1, int=1 for dac2'''
        channel_number_ptr = ffi.new("long *", channel_number)
        value_ptr = ffi.new("double *", value)
        result_code = Core.__lib.IV_setdac(channel_number_ptr, value_ptr)
        return result_code

    @staticmethod
    def IV_getadc(channel_number: int) -> tuple[int, int]:
        '''REVISE! Returns measured voltage on external ADC port, int=channelnr. 0-7'''
        channel_number_ptr = ffi.new("long *", channel_number)
        measured_voltage_ptr = ffi.new("double *")
        result_code = Core.__lib.IV_getdac(
            channel_number_ptr, measured_voltage_ptr)
        return result_code, measured_voltage_ptr[0]

    @staticmethod
    def IV_setmuxchannel(channel_number=0) -> int:
        '''Set channel of multiplexer, int=channelnr. starting from 0(default)'''
        channel_number_ptr = ffi.new("long *", channel_number)
        result_code = Core.__lib.IV_setmuxchannel(channel_number_ptr)
        return result_code

    @staticmethod
    def IV_setdigout(value: int) -> int:
        '''REVISE! Set digital lines on external port, int is bitmask'''
        value_ptr = ffi.new("long *", value)
        result_code = Core.__lib.IV_setdigout(value_ptr)
        return result_code

    @staticmethod
    def IV_getdigin() -> tuple[int, int]:
        '''REVISE! Returns status of digital inputs from external port, int is bitmask'''
        value_ptr = ffi.new("long *")
        result_code = Core.__lib.IV_getdigin(value_ptr)
        return result_code, value_ptr[0]

    @staticmethod
    def IV_setfrequency(frequency: float) -> int:
        frequency_ptr = ffi.new("double *", frequency)
        result_code: int = Core.__lib.IV_setfrequency(frequency_ptr)
        return result_code

    @staticmethod
    def IV_setamplitude(amplitude: float) -> int:
        amplitude_ptr = ffi.new("double *", amplitude)
        result_code: int = Core.__lib.IV_setamplitude(amplitude_ptr)
        return result_code

    @staticmethod
    def IV_getcurrenttrace(points_quantity: int, interval_rate: float) -> tuple[int, float]:
        '''Returns a sequence of measured currents at defined samplingrate
            (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        points_quantity_ptr = ffi.new("long *", points_quantity)
        interval_rate_ptr = ffi.new("double *", interval_rate)
        result_ptr = ffi.new("double *")
        result_code = Core.__lib.IV_getcurrenttrace(
            points_quantity_ptr, interval_rate_ptr, result_ptr)
        return result_code, result_ptr[0]

    @staticmethod
    def IV_getcurrentWE2trace(points_quantity: int, interval_rate: float) -> tuple[int, float]:
        '''Returns a sequence of measured WE2 currents at defined samplingrate
            (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        points_quantity_ptr = ffi.new("long *", points_quantity)
        interval_rate_ptr = ffi.new("double *", interval_rate)
        result_ptr = ffi.new("double *")
        result_code = Core.__lib.IV_getcurrentWE2trace(
            points_quantity_ptr, interval_rate_ptr, result_ptr)
        return result_code, result_ptr[0]

    @staticmethod
    def IV_getpotentialtrace(points_quantity: int, interval_rate: float) -> tuple[int, float]:
        '''Returns a sequence of measured potentials at defined samplingrate
            (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        points_quantity_ptr = ffi.new("long *", points_quantity)
        interval_rate_ptr = ffi.new("double *", interval_rate)
        result_ptr = ffi.new("double *")
        result_code = Core.__lib.IV_getpotentialtrace(
            points_quantity_ptr, interval_rate_ptr, result_ptr)
        return result_code, result_ptr[0]

    ########################
    #### WE32 FUNCTIONS ####
    ########################

    @staticmethod
    def IV_we32setchannel(channel_index: int) -> int:
        '''Select active WE32 channel (chan)'''
        channel_index_ptr = ffi.new("long *", channel_index)
        result_code = Core.__lib.IV_we32setchannel(channel_index_ptr)
        return result_code

    @staticmethod
    def IV_we32setoffset(channel_index: int, value: float) -> int:
        '''Set WE32 offset (chan,value), value -2 to +2V.
            Use chan=0 to apply the same offset to all channels.'''
        channel_index_ptr = ffi.new("long *", channel_index)
        value_ptr = ffi.new("double *", value)
        result_code = Core.__lib.IV_we32setoffset(channel_index_ptr, value_ptr)
        return result_code

    @staticmethod
    def IV_we32setoffsets(number_of_channels: int, value: float) -> int:
        '''REVISE! Set WE32 offsets values (Nchan,values),
            with Nchan the number of channels (1..32)'''
        number_of_channels_index_ptr = ffi.new("long *", number_of_channels)
        value_ptr = ffi.new("double *", value)
        result_code = Core.__lib.IV_we32setoffsets(
            number_of_channels_index_ptr, value_ptr)
        return result_code

    @staticmethod
    def IV_we32getoffsets(number_of_channels: int) -> tuple[int, float]:
        '''REVISE! Returns actual WE32 offset values (Nchan,values),
            with Nchan the number of channels (1..32)'''
        number_of_channels_index_ptr = ffi.new("long *", number_of_channels)
        values_ptr = ffi.new("double *")
        result_code = Core.__lib.IV_we32getoffsets(
            number_of_channels_index_ptr, values_ptr)
        return result_code, values_ptr[0]

    @staticmethod
    def IV_we32readcurrents() -> tuple[int, float]:
        '''REVISE! Returns array with 32 WE32 current values,
            that are measured simultaneously'''
        current_values_ptr = ffi.new("double *")
        result_code = Core.__lib.IV_we32readcurrents(current_values_ptr)
        return result_code, current_values_ptr[0]

    ###############################
    #### METHOD MODE FUNCTIONS ####
    ###############################

    @staticmethod
    def IV_readmethod(method_file_path: str) -> tuple[int, str]:
        '''Loads method procedure previously saved to a file.
            method_file_path represents the full path to the file.'''
        method_file_path_ptr = ffi.new(
            "char []", method_file_path.encode("utf-8"))
        result_code = Core.__lib.IV_readmethod(method_file_path_ptr)
        return result_code, ffi.string(method_file_path_ptr).decode("utf-8")

    @staticmethod
    def IV_savemethod(method_file_path: str) -> tuple[int, str]:
        '''Saves currently loaded method procedure to a file.
            method_file_path represents the full path to the new file.'''
        method_file_path_ptr = ffi.new(
            "char []", method_file_path.encode("utf-8"))
        result_code = Core.__lib.IV_savemethod(method_file_path_ptr)
        return result_code, ffi.string(method_file_path_ptr).decode("utf-8")

    @staticmethod
    def IV_startmethod(method_file_path='') -> tuple[int, str]:
        '''Starts a method procedure.
            If method_file_path is an empty string then the presently loaded procedure is started.
            If the full path to a previously saved method is provided
            then the procedure is loaded from the file and started.'''
        method_file_path_ptr = ffi.new(
            "char []", method_file_path.encode("utf-8"))
        result_code = Core.__lib.IV_startmethod(method_file_path_ptr)
        return result_code, ffi.string(method_file_path_ptr).decode("utf-8")

    @staticmethod
    def IV_abort() -> int:
        '''Aborts the ongoing method procedure'''
        return Core.__lib.IV_abort()

    @staticmethod
    def IV_savedata(method_data_file_path: str) -> tuple[int, str]:
        '''Saves the results of the last method execution into a file.
            method_file_path represents the full path to the new file.'''
        method_data_file_path_ptr = ffi.new(
            "char []", method_data_file_path.encode("utf-8"))
        result_code = Core.__lib.IV_savedata(method_data_file_path_ptr)
        return result_code, ffi.string(method_data_file_path_ptr).decode("utf-8")

    @staticmethod
    def IV_setmethodparameter(parameter_name: str, parameter_value: str) -> int:
        '''Allows updating the parameter values for the currently loaded method procedrue.
            It only works for text based parameters and dropdowns (multiple option selectors).'''
        parameter_name_ptr = ffi.new("char []", parameter_name.encode("utf-8"))
        parameter_value_ptr = ffi.new(
            "char []", parameter_value.encode("utf-8"))
        result_code = Core.__lib.IV_setmethodparameter(
            parameter_name_ptr, parameter_value_ptr)
        return result_code

    @staticmethod
    def IV_Ndatapoints() -> tuple[int, int]:
        '''Returns actual available number of datapoints: indicates the progress during a run'''
        data_point_ptr = ffi.new("long *")
        result_code = Core.__lib.IV_Ndatapoints(data_point_ptr)
        return result_code, data_point_ptr[0]

    @staticmethod
    def IV_getdata(data_point_index: int) -> tuple[int, float, float, float]:
        '''Get the data from a datapoint with index int, returns 3 values that depend on
            the used technique. For example LSV/CV methods return (E/I/0) Transient methods
            return (time/I,E/0), Impedance methods return (Z1,Z2,freq) etc.'''
        selected_data_point_index_ptr = ffi.new("long *", data_point_index)
        measured_value1_ptr = ffi.new("double *")
        measured_value2_ptr = ffi.new("double *")
        measured_value3_ptr = ffi.new("double *")
        result_code = Core.__lib.IV_getdata(
            selected_data_point_index_ptr, measured_value1_ptr, measured_value2_ptr, measured_value3_ptr)
        return result_code, measured_value1_ptr[0], measured_value2_ptr[0], measured_value3_ptr[0]

    @staticmethod
    def IV_getdatafromline(data_point_index: int, scan_index: int) -> tuple[int, float, float, float]:
        '''Same as get_data_point, but with the additional scan_index parameter.
            This function will allow reading data from non-selected (previous) scans.'''
        selected_data_point_index_ptr = ffi.new("long *", data_point_index)
        selected_line_index_ptr = ffi.new("long *", scan_index)
        measured_value1_ptr = ffi.new("double *")
        measured_value2_ptr = ffi.new("double *")
        measured_value3_ptr = ffi.new("double *")
        result_code = Core.__lib.IV_getdatafromline(
            selected_data_point_index_ptr,
            selected_line_index_ptr,
            measured_value1_ptr,
            measured_value2_ptr,
            measured_value3_ptr)
        return result_code, measured_value1_ptr[0], measured_value2_ptr[0], measured_value3_ptr[0]
