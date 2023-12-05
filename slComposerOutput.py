#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:50:55 2023

@author: mhurtgen
"""

import streamlit as st
import matplotlib.pyplot as plt
import getcomposers as gc
import numpy


instruments=['all','piano','violin','flute','clarinet','oboe','trumpet','horn','bassoon',
                 'cello','viola','guitar','double_base','string','wind','organ']

types=['all','concerto','symphony','sonata','minuet','toccata','fuga','prelude',
           'lied','oratorio','cantata','mass','opera','waltz',
           'trio','quartet','quintet','sextet','septuor','octuor','ländler','song','variation','romance']


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct


df_c=gc.getcomposers()
C = list(zip(df_c.iloc[:,0].values,df_c.iloc[:,1].values))

dict_composers=dict(C)
composer=st.selectbox('composer',
                        options=df_c.iloc[:,0].values,
                        format_func=lambda  x:dict_composers.get(x)
                        )
df_t0=gc.getcomposer_types(composer)
df_t=df_t0.sort_values(df_t0.columns[1],ascending=False)
 
T=zip(df_t.iloc[:,0],df_t.iloc[:,1].values)

fig = plt.figure(figsize=(8,8))
#axes = fig.add_subplot(111)
#axes.set_ylim(0,500)
labels=df_t.iloc[:,0]
plt.pie(df_t.iloc[:,1],labels=labels, autopct='%.2f')#make_autopct(df_t.iloc[:,1]))
#plt.pie(df_t.iloc[:,1],labels=labels, autopct= lambda x: '{:.0f}'.format(x*df_t.iloc[:,1].sum()/100))

#plt.bar(labels,df_t.iloc[:,1],align='center',width=0.8, orientation='horizontal')#,height=1)#df_t.iloc[:,1].values ,height=1, labels=df_t.iloc[:,0])
st.pyplot(fig)


df_typ=gc.gettypes()
T = list(zip(df_typ.iloc[:,0].values,df_typ.iloc[:,1].values))
dict_types=dict(T)

types=st.selectbox(
    'type',
    options=df_typ.iloc[:,0].values,
    format_func=lambda x:dict_types.get(x)
    )

st.write(types)

dict_instr=gc.getcomposer_instruments(types,composer)
#if (types==1):
# I = list(zip(df_instr.iloc[:,0].values,df_typ.iloc[:,1].values))
# dict_types=dict(I)
fig = plt.figure(figsize=(8,8))
#labels=df_instr.iloc[:,0]
labels=list(dict_instr.keys())
plt.pie(list(dict_instr.values()), labels=labels, autopct='%.2f')

st.pyplot(fig)

st.table(dict_instr)

df_ti=gc.getcomposer_details(types,composer)
st.table(df_ti)
# fig2=plt.figure(figsize=(8,8))

# labels2=df_ti.iloc[:,0]
# plt.pie(df_ti.iloc[:,1],labels=labels2, autopct='%.2f')
# st.pyplot(fig2)

#st.write(composer)