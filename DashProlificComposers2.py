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
from dash.dependencies import Input, Output
import plotly.express as px
#from collections import OrderedDict
#import dash_core_components as dcc

instruments=['all','piano','violin','flute','clarinet','oboe','trumpet','horn',
                 'cello','viola','guitar','double_base','string','wind','organ']

types=['all','concerto','symphony','sonata','minuet','toccata','fuga','prelude',
           'lied','oratorio','cantata','mass','opera','waltz',
           'trio','quartet','quintet','sextet','septuor','octuor','ländler','song','variation','romance']


def composers(p,i,t):
    #df=gc.getcomposerperiod2(p)
    df=gc.getcomposerperiodinstrument(p,i,t)
    
    x=df.iloc[:, 0]
    y=df.iloc[:, 1]
    
    fig=px.bar(df,x,y)
    
    return fig
    #t=table_update(p)
    
    
app = Dash(__name__)

fig=composers('0','all','all')
# Define the layout

app.layout = html.Div([
    dcc.Dropdown(id='dropdown_period',options=[
                                 {'label':'all','value':'0'}                       
                               ,{'label':'baroque','value':'1'}
                              ,{'label':'classical','value':'2'}  
                              ,{'label':'romantic','value':'3'},
                              {'label':'contemporary','value':'4'}],value='0',
    
        ), 
        
    html.Div([
        dcc.Dropdown(id='dropdown_instrument',options=[
                                 {'label':i,'value':i} for i in instruments],value='all',
    
        ), 
    ]),
    html.Div([
        dcc.Dropdown(id='dropdown_type',options=[
                                 {'label':i,'value':i} for i in types],value='0',
    
        ) 
    ]),
 
    html.Div(
            dcc.Graph(
        id = 'fig',figure=fig,
        style={'width':'600px','height':'450px'}
    ))
        
])
    
@app.callback(Output(component_id='fig', component_property= 'figure'),
              [Input(component_id='dropdown_period', component_property= 'value')],
              [Input(component_id='dropdown_instrument', component_property= 'value')],
              [Input(component_id='dropdown_type', component_property= 'value')])
def table_update(dropdown_period,dropdown_instrument,dropdown_type):
    df=gc.getcomposerperiodinstrument(dropdown_period,dropdown_instrument,dropdown_type)
    x=df.iloc[:, 0]
    y=df.iloc[:, 1]
    fig=px.bar(df,x,y)
    
    return fig

#dash_table.DataTable(data=df.to_dict('records'))
#html.Div([
#    html.Div(
#        dcc.Tab(
#            dash_table.DataTable(
#                id='tab',
#                data=composers()  # Make sure this function returns valid data
#            ),
#            style={'width': '600px', 'height': '450px'}
#        ),
#        style={'display': 'inline-block'}
#    ),
#],
#style={'width': '41%', 'display': 'inline-block'}
#)

#        dcc.Dropdown(id='dropdown_period',options=[
#                                 {'label':'all','value':'0'}                       
#                               ,{'label':'baroque','value':'1'}
#                              ,{'label':'classical','value':'2'}  
#                              ,{'label':'romantic','value':'3'},
#                              {'label':'contemporary','value':'4'}],value='0',
#    
#        ), 
#    ],
#        style={'width': '90%', 'display': 'inline-block'}
#        ),
#        dash_table.DataTable(
#                id='tab',
#                data=composers()  # Make sure this function returns valid data
#            )
#       ]) 
#html.Div(
#        dcc.Tab(
#            dash_table.DataTable(
#                id='tab',
#                data=composers()  # Make sure this function returns valid data
#            ),
#            style={'width': '600px', 'height': '450px'}
#        ),
#        style={'display': 'inline-block'}
#    ),
#],
#style={'width': '41%', 'display': 'inline-block'}
#)

#@app.callback(Output(component_id='tab', component_property= 'table'),
#              [Input(component_id='dropdown_period', component_property= 'value')])
#def table_update(dropdown_period):
#    df=gc.getcomposerperiod2(dropdown_period)
#    t=dash_table.DataTable(data=df.to_dict('records'))
#    return t

if __name__ == "__main__":
    app.run_server(debug=True)
