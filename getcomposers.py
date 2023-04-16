#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:36:18 2023

@author: mhurtgen
"""

import sqlite3

import pandas as pd
import numpy as np

#from collections import OrderedDict
#import dash_core_components as dcc

conn=sqlite3.connect('ISMLPperiodtotal2',check_same_thread=False)
cur=conn.cursor()
instruments=['piano','violin','flute','clarinet','oboe','trumpet',
             'horn','cello','viola','guitar','string','wind']

def getcomposerperiod(p):
        """execute sql query"""
        #conn=connect()
        rs=cur.execute("""SELECT C.name, COUNT(*)
  FROM works AS W
JOIN composers  AS C
  ON W.FK_composer=C.PK_composer
WHERE FK_period=?
GROUP BY FK_composer, FK_period
ORDER BY COUNT(*) DESC
LIMIT 10""",p)
    
        
        
        columnsSQL = [column[0] for column in rs.description]
        
        f=rs.fetchall()
        
    
        k=np.asarray(f)
    
    
        sql_data=pd.DataFrame(k,columns=columnsSQL)
        
        return sql_data

def getcomposerperiod2(p):
        """execute sql query"""
        if (p=='0'):
                    rs=cur.execute("""SELECT C.name, COUNT(*)
  FROM works AS W
JOIN composers  AS C
  ON W.FK_composer=C.PK_composer
GROUP BY FK_composer, FK_period
ORDER BY COUNT(*) DESC
LIMIT 10""")
        else:
        #conn=connect()
            rs=cur.execute("""SELECT C.name, COUNT(*)
  FROM works AS W
JOIN composers  AS C
  ON W.FK_composer=C.PK_composer
WHERE FK_period=?
GROUP BY FK_composer, FK_period
ORDER BY COUNT(*) DESC
LIMIT 10""",p)
    
        
        
        columnsSQL = [column[0] for column in rs.description]
        
        f=rs.fetchall()
        
    
        k=np.asarray(f)
    
    
        sql_data=pd.DataFrame(k,columns=columnsSQL)
        
        return sql_data

def getinstrument(instr):
    number_instruments=len(instruments)
    s=""
    if (instr=="all"):
        s=""
    else:
        for i in range(0,number_instruments-1):
            if (instr==instruments[i]):
                s=str(instr)+"=1"
    return s

def getperiod(p):
    s1="""FK_period="""
    s2=str(p)
    if (p=="0"):
        s=""
    else:
        s=s1+s2+" "
    return s

def getcomposerperiodinstrument(p,i):
        """execute sql query"""
        s1="""SELECT C.name, COUNT(*)
  FROM works AS W
JOIN composers  AS C
  ON W.FK_composer=C.PK_composer """
        
        si=getinstrument(i)
        sp=getperiod(p)
        
        s3="""GROUP BY FK_composer, FK_period
ORDER BY COUNT(*) DESC
LIMIT 10"""
        
        if (p=='0'):
            if (i=="all"):
                s2=""
            else:
                s2="""WHERE """+si+" "
            
        elif (i=="all"):
            s2="""WHERE """+sp+" "
        else:
            s2="""WHERE """+sp+" AND "+si+" "
        
        query=s1+s2+s3
        print(query)
        
        
        
        rs=cur.execute(query)
        
        
        
        columnsSQL = [column[0] for column in rs.description]
        
        f=rs.fetchall()
        
    
        k=np.asarray(f)
    
    
        sql_data=pd.DataFrame(k,columns=columnsSQL)
        
        return sql_data


getcomposerperiodinstrument("3","piano")

#            
#    if (instr=="violin"):
#        s="violin=1"
#    elif(instr="piano"):
#        s="violin=1"
#        query="""SELECT C.name, FK_period, COUNT(*)
#  FROM works AS W
#JOIN composers  AS C
#  ON W.FK_composer=C.PK_composer
#WHERE FK_period IN (3,1) AND violin=1
#GROUP BY FK_composer, FK_period
#ORDER BY COUNT(*) DESC"""
#cur.close()

#df = pd.read_sql(("""
#            SELECT C.name, COUNT(*)
#  FROM works AS W
#JOIN composers  AS C
#  ON W.FK_composer=C.PK_composer
#WHERE FK_period=%(period)i
#GROUP BY FK_composer, FK_period
#ORDER BY COUNT(*) DESC
#LIMIT 10
#            """), conn,params={"period":1})
#
#x=df.iloc[:, 1]
#y=df.iloc[:, 0]
#fig = px.bar(df, x, y, orientation='h',
#             
#             height=400,
#             title='Prolific composers')
#fig.show()