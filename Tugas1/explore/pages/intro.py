import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from flask import Flask

dash.register_page(__name__,
                   path='/',
                   name='Home Page',
                   title='Home Page',
                   description='Home Page.'
)

layout = html.Div(
    [
        html.H1('Home Page')
    ]
)