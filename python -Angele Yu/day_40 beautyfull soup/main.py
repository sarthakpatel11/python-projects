from bs4 import BeautifulSoup
from bs4.element import SoupStrainer
import lxml
import requests

# with open("./website.html", encoding="utf8") as file:
#     read_file = file.read()

# soup = BeautifulSoup(read_file, "html.parser")
# print(soup.title)
# print(soup.p)
# a_tag = soup.find_all(name="a")
# for a in a_tag:
#     # print(a.getText())
#     print(a.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# compny_url = soup.select_one(selector="p a")
# print(compny_url)

# my_name = soup.select_one(selector="#name")
# print(my_name)


#   Hacker news -------------------------------------------------------------------

# response = requests.get("https://news.ycombinator.com/news")
# Hacker_news = response.text

# soup = BeautifulSoup(Hacker_news, "html.parser")
# a_tag = soup.select(selector=".storylink")
# # print(a_tag)

# for tag in a_tag:
#     a_tag_txt = tag.getText()
#     print(a_tag_txt)

# for tag in a_tag:
#     a_tag_link = tag.get("href")
#     print(a_tag_link)


#   Empier movies list  -------------------------------------------------------------------


response = requests.get(
    "https://www.empireonline.com/movies/features/best-movies-2/")
Empire_movie = response.text

soup = BeautifulSoup(Empire_movie, "html.parser")
h3 = soup.find_all(name="h3", class_="title")
print(h3)