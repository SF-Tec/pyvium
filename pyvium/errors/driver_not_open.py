class DriverNotOpenError(Exception):
    '''Raised when the IviumSoft driver has not been open'''

    def __init__(self, message="The driver is not open. Please, use open_driver() to open it."):
        self.message = message
        super().__init__(self.message)
