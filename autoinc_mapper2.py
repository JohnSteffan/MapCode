#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # [derive mapper output key values]
    linesplit = line.split('\t')
    key = linesplit[0][1:-1] + linesplit[1][1:-2]#.split('\'')
    value = '1'
    print('%s\t%s' % (key, value))