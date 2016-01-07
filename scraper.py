# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html

print 'hello'
urltoscrape = 'http://site.com/'
print urltoscrape
urltoscrape2 = urltoscrape+'/p1'
print urltoscrape2
listylist = ['p1','p2','p3']
for blah in listylist:
    print blah
    fullurl = urltoscrape+blah
    print fullurl
#
# # Read in a page
html = scraperwiki.scrape("http://uk.soccerway.com/teams/netherlands/fortuna-sittard/1551/")
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
tds = root.cssselect("table.table.squad.sortable td div")
print tds

indexno = 0
record = {}
for td in tds:
    indexno = indexno+1
    print lxml.html.tostring(td)
    print td.text
    fullentry = lxml.html.tostring(td)
    record['td'] = fullentry
    record['index'] = indexno
    scraperwiki.sqlite.save(unique_keys=['indexno'], data=record)
#
# # Write out to the sqlite database using scraperwiki library

#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
