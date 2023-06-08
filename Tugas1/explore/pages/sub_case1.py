import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, callback, Output, Input, dash_table
from flask import Flask
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path='/sub-case-1',
                   name='Sub Case 1',
                   title='Kawasan Hutan x Pemenuhan Bahan Baku',
                   description='Kawasan Hutan x Pemenuhan Bahan Baku'
)

PAGE_SIZE = 10

# Read the dataset
data_kawasan_hutan = pd.read_csv("../kawasan_hutan.csv")

############################################################
# Area Kawasan Hutan Paling Luas berdasarkan provinsi
############################################################    

# Group by provinsi and calculate the sum of the area
area_grouped_by_provinsi = data_kawasan_hutan.groupby('provinsi')['area'].sum().reset_index()

# Set the desired formatting for the values
pd.options.display.float_format = '{:,.2f}'.format

# Sort the values in descending order
area_grouped_by_provinsi_sorted = area_grouped_by_provinsi.sort_values(by='area', ascending=False)

# Rename the columns
area_grouped_by_provinsi_sorted = area_grouped_by_provinsi_sorted.rename(columns={'provinsi': 'Provinsi', 'area': 'Luas Tanah (Ha)'})

############################################################
# Area Kawasan Hutan Paling Luas berdasarkan jenis
############################################################   

# Group by jenis and calculate the sum of the area
area_grouped_by_jenis = data_kawasan_hutan.groupby('jenis')['area'].sum().reset_index()

# Set the desired formatting for the values
pd.options.display.float_format = '{:,.2f}'.format

# Sort the values in descending order
area_grouped_by_jenis_sorted = area_grouped_by_jenis.sort_values(by='area', ascending=False)

# Rename the columns
area_grouped_by_jenis_sorted = area_grouped_by_jenis_sorted.rename(columns={'jenis': 'Jenis Hutan', 'area': 'Luas Tanah (Ha)'})

# Dropdown component for selecting rows per page
dropdown_rows = dcc.Dropdown(
    id='dropdown-rows',
    options=[
        {'label': '10', 'value': 10},
        {'label': '20', 'value': 20},
        {'label': '50', 'value': 50}
    ],
    value=10,
    clearable=False,
    style={'width': '100px'}
)

layout = html.Div(
    [
        html.H2('Kawasan Hutan x Pemenuhan Bahan Baku'),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3('Luas Tanah (Ha) Berdasarkan Provinsi'),
                        html.P(f"Total Luas Tanah (Ha): {data_kawasan_hutan['area'].sum()}"),
                        html.Div([
                                html.Label('Rows per Page: '),
                                dropdown_rows
                            ]),
                       html.Div(
                            id='table-container',
                            style={'display': 'none'},  # Hide the container initially
                            children=[
                                dash_table.DataTable(
                                    id='table-pagination',
                                    columns=[{'name': i, 'id': i} for i in area_grouped_by_provinsi_sorted.columns],
                                    data=area_grouped_by_provinsi_sorted.to_dict('records'),
                                    page_current=0,
                                    page_size=PAGE_SIZE,
                                    page_action='custom',
                                    style_data={'whiteSpace': 'normal', 'height': 'auto'},
                                    style_cell={'textAlign': 'center'},
                                    style_table={'overflowX': 'auto'},
                                )
                            ]
                        ),
                        html.Div(id='table-pagination-container')
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        dcc.Graph(
                            figure=px.bar(area_grouped_by_provinsi_sorted, x='Provinsi', y='Luas Tanah (Ha)')
                        )
                    ],
                    md=6,
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3('Luas Tanah (Ha) Berdasarkan Jenis Hutan'),
                        dbc.Table.from_dataframe(area_grouped_by_jenis_sorted, striped=True, bordered=True, hover=True),
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        dcc.Graph(
                            figure=px.bar(area_grouped_by_jenis_sorted, x='Jenis Hutan', y='Luas Tanah (Ha)')
                        ),
                    ],
                    md=6,
                ),
            ]
        ),         
    ]
)
    
@callback(
    Output('table-pagination-container', 'children'),
    Input('table-pagination', 'page_current'),
    Input('table-pagination', 'page_size'),
)
def update_table_pagination(page_current, page_size):
    start_index = page_current * page_size
    end_index = (page_current + 1) * page_size

    table_data = area_grouped_by_provinsi_sorted.iloc[start_index:end_index].to_dict('records')

    return dash_table.DataTable(
        id='table-pagination',
        columns=[{'name': i, 'id': i} for i in area_grouped_by_provinsi_sorted.columns],
        data=table_data,
        page_current=page_current,
        page_size=page_size,
        page_action='custom',
        style_data={'whiteSpace': 'normal', 'height': 'auto'},
        style_cell={'textAlign': 'center'},
        style_table={'overflowX': 'auto'},
    )