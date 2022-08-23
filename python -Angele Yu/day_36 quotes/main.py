import requests
import random

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

querystring = {"q": "tesla", "region": "US"}

headers = {
    'x-rapidapi-key': "03cbef3edbmsh7b456eed84f8735p1f2af2jsn5599d2316da4",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
data_quotes = data["quotes"]
data_news = data["news"]
data_quotes_longname = [data["quotes"][i]["longname"]
                        for i in range(0, len(data_quotes)) if data["quotes"][i]["longname"] == "Tesla, Inc."]
data_quotes_symbol = [data["quotes"][i]["symbol"]
                      for i in range(0, len(data_quotes_longname))]
data_quotes_score = [data["quotes"][i]["score"]
                     for i in range(0, len(data_quotes_longname))]
data_news_title = [data["news"][i]["title"]
                   for i in range(0, len(data_news))]
differnce = data_quotes_score[-1]-data_quotes_score[1]
if differnce < 0:
    print(
        f"↓ {differnce} ({round(100-((data_quotes_score[1]*100)/data_quotes_score[-1]),3)}%)")
else:
    print(
        f"↑ {differnce} ({round(100-((data_quotes_score[1]*100)/data_quotes_score[-1]),3)}%)")

data_news = random.choice(data_news_title)
print(data_news)
