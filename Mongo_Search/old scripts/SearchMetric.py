#generate set up checks for python
# check all brands in a market

import pymongo
from pymongo import MongoClient
import pandas as pd
import numpy as np
import os

#con = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
con = pymongo.MongoClient("mongodb://192.168.1.181:27017/")
db = con['mm_dev']  
coll = db['attributes']
print("Have we successfully connected to Mongo?")
print(" Please note this will need to be run in python 2")
MET = input("Please enter the Metric you are looking at ")

mydoc4 = db.attributes.aggregate([{
	'$project' :{'_id':0,'code':1,'source':1,'report':1,'metric':'$metric'}},
    {'$unwind':'$metric'},
    {'$project':{'_id':0,'code':1,'source':1,'report':1,'mstd' : '$metric.value',	'mraw' : '$metric.name','fact' : '$metric.factor'}},
    {'$match':{	'mstd':	{'$in':	[MET,]}}}])
doc5 = []
for x in mydoc4:
     doc5.append(x)
df = pd.DataFrame(data =doc5)
index = ['code', 'source', 'report', 'mraw', 'mstd', 'fact']
df = df.reindex(columns = index)
#print(df)
name= 'Metric finder for '+MET+'.csv'
df.to_csv(name)

print(" CSV of all metrics you are that are mapped has been outputted to", os.getcwd())