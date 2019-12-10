import sqlite3
from flask import Flask, flash, render_template, request, session, redirect, url_for, make_response

tapDB = 'db/tapDatabase.db'

# Function to retrieve all taps from tapDB.Locations
# If approved is False only unapproved taps are returned
def retrieveTaps(approved):
    conn = sqlite3.connect(tapDB)
    cur = conn.cursor()
    if approved is False:
        cur.execute("SELECT * FROM Locations WHERE Approved=0;")
    else:
        cur.execute("SELECT * FROM Locations;")
    result = cur.fetchall()
    conn.close()
    return(result)

def countTaps():
    conn = sqlite3.connect(tapDB)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM Locations WHERE Approved=0;")
    unapproved = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Locations;")
    total = cur.fetchone()[0]
    conn.close()
    return([unapproved, total])

def approveTap(coordinates):
    coordinates_list = coordinates.split(", ")
    try:
        conn = sqlite3.connect(tapDB)
        cur = conn.cursor()
        cur.execute("UPDATE Locations SET Approved=1 WHERE Latitude=? AND Longitude=?;",[coordinates_list[0],coordinates_list[1]])
        conn.commit()
        conn.close()
        return("Successfully Approved Tap.")

    except sqlite3.Error as e:
        return(str(e))

def removeTap(coordinates):
    coordinates_list = coordinates.split(", ")
    try:
        conn = sqlite3.connect(tapDB)
        cur = conn.cursor()
        cur.execute("DELETE FROM Locations WHERE Latitude=? AND Longitude=?;",[coordinates_list[0],coordinates_list[1]])
        conn.commit()
        conn.close()
        return("Successfully Removed Tap.")

    except sqlite3.Error as e:
        return(str(e))
