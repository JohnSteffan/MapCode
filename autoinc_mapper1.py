#!/usr/bin/env python
import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    # [derive mapper output key values]
    vals = line.split(',')
    if vals[1] in ['I', 'A']:
        print('%s\t%s' % (vals[2], [vals[1], vals[3], vals[5]]))