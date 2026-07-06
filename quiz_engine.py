# -*- coding: utf-8 -*-
"""
quiz_engine.py -- Engine team.

Responsibility: run the quiz for the player and check answers.
"""


def check_answer(question, answer_index):
    """
    Check whether the chosen answer is correct.

    Parameters:
        question     -- a question dictionary (see structure in question_bank.py)
        answer_index -- the index the player chose

    Returns: True if answer_index equals the question's correct_index,
             otherwise False.

    Note: if the answer is wrong, increase question["wrong_count"] by 1
    (this is what lets the Results team find the hardest question).
    """
    pass  # TODO Engine team


def run_quiz(bank, player):
    """
    Run a full quiz for a player: show each question, print the options
    numbered, read the choice, and check it with check_answer.

    Parameters:
        bank   -- the list of questions
        player -- the player's name

    Returns: a list of booleans (True/False) -- one answer per question.
             This list is passed to the Scoring team to compute a score.

    Hint: loop over bank, print question["text"] and the options, read the
    player's choice, and append the result of check_answer to the results list.
    """
    pass  # TODO Engine team
