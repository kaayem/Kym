import openpyxl
import os
import pandas as pd
import ConfigReader 
import mongoCon
import searchingFunctions

path = 'C:/Users/Kaayem/Documents/Python/Kym'

config = ConfigReader.read_config(path)
Query = pd.DataFrame.to_dict(config['MMsearch'],orient='record')
Query = Query[0]
print(Query)
#test = config['MMsearch']
function = Query['Function']
print(function)
dst = Query['dst']

#Allvalues = {x[0]:[y for y in x[1:] if pd.notnull(y)] for x in config['MMsearch'].values}
#metrics = {k:v for k, v in config['metrics'].values}
#levels = {x[0]:[y for y in x[1:] if pd.notnull(y)] for x in config['levels'].values}
#description = {x[0]:[y for y in x[1:] if pd.notnull(y)] for x in config['description'].values}

funcDict = searchingFunctions.functionDict()
d= funcDict[function](Query)

searchingFunctions.csvreturn(dst,d['name'],d['df'])