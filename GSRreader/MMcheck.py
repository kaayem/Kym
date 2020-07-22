import openpyxl
import os
import pandas as pd
import ConfigReader 
import mongoCon
import searchingFunctions

config_path = 'C:/Users/Kaayem/Documents/Python/Kym'

config = ConfigReader.read_config(config_path)
Query = pd.DataFrame.to_dict(config['MMsearch'],orient='record')
Query = Query[0]
print(Query)
#test = config['MMsearch']
function = Query['Function']
print(function)
dst = Query['dst']


funcDict = searchingFunctions.functionDict()
d= funcDict[function](Query)

searchingFunctions.csvreturn(dst,d['name'],d['df'])