import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, callback, Output, Input, dash_table
from flask import Flask
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

dash.register_page(__name__,
                   path='/sub-case-1',
                   name='Sub Case 1',
                   title='Kawasan Hutan x Pemenuhan Bahan Baku',
                   description='Kawasan Hutan x Pemenuhan Bahan Baku'
)

PAGE_SIZE = 10

# Read the dataset
data_kawasan_hutan = pd.read_csv("../kawasan_hutan.csv")
data_bahan_baku = pd.read_csv("../pemenuhan_bahan_baku.csv")

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

############################################################
# Pemenuhan Bahan Baku Terbanyak berdasarkan provinsi
############################################################  

# Group by provinsi and calculate the sum of the bahan baku
bahan_baku_grouped_by_provinsi = data_bahan_baku.groupby('provinsi')['value'].sum().reset_index()

# Set the desired formatting for the values
pd.options.display.float_format = '{:,.2f}'.format

# Sort the values in descending order
bahan_baku_grouped_by_provinsi_sorted = bahan_baku_grouped_by_provinsi.sort_values(by='value', ascending=False)

# Rename the columns
bahan_baku_grouped_by_provinsi_sorted = bahan_baku_grouped_by_provinsi_sorted.rename(columns={'provinsi': 'Provinsi', 'value': 'Bahan Baku'})

############################################################
# Bahan Baku Paling Banyak berdasarkan jenis kayu
############################################################   

# Group by jenis and calculate the sum of the bahan_baku
bahan_baku_grouped_by_jenis = data_bahan_baku.groupby('jenis')['value'].sum().reset_index()

# Set the desired formatting for the values
pd.options.display.float_format = '{:,.2f}'.format

# Sort the values in descending order
bahan_baku_grouped_by_jenis_sorted = bahan_baku_grouped_by_jenis.sort_values(by='value', ascending=False)

# Rename the columns
bahan_baku_grouped_by_jenis_sorted = bahan_baku_grouped_by_jenis_sorted.rename(columns={'jenis': 'Jenis Kayu', 'value': 'Bahan Baku'})

############################################################
# Perbandingan Provinsi berdasrkan Kawasan Hutan dan Bahan Baku
############################################################  

# Merge the data based on the 'provinsi' column
merged_data = pd.merge(area_grouped_by_provinsi, bahan_baku_grouped_by_provinsi, on='provinsi', how='outer')

# Replace NaN values with 0
merged_data['area'] = merged_data['area'].fillna(0)
merged_data['value'] = merged_data['value'].fillna(0)

# Sort the merged dataframe by land area and bahan baku in descending order
merged_data_sorted = merged_data.sort_values(by=['area', 'value'], ascending=False)

# Rename the columns
merged_data_sorted = merged_data_sorted.rename(columns={'provinsi': 'Provinsi', 'area': 'Luas Tanah (Ha)', 'value': 'Bahan Baku'})

############################################################  
# Graph Merge Data
############################################################  

# Create the Plotly figure
fig = go.Figure()

# Add bar traces for Luas Tanah (Ha)
fig.add_trace(go.Bar(
    x=merged_data_sorted['Provinsi'],
    y=merged_data_sorted['Luas Tanah (Ha)'],
    name='Luas Tanah (Ha)',
    yaxis='y',
    offset=0,
    width=0.4,
    marker_color='blue'
))

# Add bar traces for Bahan Baku
fig.add_trace(go.Bar(
    x=merged_data_sorted['Provinsi'],
    y=merged_data_sorted['Bahan Baku'],
    name='Bahan Baku',
    yaxis='y2',
    offset=0.4,
    width=0.4,
    marker_color='green'
))

# Set layout
fig.update_layout(
    title='Luas Tanah dan Bahan Baku Berdasarkan Provinsi',
    xaxis=dict(title='Provinsi'),
    yaxis=dict(title='Luas Tanah (Ha)', side='left', showgrid=False, tickformat=',.2f'),
    yaxis2=dict(title='Bahan Baku', side='right', overlaying='y', showgrid=False, tickformat=',.2f'),
    barmode='group',
    legend=dict(x=0.8, y=1),
)

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

############################################################  
# Perbandingan Bahan Baku Impor dan Lokal
############################################################  

# Aggregate the "Bahan Baku" for all provinces
total_bahan_baku = merged_data_sorted['Bahan Baku'].sum()
bahan_baku_impor = merged_data_sorted[merged_data_sorted['Provinsi'] == 'Impor Bahan Baku']['Bahan Baku'].values[0]
bahan_baku_lokal = total_bahan_baku - bahan_baku_impor

# Calculate the percentage
percentage_bahan_baku_impor = (bahan_baku_impor / total_bahan_baku) * 100
percentage_bahan_baku_lokal = (bahan_baku_lokal / total_bahan_baku) * 100

# Create a new DataFrame for the comparison
comparison_data = pd.DataFrame({
    'Sumber': ['Bahan Baku Lokal', 'Impor Bahan Baku', 'Total Bahan Baku'],
    'Bahan Baku': [bahan_baku_lokal, bahan_baku_impor, total_bahan_baku],
    'Persentase (%)': [percentage_bahan_baku_lokal, percentage_bahan_baku_impor, 100]
})

############################################################  
# Graph Perbandingan Data
############################################################  

# Create the Plotly figure
fig2 = go.Figure()

# Filter the comparison data for Impor Bahan Baku and Bahan Baku Lokal
filtered_data = comparison_data[:-1]  # Exclude the last row for Total Bahan Baku

# Create a bar trace for Impor Bahan Baku and Bahan Baku Lokal
bar_trace = go.Bar(
    x=filtered_data['Sumber'],
    y=filtered_data['Bahan Baku'],
    text=filtered_data['Bahan Baku'],
    textposition='auto',
    marker_color=['blue', 'green']
)

# Set layout
layout = go.Layout(
    title='Perbandingan Sumber Pemenuhan Bahan Baku',
    xaxis=dict(title='Sumber Bahan Baku'),
    yaxis=dict(title='Bahan Baku'),
)

# Create a figure and add the trace
fig2 = go.Figure(data=[bar_trace], layout=layout)

layout = html.Div(
    [
        html.H2('Kawasan Hutan x Pemenuhan Bahan Baku'),
        ################################################################
        # SUB CASE 1
        ################################################################
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
        ################################################################
        # SUB CASE 2
        ################################################################
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3('Pemenuhan Bahan Baku Berdasarkan Provinsi'),
                        html.P(f"Total Bahan Baku: {data_bahan_baku['value'].sum()}"),
                        html.Div([
                                html.Label('Rows per Page: '),
                                dropdown_rows
                            ]),
                       html.Div(
                            id='table-container2',
                            style={'display': 'none'},  # Hide the container initially
                            children=[
                                dash_table.DataTable(
                                    id='table-pagination2',
                                    columns=[{'name': i, 'id': i} for i in bahan_baku_grouped_by_provinsi_sorted.columns],
                                    data=bahan_baku_grouped_by_provinsi_sorted.to_dict('records'),
                                    page_current=0,
                                    page_size=PAGE_SIZE,
                                    page_action='custom',
                                    style_data={'whiteSpace': 'normal', 'height': 'auto'},
                                    style_cell={'textAlign': 'center'},
                                    style_table={'overflowX': 'auto'},
                                )
                            ]
                        ),
                        html.Div(id='table-pagination-container2')
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        dcc.Graph(
                            figure=px.bar(bahan_baku_grouped_by_provinsi_sorted, x='Provinsi', y='Bahan Baku')
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
                        html.H3('Pemenuhan Bahan Baku Berdasarkan Jenis Kayu'),
                        dbc.Table.from_dataframe(bahan_baku_grouped_by_jenis_sorted, striped=True, bordered=True, hover=True),
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        dcc.Graph(
                            figure=px.bar(bahan_baku_grouped_by_jenis_sorted, x='Jenis Kayu', y='Bahan Baku')
                        ),
                    ],
                    md=6,
                ),
            ]
        ),     
        ################################################################
        # SUB CASE 3
        ################################################################
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3('Perbandingan Provinsi berdasarkan Kawasan Hutan dan Bahan Baku'),
                        html.Div([
                                html.Label('Rows per Page: '),
                                dropdown_rows
                            ]),
                       html.Div(
                            id='table-container3',
                            style={'display': 'none'},  # Hide the container initially
                            children=[
                                dash_table.DataTable(
                                    id='table-pagination3',
                                    columns=[{'name': i, 'id': i} for i in merged_data_sorted.columns],
                                    data=merged_data_sorted.to_dict('records'),
                                    page_current=0,
                                    page_size=PAGE_SIZE,
                                    page_action='custom',
                                    style_data={'whiteSpace': 'normal', 'height': 'auto'},
                                    style_cell={'textAlign': 'center'},
                                    style_table={'overflowX': 'auto'},
                                )
                            ]
                        ),
                        html.Div(id='table-pagination-container3')
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        dcc.Graph(id='bar-chart', figure=fig)
                    ],
                    md=6,
                )
            ]
        ),   
        ################################################################
        # SUB CASE 4
        ################################################################
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H3('Perbandingan Bahan Baku Impor dan Lokal'),
                        html.Div([
                                html.Label('Rows per Page: '),
                                dropdown_rows
                            ]),
                       dbc.Table.from_dataframe(comparison_data, striped=True, bordered=True, hover=True),
                    ],
                    md=6,
                ),
                dbc.Col(
                    [
                        dcc.Graph(id='bar-chart', figure=fig2)
                    ],
                    md=6,
                )
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



@callback(
    Output('table-pagination-container2', 'children'),
    Input('table-pagination2', 'page_current'),
    Input('table-pagination2', 'page_size'),
)
def update_table_pagination2(page_current, page_size):
    start_index = page_current * page_size
    end_index = (page_current + 1) * page_size

    table_data = bahan_baku_grouped_by_provinsi_sorted.iloc[start_index:end_index].to_dict('records')

    return dash_table.DataTable(
        id='table-pagination2',
        columns=[{'name': i, 'id': i} for i in bahan_baku_grouped_by_provinsi_sorted.columns],
        data=table_data,
        page_current=page_current,
        page_size=page_size,
        page_action='custom',
        style_data={'whiteSpace': 'normal', 'height': 'auto'},
        style_cell={'textAlign': 'center'},
        style_table={'overflowX': 'auto'},
    )




@callback(
    Output('table-pagination-container3', 'children'),
    Input('table-pagination3', 'page_current'),
    Input('table-pagination3', 'page_size'),
)
def update_table_pagination3(page_current, page_size):
    start_index = page_current * page_size
    end_index = (page_current + 1) * page_size

    table_data = merged_data_sorted.iloc[start_index:end_index].to_dict('records')

    return dash_table.DataTable(
        id='table-pagination3',
        columns=[{'name': i, 'id': i} for i in merged_data_sorted.columns],
        data=table_data,
        page_current=page_current,
        page_size=page_size,
        page_action='custom',
        style_data={'whiteSpace': 'normal', 'height': 'auto'},
        style_cell={'textAlign': 'center'},
        style_table={'overflowX': 'auto'},
    )