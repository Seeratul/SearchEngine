def saver(soup,index,url):
    title = soup.html.title.text
    body = soup.html.p.text
    writer = index.writer()
    writer.add_document(url = url,title= title, body = body+" "+title) 
    writer.commit()
    return