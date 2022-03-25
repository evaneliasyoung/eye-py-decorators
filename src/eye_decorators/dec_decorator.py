#!/usr/bin/env python3
"""
@file      dec_decorator.py
@brief     Decorator module.

@author    Evan Elias Young
@date      2022-02-22
@date      2022-03-25
@copyright Copyright 2022 Evan Elias Young. All rights reserved.
"""


import re
from inspect import (
    Signature,
    signature,
    iscoroutinefunction,
    isgeneratorfunction,
    _ParameterKind,
    Parameter,
    BoundArguments,
    _empty,
)
from typing import Any, Pattern, cast

from .stub import VarArgs, KwArgs


DEF: Pattern[str] = re.compile(r"\s*def\s*([_\w][_\w\d]*)\s*\(")
POS: _ParameterKind = Parameter.POSITIONAL_OR_KEYWORD


def fix(
    args: VarArgs,
    kwds: KwArgs,
    sig: Signature,
) -> tuple[VarArgs, KwArgs]:
    ba: BoundArguments = sig.bind(*args, **kwds)
    ba.apply_defaults()
    return ba.args, ba.kwargs


def decorate(
    func,
    caller,
    extras: VarArgs = (),
    kwsyntax: bool = False,
):
    sig: Signature = signature(func)
    if iscoroutinefunction(caller):

        async def fun(*args, **kwds):
            if not kwsyntax:
                args, kwds = fix(args, kwds, sig)
            return await caller(func, *(extras + args), **kwds)

    elif isgeneratorfunction(caller):

        def fun(*args, **kwds):
            if not kwsyntax:
                args, kwds = fix(args, kwds, sig)
            for res in caller(func, *(extras + args), **kwds):
                yield res

    else:

        def fun(*args, **kwds):
            if not kwsyntax:
                args, kwds = fix(args, kwds, sig)
            return caller(func, *(extras + args), **kwds)

    fun.__name__ = func.__name__
    fun.__doc__ = func.__doc__
    cast(Any, fun).__wrapped__ = func
    cast(Any, fun).__signature__ = sig
    fun.__qualname__ = func.__qualname__
    try:
        cast(Any, fun).__defaults__ = func.__defaults__
    except AttributeError:
        pass
    try:
        cast(Any, fun).__kwdefaults__ = func.__kwdefaults__
    except AttributeError:
        pass
    try:
        fun.__annotations__ = func.__annotations__
    except AttributeError:
        pass
    try:
        fun.__module__ = func.__module__
    except AttributeError:
        pass
    try:
        fun.__dict__.update(func.__dict__)
    except AttributeError:
        pass
    return fun


def decorator(
    caller,
    _func=None,
    kwsyntax: bool = False,
):
    if _func is not None:
        return decorate(_func, caller, (), kwsyntax)
    sig: Signature = signature(caller)
    fun_params: list[Parameter] = [p for p in sig.parameters.values() if p.kind is POS]

    def fun(func=None, *args, **kwds):
        na: int = len(args) + 1
        extras: VarArgs = args + tuple(
            kwds.get(p.name, p.default)
            for p in fun_params[na:]
            if p.default is not _empty
        )
        return (
            decorate(func, caller, extras, kwsyntax)
            if func is not None
            else lambda func: decorate(func, caller, extras, kwsyntax)
        )

    cast(Any, fun).__signature__ = sig.replace(parameters=fun_params)
    fun.__name__ = caller.__name__
    fun.__doc__ = caller.__doc__
    cast(Any, fun).__wrapped__ = caller
    fun.__qualname__ = caller.__qualname__
    cast(Any, fun).__kwdefaults__ = getattr(caller, "__kwdefaults__", None)
    fun.__dict__.update(caller.__dict__)
    return fun
