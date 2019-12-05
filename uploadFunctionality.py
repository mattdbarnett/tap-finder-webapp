import sqlite3
import os
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
from flask import Flask, flash, render_template, request, session, redirect, url_for, make_response

tapDB = 'db/tapDatabase.db'

# REFERENCE
# Code adapted from: https://developer.here.com/blog/getting-started-with-geocoding-exif-image-metadata-in-python3
# Date Accessed: 4/12/19

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

def get_decimal_from_dms(dms, ref):

    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1] / 60.0
    seconds = dms[2][0] / dms[2][1] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return ([lat, lon])

# END OF REFERENCE

def analyse_image(image, tapname="New Tap"):
    try:
        exif = get_exif(image)
        geotags = get_geotagging(exif)
        flash("Added tap successfully. Pending Admin Approval.", "success")
        # Need to add DB submission here
        return render_template("tapadded.html", coordinates=get_coordinates(geotags), tapname=tapname)
    # If the image does not contain geotagging data
    except ValueError:
        flash(u"Image is missing neccessary geotagging data.", "error")
        os.remove(image)
        return redirect(url_for("addatapPage"))
    # If the image cannot be found
    except FileNotFoundError:
        flash(u"Could not retrieve image.", "error")
        return redirect(url_for("adddatapPage"))
