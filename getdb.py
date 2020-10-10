#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:34:08 2020

@author: mhurtgen
"""


import sqlite3
import composersimslp2period2 as cp

def initcursor():
    conn = sqlite3.connect('ILSMP')
    cur=conn.cursor()
    return conn,cur

def init():
    conn,cur=initcursor()
    sql_create_composer_table = """CREATE TABLE IF NOT EXISTS composers (  
                                            PK_composer int,                                     
                                            name text,
                                            period int
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
    
def insertdata(data,period):
    count=0
    for el in data:    
        
        cur.execute('INSERT INTO composers values(?,?,?)',(data[count][0],data[count][1], period))
        count=count+1
        conn.commit()

def main():
    index=0
    for i in range(1,5):
        
        data,k=cp.getcomposersofperiod(i,index)
        insertdata(data,i)
        index=k



