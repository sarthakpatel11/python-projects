from requests.models import Response
from flight_input import flight_from, flight_to, min_price, today_date, six_month_date
import requests
import smtplib
from typing import ItemsView

flight_date = ""
flight_price = ""

AFFILATE_ID = "fotase8070ovooovoovooovo"
header = {
    "apikey": "R7CWW7Sj1SE3mga0iXo64ciTmgU2FZ9Z",
}
params = {
    "fly_from": flight_from,
    "fly_to": flight_to,
    "date_from": str(today_date),
    "date_to": str(six_month_date),
}
url = "https://tequila-api.kiwi.com/aggregation_search/price_per_date?"

response = requests.get(url=url, headers=header, params=params)
json = response.json()
json_data = json["data"]

for i in range(0, len(json_data)):
    data_price = json_data[i]["price"]

    if int(min_price) >= data_price:
        flight_date += f"{json_data[i]['date']}, "
        flight_price += f"{json_data[i]['price']}, "

if flight_price[0] != "":
    sender_email = "mastimajaknahikarva@gmail.com"
    password = "M@stiM@j@K1"
    resever_email = "2maxjohnny292@gmail.com"
    msg = f"Subject:Chepest Flight\n\nWe have find some date for chepeast price rate for flight\nFrom : {flight_from}\nto : {flight_to}\ndate : {flight_date}\nprice : {flight_price}\nfor more info call 911"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs=resever_email,
                            msg=msg)
        connection.close()
