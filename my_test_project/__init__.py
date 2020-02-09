"""
Test project for cookiecutter template
"""

from .dummy import dummy_function

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
