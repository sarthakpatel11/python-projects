import requests

responce = requests.get(
    "https://open.spotify.com/user/7d2D2S200NyUE5KYs80PwO")

res = requests.get(
    "https://api.spotify.com/v1/users/7d2D2S200NyUE5KYs80PwO/playlists")
print(res.text)

# {
#     "display_name": "fotase8070",
#     "email": "fotase8070@ovooovo.com",
#     "external_urls": {
#         "spotify": "https://open.spotify.com/user/kfaw0pyir7v3yl8qlfm78fja6"
#     },
#     "followers": {
#         # "href": ,
#         "total": 0
#     },
#     "href": "https://api.spotify.com/v1/users/kfaw0pyir7v3yl8qlfm78fja6",
#     "id": "kfaw0pyir7v3yl8qlfm78fja6",
#     "images": [],
#     "type": "user",
#     "uri": "spotify:user:kfaw0pyir7v3yl8qlfm78fja6"
# }
