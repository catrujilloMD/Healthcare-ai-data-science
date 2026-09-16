# Week 1 Learning Log

## Goal

Create a reproducible learning and portfolio system for Healthcare AI and Data Science.

## Completed

- [x] Created the public GitHub repository
- [x] Configured Git
- [x] Cloned the repository
- [x] Created the initial folder structure
- [x] Created and published the main README
- [x] Completed the Week 3 Practice Lab: Logistic Regression
- [x] Earned 100% on the graded programming assignment
- [x] Confirmed the laboratory passed its tests and grader
- [x] Created public completion evidence without publishing protected assignment code
- [x] Completed the conceptual diabetes-classification healthcare application: [View report](../reports/diabetes-classification-concept.md)
- [ ] Build an original diabetes-classification project using public or synthetic data
- [x] Documented the core Git and GitHub concepts in the main README
- [x] Completed the 0–3 baseline skills assessment
- [x] Created the requirements environment file
- [x] Created the six required GitHub Issues
- [x] Stated the portfolio goal and included all eight required portfolio themes

### Flask API Development

- [x] Completed the IBM Flask lab covering routes, HTTP methods, JSON requests, universally unique identifier parameters, and global error handlers
- [x] Built an original Flask health-check application with `GET /health`
- [x] Added a structured JSON `404` error response
- [x] Manually verified the `200` and `404` responses
- [x] Added two automated tests and confirmed both passed

## Udemy Day 6 — Functions and Reeborg Maze

### Completion Evidence

- [x] Completed the Reeborg Maze final project
- [x] Refactored the solution into clearly named functions
- [x] Reduced repetition in `turn_right()` by using a loop
- [x] Tested a normal maze configuration
- [x] Tested an unexpected randomized configuration
- [x] Tested a boundary/custom configuration
- [x] All three manual tests passed

- [View refactored source code](../src/udemy_day_06_reeborg_maze.py)
- [View manual test record](../tests/udemy_day_06_reeborg_maze_manual_tests.md)

### Three-Sentence Reflection

I learned how functions divide a program into smaller actions with clear responsibilities. I corrected repeated commands and separated maze initialization from the right-hand navigation logic. I can now explain how functions, `while` loops, conditional statements, and Reeborg's sensor functions work together to solve the maze.

**Next action:** Validate, commit, and publish the refactored project, test evidence, and learning-log update.

## Concepts to Review
- Precision
- Recall
- Logistic regression
- Regularization
- Training and testing datasets
- Model overfitting
### Week 1 Competency Ratings

Scale: 1 = beginning, 3 = developing, 5 = independent

| Competency | Rating |
|---|---:|
| Git and GitHub workflow | 3/5 |
| Python functions and loops | 3/5 |
| Logistic regression | 2/5 |
| Flask and API concepts | 2/5 |
| Manual and automated testing | 3/5 |

## Errors and Solutions

- **Problem:** The `python` command pointed to a Python installation that no longer existed.
- **Solution:** Used the working Windows Python launcher with `py` and installed Flask using `py -m pip install flask`.
- **Problem:** The terminal layout made some HTTP headers and automated-test results difficult to see.
- **Solution:** Used compact `curl.exe` commands and expanded the terminal to verify the HTTP status, content type, JSON response, and two passing tests.
- **Lesson learned:** A dependency listed in `requirements.txt` is not automatically installed, and application behavior should be verified with both manual requests and automated tests.

## Weekly Reflection

**What I learned:**  
I learned how to use Git and GitHub to document my work as evidence of my learning. I continued developing my Python skills by practicing functions, and I began working with logistic regression and Flask as part of my machine-learning journey.

**What remains unclear:**  
I need more practice with logistic regression, especially interpreting the model, and with Flask, especially understanding how routes, requests, and responses work together.

**Next action:**  
Review logistic regression and Flask, practice both concepts with small projects, and begin the next week of the curriculum.