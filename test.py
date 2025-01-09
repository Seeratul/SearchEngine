from flask import Flask, request, render_template
from whoosh import index
from whoosh.qparser import QueryParser
import numpy as np

#open woosh index
#ix = index.open_dir("indexdir") 

# Retrieving data

#flask --app search run

app = Flask(__name__)

#landing page
@app.route("/")
def start():
    return render_template('start.html')

#search page
@app.route("/search")
def search():
    return render_template('start.html')
        