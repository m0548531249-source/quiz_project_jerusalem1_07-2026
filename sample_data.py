# -*- coding: utf-8 -*-
"""
sample_data.py -- a sample question bank for testing.

This file is provided ready-made -- nothing to implement here.
You can import get_sample_bank() to test your code without entering
questions by hand.
"""


def get_sample_bank():
    """Return a list of sample questions (multiple choice and true/false)."""
    return [
        {
            "id": 1,
            "text": "What is the capital of France?",
            "options": ["Madrid", "Paris", "Rome", "Berlin"],
            "correct_index": 1,
            "wrong_count": 0,
            "type": "multi",
        },
        {
            "id": 2,
            "text": "Python is a programming language.",
            "options": ["True", "False"],
            "correct_index": 0,
            "wrong_count": 0,
            "type": "tf",
        },
        {
            "id": 3,
            "text": "What is 7 * 6?",
            "options": ["42", "36", "48", "40"],
            "correct_index": 0,
            "wrong_count": 0,
            "type": "multi",
        },
        {
            "id": 4,
            "text": "The print function is used to read input from the user.",
            "options": ["True", "False"],
            "correct_index": 1,
            "wrong_count": 0,
            "type": "tf",
        },
        {
            "id": 5,
            "text": "Which data structure stores key-value pairs?",
            "options": ["list", "string", "dictionary", "tuple"],
            "correct_index": 2,
            "wrong_count": 0,
            "type": "multi",
        },
    ]

#שאלה = : טקסט של השאלה + אוסף שך טקסט שמיצג תשובות + המיקום שך התשובה הנכונה + סוג השאלה  + כמה פעמים ענו לא נכון על השאלה 