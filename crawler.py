import requests
from bs4 import BeautifulSoup as bs
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
#from funcs import saver


#for setup we use simple presets they are inelegant but they do the job
prefix = 'https://vm009.rz.uos.de/crawl/'
start_url = prefix+'index.html'
agenda = [start_url]
#We create the schema in which woosh will store data
schema = Schema(url =TEXT(stored=True),title = TEXT(stored=True), body = TEXT,excerpt =TEXT(stored=True))
ix = create_in("indexdir", schema)

#we 
def saver(soup,index,url):
    title = soup.html.title.text
    body = soup.html.p.text
    writer = index.writer()
    excerpt =  soup.html.p.text
    excerpt = excerpt[0:50]
    writer.add_document(url = url,title= title, body = body+" "+title, excerpt = excerpt) 
    writer.commit()
    return

while agenda:
    url = agenda.pop()  
    print("Get ",url)
   
    #time.sleep(2)
    r = requests.get(url)
    print(r, r.encoding)
    if r.status_code == 200:
        # writer = ix.writer()
        # writer.add_document(url = url) 
        # writer.commit()
        soup = bs(r.text,features= "lxml")
        saver(soup,ix,url)

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

            
