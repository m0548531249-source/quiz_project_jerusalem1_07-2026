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

        print("1. Add question")#הוספת שאלה
        print("2. List questions")#רשימת שאלות
        print("3. Remove question")#מחיקת שאלה

        print("4. Run quiz")
        print("5. Leaderboard")
        print("6. Hardest question")
        print("7. Player statistics")
        print("0. Exit")
        choice = input("Choice: ")

        # ------------------------------------------------------------------
        # TODO Question Bank team: connect add_question / list_questions /
        # remove_question here (options 1, 2, 3)
        #bank = get_sample_bank()
        if choice == '1':
            add_question_to_bank(bank)

        elif(choice == '2'):
            print_bank(bank)

        elif(choice == '3'):
            delete_question(bank)
  
        
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


def add_question_to_bank(bank):

    list_of_answ = []
    text = input("enter the text :")
    type = input("is the kind of question bool (tf/muilti)?:")
    number_of_questions(list_of_answ , type)
    correct_index = One_answer(list_of_answ)
    
    bank = add_question(bank, text, list_of_answ, correct_index, type)


def number_of_questions(Answers , type):
    if (type != "tf"):
        while True:
            questions = input("enter the answer :")
            Answers.append(questions)
            more = input("are you done? (yes/no) :")
            if(more == "yes"):
                break
    else:
        Answers.append("True")
        Answers.append("False")
    
def One_answer(Answers):
    while True:
        correct_index = int(input("what iz the correct_index ? :"))
        if(correct_index < 0 or correct_index >= len(Answers)):
            print("the index is err ")
        else:
             break
    return correct_index

def print_bank(bank):
    for x in bank:
        print(x["id"],":",x["text"])
        sum = 0
        for v in x["options"]:
            sum += 1
            print(" ",sum ,".",v,end= "\n")


def delete_question(bank):
    vv = int(input("הזיא הלאש התא הצור קוחמל ? :"))
    lch_fand = False
    for s in bank: 
        if s ["id"] == vv:
            lch_fand = True
            bank.remove(s)
            print("הצלחת!")   
            break
            
    if(lch_fand == False):
        print("שגיאה")
 

if __name__ == "__main__":
    main_menu()





