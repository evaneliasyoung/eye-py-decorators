# EYE-Py-Decorators

[![Python Version][pyv-img]][pyv-url]
[![Tox][tox-img]][tox-url]
[![Typed][mpy-img]][mpy-url]
[![Code Style][pep-img]][pep-url]

The goal of the `eye_decorators` module is to make it easy to define signature-preserving function decorators and decorator factories.
The module also includes simple utility decorators.

## Installation

Install the full distribution from source, clone the [GitHub repo](https://github.com/evaneliasyoung/eye-py-decorators) and run

> `$ pip install .`

## Decorator

```py
from eye_decorators import decorator

@decorator
def warn_slow(func, timelimit=60, *args, **kw):
    t0 = time.time()
    result = func(*args, **kw)
    dt = time.time() - t0
    if dt > timelimit:
        logging.warn('%s took %d seconds', func.__name__, dt)
    else:
        logging.info('%s took %d seconds', func.__name__, dt)
    return result

@warn_slow  # warn if it takes more than 1 minute
def preprocess_input_files(inputdir, tempdir):
    ...

@warn_slow(timelimit=600)  # warn if it takes more than 10 minutes
def run_calculation(tempdir, outdir):
    ...
```

## Timed

```py
from eye_decorators import timed

@timed  # print the runtime of the function
def preprocess_input_files(inputdir, tempdir):
    ...
```

## Rounded

```py
from eye_decorators import timed

@rounded  # return the value rounded to an integer
def random_int(min, max) -> float:
    ...

@rounded(6)  # return the value rounded to 6 decimal places
def secant_method(f, P) -> float:
    ...
```

[pyv-img]: https://img.shields.io/static/v1?label=python&message=>=3.9&color=blue
[pyv-url]: https://docs.python.org/release/3.9.0/
[mpy-img]: https://img.shields.io/badge/mypy-checked-2A6DB2.svg
[mpy-url]: https://mypy-lang.org/
[tox-img]: https://github.com/evaneliasyoung/eye-py-decorators/actions/workflows/tox.yml/badge.svg
[tox-url]: https://github.com/evaneliasyoung/eye-py-decorators/actions/workflows/tox.yml
[pep-img]: https://img.shields.io/badge/code%20style-pep8-orange.svg
[pep-url]: https://www.python.org/dev/peps/pep-0008/
