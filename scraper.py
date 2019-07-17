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
name = root.cssselect('title')
#for has to match text
for companyname in name: 
  print companyname.text

 #Gettomg the descriptive list
list = root.cssselect('dl')
  print companylist.text
  record = { "companylist" : companylist.text } # column name and value
  scraperwiki.sqlite.save(["companylist"], record)

    #Find info on index
#info = root.cssselect('dt')
#for companyinfo in info:
 #print companyinfo.text
#write out in ordered table
#  record = { "companyinfo" : companyinfo.text } # column name and value
 # scraperwiki.sqlite.save(["companyinfo"], record) # save the records one by one

#
#Find another thing on the page using css selectors
#address = root.cssselect('dd')
#for companyaddress in address:
  #print companyaddress.text
 # record = { "companyaddress" : companyaddress.text } # column name and value
 # scraperwiki.sqlite.save(["companyaddress"], record) # save the records one by one


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
