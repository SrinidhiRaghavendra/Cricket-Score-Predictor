#!/usr/bin/env python2 -i

import yaml
import json
import sys
import os

from utils import *

if len(sys.argv) != 2 :
    print "USAGE : ./pgm <yaml-dir>"
    exit(1)

def insert(inn,ground, ball, score, data) :
    if inn not in data.keys():
        data[inn] ={}
    if ground not in data[inn].keys() :
        data[inn][ground] = []
        for i in range(121) :
            tmp = {}
            for i in range(-1, 8) :
                tmp[str(i)] = 0
            data[inn][ground].append(tmp)
    #print ground, ball, score
    try:
        data[inn][ground][ball][str(score)] += 1
    except:
        pass

def save_inning(inn_no,_inn, grnd, data) :
    inn = cleanse_inning(_inn)
    ball = 1
    for i in inn :
        j = i[i.keys()[0]]
        score = -1
        if "wicket" not in j.keys() :
            score = int(j["runs"]["batsman"])
        insert(inn_no,grnd, ball, score, data)
        ball += 1


CWD = os.getcwd()
os.chdir(sys.argv[1])
data = {}
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

f = open("../../data/json/ground_1.json","w")
f.write(json_data_1)
f.close()
f = open("../../data/json/ground_2.json","w")
f.write(json_data_2)
f.close()
