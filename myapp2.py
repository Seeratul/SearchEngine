from flask import Flask, request, render_template
from whoosh import index
from whoosh.qparser import QueryParser
import numpy as np

ix = index.open_dir("indexdir") 

# Retrieving data

#flask --app myapp2 run

app = Flask(__name__)

@app.route("/")
def start():
    return render_template('start.html')

@app.route("/search")
def search():
        urls = [""]
        with ix.searcher() as searcher:
        # find entries with the words 'first' AND 'last'
            query = QueryParser("body", ix.schema).parse(request.args["q"])
            results = searcher.search(query)
            print(results[0])
            for i in range(len(results)):
                urls.append(results[i]["url"])
                print(urls[i])
            #query = "a"
        # print all results
        return render_template("searched.html", rev= urls, len = len(results))

