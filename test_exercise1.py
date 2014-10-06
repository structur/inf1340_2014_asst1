#!/usr/bin/env python3

""" Module to test exercise1.py """

__author__ = 'Curtis McCord and Ryan Prance'
__email__ = "curtis.mccord@utoronto.ca; ryan.prance@mail.utoronto.ca"

__copyright__ = "All rights reserved until grade returned"
__license__ = "INF1340"

__status__ = "Tested Prototype"

# imports one per line
import pytest
from exercise1 import grade_to_gpa


def test_letter_grade():
    """
    Letter grade inputs
    """
    assert grade_to_gpa("A+") == 4.0
    assert grade_to_gpa("A") == 4.0
    assert grade_to_gpa("A-") == 3.7
    assert grade_to_gpa("B+") == 3.3
    assert grade_to_gpa("B") == 3.0
    assert grade_to_gpa("B-") == 2.7
    assert grade_to_gpa("FZ") == 0.0
    # further tests for invalid values
    with pytest.raises(ValueError):
        grade_to_gpa("q")
        grade_to_gpa("C-")
        grade_to_gpa('A++')
        grade_to_gpa('85%')


def test_percentage_grade():
    """
    Numeric grade inputs
    """
    assert grade_to_gpa(100) == 4.0
    assert grade_to_gpa(95) == 4.0
    assert grade_to_gpa(90) == 4.0
    
    assert grade_to_gpa(89) == 4.0
    assert grade_to_gpa(87) == 4.0
    assert grade_to_gpa(85) == 4.0

    assert grade_to_gpa(84) == 3.7
    assert grade_to_gpa(82) == 3.7
    assert grade_to_gpa(80) == 3.7

    assert grade_to_gpa(79) == 3.3
    assert grade_to_gpa(78) == 3.3
    assert grade_to_gpa(77) == 3.3

    assert grade_to_gpa(76) == 3.0 
    assert grade_to_gpa(74) == 3.0
    assert grade_to_gpa(73) == 3.0

    assert grade_to_gpa(72) == 2.7
    assert grade_to_gpa(71) == 2.7
    assert grade_to_gpa(70) == 2.7

    assert grade_to_gpa(69) == 0.0
    assert grade_to_gpa(37) == 0.0
    assert grade_to_gpa(0) == 0.0

    with pytest.raises(ValueError):
        grade_to_gpa(101)
        grade_to_gpa(-1)


def test_invalid_input():
    """
    Float, tuple and list inputs
    """
    with pytest.raises(TypeError):
        grade_to_gpa(82.5)
        grade_to_gpa(['A+', 100])
        grade_to_gpa(('B+', 79))

# add functions for any other tests


def test_gpa_consistency():
    """
    Makes sure that the letters and numbers return the same values
    """
    assert grade_to_gpa(100) == grade_to_gpa("A+")
    assert grade_to_gpa(80) == grade_to_gpa("A-")
    assert grade_to_gpa(70) == grade_to_gpa("B-")
    assert grade_to_gpa(50) == grade_to_gpa("FZ")

test_letter_grade()
test_percentage_grade()
test_invalid_input()
test_gpa_consistency()