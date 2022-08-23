from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World !"


#  --------- no need to set FLASK_APP=app.py and flask run    -----------------

if __name__ == "__main__":
    app.run()
