#!/usr/bin/env python3
"""
@file      stub.py
@brief     Decorator types.

@author    Evan Elias Young
@date      2022-02-22
@date      2022-02-22
@copyright Copyright 2022 Evan Elias Young. All rights reserved.
"""


from typing import Any, Callable, TypeVar


_T = TypeVar("_T")
VarArgs = tuple[Any, ...]
KwArgs = dict[str, Any]
AnonCallable = Callable[..., _T]
