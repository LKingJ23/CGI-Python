#!/usr/bin/python
# -*- coding: utf8 -*-

import lxml
from lxml import etree
import urllib2

print "Content-type: text/html\n\n"
print "<head>"
print "<meta charset=UTF-8>"
print "</head>"

ns={"Atom" : "http://www.w3.org/2005/Atom"}
parser=etree.XMLParser()
tree=etree.parse(urllib2.urlopen('https://api.flickr.com/services/feeds/photos_public.gne?tags=sevilla'),parser)
for node in tree.xpath('//Atom:entry/Atom:title', namespaces=ns) :
    print node.text.encode("utf8") + "<br />"
