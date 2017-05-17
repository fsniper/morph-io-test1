# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful


import scraperwiki
import lxml.html
try:
     from HTMLParser import HTMLParser
except ImportError:
     from html.parser import HTMLParser
 
h = HTMLParser()

from lxml.etree import tostring

url = "http://www.tmo.gov.tr:8081/default.asp?kimlikno=%s"
tcks = [ "22870737466",
         "22870737466"]
#
# # Read in a page
for tck in tcks:
  html = scraperwiki.scrape(url % (tck,))

#
# # Find something on the page using css selectors
  root = lxml.html.fromstring(html)
  d = root.cssselect("tr")

  output = ""
  for t in d:
         output = output  + h.unescape(tostring(t)) + "\n"
         
#
# # Write out to the sqlite database using scraperwiki library
  scraperwiki.sqlite.save(unique_keys=['tck'], data={"tck": tck, "data": output.encode("utf8") })
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
