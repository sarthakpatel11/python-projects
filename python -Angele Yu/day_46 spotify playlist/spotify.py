import requests

responce = requests.get(
    "https://open.spotify.com/user/7d2D2S200NyUE5KYs80PwO")

res = requests.get(
    "https://api.spotify.com/v1/users/7d2D2S200NyUE5KYs80PwO/playlists")
print(res.text)
