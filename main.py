from flask import Flask, render_template
from flask_nav import *


app = Flask(__name__)
nav=


@app.route("/")
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/chinese')
def chinese():
    return render_template("chinese.html")

@app.route('/korean')
def korean():
    return render_template("korean.html")

@app.route('/arabic')
def arabic():
    return render_template("arabic.html")

if __name__=="__main__":
    app.run(debug=True)

#https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/
