Python Mini Projects – Beginner Level
These are simple Python projects built during the learning process. Each project demonstrates core concepts like input handling, randomness, file operations, and basic logic.
 
1. Password Generator
Generates a strong, customizable password based on user input.
Features:
• 
Choose number of letters, numbers, and symbols.
• 
Option to start the password with an uppercase letter.
• 
Input validation to avoid weak combinations.
• 
Copies the password to clipboard automatically using pyperclip.
 
2. Guess the Number – Mini Game
A terminal-based number guessing game that includes leveling mechanics.
How it works:
• 
Guess a number in a range.
• 
Each correct guess gives 2 points.
• 
Level increases as more points are earned.
• 
With each level, the guessing range expands and point requirement increases.
 
3. Temp Folder Cleaner
Script to delete system temporary folders.
How to use:
1. 
Before running, open the script and update the paths list with your system's temp folder paths in dubble quotes
• 
Example:
• 
C:/Users/YourUsername/AppData/Local/Temp
• 
C:/Windows/Temp
2. 
Run the script. It will try to delete the folders listed.
• 
Skips folders it doesn't have permission to delete.
• 
Windows will recreate the temp folders automatically if needed.
Note: This script is still under improvement. Some files may not delete due to permission or being in use.
 
4. Toss Game
A basic coin toss simulator.
How it works:
• 
User picks 1 for heads, 2 for tails.
• 
Script randomly selects the outcome.
• 
Displays result after a short delay.

5. Snake and Ladders - Python Console Game 🎲🐍🪜

A fun console-based implementation of the classic Snake and Ladders game. Play against a randomly chosen Indian-named bot. Avoid snakes, climb ladders, and be the first to reach 100!

## Features

- 🎲 Dice rolling mechanics for both user and bot
- 🐍 Snakes that pull you back
- 🪜 Ladders that boost your score
- 👤 Player name input with validation (4–18 characters)
- 🤖 Random bot opponent selection
- 🎉 Win/lose messages with a 5-second delay before exiting
- 🔄 Input options: 
  - `r` to roll dice
  - `s` to view snake positions
  - `l` to view ladder positions

## Rules

- First to exactly **100 wins**
- If a dice roll overshoots 100, the move is cancelled
- Landing on a snake drops your score
- Landing on a ladder boosts your score

6. # Rock Paper Scissors (RPS) – Command Line Game 🎮

This is a simple and interactive command-line implementation of the classic **Rock, Paper, Scissors** game written in Python.

## 🧠 Game Rules

- **Rock** beats **Scissors**
- **Scissors** beats **Paper**
- **Paper** beats **Rock**
- Same choices result in a **Draw**

## ▶️ How to Play

1. Run the `rps.py` script using Python 3.
2. You’ll be prompted to enter:
   - `r` for **Rock**
   - `p` for **Paper**
   - `s` for **Scissors**
   - `q` to **Quit the game**
3. The computer randomly selects its choice.
4. The result (Win / Lose / Draw) is shown.
5. The game runs in a loop until you type `q` to exit.

## 🖥️ Example

```bash
Your selection:
Type 'r' for Rock
Type 'p' for Paper
Type 's' for Scissors
Type 'q' for exiting the game
Enter your choice: s
You win! Computer selected Paper.
