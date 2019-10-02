#!/usr/bin/env python2 -i

import yaml
import json
import sys
import os
from utils import *

if len(sys.argv) != 2 :
    print "USAGE : ./pgm <yaml-dir>"
    exit(1)

def insert(inn, bowl, ground, ball, score, data) :
    if bowl not in data.keys() :
        data[inn][bowl] = {}
    if ground not in data[inn][bowl].keys() :
        data[inn][bowl][ground] = []
        for i in range(121) :
            tmp = {}
            for i in range(-1, 8) :
                tmp[str(i)] = 0
                
            data[inn][bowl][ground].append(tmp)
    try:        
        data[inn][bowl][ground][ball][str(score)] += 1
    except:
        pass

def save_inning(inn_number, _inn, ground, data) :
    inn = cleanse_inning(_inn)
    ball = 1
    for i in inn :
        j = i[i.keys()[0]]
        score = -1
        if "wicket" not in j.keys() :
            score = int(j["runs"]["batsman"])
        insert(inn_number, j["bowler"], ground, ball, score, data)
        ball += 1

CWD = os.getcwd()
os.chdir(sys.argv[1])
data = {"1": {}, "2":{}}
for i in os.listdir(os.getcwd()) : 
    f = open(i, "r")
    whole = f.read()
    f.close()

    #print i
    try:
        y_data = yaml.load(whole)
        save_inning("1",y_data["innings"][0]["1st innings"]["deliveries"], y_data["info"]["venue"], data)
        save_inning("2",y_data["innings"][1]["2nd innings"]["deliveries"], y_data["info"]["venue"], data)
    except:
        pass

os.chdir(CWD)

json_data_1 = json.dumps(data["1"])
json_data_2 = json.dumps(data["2"])

f = open("../../data/json/bowl_ground_1.json","w")
f.write(json_data_1)
f.close()
f = open("../../data/json/bowl_ground_2.json","w")
f.write(json_data_2)
f.close()
