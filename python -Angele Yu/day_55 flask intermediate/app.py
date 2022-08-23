from logging import root
from flask import Flask
app = Flask(__name__)


def make_bold():
    return '<b></b>'


def make_italik():
    return '<em></em>'


def make_underline():
    return '<u></u>'


@app.route("/")
def starting_string():
    return '<h1>Hello There Plz guess a number between 0 to 9</h1>'


@app.route("/<guessed_number>")
@make_bold
@make_italik
@make_underline
def statement(guessed_number):
    return f"You have searched a number {guessed_number}"


if __name__ == "__main__":
    app.run(debug=True)
