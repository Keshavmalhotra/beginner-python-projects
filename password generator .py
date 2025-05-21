import random
import pyperclip
def password():
 user_input= None
 user_input2= None
 user_input3= None
 while True:
  try:
   user_input = int(input("how much letters you need on your password:"))
   user_input2= int(input("how  much numbers you need on your password:"))
   user_input3=  int(input("how much symbols  you need on your password:"))
  except ValueError:
   print("the input must be number!")
   continue  
  user_input4= input("do  you want first carictor to be uppercase?  y for yes, n for no:")
  count= user_input + user_input2 + user_input3
  if user_input<0 or user_input2<0 or user_input3<0 or user_input==0 and user_input2==0 and user_input3==0:
   print("The method is incorrect!")
   continue
  elif user_input==0 and user_input2==0 and user_input3>0:
   print("password  with only  simbels   cannot be made")
   continue
  elif count<6 or count>128:
   print("the password length should not be <than 6 characters, or >than  128 characters..")
   continue
  elif user_input4!= "y" and user_input4!= "n":
   print("invalid input!")
   continue
  numbers= "0123456789"
  chars= "abcdefghijklmnopqrstuvwxyz"
  symbols= "@!#$%^&*()_+=/.,:;|\<>[]{}"
  password_numbers= random.choices(numbers, k= user_input2)
  password_characters= random.choices(chars, k= user_input)
  password_symbols= random.choices(symbols, k= user_input3)
  all= password_characters + password_numbers + password_symbols
  all_joind= "".join(all)
  result= random.choices(all_joind, k= count)
  while not( result[0] in password_characters) and user_input>0:
   result= random.choices(all_joind, k= count)
  f_result= "".join(result)
  if user_input4== "y":
   f_result2= f_result.capitalize()
   pyperclip.copy(f_result2)
   print(F"your password is:{f_result2} it is  copied to your clipboard.")
  else:
   pyperclip.copy(f_result)
   print(F"your password is:{f_result} it is  copied to your clipboard.")
password()