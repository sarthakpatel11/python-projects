# import smtplib

# my_email = your email
# password = password
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=victim email, msg="Subject:Hello\n\nThis is body of mail.")
#     connection.close()

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.weekday()
# date = now.date()
# print(now)
# print(year, month, day, date)

# date_of_birth = dt.datetime(year=2002, month=2, day=2)
# print(date_of_birth)


# ---------------------------------------------------------
import smtplib
import datetime as dt
from typing import ItemsView
import pandas as pd
import random

# constants ----------------------
sender_email = your mail
password = pass
date_of_birth = []
month_of_birth = []
PLACEHOLDER = "[name]"


# open file -----------------------
file = pd.read_csv("./day_32 BIRTHDAY/birthday- Sheet1.csv")
file_data = pd.DataFrame(file)
# print(file_data)

# csv file day and month -----------
date = {index: row.day for (index, row) in file_data.iterrows()}
# print(date)

name_mail = {index: row.names for (index, row) in file_data.iterrows()}
# print(name_mail)

resever_email = {index: row.email for (index, row) in file_data.iterrows()}
# print(resever_email)

month = {index: row.month for (index, row) in file_data.iterrows()}
# print(month)

# date and time ---------------------
now = dt.datetime.today()
month_now = now.month
day_now = now.day


#  coustom date from csv liist ------
for i in range(0, len(date)):
    setting_date = dt.datetime(year=now.year, month=month[i], day=date[i])
    date_of_birth.append(setting_date.day)
    month_of_birth.append(setting_date.month)
    # print(date_of_birth, month_of_birth)


# birthday-wisheer letter ----------

with open("./day_32 BIRTHDAY/wisher1.txt") as wisher_letter_1:
    letter_1 = wisher_letter_1.read()
    # print(letter_1)


with open("./day_32 BIRTHDAY/wisher2.txt") as wisher_letter_2:
    letter_2 = wisher_letter_2.read()
    # print(letter_2)


with open("./day_32 BIRTHDAY/wisher3.txt") as wisher_letter_3:
    letter_3 = wisher_letter_3.read()
    # print(letter_3)


def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs=resever_email[i],
                            msg=msg)
        connection.close()

# # checking condtion ----------------


for i in range(0, len(date)):
    if month_of_birth[i] == month_now and date_of_birth[i] == day_now:
        # print(f"Month and date is match.")

        # random letter ----------------

        randInt = random.randint(0, 2)
        if randInt == 0:
            letter = letter_1
        elif randInt == 1:
            letter = letter_2
        elif randInt == 2:
            letter = letter_3
        else:
            print("Error")

        # changing content of the letter ----

        modifed_letter = letter.replace(
            PLACEHOLDER, name_mail[i])
        # print(modifed_letter)

        msg = "Subject:Happy Birth Day\n\n"+modifed_letter
        # print(msg)

        # connection --------------------
        send_mail()
