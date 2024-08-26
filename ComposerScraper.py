
import requests
from bs4 import BeautifulSoup

next=''
 
class ComposerScraper:

   
    def __init__(self,Composer):
        self.composer=Composer
        
    def geturl(self):
        name2=self.composer.name.replace(' ','_')
        url='https://imslp.org/wiki/Category:'+name2
        return url
   
    def getlistofworks(self,url):
        next=''
        links=list()
        """download html from url"""
        webcontent=requests.get(url)
        """parse downloaded html"""
        bs_obj = BeautifulSoup(webcontent.text,"html.parser")

        tag=bs_obj.find(id="mw-pages")
    
        if tag!=None:
            links = tag.findAll('a')
        
        """get all titles on page"""
        for link in links:
       
            if 'next' not in link.text:# &('previous' not in link.text):
                self.composer.addComposition(link.text)
            else:
                next=link['href']

        return next
    
    def getallworks_page(self,url):
        """get works on page"""

        next=self.getlistofworks(url)
   
        return next

    def getallworks(self,Composer):

        """loop over all pages listing works of composer"""
    
        url=self.geturl()
    
    
        next=''
        next_pre=''
    
        while (next!='null'):
             """get works on page"""
             next=self.getallworks_page(url)
       
             if (next_pre==next):
                  break
             next_pre=next
             url='https://imslp.org'+next

              
        
