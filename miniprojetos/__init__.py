from flask import Flask, render_template, url_for, request, flash, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = '0e9BA7DfafcA17Ca0F14eC04289BB4d6'

# Importando o routes para ser executado e colocar os links no ar
from miniprojetos import routes