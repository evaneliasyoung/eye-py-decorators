#!/usr/bin/env python3
"""
@file      test_rounded.py
@brief     Test @rounded.
"""

from eye_decorators import rounded
from math import pi
import pytest


@pytest.mark.parametrize(
    "ndigits,expected",
    [(i, round(pi, i)) for i in range(10)],
)
def test_multi_rounded(ndigits, expected):
    assert rounded(lambda x: x, ndigits=ndigits)(pi) == expected


def test_int_rounded():
    assert isinstance(rounded(lambda x: x)(pi), int)
    assert isinstance(rounded(lambda x: x, ndigits=None)(pi), int)
    assert isinstance(rounded(lambda x: x, ndigits=0)(pi), int)
