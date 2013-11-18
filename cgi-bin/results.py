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
    lang = sys.argv[2]
else:
    query = form.getvalue('query')
    lang = form.getvalue('language')

#get wiki page
wiki = Wiki()
results, categories = wiki.searchwiki(query,lang,True)

langdic = {
                'english'   : 'en',
                'dutch'     : 'nl',
                'german'    : 'de',
                'sweedish'  : 'sv',
                'french'    : 'fr',
                'italian'   : 'it',
                'russian'   : 'ru',
                'spanish'   : 'es',
                'polish'    : 'pl',
                'waray-waray' : 'war',
                'cebuano'   : 'ceb',
                'cietnamese': 'vi',
                'japanese'  : 'ja',
                'portuguese': 'pt',
                'chinese'   : 'zh',
                'ukranian'  : 'uk',
                'catalan'   : 'ca',
                'norwegian' : 'no',
                'finnish'   : 'fi',
                'persian'   : 'fa',
                'indonesian': 'id',
                'czech'     : 'cs',
                'korean'    : 'ko',
                'hungarian' : 'hu',
                'arabic'    : 'ar',
                'malay'     : 'ms',
                'romanian'  : 'ro',
                'serbian'   : 'sr',
                'minangkabau':'min',
                'turkish'   : 'tr',
                'kazakh'    : 'kk',
                'slovak'    : 'sk',
                'esperanto' : 'eo',
                'danish'    : 'da',
                'basque'    : 'eu',
                'lithuanian': 'lt',
                'bulgarian' : 'bg',
                'hebrew'    : 'he',
                'croatian'  : 'hr',
                'slovenian' : 'sl',
                'uzbek'     : 'uz',
                'volapuk'   : 'vo',
                'estonian'  : 'et',
                'hindi'     : 'hi',
                'galician'  : 'gl',
                'nynorsk'   : 'nn',
                'simple'    : 'simple'
            }

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
            <a href="../index.html" class="nav">Home</a>
            <a href="stats.py" class="nav">Stats</a>
            <a href="../faq.html" class="nav">FAQ</a>
        </div>
    </div> 
    
    <div>
        <form action="results.py" method="post" autocomplete="on" style="margin-left:20px; margin-bottom:10px;">
            <img src="../art/wikibot_logo.png" alt="WikiBot Logo" height="79" width="136"> <input type="text" name="query" size="60" autofocus>
            <input type="submit" value="Search">
            <select name="language" class="lang">
"""

for l in langdic:
    if langdic[l] == lang:
        print '<option value="%s" selected>%s</option>' % (langdic[l], l)
    else:
        print '<option value="%s">%s</option>' % (langdic[l], l)

print """                    
              </select>
        </form>
        <hr>
    </div>
"""
print """
    <div style="margin-left:40px; margin-right:5%%; font-size:18px; font-family:Hoefler Text, 'Times New Roman';">
        <p>%s<p>
    <div>
""" % results

print "</body>"
print "</html>"
