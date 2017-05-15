# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import json


### converting the csv files to json format to make
### them readable by d3.js

nodes = np.genfromtxt("Datasets/FB_Group_Data/group_nodes.csv",
                      dtype = 'object',
                      delimiter=',',
                      skip_header=1,
                      usecols=(0,1)) ##reading only the name and label

edges = np.genfromtxt("Datasets/FB_Group_Data/group_edges.csv",
                      dtype='object',
                      delimiter=',',
                      skip_header=1,
                      usecols=(0,1)) ## only the source and target values

### replacing the appearance of each ID in the edges 
### with their position in the list of nodes
for n in range(len(nodes)):
    for ls in range(len(edges)):
        if nodes[n][0] == edges[ls][0]:
            edges[ls][0] = n
        if nodes[n][0] == edges[ls][1]:
            edges[ls][1] = n

data = {} ### creating a dictionary to store the JSON file
 
## we want nodes in the format [{"name":"X", "label":"Y"}]
lst = []
for x in nodes:
    d = {}
    d["name"]=str(x[0]).replace("b'","").replace("","")
    d["label"]=str(x[1]).replace("b'","").replace("","")
    lst.append(d)
data["nodes"] = lst

## we want edges in the format [{"source":"O", "target":"1"}]
lnks = []
for ls in edges:
    d = {}
    d["source"]=ls[0]
    d["target"]=ls[1]
    lnks.append(d)
data["edges"]=lnks

## saving the data to json format
with open("Datasets/FB_Group_Data/group_posts.json", "w") as f:
    f.write(json.dumps(data))
    
