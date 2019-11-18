from flask import Flask, request, render_template

#Import Blueprints
from blueprints.UserInterfaceHome import UI_Home

app = Flask(__name__)

#Register Blueprints
app.register_blueprint(UI_Home)
#app.register_blueprint(UI_About_Us)

@app.route('/test')
def return_test():
    return render_template('UI-template.html')

#Start Web Application -- Allow Threading and Debugging
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True)
