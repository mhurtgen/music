#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:29:39 2023

@author: mhurtgen
"""

#import sqlite3
import getcomposers as gc
#import pandas as pd

from dash import Dash, dash_table,html,dcc 
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
#from collections import OrderedDict
#import dash_core_components as dcc

instruments=['all','piano','violin','flute','clarinet','oboe','trumpet','horn',
                 'cello','viola','guitar','contrabass','string','wind','organ']

types=['all','concerto','symphony','sonata','minuet','toccata','fugue','prelude',
           'lied','oratorio','cantata','mass','opera','waltz',
           'trio','quartet','quintet','sextet','septuor','octuor','ländler','song','variation'
           ,'romance','other']


def composers():
    #df=gc.getcomposerperiod2(p)
    df=gc.getcomposers()
#    tab=df.values.to_list()
#    #t=table_update(p)
    
#    t=dash_table.DataTable(
#                id='tab',
#                data=df.to_dict('records')
#            )
    
    return df

def composer_types(c):
    df_c=gc.getcomposer_types(c)
    
    fig=px.pie(df_c,values=df_c.iloc[:,1],names=df_c.iloc[:,0])
    
    return fig

def composer_instruments(t,c):
    df_c=gc.getcomposer_instruments(t,c)
    
    fig=px.pie(df_c,values=df_c.iloc[:,1],names=df_c.iloc[:,0])
    
    return fig

app = Dash(__name__)

df=composers()
C = list(zip(df.iloc[:,0].values,df.iloc[:,1].values))

dft=gc.getcomposer_types('0')
dfi=gc.getcomposer_instruments('0','0')



#lg=len(tab)
# Define the layout

app.layout = html.Div([
        
        html.H4('Composer''s music'),
        dcc.Dropdown(
        id='dropdown_composer',
        options=[
                {'label': e[1], 'value': e[0]} for e in C 
                ],
                value='0',
            ),
            #dbc.Tabs([
            dbc.Tabs(
            [
                dcc.Graph(id="graph1"),
                dcc.Graph(id="graph2")                
            ],
            id="tabs"
            )
#            html.Div(
#                children=[dbc.Tab(
#                id='tab'
#            ),
#              dbc.Tab(
#                id='tab_instr'
#            )
            ])
#    ,
#                dbc.Tab([dash_table.DataTable(
#                id='tab_instr',
#                columns=[{"name": str(i), "id": str(i)} for i in dfi.columns],
#                data=dfi.to_dict('records_instr'))]
#            )
