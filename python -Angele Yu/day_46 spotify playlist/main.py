from typing import Iterator
from bs4 import BeautifulSoup
from bs4.element import SoupStrainer
import lxml
import requests
from requests.models import iter_slices

respones = requests.get("https://www.billboard.com/charts/hot-100")
res_txt = respones.text

soup = BeautifulSoup(res_txt, "html.parser")

# li = soup.select(selector="ol li")
# print(li)

song_number = soup.select(selector="span .chart-element__rank__number")
song_name = soup.select(
    selector="span .chart-element__information__song")
song_singer = soup.select(
    selector="span .chart-element__information__artist")

song_list = []
for i in range(0, len(song_number)):
    song_list.append((song_number[i].getText(),
                      song_name[i].getText(), song_singer[i].getText()))
    print(song_list)
