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
instruments=['all','piano','violin','flute','clarinet','oboe','trumpet',
             'horn','cello','viola','guitar','string','wind']
types=['all','concerto','symphony','sonata','menuet','toccata','fuga','prelude',
           'lied','oratorio','cantata','mass','opera','waltz'
           'trio','quartet','quintet','sextet','septuor','octuor','ländler','song','variation']

def getcomposerperiod(p):
        """execute sql query"""
        #conn=connect()
        rs=cur.execute("""SELECT DISTINCT C.name, COUNT(*)
  FROM works AS W
JOIN composers  AS C
  ON W.FK_composer=C.PK_composer
WHERE FK_period=?
GROUP BY FK_composer, FK_period
ORDER BY COUNT(*) ASC
LIMIT 10""",p)
    
        
        
        columnsSQL = [column[0] for column in rs.description]
        
        f=rs.fetchall()
        
    
        k=np.asarray(f)
    
    
        sql_data=pd.DataFrame(k,columns=columnsSQL)
        
        return sql_data

def getcomposerperiod2(p):
        """execute sql query"""
        if (p=='0'):
                    rs=cur.execute("""SELECT DISTINCT C.name, COUNT(*)
  FROM works AS W
JOIN composers  AS C
  ON W.FK_composer=C.PK_composer
GROUP BY FK_composer, FK_period
ORDER BY COUNT(*) DESC
LIMIT 10""")
        else:
        #conn=connect()
            rs=cur.execute("""SELECT DISTINCT C.name, COUNT(*)
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
        sql_data.rename(columns={0:'name',1:'total'})
        
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

def gettypeindex(s):
    lgt=len(types)
    j="0"
    for i in range(0,lgt-1):
        if (types[i]==s):
            j=str(i)
            
    return j       

def gettype(s):
    s1="""FK_type="""
    s_out=""
    
    if (s=="all"):
        s_out=""
    else:
        t=gettypeindex(s)
        s_out=s1+t+" "
    return s_out

def getcomposerperiodinstrument(p,i,t):
        """execute sql query"""
        s1="""SELECT DISTINCT C.name, COUNT(*) 
  FROM works AS W
JOIN composers  AS C
  ON W.FK_composer=C.PK_composer
 LEFT OUTER JOIN Types T
ON W.FK_type=T.PK_type """
        
        si=getinstrument(i)
        sp=getperiod(p)
        st=gettype(t)
        s3="""GROUP BY FK_composer, FK_period
ORDER BY COUNT(*) DESC
LIMIT 10"""
        
        if (p=='0'):
            if (i=="all"):
                if (t=="0"):
                    s2=""
                else:
                    s2="""WHERE """+st+" "
            else:
                if (t=="0"):
                    s2="""WHERE """+si+" "
                else:
                    s2="""WHERE """+si+" AND "+st+" "
        elif (i=="all"):
            if (t=="0"):
                s2="""WHERE """+sp
            else:
                s2="""WHERE """+sp+ " AND "+st
        elif (t=="0"):
            s2="""WHERE """+sp+ " AND "+si
        else:
            s2="""WHERE """+sp+" AND "+si+" AND "+st
        
        query=s1+s2+'\n'+s3
        print(query)
        
        
        
        rs=cur.execute(query)
        
        
        
        columnsSQL = [column[0] for column in rs.description]
        
        f=rs.fetchall()
        
    
        k=np.asarray(f)
    
    
        sql_data=pd.DataFrame(k,columns=columnsSQL)
        
        return sql_data

#print(gettype("sonata"))
#print(getinstrument("all"))
#getcomposerperiodinstrument("0","clarinet","0")
#getcomposerperiodinstrument("0","piano","1")
#getcomposerperiodinstrument("0","all","0")
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