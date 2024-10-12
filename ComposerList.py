import Composer, ComposerScraper
import re
import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
import pickle

conn = sqlite3.connect('ISMLPperiodtotal2')

class ComposerList:
    

    composer_pattern=re.compile('.*,.*')
    next_pattern=re.compile('.*next.*')
    conn = sqlite3.connect('ISMLPperiodtotal2')
    
    def __init__(self):
        self.ComposerList=list()

    def getlist(self):
        return self.ComposerList
    
    def getsize(self):
        return len(self.ComposerList)

    def getdata(self,conn):
        query="""
        SELECT PK_composer, name
        FROM composers 
        WHERE PK_composer=1302
        """
   
        sql_data=pd.read_sql(query,conn)
    
        return sql_data

    def gethrefnext(self,bs_obj):
        for el in bs_obj.select('a'):
            data=el.text
        
            test=next_pattern.match(data)
            if (test!=None):
                href=el['href']
        return href
    
    def getcomposers(self,bs_obj):
    
        for li in bs_obj.select('li'):
            """index of composer"""
            index_composer=getlistsize()+1
            """name of composer"""
            data=li.text
            print(data)
            
            test=composer_pattern.match(data)
            if (test!=None):
                """create composer using name"""
                comp=Composer(data)
                scraper=ComposerScraper(comp)
                
                """add works to composition field of Composer object""" #TEST
                scraper.getallworks(comp)

                """add composer to self.ComposerList"""
                self.ComposerList.append(comp)

    def getperiodstring(self,period):
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


    def getcomposersofperiod(self,period):
        """modify next read"""

        url=self.getperiodstring(period)
        print(url)
        webcontent=requests.get(url)
        
        bs_obj = BeautifulSoup(webcontent.text,"html.parser")
        
        while True:
        
            try:
                self.getcomposers(bs_obj)
                href=gethrefnext(bs_obj)

                if (href!=None):
                    nextpage.add(href)
               
                url1="https://imslp.org"+href

                newpage=requests.get(url1)
                bs_obj=BeautifulSoup(newpage.text,"html.parser")
            
            except Exception:
                break
            
    def allcomposers(self):
        for period in range(1,5):
            self.getcomposersofperiod(period)

    def printout(self):
        for c in self.ComposerList:
            print(c.getname())

    def getimslp(self):
        data=self.getdata(conn)

        for index,row in data.iterrows():
            index_composer=row['PK_composer']
            name=row['name']

        
            """create composer using name"""
            comp=Composer.Composer(name)
            scraper=ComposerScraper.ComposerScraper(comp)
            #print(index_composer)    
            """add works to composition field of Composer object""" #TEST
            scraper.getallworks(comp)

            """add composer to ComposerList"""
            self.ComposerList.append(comp)

        #works,next=getallworks_page(url)
        
    def export(self,filename):
        with open(filename,'wb') as f:
            pickle.dump(self,f)

    def setinfo(self):
        """set parameters of compositions"""
        for c in self.ComposerList:
            c.setinfocompositions()

    def export_compositions(self):
        """get table of all compositions and index of corresponding composer"""

        compositions=pd.DataFrame()
        """i is composer index"""
        i=0
        for c in self.ComposerList:
            i=i+1
            
            info=c.getinfocompositions()
            
            info.columns=['title','type','tone','mode','piano','violin','flute','clarinet','oboe','trumpet','horn','bassoon','cello','viola','guitar','contrabass','string','wind','organ','harp','saxophone']
            
            info['FK_composer']=i
            
            compositions.append(info)
            
        return compositions

    def export_composers(self):
        """get table of all composers and index"""
        
        composers=pd.DataFrame()
        
        """define composer index i"""
        i=0
        for c in self.ComposerList:
            i=i+1
            info=[i, c.getname()]
            dfinfo= pd.DataFrame(info)
            composers=pd.concat([composers,dfinfo],ignore_index=True)

        return composers



    
