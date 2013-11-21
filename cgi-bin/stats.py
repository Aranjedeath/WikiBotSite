#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()
import sys
import json
import operator

#open json containg stats
with open('../../WikiBot/stats') as statistics:
        for line in statistics:
            stats = json.loads(line.strip())

#get categories
topcats = {}
for sub in stats['categories']:
    for cat in stats['categories'][sub]:
        try:
            topcats[cat] += stats['categories'][sub][cat]
        except KeyError:
            topcats[cat] = stats['categories'][sub][cat]
        
topcatlist = sorted(topcats.iteritems(), key=operator.itemgetter(1), reverse=True)

print """
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="Keywords" content="wikipedia,wikibot,wiki,bot,reddit">
	<meta name="Description" content="Stats for WikiBot">
	<title>WikiBot Stats</title>
    
    <link rel="stylesheet" type="text/css" href="../style.css">
    
</head>

<body>
    
    <div class="navbar">
        <div style="margin-left:15px; padding-top:10px; font-size:25px; font-family:Arial;">
            <a href="../index.html" class="nav">Home</a>
            <a href="stats.py" class="nav">Stats</a>
            <a href="../faq.html" class="nav">FAQ</a>
        </div>
    </div>
    
    <div style="margin-top:20px; margin-bottom:20px; text-align:center">
        <img src="../art/wikibot_stats.png" alt="WikiBot faq" height=158 width=413 style="text-align:center;">
    </div>
    
    <div style="font-family:Arial; font-size:25px; text-align:center">
    
        <div>
            <b>Number of WikiBot calls:</b>
            <p style="margin-top:5px">%s</p>
        </div>
""" % str(stats['count'])

print """      
        <div style="width:30%; margin-left:15%; height:425px; float:left; padding:20px;">
            <b>10 Most Recent Queries</b>
            <hr>
            <ol class="stat">
"""

for query in stats['queries']:
    print "<li>" + query + "</li>"

print """               
            </ol>
        </div>
            
        <div style="width:30%; margin-right:15%; height:425px; float:right; padding:20px;">
            <b>Top 25 SubReddits</b>
            <hr>
            <ol class="stat">
""" 

subs = []
for sub in stats['subreddits']:
    subs.append((sub,stats['subreddits'][sub]['count']))

for sub in sorted(subs, key=lambda tup: tup[1], reverse=True)[:25]:
    print '<li><a href="http://www.reddit.com/r/' + sub[0] + '">' + sub[0] + "</a>" + ": " + str(sub[1]) + "</li>"

print """
            </ol>
        </div>
        
        <div style="width:30%; margin-left:15%; height:400px; float:left; padding:20px;">
            <b>Top 10 Wikipedia Categories</b>
            <hr>
            <ol class="stat">
""" 

for x in topcatlist[0:10]:
    print "<li>" + x[0].replace("_"," ") + ": " + str(x[1]) + "</li>"

print """
            </ol>
        </div>
                   
            </ol>
        </div>
        
    </div>
    
</body>
</html>
"""
