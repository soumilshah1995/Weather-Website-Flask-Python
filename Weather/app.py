from flask import render_template, url_for, request
from wtforms import StringField, SubmitField
from flask import Flask
from flask_wtf import FlaskForm
from weatherdata import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"


@app.route('/', methods=["POST", "GET"])
def index():
    w = Weather()
    form = Form()
    data = w.weather_get(zip='06604')

    if request.method == "POST":

        if form.validate_on_submit():

            txt_search = form.search.data
            data = w.weather_get(zip=txt_search)
            return render_template("home.html", data=data, form=form)
    else:
        return render_template("home.html", data=data, form=form)

class Form(FlaskForm):
    button = SubmitField('Search')
    search = StringField('submit')

if __name__ == "__main__":
    app.run(debug=True)
