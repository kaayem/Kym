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
SOURCE = input("Please enter the source you are looking at ")

mydoc6 = db.attributes.aggregate(
[{
	'$project' : 
	{
		'_id':0, 
		'code':1, 
		'source':1, 
		'report':1, 
		'metric':'$metric'
	}
},
{
	'$unwind':'$metric'
	},
{	
	'$project':
	{
		'_id':0, 
		'code':1, 
		'source':1, 
		'report':1, 
		'std' : '$metric.value', 
		'raw' : '$metric.name',
        'fact' : '$metric.factor'
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
index = ['source', 'report', 'raw', 'std','fact']
header = [np.array(df['report']),np.array(index)]
df = df.reindex(columns = index)
#df =df.pivot(index = 'raw',columns = 'report', values= ['std', 'fact'] )
df =df.pivot_table(index = 'raw',columns = 'report', values= ['std', 'fact'], aggfunc=lambda x: ' '.join(str(v) for v in x) )
df.to_csv('metric_check.csv')
print('complete')

print(" CSV of all metrics you are that are mapped has been outputted to", os.getcwd())