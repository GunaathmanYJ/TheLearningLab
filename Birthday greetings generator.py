
import random
from operator import truediv

wising_lists = ["May this year bring you endless opportunities, great memories, and all the happiness you deserve." ,
                "Wishing you a day filled with joy, love, and laughter. Cheers to many more wonderful years ahead! 🎈",
                "May each moment of this year be as special and unforgettable as today!"]
print("Welcome to birthday greeting maker!")
name = input("enter the name: ")
age = int(input("what age is he/she turning: "))
extras = input("Do you want to tell her/him something?")
birthday_greet = True
while birthday_greet:
    def birthdaywish():
        greet = random.choice(wising_lists)
        greeting = f"Happy Birthday, {name}! 🎉\n"
        greeting += f"Congratulations on turning {age} years old! 🎂\n"
        greeting += f"{extras}\n"
        greeting += greet
        print(greeting)
    birthdaywish()
    one_more = input("do you want to generate another? type yes or no:\n").lower()
    if one_more == "no":
        birthday_greet = False
        print("\n" * 100)
        print("Thank you. come back again!")
