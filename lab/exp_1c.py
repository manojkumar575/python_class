# Determine the senior citizonship

import datetime

name = input("Enter your name: ")
yob = eval(input("Enter your year of birth: "))

current_year = datetime.datetime.now().year

age = current_year - yob

if age >= 60:
    print(f"{name} is {age} years old and senior citizon")
else:
    print(f"{name} is {age} years old and not a senior citizon")