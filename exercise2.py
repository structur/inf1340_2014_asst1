#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Curtis McCord and Ryan Prance'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "All rights reserved until marks returned"

__status__ = "Prototype"

# imports one per line


def checksum(upc_number):
    """
    (int) -> Bool
    Checks if the digits in a UPC is consistent with checksum

    :param upc_number: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """
    # check type of input
    # raise TypeError if not string
    if type(upc_number) != str:
        raise TypeError
    # check length of string
    # raise ValueError if not 12
    elif len(upc_number)!= 12:
        raise ValueError
    else:
        upc_str_list = list(upc_number)  # convert string to list
        upc_list = [int(i) for i in upc_str_list]  # converts them to ints
        upc_last = (upc_list[-1])  # slices out the last position and makes it an int
        upc_list = upc_list[0:11]  # keeps the first 11 positions
        upc_sum = (sum(upc_list[0::2]) * 3) + (sum(upc_list[1::2]))  # sum of odds times 3 plus sum of evens
        upc_mod = (upc_sum % 10)
        upc_checksum = (10 - upc_mod)
        if upc_checksum == upc_last:
            return True
        else:
            return False


    # check against the the twelfth digit

    # return True if they are equal, False otherwise
    #return False

