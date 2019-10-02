#!/usr/bin/env python2

import sys
import json

if len(sys.argv) != 3 :
    print "USAGE : ./pgm <json-file> <csv-file>"
    exit(1)

f = open(sys.argv[1], "r")
w = f.read()
f.close()

#data = eval(w)
data = json.loads(w)

stats = []

for bat in data.keys() :
    for bowl in data[bat].keys() :
        all_balls = data[bat][bowl]
        for ball in range(len(all_balls)) :
            tmp = [bat, bowl, ball]
            tmp1 = all_balls[ball]
            tmp_list = []
            for i in range(7, -2,-1) :
                tmp_list.append(tmp1[str(i)])

            max_val = max(tmp_list)
            ev = 7 - tmp_list.index(max_val)
            tot = sum(tmp_list)
            if tot != 0 :
                prob = max_val / float(sum(tmp_list))
                tmp += [ev, prob]

                stats.append(tmp)
s = ""
for i in stats :
    s += ":".join([str(x) for x in i]) + "\n"
f = open(sys.argv[2], "w")
f.write(s)
f.close()

