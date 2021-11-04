"""
this is a sort of navigator file, helping the app managing the URLs of the different pages.
Also this file is very standard:
    I recommend to follow the Plotly Dash guidelines for it,
    as we just need to customise the path names to have this working.
"""

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import math

static_image_route = '/static/heart.jpg'
# initialize Dash
external_stylesheets = "assets\\bWLwgP.css"
# external_stylesheets=[external_stylesheets]
app = dash.Dash()

# Dataset Operations
data = pd.read_csv("data\\heart_failure_clinical_records_dataset.csv")
# print(data.head())
total_count = data['DEATH_EVENT'].count()
death_count = data['DEATH_EVENT'].sum()
male_death_count = data[(data['DEATH_EVENT'] == 1) & (data['sex'] == 1)]['sex'].sum()
smokers_death_count = data[(data['DEATH_EVENT'] == 1) & (data['smoking'] == 1)]['smoking'].sum()
anaemia_death_count = data[(data['DEATH_EVENT'] == 1) & (data['anaemia'] == 1)]['anaemia'].sum()
diabetes_death_count = data[(data['DEATH_EVENT'] == 1) & (data['diabetes'] == 1)]['diabetes'].sum()
pressure_death_count = data[(data['DEATH_EVENT'] == 1) & (data['high_blood_pressure'] == 1)][
    'high_blood_pressure'].sum()
print("Count of Deaths = {0}, Deaths between Male = {1}, Deaths between smokers = {2}"
      .format(death_count, male_death_count, smokers_death_count))
print("Blood Pressure Deaths = {0}, Deaths have anaemia = {1}, Deaths have diabetes = {2}"
      .format(pressure_death_count, anaemia_death_count, diabetes_death_count))
max_time = data['time'].max()
min_time = data['time'].min()
times_list = data['time'].unique()
# ========================================================================================
cols = data.drop(["DEATH_EVENT"], axis=1).columns.tolist()
print(cols)

# Figures
fig_age_death = px.histogram(data, x='age', y='DEATH_EVENT', color='sex', title='age - death')
fig_age_death_smoke_diabetes = px.histogram(data, x='age', y='DEATH_EVENT', color='sex', title='age - death',
                                            barmode="group", facet_row="smoking", facet_col="diabetes")
fig_anaemia_death = px.histogram(data, x='anaemia', y='DEATH_EVENT', color='sex', title='anaemia - death')
fig3 = px.histogram(data, x='time', y='DEATH_EVENT', color='sex', title='time - death')

colors = {
    'background': '#68788C',
    'text': '#F2E205'
}
# Application Layout
app.layout = html.Div([
    # html.Title("Dash Final Project"),
    # Header Div Design
    html.Div(className="header", children=[
        html.P("Heart Failure Prediction",
               style={'color': 'white', 'font-size': '40px', 'text-align': 'center'}),
        html.P("clinical features for predicting death events",
               style={'color': 'white', 'font-size': '20px', 'text-align': 'center'})
    ], style={
        #'background-image': 'url("/assets/background.jpg")','background-size': 'cover'
    }),

    # Summary Div Design
    html.Div(className="graphs-summary", children=[
        html.Div(className="summary-1", children=[
            html.H6('Total Deaths', className='my-class', style={'color': 'white'}),
            html.H5(str(math.floor(death_count/total_count*100))+" %", className='my-class', style={'color': 'white'})],
                 style={'margin': 5, 'width': 150, 'border-radius': '15px 50px',
                        'backgroundColor': '#3EB595', 'float': 'left', 'padding': 5}),

        html.Div(className="summary-1", children=[
            html.H6('Male Deaths', className='my-class', style={'color': 'white'}),
            html.H5(str(math.floor(male_death_count/total_count*100))+" %", className='my-class', style={'color': 'white'})],
                 style={'margin': 5, 'width': 150, 'border-radius': '15px 50px',
                        'backgroundColor': '#F2C53D', 'float': 'left', 'padding': 5}),

        html.Div(className="summary-1", children=[
            html.H6('Smokers Deaths', className='my-class', style={'color': 'white'}),
            html.H5(str(math.floor(smokers_death_count/total_count*100))+" %", className='my-class', style={'color': 'white'})],
                 style={'margin': 5, 'width': 150, 'border-radius': '15px 50px',
                        'backgroundColor': '#668C4A', 'float': 'left', 'padding': 5}),
        # html.Div(style={'margin': 5, 'width': 150,'height':96, 'border-radius': '15px 15px',
        #               'background-image': 'url("/assets/heart1.jpg")',
        #              'background-size': 'cover', 'float': 'left', 'padding': 5}),
        html.Div(className="summary-1", children=[
            html.H6('Diabetes Deaths', className='my-class', style={'color': 'white'}),
            html.H5(str(math.floor(diabetes_death_count/total_count*100))+" %", className='my-class', style={'color': 'white'})],
                 style={'margin': 5, 'width': 150, 'border-radius': '50px 15px',
                        'backgroundColor': '#696969', 'float': 'left', 'padding': 5}),

        html.Div(className="summary-1", children=[
            html.H6('Anaemia Deaths', className='my-class', style={'color': 'white'}),
            html.H5(str(math.floor(anaemia_death_count/total_count*100))+" %", className='my-class', style={'color': 'white'})],
                 style={'margin': 5, 'width': 150, 'border-radius': '50px 15px',
                        'backgroundColor': '#A6BF4B', 'float': 'left', 'padding': 5}),

        html.Div(className="summary-1", children=[
            html.H6('Blood Pressure Deaths', className='my-class', style={'color': 'white'}),
            html.H5(str(math.floor(pressure_death_count/total_count*100))+" %", className='my-class', style={'color': 'white'})],
                 style={'margin': 5, 'border-radius': '50px 15px',
                        'backgroundColor': '#2983A6', 'float': 'left', 'padding': 5})

    ], style={'margin': '0 auto', 'width': 'fit-content',
              'height': '100', 'padding': 5, 'text-align': 'center'}),

    # Graphs Div Design
    html.Div(className="graphs-container", children=[
        html.Div(className="graphs", children=[
            html.P('All features vs Death Event', className='my-class', id="my-p-element3",
                   style={'color': 'white', 'fontSize': 16, 'text-align': 'center'}),
            dcc.Dropdown(id='product',
                         options=[{'label': i, 'value': i} for i in cols],
                         multi=False, value='age'),
            dcc.Graph(id='feature-graphic')],
                 style={'margin': 25, 'backgroundColor': 'black',
                        'width': '93vw', 'float': 'left', 'padding': 5}),
        html.Div(className="graphs", children=[
            html.P('Death Event Vs (Smokers & Diabetes) Graph', className='my-class', id="my-p-element2",
                   style={'color': 'white', 'fontSize': 16, 'text-align': 'center'}),
            dcc.Graph(figure=fig_age_death_smoke_diabetes)],
                 style={'margin': 25, 'backgroundColor': 'black',
                        'width': '93vw', 'float': 'left', 'padding': 5}),
        html.Div(className="graphs", children=[
            html.P('Death Event Vs Follow-up period (days) Graph', className='my-class', id="my-p-element4",
                   style={'color': 'white', 'fontSize': 16, 'text-align': 'center'}),
            dcc.Graph(id='time-graph', figure={}),
            dcc.Slider(id='my-slider',
                       min=min_time, max=max_time, value=33,
                       marks={
                           # str(time): str(time) for time in times_list
                           min_time: {'label': str(min_time), 'style': {'color': '#f50'}},
                           max_time: {'label': str(max_time), 'style': {'color': '#77b0b1'}}
                       },
                       step=1, tooltip={"placement": "bottom", "always_visible": True},
                       )],
                 style={'margin': 25, 'backgroundColor': 'black',
                        'width': '93vw', 'float': 'left', 'padding': 5})
    ])
], style={'backgroundColor': '#00A19D',
          # 'background-image': 'url("/assets/background.jpg")','background-size': 'cover',
          'min-height': '290vh'})


@app.callback(
    Output('feature-graphic', 'figure'),
    Output(component_id='time-graph', component_property='figure'),
    Input('product', 'value'),
    Input(component_id='my-slider', component_property='value')
)
def update_graph(input_column, slider_value):
    fig = px.histogram(data, x=input_column, y='DEATH_EVENT', color='sex', title=str(input_column) + ' - death')
    print(data[data['time'] == slider_value])
    time_fig = px.histogram(data[data['time'] == slider_value], x='time', y='DEATH_EVENT', color='sex',
                            title='follow-up period (days) - death')

    return fig, time_fig


# Run Server
app.run_server(debug=True)
'''html.Div(className="graphs", children=[
            html.P('Death Event Vs Age Graph', className='my-class', id="my-p-element1",
                   style={'color': 'white', 'fontSize': 16}),
            dcc.Graph(figure=fig_age_death)],
                 style={'margin': 25, 'backgroundColor': 'black',
                        'width': 600, 'float': 'left', 'padding': 5}),'''

'''html.Img(src='/assets/background.jpg', style={'img': {
           'max-width': '100%', 'max-height': '100%', 'display': 'block'}}),'''
