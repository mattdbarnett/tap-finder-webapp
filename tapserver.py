import sqlite3
from flask import Flask, render_template, request, session, redirect, url_for

tapDB = 'tapDatabase.db'

app = Flask(__name__)
app.config["SECRET_KEY"] = "arjT3S6tTdiC0Dq5cbvifA"

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

@app.route("/login")
def loginPage():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
