#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:04:20 2020

@author: mhurtgen
"""

import pickle as pk
import sqlite3
import pandas as pd

types=['concerto','symphony','sonata','menuet','toccata','fuga','prelude',
           'lied','oratorio','cantata','mass','opera','waltz'
           'trio','quartet','quintet','sextet','septuor','octuor','ländler','song','variation']
instruments=['piano','violin','flute','clarinet','oboe','trumpet',
             'horn','cello','viola','guitar','string','wind']
modes=['major','minor'
       ]


Typestab={'PK_type':range(1,len(types)+1),'type':types}
#
types = pd.DataFrame(Typestab, columns= ['PK_type', 'type'])

with open('composers.pkl','rb') as f:
    composers=pk.load(f)
    

with open('tunes.pkl','rb') as g:
    musiclist=pk.load(g)
    
conn=sqlite3.connect('ISMLPperiodtotal2')
types.to_sql('Types', conn, if_exists='replace', index = False)

composers.to_sql('composers', conn, if_exists='replace', index = False)
musiclist.to_sql('works', conn, if_exists='replace', index = False)        
conn.commit()    
conn.close()
