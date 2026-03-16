# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game appeared as a basic Streamlit number guessing app with a sidebar for difficulty settings, a text input for guesses, and debug info showing the secret number, attempts, score, and history. However, it was frustratingly unplayable right from the start, with the interface looking functional but the logic completely broken. Two concrete bugs I noticed immediately were that the hints were backwards—for example, guessing higher than the secret would tell me to "Go HIGHER!" instead of lower—and the secret number seemed unstable, sometimes causing comparison errors that made winning impossible even with correct guesses.

---

## 2. How did you use AI as a teammate?

- I used GitHub Copilot and Claude as my AI tools for this project, leveraging its code suggestions, debugging assistance, and test generation capabilities.
- One correct AI suggestion was to simplify the `check_guess` function by removing the try/except block and ensuring both guess and secret are always converted to integers for consistent comparisons. I verified this by running the Streamlit app, making guesses, and confirming that hints were now accurate (e.g., guessing 60 against a secret of 50 correctly showed "Too High" with "Go LOWER!"), and by running pytest tests which all passed.
- One incorrect or misleading AI suggestion was the original code's hint logic, where for a "Too High" guess, it suggested "Go HIGHER!" instead of "Go LOWER!", which was backwards. I verified this by playing the game initially, where hints were lying (e.g., guessing higher than the secret prompted to go even higher), leading to confusion and inability to win consistently.

---

## 3. Debugging and testing your fixes

- I decided a bug was really fixed by first running the Streamlit app manually to play the game, checking if I could win, if hints were correct, and if the history reset on new games. Then, I ran automated pytest tests to ensure the logic functions worked as expected.
- One test I ran was the new pytest test `test_guess_handles_string_inputs` in `tests/test_game_logic.py`, which verified that `check_guess` correctly handles string inputs by converting them to integers, preventing the type inconsistency bug. It showed that the function now returns correct outcomes even with mixed input types, confirming the fix for the original comparison errors.
- Yes, AI helped me design the test by suggesting to add a specific test case that targets the type bug, ensuring robustness against string inputs, and I verified it by running pytest and seeing it pass alongside existing tests.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
