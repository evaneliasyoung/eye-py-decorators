#!/usr/bin/env python3
"""
@file      dec_rounded.py
@brief     Decorator to round floating-point returns.
"""


from typing import Optional, SupportsIndex, SupportsRound, Union

from .dec_decorator import decorator
from .stub import AnonCallable, VarArgs, KwArgs, _T


@decorator
def rounded(
    func: AnonCallable[SupportsRound[_T]],
    ndigits: Optional[SupportsIndex] = None,
    *args: VarArgs,
    **kwds: KwArgs,
) -> Union[int, _T]:
    if ndigits and int(ndigits) != 0:
        return round(func(*args, **kwds), ndigits)
    else:
        return round(func(*args, **kwds))
