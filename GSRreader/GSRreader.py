import openpyxl
import os
import pandas as pd
import ConfigReader
import mongoCon


#def demo():
    #print("now in package")

#path for personal pc
config_path = 'C:/Users/Kaaye/Documents/Python/Kym'
#pull in config GSR data
config = ConfigReader.read_config(config_path)
Query = pd.DataFrame.to_dict(config,orient='record')
#this needs fixing
Query = Query[0]
#p/#rint(Query)
#test = config['MMsearch']
#find path od GSR file
stpath = Query['stpath']
dst = Query['dst']

#TEST_PATH = 'C:/Users/Kaaye/Documents/Python/Kym/GSRreader/FinalAUABM.xlsm'
#file = os.path.join(TEST_PATH,file_name)
#print(TEST_PATH)

#print(df)
#wb = openpyxl.load_workbook(file_name)
#type(wb)
#print(wb.sheetnames)
#config_path = 'C:/Users/Kaayem/Documents/Python/Kym'
def GSRtoDF(stpath):
    df = pd.read_excel(stpath)
    return df
#config = ConfigReader.read_config(config_path)
#print(df.drop(df.index[[1, 2, 3,4,5]]))
#getting the top table
def GSRdfTrim():
    df_trim = df.iloc[0:90,6:46]
    new_header = df_trim.iloc[0] #grab the first row for the header
    df_trim = df_trim[1:] #take the data less the header row
    df_trim.columns = new_header #set the header row as the df header
    df_trim.head()
    print(df_trim)
    df_trim['MAT']= df_trim.iloc[:, -12:].sum(axis=1)
    print(df_trim['MAT'])
    df_trim['MAT-1']= df_trim.iloc[:, -25:-13].sum(axis=1)
    print(df_trim['MAT-1'])
    df_trim['MAT-2']= df_trim.iloc[:, -38:-26].sum(axis=1)
    print(df_trim['MAT-2'])
    df_catjj = df_trim[['Check Template','MAT-2','MAT-1','MAT']]
    df_catjj = df_catjj.iloc[1:3]
    print(df_catjj)
    return df_catjj
