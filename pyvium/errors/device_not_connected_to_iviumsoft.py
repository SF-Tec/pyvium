class DeviceNotConnectedToIviumSoftError(Exception):
    '''Raised when your device is not connected in the IviumSoft software'''

    def __init__(self, message="IviumSoft has no connected device. Please, connect one."):
        self.message = message
        super().__init__(self.message)
