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
print("We have successfully connected to Mongo")

CODE = input("Please enter the market you are looking at ")
REPORT = input("Please enter the category you are looking at ")
SOURCE = input("Please enter the source you are looking at ")
mydoc4 = db.attributes.aggregate([{'$project' : {'_id':0,'code':1,'source':1, 'report':1, 'brand':'$brand'}},{'$unwind':'$brand'},{'$project':{'_id':0,'code':1,'source':1,'report':1,'std' : '$brand.value','raw': '$brand.name'}},{'$match':{'code':{'$in':[CODE,]},'source':{'$in':[SOURCE,]}}}])
doc5 = []
for x in mydoc4:
     doc5.append(x)
print("complete3")
df = pd.DataFrame(data =doc5)
index = ['code', 'source', 'report', 'raw', 'std']
df = df.reindex(columns = index)
print(df)
df.to_csv('brandcheck.csv')

print(" CSV of all brands you are that are mapped has been outputted to", os.getcwd())