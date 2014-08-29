#!/usr/bin/python

import sys
mydict=dict()
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisWord, thisId = data_mapped
    if thisId not in mydict.setdefault(thisWord,[]):
    	mydict.setdefault(thisWord,[]).append(thisId)
for id in sorted(mydict['fantastic'],key=int):
	print(id+','),
