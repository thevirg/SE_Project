import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

def generate_dash(bar_fig, bar_desc, stack_fig, stack_desc, line_fig, line_desc, multi_fig, multi_desc, heat_fig,
                  heat_desc, bubble_fig, bubble_desc, dashboard_title):
    app = dash.Dash()

    # Layout
    app.layout = html.Div(children=[
        html.H1(children='Python Dash',
                style={
                    'textAlign': 'center',
                    'color': '#ef3e18'
                }
                ),
        html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
        html.Div(dashboard_title, style={'textAlign': 'center'}),
        html.Br(),
        html.Br(),
        html.Hr(style={'color': '#7FDBFF'}),
        html.H3('Bar chart', style={'color': '#df1e56'}),
        html.Div(bar_desc),
        dcc.Graph(id='graph2',
                  figure=bar_fig),
        html.Hr(style={'color': '#7FDBFF'}),
        html.H3('Stack bar chart', style={'color': '#df1e56'}),
        html.Div(stack_desc),
        dcc.Graph(id='graph3',
                  figure=stack_fig),
        html.Hr(style={'color': '#7FDBFF'}),
        html.H3('Line chart', style={'color': '#df1e56'}),
        html.Div(line_desc),
        dcc.Graph(id='graph4',
                  figure=line_fig),
        html.Hr(style={'color': '#7FDBFF'}),
        html.H3('Multi Line chart', style={'color': '#df1e56'}),
        html.Div(multi_desc),
        dcc.Graph(id='graph5',
                  figure=multi_fig),
        html.Hr(style={'color': '#7FDBFF'}),
        html.H3('Bubble chart', style={'color': '#df1e56'}),
        html.Div(bubble_desc),
        dcc.Graph(id='graph6',
                  figure=bubble_fig),
        html.Hr(style={'color': '#7FDBFF'}),
        html.H3('Heat map', style={'color': '#df1e56'}),
        html.Div(heat_desc),
        dcc.Graph(id='graph7',
                  figure=heat_fig)
    ])


    # @app.callback(Output('graph1', 'figure'),
    #               [Input('select-continent', 'value')])
    # def update_figure(selected_continent):
    #     filtered_df = df1[df1['Continent'] == selected_continent]
    #
    #     filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    #     new_df = filtered_df.groupby(['Country'])['Confirmed'].sum().reset_index()
    #     new_df = new_df.sort_values(by=['Confirmed'], ascending=[False]).head(20)
    #     data_interactive_barchart = [go.Bar(x=new_df['Country'], y=new_df['Confirmed'])]
    #     return {'data': data_interactive_barchart, 'layout': go.Layout(title='Corona Virus Confirmed Cases in '+selected_continent,
    #                                                                    xaxis={'title': 'Country'},
    #                                                                    yaxis={'title': 'Number of confirmed cases'})}
    #

    if __name__ == '__main__':
        app.run_server()
