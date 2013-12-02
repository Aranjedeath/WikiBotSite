#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()
import sys
from unidecode import unidecode
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
                'English'   : 'en',
                'Dutch'     : 'nl',
                'German'    : 'de',
                'Sweedish'  : 'sv',
                'French'    : 'fr',
                'Italian'   : 'it',
                'Russian'   : 'ru',
                'Spanish'   : 'es',
                'Polish'    : 'pl',
                'Waray-waray' : 'war',
                'Cebuano'   : 'ceb',
                'Cietnamese': 'vi',
                'Japanese'  : 'ja',
                'Portuguese': 'pt',
                'Chinese'   : 'zh',
                'Ukranian'  : 'uk',
                'Catalan'   : 'ca',
                'Norwegian' : 'no',
                'Finnish'   : 'fi',
                'Persian'   : 'fa',
                'Indonesian': 'id',
                'Czech'     : 'cs',
                'Korean'    : 'ko',
                'Hungarian' : 'hu',
                'Arabic'    : 'ar',
                'Malay'     : 'ms',
                'Romanian'  : 'ro',
                'Serbian'   : 'sr',
                'Minangkabau':'min',
                'Turkish'   : 'tr',
                'Kazakh'    : 'kk',
                'Slovak'    : 'sk',
                'Esperanto' : 'eo',
                'Danish'    : 'da',
                'Basque'    : 'eu',
                'Lithuanian': 'lt',
                'Bulgarian' : 'bg',
                'Hebrew'    : 'he',
                'Croatian'  : 'hr',
                'Slovenian' : 'sl',
                'Uzbek'     : 'uz',
                'Volapuk'   : 'vo',
                'Estonian'  : 'et',
                'Hindi'     : 'hi',
                'Galician'  : 'gl',
                'Nynorsk'   : 'nn',
                'Simple'    : 'simple'
            }

print "<!DOCTYPE html>"
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
