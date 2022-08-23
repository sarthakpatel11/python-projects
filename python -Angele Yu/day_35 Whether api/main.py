from twilio.rest import Client
import os
import requests


# constants --------------
latitude = "22"
longitude = "70"
api_key = key
api_endpoint = api
whether = {
    "lat": "22.23",
    "lon": "70.89",
    "appid":  api_key,
    "exclude": "current,minutely,daily"
}
ACCOUNT_SID = sid
AUTH_TOKEN =token
will_rain = False
#
res = requests.get(api_endpoint, params=whether)
res.raise_for_status()
data = res.json()
whether_slice = data["hourly"][0:12]
for hour_data in whether_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Rainy")

# Download the helper library from https://www.twilio.com/docs/python/install


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. 
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="It's getting rain today so keep Umbrella with you.",
                    from_='++1 323 310 9424',
                    to='Your verified number'
                )

print(message.sid)
