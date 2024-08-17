from bs4 import BeautifulSoup
import requests
import sqlite3
import pandas as pd
import numpy as np
import re

works=list()
next='null'
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

def getlinks(url):
    
    """download html from url"""
    webcontent=requests.get(url)
    """parse downloaded html"""
    bs_obj = BeautifulSoup(webcontent.text,"html.parser")

    #links=bs_obj.findAll('a',attrs={'id':'mw-pages'})
    tag=bs_obj.find(id="mw-pages")
    links = tag.findAll('a')
    
    #next=tag.findAll(lambda tag:'text' in tag.text)
    
    return links

    #return bs_obj

def getlistofworks(links):
    global next
    """get all titles on page"""
    for link in links:
       
        if ('next' not in link.text):
            works.append(link.text)
        else:
            
                next=link['href']
               
           
           
    
    return next
            
def getallworks_page(url):
    """get works on page"""
    links=getlinks(url)
    next=getlistofworks(links)
    
    return next

def getallworks(name):
    works=list()
    """loop over all pages listing works of composer"""
    name='Mozart,_Wolfgang_Amadeus'
    url=geturl(name)
    next=getallworks_page(url)
    next_pre=next
    
    while (next!='null'):
        """get works on page"""
        
        url='https://imslp.org'+next
        next=getallworks_page(url)
        #works.append(works)
        if (next_pre==next):
            break
        next_pre=next
        print(next)
       
        
       
    return 

name='Mozart,_Wolfgang_Amadeus'

#list=getlinks(url
def getallworksallcomposers(conn):
    data=getdata(conn)
    
    
    for index,row in data.iterrows():
        index_composer=row['PK_composer']
        name=row['name']
       
        works=getallworks(name)
        #works,next=getallworks_page(url)
        
    return works
 


#works=getallworkstot(conn)
#print(works)


#print(works)
#getallworks_page(url)
getallworks(name)
#with open('w','testworks.txt') as f:
#    f.write(works)
#print(next)
#print(next['href'])


"""prints titles"""
#print(works)




