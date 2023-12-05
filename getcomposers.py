#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 09:36:18 2023

@author: mhurtgen
"""

import sqlite3

import pandas as pd
import numpy as np
import math

#from collections import OrderedDict
#import dash_core_components as dcc

conn=sqlite3.connect('ISMLPperiodtotal2',check_same_thread=False)
cur=conn.cursor()
instruments=['piano','violin','flute','clarinet','oboe','trumpet','horn',
                 'cello','viola','guitar','double_base','string','wind','organ']
types=['all','concerto','symphony','sonata','menuet','toccata','fuga','prelude',
           'lied','oratorio','cantata','mass','opera','waltz',
           'trio','quartet','quintet','sextet','septuor','octuor','ländler','song','variation','romance']

def getcomposers():
    """execute sql query"""
    rs=cur.execute("""SELECT PK_composer,name
                         FROM composers
                         ORDER BY name""")
    columnsSQL = [column[0] for column in rs.description]
       
    f=rs.fetchall()
        
    
    k=np.asarray(f)
    
    
    sql_data=pd.DataFrame(k,columns=columnsSQL)
        
    return sql_data

def gettypes():
    """execute sql query"""
    rs=cur.execute("""SELECT PK_type,type
                         FROM types""")
    columnsSQL = [column[0] for column in rs.description]
       
    f=rs.fetchall()
        
    
    k=np.asarray(f)
    
    
    sql_data=pd.DataFrame(k,columns=columnsSQL)
        
    return sql_data

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
        for i in range(0,number_instruments):
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
        sql_data=pd.DataFrame()
        s1="""SELECT DISTINCT C.name, COUNT(*) AS Compositions
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
                if (t=="all"):
                    s2=""
                else:
                    s2="""WHERE """+st+" "
            else:
                if (t=="all"):
                    s2="""WHERE """+si+" "
                else:
                    s2="""WHERE """+si+" AND "+st+" "
        else:
            if (i=="all"):
                if (t=="all"):
                    s2="""WHERE """+sp
                else:
                    s2="""WHERE """+sp+ " AND "+st
            else:
                if (t=="all"):
                    s2="""WHERE """+sp+ " AND "+si
                else:
                    s2="""WHERE """+sp+" AND "+si+" AND "+st
        
        query=s1+s2+'\n'+s3
        print(query)
        
        
        
        rs=cur.execute(query)
        
        
        try: 
            columnsSQL = [column[0] for column in rs.description]
        
            f=rs.fetchall()
        
    
            k=np.asarray(f)
    
    
            sql_data=pd.DataFrame(k,columns=columnsSQL)
        except: ValueError
        
        return sql_data

def getcomposerperiodinstrument2(p,i,t):
        """execute sql query"""
        sql_data=pd.DataFrame()
        s1="""SELECT DISTINCT C.PK_composer, C.name
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
                if (t=="all"):
                    s2=""
                else:
                    s2="""WHERE """+st+" "
            else:
                if (t=="all"):
                    s2="""WHERE """+si+" "
                else:
                    s2="""WHERE """+si+" AND "+st+" "
        elif (i=="all"):
            if (t=="all"):
                s2="""WHERE """+sp
            else:
                s2="""WHERE """+sp+ " AND "+st
        elif (t=="all"):
            s2="""WHERE """+sp+ " AND "+si
        else:
            s2="""WHERE """+sp+" AND "+si+" AND "+st
        
        query=s1+s2+'\n'+s3
        #print(query)
        
        
        
        rs=cur.execute(query)
        
        
        try: 
            columnsSQL = [column[0] for column in rs.description]
        
            f=rs.fetchall()
        
    
            k=np.asarray(f)
    
    
            sql_data=pd.DataFrame(k,columns=columnsSQL)
        except: ValueError
        
        return sql_data


def getcomposerperiodinstrument_details(p,i,t,FK_composer):
        """execute sql query"""
#        if (i=="all" or t=="0"):
#            return
#        
        s1="""SELECT T.PK_type, C.name
  FROM works AS W
JOIN composers  AS C
  ON W.FK_composer=C.PK_composer
 LEFT OUTER JOIN Types T
ON W.FK_type=T.PK_type """
        
        si=getinstrument(i)
        sp=getperiod(p)
        st=gettype(t)
        s3="""
        ORDER BY C.PK_composer, W.FK_type"""
        
        if (p=='0'):
            if (i=="all"):
                if (t=="all"):
                    s2=""
                else:
                    s2="""WHERE """+st+" "
            else:
                if (t=="all"):
                    s2="""WHERE """+si+" "
                else:
                    s2="""WHERE """+si+" AND "+st+" "
        elif (i=="all"):
            if (t=="all"):
                s2="""WHERE """+sp
            else:
                s2="""WHERE """+sp+ " AND "+st
        elif (t=="all"):
            s2="""WHERE """+sp+ " AND "+si
        else:
            s2="""WHERE """+sp+" AND "+si+" AND "+st
        sc=" AND FK_composer=?"
        query=s1+s2+sc+'\n'+s3
        print(query)
        
        
        
        rs=cur.execute(query,FK_composer)
        
        
        try:
            columnsSQL = [column[0] for column in rs.description]
        
            f=rs.fetchall()
        
    
            k=np.asarray(f)
    
    
            sql_data=pd.DataFrame(k,columns=columnsSQL)
            return sql_data
        except: ValueError
        
def getcomposer_details(t,FK_composer):  
        """execute sql query"""
#        if (i=="all" or t=="0"):
#            return
#        
        query="""SELECT W.title
  FROM works AS W
JOIN composers  AS C
  ON W.FK_composer=C.PK_composer
 WHERE W.FK_type=? AND FK_composer=?"""
        
                
        
        rs=cur.execute(query,(t,FK_composer,))
        
        
        try:
            columnsSQL = [column[0] for column in rs.description]
        
            f=rs.fetchall()
        
    
            k=np.asarray(f)
    
    
            sql_data=pd.DataFrame(k,columns=columnsSQL)
            return sql_data
        except: ValueError

def getcomposer_types(FK_composer):
        """execute sql query"""
#        if (i=="all" or t=="0"):
#            return
#       
        if (FK_composer=='0'):
            rs=cur.execute("""SELECT T.type, COUNT(*)
  FROM works AS W
JOIN composers  AS C
  ON W.FK_composer=C.PK_composer
 LEFT OUTER JOIN Types T
ON W.FK_type=T.PK_type 
GROUP BY W.FK_type
ORDER BY W.FK_type""")
        else:            
            rs=cur.execute("""SELECT T.type, COUNT(*)
  FROM works AS W
JOIN composers  AS C
  ON W.FK_composer=C.PK_composer
 LEFT OUTER JOIN Types T
ON W.FK_type=T.PK_type 
WHERE FK_composer=?
GROUP BY W.FK_type
ORDER BY W.FK_type""",(FK_composer,))
        
        
        try:
            columnsSQL = [column[0] for column in rs.description]
        
            f=rs.fetchall()
        
    
            k=np.asarray(f)
    
    
            sql_data=pd.DataFrame(k,columns=columnsSQL)
            #sql_data=pd.to_numeric(sql_data)#.columns[1])
            s2=sql_data.sort_values(sql_data.columns[1],ascending=False)
            return s2#sql_data#.values.tolist()
        
        except: ValueError
        
        
def getcomposer_instruments(FK_type,FK_composer):#corriger colonnes: à séparer
        """execute sql query"""
#        if (i=="all" or t=="0"):
#            return
#       
        if (FK_composer=='0'):
            sql_data=pd.read_sql("""SELECT SUM(piano) AS piano, SUM(violin) AS violin, 
                       SUM(flute) AS flute, SUM(clarinet) AS clarinet, SUM(oboe) AS oboe,
                       SUM(trumpet) AS trumpet, SUM(horn) AS horn, SUM(bassoon) AS bassoon, SUM(cello) AS cello,
                        SUM(viola) AS viola, SUM(guitar) AS guitar, SUM(contrabass) AS contrabass,
                        SUM(organ) AS organ
FROM works
WHERE FK_Type=?""",(FK_type,))
            rs=cur.execute("""SELECT SUM(piano) AS piano, SUM(violin) AS violin, 
                       SUM(flute) AS flute, SUM(clarinet) AS clarinet, SUM(oboe) AS oboe,
                       SUM(trumpet) AS trumpet, SUM(horn) AS horn, SUM(bassoon) AS bassoon, SUM(cello) AS cello,
                        SUM(viola) AS viola, SUM(guitar) AS guitar, SUM(contrabass) AS contrabass,
                        SUM(organ) AS organ
FROM works
WHERE FK_Type=?""",(FK_type,))
        else:
#             sql_data=pd.read_sql("""SELECT SUM(piano) AS piano, SUM(violin) AS violin, 
#                        SUM(flute) AS flute, SUM(clarinet) AS clarinet, SUM(oboe) AS oboe,
#                        SUM(trumpet) AS trumpet, SUM(horn) AS horn, SUM(bassoon) AS bassoon, SUM(cello) AS cello,
#                         SUM(viola) AS viola, SUM(guitar) AS guitar, SUM(contrabass) AS contrabass,
#                         SUM(organ) AS organ
# FROM works
# WHERE FK_Type=?""",(FK_type,))
            
            rs=cur.execute("""SELECT SUM(piano) AS piano, SUM(violin) AS violin, 
                        SUM(flute) AS flute, SUM(clarinet) AS clarinet, SUM(oboe) AS oboe,
                        SUM(trumpet) AS trumpet, SUM(horn) AS horn, SUM(bassoon) AS bassoon, SUM(cello) AS cello,
                        SUM(viola) AS viola, SUM(guitar) AS guitar, SUM(contrabass) AS contrabass,
                        SUM(organ) AS organ
FROM works
WHERE FK_Type=? AND FK_composer=?""",(FK_type,FK_composer,))
            #print(rs.description)
        
        try:
            #columnsSQL=[rs.fetchall()]            
            columnsSQL = [column[0] for column in rs.description]
        
            f=rs.fetchall()
            print (columnsSQL)
            #print(f)
            k=np.asarray(f)
    
            # print(f)
            #print(k)
            # k2=columnsSQL+k
            # print(k2)
            sql_data=pd.DataFrame(k,columns=columnsSQL).transpose()
            #C=zip(columnsSQL,sql_data.values)
           #print(C[1])
            sql_data_f=pd.DataFrame(sql_data[sql_data[0].notnull()])
            sqlarray=sql_data.values
            print(sqlarray)
            dict_instr = { columnsSQL[i]: sqlarray[i].item()  for i in range(len(columnsSQL))}
            #print (sql_data_f.header)
            return dict_instr
        except: ValueError
dict_instr=getcomposer_instruments(1,1838)
# listinstr=columnsSQL.append(sqlarray.tolist())
# print(listinstr)
# print(sqlarray.tolist())
#print(list(dict_instr))
# print(list(dict_instr.keys()))
# for key, value in dict_instr:
#     if not math.isnan(value):
#         print(key+','+value)
print(dict_instr)
#print(list(dict_instr.keys()) if not math.isnan(sqlarray[i].item()))
#print(list(dict_instr.values()))
#print(getcomposer_instruments(1,1838).iloc[:,0].values)        
#getcomposerperiodinstrument('0','all','all')
#print(getcomposer_types(3202).iloc[:,1].values) 

# print(getcomposer_instruments(1,1838).head())
#print(gettype("sonata"))
#print(getinstrument("string"))
#print(getcomposerperiodinstrument("2","all","all"))
