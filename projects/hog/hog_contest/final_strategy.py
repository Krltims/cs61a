"""
    This file contains your final_strategy that will be submitted to the contest.
    It will only be run on your local machine, so you can import whatever you want!
    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""

PLAYER_NAME = ''  # Change this line!


def final_strategy(score, opponent_score):
    if opponent_score-score>=10:
        return num_rolls
    else:
        return extra_turn_strategy(score, opponent_score,cutoff, num_rolls)