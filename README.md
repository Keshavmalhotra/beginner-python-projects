# Python Learning Projects

This repository contains three mini-projects created while learning Python. Each project focuses on core programming concepts like input/output, conditionals, loops, randomness, and system-level operations.

---

## 1. Password Generator

A flexible password generator that allows users to choose:
- Number of letters, numbers, and symbols
- Whether the first character should be uppercase
- Automatically copies the password to your clipboard

### Features:
- Input validation
- Randomized character selection
- Clipboard support with `pyperclip`

---

## 2. Guess the Number - Mini Game

A number guessing game where:
- The range increases with each level
- You need points to level up
- Incorrect guesses show the correct answer
- Game ends on EOF or invalid input repeatedly

### Features:
- Dynamic difficulty scaling
- Clean input validation
- Motivational feedback during gameplay

---

## 3. Temp Folder Cleaner

A utility script that deletes system temp folders to clean up junk files.

### ⚠️ Important Before Use:
You must **manually enter** the full paths of your temp folders inside the script. Open the `.py` file and add the paths as strings inside the `paths = ["", ""]` list.

Example:
```python
paths = ["C:/Users/YourName/AppData/Local/Temp", "C:/Windows/Temp"]
How to Run:
python temp_cleaner.py
Notes:
• 
Files that require admin access or are in use will be skipped.
• 
Windows will recreate deleted temp folders automatically if needed.
• 
This script is simple and still under improvement; it may not remove all junk.
 
Disclaimer
These projects were made during the learning phase. The code may not follow best practices and is subject to updates and improvements over time.
