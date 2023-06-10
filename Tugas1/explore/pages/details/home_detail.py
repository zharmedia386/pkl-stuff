import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, callback, Output, Input, dash_table
from flask import Flask
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Read the dataset
data_kayu_bulat = pd.read_csv("../produksi_kayu_bulat.csv")
data_ekspor = pd.read_csv("../ekspor.csv")

# Group by provinsi and calculate the sum of the kayu bulat
kayu_bulat_grouped_by_provinsi = data_kayu_bulat.groupby('provinsi')['volume'].sum().reset_index()

# Group by provinsi and calculate the sum of the ekspor
ekspor_grouped_by_provinsi = data_ekspor.groupby('provinsi')['value usd'].sum().reset_index()

kbulat_grouped_by_provinsi_sorted = data_kayu_bulat.groupby(['provinsi', 'kelompok'])['volume'].sum().reset_index()

############################################################
# Perbandingan Provinsi berdasrkan Produksi Kayu Bulat dan Ekspor
############################################################  

# Merge the data based on the 'provinsi' column
merged_data = pd.merge(kayu_bulat_grouped_by_provinsi, ekspor_grouped_by_provinsi, on='provinsi', how='outer')

# Replace NaN values with 0
merged_data['volume'] = merged_data['volume'].fillna(0)
merged_data['value usd'] = merged_data['value usd'].fillna(0)

# Sort the merged dataframe by land area and bahan baku in descending order
merged_data_sorted = merged_data.sort_values(by=['volume', 'value usd'], ascending=False)

# Rename the columns
merged_data_sorted = merged_data_sorted.rename(columns={'provinsi': 'Provinsi', 'volume': 'Volume(m3)', 'value usd': 'Nilai Ekspor(USD)'})
