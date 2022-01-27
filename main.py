# import "packages" from flask
from flask import Flask, render_template, request, url_for, redirect, jsonify, make_response
import requests
from __init__ import app
from crud.app_crud import app_crud, users_ilike, user_by_id, users_all
from crud.model import Users
from homepages.homepages import app_homepages

app.register_blueprint(app_crud)
app.register_blueprint(app_homepages)


@app.route('/todo/')
def todo():
    return render_template("todo.html")


@app.route('/studyroom/')
def studyroom():
    return render_template("studyroom.html")


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


# CRUD delete
@app.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        userid = request.form.get("userid")
        po = user_by_id(userid)
        if po is not None:
            po.delete()
    return redirect(url_for('crudtable'))


# CRUD update
@app.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        userid = request.form.get("userid")
        name = request.form.get("name")
        po = user_by_id(userid)
        if po is not None:
            po.update(name)
    return redirect(url_for('crudtable'))


# CRUD read
@app.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        userid = request.form.get("userid")
        po = user_by_id(userid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("crudtable.html", table=table)


# CRUD create/add
@app.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Users(
            request.form.get("name"),
            request.form.get("email"),
            request.form.get("password"),
            request.form.get("phone")
        )
        po.create()
    return redirect(url_for('crudtable'))


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
