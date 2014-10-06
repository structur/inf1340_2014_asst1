#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Curtis McCord and Ryan Prance'
__email__ = "curtis.mccord@utoronto.ca; ryan.prance@mail.utoronto.ca"

__copyright__ = "2014 Susan Sim"
__license__ = "INF1340"

__status__ = "Tested Prototype"

# imports one per line


def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    (int OR str) -> float
    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade = ""
    gpa = 0.0

    if type(grade) is str:
        # check that the grade is one of the accepted values
        accepted_values = ["A+", "A", "A-", "B+", "B", "B-", "FZ"]
        # assign grade to letter_grade
        if grade in accepted_values:

            letter_grade = grade
        else:
            raise ValueError("Invalid input!  Grade must be an acceptable graduate letter grade.")

    elif type(grade) is int:
        # check that grade is in the accepted range (0-100)
        if 0 <= grade <= 100:
        # convert the numeric grade to a letter grade
            mark_to_letter = grade
        # assign the value to letter_grade
            if mark_to_letter >= 90:
                letter_grade= "A+"
            elif mark_to_letter >= 85:
                letter_grade = "A"
            elif mark_to_letter >= 80:
                letter_grade = "A-"
            elif mark_to_letter >= 77:
                letter_grade = "B+"
            elif mark_to_letter >= 73:
                letter_grade = "B"
            elif mark_to_letter >= 70:
                letter_grade = "B-"
            elif mark_to_letter >= 0:
                letter_grade = "FZ"
        else:
            raise ValueError("Grade must be within range of 0-100")
    else:
        raise TypeError("Invalid type passed as parameter")

        # assign the value to gpa
    if letter_grade == "A+":
        gpa = 4.0
    elif letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7
    elif letter_grade == "B+":
        gpa = 3.3
    elif letter_grade == "B":
        gpa = 3.0
    elif letter_grade == "B-":
        gpa = 2.7
    elif letter_grade == "FZ":
        gpa = 0.0

    return gpa

