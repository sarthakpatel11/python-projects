from os import name
from flask import Flask, render_template
import requests


app = Flask(__name__)


# @app.route("/<name>")
# def home(name):
#     url = f"https://api.genderize.io/?name={name}"
#     res = requests.get(url=url)
#     data = res.json()
#     person = data["name"]
#     gender = data["gender"]
#     print(data, person, gender)
#     return render_template("./index.html", name=person, gender=gender)

blog_id = []
blog_subject = []
blog_data = []
blog_url = "https://api.npoint.io/"
res = requests.get(url=blog_url)
blog = res.json()
for i in range(0, 3):
    print(i)
    bid = blog[i]["id"]
    subject = blog[i]["subject"]
    data = blog[i]["blog"]
    blog_id.append(bid)
    blog_subject.append(subject)
    blog_data.append(data)


@app.route("/blog", methods=["GET"])
def blog():
    return render_template("./blog.html", id=blog_id, subject=blog_subject)


@app.route("/blog/<num>")
def get_blog(num):
    no = int(num)+1
    return render_template("./index1.html", no=no, blog_data=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
