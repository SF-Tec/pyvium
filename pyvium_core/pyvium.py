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

    long __stdcall IV_StatusParGet(long *value);
    long __stdcall IV_StatusParSet(long *value);
""")

MODULE_DIRECTORY = path.dirname(modules["pyvium_core"].__file__)

IVIUM_DLL_PATH = path.join(MODULE_DIRECTORY, "Ivium_remdriver64.dll")

if maxsize <= 2**32:
    IVIUM_DLL_PATH = path.join(MODULE_DIRECTORY, "Ivium_remdriver.dll")

@dataclass
class Pyvium:
    '''Represents an execution of the Pyvium module'''
    _lib = ffi.dlopen(IVIUM_DLL_PATH)

    # Deleting (Calling destructor)
    def __del__(self):
        ffi.dlclose(self._lib)

    def open_driver(self):
        '''Open the driver to manipulate the Ivium software'''
        return self._lib.IV_open()

    def close_driver(self):
        '''Closes the iviumSoft driver'''
        return self._lib.IV_close()

    def get_max_device_number(self):
        '''Returns the maximum number of devices that can be managed by IviumSoft'''
        return self._lib.IV_MaxDevices()

    def get_device_serial_number(self):
        '''Returns the serial number of the currently selected device'''
        device_serial_number = ffi.new("char[]", 16)
        result_code = self._lib.IV_readSN(device_serial_number)

        return result_code, ffi.string(device_serial_number).decode("utf-8")

    def select_iviumsoft_instance(self, iviumsoft_instance_number):
        '''It allows to select one instance of the currently running IviumSoft instances'''
        instance_number = ffi.new("long *", iviumsoft_instance_number)
        result_code = self._lib.IV_selectdevice(instance_number)

        return result_code

    def connect_device(self):
        '''It connects the currently selected device'''
        connection_on = ffi.new("long *", 1)
        return self._lib.IV_connect(connection_on)

    def disconnect_device(self):
        '''It disconnects the currently selected device'''
        connection_off = ffi.new("long *", 0)
        return self._lib.IV_connect(connection_off)

    def get_dll_version(self):
        '''Returns the version of the IviumSoft dll'''
        return self._lib.IV_VersionDll()

    def is_iviumsoft_running(self):
        '''It returns true if, at least, one instance of IviumSoft is running'''
        return self._lib.IV_VersionCheck() == 1
