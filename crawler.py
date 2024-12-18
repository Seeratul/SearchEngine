import requests
from bs4 import BeautifulSoup as bs
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
import time

#for setup
prefix = 'https://vm009.rz.uos.de/crawl/'
start_url = prefix+'index.html'
agenda = [start_url]
ix = open_dir("indexdir")
schema = Schema(url =TEXT(stored=True))
ix = create_in("indexdir", schema)


while agenda:
    url = agenda.pop()  
    print("Get ",url)
    #time.sleep(2)
    r = requests.get(url)
    print(r, r.encoding)
    if r.status_code == 200:
        writer = ix.writer()
        writer.add_document(url = url) 
        writer.commit()
        soup = bs(r.text,features= "lxml")

        for link in soup.find_all('a'):
            string = link.get('href')
            #move out string analyzer
            if ".html" in string:
                
                if prefix in string:
                    newurl = string
                else:
                    newurl= prefix+string

                query = QueryParser("url", ix.schema).parse(string)
                with ix.searcher() as searcher:
                    results = searcher.search(query)
                if len(results) == 0:
                    if (newurl in agenda)== False:
                        print(string)
                        agenda.append(newurl)
query = QueryParser("url", ix.schema).parse("https")
with ix.searcher() as searcher:
    results = searcher.search(query)
    print(len(results))
    print(results)

            
