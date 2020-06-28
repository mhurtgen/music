#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:34:08 2020

@author: mhurtgen
"""


import sqlite3
import composersimslp2 as cp
import worksislmp as w
import pickle as p

def initcursor():
    conn = sqlite3.connect('ILSMP')
    cur=conn.cursor()
    return conn,cur

def init():
    conn,cur=initcursor()
    sql_create_composer_table = """CREATE TABLE IF NOT EXISTS composers (  
                                            PK_composer int,                                     
                                            name text,
                                            url text                                           
                                        );"""
    cur.execute(sql_create_composer_table)
    conn.commit()
    
    sql_create_works_table="""CREATE TABLE IF NOT EXISTS works (  
                                            PK_work int,                                     
                                            title text,
                                            FK_composer int
                                        );"""
    
    cur.execute(sql_create_works_table)
    conn.commit()
    
def insertdata(data):
    conn,cur=initcursor()
    count=0
    for el in data:    
        
        cur.execute('INSERT INTO composers values(?,?,?)',(data[count][0],data[count][1],data[count][2]))
        count=count+1
        conn.commit()

def insertwork(data):
    conn,cur=initcursor()
    count=0
    for el in data:    
        
        cur.execute('INSERT INTO works values(?,?,?)',(data[count][0],data[count][1],data[count][2]))
        count=count+1
        conn.commit()

def getsqlcomposers():
    conn,cur=initcursor()    
    data=cp.allcomposers()
    insertdata(cur,conn,data)

def getpickleworks():
    data=w.getallworks()
    with open ('works.pkl', 'wb') as f:
        p.dump(data,f)
    
def getsqlworks():    
    conn,cur=initcursor()
    data=w.getallworks()
    insertwork(data)
    
def fillcomposers():
    conn = sqlite3.connect('ILSMP')
    cur=conn.cursor()
    #only for table creation
    init(cur,conn)
    getsqlcomposers(cur,conn)
    cur.close()
    conn.close()
    
def fillworks():
    conn,cur=initcursor()
    #only for table creation
#    init()
    getsqlworks()
    
    cur.close()
    conn.close()
