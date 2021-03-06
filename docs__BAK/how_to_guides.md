# How-To Guides

_A how-to guide:_

- _is **goal-oriented**_
- _shows how to solve a specific problem_
- _is a series of steps_

_(See [here](https://www.divio.com/blog/documentation/) for context and more information.)_

## Users

### Installing my_test_project

You can install the latest release by running:
```
$ pip install -U my_test_project
```

You can also grab the latest development version directly from GitHub:
```
$ pip install git+https://github.com/maxalbert/my_test_project
```


## Developers

### Setting up a development environment

`my_test_project` uses [poetry](https://python-poetry.org/) for dependency management, so make sure you have it [installed](https://python-poetry.org/docs/#installation).

Next, install the necessary dependencies for `my_test_project`.
We specify the `--extras` options to install the complete set of packages for a full development environment.
```
$ poetry install --extras "develop testing docs deploy"
```


### Running the tests

```
$ poetry run pytest
```

Example output:
```
============================= test session starts ==============================
platform linux -- Python 3.8.1, pytest-3.10.1, py-1.8.0, pluggy-0.13.0
rootdir: /path/to/code/my_test_project, inifile:
collected 1 item

tests/test_my_test_project.py .                                           [100%]

=========================== 1 passed in 0.11 seconds ===========================
```
