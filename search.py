from whoosh import index

ix = index.open_dir("indexdir") 

# Retrieving data
from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
    # find entries with the words 'first' AND 'last'
    query = QueryParser("body", ix.schema).parse("Home")
    results = searcher.search(query)

    # print all results
    for r in results:
        print(r["url"])
        