#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:43:28 2018

@author: mhurtgen
"""
import re
import requests
from bs4 import BeautifulSoup

composers=list()
nextpage=set()





#with open('composerlistimslp.txt','w') as f:
#    f.write(webcontent.text)
composer_pattern=re.compile('.*,.*')
next_pattern=re.compile('.*next.*')





def getpattern():
    composer_pattern=re.compile('.*,.*')
    next_pattern=re.compile('.*next.*')
    
def getlistsize():
    return len(composers)

def gethrefnext(bs_obj):
    for el in bs_obj.select('a'):
        data=el.text
        
        test=next_pattern.match(data)
        if (test!=None):
            href=el['href']
#        else:
#            href=None
    return href
    
def getcomposers(bs_obj):
    
    i=1
    for li in bs_obj.select('li'):
        data=li.text
        test=composer_pattern.match(data)
        if (test!=None):
            worksurl=getcomposerurl(data)
            index_composer=getlistsize()+1
            composers.append([index_composer,data,worksurl])
            i=i+1
    #return composers

def getcomposerurl(txt):
    names=txt.split(',')#.trim()
    
    resultstr="https://imslp.org/wiki/Category:"+names[0].replace(" ","_")+'%2C'+names[1].replace(" ","_")
    return resultstr
    
    
def allcomposers():
    webcontent=requests.get('https://imslp.org/wiki/Category:Composers')
    bs_obj = BeautifulSoup(webcontent.text,"html.parser")
    while True:
        #extract href next
        try:
            getcomposers(bs_obj)
            href=gethrefnext(bs_obj)
            #print(href)
            if (href!=None):
                nextpage.add(href)
               
                url='https://imslp.org'+href
                newpage=requests.get(url)
                bs_obj=BeautifulSoup(newpage.text,"html.parser")
        except Exception:
            break
    return composers
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
