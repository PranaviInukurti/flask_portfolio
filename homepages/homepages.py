import requests
from flask import Blueprint, render_template

app_homepages = Blueprint('homepages', __name__,
                          url_prefix='/homepages/',
                          template_folder='templates/homepages/',
                          static_folder='static',
                          static_url_path='static/assets')


@app_homepages.route('/alice/')
def alice():
    url = "https://brianiswu-cat-facts-v1.p.rapidapi.com/facts"

    headers = {
        'x-rapidapi-host': "brianiswu-cat-facts-v1.p.rapidapi.com",
        'x-rapidapi-key': "f877084053msh82cfa972b631ab7p1c4893jsn442e2f514bb0"
    }

    response = requests.request("GET", url, headers=headers)
    # list1 is 5 items long, random number to use as index in list
    output = response.json()
    list1 = []
    for i in range(len(output)):
        list1.append(output[i]['text'])

    return render_template("alice.html", output=list1)


@app_homepages.route('/linda/')
def linda():
    return render_template("linda.html")


@app_homepages.route('/pranavi/')
def pranavi():
    return render_template("pranavi.html")


@app_homepages.route('/saathvika/')
def saathvika():
    return render_template("saathvika.html")


@app_homepages.route('/samaya/')
def samaya():
    return render_template("samaya.html")
