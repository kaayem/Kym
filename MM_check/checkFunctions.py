# collection of searching functions
import openpyxl
import os
import pandas as pd
import ConfigReader 
import mongoCon

def attributeCheck(dict):  
    db = mongoCon.AttDB()
    CODE = dict['code']
    REPORT = dict['report']
    SOURCE = dict['source']
    mydoc4 = db.attributes.aggregate([{'$project' : {'_id':0,'code':1,'source':1, 'report':1, 'attribute':'$attribute'}},
                                      {'$unwind':'$attribute'},
                                      {'$project':{'_id':0,'code':1,'source':1,'report':1,'std' : '$attribute.value','raw': '$attribute.name'}},
                                      {'$match':{'code':{'$in':[CODE,]},'source':{'$in':[SOURCE,]}}}])
    doc5 = []
    for x in mydoc4:
         doc5.append(x)
    print("complete3")
    df = pd.DataFrame(data =doc5)
    index = ['code', 'source', 'report', 'raw', 'std']
    df = df.reindex(columns = index)
    df =df.pivot_table(index = 'raw',columns = 'report', values= 'std', aggfunc=lambda x: ' '.join(str(v) for v in x) )
    d = {'name':name, 'df':df}
    return d
    
def brandCheck(dict):  
    db = mongoCon.AttDB()
    CODE = dict['code']
    REPORT = dict['report']
    SOURCE = dict['source']
    mydoc4 = db.attributes.aggregate([{'$project' : {'_id':0,'code':1,'source':1, 'report':1, 'brand':'$brand'}},
                                      {'$unwind':'$brand'},
                                      {'$project':{'_id':0,'code':1,'source':1,'report':1,'std' : '$brand.value','raw': '$brand.name'}},
                                      {'$match':{'code':{'$in':[CODE,]},'source':{'$in':[SOURCE,]}}}])
    doc5 = []
    for x in mydoc4:
         doc5.append(x)
    print("complete3")
    df = pd.DataFrame(data =doc5)
    index = ['code', 'source', 'report', 'raw', 'std']
    df = df.reindex(columns = index)
    name= 'Brand check for '+CODE+ ' '+SOURCE+'.csv'
    d = {'name':name, 'df':df}
    return d    
    
def ChannelCheck(dict):  
    db = mongoCon.AttDB()
    CODE = dict['code']
    REPORT = dict['report']
    SOURCE = dict['source']
    mydoc6 = db.attributes.aggregate([{'$project':{'_id':0, 'code':1, 'source':1, 'report':1, 'channel':'$channel'}},
                                      {'$unwind':'$channel'},
                                      {'$project':{'_id':0, 'code':1, 'source':1, 'report':1, 'std' : '$channel.value', 'raw' : '$channel.name'}}])
    Channel_report = []
    for x in mydoc6:
         Channel_report.append(x)
    df = pd.DataFrame(data =Channel_report)
    index = ['source', 'code', 'raw', 'std']
    header = [np.array(df['code']),np.array(index)]
    df = df.reindex(columns = index)
    name= 'channel check for '+CODE+ ' '+REPORT+'.csv'
    d = {'name':name, 'df':df}
    return d        

def levelCheck(dict):
    db = mongoCon.AttDB()
    CODE = dict['code']
    SOURCE = dict['source']
    mydoc4 = db.attributes.aggregate([{'$project' : {'_id':0,'code':1,'source':1, 'report':1, 'level':'$level'}},
                                      {'$unwind':'$level'},
                                      {'$project':{'_id':0,'code':1,'source':1,'report':1,'std' : '$level.value','raw': '$level.name'}},
                                      {'$match':{'code':{'$in':[CODE,]},'source':{'$in':[SOURCE,]}}}])
    doc5 = []
    for x in mydoc4:
         doc5.append(x)
    print("complete3")
    df = pd.DataFrame(data =doc5)
    index = ['code', 'source', 'report', 'raw', 'std']
    df = df.reindex(columns = index)
    df = df.pivot_table(index = 'raw',columns = 'report', values= 'std', aggfunc=lambda x: ' '.join(str(v) for v in x) )
    name= 'Level check for '+CODE+ ' '+SOURCE+'.csv'
    d = {'name':name, 'df':df}
    return d

def mnfCheck(dict):
    db = mongoCon.AttDB()
    CODE = dict['code']
    SOURCE = dict['source']
    mydoc4 = db.attributes.aggregate([
            {'$project' : {'_id':0,'code':1,'source':1, 'report':1, 'manufacturer':'$manufacturer'}},
            {'$unwind':'$manufacturer'},
            {'$project':{'_id':0,'code':1,'source':1,'report':1,'std' : '$manufacturer.value','raw': '$manufacturer.name'}},
            {'$match':{'code':{'$in':[CODE,]},'source':{'$in':[SOURCE,]}}}])
    doc5 = []
    for x in mydoc4:
         doc5.append(x)
    df = pd.DataFrame(data =doc5)
    index = ['code', 'source', 'report', 'raw', 'std']
    df = df.reindex(columns = index)
    name= 'MNF check for '+CODE+ ' '+SOURCE+'.csv'
    d = {'name':name, 'df':df}
    return d

def metricCheck(dict):
    db = mongoCon.AttDB()
    CODE = dict['code']
    SOURCE = dict['source']
    mydoc6 = db.attributes.aggregate(
            [{'$project' : {'_id':0, 'code':1, 'source':1, 'report':1, 'metric':'$metric'}},
             {'$unwind':'$metric'},
             {'$project':{'_id':0, 'code':1, 'source':1, 'report':1, 'std' : '$metric.value','raw' : '$metric.name','fact' : '$metric.factor'}},
             {'$match':{'code':{'$in':[CODE,]},'source':{'$in':[SOURCE,]}}}])
    Channel_report = []
    for x in mydoc6:
         Channel_report.append(x)
    df = pd.DataFrame(data =Channel_report)
    index = ['source', 'report', 'raw', 'std','fact']
    header = [np.array(df['report']),np.array(index)]
    df = df.reindex(columns = index)
    #df =df.pivot(index = 'raw',columns = 'report', values= ['std', 'fact'] )
    df =df.pivot_table(index = 'raw',columns = 'report', values= ['std', 'fact'], aggfunc=lambda x: ' '.join(str(v) for v in x) )
    name= 'metric check for '+CODE+ ' '+SOURCE+'.csv'
    d = {'name':name, 'df':df}
    return d
# 
def recordCheck(dict):
    db = mongoCon.AttDB()
    CODE = dict['code']
    SOURCE = dict['source']
    mydoc4 = db.attributes.aggregate([{'$project' : {'_id':0,'code':1,'source':1, 'report':1, 'record':'$record'}},
                                    {'$unwind':'$record'},
                                    {'$project':{'_id':0,'code':1,'source':1,'report':1,'std' : '$record.value','raw': '$record.name'}},
                                    {'$match':{'code':{'$in':[CODE,]},'source':{'$in':[SOURCE,]}}}])
    recordReport= []
    for x in mydoc4:
         recordReport.append(x)
    df = pd.DataFrame(data =recordReport)
    index = ['source', 'report', 'raw', 'std','fact']
    header = [np.array(df['report']),np.array(index)]
    df = df.reindex(columns = index)
    #df =df.pivot(index = 'raw',columns = 'report', values= ['std', 'fact'] )
    df =df.pivot_table(index = 'raw',columns = 'report', values= ['std', 'fact'], aggfunc=lambda x: ' '.join(str(v) for v in x) )
    name= 'record check for '+CODE+ ' '+SOURCE+'.csv'
    d = {'name':name, 'df':df}
    return d


def functionDict ():
    Dict1 = { 'attributeCheck': attributeCheck, 'brandCheck':brandCheck, 'channelCheck':channelCheck, 'levelCheck':levelCheck,'mnfCheck':mnfCheck, 'metricCheck':metricCheck, 'recordCheck':recordCheck}
    return Dict1
    
def csvreturn(dst,name,df):
    if dst == 'print':
        print(df)
        return
    df.to_csv(os.path.join(dst,name))
    print(" CSV outputted to", dst)
    return