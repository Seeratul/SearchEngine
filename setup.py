from whoosh.index import create_in
from whoosh.fields import *


#schema = Schema(url =TEXT(stored=True) ,title=TEXT(stored=True), content=TEXT)
schema = Schema(url =TEXT(stored=True))
ix = create_in("indexdir", schema)