import os, base64
import sqlite3
from datetime import datetime, timedelta
from flask import Flask, render_template, request, session, redirect, url_for, make_response
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

tapDB = 'db/tapDatabase.db'

# Functions to handle hashing and 'un-hashing' passwords
def hash_password(Pw):
    return(bcrypt.generate_password_hash(Pw).decode('utf-8'))

def check_password(hashedPw, inputPw):
    return(bcrypt.check_password_hash(hashedPw, inputPw))

# Function to generate a unique sessionID
def generate_session_id():
    return str(base64.b64encode(os.urandom(32)))[2:45]

# Function to check whether an IP has a registered session in tapDB.Sessions
def check_for_session(IP):
    conn = sqlite3.connect(tapDB)
    cur = conn.cursor()
    # Check for sessions matching the users' IP
    cur.execute("SELECT sessionID, email, IP, expiryDT FROM Sessions WHERE IP=?;", [IP])
    result = cur.fetchone()
    # If there is no session registered to the IP  within tapDB.Sessions
    if result is None:
        return False
    else:
        return(result)

# Function to check validate whether the client has a session and whether it is valid
def check_session(sessionID):
    # Retrieve the users' IP Address
    Local_IP = str(request.environ['REMOTE_ADDR'])
    result = check_for_session(Local_IP)
    if result is False:
        return redirect(url_for("loginPage"))
    else:
        # Unpack results from check_for_session(Local_IP)
        stored_sessionID, email = result[0], result[1]
        IP, expiryDT = result[2], datetime.strptime(result[3], '%Y-%m-%d %H:%M:%S')
        conn = sqlite3.connect(tapDB)
        cur = conn.cursor()
        # If there is a registered session but it is invalid
        # Either the session has expired or the IP's do not match
        if (datetime.now() > expiryDT) or (Local_IP != IP):
            session.pop("sessionID")
            cur.execute("DELETE FROM Sessions WHERE sessionID=?", [sessionID])
            conn.commit()
            conn.close()
            return redirect(url_for("loginPage"))
        # If the clients' sessionID does not match the tapDB.Sessions sessionID
        elif (sessionID != stored_sessionID):
            session.clear()
            cur.execute("DELETE FROM Sessions WHERE IP=?", [Local_IP])
            conn.commit()
            conn.close()
            return redirect(url_for("loginPage"))
        # If there is a valid session
        else:
            # Check the accessLevel of the user and retrieve their full name in the same query
            cur.execute("SELECT accessLevel, firstName, lastName FROM Users WHERE email=?", [email])
            result = cur.fetchone()
            # Unpack the query result into appropriate variables
            accessLevel, name = result[0], (f"{result[1]} {result[2]}")
            # If the user in an admin
            if accessLevel == "Admin":
                return render_template("admin.html")
            # Else they must be a standard user
            else:
                return render_template("profile.html", email=email)

# Function to revoke a sessionID
def revoke_session(sessionID):
    session.clear()
    conn = sqlite3.connect(tapDB)
    cur = conn.cursor()
    cur.execute("DELETE FROM Sessions WHERE sessionID=?", [sessionID])
    conn.commit()
    conn.close()

# Function to log a user out dependent on their IP address
def logout(IP):
    # Try revoking the session if the user has a sessionID set in cookies
    try:
        sessionID = session["sessionID"]
        revoke_session(session["sessionID"])
        return("Logged Out.")
    # If a sessionID is not set in cookies a KeyError is returned
    # Therefore remove any associated sessions from the database that matches the users'
    # IP address
    except KeyError:
        conn = sqlite3.connect(tapDB)
        cur = conn.cursor()
        conn.execute("SELECT * FROM Sessions WHERE IP=?", [IP])
        result = cur.fetchone()
        # If no sessions are associated with the IP addess, no users must be logged in
        if result is None:
            return("No user logged in. Therefore cannot logout.")
        # Else remove the session from tapDB
        else:
            cur.execute("DELETE FROM Sessions WHERE IP=?", [IP])
            conn.commit()
            conn.close()
            return("Logged Out.")
