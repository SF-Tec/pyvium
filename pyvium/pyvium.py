'''This module is a simple wrapper around the "Software development driver DLL" for IviumSoft.'''
from .core import Core
from .pyvium_verifiers import PyviumVerifiers
from .errors import DeviceNotConnectedToIviumSoftError, IviumSoftNotRunningError


class Pyvium:
    '''Represents an execution of the Pyvium module'''

    ###########################
    #### GENERIC FUNCTIONS ####
    ###########################

    @staticmethod
    def open_driver():
        '''Open the driver to manipulate the Ivium software'''
        if Core.is_driver_open():
            Core.IV_close()
        Core.IV_open()
        try:
            PyviumVerifiers.verify_iviumsoft_is_running()
        except:
            Core.IV_close()
            raise

    @staticmethod
    def close_driver():
        '''Closes the iviumSoft driver'''
        PyviumVerifiers.verify_driver_is_open()
        Core.IV_close()

    @staticmethod
    def get_max_device_number():
        '''Returns the maximum number of devices that can be managed by IviumSoft'''
        PyviumVerifiers.verify_driver_is_open()
        return Core.IV_MaxDevices()

    @staticmethod
    def get_device_status() -> tuple[int, str]:
        '''It returns -1 (no IviumSoft), 0 (not connected), 1 (available_idle), 2 (available_busy),
            3 (no device available)'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()
        status_labels = {
            '-1': 'no IviumSoft',
            '0': 'connected',
            '1': 'available_idle',
            '2': 'available_busy',
            '3': 'no device available'
        }
        result_code = Core.IV_getdevicestatus()
        return result_code, status_labels[str(result_code)]

    @staticmethod
    def is_iviumsoft_running() -> bool:
        '''It returns true if if the selected instance of IviumSoft is running'''
        PyviumVerifiers.verify_driver_is_open()
        return not Core.IV_getdevicestatus() == -1

    @staticmethod
    def get_active_iviumsoft_instances():
        '''Returns a list of active(opened) IviumSoft instances'''
        PyviumVerifiers.verify_driver_is_open()
        active_instances = []
        first_active_instance_number = 0
        for instance_number in range(1, 32):
            Core.IV_selectdevice(instance_number)

            if not Core.IV_getdevicestatus() == -1:
                active_instances.append(instance_number)

                if first_active_instance_number == 0:
                    first_active_instance_number = instance_number

        if first_active_instance_number == 0:
            first_active_instance_number = 1

        Core.IV_selectdevice(first_active_instance_number)
        return active_instances

    @staticmethod
    def select_iviumsoft_instance(iviumsoft_instance_number: int):
        '''It allows to select one instance of the currently running IviumSoft instances'''

        PyviumVerifiers.verify_driver_is_open()
        active_instances = Pyvium.get_active_iviumsoft_instances()
        if iviumsoft_instance_number not in active_instances:
            error_msg = 'No IviumSoft on instance number {}, actual active instances list = {}'
            raise IviumSoftNotRunningError(error_msg.format(
                iviumsoft_instance_number, active_instances))
        Core.IV_selectdevice(iviumsoft_instance_number)

    @staticmethod
    def get_device_serial_number():
        '''Returns the serial number of the currently selected device if available'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()
        PyviumVerifiers.veryfy_device_is_connected_to_computer()
        _, serial_number = Core.IV_readSN()
        if serial_number == '':
            raise DeviceNotConnectedToIviumSoftError(
                'This device needs to be connected to get its serial number')
        return serial_number

    @staticmethod
    def connect_device():
        '''It connects the currently selected device'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()
        PyviumVerifiers.veryfy_device_is_connected_to_computer()
        Core.IV_connect(1)

    @staticmethod
    def disconnect_device():
        '''It disconnects the currently selected device'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()
        PyviumVerifiers.veryfy_device_is_connected_to_computer()
        Core.IV_connect(0)

    @staticmethod
    def get_dll_version() -> int:
        '''Returns the version of the IviumSoft dll'''
        PyviumVerifiers.verify_driver_is_open()
        return Core.IV_VersionDll()

    @staticmethod
    def select_channel(chanel_number: int):
        '''Sending the integer value communicates with Multichannel control:
            if not yet active, the [int] number of tabs is automatically opened and the [int] tab becomes active;
            if Ivium-n-Soft is active already, the [int] tab becomes active. 
            Now the channel/instrument that is connected to this tab can be controlled. 
            If no instrument is connected, the next available instrument in the list can be connected (IV_connect) and controlled.'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()
        Core.IV_SelectChannel(chanel_number)

    ###############################
    #### DIRECT MODE FUNCTIONS ####
    ###############################

    @staticmethod
    def get_cell_status() -> list:
        '''Returns cell status labels
            ["I_ovl", "Anin1_ovl","E_ovl", "CellOff_button pressed", "Cell on"]'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()
        PyviumVerifiers.verify_device_is_connected_to_iviumsoft()
        _, cell_status_bits = Core.IV_getcellstatus()
        cell_status_labels = []

        labels = ["I_ovl", "", "Anin1_ovl", "E_ovl",
                  "", "CellOff_button pressed", "Cell on"]
        for i, label in enumerate(labels, 2):
            if cell_status_bits & (1 << i) and label:
                cell_status_labels.append(label)
        if len(cell_status_labels) == 0:
            cell_status_labels = ['Cell off']
        return cell_status_labels

    @staticmethod
    def set_connection_mode(connection_mode_number: int):
        ''' Select the connection mode for the currently connected device.
            The available modes depend on the connected device.
            These are all the supported connection modes: 0=off; 1=EStat4EL(default), 2=EStat2EL,
            3=EstatDummy1,4=EStatDummy2,5=EstatDummy3,6=EstatDummy4
            7=Istat4EL, 8=Istat2EL, 9=IstatDummy, 10=BiStat4EL, 11=BiStat2EL'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()
        PyviumVerifiers.verify_device_is_connected_to_iviumsoft()
        Core.IV_setconnectionmode(connection_mode_number)

    @staticmethod
    def set_cell_on():
        '''Set cell off '''
        if 'Cell off' in Pyvium.get_cell_status():
            Core.IV_setcellon(1)

    @staticmethod
    def set_cell_off():
        '''Set cell on '''
        if 'Cell on' in Pyvium.get_cell_status():
            Core.IV_setcellon(0)

    @staticmethod
    def set_potential(potential_value: float):
        '''Set cell potential'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()
        PyviumVerifiers.verify_device_is_connected_to_iviumsoft()
        Core.IV_setpotential(potential_value)

    @staticmethod
    def set_we2_potential(potential_we2_value: float):
        '''Set BiStat offset potential'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()
        PyviumVerifiers.verify_device_is_connected_to_iviumsoft()
        Core.IV_setpotentialWE2(potential_we2_value)

    @staticmethod
    def set_current(current_value: float):
        '''Set cell current (galvanostatic mode)'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()
        PyviumVerifiers.verify_device_is_connected_to_iviumsoft()
        Core.IV_setpotentialWE2(current_value)

    @staticmethod
    def get_potential() -> float:
        '''Returns measured potential'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()
        PyviumVerifiers.verify_device_is_connected_to_iviumsoft()
        _, potential_value = Core.IV_getpotential()
        return potential_value

    @staticmethod
    def get_current_trace(points_quantity: int, interval_rate: float):
        '''Returns a sequence of measured currents at defined samplingrate
            (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        result_code, current = Core.IV_getcurrenttrace(
            points_quantity, interval_rate)

        return result_code, current

    @staticmethod
    def get_current_we2_trace(points_quantity: int, interval_rate: float):
        '''Returns a sequence of measured WE2 currents at defined samplingrate
            (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        result_code, current = Core.IV_getcurrentWE2trace(
            points_quantity, interval_rate)

        return result_code, current

    @staticmethod
    def get_potencial_trace(points_quantity: int, interval_rate: float):
        '''Returns a sequence of measured potentials at defined samplingrate
            (npoints, interval, array of double): npoints<=256, interval: 10us to 20ms'''
        result_code, potential = Core.IV_getpotentialtrace(
            points_quantity, interval_rate)

        return result_code, potential

    @staticmethod
    def set_ac_amplitude(ac_amplitude: float):
        '''Set the value of the ac amplitude in Volts'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()

        Core.IV_setamplitude(ac_amplitude)

    @staticmethod
    def set_ac_frequency(ac_frequency: float):
        '''Set the value of the ac frequency in Hz'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()

        Core.IV_setfrequency(ac_frequency)

    ###############################
    #### METHOD MODE FUNCTIONS ####
    ###############################

    @staticmethod
    def load_method(method_file_path: str):
        '''Loads method procedure previously saved to a file.
            method_file_path represents the full path to the file.'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()

        result_code, _ = Core.IV_readmethod(method_file_path)

        if result_code == 1:
            raise FileNotFoundError

    @staticmethod
    def save_method(method_file_path: str):
        '''Saves currently loaded method procedure to a file.
            method_file_path represents the full path to the new file.'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()

        Core.IV_savemethod(method_file_path)

    @staticmethod
    def start_method(method_file_path=''):
        '''Starts a method procedure.
            If method_file_path is an empty string then the presently loaded procedure is started.
            If the full path to a previously saved method is provided
            then the procedure is loaded from the file and started.'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()
        PyviumVerifiers.verify_device_is_connected_to_iviumsoft()

        result_code, _ = Core.IV_startmethod(method_file_path)

        if result_code == 1:
            raise FileNotFoundError

    @staticmethod
    def abort_method():
        '''Aborts the ongoing method procedure'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()
        PyviumVerifiers.verify_device_is_connected_to_iviumsoft()

        Core.IV_abort()

    @staticmethod
    def save_method_data(method_data_file_path: str):
        '''Saves the results of the last method execution into a file.
            method_file_path represents the full path to the new file.
           IMPORTANT: If the path provided is not valid,
           it will close the selected iviumsoft instance.
        '''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()

        Core.IV_savedata(method_data_file_path)

    @staticmethod
    def set_method_parameter(parameter_name: str, parameter_value: str):
        '''Allows updating the parameter values for the currently loaded method procedrue.
            It only works for text based parameters and dropdowns (multiple option selectors).'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()

        Core.IV_setmethodparameter(
            parameter_name, parameter_value)

    @staticmethod
    def get_available_data_points_number():
        '''Returns actual available number of datapoints: indicates the progress during a run'''
        PyviumVerifiers.verify_driver_is_open()
        PyviumVerifiers.verify_iviumsoft_is_running()

        _, available_data_points_number = Core.IV_Ndatapoints()

        return available_data_points_number

    @staticmethod
    def get_data_point(data_point_index: int):
        '''Get the data from a datapoint with index int, returns 3 values that depend on
            the used technique. For example LSV/CV methods return (E/I/0) Transient methods
            return (time/I,E/0), Impedance methods return (Z1,Z2,freq) etc.'''
        result_code, value1, value2, value3 = Core.IV_getdata(
            data_point_index)

        return result_code, value1, value2, value3

    @staticmethod
    def get_data_point_from_scan(data_point_index: int, scan_index: int):
        '''Same as get_data_point, but with the additional scan_index parameter.
            This function will allow reading data from non-selected (previous) scans.'''
        result_code, value1, value2, value3 = Core.IV_getdatafromline(
            data_point_index, scan_index)

        return result_code, value1, value2, value3
