from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib

MIN_SOEED = 10
sender_email = "mastimajaknahikarva@gmail.com"
password = "M@stiM@j@K1"
resever_email = "2maxjohnny292@gmail.com"

chrome_driver_path = "D:/Learning Stuff/python/python -Angele Yu/devlopment/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()

driver.get(
    f"https://fast.com/")
time.sleep(15)
speed_value = driver.find_element_by_css_selector("#speed-value").text
print(speed_value)


def send_mail(speed_value):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        msg = f"Subject:Your Internet speed is very slow\n\nYou have told us that you provide minime internet speed will be {MIN_SOEED} mb/s,but your network speed is {speed_value} mb/s."
        connection.sendmail(from_addr=sender_email, to_addrs=resever_email,
                            msg=msg)
        connection.close()


if speed_value <= MIN_SOEED:
    send_mail(speed_value)

driver.quit()
