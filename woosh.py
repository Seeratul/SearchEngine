from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.fields import *

# Here, the structure of index entries is defined. You can add more fields with metadata, computed values etc.,
# and use them for searching and ranking.
# We only use a title and a text.
#
# The "stored" attribute is used for all parts that we want to be able to fully retrieve from the index

#schema = Schema(title=TEXT(stored=True), content=TEXT)

# Create an index in the directory indexdr (the directory must already exist!)
ix = open_dir("indexdir")
writer = ix.writer()

# now let's add some texts (=documents)
writer.add_document(url =u"lorem.ipsum1",title=u"First document", content=u"This is the first document we've added!")
writer.add_document(url =u"lorem.ipsum2",title=u"Second document", content=u"The second one is even more interesting!")
writer.add_document(url =u"lorem.ipsum3",title=u"Songtext", content=u"Music was my first love and it will be the last")

# write the index to the disk
writer.commit()

# Retrieving data
ix = open_dir("indexdir")
from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
    # find entries with the words 'first' AND 'last'
    query = QueryParser("url", ix.schema).parse("lorem.ipsum2")
    results = searcher.search(query)
    
    # print all results
    for r in results:
        print(r)

#Optional cleanup
schema = Schema(url =TEXT(stored=True) ,title=TEXT(stored=True), content=TEXT)
ix = create_in("indexdir", schema)
