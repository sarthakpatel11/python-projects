from tkinter import *
import requests


#  geolocation ----------

# req = requests.get(url="http://api.open-notify.org/iss-now.json")
# data = req.json()
# print(data)

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# print(longitude, latitude)


# quotes ----------------


window = Tk()
window.title("Quotes")
window.minsize(width=500, height=500)


def text():
    req = requests.get(url="https://api.kanye.rest")
    data = req.json()
    quote = data["quote"]
    label = Label(text=quote,  font=("Arial", 24))
    label.place(x=30, y=30)


button = Button(text="change", command=text)
button.place(x=100, y=250)
window.mainloop()
