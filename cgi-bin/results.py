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
print """
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="Keywords" content="wikipedia,wikibot,wiki,bot,reddit">
	<meta name="Description" content="Site for the Reddit bot WikiBot">
    <link rel="stylesheet" type="text/css" href="../style.css">
"""


print "<title>WikiBot Results</title>"
print "</head>"
print "<body>"

print """
    <div class="navbar">
        <div style="margin-left:15px; padding-top:10px; font-size:25px; font-family:Arial;">
            <a href="../index.html">Home</a>
            <a href="../stats.html">Stats</a>
            <a href="../faq.html">FAQ</a>
        </div>
    </div> 
"""
print "<h2>This is your query: %s</h2>" % query
print "</body>"
print "</html>"