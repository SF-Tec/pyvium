from .base import CHAR_ARRAY, LONG_PTR, UTF_ENCODING, Base, ffi

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
""")


class GenericFunctions(Base):
    @staticmethod
    def IV_open() -> int:
        '''Open the driver to manipulate the Ivium software'''
        Base.set_driver_open(True)
        return Base.get_lib().IV_open()

    @staticmethod
    def IV_close() -> int:
        '''Closes the iviumSoft driver'''
        Base.set_driver_open(False)
        return Base.get_lib().IV_close()

    @staticmethod
    def IV_MaxDevices() -> int:
        '''Returns the maximum number of devices that can be managed by IviumSoft'''
        return Base.get_lib().IV_MaxDevices()

    @staticmethod
    def IV_selectdevice(iviumsoft_instance_number: int = 1) -> tuple[int, int]:
        '''It allows to select one instance of the currently running IviumSoft instances'''
        instance_number_ptr = ffi.new(LONG_PTR, iviumsoft_instance_number)
        result_code = Base.get_lib().IV_selectdevice(instance_number_ptr)
        return result_code, instance_number_ptr[0]

    @staticmethod
    def IV_getdevicestatus() -> int:
        '''It returns -1 (no IviumSoft), 0 (not connected), 1 (available_idle), 2 (available_busy),
            3 (no device available)'''
        return Base.get_lib().IV_getdevicestatus()

    @staticmethod
    def IV_readSN() -> tuple[int, str]:
        '''Returns the serial number of the currently selected device'''
        device_serial_number_ptr = ffi.new(CHAR_ARRAY, 16)
        result_code = Base.get_lib().IV_readSN(device_serial_number_ptr)
        return result_code, ffi.string(device_serial_number_ptr).decode(UTF_ENCODING)

    @staticmethod
    def IV_connect(connection_status: int) -> tuple[int, int]:
        '''It connects the currently selected device'''
        connection_status_ptr = ffi.new(LONG_PTR, connection_status)
        result_code = Base.get_lib().IV_connect(connection_status_ptr)
        return result_code, connection_status_ptr[0]

    @staticmethod
    def IV_VersionHost(version_host: int) -> tuple[int, int]:
        '''REVISE!!! Returns the version Host'''
        version_host_ptr = ffi.new(LONG_PTR, version_host)
        result_code = Base.get_lib().IV_VersionHost(version_host_ptr)
        return result_code, version_host_ptr[0]

    @staticmethod
    def IV_VersionDll() -> int:
        '''Returns the version of the IviumSoft dll'''
        return Base.get_lib().IV_VersionDll()

    @staticmethod
    def IV_VersionCheck() -> int:
        '''It returns 1 if the selected instance of IviumSoft is running'''
        return Base.get_lib().IV_VersionCheck()

    @staticmethod
    def IV_HostHandle() -> int:
        '''REVISE!!! Returns Host Handle'''
        return Base.get_lib().IV_HostHandle()

    @staticmethod
    def IV_VersionDllFile() -> int:
        '''REVISE!!! Returns DLL file version'''
        return Base.get_lib().IV_VersionDllFile()

    @staticmethod
    def IV_VersionDllFileStr() -> str:
        '''REVISE!!! Returns DLL file version str'''
        return Base.get_lib().IV_VersionDllFileStr()

    @staticmethod
    def IV_SelectChannel(channel_number: int) -> int:
        '''Sending the integer value communicates with Multichannel control:
            if not yet active, the [int] number of tabs is automatically opened and the [int] tab becomes active;
            if Ivium-n-Soft is active already, the [int] tab becomes active. 
            Now the channel/instrument that is connected to this tab can be controlled. 
            If no instrument is connected, the next available instrument in the list can be connected (IV_connect) and controlled.'''
        channel_number_ptr = ffi.new(LONG_PTR, channel_number)
        result_code = Base.get_lib().IV_SelectChannel(channel_number_ptr)
        return result_code
