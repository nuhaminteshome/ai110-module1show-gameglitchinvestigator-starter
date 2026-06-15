# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- This game is intended to let users guess a number from 1 to 100. 
- When I first played the game, I noticed there were a few bugs that showed the game was not working properly. Here a few bugs:
1. I noticed that that after submitting my last attempt, the number of attempts left said 1 but I was expecting it to be 0.

2. The hints were not correct. For one game, the secret number was 38. I first guessed number 10, but the hint told me to "Go lower". In another game, the hint told me to go lower than 5 I did and guessed 0 and it told me to go lower again. I was expecting it to say 0 is not an appropriate guess since we have to guess a number from 1 to 100.

3. The game ends after 6 attempts, although it shows I had 7 attempts.

4. After clicking on the New Game button, the game doesn't restart. The only thing that changes is the number of attempts left. When you submit a guess for a new game, it doesn't work. I was expecting the game to reset and when I guessed 1 number the Submit guess button would work and the number of attempts would be reduced by 1.
- Here are the things I did to fix these issues:
Fix 5 game logic bugs and refactor helpers into logic_utils
- parse_guess: add range check to reject guesses outside 1–100
- check_guess: fix swapped hint messages (Go HIGHER/LOWER were reversed)
- Fix attempts display off-by-1 by initializing attempts to 0
- Fix new game not resetting status to "playing", leaving game stuck
- Add st.rerun() after submit so attempts counter updates immediately
- Save hint to session_state so it survives the st.rerun() refresh


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 50
2. Game returns "Go HIGHER"
3. User enters a guess of 70 → "Go LOWER"
4. Score updates correctly after each guess
5. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
