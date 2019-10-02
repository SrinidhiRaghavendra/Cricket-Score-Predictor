#!/usr/bin/env python2 -i

import yaml
import json
import sys
import os

from utils import *

if len(sys.argv) != 2 :
    print "USAGE : ./pgm <yaml-dir>"
    exit(1)

def insert(inn_no,bowl, ball, score, data) :
    if inn_no not in data.keys():
        data[inn_no] = {}
    if bowl not in data[inn_no].keys() :
        data[inn_no][bowl] = []
        for i in range(121) :
            tmp = {}
            for i in range(-1, 8) :
                tmp[str(i)] = 0
            data[inn_no][bowl].append(tmp)
    #print bowl, ball, score
    try:
        data[inn_no][bowl][ball][str(score)] += 1
    except:
        pass

def save_inning(inn_no,_inn, data) :
    inn = cleanse_inning(_inn)
    ball = 1
    for i in inn :
        j = i[i.keys()[0]]
        score = -1
        if "wicket" not in j.keys() :
            score = int(j["runs"]["batsman"])
        insert(inn_no,j["bowler"], ball, score, data)
        ball += 1


CWD = os.getcwd()
os.chdir(sys.argv[1])
data = {"1":{},"2":{}}
for i in os.listdir(os.getcwd()) : 
    f = open(i, "r")
    whole = f.read()
    f.close()

    print i
    try:
        y_data = yaml.load(whole)
        save_inning("1",y_data["innings"][0]["1st innings"]["deliveries"], data)
        save_inning("2",y_data["innings"][1]["2nd innings"]["deliveries"], data)
    except:
        pass

os.chdir(CWD)
'''
f = open("bowl.json", "w")
f.write(json.dumps(data))
f.close()
'''
json_data_1 = json.dumps(data["1"])
json_data_2 = json.dumps(data["2"])

f = open("../../data/json/bowl_1.json","w")
f.write(json_data_1)
f.close()
f = open("../../data/json/bowl_2.json","w")
f.write(json_data_2)
f.close()
