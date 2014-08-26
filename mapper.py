#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, f2, f3, date, timezone, verb, url, methods, response, size = data
        print "{0}\t1".format(url)
