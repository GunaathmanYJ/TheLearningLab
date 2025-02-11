print("welcome to determinant calculator")
determinant_wanted = True
while determinant_wanted:
    a1 = int(input("enter the first value: "))
    a2 = int(input("enter the second value: "))
    b1 = int(input("enter the third value: "))
    b2 = int(input("enter the fourth value: "))
    determinant_look = f'| {a1}  {b1} |'
    determinant_look2= f'| {a2}  {b2} |'
    print(determinant_look)
    print(determinant_look2)
    determinant_value = (a1 * b2) - (a2 * b1)
    print(f'The answer for the given determinant is {determinant_value}.')
    recalculating_det = input("Do you want to calculate another determinant? Type yes or no: ").lower()
    if recalculating_det == "no":
        determinant_wanted = False
        print("Thank you. Come again later!")
