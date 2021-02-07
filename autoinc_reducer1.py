#!/usr/bin/env python
import sys

# [Define group level master information]
make = None
year = None
vin = None
alist = 0

def reset():
    # [Logic to reset master info for every new group]
    make = None
    year = None
    alist = 0

# Run for end of every group
def flush():
    # [Write the output]
    for x in range(alist):
        #pass
        print('%s\t%s' % (make, year))


# input comes from STDIN
for line in sys.stdin:
    # [parse the input we got from mapper and update the master info]
    current_vin = line[0:17]
    smallline = line[18:]

    #if smallline[2] == 'I':
    #    smallline.strip
    #    vals = line.split(',')
    #    make = vals[1].strip()
    #    year = vals[2][:-1].strip(' ]')

    #if smallline[2] == 'A':
    #    alist += 1
        #print('%s\t%s' % (make, year))
    #print('%s\t%s' % ('A  ', smallline))
    # [detect key changes]
    #print('%s\t%s' % (current_vin, vin))
    if current_vin != vin:
        if (vin != None):
            # write result to STDOUT
            flush()
        reset()
        alist = 0

    if smallline[2] == 'A':
        alist += 1

    if smallline[2] == 'I':
        smallline.strip
        vals = line.split(',')
        make = vals[1].strip()
        year = vals[2][:-1].strip(' ]')
    # [update more master info after the key change handling]
    #current_vin = vin
    vin = current_vin
# do not forget to output the last group if needed!
flush()