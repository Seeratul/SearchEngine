from flask import Flask, request, render_template
from whoosh import index
from whoosh.qparser import QueryParser
import numpy as np

#open woosh index
ix = index.open_dir("indexdir") 

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
    #Instantiate hits
    hits = [""]
    #open the searcher
    with ix.searcher() as searcher:

    # find entries containing the query
        print(type("q"))
        query = QueryParser("body", ix.schema).parse(request.args["q"])
        results = searcher.search(query)
        #extract data from the individual results while iterating over them
        for i in range(len(results)):
            hits.append([results[i]["url"],[results[i]["title"]],[results[i]["excerpt"]]])
            
    #Hand the extratcted data over to the template
    return render_template("searched.html", rev= hits, len = len(results))

