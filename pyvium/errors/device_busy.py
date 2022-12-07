class DeviceBusyError(Exception):
    '''Raised when the IviumSoft software all devices are busy'''
    def __init__(self, message = "There is no available device. Please, connect one."):
        self.message = message
        super().__init__(self.message)
