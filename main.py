# import "packages" from flask
from flask import Flask, render_template
from __init__ import app
from crud.app_crud import app_crud
from homepages.homepages import app_homepages
from tools.tools import app_tools

app.register_blueprint(app_crud)
app.register_blueprint(app_homepages)
app.register_blueprint(app_tools)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/studyroom/')
def studyroom():
    return render_template("studyroom.html")



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
