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
@app.route('/test/')
def test():
    return render_template("test.html")

@app.route('/calendar/')
def calendar():
    return render_template("calendar.html")

@app.route('/wordle2/')
def wordle2():
    return render_template("wordle2.html")

@app.route('/snake/')
def snake():
    return render_template("snake.html")

@app.route('/graph/')
def graph():
    return render_template("graph.html")

@app.route('/quiz/')
def quiz():
    return render_template("quiz.html")

@app.route('/quiz1/')
def quiz1():
    return render_template("quiz1.html")

@app.route('/wordle/')
def wordle():
    return render_template("wordle.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
