import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from flask import Flask
import dash_bootstrap_components as dbc
import dash_auth

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {"hello12": "world"}

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    suppress_callback_exceptions=True,
)
server = app.server

auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

app.layout = html.Div(children=[dash.page_container])


if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run_server(debug=True, host="0.0.0.0", port=8080)
