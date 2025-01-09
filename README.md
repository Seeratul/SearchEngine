# SearchEngine by JHattendorf and FSenkbeil
## Local Quickstart
- Install needed packages 
    - either by creating a conda environment with ```conda env create -f env.yml``` or 
    - installing with ```pip install -r requirements.txt```
- Run crawler.py
- Call ```flask --app search run``` in the terminal
- Navigate to the site given (see 'Running on')
- Enter your query 

## Serverlink
http://vm146.rz.uni-osnabrueck.de/u032/search_app.wsgi/ 


Adjustment of code for server use:
    line 7 in search.py is a local path to indexdir. On the server line 7 needs to be ```ix = index.open_dir("SearchEngine/indexdir")``` instead of ```ix = index.open_dir("indexdir")``` 

## Features
A simple crawler that can:
- stay on the server 
- ignore non-html responses
- deal with short and long http responses
- ignores non-reachable sites
- collects url, headline, and the text of the page
- crawls to new unknown links
- creates a database after its crawl

A Searchpage that:
- has a landing site
- searches for the requested string in the preconstructed db
- displays all found hits in an unordered fashion
- displays the links with the page name and a small excerpt
- displays a help text if no hits are found
- isnt awfully ugly

Templates that:
- make reasonable use of flasks ability to use python
