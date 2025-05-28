import random
import time
user_name= input("Type your name: ")
while len(user_name)>18 or len(user_name)<4 or user_name== "":
 if user_name== "":
  print("the name  cannot be empty")
  time.sleep(0.1)
  user_name= input("Type your name: ")
 elif len(user_name)>18:
  print("You can't use a name longer than 18 characters.")
  time.sleep(0.1)
  user_name= input("Type your name: ")
 elif len(user_name) <4:
  print("You can't use a name smaller than 4 characters.")
  time.sleep(0.1)
  user_name= input("Type your name: ")
bot_names= ["Arjun", "Priya", "Rohan", "Ananya", "Rahul", "Sneha",  "simran"]
bot_name= random.choice(bot_names)
user_score= 0
bot_score= 0
snakes= [16, 46, 49, 62, 64, 74, 89, 92, 95, 99]
snake_ends= [6, 25, 11, 19, 60, 53, 68, 88, 75, 7]
ladders= [2, 4, 8, 21, 28, 36, 51, 71, 78, 87]
ladder_ends= [38, 14, 31, 42, 84, 44, 67, 91, 98, 94]
welcome_message= F"Hello, {user_name}!, Welcome to Snake and Ladders game, Your opponent is: {bot_name}."
print(welcome_message)
while user_score<100 and bot_score<100:
 try:
  time.sleep(0.5)
  action= input("Type r to roll the dice, s to see snake positions, l to see ladder positions: ")
 except EOFError:
  print("No input: exiting...")
  break
 action2= action.lower()
 if action2== "r":
  user_roll= random.randint(1,6)
  user_score+= user_roll
  if user_score>100:
   user_score-= user_roll
  elif user_score== 100:
   print(f"Congratulations, {user_name}, for winning the game!  {bot_name} was defeated.")  
   time.sleep(5)
   break
  print(f"{user_name} rolled the dice.  {user_name} got {user_roll}.  {user_name}'s score is {user_score}.")
  for i in snakes:
   index= snakes.index(i)
   if user_score== i:
    user_score= snake_ends[index]
    print(F"Aww, snake bit {user_name}, {user_name} score is now {user_score}")
  for x in ladders:
   index2= ladders.index(x)
   if user_score== x:
    user_score= ladder_ends[index2]
    print(F"Wow! {user_name} climbed to {user_score}")
 elif action2== "s":
  print(snakes)
  continue
 elif action2== "l" :
  print(ladders)
  continue
 elif action2!= "r" or action2!= "s"  or action2!= "l":
  print("invalid input!")
  continue
 bot_roll= random.randint(1,6)
 bot_score+= bot_roll
 if bot_score>100:
  bot_score-= bot_roll
 print(f"It's {bot_name}'s turn. {bot_name} rolled the dice and got {bot_roll}. {bot_name}'s score is {bot_score}.")
 for y in snakes:
  index3= snakes.index(y)
  if bot_score== y:
   bot_score= snake_ends[index3]
   print(F"Aww, snake bit {bot_name}, {bot_name} score is now {bot_score}")
 for z in ladders:
  index4= ladders.index(z)
  if bot_score== z:
   bot_score= ladder_ends[index4]
   print(F"Wow! {bot_name} climbed to {bot_score}")
 if bot_score== 100:
  print(f"Congratulations, {bot_name}, for winning the game!  {user_name} was defeated.")  
  time.sleep(5)
  break