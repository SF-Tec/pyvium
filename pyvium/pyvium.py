'''This module is a simple wrapper around the "Software development driver DLL" for IviumSoft.'''
from .core import Core


class Pyvium:

    @staticmethod
    def get_max_device_number():
        '''Returns the maximum number of devices that can be managed by IviumSoft'''
        '''Returns:
                    crash if the driver is not open
                    24 rest of cases (no device, device not conected, device connected, device bussy...)
        '''
        return Core.IV_MaxDevices()

    @staticmethod
    def get_device_serial_number():
        '''Returns the serial number of the currently selected device'''
        '''Returns:
                    crash if the driver is not open
                    -1,'' --> no iviumsoft or driver opened with no iviumsoft
                    0,'' --> not conected CompacStat/OctoStat..., no device (or driver opened with no device?, check with DemoStat)
                    0,'sn' --> device not conected (at least for DemoStat), not working for CompacStat or OctoStat (at least)
                    0,'sn' --> conected device (compacstat gives "BXXX" instead of "bXXX" when usb powered, Octostat gives "Oct-1"...)
        '''
        result_code, serial_number = Core.IV_readSN()

        return result_code, serial_number

    @staticmethod
    def select_iviumsoft_instance(iviumsoft_instance_number):
        '''It allows to select one instance of the currently running IviumSoft instances'''
        result_code = Core.IV_selectdevice(iviumsoft_instance_number)

        return result_code

    @staticmethod
    def connect_device():
        '''It connects the currently selected device'''
        return Core.IV_connect(1)

    @staticmethod
    def disconnect_device():
        '''It disconnects the currently selected device'''
        return Core.IV_connect(0)

    @staticmethod
    def get_dll_version():
        '''Returns the version of the IviumSoft dll'''
        return Core.IV_VersionDll()

    @staticmethod
    def is_iviumsoft_running():
        '''It returns true if, at least, one instance of IviumSoft is running'''
        return Core.IV_VersionCheck() == 1

    @staticmethod
    def get_device_status():
        '''It returns -1 (no IviumSoft), 0 (not connected), 1 (available_idle), 2 (available_busy),
            3 (no device available)'''
        return Core.IV_getdevicestatus()

    @staticmethod
    def get_data_points_quantity():
        '''Returns actual available number of datapoints: indicates the progress during a run'''
        result_code, data_point = Core.IV_Ndatapoints()

        return result_code, data_point

    @staticmethod
    def get_data_point(data_point_index):
        '''Get the data from a datapoint with index int, returns 3 values that depend on
            the used technique. For example LSV/CV methods return (E/I/0) Transient methods
            return (time/I,E/0), Impedance methods return (Z1,Z2,freq) etc.'''
        result_code, value1, value2, value3 = Core.IV_getdata(
            data_point_index)

        return result_code, value1, value2, value3

    @staticmethod
    def get_data_point_from_scan(data_point_index, scan_index):
        '''Same as get_data_point, but with the additional scan_index parameter.
            This function will allow reading data from non-selected (previous) scans.'''
        result_code, value1, value2, value3 = Core.IV_getdatafromline(
            data_point_index, scan_index)

        return result_code, value1, value2, value3

    @staticmethod
    def get_cell_status():
        '''Returns cell status labels
            ["I_ovl", "Anin1_ovl","E_ovl", "CellOff_button pressed", "Cell on"]'''
        result_code, cell_status_bits = Core.IV_getcellstatus()
        cell_status_labels = []
        if result_code == 0:
            labels = ["I_ovl", "", "Anin1_ovl", "E_ovl",
                    "", "CellOff_button pressed", "Cell on"]
            for i, label in enumerate(labels, 2):
                if cell_status_bits & (1 << i) and label:
                    cell_status_labels.append(label)
        return result_code, cell_status_labels


    @staticmethod
    def load_method( method_file_path):
        '''Loads method procedure previously saved to a file.
            method_file_path represents the full path to the file.'''
        result_code, path = Core.IV_readmethod(method_file_path)

        return result_code, path


    @staticmethod
    def save_method( method_file_path):
        '''Saves currently loaded method procedure to a file.
            method_file_path represents the full path to the new file.'''
        result_code, path = Core.IV_savemethod(method_file_path)

        return result_code, path


    @staticmethod
    def start_method( method_file_path=''):
        '''Starts a method procedure.
            If method_file_path is an empty string then the presently loaded procedure is started.
            If the full path to a previously saved method is provided
            then the procedure is loaded from the file and started.'''
        result_code, path = Core.IV_startmethod(method_file_path)

        return result_code, path


    @staticmethod
    def save_method_data( method_data_file_path):
        '''Saves the results of the last method execution into a file.
            method_file_path represents the full path to the new file.'''
        result_code, path = Core.IV_savedata(method_data_file_path)

        return result_code, path


    @staticmethod
    def abort_method():
        '''Aborts the ongoing method procedure'''
        result_code = Core.IV_abort()

        return result_code


    @staticmethod
    def set_method_parameter_value( parameter_name, parameter_value):
        '''Allows updating the parameter values for the currently loaded method procedrue.
            It only works for text based parameters and dropdowns (multiple option selectors).'''
        result_code = Core.IV_setmethodparameter(
            parameter_name, parameter_value)

        return result_code


    @staticmethod
    def set_connection_mode( connection_mode_number):
        ''' Select the connection mode for the currently connected device.
            The available modes depend on the connected device.
            These are all the supported connection modes: 0=off; 1=EStat4EL(default), 2=EStat2EL,
            3=EstatDummy1,4=EStatDummy2,5=EstatDummy3,6=EstatDummy4
            7=Istat4EL, 8=Istat2EL, 9=IstatDummy, 10=BiStat4EL, 11=BiStat2EL'''
        result_code = Core.IV_setconnectionmode(connection_mode_number)

        return result_code


    @staticmethod
    def get_current_trace( points_quantity, interval_rate):
        '''Returns a sequence of measured currents at defined samplingrate
            (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        result_code, current = Core.IV_getcurrenttrace(
            points_quantity, interval_rate)

        return result_code, current


    @staticmethod
    def get_current_we2_trace( points_quantity, interval_rate):
        '''Returns a sequence of measured WE2 currents at defined samplingrate
            (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        result_code, current = Core.IV_getcurrentWE2trace(
            points_quantity, interval_rate)

        return result_code, current


    @staticmethod
    def get_potencial_trace( points_quantity, interval_rate):
        '''Returns a sequence of measured potentials at defined samplingrate
            (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        result_code, potential = Core.IV_getpotentialtrace(
            points_quantity, interval_rate)

        return result_code, potential


    @staticmethod
    def set_ac_amplitude( ac_amplitude):
        '''Set the value of the ac amplitude in Volts'''
        result_code, amplitude = Core.IV_setamplitude(ac_amplitude)
        return result_code, amplitude


    @staticmethod
    def set_ac_frequency( ac_frequency):
        '''Set the value of the ac frequency in Hz'''
        result_code, frequency = Core.IV_setfrequency(ac_frequency)
        return result_code, frequency
