import pytest
from .bit_problems import *


def bit_is_even():
    given = "0010"
    expected = "even"
    got = bit_is_even(given)
    assert got == expected


def bit_is_odd():
    given = "00o0"
    expected = "odd"
    got = bit_is_odd(given)
    assert got == expected


