import re

class Composition:
    
    def __init__(self,title):
        self.title=title
        self.type=0
        self.tone=''
        self.mode=''
        self.piano=0
        self.violin=0
        self.flute=0
        self.clarinet=0
        self.oboe=0
        self.trumpet=0
        self.horn=0
        self.bassoon=0
        self.cello=0
        self.viola=0
        self.guitar=0
        self.contrabass=0
        self.string=0
        self.wind=0
        self.organ=0
        self.harp=0
        self.saxophone=0
        

    def gettitle(self):
        return self.title

    def switch_instrument(self,data):
        if data=="piano":
            self.piano=1
        if data=="violin":
            self.violin=1
        if data=="flute":
            self.flute=1
        if data=="clarinet":
            self.clarinet=1
        if data=="oboe":
            self.oboe=1
        if data=="trumpet":
            self.trumpet=1
        if data=="horn":
            self.horn=1
        if data=="bassoon":
            self.bassoon=1
        if data=="cello":
            self.cello=1
        if data=="viola":
            self.viola=1
        if data=="guitar":
            self.guitar=1
        if data=="contrabass":
            self.contrabass=1
        if data=="string":
            self.string=1
        if data=="wind":
            self.wind=1
        if data=="organ":
            self.organ=1
        if data=="harp":
            self.harp=1
        if data=="saxophone":
            self.saxophone=1
            
            
    def setinstrument(self):
        """get instruments"""
        
        instruments=['all','piano','violin','flute','clarinet','oboe','trumpet','horn','bassoon', 'cello','viola','guitar','contrabass','string','wind','organ','harp','saxophone']

        lgt=len(instruments)
        #matches=sum(x in w for x in datalist)
        for i in range(0,lgt):
            data=instruments[i]
            if (data in self.title.lower()):
                self.switch_instrument(data)

    def getinstrument(self):
        if self.piano==1:
            print('piano ')
        if self.violin==1:
            print('violin ')            
        if self.flute==1:
            print('flute ')
        if self.clarinet==1:
            print('clarinet ')
        if self.oboe==1:
            print('oboe ')
        if self.trumpet==1:
            print('trumpet ')
        if self.horn==1:
            print('horn ')           
        if self.bassoon==1:
            print('bassoon ')
        if self.cello==1:
            print('cello ')
        if self.viola==1:
            print('viola ')
        if self.guitar==1:
            print('guitar ')
        if self.contrabass==1:
            print('contrabass ')
        if self.string==1:
            print('string ')
        if self.wind==1:
            print('wind ')
        if self.organ==1:
            print('organ')

    def setkey(self):
        mode_pattern=re.compile('.*in [A-G](-(flat|sharp))? major|minor.*')
        mode=''
        tone=''
        test=mode_pattern.search(self.title)
        
    
        if test:
            words=self.title.split()
            lg=len(words)
            for i in range(1,lg):
                if (words[i]=='in'):
                    tone=words[i+1]
                    modetot=words[i+2]
                    lg=len(modetot)
                    if (lg==5):
                        mode=modetot
                    else:
                        mode=modetot[0:lg-1]    
            self.mode=mode
            self.tone=tone

    def gettone(self):
        return self.tone

    def getmode(self):
        return self.mode
    
    def settype(self):
        """get type of tune"""
        
        types=['concerto','symphony','sonata','minuet','toccata','fugue','prelude',
           'lied','oratorio','cantata','mass','opera','waltz',
           'trio','quartet','quintet','sextet','septuor','octuor','ländler','song',
           'variation','romance','other']

        lgt=len(types)
    
        for i in range(0,lgt):
            if (types[i] in self.title.lower()):
                self.type=i+1

    def gettype(self):
        return self.type

    def setinfo(self):
        self.settype()
        self.setkey()
        self.setinstrument()

    def getpiano(self):
        return self.piano

    def getviolin(self):
        return self.violin

    def getflute(self):
        return self.flute

    def getclarinet(self):
        return self.clarinet
    
    def getoboe(self):
        return self.oboe

    def gettrumpet(self):
        return self.trumpet
    
    def gethorn(self):
        return self.horn 

    def getbassoon(self):
        return self.bassoon
    
    def getcello(self):
        return self.cello

    def getviola(self):
        return self.viola

    def getguitar(self):
        return self.guitar

    def getcontrabass(self):
        return self.contrabass

    def getstring(self):
        return self.string

    def getwind(self):
        return self.wind

    def getorgan(self):
        return self.organ

    def getharp(self):
        return self.harp

    def getsaxophone(self):
        return self.saxophone

        
