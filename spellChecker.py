#!/usr/bin/python
from enchant.checker import SpellChecker

chkr = SpellChecker("en_GB")
chkr.set_text("astrnaut")
for err in chkr:
    print "ERROR:", err.word
