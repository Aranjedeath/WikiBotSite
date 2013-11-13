#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
query = form.getvalue('query')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>WikiBot Results</title>"
print "</head>"
print "<body>"
print "<h2>This is your query: </h2>" % (query)
print "</body>"
print "</html>"