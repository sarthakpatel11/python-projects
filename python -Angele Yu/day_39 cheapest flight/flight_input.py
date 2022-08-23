from main import col, sheet
import datetime

now = datetime.datetime.today()
today_date = f"{str(now.day)}/{str(now.month)}/{str(now.year)}"
# print(today_date)

six_month = now.month+6
if six_month > 12:
    six_month = six_month-12

six_month_date = f"{str(now.day)}/{str(six_month)}/{str(now.year)}"
# print(six_month_date)

no_of_row = len(col)+1
choise = input(
    "Do you want to change your sheet or not ? (Yes or No) ").lower()

if choise == "yes" or choise == "Yes":
    flight_from = input(
        "Enter from where you want to go by flight ? ").upper()
    flight_to = input("Enter where you want to go by flight ? ").upper()
    min_price = int(input("Enter your min value for flight ? $ "))

    sheet.update_cell(no_of_row, 1, flight_from)
    sheet.update_cell(no_of_row, 2, flight_to)
    sheet.update_cell(no_of_row, 3, min_price)
    sheet.update_cell(no_of_row, 4, today_date)
    sheet.update_cell(no_of_row, 5, six_month_date)

else:
    flight_from = sheet.row_values(no_of_row-1)[0]
    flight_to = sheet.row_values(no_of_row-1)[1]
    min_price = sheet.row_values(no_of_row-1)[2]
    today_date = sheet.row_values(no_of_row-1)[3]
    six_month_date = sheet.row_values(no_of_row-1)[4]
