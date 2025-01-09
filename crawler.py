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
schema = Schema(url =TEXT(stored=True),title = TEXT(stored=True), body = KEYWORD,excerpt =TEXT(stored=True))
ix = create_in("indexdir", schema)

#Predefine saver to help with code legibility
def saver(soup,index,url):
    #Extract and cut to size various parts of the soup
    title = soup.html.title.text
    body = soup.html.p.text
    writer = index.writer()
    excerpt =  soup.html.p.text
    excerpt = excerpt[0:50]
    #Save the extracted parts
    writer.add_document(url = url,title= title, body = body+" "+title, excerpt = excerpt) 
    writer.commit()
    return

#Loop for as long as there is something on the agenda
while agenda:

    #Grab the top object from the agenda
    url = agenda.pop()  
    #Create a requests object
    r = requests.get(url)
 
    #Check wheter the target page is reachable
    if r.status_code == 200:
        
        #Extracts the soup from the page and saves it into our woosh library
        soup = bs(r.text,features= "lxml")
        saver(soup,ix,url)

        #look for further links to crawl
        for link in soup.find_all('a'):
            string = link.get('href')

            #ensusure found links are html links
            if ".html" in string:

                #ensures that links with and without the proper prefix get added
                if prefix in string:
                    newurl = string
                else:
                    newurl= prefix+string

                #Checks wheter the link already as been visited or is alredy in agenda
                query = QueryParser("url", ix.schema).parse(string)
                with ix.searcher() as searcher:
                    results = searcher.search(query)
                    
                if len(results) == 0:
                    if (newurl in agenda)== False:
                        agenda.append(newurl)



            
