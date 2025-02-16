import random

birthday_lists = [
    "May this year bring you endless opportunities, great memories, and all the happiness you deserve.",
    "Wishing you a day filled with joy, love, and laughter. Cheers to many more wonderful years ahead! 🎈",
    "May each moment of this year be as special and unforgettable as today!"
]

invest_list = [
    "May your new role bring you success, wisdom, and the strength to inspire those around you.",
    "Wishing you the courage and determination to lead with confidence and make a positive impact.",
    "May this honor be the beginning of a journey filled with achievements, growth, and great leadership."
]

graduate_list = [
    "May this achievement open doors to new opportunities and a future filled with success.",
    "Wishing you the confidence to chase your dreams and the strength to achieve them.",
    "May your journey ahead be filled with learning, growth, and exciting new adventures."
]
print("GREETING-MAKER")
what_greet = int(input("What kind of greeting card do you need? Enter 1 for Birthday, 2 for Investiture Ceremony, 3 for Graduation: "))
name = input("Enter the name: ")
if what_greet == 1:
    age = int(input("What age is he/she turning: "))
    extras = input("Tell her/him something?: ")
elif what_greet == 2:
    role = input("what role is he/she?: ")
    extras = input("Tell her/him somthing: ")
elif what_greet == 3:
    milestone = input("Where is he/she graduation from: ")
    extras = input("Tell her/him something: ")
else:
    print("Enter a valid input!")
if what_greet == 1:
    birthday_again = True
    while birthday_again:
        def birthday_wish():
            greet = random.choice(birthday_lists)
            greeting = f"Happy Birthday, {name}! 🎉\n"
            greeting += f"Congratulations on turning {age} years old! 🎂\n"
            greeting += f"{extras}\n"
            greeting += greet
            print(greeting)
        birthday_wish()
        birth_again = input("Do you want to generate a different message?: Type yes or no: ").lower()
        if birth_again == "no":
            birthday_again = False

elif what_greet == 2:
    invest_again = True
    while invest_again:
        def invest_wish():
            greet = random.choice(invest_list)
            greeting = f"Congratulations, {name}, on your Investiture! 🎖️\n"
            greeting += f"Wishing you success and wisdom in your new role as a {role}. 🌟\n"
            greeting += f"{extras}\n"
            greeting += greet
            print(greeting)
        invest_wish()
        invest_more = input("Do you want to generate a different message?: Type yes or no: ").lower()
        if invest_more == "no":
            invest_again = False
elif what_greet == 3:
    def graduate_wish():
        grad_again = True
        while grad_again:
            greet = random.choice(graduate_list)
            greeting = f"Congratulations, {name}, on your Graduation from {milestone}! 🎓\n"
            greeting += f"May this milestone open doors to a bright future. 🚀\n"
            greeting += f"{extras}\n"
            greeting += greet
            print(greeting)
        graduate_wish()
        grad_more = input("Do you want to generate a different message?: Type yes or no: ").lower()
        if grad_more == "no":
            grad_again = False
print("thank you! come back again")
