#!/usr/local/bin/python3

import nltk
import urllib.request as urlreq

pageHtml = ''
with open('facts.txt','r') as pageFile:
    pageHtml = pageFile.read()


#tokens = nltk.word_tokenize(pageHtml)
tokens = nltk.sent_tokenize(pageHtml)

for line in tokens:
   print(nltk.pos_tag(nltk.word_tokenize(line)))
