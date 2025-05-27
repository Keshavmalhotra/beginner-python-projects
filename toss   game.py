import random
import time

welcome_message = "Hello, welcome to the Toss Game:"
print(welcome_message)
time.sleep(1.00)

while True:
 try:
  user_input = int(input("What do you like to pick, 1 for Heads, 2 for Tails:"))
 except ValueError:
  print("Invalid input!")
  continue
 except EOFError:
  print("No inputs, exiting..")
  break
 if user_input > 2:
  print("Invalid input!")
  continue
 outcomes = ["Heads", "Tails"]
 time.sleep(0.5)
 result = random.choice(outcomes)
 print(f"The result is {result}:")