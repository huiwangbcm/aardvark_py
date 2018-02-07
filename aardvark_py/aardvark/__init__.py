"""Under the hood, the 'aardvark' submodule is actually a python extension module provided by Total Phase in the API release:

``aardvark.so``      --  Linux/Mac shared object

``aardvark.dll/pyd`` --  Windows dynamic link library

The official API documentation can be found at https://www.totalphase.com/support/articles/200468316-Aardvark-I2C-SPI-Host-Adapter-User/#s5
"""

import platform

_system = platform.system()

if (_system in ('Darwin')):
    from .darwin import *
elif (_system in ('Linux')):
    from .linux import *
elif (_system in ('Windows', 'Microsoft')):
    from .windows import *
else:
    raise ImportError("%s is not supported by Aardvark API" % _system)
