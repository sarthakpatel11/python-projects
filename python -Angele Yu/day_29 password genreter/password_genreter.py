import random
from typing import final


password_letter = 10
# int(
#     input("Enter how many letters password you want ? (8 to 10)"))
password_number = 3
# int(
#     input("Enter how many number you want ? (1 to 3 allowed)"))
password_special_character = 2
# int(input(
#     "Enter how many special character you want ? (1 to 2 is allowed)"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_character = ['@', '#', '$', '%', '&']

# print(password_letter, password_number, password_special_character)
password = []

if password_letter >= 8 and password_letter <= 10:
    if password_number >= 1 and password_number <= 3:
        if password_special_character == 1 or password_special_character == 2:
            if password_letter == 8:
                for n in range(0, password_letter-password_number-password_special_character):
                    randInt = random.randint(0, 25)
                    # print(letters[randInt])
                    password += letters[randInt]
                if password_number == 1:
                    for n in range(0, password_number):
                        randInt = random.randint(0, 9)
                        # print(numbers[randInt])
                        password += numbers[randInt]
                elif password_number == 2:
                    for n in range(0, password_number):
                        randInt = random.randint(0, 9)
                        # print(numbers[randInt])
                        password += numbers[randInt]
                elif password_number == 3:
                    for n in range(0, password_number):
                        randInt = random.randint(0, 9)
                        # print(numbers[randInt])
                        password += numbers[randInt]
                else:
                    print("error !!!!!!")
                if password_special_character == 1:
                    for n in range(0, password_special_character):
                        randInt = random.randint(0, 4)
                        # print(special_character[randInt])
                        password += special_character[randInt]
                elif password_special_character == 2:
                    for n in range(0, password_special_character):
                        randInt = random.randint(0, 4)
                        # print(special_character[randInt])
                        password += special_character[randInt]
                else:
                    print("Error !!!!")
            elif password_letter == 9:
                for n in range(0, password_letter-password_number-password_special_character):
                    randInt = random.randint(0, 25)
                    # print(letters[randInt])
                    password += letters[randInt]
                if password_number == 1:
                    for n in range(0, password_number):
                        randInt = random.randint(0, 9)
                        # print(numbers[randInt])
                        password += numbers[randInt]
                elif password_number == 2:
                    for n in range(0, password_number):
                        randInt = random.randint(0, 9)
                        # print(numbers[randInt])
                        password += numbers[randInt]
                elif password_number == 3:
                    for n in range(0, password_number):
                        randInt = random.randint(0, 9)
                        # print(numbers[randInt])
                        password += numbers[randInt]
                else:
                    print("error !!!!!!")
                if password_special_character == 1:
                    for n in range(0, password_special_character):
                        randInt = random.randint(0, 4)
                        # print(special_character[randInt])
                        password += special_character[randInt]
                elif password_special_character == 2:
                    for n in range(0, password_special_character):
                        randInt = random.randint(0, 4)
                        # print(special_character[randInt])
                        password += special_character[randInt]
                else:
                    print("Error !!!!")
            elif password_letter == 10:
                for n in range(0, password_letter-password_number-password_special_character):
                    randInt = random.randint(0, 25)
                    # print(letters[randInt])
                    password += letters[randInt]
                if password_number == 1:
                    for n in range(0, password_number):
                        randInt = random.randint(0, 9)
                        # print(numbers[randInt])
                        password += numbers[randInt]
                elif password_number == 2:
                    for n in range(0, password_number):
                        randInt = random.randint(0, 9)
                        # print(numbers[randInt])
                        password += numbers[randInt]
                elif password_number == 3:
                    for n in range(0, password_number):
                        randInt = random.randint(0, 9)
                        # print(numbers[randInt])
                        password += numbers[randInt]
                else:
                    print("error !!!!!!")
                if password_special_character == 1:
                    for n in range(0, password_special_character):
                        randInt = random.randint(0, 4)
                        # print(special_character[randInt])
                        password += special_character[randInt]
                elif password_special_character == 2:
                    for n in range(0, password_special_character):
                        randInt = random.randint(0, 4)
                        # print(special_character[randInt])
                        password += special_character[randInt]
                else:
                    print("Error !!!!")
            else:
                print("Error !!!!!!!!!---")
        else:
            print("Plz enter valid number of special character !")
    else:
        print("Plz enter valid number of special character !")
else:
    print("Plz enter valid number of special character !")
# print(password)
random.shuffle(password)
# print(password)

final_password = ""
for n in password:
    final_password += n
# print(final_password)

randInt = random.randint(0, len(password))

for n in range(0, randInt):
    randInt1 = random.randint(0, len(password)-1)
    randInt2 = random.randint(0, len(password)-1)
    if randInt1 != randInt2:
        a = randInt1
        randInt1 = randInt2
        randInt2 = a
