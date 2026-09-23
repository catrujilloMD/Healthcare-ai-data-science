# Learning from today's Lesson: Hangman Game

## Input: What does the player enter?
a//The player enters a letter.
## Method: How do the while loop, for loop, and conditions process that guess?
a// While will repeat turns until game_over becomes True. Next,
for evaluates each character in the chosen word and builds the display. Conditions decide whether to reveal letters, deduct a life, warn about repeated guesses, or end the game.
## Output: What does the game display?
a//The game displays either a letter that belongs to the spot ('_') or takes off a life and states that the letter is wrong if the letter guessed by the user is not correct.
## Limitation: What happens if someone enters two letters or presses Enter without typing? If you haven’t tested this, write “Not yet tested.”
a//The system has been tested and when the user enters 2 letters it outputs "You guessed (double letter), that's not in the word. You lose a life."When the user only "enters" in the guess it triggers the already-guessed warning. The game does not validate that the input contains exactly one letter.

## Verified results:
- Winning displays “YOU WIN” and stops.
- Losing reveals the word and stops.
- Repeating a guess displays a warning without deducting another life.

## Correction I learned:
Had to restore display = "" loop in order to the program to work properly. I had to restores files (art and words) in the old folder so that the file Hangman_game could run properly.

## Reflection sentences: 
- What you learned: How while, for loops and conditionals work applied into a game.
- What you corrected or simplified: I corrected the display "" section loop simplifying the code.
- limitation remains: The program still lacks single-letter input validation: `aa` cost one life in my test, while repeated empty input triggered an already-guessed warning without deducting another life.

## Next action
Commit the Hangman project and evidence, then begin Week 2 Day 3.