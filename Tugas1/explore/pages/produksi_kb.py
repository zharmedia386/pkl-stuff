import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from flask import Flask

dash.register_page(__name__,
                   path='/produksi-kayu-bulat',
                   name='Kayu Bulat',
                   title='Kayu Bulat',
                   description='Produksi Kayu Bulat.'
)

# Read the dataset
df = pd.read_csv('../produksi_kayu_bulat.csv')

# Define the order of months
month_order = [
    'Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli',
    'Agustus', 'September', 'Oktober', 'November', 'Desember'
]

# Convert the "bulan" column to ordered categorical
df['bulan'] = pd.Categorical(df['bulan'], categories=month_order, ordered=True)

# Group the data by "tahun" and calculate the total volume
df_grouped_tahun = df.groupby('tahun')['volume'].sum().reset_index()

# Group the data by "kelompok" and calculate the total volume
df_grouped_kelompok = df.groupby('kelompok')['volume'].sum().reset_index()

# Group the data by "bulan" and calculate the total volume
df_grouped_bulan = df.groupby('bulan')['volume'].sum().reset_index()

# Group the data by "provinsi" and calculate the total volume
df_grouped_provinsi = df.groupby('provinsi')['volume'].sum().reset_index()

layout = html.Div(
    [
        html.H1('Produksi Kayu Bulat'),
        html.H2('Total Volume'),
        html.P(f"Total Volume: {df['volume'].sum()}"),
        html.H2('Data Volume per Tahun'),
        dcc.Graph(
            figure=px.bar(df_grouped_tahun, x='tahun', y='volume', title='Data Volume per Tahun')
        ),
        html.H2('Data Volume per Kelompok'),
        dcc.Graph(
            figure=px.bar(df_grouped_kelompok, x='kelompok', y='volume', title='Data Volume per Kelompok')
        ),
        html.H2('Data Volume per Bulan'),
        dcc.Graph(
            figure=px.bar(df_grouped_bulan, x='bulan', y='volume', title='Data Volume per Bulan')
        ),
        html.H2('Data Volume per Provinsi'),
        dcc.Graph(
            figure=px.bar(df_grouped_provinsi, x='provinsi', y='volume', title='Data Volume per Provinsi')
        )
    ]
)