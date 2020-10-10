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
from pandas import DataFrame

def getinfotunes():
    types=['concerto','symphony','sonata','menuet','toccata','fuga','prelude',
           'lied','oratorio','cantata','mass','opera','waltz'
           'trio','quartet','quintet','sextet','septuor','octuor']
    instruments=['piano','violin','flute','clarinet','oboe','trumpet','horn','cello','viola','guitar','double_base']

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
    query2='''SELECT PK_work,  W.title, FK_composer
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
    return sql_data,conn




def getinfotune(w,datalist):
    lgt=len(datalist)
    #matches=sum(x in w for x in datalist)
    for i in range(0,lgt):
        if (datalist[i] in w.lower()):
            return 1

def instrumenttest(w,data):
    lgt=len(data)
    #matches=sum(x in w for x in datalist)
    for i in range(0,lgt):
        if (data in w.lower()):
            return 1


def getmode(w):
    test=mode_pattern.search(w)
    
    #return test
    if test:
        words=w.split()
        lg=len(words)
        for i in range(1,lg):
            if (words[i]=='in'):
                tone=words[i+1]
                mode=words[i+2]
        
        
                return mode

def gettone(w):
    test=mode_pattern.search(w)
    
    #return test
    if test:
        words=w.split()
        lg=len(words)
        for i in range(1,lg):
            if (words[i]=='in'):
                tone=words[i+1]
                mode=words[i+2]
        
        
                return tone

 
musiclist,conn=connsql()
types,instruments,mode_pattern=getinfotunes()

musiclist['FK_Type']=musiclist.apply(lambda x: getinfotune(x.title,types),axis=1)

lginstr=len(instruments)
for i in range(0,lginstr):
    musiclist[instruments[i]]=musiclist.apply(lambda x: instrumenttest(x.title,instruments[i]),axis=1)



musiclist['mode']=musiclist.apply(lambda x: getmode(x.title),axis=1)
musiclist['tone']=musiclist.apply(lambda x: gettone(x.title),axis=1)

lg=len(musiclist)

works2={'PK_work':range(1,lg+1),'title':musiclist['title'],'FK_composer':musiclist['FK_composer'],
        'FK_Type':musiclist['FK_Type'], 
            'piano':musiclist['piano'],
'violin':musiclist['violin'],
'flute':musiclist['flute'],
'clarinet':musiclist['clarinet'],
'oboe':musiclist['oboe'],
'trumpet':musiclist['trumpet'],
'horn':musiclist['horn'],
'cello':musiclist['cello'],
'viola':musiclist['viola'],
'guitar':musiclist['guitar'],
'double_base':musiclist['double_base'],
'Mode':musiclist['mode'],'Tone':musiclist['tone']}
dfml=DataFrame(works2,columns=['PK_work','title','FK_composer','FK_Type',
                               'FK_Instrument',
                               'piano',
'violin',
'flute',
'clarinet',
'oboe',
'trumpet',
'horn',
'cello',
'viola',
'guitar',
'double_base',

                               'Mode',
                               'Tone'])

dfml.to_sql('work2', conn, if_exists='replace', index = False)
#
#
#musiclist.to_csv('islmp.csv')
##test=musiclist.title.head(50)
#
#print(test)
#print(test3)