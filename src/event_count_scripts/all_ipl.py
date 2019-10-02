#!/usr/bin/env python2 -i

import yaml
import json
import sys
import os

from utils import *

if len(sys.argv) != 2 :
    print "USAGE : ./pgm <yaml-dir>"
    exit(1)

def save_inning(inn_no,_inn, data) :
    inn = cleanse_inning(_inn)
    ball = 1

    for i in inn :
        j = i[i.keys()[0]]
        #print j
        score = -1
        if "wicket" not in j.keys() :
            score = int(j["runs"]["batsman"])
        try:
           data[inn_no][ball][str(score)] += 1
        except:
           pass
        ball += 1
    

CWD = os.getcwd()
os.chdir(sys.argv[1])
data = {"1":[],"2":[]}

#data.append({"1":None})
#data.append({"2":None})
for i in range(200) :
    tmp = {}
    tmp2 = {}
    for j in range(-1, 8) :
        tmp[str(j)] = 0
        tmp2[str(j)] = 0

    data["1"].append(tmp) 
    data["2"].append(tmp2)
#print id(data["1"]),id(data["2"])
#exit()
for i in os.listdir(os.getcwd()) : 
    f = open(i, "r")
    whole = f.read()
    f.close()

    #print i
    try:
        y_data = yaml.load(whole)
        save_inning("1",y_data["innings"][0]["1st innings"]["deliveries"], data)
        save_inning("2",y_data["innings"][1]["2nd innings"]["deliveries"], data)
    except:
        pass

json_data_1 = json.dumps(data["1"])
json_data_2 = json.dumps(data["2"])

#print (data["1"])
#print (data["2"])

f = open("../../data/json/all_ipl_1.json","w")
f.write(json_data_1)
f.close()
f = open("../../data/json/all_ipl_2.json","w")
f.write(json_data_2)
f.close()
