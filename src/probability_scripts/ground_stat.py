#!/usr/bin/env python2

import sys
import json

if len(sys.argv) != 3 :
    print "USAGE : ./pgm <json-file>"
    exit(1)

f = open(sys.argv[1], "r")
w = f.read()
f.close()

data = json.loads(w)

stats = []
for ground in data.keys() :
    for ball in range(len(data[ground])) :
        tmp = data[ground][ball]
        tmp1 = []
        for i in range(7,-2,-1) :
            tmp1.append(tmp[str(i)])
       
        tot = sum(tmp1)
        if tot != 0 :
            ev = tmp1.index(max(tmp1))
            ev = 7 - ev
            prob = max(tmp1) / float(tot)
            stats.append([ground, ball, ev, prob])


s = ""
for i in stats :
    s += ":".join([str(x) for x in i]) + "\n"
f = open(sys.argv[2], "w")
f.write(s)
f.close()

