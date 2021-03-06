#!/usr/bin/env python3
"""
@file      dec_timed.py
@brief     Decorator to time functions.
"""


from time import time

from .dec_decorator import decorator
from .stub import AnonCallable, VarArgs, KwArgs, _T


@decorator
def timed(
    func: AnonCallable[_T],
    *args: VarArgs,
    **kwds: KwArgs,
) -> _T:
    st: float = time()
    result: _T = func(*args, **kwds)
    dt: float = time() - st
    print(f"{func.__name__} took {dt * 1000} ms")
    return result
