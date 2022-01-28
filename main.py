# import "packages" from flask
from flask import Flask, render_template, request, url_for, redirect, jsonify, make_response
import requests
from __init__ import app
from crud.app_crud import app_crud, users_ilike, user_by_id, users_all
from crud.model import Users
from homepages.homepages import app_homepages

app.register_blueprint(app_crud)
app.register_blueprint(app_homepages)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/todo/')
def todo():
    return render_template("todo.html")


@app.route('/flashcards/')
def flashcards():
    return render_template("flashcards.html")



@app.route('/studyroom/')
def studyroom():
    return render_template("studyroom.html")


@app.route('/calculator/')
def calculator():
    return render_template("calculator.html")


@app.route('/notepad/')
def notepad():
    return render_template("notepad.html")


@app.route('/crudtable/')
def crudtable():
    return render_template("crudtable.html", table=users_all())


@app.route('/search/')
def search():
    return render_template("search.html")


@app.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(users_ilike(term)), 200)
    return response


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
