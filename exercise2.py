#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Curtis McCord and Ryan Prance'
__email__ = "curtis.mccord@utoronto.ca ryan.prance@utoronto.ca"

__copyright__ = "2014 Susan Sim, modified by Curtis McCord and Ryan Prance"
__license__ = "All rights reserved until marks returned"

__status__ = "Prototype: Validated"

# imports one per line


def checksum(upc_number):
    """
    Checks if the digits in a UPC is consistent with checksum (final) digit

    (str) -> Bool
    :param upc_number: a 12-digit universal product code in str format
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """
    # check type of input
    # raise TypeError if not string
    if type(upc_number) != str:
        raise TypeError
    # check length of string
    # raise ValueError if not 12
    elif len(upc_number) != 12:
        upc_over_under = (12 - len(upc_number))  # shows the discrepancy between entered and expected values
        raise ValueError("Entered UPC is" + str(upc_over_under) + "digits away from 12")
    else:
        upc_str_list = list(upc_number)  # convert string to list of strings
        upc_int_list = [int(i) for i in upc_str_list]  # converts strings to ints
        upc_last = (upc_int_list[-1])  # makes the checksum (last) digit a variable
        upc_int_list = upc_int_list[0:11]  # keeps the first 11 positions
        upc_sum = (sum(upc_int_list[0::2]) * 3) + (sum(upc_int_list[1::2]))  # sum of odds times 3 plus sum of evens
        upc_mod = (upc_sum % 10)
        upc_checksum = (10 - upc_mod)
        if upc_checksum == upc_last:  # check against the the twelfth digit
            return True  # return True if they are equal, False otherwise
        else:
            return False