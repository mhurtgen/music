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
import pickle as p

from pandas import DataFrame

def column(matrix, i):
    return [row[i] for row in matrix]

def getinfotunes():
    types=['concerto','symphony','sonata','menuet','toccata','fuga','prelude',
           'lied','oratorio','cantata','mass','opera','waltz'
           'trio','quartet','quintet','sextet','septuor','octuor','ländler','song','variation']
    instruments=['piano','violin','flute','clarinet','oboe','trumpet','horn',
                 'cello','viola','guitar','double_base']

    mode_pattern=re.compile('.*in [A-G](-(flat|sharp))? major|minor.*')
    return types,instruments,mode_pattern


def connsql():
    conn = sqlite3.connect('ILSMPperiod')   
    return conn

def composers():
    query1='''SELECT PK_composer, name, FK_period
        FROM composers'''
    return query1
    

def bestcomposers():
   # cur=conn.cursor()
    query1='''SELECT C.name, COUNT(*)
  FROM works AS W
JOIN composers  AS C
  ON W.FK_composer=C.PK_composer
--WHERE C.name LIKE '%Beethoven%'
GROUP BY FK_composer, FK_period
ORDER BY COUNT(*) DESC
'''
    return query1

def works():
    query2='''SELECT PK_work,  W.title, FK_composer
  FROM works AS W
--JOIN composers  AS C
--  ON W.FK_composer=C.PK_composer
--WHERE C.name LIKE '%Beethoven%'
--GROUP BY FK_composer
--ORDER BY COUNT(*) DESC
'''
    return query2

def getdata(conn,query):    
    cursor = conn.execute(query)
    
    columnsSQL = [column[0] for column in cursor.description]
    f=cursor.fetchall()
    k=np.asarray(f)


    sql_data=pd.DataFrame(k,columns=columnsSQL)
    return sql_data




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

def getinstruments(pk,w,instruments):
    lgt=len(instruments)
    work_instruments=list()
    work=pk
    for i in range(0,lgt):
        instrument=instruments[i]
        if (instrument in w.lower()):
            
            work_instruments.append([work,i])
    return work_instruments

def getmode(mode_pattern,w):
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

def gettone(mode_pattern,w):
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

def main(): 
    
     
    conn=connsql()
    
    composer=composers()
    tunes=works()
    
    musiclist=getdata(conn,tunes)
    
    types,instruments,mode_pattern=getinfotunes()
    
    musiclist['FK_Type']=musiclist.apply(lambda x: getinfotune(x.title,types),axis=1)
    
    lginstr=len(instruments)
    for i in range(0,lginstr):
        musiclist[instruments[i]]=musiclist.apply(lambda x: instrumenttest(x.title,instruments[i]),axis=1)
    #musiclist.apply(lambda x: getinstruments(x.PK_work,x.title,instruments),axis=1)
    
    
    musiclist['mode']=musiclist.apply(lambda x: getmode(mode_pattern,x.title),axis=1)
    musiclist['tone']=musiclist.apply(lambda x: gettone(mode_pattern,x.title),axis=1)
    
    lg=len(musiclist)
    
    works2={'PK_work':range(1,lg+1),'title':musiclist['title'],'FK_composer':musiclist['FK_composer'],
            'FK_Type':musiclist['FK_Type'],'Mode':musiclist['mode'],'Tone':musiclist['tone'],
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
            'double_base':musiclist['double_base']}

   # work_instruments2={'FK_work':column(work_instruments,0),'FK_instrument':column(work_instruments,1)}
    
    dfml=DataFrame(works2,columns=['PK_work','title','FK_composer','FK_Type',                               
                                   'Mode',
                                   'Tone',
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
                                    'double_base'
                        ])
    
   # dfwi=DataFrame(work_instruments2,columns=['FK_work','FK_instrument'])
    #
    #dfml.to_sql('work2', conn, if_exists='replace', index = False)
    
    with open('tunes.pkl','wb') as f:
        dfml.to_pickle(f);

#    composer2={'PK_composer':composer['PK_composer'],'name':composer['name']
#    ,'FK_period':composer['FK_period']}
#    dfc=DataFrame(composer2,columns=['PK_composer','name','FK_period'])
#    with open('composers.pkl','wb') as f:
#        dfc.to_pickle(f);

    conn.close()

def getcomposers() :
    conn=connsql()
    
    composer=composers()
    composers2=getdata(conn,composer)
    composer2={'PK_composer':composers2['PK_composer'],'name':composers2['name']
    ,'FK_period':composers2['FK_period']}
    dfc=DataFrame(composer2,columns=['PK_composer','name','FK_period'])
    with open('composers.pkl','wb') as f:
        dfc.to_pickle(f);
    

    conn.close()
#test()
main()
#
#
#musiclist.to_csv('islmp.csv')
##test=musiclist.title.head(50)
#
#print(test)
#print(test3)