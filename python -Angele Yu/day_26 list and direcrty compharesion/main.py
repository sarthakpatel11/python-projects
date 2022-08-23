# number = [1, 2, 3]
# new_list = [n+1 for n in number]
# new_list = [n+1 for n in new_list]
# print(new_list)

# name = ["sdf", "asf", "ert"]
# new_name = [name.upper() for name in name]
# print(new_name)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squed_number = [num*num for num in numbers]
# print(squed_number)

# result = [num for num in numbers if num % 2 == 0]
# print(result)


# with open("./txt1.txt") as file_1:
#     file_1_number = file_1.readlines()


# with open("./txt2.txt") as file_2:
#     file_2_number = file_2.readlines()


# if len(file_2_number) > len(file_1_number):
#     loop_number = len(file_2_number)
# else:
#     loop_number = len(file_1_number)

# file_1 = [int(i) for i in file_1_number]
# file_2 = [int(i) for i in file_2_number]

# print(file_1)
# print(file_2)

# same_number = [i for i in file_1
#                if i in file_2]
# print(same_number)


# sentance = "What is the Airspeed Valocity of an Unladen Swallow."

# for i in range(0, len(sentance)):
#     words = sentance.split(" ")

# result = {word: len(word) for word in words}
# print(result)


# wether = {
#     "monday": 12,
#     "tuesday": 15,
#     "wensdaty": 14,
#     "thrusday": 21,
#     "friday": 22,
#     "saturday": 24,
# }

# result = {day: (wether[day]*9/5)+32 for day in wether}
# print(result)


import pandas as pd
NATO_alphabet = pd.read_csv(
    "./day_26 list and direcrty compharesion/alphabet.csv")

input = input("Enter the Name ").upper()
Alphabets = pd.DataFrame(NATO_alphabet)

which_position = {row.letter: row.name for(index, row) in Alphabets.iterrows()}
print(which_position)
output_words = [which_position[letter] for letter in input]
print(output_words)
