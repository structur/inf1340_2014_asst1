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

upc_number = input(str('Please Enter UPC number here:'))


def checksum (upc_number):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc_number: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """
    upc_list = list(upc_number)
    # check type of input
    # raise TypeError if not string
    if upc_number != type(str):
        print('Value Error! Please try again!')
    # check length of string
    # raise ValueError if not 12
    elif len(upc_number)!=12:
        print("Value Error! Please make sure your UPC number is 12 digits and reenter it!")
    else: checksum(upc_odds, upc_evens)

upc_array = list(upc_number) # convert string to array
                                # hint: use the list function
upc_odds = (int(upc_array[0]) + int(upc_array[2]) + int(upc_array[4]) + \
            int(upc_array[6]) + int(upc_array[8]) + int(upc_array[10])) * 3

upc_evens = int(upc_array[1]) + int(upc_array[3]) + int(upc_array[5]) + \
            int(upc_array[7]) + int(upc_array[9])
upc_last = int(upc_array[10])
def checksum(upc_evens, upc_odds):
        """
        (int + int) - > int
        :param upc_array: This is the array made earlier to be broken down into multiple part and summed
        :return: This returns the sum of upc_odds/3 and upc_evens
        """# generate checksum using the first 11 digits provided
        upc_sum = (upc_evens + upc_odds % 10)
        if upc_sum  == 0:
            return 10 - upc_sum
        elif 10 - upc_sum == upc_last:
                print("UPC number valid.")
        else:
                return "Invalid UPC number."
    # check against the the twelfth digit

    # return True if they are equal, False otherwise
    #return False

