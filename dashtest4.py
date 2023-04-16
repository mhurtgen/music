#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:29:39 2023

@author: mhurtgen
"""

import getcomposers as gc

from dash import Dash, html,dcc 

from dash.dependencies import Input, Output

import plotly.express as px

#from collections import OrderedDict
#import dash_core_components as dcc


instruments=['all','piano','violin','flute','clarinet','oboe','trumpet',
             'horn','cello','viola','guitar','string','wind']

app = Dash(__name__)


#x=df.iloc[:, 1]
#y=df.iloc[:, 0]
#fig = px.bar(df, x, y, orientation='h',height=400,title='Prolific composers')



def composers():
    df=gc.getcomposerperiodinstrument("0","all")
    x=df.iloc[:, 1]
    y=df.iloc[:, 0]
    fig = px.bar(df, x, y, orientation='h',height=400,title='Prolific composers')
    fig.update_layout(title='Prolific composers - baroque period',
                      xaxis_title='number of tunes',
                      yaxis_title='Composer')
    return fig

app.layout = html.Div([

html.Div([
        dcc.Dropdown(id='dropdown_period',options=[
                                 {'label':'all','value':'0'}                       
                               ,{'label':'baroque','value':'1'}
                              ,{'label':'classical','value':'2'}  
                              ,{'label':'romantic','value':'3'},
                              {'label':'contemporary','value':'4'}],value='0',
    
        ), 
    ],
        style={'width': '90%', 'display': 'inline-block'}
        ),
html.Div([
        dcc.Dropdown(id='dropdown_instrument',options=[
                                 {'label':i,'value':i} for i in instruments],value='all',
    
        ), 
    ],
        style={'width': '90%', 'display': 'inline-block'}
        ),

    html.Div(id='tablecontainer1'),
html.Div(
    dcc.Graph(
        id = 'bar_plot',figure=composers(),
        style={'width':'600px','height':'450px'}
    ),
    style={'display':'inline-block'}
)
],
        style={'width': '41%', 'display': 'inline-block'}
        )
@app.callback(Output(component_id='bar_plot', component_property= 'figure'),
              [Input(component_id='dropdown_period', component_property= 'value')],
              [Input(component_id='dropdown_instrument', component_property= 'value')])
def graph_update(dropdown_period,dropdown_instrument):
    df = gc.getcomposerperiodinstrument(dropdown_period,dropdown_instrument)
    x=df.iloc[:, 1]
    y=df.iloc[:, 0]
    fig = px.bar(df, x, y, orientation='h',height=400,title='Prolific composers')
    fig.update_layout(title='Prolific composers',
                      xaxis_title='number of tunes',
                      yaxis_title='Composer')
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)                 
#            id='table-dropdown',
#            data=df.to_dict('records'),
#            columns=[
#                    {'id': 'title','name':'title'},
#                    {'id': 'name','name':'name'},
#                    {'id': 'tone','name':'tone'},
#                    {'id': 'mode', 'name':'mode','presentation': 'dropdown'}
#                ],
#            editable=True,
#            dropdown=[
#                    'mode', 
#                    {
#                        'options': [
#                            {'label': i, 'value': i}
#                            for i in ['major','minor']
#                                                     
#                        ]
#                             }]
#                    
#            ),
#            html.Div(id='table-dropdown-container')
#])

