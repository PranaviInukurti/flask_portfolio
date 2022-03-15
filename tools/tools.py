from flask import Blueprint, render_template

app_tools = Blueprint('tools', __name__,
                      url_prefix='/tools/',
                      template_folder='templates/tools/',
                      static_folder='static',
                      static_url_path='static/assets')


@app_tools.route('/todo/')
def todo():
    return render_template("todo.html")


@app_tools.route('/timer/')
def timer():
    return render_template("timer.html")


@app_tools.route('/calculator/')
def calculator():
    return render_template("calculator.html")


@app_tools.route('/notepad/')
def notepad():
    return render_template("notepad.html")


@app_tools.route('/websearch/')
def websearch():
    return render_template("websearch.html")


@app_tools.route('/flashcards/')
def flashcards():
    return render_template("flashcards.html")


@app_tools.route('/googlesearch/')
def googlesearch():
    return render_template("googlesearch.html")




