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

CODE = input("Please enter the market you are looking at ")
SOURCE = input("Please enter the source you are looking at ")

mydoc6 = db.attributes.aggregate(
[{
	'$project' : 
	{
		'_id':0, 
		'code':1, 
		'source':1, 
		'report':1, 
		'channel':'$channel'
	}
},
{
	'$unwind':'$channel'
	},
{	
	'$project':
	{
		'_id':0, 
		'code':1, 
		'source':1, 
		'report':1, 
		'std' : '$channel.value', 
		'raw' : '$channel.name'
	}
},
{	
	'$match':
	{
		'code':
		{
			'$in':
			[
            CODE, 	
			]
		},
        'source':
		{
			'$in':
			[
            SOURCE, 	
			]
		}
	}
} 
]
)
Channel_report = []
for x in mydoc6:
     Channel_report.append(x)
df = pd.DataFrame(data =Channel_report)
index = ['source', 'report', 'raw', 'std']
header = [np.array(df['report']),np.array(index)]
df = df.reindex(columns = index)
df =df.pivot(index = 'raw',columns = 'report', values= 'std' )

df.to_csv('channel_check.csv')
print('complete')

print(" CSV of all channels you are that are mapped has been outputted to", os.getcwd())