from os import name
import requests
from bs4 import BeautifulSoup
import smtplib

URL_AMAZON_MACBOOK = "https://www.amazon.com/Apple-MacBook-Pro-8-core-Silver/dp/B091V55WNY/ref=sr_1_8?crid=27UVUVOYSBO0H&dchild=1&keywords=macbook&qid=1626495944&sprefix=macb%2Caps%2C1048&sr=8-8"
URL_AMAZON_IPHONE = "https://www.amazon.in/New-Apple-iPhone-Mini-128GB/dp/B08L5VG843/ref=sr_1_3?dchild=1&keywords=iphone+12+mini&qid=1626517754&sr=8-3"
URL_CAMMAL = "https://camelcamelcamel.com/product/B091V55WNY"
URL_FLIPKART_IPHONE_XR = "https://www.flipkart.com/apple-iphone-xr-product-red-64-gb-includes-earpods-power-adapter/p/itmf9z7zhydhtbn5?pid=MOBF9Z7ZRWGTX3FA&lid=LSTMOBF9Z7ZRWGTX3FAWC8NB0&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=clp_banner_1_9.banner.BANNER_appledays-2021-store_BGN1WD7HYH35&fm=neo%2Fmerchandising&iid=ec7105c3-879f-4515-b8a3-e63936084ef8.MOBF9Z7ZRWGTX3FA.SEARCH&ppt=clp&ppn=appledays-2021-store&ssid=h47n2xjuc00000001626522840200"


response = requests.get(url=URL_FLIPKART_IPHONE_XR)
data = response.text

# response1 = requests.get(url=URL_AMAZON_MACBOOK)
# print(response1)
# data1 = response1.text


# response2 = requests.get(url=URL_AMAZON_IPHONE)
# print(response2.text)
# data2 = response2.text


# response3 = requests.get(url=URL_CAMMAL)
# print(response3.text)
# data3 = response3.text

# soup1 = BeautifulSoup(data1, "html.parser")
# soup2 = BeautifulSoup(data2, "html.parser")
# soup3 = BeautifulSoup(data3, "html.parser")


#    --------------       filpkart (iphine xr)   ------------------

def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        sender_email = "mail"
        password = "pass"
        resever_email = "mail"
        msg = "Subject:Iphonr XR is at cheapest price.\n\nI think need to chang your phone plz visit the filpkart moblie section."+URL_FLIPKART_IPHONE_XR
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs=resever_email,
                            msg=msg)
        connection.close()


soup = BeautifulSoup(data, "html.parser")
price_tag = soup.find(name="div", class_="_30jeq3 _16Jk6d")
price = price_tag.getText()
price = int(f"{price[1:3]}{price[4:]}")
if price <= 40000:
    send_mail()


# #   ------------       Amazon data- scripting (Mac book)    ---------------------
# price_tag = soup1.find(name="span", id="#priceblock_ourprice")
# print(price_tag)

# title_tag = soup1.find(name="span", id="#productTitle")
# print(title_tag)

# #   ------------       Amazon data- scripting (Iphone 12 mini)    ---------------------
# price_tag = soup2.find(name="span", id="#priceblock_ourprice")
# print(price_tag)

# title_tag = soup2.find(name="span", id="#productTitle")
# print(title_tag)

# #   ------------------     cammalcammalcammal.com    --------------------
# price_tag = soup3.find(name="tr", class_=".lowest_price")
# print(price_tag)
