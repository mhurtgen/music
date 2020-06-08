#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:34:08 2020

@author: mhurtgen
"""


import sqlite3
import composersimslp2period as cp


def init():
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
    
def insertdata(j,data,period):
    for el in data:    
        cur.execute('INSERT INTO composers values(?,?,?)',(j, el, period))
        conn.commit()

def main():
    j=0
    for i in range(1,5):
        j=j+1
        data=cp.getcomposersofperiod(i)
        insertdata(j,data,i)

conn = sqlite3.connect('Works')
cur=conn.cursor()
init()
main()
cur.close()
conn.close()
    
