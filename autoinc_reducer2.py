import sys
# [Define group level master information]
acount = 0
key_old = None

def reset():
    # [Logic to reset master info for every new group]
    acount = 0
    # Run for end of every group

def flush():
    print('%s\t%s' % (key_old, acount))
    # [Write the output]

    # input comes from STDIN
for line in sys.stdin:
    #    [parse the input we got from mapper and update the master info]
    linesplit = line.split('\t')
    key = linesplit[0]
    value = int(linesplit[1])
    if key_old != key:
        if (key_old != None):
            flush()
            acount = 0
    # [detect key changes]
        reset()
    acount += value
    # [update more master info after the key change handling]
    key_old = key
# do not forget to output the last group if needed!
flush()