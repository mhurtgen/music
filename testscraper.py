from bs4 import BeautifulSoup
import requests
import sqlite3
import pandas as pd
import numpy as np
import re

works=list()
allworks_composer=list()
url='https://imslp.org/wiki/Category:Mozart,_Wolfgang_Amadeus'
conn = sqlite3.connect('ISMLPperiodtotal2')
next_pattern=re.compile('.*next.*')

def getdata(conn):
    query="""
    SELECT PK_composer, name
    FROM composers 
    WHERE PK_composer=3202   
"""
   
    sql_data=pd.read_sql(query,conn)
    
    return sql_data

def geturl(name):
    url='https://imslp.org/wiki/Category:'+name
    
    return url

def gethrefnext(bs_obj):
    for el in bs_obj.select('a'):
        data=el.text
        
        test=next_pattern.match(data)
        if (test!=None):
            href=el['href']
#        else:
#            href=None
    return href



def getlinks(url):
    """get url"""
    
   
    """download html from url"""
    webcontent=requests.get(url)
    """parse downloaded html"""
    bs_obj = BeautifulSoup(webcontent.text,"html.parser")

    tag=bs_obj.find(id="mw-pages")
    links = tag.findAll('a')
    
    return links
    #return bs_obj

def getlistofworks(links):
    """get all titles on page"""
    for link in links:
        if ('next' not in link.text):
            works.append(link.text)
        else:
            next=link['href']
    return works, next

def getallworks_page(url):
    """get works on page"""
    links=getlinks(url)

    works,next=getlistofworks(links)
    print(next)
    return works, next

def getallworks(name):
    
    """loop over all pages listing works of composer"""
    name='Mozart,_Wolfgang_Amadeus'
    url=geturl(name)
    
    while True:
        """get works on page"""
        works,next=getallworks_page(url)
        works.append(works)
       
        url='https://imslp.org'+next
        
       
    return works

name='Mozart,_Wolfgang_Amadeus'

#list=getlinks(url
def getallworkstot(conn):
    data=getdata(conn)
    
    
    for index,row in data.iterrows():
        index_composer=row['PK_composer']
        name=row['name']
       
        works=getallworks(name)
        #works,next=getallworks_page(url)
        
    return works
 


#works=getallworkstot(conn)
#print(works)


url=geturl(name)
links=getlinks(url)

works,next=getallworks_page(url)
print(next)
url='https://imslp.org'+next
webcontent=requests.get(url)
print(url)
test=getlinks(url)
print(test)
#print(next)
#print(next['href'])


"""prints titles"""
#print(works)




