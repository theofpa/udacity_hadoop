#!/usr/bin/python

import sys
import re
for line in sys.stdin:
    data = line.strip().split("	")
    if len(data) == 19:
        id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = data
	for word in re.findall(r"[\w']+",body):
        	print "{0}\t{1}".format(word.lower(),id.replace("\"",""))
