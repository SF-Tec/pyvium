# PYVIUM

Tiny Python wrapper around the "Software development driver DLL" for IviumSoft.

# Important:
This module uses a dll from the IviumSoft application. You need to have this software installed on a Windows machine. The IviumSoft application can be downloaded from here: https://www.ivium.com/support/#Software%20update

## Installation

Install PYVIUM easily with pip:

```
pip install pyvium
```

Or with poetry:

```
poetry add pyvium
```

## Usage Example (Using IviumSoft Core functions)

To use the same functions available in the "IviumSoft driver DLL" you can import the Core class as follows. All functions return a result code (integer) and a result value if available. For further information you can check the IviumSoft documentation.

```
from pyvium import Core

Core.IV_open()
Core.IV_getdevicestatus()
Core.IV_close()
```

<!-- ## Usage Example (Using Pyvium methods)

This is a wrapper around the Core functions that adds a few things:
- Exception management
- New functionalities

```
from pyvium import Pyvium

app = Pyvium()

app.connect_device()
``` -->


## Not working functions
- IV_getcurrentWE2trace
- IV_getpotentialtrace

## Links

* [See on GitHub](https://github.com/sftec/pyvium)
* [See on PyPI](https://pypi.org/project/pyvium)