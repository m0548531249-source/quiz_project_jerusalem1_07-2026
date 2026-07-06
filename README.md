# Quiz System 🎯

A team project in Python for practicing functions and collaborative work
with Git and GitHub. The system manages a question bank (multiple choice and
true/false), runs quizzes, computes scores, and shows a leaderboard -- all in
memory, without files and without OOP.

## Coding constraints

- **Do not** use `sum`, `max`, `min` -- implement all such logic manually with loops.
- **No** classes (OOP) -- use dictionaries and lists only.
- **No** file reading/writing -- all data is kept in memory during the run.

## Project structure

| File | Description | Owner team |
|------|-------------|------------|
| `main.py` | Main menu -- the integration point (**shared**) | all teams |
| `question_bank.py` | Manage the question bank | Question Bank |
| `quiz_engine.py` | Run the quiz and check answers | Engine |
| `scoring.py` | Compute score and save results | Scoring |
| `results.py` | Leaderboard, hardest question, statistics | Results |
| `sample_data.py` | Sample question bank (ready) | -- |

## Team breakdown

**Question Bank team** -- `add_question`, `list_questions`, `remove_question`
**Engine team** -- `check_answer`, `run_quiz`
**Scoring team** -- `calculate_score`, `save_result`
**Results team** -- `show_leaderboard`, `find_hardest_question`, `player_statistics`

Each team has 3-4 members. Even when a team has more members than functions,
there is work for everyone:
- One member per main function.
- Another member owns **testing** (write test scenarios using `sample_data`).
- Another member owns **integration** -- wiring the team's functions into
  `main.py` and helping resolve the merge conflict.

## Data model

**Question** (dictionary):
```python
{
    "id": 1,
    "text": "What is the capital of France?",
    "options": ["Madrid", "Paris", "Rome"],
    "correct_index": 1,
    "wrong_count": 0,
    "type": "multi"   # or "tf" for a true/false question
}
```

**Bank** = a list of questions. **Results** = a list of `{"player": str, "score": int}`.

## Run

```
python main.py
```

## How do we work together?

See `CONTRIBUTING.md` for the full instructions on Fork, Branch, and Pull Request.
