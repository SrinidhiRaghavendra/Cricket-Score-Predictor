#!/usr/bin/env python2

import sys
import json

if len(sys.argv) != 3 :
    print "USAGE : ./pgm <json-file> <csv-file>"
    exit(1)

f = open(sys.argv[1], "r")
w = f.read()
f.close()

data = json.loads(w)

stats = []

for bat in data.keys() :
    for bowl in data[bat].keys() :
        for ground in data[bat][bowl].keys() :
            all_balls = data[bat][bowl][ground]
            for ball in range(len(all_balls)) :
                tmp = [bat, bowl, ground, ball]
                tmp1 = all_balls[ball]
                tmp_list = []
                for i in range(7,-2,-1) :
                    tmp_list.append(tmp1[str(i)])

                max_val = max(tmp_list)
                ev = 7 - tmp_list.index(max_val)
                tot = sum(tmp_list)
                if tot != 0 :
                    prob = max_val / float(tot)
                    tmp += [ev, prob]
                    stats.append(tmp)


"""
for bowl in data.keys() :
    for ground in data[bowl].keys() :
        all_balls = data[bowl][ground]
        for ball in range(len(all_balls)) :
            tmp = [bowl, ground, ball]
            tmp1 = all_balls[ball]
            tmp_list = []
            for i in range(-1, 8) :
                tmp_list.append(tmp1[str(i)])

            max_val = max(tmp_list)
            ev = tmp_list.index(max_val) - 1
            tot = sum(tmp_list)
            if tot != 0 :
                prob = max_val / float(sum(tmp_list))
                tmp += [ev, prob]

                stats.append(tmp)
"""

s = ""
for i in stats :
    s += ":".join([str(x) for x in i]) + "\n"
f = open(sys.argv[2], "w")
f.write(s)
f.close()

