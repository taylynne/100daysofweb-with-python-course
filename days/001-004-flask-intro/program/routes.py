from program import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/secret_page')
def secret_page():
    return "Wow... you found the secret page!"

@app.route("/100days")
def p100days():
    return render_template("100days.html")
