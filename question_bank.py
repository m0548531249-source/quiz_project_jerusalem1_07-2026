# -*- coding: utf-8 -*-
"""
question_bank.py -- Question Bank team.

Responsibility: manage the question bank (add, list, remove).

Question structure (dictionary):
{
    "id": 1,                              # unique id (number)
    "text": "What is the capital of France?",
    "options": ["Madrid", "Paris"],       # list of options
    "correct_index": 1,                   # index of the correct answer in options
    "wrong_count": 0,                     # times answered incorrectly (for hardest question)
    "type": "multi"                       # "multi" = multiple choice, "tf" = true/false
}

A true/false question is represented as multiple choice with
options = ["True", "False"] and type = "tf". Thanks to this, checking
an answer is identical for both types.

The question bank = a list of such dictionaries.
"""


def add_question(bank, text, options, correct_index, qtype="multi"):#?
    new_question={}# מגדיר מילון ריק

    id=len(bank)+1# מוסיך ל iD את האורך של bank  (אבל ה bank ריק ?!)

    wrong_count=0 # מגדיר סוג של מאגר ששווה ל 0

    new_question["id"]=id  # מוסיף למילון את המפתח שהוא "id" שערך שלו שווה ל id

    new_question["text"]=text # מוסיף למילון את המפתח שהוא "text" שערך שלו שווה ל text

    new_question["options"]=options # מוסיף למילון את המפתח שהוא "options" שערך שלו שווה ל options

    new_question["correct index"]=correct_index # מוסיף למילון את המפתח שהוא "icorrect indexd" שערך שלו שווה ל correct index

    new_question["wrong_count"]=wrong_count # מוסיף למילון את המפתח שהוא "wrong_count" שערך שלו שווה ל wrong_count

    new_question["type"]=qtype # מוסיף למילון את המפתח שהוא "type" שערך שלו שווה ל type

    bank.append(new_question)# מוסיך לרשימה את המילון
    return bank # מגדיר למה אני רוצה לקרוא

    """
    Add a new question to the bank.

    Parameters:
        bank          -- the list of questions (modified in place)
        text          -- the question text
        options       -- the list of options
        correct_index -- index of the correct answer
        qtype         -- "multi" or "tf"

    Compute a unique id (e.g. number of existing questions + 1) and set
    wrong_count to 0.
    Returns: the question dictionary that was created.
    """
 




def list_questions(bank):
    """
    Display every question in the bank (id + text + options).
    Useful for management and editing. If the bank is empty, print a
    suitable message.
    """
def list_questions(bank):
    if len(bank) ==0:
        print("no questions at the bank")
    else:
        for questions in bank:
            print(questions)
            print(len(questions["options"]))
    


def remove_question(bank, qid):
    # for question in bank:
    #         if question:



    """
    Remove the question whose id equals qid from the bank.

    Returns: True if found and removed, otherwise False.
    Hint: loop over the list and find the question with the matching id.
    """
    pass  # TODO Question Bank team
