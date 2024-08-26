class ComposerList:
    import Composer, ComposerScraper, re, requests

    composer_pattern=re.compile('.*,.*')
    next_pattern=re.compile('.*next.*')

    def __init__(self):
        self.ComposerList=list()

 

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
            
            
            test=composer_pattern.match(data)
            if (test!=None):
                """create composer using name"""
                comp=Composer(data)
                scraper=ComposerScraper(comp)
                
                """add works to composition field of Composer object""" #TEST
                #scraper.getallworks(comp)

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

    def __repr__(self):
        for c in self:
            print(c.getname())



    
