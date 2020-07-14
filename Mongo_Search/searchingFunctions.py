# collection of searching functions
import openpyxl
import os
import pandas as pd
import ConfigReader 
import mongoCon


def brandSearch (dict):
    db = mongoCon.AttDB()
    BRD = dict['brand']
    mydoc4 = db.aggregate([{
        '$project' :{'_id':0,'code':1,'source':1,'report':1,'brand':'$brand'}},
        {'$unwind':'$brand'},
        {'$project':{'_id':0,'code':1,'source':1,'report':1,'bstd' : '$brand.value','braw' : '$brand.name',}},
        {'$match':{	'bstd':	{'$in':	[BRD,]}}}])
    doc5 = []
    for x in mydoc4:
         doc5.append(x)
    df = pd.DataFrame(data =doc5)
    index = ['code', 'source', 'report', 'braw', 'bstd']
    df = df.reindex(columns = index)
    
    #print(df)
    name= 'Brand finder for '+BRD+'.csv'
    #df.to_csv(name)
    #print(" CSV outputted to", os.getcwd())
    d = {'name':name, 'df':df}
    return d
  

def ChannelSearch(dict):
    db = mongoCon.AttDB()
    CH = dict['channel']

    mydoc4 = db.aggregate([{
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
    #df.to_csv(name)
    #print(" CSV outputted to", os.getcwd())
    d = {'name':name, 'df':df}
    return d
    
def MNFSearch(dict):
    db = mongoCon.AttDB()
    MNF = dict['manufacturer']

    mydoc4 = db.aggregate([{
        '$project' :{'_id':0,'code':1,'source':1,'report':1,'manufacturer':'$manufacturer'}},
        {'$unwind':'$manufacturer'},
        {'$project':{'_id':0,'code':1,'source':1,'report':1,'mstd' : '$manufacturer.value',	'mraw' : '$manufacturer.name',}},
        {'$match':{	'mstd':	{'$in':	[MNF,]}}}])
    doc5 = []
    for x in mydoc4:
         doc5.append(x)
    df = pd.DataFrame(data =doc5)
    index = ['code', 'source', 'report', 'mraw', 'mstd']
    df = df.reindex(columns = index)
    #print(df)
    name= 'Manufacturer finder for'+MNF+'.csv'
    #df.to_csv(name)
    #print(" CSV outputted to", os.getcwd())
    d = {'name':name, 'df':df}
    return d
   
def MetricSearch(dict): 
    db = mongoCon.AttDB() 
    MET = dict['metric']

    mydoc4 = db.aggregate([{
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
    #df.to_csv(name)
    #print(" CSV outputted to", os.getcwd())
    d = {'name':name, 'df':df}
    return d
def SegSearch(dict): 
    db = mongoCon.AttDB()  
    SEG = dict['segment']

    mydoc4 = db.aggregate([{
        '$project' :{'_id':0,'code':1,'source':1,'report':1,'segment':'$segment'}},
        {'$unwind':'$segment'},
        {'$project':{'_id':0,'code':1,'source':1,'report':1,'sstd' : '$segment.value','sraw' : '$segment.name',}},
        {'$match':{	'sstd':	{'$in':	[SEG,]}}}])
    doc5 = []
    for x in mydoc4:
         doc5.append(x)
    df = pd.DataFrame(data =doc5)
    index = ['code', 'source', 'report', 'sraw', 'sstd']
    df = df.reindex(columns = index)
    #print(df)
    name= 'Segment finder for '+SEG+'.csv'
    #df.to_csv(name)
    #print(" CSV outputted to", os.getcwd())
    d = {'name':name, 'df':df}
    return d
    
def functionDict ():
    Dict1 = { 'brandSearch': brandSearch, 'ChannelSearch':ChannelSearch, 'MNFSearch':MNFSearch, 'MetricSearch':MetricSearch,'SegSearch':SegSearch}
    return Dict1
    
def csvreturn(dst,name,df):
    if dst == 'print':
        print(df)
        return
    df.to_csv(os.path.join(dst,name))
    print(" CSV outputted to", dst)
    return