# -*- coding: utf-8 -*-
"""
scoring.py -- Scoring team.

Responsibility: compute the score and save the result.

Important! Using sum is not allowed. Counting the correct answers must be
done manually with a loop and a counter.
"""


def calculate_score(answers):
    """
    Compute a score from the list of answers returned by run_quiz.

    Parameters:
        answers -- a list of booleans (True = correct answer)

    Returns: the number of correct answers.

    Required: count manually! Start a counter at 0, loop over the list,
    and add 1 for every True. Do not use sum.
    """
    total = 0
    for answer in answers:
        if answer == True:
            total  += 1
    return total



def save_result(results, player, score):
    """
    Save the player's result into the results list.

    Parameters:
        results -- the results list (modified in place)
        player  -- the player's name
        score   -- the computed score

    Appends to results a dictionary of the form: {"player": player, "score": score}.
    """
    dicts = {player: score}
    results.append(dicts)
