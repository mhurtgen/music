#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 07:51:29 2020

@author: mhurtgen
"""
import sqlite3
import numpy as np
import pandas as pd
import re

def getinfotunes():
    types=['concerto','symphony','sonata','menuet','toccata','fuga','prelude',
           'lied','oratorio','cantata','mass','opera','waltz'
           'trio','quartet','quintet','sextet','septuor','octuor']
    instruments=['piano','violin','flute','clarinet','oboe','trumpet','horn','cello','viola','guitar']

    mode_pattern=re.compile('.*in [A-G](-(flat|sharp))? major|minor.*')
    return types,instruments,mode_pattern


def connsql():
    conn = sqlite3.connect('ILSMP')   
    
   # cur=conn.cursor()
    query1='''SELECT C.name, COUNT(*)
  FROM works AS W
JOIN composers  AS C
  ON W.FK_composer=C.PK_composer
--WHERE C.name LIKE '%Beethoven%'
GROUP BY FK_composer
ORDER BY COUNT(*) DESC
'''
    query2='''SELECT FK_composer, W.title
  FROM works AS W
--JOIN composers  AS C
--  ON W.FK_composer=C.PK_composer
--WHERE C.name LIKE '%Beethoven%'
--GROUP BY FK_composer
--ORDER BY COUNT(*) DESC
'''
    
    cursor = conn.execute(query2)
    
    columnsSQL = [column[0] for column in cursor.description]
    f=cursor.fetchall()
    k=np.asarray(f)


    sql_data=pd.DataFrame(k,columns=columnsSQL)
    return sql_data




def getinfotune(w,datalist):
    lgt=len(datalist)
    matches=sum(x in w for x in datalist)
    for i in range(0,lgt):
        if (datalist[i] in w.lower()) and (matches==1):
            return i

def getmodes(w):
    test=mode_pattern.search(w)
    
    #return test
    if (test):
        return w
#    
musiclist=connsql()
types,instruments,mode_pattern=getinfotunes()
musiclist['FK_Type']=musiclist.apply(lambda x: getinfotune(x.title,types),axis=1)
musiclist['FK_Instrument']=musiclist.apply(lambda x: getinfotune(x.title,instruments),axis=1)
musiclist['modes']=musiclist.apply(lambda x: getmodes(x.title),axis=1)
test=musiclist.modes.head(100)
#test2=musiclist.Type.value_counts()
#test3=musiclist.Instrument.value_counts()

#
#
musiclist.to_csv('islmp.csv')
##test=musiclist.title.head(50)
#
#print(test)
#print(test3)