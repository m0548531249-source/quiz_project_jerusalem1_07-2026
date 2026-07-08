# -*- coding: utf-8 -*-
"""
main.py -- the integration point of the project (the manager function).

This is the shared file that every team connects to.
Each team adds its function calls at the matching TODO marker.

Note: because several teams edit this file, a merge conflict is likely
when the PRs are merged. This is expected and intentional -- it is an
opportunity to practice resolving a conflict by hand. Don't panic.
"""

from question_bank import add_question, list_questions, remove_question
from sample_data import get_sample_bank
from quiz_engine import run_quiz
from scoring import calculate_score, save_result
from results import show_leaderboard, find_hardest_question, player_statistics


def main_menu():
    """Main menu loop. Holds the system state and routes to every action."""
    # System state -- kept in memory only (no files)
    bank = []       # list of question dictionaries
    # list of result dictionaries: {"player": str, "score": int}
    results = []

    while True:
        print("\n===== Quiz System =====")
        print("1. Add question")
        print("2. List questions")
        print("3. Remove question")
        print("4. Run quiz")
        print("5. Leaderboard")
        print("6. Hardest question")
        print("7. Player statistics")
        print("0. Exit")
        choice = input("Choice: ")

        # ------------------------------------------------------------------
        # TODO Question Bank team: connect add_question / list_questions /
        # remove_question here (options 1, 2, 3)
        bank = get_sample_bank
        if choice == 1:
            textt = input("add a txt")
            list_of_answ=[fgjh,jhdt]

            bank = add_question()
        
        # ------------------------------------------------------------------

        # ------------------------------------------------------------------
        # TODO Engine team: connect run_quiz here (option 4)
        # ------------------------------------------------------------------
        if choice == "4":
            player = input("Enter player name: ")
            answers = run_quiz(bank, player) #[True,True,False,True,False,False]

        # ------------------------------------------------------------------
        # TODO Scoring team: connect calculate_score / save_result here
        # (works together with running the quiz)
        # ------------------------------------------------------------------

        # ------------------------------------------------------------------
        # TODO Results team: connect show_leaderboard / find_hardest_question /
        # player_statistics here (options 5, 6, 7)
        # ------------------------------------------------------------------

        if choice == "0":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main_menu()
