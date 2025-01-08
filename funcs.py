def saver(soup,index,url):
    title = soup.html.title.text
    body = soup.html.p.text
    writer = index.writer()
    excerpt =  soup.html.p.text
    excerpt = excerpt[0:50]
    writer.add_document(url = url,title= title, body = body+" "+title, excerpt = excerpt) 
    writer.commit()
    return