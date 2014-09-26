#!/usr/bin/env python3

"""
Allows 2 players to play the game 'Rock, Paper, Scissors'
"""
__author__ = 'Curtis McCord and Ryan Prance'
__email__ = "curtis.mccord@utoronto.ca and ????"

__copyright__ = "2014 Susan Sim"
__license__ = "INF1340 2014"

__status__ = "Prototype"

def decide_rps(player1, player2):
    """
    (str, str) ->
    This function allows players 1 and 2 to input
    :param player1: is an input string (Rock, Paper, or Scissors)
    :param player2: is an input string (Rock, Paper, or Scissors)
    :return: If both players enter valid answers, then this function will execute rps_winner
    """
    player1 = input(str('Player 1, choose Rock, Paper, or Scissors!'))
    if player1 != 'Rock' or 'Paper' or 'Scissors':
        print ('Invalid choice! Pick Rock or Paper or Scissors')
    player2 = input(str('Player 2, choose Rock, Paper, or Scissors!'))
    if player2 != 'Rock' or 'Paper' or 'Scissors':
        print ('Invalid Choice! Pick Rock or Paper or Scissors')
    else: return rps_winner



Rock = 0
Paper = 1
Scissors = 2

def rps_winner(p1_choice, p2_choice):
    """
    (int, int) -> int4
    :param p1_choice: this is an int (0, 1, 2) corresponding to Player 1's input
    :param p2_choice: this is an int (0, 1, 2) corresponding to Player 2's input
    :return: the int returned (0, 1, 2) is the victor of rps; 0 is a tie, 1 is a P1 victory, and 2 is a P2 victory

    This function takes the two str inputs (which have now been converted to ints).
    It then subtracts them from one another (P1 - P2) and then applies modulo (3) (there are three choices).
    It returns a value (0, 1, 2) corresponding to the victor.
    """
    rps_winner = ((p1_choice - p2_choice) % 3)
    if rps_winner == 0:
        print("0! Tie game!")
    elif rps_winner == 1:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")