from flask import Flask, Blueprint, render_template

#Construct Blueprint
UI_Home = Blueprint('UserInterfaceHome', __name__)
#Setup Route for login-interface
@UI_Home.route('/')
def return_login_interface():
        return render_template("UI-Home.html")
