# SearchEngine by JHattendorf and FSenkbeil
Quickstart:
    run crawler.py
    call flask --app search run in the terminal
    navigate to the site given
    enter your query

For server use:
    line 7 in search.py is a local path so if you download SearchEngine from git in its folder
    line 7 needs to be "ix = index.open_dir("SearchEngine/indexdir")" instead of ix = index.open_dir("indexdir") 

Features:
    A simple crawler that can:
        stay on the server 
        ignore non html responses
        deal with short and long http responses
        ignoreses non reachable sites
        collects url, headline and the text of the page
        crawls to new unknown links
        creates a database after its crawl

    A Searchpage that:
        has a landing site
        searches for the requested string in the preconstructed db
        displays all found hits in an unordered fashion
        dislays the links with the page name and a small excerpt
        displays a help text if no hits are found
        isnt afwully ugly.

    Templates:
        Templates that make reasonable use of flasks ability to use python
