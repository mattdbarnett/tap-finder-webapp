import sqlite3
from flask import Flask, flash, render_template, request, session, redirect, url_for

import loginFunctionality
from loginFunctionality import *

tapDB = 'db/tapDatabase.db'

app = Flask(__name__)
app.config["SECRET_KEY"] = "arjT3S6tTdiC0Dq5cbvifA"

@app.route("/home")
def homePage():
    return render_template("home.html")

@app.route("/about")
def aboutPage():
    return render_template("about.html")

@app.route("/addatap")
def addatapPage():
    return render_template("addatap.html")

@app.route("/contact")
def contactPage():
    return render_template("contact.html")

@app.route("/map")
def mapPage():
    return render_template("map.html")

@app.route("/profile")
def profilePage():
    return(check_session(session.get("sessionID")))

@app.route("/login", methods=["GET", "POST"])
def loginPage():
    if request.method == "POST":
        login = request.form
        email = login.get("Email")
        password = login.get("Password")
        conn = sqlite3.connect(tapDB)
        cur = conn.cursor()
        cur.execute("SELECT hashedPW FROM Users WHERE email=?;", [email])
        result = cur.fetchone()
        if result != None:
            hashedPW = result[0]
            if check_password(hashedPW, password) is True:
                IP = str(request.environ['REMOTE_ADDR'])
                session_status = check_for_session(IP)
                if session_status is False:
                    sessionID = generate_session_id()
                    session["sessionID"] = sessionID
                    cur.execute("INSERT INTO Sessions ('email','sessionID','IP') VALUES (?,?,?)", [email, sessionID, IP])
                elif str(session_status[1]) == email:
                    session["sessionID"] = session_status[0]
                else:
                    cur.execute("DELETE FROM Sessions WHERE IP=?", [IP])
                    sessionID = generate_session_id()
                    session["sessionID"] = sessionID
                    cur.execute("INSERT INTO Sessions ('email','sessionID','IP') VALUES (?,?,?)", [email, sessionID, IP])
                conn.commit()
                conn.close()
                return redirect(url_for("profilePage"))

        return("Error")

    return render_template("login.html")

@app.route("/logout")
def logoutRoute():
    IP = request.environ['REMOTE_ADDR']
    result = logout(IP)
    if result == "Logged Out.":
        flash("Logged Out Successfully!", "success")
        return redirect(url_for("homePage"))
    else:
        flash(str(result), "error")
        return redirect(url_for("homePage"))

if __name__ == "__main__":
    app.run(debug=True)
