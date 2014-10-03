#!/usr/bin/env python3

"""
Allows 2 players to play the game 'Rock, Paper, Scissors'
"""
__author__ = 'Curtis McCord and Ryan Prance'
__email__ = "curtis.mccord@utoronto.ca and ????"

__copyright__ = "2014 Susan Sim"
__license__ = "INF1340 2014"

__status__ = "Prototype"

rps_results = {}
rps_results[("Rock", "Paper")] = 2
rps_results[("Rock", "Scissors")] = 1
rps_results[("Rock", "Rock")] = 0
rps_results[("Paper", "Rock")] = 1
rps_results[("Paper","Paper")] = 0
rps_results[("Paper","Scissors")] = 2
rps_results[("Scissors", "Scissors")] = 0
rps_results[("Scissors", "Paper")] = 1
rps_results[("Scissors", "Rock")] = 2

valid_inputs = ["Rock", "Paper", "Scissors"]

def decide_rps(player1, player2):
    """
    (tuple) -> int
    :param p1_choice: This is a string linked to a tuple in the dictionary rps_results
    :param p2_choice: This is a string linked to a tuple in the dictionary rps_results
    :return: the int returned (0, 1, 2) is the victor of rps; 0 is a tie, 1 is a P1 victory, and 2 is a P2 victory

    This function take a tuple and returns a value which shows the winner, based on a dictionary!
    """
    if player1 not in valid_inputs:
        raise ValueError("Player 1, we didn\'t recognize your entry.")
    elif player2 not in valid_inputs:
        raise ValueError("Player 2, we didn\'t recognize your entry.")
    else:
        return rps_results[(player1, player2)]
