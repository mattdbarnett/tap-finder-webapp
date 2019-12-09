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
