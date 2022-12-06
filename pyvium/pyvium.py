'''This module is a simple wrapper around the "Software development driver DLL" for IviumSoft.'''
from .core import Core

core = Core()


class Pyvium:

    def __init__(self):
        '''@@--> Se podría cerrar el driver de alguna manera externa?
            Returns:
                -1 no iviumsoft (but opends the driver anyway so you can call rest of the fn)
                 0 rest of cases (no device, device not conected, device connected, device bussy...)
       '''
        core.IV_open()  # Open the driver to manipulate the Ivium software

    # Deleting (Calling destructor)
    def __del__(self):
        '''@@--> Se podría cerrar el driver de alguna manera externa?
            Returns:
                crash if the driver is not open
                0 rest of cases (no device, device not conected, device connected, device bussy...)
       '''
        core.IV_close()  # Closes the iviumSoft driver

    def get_max_device_number(self):
        '''Returns the maximum number of devices that can be managed by IviumSoft'''
        '''Returns:
                crash if the driver is not open
                24 rest of cases (no device, device not conected, device connected, device bussy...)
       '''
        return core.IV_MaxDevices()

    def get_device_serial_number(self):
        '''Returns the serial number of the currently selected device'''
        '''Returns:
                crash if the driver is not open
                -1,'' --> no iviumsoft or driver opened with no iviumsoft
                0,'' --> not conected CompacStat/OctoStat..., no device (or driver opened with no device?, check with DemoStat)
                0,'sn' --> device not conected (at least for DemoStat), not working for CompacStat or OctoStat (at least)
                0,'sn' --> conected device (compacstat gives "BXXX" instead of "bXXX" when usb powered, Octostat gives "Oct-1"...)
       '''
        result_code, serial_number = core.IV_readSN()

        return result_code, serial_number

    def select_iviumsoft_instance(self, iviumsoft_instance_number):
        '''It allows to select one instance of the currently running IviumSoft instances'''
        result_code = core.IV_selectdevice(iviumsoft_instance_number)

        return result_code

    def connect_device(self):
        '''It connects the currently selected device'''
        return core.IV_connect(1)

    def disconnect_device(self):
        '''It disconnects the currently selected device'''
        return core.IV_connect(0)

    def get_dll_version(self):
        '''Returns the version of the IviumSoft dll'''
        return core.IV_VersionDll()

    def is_iviumsoft_running(self):
        '''It returns true if, at least, one instance of IviumSoft is running'''
        return core.IV_VersionCheck() == 1

    def get_device_status(self):
        '''It returns -1 (no IviumSoft), 0 (not connected), 1 (available_idle), 2 (available_busy),
        3 (no device available)'''
        return core.IV_getdevicestatus()

    def get_data_points_quantity(self):
        '''Returns actual available number of datapoints: indicates the progress during a run'''
        result_code, data_point = core.IV_Ndatapoints()

        return result_code, data_point

    def get_data_point(self, data_point_index):
        '''Get the data from a datapoint with index int, returns 3 values that depend on
        the used technique. For example LSV/CV methods return (E/I/0) Transient methods
        return (time/I,E/0), Impedance methods return (Z1,Z2,freq) etc.'''
        result_code, value1, value2, value3 = core.IV_getdata(
            data_point_index)

        return result_code, value1, value2, value3

    def get_data_point_from_scan(self, data_point_index, scan_index):
        '''Same as get_data_point, but with the additional scan_index parameter.
        This function will allow reading data from non-selected (previous) scans.'''
        result_code, value1, value2, value3 = core.IV_getdatafromline(
            data_point_index, scan_index)

        return result_code, value1, value2, value3

    def get_cell_status(self):
        '''Returns cell status labels
        ["I_ovl", "Anin1_ovl","E_ovl", "CellOff_button pressed", "Cell on"]'''
        result_code, cell_status_bits = core.IV_getcellstatus()
        cell_status_labels = []
        if result_code == 0:
            labels = ["I_ovl", "", "Anin1_ovl", "E_ovl",
                      "", "CellOff_button pressed", "Cell on"]
            for i, label in enumerate(labels, 2):
                if cell_status_bits & (1 << i) and label:
                    cell_status_labels.append(label)
        return result_code, cell_status_labels

    def load_method(self, method_file_path):
        '''Loads method procedure previously saved to a file.
        method_file_path represents the full path to the file.'''
        result_code, path = core.IV_readmethod(method_file_path)

        return result_code, path

    def save_method(self, method_file_path):
        '''Saves currently loaded method procedure to a file.
        method_file_path represents the full path to the new file.'''
        result_code, path = core.IV_savemethod(method_file_path)

        return result_code, path

    def start_method(self, method_file_path=''):
        '''Starts a method procedure.
        If method_file_path is an empty string then the presently loaded procedure is started.
        If the full path to a previously saved method is provided
        then the procedure is loaded from the file and started.'''
        result_code, path = core.IV_startmethod(method_file_path)

        return result_code, path

    def save_method_data(self, method_data_file_path):
        '''Saves the results of the last method execution into a file.
        method_file_path represents the full path to the new file.'''
        result_code, path = core.IV_savedata(method_data_file_path)

        return result_code, path

    def abort_method(self):
        '''Aborts the ongoing method procedure'''
        result_code = core.IV_abort()

        return result_code

    def set_method_parameter_value(self, parameter_name, parameter_value):
        '''Allows updating the parameter values for the currently loaded method procedrue.
        It only works for text based parameters and dropdowns (multiple option selectors).'''
        result_code = core.IV_setmethodparameter(
            parameter_name, parameter_value)

        return result_code

    def set_connection_mode(self, connection_mode_number):
        ''' Select the connection mode for the currently connected device.
        The available modes depend on the connected device.
        These are all the supported connection modes: 0=off; 1=EStat4EL(default), 2=EStat2EL,
        3=EstatDummy1,4=EStatDummy2,5=EstatDummy3,6=EstatDummy4
        7=Istat4EL, 8=Istat2EL, 9=IstatDummy, 10=BiStat4EL, 11=BiStat2EL'''
        result_code = core.IV_setconnectionmode(connection_mode_number)

        return result_code

    def get_current_trace(self, points_quantity, interval_rate):
        '''Returns a sequence of measured currents at defined samplingrate
        (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        result_code, current = core.IV_getcurrenttrace(
            points_quantity, interval_rate)

        return result_code, current

    def get_current_we2_trace(self, points_quantity, interval_rate):
        '''Returns a sequence of measured WE2 currents at defined samplingrate
        (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        result_code, current = core.IV_getcurrentWE2trace(
            points_quantity, interval_rate)

        return result_code, current

    def get_potencial_trace(self, points_quantity, interval_rate):
        '''Returns a sequence of measured potentials at defined samplingrate
        (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        result_code, potential = core.IV_getpotentialtrace(
            points_quantity, interval_rate)

        return result_code, potential

    def set_ac_amplitude(self, ac_amplitude):
        '''Set the value of the ac amplitude in Volts'''
        result_code, amplitude = core.IV_setamplitude(ac_amplitude)
        return result_code, amplitude

    def set_ac_frequency(self, ac_frequency):
        '''Set the value of the ac frequency in Hz'''
        result_code, frequency = core.IV_setfrequency(ac_frequency)
        return result_code, frequency
