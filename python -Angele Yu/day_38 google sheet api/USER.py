from os import write
from main import sheet, col
import datetime

number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
worked = ""

user_str = input("Enter your work do today ? ").lower().split(" ")
print(user_str)

for i in range(0, len(user_str)):
    print(user_str[i])
    if user_str[i][0] == "w":
        word = "w"
    if user_str[i][0] == "c":
        word = "c"
    for j in range(0, len(user_str[i])):
        for z in range(0, len(number)):
            if user_str[i][j] == number[z] and word == "w":
                col_name = "walk"
                print(number[z])
                worked += number[z]
    for j in range(0, len(user_str[i])):
        for z in range(0, len(number)):
            if user_str[i][j] == number[z] and word == "c":
                col_name = "cycle"
                print(number[z])
                worked += number[z]
no_of_row = len(col)+1
# print(col_name, worked, no_of_row)

date = datetime.datetime.today()
date = date.date()
print(date)

sheet.update_cell(no_of_row, 1, str(date))
sheet.update_cell(no_of_row, 2, col_name)
sheet.update_cell(no_of_row, 3, worked)
