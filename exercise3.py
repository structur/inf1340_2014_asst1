#!/usr/bin/env python3

"""
Allows 2 players to play the game 'Rock, Paper, Scissors'

Assignment 1, Exercise 3, INF1340 Fall 2014
"""
__author__ = 'Curtis McCord and Ryan Prance'
__email__ = "curtis.mccord@utoronto.ca and ryan.prance@mail.utoronto.ca"

__copyright__ = "2014 Susan Sim"
__license__ = "INF1340 2014"

__status__ = "Tested Prototype"

rps_results = {("Rock", "Paper"): 2,
               ("Rock", "Scissors"): 1,
               ("Rock", "Rock"): 0,
               ("Paper", "Rock"):1,
               ("Paper","Paper"): 0,
               ("Paper","Scissors"): 2,
               ("Scissors", "Scissors"): 0,
               ("Scissors", "Paper"): 1,
               ("Scissors", "Rock"): 2}

valid_inputs = ["Rock", "Paper", "Scissors"]

def decide_rps(player1, player2):
    """
    This function takes a tuple and returns a value which shows the winner, based on a dictionary!

    (tuple) -> int
    :param player1: This is a string linked to a tuple in the dictionary rps_results
    :param player2: This is a string linked to a tuple in the dictionary rps_results
    :return: the int returned (0, 1, 2) is the victor of rps; 0 is a tie, 1 is a P1 victory, and 2 is a P2 victory
    :raises: ValueError if one element of tuple not a valid input
    """
    if player1 not in valid_inputs:
        raise ValueError("Player 1, we didn\'t recognize your entry.")
    elif player2 not in valid_inputs:
        raise ValueError("Player 2, we didn\'t recognize your entry.")
    else:
        return rps_results[(player1, player2)]
