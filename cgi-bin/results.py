#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()
import sys
from getWiki import Wiki

# Create instance of FieldStorage 
form = cgi.FieldStorage()

# Get data from fields
if len(sys.argv) > 1:
    query = sys.argv[1]
else:
    query = form.getvalue('query')

#get wiki page
wiki = Wiki()
results, categories = wiki.searchwiki(query,"en")

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
    
    <div>
        <form action="results.py" method="post" autocomplete="on" style="margin-left:20px; margin-bottom:10px;">
            <img src="../art/wikibot_logo.png" alt="WikiBot Logo" height="79" width="136"> <input type="text" name="query" size="60" autofocus>
            <input type="submit" value="Search">
        </form>
        <hr>
    </div>
"""
print """
    <div style="margin-left:40px; margin-right:5%; font-size:18px; font-family:Hoefler Text, 'Times New Roman';">
        %s
    <div>
""" % results

print "</body>"
print "</html>"
