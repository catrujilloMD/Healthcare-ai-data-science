# Week 2 — Day 3: Python and Flask

## Course completion
- Course: IBM Developing AI Applications with Python and Flask
- Completed: October 7, 2026
- Final grade: 88.12%
- All three modules completed; certificate received.

## Evidence
- [Certificate](../reports/course-evidence/ibm-python-flask-certificate.pdf)
- [Course completion screenshot](../reports/course-evidence/ibm-python-flask-course-completed.png)

## Retrieval practice
Completed Flask questions covering routes, GET requests,
status-route limitations, input validation, and test cases.

## Project explanation
- Input: A sentence entered by the user for emotion analysis.
- Method: Flask connects the URL path to a Python function using
  @app.route(...). The application sends the text to the emotion
  analysis service and processes its response.
- Output: Scores for anger, disgust, fear, joy, and sadness,
  together with the dominant emotion.
- Limitation: The application depends on an external service.
  Its predictions may misinterpret the meaning or context of text.

## Reflection
- One thing I learned: You can learn how program an app via python that connects the information in flask, an input from a user, send to a route @app.route(...) and then delivers the comunication as an output in the website. 
- One error I encountered: syntax and indentation errors like last line 37 in server.py needed 4 spaces to get a score 10/10 and the ' cd" while checking the location of the file.
- How I corrected it: Just fixed them after the output explaination.
- Need frequent practice.

## Remaining verification
- Check input validation.
- Confirm two tests and their results.
- Include an example client request.
- Document the healthcare application using synthetic data.

## Next action
Review the Emotion Detector project against the remaining
Day 3 requirements, then commit and link the verified evidence.
## Project verification and evidence

- Completed the IBM Flask course and received the certificate.
- Added local validation for missing, empty, and whitespace-only input.
- Passed all three Flask route tests using simulated Watson responses.
- Verified that an empty request through curl returns HTTP 400.
- Tested fictional clinic feedback: the Watson connection timed out,
  so no emotion scores were obtained locally.

Project commit:
https://github.com/catrujilloMD/oaqjp-final-project-emb-ai/commit/5dc779b

Next improvement: handle external-service connection failures
and return HTTP 503.