from .direct_mode_functions import DirectModeFunctions
from .generic_functions import GenericFunctions
from .method_mode_functions import MethodModeFunctions


class Pyvium(DirectModeFunctions, GenericFunctions, MethodModeFunctions):
    pass
