import os
import sqlite3
from flask import Flask, flash, render_template, request, session, redirect, url_for, abort
from werkzeug.utils import secure_filename
import smtplib, ssl

import loginFunctionality
from loginFunctionality import *

import uploadFunctionality
from uploadFunctionality import *

import adminFunctionality
from adminFunctionality import *

tapDB = 'db/tapDatabase.db'

# Application Configuration Variables
UPLOAD_FOLDER = 'SubmittedImages'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
#SENDER_EMAIL = THE TAP EMAIL (WILL BE ADDED)
#TAPEMAIL_PW =
ALLOWED_EXTENSIONS = {'jpg'}

# Application Configuration
app = Flask(__name__)
app.config["SECRET_KEY"] = "arjT3S6tTdiC0Dq5cbvifA"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Client HTTP Error Handling
# Use abort(error_number) to call

# 404 - Not Found
@app.errorhandler(404)
def error404(error):
    HTTPError = str(error).split(":")
    flash(f"'{request.path}' produced the following error:", "error")
    return render_template("error.html", error=HTTPError[0], desc=HTTPError[1]), 404

# 403 - Forbidden
@app.errorhandler(403)
def error403(error):
    HTTPError = str(error).split(":")
    flash(f"'{request.path}' produced the following error:", "error")
    return render_template("error.html", error=HTTPError[0], desc=HTTPError[1]), 403

# 401 - Unauthorized
@app.errorhandler(401)
def error401(error):
    HTTPError = str(error).split(":")
    flash(f"'{request.path}' produced the following error:", "error")
    return render_template("error.html", error=HTTPError[0], desc=HTTPError[1]), 401

# 405 - Method Not Allowed
@app.errorhandler(405)
def error405(error):
    HTTPError = str(error).split(":")
    flash(f"'{request.path}' produced the following error:", "error")
    return render_template("error.html", error=HTTPError[0], desc=HTTPError[1]), 405

# End of Client Error Handling

@app.route("/")
def homePage():
    return render_template("home.html")

@app.route("/about")
def aboutPage():
    return render_template("about.html")

@app.route("/help")
def helpPage():
    return render_template("help.html")

@app.route("/addatap", methods=["GET", "POST"])
def addatapPage():
    if request.method == "POST":
        tapdata = request.form
        email = tapdata.get("emailAddress")
        # IP = str(request.environ['REMOTE_ADDR'])
        # session_info = check_for_session(IP)
        # if session_info is not False:
        #     email = session_info[1]
        tapname = tapdata.get("Name")
        image = request.files['image']
        # If no image is submitted check for manually inputted coordinates
        if image.filename == '':
            latitude = tapdata.get("lat")
            longitude = tapdata.get("long")
            return(submitTap(email, tapname, latitude, longitude))
        # Else if an image has been submitted
        else:
            filename = secure_filename(image.filename)
            # Validate that the file is of the correct filetype
            if str(filename.split(".")[1]).lower() not in ALLOWED_EXTENSIONS:
                flash(u"Invalid file type.", "error")
                return redirect(url_for("addatapPage"))
            # If the file is of the correct filetype upload it to the server for further checks
            else:
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return(analyse_image((UPLOAD_FOLDER+"/"+filename), email, filename, tapname))

    # If there is a user logged in
    elif check_session(session.get("sessionID"), True) is True:
        return(check_session(session.get("sessionID"), "addatap"))
    # If the user is a guest
    else:
        return render_template("addatap.html", user="a guest")

@app.route("/contact", methods=["GET", "POST"])
def contactPage():
    if request.method == "POST":
        contactdata = request.form
        name = contactdata.get("name")
        email = contactdata.get("emailAddress")
        query = contactdata.get("text")

        subject = "A new query from " + name + " (" + email + ")"
        username = "nsatapapp@gmail.com"
        password = "NSAtap1234"
        smtp_server = "smtp.gmail.com:587"
        email_from = "nsatapapp@gmail.com"
        email_to = "nsatapapp@gmail.com"
        email_body = 'Subject:{}\n\n{}'.format(subject, query)

        server = smtplib.SMTP(smtp_server)
        server.starttls()
        server.login(username, password)
        server.sendmail(email_from, email_to, email_body)
        server.quit()
        flash("Query Sent Successfully!", "success")
        flash("Process Was Not Successful", "error")

        return render_template("contact.html")
    else:
        return render_template("contact.html")

@app.route("/map")
def mapPage():
    return render_template("map.html")

@app.route("/profile")
def profilePage():
    return(check_session(session.get("sessionID")))

@app.route("/signin", methods=["GET", "POST"])
def signinPage():
    if request.method == "POST":
        # Gather login data from login form
        login = request.form
        email = login.get("Email")
        password = login.get("Password")
        # Query the database to check whether there is a user associated to the input email
        conn = sqlite3.connect(tapDB)
        cur = conn.cursor()
        cur.execute("SELECT hashedPW FROM Users WHERE email=?;", [email])
        result = cur.fetchone()
        # If the inputted email does return a user
        if result != None:
            # Retrieve the stored_hashedPW
            hashedPW = result[0]
            # If the user has input the correct password
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
            # If the user has input an incorrect password
            else:
                flash(u"Incorrect Password. Please try again.", "error")
                return redirect(url_for("signinPage"))
        # If the inputted email does not return a user
        flash(u"No user registered with that email address.", "error")
        return redirect(url_for("signinPage"))

    return render_template("signin.html")

@app.route("/logout")
def logoutRoute():
    IP = request.environ['REMOTE_ADDR']
    result = logout(IP)
    # If user is logged out successfully flash an appropriate message
    if result == "Logged Out.":
        flash("Logged Out Successfully!", "success")
        return redirect(url_for("homePage"))
    # Else flash the appropriate error
    else:
        flash(str(result), "error")
        return redirect(url_for("homePage"))

@app.route("/signup", methods=["GET", "POST"])
def signupPage():
    if request.method == "POST":
        signup = request.form
        values = []
        values.append(signup.get("FirstName"))
        values.append(signup.get("LastName"))
        values.append(signup.get("Email"))
        values.append(signup.get("Password1"))
        values.append(signup.get("Password2"))
        result = validate_new_user(values)
        # If new user is valid redirect to sign in page
        if result is True:
            return redirect(url_for("signinPage"))
        # If email is already in use redirect to reset password page
        elif result == "Reset":
            return redirect(url_for("resetpwPage"))
        # Else if user is invalid redirect to signup page
        else:
            return redirect(url_for("signupPage"))

    return render_template("signup.html")

@app.route("/resetpw", methods=["GET", "POST"])
def resetpwPage():
    if request.method == "POST":
        #code for reset password email send
        email_toreset = request.form["Email"]
        context = ssl.create_default_context()
        try:
            server = smtplib.SMTP(smtp_server)
            server.ehlo()
            server.startttls(context=context)
            server.ehlo()
            server.login("nsatapapp@gmail.com","NSAtap1234")
            #send an email here
        except Exception as e:
            print(e) #print any errors that may occur during email sending
        finally:
            server.quit() #end mail instance
            return("printed")
    return render_template("reset.html")

if __name__ == "__main__":
    app.run(debug=True)
