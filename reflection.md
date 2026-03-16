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

The secret number kept changing in the original app because Streamlit reruns the entire script every time there's a user interaction, like clicking a button or entering input, and without using session state, variables like the secret get reset to new random values on each rerun. I'd explain Streamlit reruns to a friend by saying that unlike traditional apps where code runs once and waits for events, Streamlit treats every interaction as a full script restart from the top—it's like the app "refreshes" itself constantly to update the UI, which is efficient for data apps but tricky for games. Session state is like a persistent backpack that carries your important variables (like the secret number or score) across these reruns, so they don't get lost. The change I made that finally gave the game a stable secret number was initializing and storing the secret in `st.session_state.secret` only when it wasn't already set, ensuring it persists across reruns instead of regenerating randomly.

---

## 5. Looking ahead: your developer habits

- One habit I want to reuse is thoroughly testing fixes with both manual gameplay and automated pytest tests, including edge-case scenarios, to ensure bugs are truly resolved and prevent regressions.
- Next time I work with AI on a coding task, I would immediately test any logic-related suggestions (like comparisons or hints) manually in the app before assuming they're correct, rather than just reviewing the code, because the original AI-generated hints were backwards and misleading, leading to wasted time.
- This project made me realize that AI-generated code, while fast to produce, often contains subtle logical errors that can make an app unusable, so I now approach it with more skepticism and prioritize hands-on verification over blind trust.
