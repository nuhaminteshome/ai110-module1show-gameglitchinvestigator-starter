# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1. I noticed that that after submitting my last attempt, the number of attempts left said 1 but I was expecting it to be 0.

2. The hints were not correct. For one game, the secret number was 38. I first guessed number 10, but the hint told me to "Go lower". In another game, the hint told me to go lower than 5 I did and guessed 0 and it told me to go lower again. I was expecting it to say 0 is not an appropriate guess since we have to guess a number from 1 to 100.

3. The game ends after 6 attempts, although it shows I had 7 attempts.

4. After clicking on the New Game button, the game doesn't restart. The only thing that changes is the number of attempts left. When you submit a guess for a new game, it doesn't work. I was expecting the game to reset and when I guessed 1 number the Submit guess button would work and the number of attempts would be reduced by 1.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess of 10 | Since the secret number was 38, the hint should be to "Go higher"| The hint displayed "Go lower" | none |
|Click on the New Game button| The game should restart, the Submit Guess button is working and the Attempts left number changes as guesses are made | Attempts left number restarts to original but Submit guess button doesn't work, which makes a user unable to make a guess.| none |
|Six guesses made| Since 7 attempts are available, 1 attempt should be left for user to make a guess |Although it says 1 attempt is left, the game stops after the 6th attempt| none |






---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

I used ClaudeAI for this project.

Correct AI suggestion:

- Claude suggested that the parse_guess function was missing a range check and the hints in the check_guess function are swapped. I verified it by fixing the code and making sure it works on the Streamlit app and using pytest.

Incorrect AI suggestion
- After fixing my bug #1 and #3, the AI suggested that the attemps left number will accurately show the correct number. However, after playing the game again I noticed that the attempts started decreasing after the 2nd guess, not the 1st. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided whether a bug was really fixed by playing the game multiple times and using different test cases. One test I ran manually was to check whether the Attempts left was displaying the correct number as I made a guess. I noticed there was still an error because as I submitted a guess, I wouldn't see the attempts count decrease. I was only able to see it after the 2nd attempt. This showed me another bug in my code and I used AI to help me understand it better. I was able to fix it by adding st.rerun() which will make reduce the attempt count right when the user submits a guess.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would explain it to them by stating that Streamlit doesn't remember the things you were doing while using the system unless it is stored somewhere else in the program, which is called a session state. So, if it's not stored in a session state, everytime you run the program, Streamlit forgets what you were doing.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse in future projects is documenting bugs first, along with their expected and actual behaviour. After completing this project, I'm now cautious about AI generated code and understand why it's important to double-check code before deploying it for production.
