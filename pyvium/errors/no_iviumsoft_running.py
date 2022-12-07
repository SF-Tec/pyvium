class IviumSoftNotRunningError(Exception):
    '''Raised when the IviumSoft software is not running'''

    def __init__(self, message="IviumSoft is not currently running. Please, start it."):
        self.message = message
        super().__init__(self.message)
