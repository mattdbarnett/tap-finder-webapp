import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def homePage():
    return render_template("home.html")

@app.route("/about")
def aboutPage():
    return render_template("about.html")

@app.route("/contact")
def contactPage():
    return render_template("contact.html")

@app.route("/map")
def mapPage():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True)
