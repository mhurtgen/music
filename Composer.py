import Composition
import pandas as pd


class Composer:

    def __init__(self, name):
        self.name=name
        self.compositions=list()
        
    def getname(self):        
        return self.name

    def getcompositions(self):
        return self.compositions

    def printcompositionlist(self):
        for c in self.compositions:
            print(c.gettitle())
        
            
    def addComposition(self,title):
        c=Composition.Composition(title)
        self.compositions.append(c)

    def setinfocompositions(self):
        for c in self.compositions:
            c.setinfo()

    def getinfocompositions(self):
        """set fields of composition objects of composer"""
        
        cinfo=list()
        for c in self.compositions:
            print(c.getorgan())
            
            i=[c.gettitle(), c.gettype(), c.gettone(), c.getmode(), c.getpiano(), c.getviolin(), c.getflute(), c.getclarinet(), c.getoboe(), c.gettrumpet(), c.gethorn(), c.getbassoon(), c.getcello(), c.getviola(), c.getguitar(), c.getcontrabass(), c.getstring(), c.getwind(), c.getorgan(),c.getharp(), c.getsaxophone()]
            cinfo.append(i)
        DF=pd.DataFrame(cinfo)
        

        return DF
    
         
    
