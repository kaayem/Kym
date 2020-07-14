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
CODE = input("Please enter the market you are looking at ")
REPORT = input("Please enter the category you are looking at ")
SOURCE = input("Please enter the source you are looking at ")

mydoc4 = db.attributes.aggregate([{
    '$project' : {'_id':0,'code':1,'source':1, 'report':1, 'manufacturer':'$manufacturer'}},
    {'$unwind':'$manufacturer'},
    {'$project':{'_id':0,'code':1,'source':1,'report':1,'std' : '$manufacturer.value','raw': '$manufacturer.name'}},
    {'$match':{'code':{'$in':[CODE,]},'source':{'$in':[SOURCE,]}}}])
doc5 = []
for x in mydoc4:
     doc5.append(x)
df = pd.DataFrame(data =doc5)
index = ['code', 'source', 'report', 'raw', 'std']
df = df.reindex(columns = index)
#print(df)
df.to_csv('manufacturer_check.csv')
print('still to do')

print(" CSV of all metrics you are that are mapped has been outputted to", os.getcwd())