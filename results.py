# -*- coding: utf-8 -*-
"""
results.py -- Results & Leaderboard team.

Responsibility: show the leaderboard, find the hardest question, and
compute per-player statistics.

Important! Using max / min / sum is not allowed. Every maximum/minimum
search and every average must be implemented manually with loops.
"""


def show_leaderboard(results):
    """
    Sort the results from highest score to lowest and display them.

    Parameters:
        results -- a list of dictionaries {"player": str, "score": int}

    Required: sort manually! (e.g. bubble sort or selection sort).
    Do not use sorted / .sort if the instructor requires a manual sort,
    and in any case do not use max / min.
    """
    pass  # TODO Results team


def find_hardest_question(bank):
    """
    Find the question with the highest number of wrong answers (wrong_count).

    Parameters:
        bank -- the list of questions

    Returns: the dictionary of the hardest question (or None if empty).

    Required: find the maximum manually! Keep a "best so far" and loop over
    all the questions. Do not use max.
    """
    pass  # TODO Results team


def player_statistics(results, player):
    """
    Compute statistics for a specific player.

    Parameters:
        results -- the results list
        player  -- the player's name

    Compute (all manually, without sum/max/min):
      - how many quizzes the player took
      - their highest score
      - their lowest score
      - their average (manual sum divided by number of quizzes)

    Returns: a dictionary with these values (or a suitable message if the
    player has no results).
    """
    pass  # TODO Results team
