# views.py

from flask import render_template

from app import app

@app.route('/')
def default():
    return query()

@app.route('/query.html')
def query():
    return render_template("query.html")


@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/results.html')
def results():
    return render_template("results.html")

@app.route('/references.html')
def references():
    return render_template("references.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/error.html')
def error():
    return render_template("error.html")
