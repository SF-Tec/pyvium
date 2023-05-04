from cffi import FFI

from ..util import get_ivium_dll_path

ffi = FFI()
IVIUM_DLL_PATH = get_ivium_dll_path()
CHAR_ARRAY = "char[]"
DOUBLE_PTR = "double *"
LONG_PTR = "long *"
UTF_ENCODING = "utf-8"


class Base:
    '''Base class for providing shared state and methods'''
    __is_driver_open = False
    __lib = ffi.dlopen(IVIUM_DLL_PATH)

    @staticmethod
    def get_lib():
        return Base.__lib

    @staticmethod
    def is_driver_open() -> bool:
        return Base.__is_driver_open

    @staticmethod
    def set_driver_open(status: bool):
        Base.__is_driver_open = status
