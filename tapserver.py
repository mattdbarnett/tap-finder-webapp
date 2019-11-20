import os
from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/home")
def homePage():
    return redirect("/static/home.html")

@app.route("/about")
def aboutPage():
    return redirect("/static/about.html")

@app.route("/contact")
def contactPage():
    return redirect("/static/contact.html")

@app.route("/map")
def mapPage():
    return redirect("/static/map.html")

if __name__ == "__main__":
    app.run(debug=True)
