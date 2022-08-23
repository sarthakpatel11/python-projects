from unicodedata import name
import selenium
from bs4 import BeautifulSoup
import requests


url = f"https://www.trivago.com/?aDateRange%5Barr%5D=2021-08-04&aDateRange%5Bdep%5D=2021-08-06&aPriceRange%5Bfrom%5D=0&aPriceRange%5Bto%5D=0&iRoomType=1&aRooms%5B0%5D%5Badults%5D=1&cpt2=85528%2F200&hasList=1&hasMap=1&bIsSeoPage=0&sortingId=1&slideoutsPageItemId=&iGeoDistanceLimit=16093&address=&addressGeoCode=&offset=0&ra=&overlayMode="
respones = requests.get(url=url)
data = respones.text
print(data)
xpath = '//*[@id="zpid_2069409669"]/div[1]'
soup = BeautifulSoup(data, "html.parser")
li = soup.find_all(name="div")
print(li)
