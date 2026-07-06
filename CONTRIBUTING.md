# Contributing Guide

The project follows the **Fork & Pull** model (also called the "triangular
workflow") -- exactly like real open source projects.

## Workflow

```
        Instructor's repo (upstream)
                 ▲
                 │  (5) Team lead opens a PR back to the instructor
                 │
          Team lead's fork
            ▲          ▲
            │          │  (3) Team member opens a PR to the team lead's fork
         branch      branch
        (member A)   (member B)
```

## Steps

### For the team lead
1. **Fork** the instructor's repo (the Fork button on GitHub).
2. Add your team members as **Collaborators** on your fork:
   `Settings → Collaborators → Add people`.
3. Clone your fork to your machine:
   ```
   git clone git@github.com:<your-username>/quiz-project.git
   ```
4. Set the instructor's repo as `upstream` so you can sync:
   ```
   git remote add upstream git@github.com:<instructor-username>/quiz-project.git
   ```

### For a team member
1. Clone the **team lead's** fork (not the instructor's).
2. Create a new **branch** for your task:
   ```
   git checkout -b feature/add-question
   ```
3. Work only on your team's file, commit, and push:
   ```
   git add question_bank.py
   git commit -m "Implement add_question"
   git push origin feature/add-question
   ```
4. Open a **Pull Request** to the `main` of the team lead's fork, with a clear
   description of what you did.

### Back to the team lead
5. Review the team's PRs and merge them into the fork's `main`.
6. Sync the fork with the instructor (`Sync fork` on GitHub, or
   `git pull upstream main`).
7. Open a **Pull Request** from your fork → the instructor's repo.

## Golden rules

- **Never** push directly to `main`. Everything goes through a branch and a PR.
- The branch name describes the task: `feature/<action-name>`.
- Every PR includes a description: what was implemented and how you tested it.
- Each member works on **their team's file** only -- to avoid unnecessary conflicts.

## About the intentional merge conflict ⚠️

The file `main.py` is **shared** -- every team adds its function calls to it.
Therefore, when several teams merge to the instructor, a conflict in `main.py`
is likely.

**This is intentional and it is a learning opportunity.** When it happens:
1. Run `git pull upstream main` to get the latest changes.
2. Git marks the conflict area with `<<<<<<<`, `=======`, `>>>>>>>`.
3. Edit `main.py` by hand so it contains the calls of **all** teams (do not
   pick just one side!).
4. Remove the conflict markers, commit, and push.

Don't be afraid of a conflict -- resolving one is an important skill, not a bug.
