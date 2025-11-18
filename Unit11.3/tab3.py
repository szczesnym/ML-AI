from dash import  dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd

def render_tab(df):

    # Preprocessing
    df['weekday'] = df['tran_date'].dt.day_name()

    layout = html.Div([

        html.H2("Analiza kanałów sprzedaży"),

        html.Div([
            html.Label("Wybierz kanał sprzedaży:"),
            dcc.Dropdown(
                id='store-dropdown',
                options=[{'label': x, 'value': x} for x in sorted(df['Store_type'].unique())],
                value=df['Store_type'].unique()[0],
                clearable=False
            )
        ], style={'width': '40%', 'margin-bottom': '20px'}),

        html.Div([
            html.Label("Wybierz daty:"),
            dcc.DatePickerRange(
                id='sales-range',
                min_date_allowed=df['tran_date'].min(),
                max_date_allowed=df['tran_date'].max(),
                start_date=df['tran_date'].min(),
                end_date=df['tran_date'].max()
            )
        ], style={'width': '40%', 'margin-bottom': '20px'}),


        html.H3("Sprzedaż według dni tygodnia"),
        dcc.Graph(id='weekday-sales'),

        html.H3("Profil klientów wybranego kanału sprzedaży"),
        html.Div([
            dcc.Graph(id='customer-basket')
        ], style={'display': 'grid', 'grid-template-columns': '1fr 1fr', 'gap': '20px'})
    ])

    return layout