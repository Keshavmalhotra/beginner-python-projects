import random as r
import time
welcome_mesege= "Hello, welcome to the Guess the Number mini game!"
level = 1
goal_level= level+1
points= 0
numbers_range= 10
need_points= 10
print(welcome_mesege)
time.sleep(0.5)
while True:
 if points== need_points:
  level+= 1
  goal_level_level= level+1
  need_points*= 2
  points= 0
  numbers_range+=10
  print(f"Congratulations! You have reached level {level}. You need {need_points} more points to reach level {goal_level}.")
 try:
  user_input= int(input(F"type the number  bitween 0 to  {numbers_range}"))
 except ValueError:
  print("invalid input!")
  time.sleep(0.5)
  continue
 except EOFError:
  print("No input was provided. The game is ending.")
  break
 time.sleep(0.5)
 numbers= r.randrange(0,numbers_range)
 if user_input<0:
  print("Negative inputs will not be accepted.")
  continue
 elif user_input== numbers:
  points+= 2
  print(f"Correct answer! Your level is {level}, your points are {points}. You need {need_points} points to reach level {goal_level}.")
 elif user_input!=  numbers:
  print(f"Incorrect answer! The correct answer is {numbers}.")