import requests

responce = requests.get(
    "https://open.spotify.com/user/")

res = requests.get(
    "https://api.spotify.com/v1/users/playlists")
print(res.text)
