from flask import Flask, render_template, url_for, request, flash, redirect

app = Flask(__name__)


# Importando o routes para ser executado e colocar os links no ar
from miniprojetos import routes