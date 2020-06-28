#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:43:28 2018

@author: mhurtgen
"""
import re
import requests
from bs4 import BeautifulSoup
import sqlite3
import numpy as np
import pandas as pd

works=list()
nextpage=set()


next_pattern=re.compile('.*next.*')


#with open('composerlistimslp.txt','w') as f:
#    f.write(webcontent.text)
conn = sqlite3.connect('ILSMP')

def getdata(conn):
    query="""
    SELECT PK_composer, name, url
    FROM composers
    LIMIT 10
"""

    cursor = conn.execute(query)
    
    columnsSQL = [column[0] for column in cursor.description]
    
    f=cursor.fetchall()
    cursor.close()

    k=np.asarray(f)


    sql_data=pd.DataFrame(k,columns=columnsSQL)
    return sql_data

def getpattern(name):
    workstr='.*('+name+')'
    work_pattern=re.compile(workstr)
    return work_pattern

def getlistsize():
    return len(works)



def gethrefnext(bs_obj):
    for el in bs_obj.select('a'):
        data=el.text
        
        test=next_pattern.match(data)
        if (test!=None):
            href=el['href']
#        else:
#            href=None
    return href
    
def getworks(bs_obj,work_pattern,i,index_composer):
    
    
    for li in bs_obj.select('li'):
        data=li.text
        test=work_pattern.match(data)
        if (test!=None):
            index_work=getlistsize()+1
            works.append([index_work,data,index_composer])
   

def getcomposerurl(txt):
    names=txt.split(',')#.trim()
    
    resultstr="https://imslp.org/wiki/Category:"+names[0].replace(" ","_")+'%2C'+names[1].replace(" ","_")
    return resultstr
    
    
def allworks(url,work_pattern,index_work,index_composer):
    webcontent=requests.get(url)
    bs_obj = BeautifulSoup(webcontent.text,"html.parser")
    while True:
        #extract href next
        try:
            getworks(bs_obj,work_pattern,index_work,index_composer)
            href=gethrefnext(bs_obj)
            #print(href)
            if (href!=None):
                nextpage.add(href)
               
                url='https://imslp.org'+href
                newpage=requests.get(url)
                bs_obj=BeautifulSoup(newpage.text,"html.parser")
            
        except Exception:
            break
    return works

def getallworks():
    data=getdata(conn)
    index_work=1
    
    for index,row in data.iterrows():
        index_composer=row['PK_composer']
        name=row['name']
        url=row['url']
        work_pattern=getpattern(name)    
        works=allworks(url,work_pattern,index_work,index_composer)
        
    return works
    #open webpage

    
    
#    for el in bs_obj.select('a'):
#        data=el.text
#        
#        test=next_pattern.match(data)
#        if (test!=None):
#            href=el['href']
#            nextpage.add((data,href))
#            webcontent=requests.get(href)
#            bs_obj=BeautifulSoup(webcontent.text,"html.parser")
#            
#            
#        else:
#            break



#
#
#for page in all_pages:
#    
#    for li in bs_obj.select('li'):
#        data=li.text
#        test=composer_pattern.match(data)
#        if (test!=None):
#            composers.add(data)

    #links.add(page["href"])

#for next_page in links:
#    pageresponse=requests.get(next_page)
#    bs_obj = BeautifulSoup(pageresponse,"html.parser")
#    for li in bs_obj.select('li'):
#        data=li.text
#        composers.add(data)
#
#with open('composerimlsp.txt','w') as f:
#    for composer in composers:
#        f.write(composer)
