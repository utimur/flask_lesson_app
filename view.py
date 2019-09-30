from app import app
from flask import render_template


users = {'id1':{'name':'timur','pass':'123'},
         'id2':{'name':'Jason','pass':'8967100000'}}


@app.route('/')
def index():
    name = 'timur'
    return render_template("index.html",n = users)

