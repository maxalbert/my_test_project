import versioneer
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Read long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="my_test_project",
    version=versioneer.get_version(),
    description="Test project for cookiecutter template",
    long_description=long_description,
    url="https://github.com/maxalbert/my_test_project",
    author="Maximilian Albert",
    author_email="maximilian.albert@gmail.com",
    license="MPLv2",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["my_test_project"],
    install_requires=[],
    extras_require={"dev": ["ipython", "jupyter"], "test": ["pytest"]},
    cmdclass=versioneer.get_cmdclass(),
)
