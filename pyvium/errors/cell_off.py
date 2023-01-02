class CellOffError(Exception):
    '''Raised when the cell is off'''

    def __init__(self, message="The cell is off"):
        self.message = message
        super().__init__(self.message)
