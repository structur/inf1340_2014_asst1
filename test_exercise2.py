#!/usr/bin/env python3

""" Module to test exercise2.py """

__author__ = 'Curtis McCord and Ryan Prance '
__email__ = "curtis.mccord@utoronto.ca; ryan.prance@mail.utoronto.ca"

__copyright__ = "2014 Susan Sim"
__license__ = "INF1340"

__status__ = "Tested Prototype"

# imports one per line

# imports one per line
import pytest
import exercise2
from exercise2 import checksum


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000841") is False
    assert checksum("065743240502") is True
    assert checksum("811138000202") is True
    assert checksum("888888888888") is False
    assert checksum("134087934837") is False
    # other tests


def test_input():
    """
    Inputs that are the incorrect format or length
    """
    with pytest.raises(TypeError):
        checksum(1.0)
        checksum(786936224306)
        checksum([1,2])
        checksum(True)

    with pytest.raises(ValueError):
        checksum("1")
        checksum("1234567890")
        checksum("noteven")
        checksum("thisonehastobetoolong")

    # other tests

# add functions for any other tests
test_checksum()
test_input()