#generate set up checks for python
# check all brands in a market

import pymongo
from pymongo import MongoClient
import pandas as pd
import numpy as np
import os



def db_connect():
    #connecting to a DB in mongoDB
    try:
        if client.get_database(DB_NAME):
            print("Connection Successful!")
            return True
    except:
        print("No, Please check your connection!!!")
        return False

def db_close():
    print ("Connection Getting Closed")
    client.close()

#con = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
con = pymongo.MongoClient("mongodb://192.168.1.181:27017/")
#db = con['mm_pharma'] 
db = con['mm_dev'] 
coll = db['attributes']
print("Have we successfully connected to Mongo?")
db_connect()
print(" Please note this will need to be run in python 2")
CH = input("Please enter the channel you are looking at ")

mydoc4 = db.attributes.aggregate([{
	'$project' :{'_id':0,'code':1,'source':1,'report':1,'channel':'$channel'}},
    {'$unwind':'$channel'},
    {'$project':{'_id':0,'code':1,'source':1,'report':1,'mstd' : '$channel.value',	'mraw' : '$channel.name'}},
    {'$match':{	'mstd':	{'$in':	[CH,]}}}])
doc5 = []
for x in mydoc4:
     doc5.append(x)
df = pd.DataFrame(data =doc5)
index = ['code', 'source', 'report', 'mraw', 'mstd']
df = df.reindex(columns = index)
#print(df)
name= 'Channel finder for '+CH+'.csv'
df.to_csv(name)

print(" CSV of all metrics you are that are mapped has been outputted to", os.getcwd())