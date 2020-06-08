#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:43:28 2018

@author: mhurtgen
"""
import re
import requests
from bs4 import BeautifulSoup

composers=set()
nextpage=list()

#with open('composerlistimslp.txt','w') as f:
#    f.write(webcontent.text)
composer_pattern=re.compile('.*,.*')
next_pattern=re.compile('.*next.*')


def getpattern():
    composer_pattern=re.compile('.*,.*')
    next_pattern=re.compile('.*next.*')
    

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
    i=0
    for li in bs_obj.select('li'):
        i=i+1
        data=li.text
        test=composer_pattern.match(data)
        if (test!=None):
            composers.add(data)

def getperiodstring(period):
    if (period==1):
        period_str="People_from_the_Baroque_era"
    elif (period==2):
        period_str="People_from_the_Classical_era"
    elif (period==3):
        period_str="People_from_the_Romantic_era"
    elif (period==4):
        period_str="People_from_the_Modern_era"
    
    http0="https://imslp.org/index.php?title=Category:"
    http2="&intersect=Composers"
    http=http0+period_str+http2    
    
    return http


def getcomposersofperiod(period):
    """modify next read"""
#https://imslp.org/index.php?title=Category:People_from_the_Baroque_era&intersect=Composers
    
    url=getperiodstring(period)
    
    webcontent=requests.get(url)
    
    bs_obj = BeautifulSoup(webcontent.text,"html.parser")
    #all_pages = bs_obj.find_all("a")
    while True:
        #extract href next
        try:
            getcomposers(bs_obj)
            href=gethrefnext(bs_obj)
            #print(href)
            if (href!=None):
                nextpage.add(href)
               
                url1=url+href
                newpage=requests.get(url1)
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


for el in composers:
    print(el)
#links = set()
#
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
