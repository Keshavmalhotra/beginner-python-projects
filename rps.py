import random
import time

elements= ["Rock", "Paper", "Scissors"]
while True:
 random_selection= random.choice(elements)

 try:
  user_input= input(
  f"Your selection:\n"
  f"Type 'r' for {elements[0]}\n"
  f"Type 'p' for {elements[1]}\n"
  f"Type 's' for {elements[2]}\n"
  f"Type 'q' for exiting  the game\n"
  f"Enter your choice: "
  ).lower()
 except EOFError:
  print("No input, exiting.")
  break
 
 if user_input!= "r" and user_input!= "p" and user_input!= "s" and  user_input!= "q":
  print("Invalid input!")
 elif user_input== "r" and random_selection==  elements[1] or user_input== "p" and random_selection==  elements[2] or user_input== "s" and  random_selection== elements[0]:
  print(f"Oh no, you lose! Computer selected {random_selection}.")
 elif user_input== "r" and random_selection== elements[0] or user_input== "p"  and random_selection== elements[1] or user_input== "s" and random_selection== elements[2]:
  print("It's a draw!")
 elif user_input== "q":
  print("exiting!")
  time.sleep(0.5)
  break
 else :
  print(f"You win! Computer selected {random_selection}.")
 time.sleep(0.5)