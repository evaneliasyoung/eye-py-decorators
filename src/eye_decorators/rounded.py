#!/usr/bin/env python3
"""
@file      rounded.py
@brief     Decorator to round floating-point returns.

@author    Evan Elias Young
@date      2022-02-22
@date      2022-03-25
@copyright Copyright 2022 Evan Elias Young. All rights reserved.
"""


from typing import Optional, SupportsIndex, SupportsRound, Union

from .decorator import decorator
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
