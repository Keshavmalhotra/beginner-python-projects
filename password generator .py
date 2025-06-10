import random
import pyperclip

def generate_password():
 user_letters = None
 user_numbers = None
 user_symbols = None
 while True:
  try:
   user_letters = int(input("How many letters do you need in your password: "))
   user_numbers = int(input("How many numbers do you need in your password: "))
   user_symbols = int(input("How many symbols do you need in your password: "))
  except ValueError:
   print("The input must be a number!")
   continue  
  except EOFError:
   print("No inputs, exiting!")   
   break

  first_upper = input("Do you want the first character to be uppercase? y for yes, n for no: ")
  total_length = user_letters + user_numbers + user_symbols

  if user_letters < 0 or user_numbers < 0 or user_symbols < 0 or user_letters == 0 and user_numbers == 0 and user_symbols == 0:
   print("The method is incorrect!")
   continue
  elif user_letters == 0 and user_numbers == 0 and user_symbols > 0:
   print("Password with only symbols cannot be made")
   continue
  elif first_upper != "y" and first_upper != "n":
   print("Invalid input!")
   continue
  elif total_length < 6 or total_length > 128:
   print("The password length should not be less than 6 characters or greater than 128 characters.")
   continue

  digits = "0123456789"
  letters = "abcdefghijklmnopqrstuvwxyz"
  special_chars = "@!#$%^&*()_+=/.,:;|<>[]{}"

  selected_numbers = random.choices(digits, k=user_numbers)
  selected_letters = random.choices(letters, k=user_letters)
  selected_symbols = random.choices(special_chars, k=user_symbols)

  combined = selected_letters + selected_numbers + selected_symbols
  shuffled = random.sample(combined, k=len(combined))

  while shuffled[0] not in selected_letters and user_letters>0:
   shuffled = random.sample(combined, k=len(combined))

  final_password = "".join(shuffled)

  if first_upper == "y":
   capitalized_password = final_password.capitalize()
   pyperclip.copy(capitalized_password)
   print(f"Your password is: {capitalized_password} — it has been copied to your clipboard.")
  else:
   pyperclip.copy(final_password)
   print(f"Your password is: {final_password} — it has been copied to your clipboard.")

generate_password()
