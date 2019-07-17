# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#

# # Read in a page
html = scraperwiki.scrape("https://beta.companieshouse.gov.uk/company/04503188")
#
# # Turn html into a string and put into a variable root
root = lxml.html.fromstring(html)
#Find something on the page to using css selectors
name = root.cssselect('company')

for title in name: 
  print companyname.text

#Find another thing on the page using css selectors
address = root.cssselect('dd')
  print companyaddress.text


#
# # Write out to the sqlite database using scraperwiki library
#scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
#scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
#6DvbCIIZJvt7okpC81Jo5NowvaUDVDAb-ZO668-Y
