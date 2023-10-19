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
    t=dash_table.DataTable(
                id='tab',
                data=df_c.to_dict('records')
            )
    
    return t

app = Dash(__name__)

df=composers()

C = list(zip(df.iloc[:,0].values,df.iloc[:,1].values))



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
    
    html.Div(
        id='tab',
            
            style={'width': '600px', 'height': '450px'}
        )
    
],
style={'width': '41%', 'display': 'inline-block'}
)
    
@app.callback(Output(component_id='tab', component_property= 'children'),
                 [Input(component_id='dropdown_composer', component_property= 'value')])
def table_update(dropdown_composer):
    df_c=gc.getcomposer_types(dropdown_composer)
    t=dash_table.DataTable(data=df_c.to_dict('records'))
    return t


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
