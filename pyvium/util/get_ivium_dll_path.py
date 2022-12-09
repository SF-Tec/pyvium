from os import path
from sys import maxsize, modules


def get_ivium_dll_path():
    '''Returns the path to the Ivium driver dll.
    It will be the 32 or 64 bit veresion depending on the version of Windows.'''
    module_directory = path.dirname(modules["pyvium"].__file__)

    ivium_dll_filename = "Ivium_remdriver64.dll"

    if maxsize <= 2**32:
        ivium_dll_filename = "IVIUM_remdriver.dll"

    return path.join(module_directory, ivium_dll_filename)
