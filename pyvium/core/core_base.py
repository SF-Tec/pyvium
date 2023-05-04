'''The module provides base class for shared state and methods related to Ivium driver.'''
from typing import Any

from cffi import FFI

from ..util import get_ivium_dll_path

ffi = FFI()


class CoreBase:
    """
    Base class for providing shared state and methods related to Ivium driver.
    """
    __is_driver_open = False
    __lib = ffi.dlopen(get_ivium_dll_path())

    @staticmethod
    def get_lib() -> Any:
        """
        Returns the library instance.
        """
        return CoreBase.__lib

    @staticmethod
    def is_driver_open() -> bool:
        """
        Returns the driver open status.
        """
        return CoreBase.__is_driver_open

    @staticmethod
    def set_driver_open(status: bool) -> None:
        """
        Sets the driver open status.

        :param status: Driver open status as a boolean.
        """
        CoreBase.__is_driver_open = status
