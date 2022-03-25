#!/usr/bin/env python3
"""
@file      stub.py
@brief     Additional package types.
"""


from typing import Any, Callable, TypeVar


_T = TypeVar("_T")
VarArgs = tuple[Any, ...]
KwArgs = dict[str, Any]
AnonCallable = Callable[..., _T]
