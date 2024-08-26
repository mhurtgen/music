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
            print(c)
        
            
    def addComposition(self,title):
        self.compositions.append(title)



         
    
