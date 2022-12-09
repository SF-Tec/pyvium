class DeviceBusyError(Exception):
    '''Raised when the IviumSoft software all devices are busy'''

    def __init__(self, message="The selected device is busy, connect/select another \
        device or wait till it becomes available."):
        self.message = message
        super().__init__(self.message)
