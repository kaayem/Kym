#connect to mongo DB


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

def AttDB ():
    #con = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
    con = pymongo.MongoClient("mongodb://192.168.1.181:27017/")
   
    db = con['mm_dev']  
    coll = db['attributes']
    #db_connect()   
    return coll