#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:04:20 2020

@author: mhurtgen
"""
import numpy as np
import pandas as pd
import pickle as pk
import sqlite3

def connsql():
    conn = sqlite3.connect('ILSMPperiod')   
    return conn

def composers():
    query1='''SELECT PK_composer, name
        FROM composers'''
    return query1
    

def getdata(conn,query):    
    cursor = conn.execute(query)
    
    columnsSQL = [column[0] for column in cursor.description]
    f=cursor.fetchall()
    k=np.asarray(f)


    sql_data=pd.DataFrame(k,columns=columnsSQL)
    return sql_data

conn=connsql()
composer=composers()

composerlist=getdata(conn,composer)
conn.close()
composers={'PK_composer':composerlist['PK_composer'], 'name':composerlist['name']}
dfc=pd.DataFrame(composers)
with open('composers.pkl','wb') as f:
    dfc.to_pickle(f)
    
    
    

