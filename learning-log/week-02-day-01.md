# Week 2 — Day 1: Flask lab

## Completed
- Completed the IBM Flask calculator lab with guidance.
- Verified addition, subtraction, and multiplication in the browser.
- Added and tested /status: "Calculator is running".
- Saved the project to GitHub in commit d494b62.
- Completed Module 2 of the Coursera Flask course.
- Added /clinic/status and tested it locally in the browser.
- Observed the response: "Demo clinic service is running".
- Completed the Flask knowledge check after feedback.

## Input → Method → Output → Limitation
- Input: Two numbers and a selected mathematical operation.
- Method: A Flask route reads the numbers and calls a calculation function.
- Output: The calculation result is returned to the browser.
- Limitation: Handling missing or invalid inputs still needs verification.

## What I learned
A route connects a URL path to a Python function.
The return statement supplies the response sent to the browser.

## Error and correction
I omitted the equals sign in result = a * b.
Adding it corrected the assignment syntax.

## Clinic route explanation
- Input: A GET request to /clinic/status.
- Method: @app.route connects the path to clinic_status().
- Output: The browser displays "Demo clinic service is running".
- Limitation: This fixed message does not check a database or appointment system.

## Additional correction
I initially confused defining a function with registering a route.
def defines the function; @app.route connects it to a URL path.

## Next action
Begin Week 2, Day 2: Udemy 100 Days of Code, Day 7.

## Project
[Flask calculator](../Week-02-flask-calculator/)
