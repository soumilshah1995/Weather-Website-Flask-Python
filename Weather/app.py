from flask import render_template, url_for, request
from flask import Flask
from weatherdata import *

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    w = Weather()
    data = w.weather_get(zip='06604')
    return render_template("home.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
