#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 07:51:29 2020

@author: mhurtgen
"""
import sqlite3

from pandas import DataFrame
import getdbperiodtotal


types=['concerto','symphony','sonata','menuet','toccata','fuga','prelude',
           'lied','oratorio','cantata','mass','opera','waltz'
           'trio','quartet','quintet','sextet','septuor','octuor','ländler','song']
instruments=['piano','violin','flute','clarinet','oboe','trumpet',
             'horn','cello','viola','guitar','string','wind']
modes=['major','minor'
       ]

conn,cursor=getdbperiodtotal.initcursor()
#c.execute('CREATE TABLE Types (PK_type int, type VARCHAR(20))')
#conn.commit()

Typestab={'PK_type':range(1,len(types)+1),'type':types}
#
df = DataFrame(Typestab, columns= ['PK_type', 'type'])
df.to_sql('Types', conn, if_exists='replace', index = False)
# 

#c.execute('CREATE TABLE Instruments (PK_instrument int, instrument VARCHAR(20))')
#conn.commit()



#c.execute('CREATE TABLE Modes (PK_mode int, mode VARCHAR(20))')
#conn.commit()
#
#Modes={'PK_mode':range(1,len(modes)+1),'mode':modes}
#
#df = DataFrame(Modes, columns= ['PK_mode', 'mode'])
#df.to_sql('Modes', conn, if_exists='replace', index = False)

conn.commit()

#def connsql():
#    conn = sqlite3.connect('ILSMP')   
#    
#   # cur=conn.cursor()
#    query1='''SELECT C.name, COUNT(*)
#  FROM works AS W
#JOIN composers  AS C
#  ON W.FK_composer=C.PK_composer
#--WHERE C.name LIKE '%Beethoven%'
#GROUP BY FK_composer
#ORDER BY COUNT(*) DESC
#'''
#    query2='''SELECT FK_composer, W.title
#  FROM works AS W
#--JOIN composers  AS C
#--  ON W.FK_composer=C.PK_composer
#--WHERE C.name LIKE '%Beethoven%'
#--GROUP BY FK_composer
#--ORDER BY COUNT(*) DESC
#'''
#    
#    cursor = conn.execute(query2)
#    
#    columnsSQL = [column[0] for column in cursor.description]
#    f=cursor.fetchall()
#    k=np.asarray(f)
#
#
#    sql_data=pd.DataFrame(k,columns=columnsSQL)
#    return sql_data
#
#
#
#
#def gettype(w,datalist):
#    lgt=len(datalist)
#    matches=sum(x in w for x in datalist)
#    for i in range(0,lgt):
#        if (datalist[i] in w.lower()) and (matches==1):
#            return i
#
#
#    
#musiclist=connsql()
#
#musiclist['FK_Type']=musiclist.apply(lambda x: gettype(x.title,types),axis=1)
#musiclist['FK_Instrument']=musiclist.apply(lambda x: gettype(x.title,instruments),axis=1)
#
##test=musiclist.Type.head(50)
##test2=musiclist.Type.value_counts()
##test3=musiclist.Instrument.value_counts()
##
##
###musiclist.to_csv('islmp.csv')
###test=musiclist.title.head(50)
##
##print(test2)
##print(test3)