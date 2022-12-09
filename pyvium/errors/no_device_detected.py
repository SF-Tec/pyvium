class NoDeviceDetectedError(Exception):
    '''Raised when the IviumSoft software cannot detect any devices.'''

    def __init__(self, message="Please, check your device is properly connected to the usb port."):
        self.message = message
        super().__init__(self.message)
