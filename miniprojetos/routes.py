from flask import Flask, render_template, url_for
from miniprojetos import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/geradordesenha')
def gerador_senha():
    return render_template("geradordesenha.html")
