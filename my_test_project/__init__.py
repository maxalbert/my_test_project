# __init__.py file for `my_test_project`

from .dummy import dummy_function

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
