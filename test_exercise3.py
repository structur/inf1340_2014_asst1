#!/usr/bin/env python3

""" Module to test exercise3.py """

__author__ = 'Curtis McCord and Ryan Prance '
__email__ = "curtis.mccord@utoronto.ca; ryan.prance@mail.utoronto.ca"

__copyright__ = "2014 Susan Sim"
__license__ = "INF1340"

__status__ = "Tested Prototype"

import pytest
from exercise3 import decide_rps


def test_decide_rps():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Paper", "Paper") == 0
    assert decide_rps("Paper", "Scissors") == 2
    assert decide_rps("Paper", "Rock") == 1

    # other tests for invalid entries
def test_invalid_params():
    """
    Inputs that are not valid game moves
    """
    with pytest.raises(ValueError):
        decide_rps("Rock", "Cheeses")
        decide_rps("Sword", "Giraffe")
        decide_rps(1, 4)
        decide_rps(4.0, "Rock")

test_decide_rps()
test_invalid_params()