import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, callback, Output, Input, dash_table
from flask import Flask
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Read the dataset
df = pd.read_csv("../PHL-Sankey.csv")
# df = pd.read_csv("Tugas1\PHL-Sankey.csv")

# Membuat dataframe pertama
df1 = df.groupby(['Bahan Baku', 'Kelompok Kayu Bulat'])['Volume(m3)'].count().reset_index()
df1.columns = ['source', 'target', 'value']
df1['source'] = df1['source'].map({'Kayu Tanaman': 'Kayu Tanaman', 'Kayu Alam': 'Kayu Alam', 'Kayu Perkebunan': 'Kayu Tanaman', 'Setengah Jadi': 'Setengah Jadi', 'Limbah': 'Kayu Tanaman'})

# Membuat dataframe kedua
df2 = df.groupby(['Kelompok Kayu Bulat', 'Jenis Kayu Olahan'])['Volume(m3)'].count().reset_index()
df2.columns = ['source', 'target', 'value']
df2['target'] = df2['target'].map({ 'Chipwood' : 'Chipwood', 'Kayu Lapis dan LVL' : 'Chipwood', 'Kayu Gergajian':'Chipwood', 'Panel':'Panel', 'Pulp':'Pulp', 'Blockboard':'Blockboard', 'Veneer': 'Veneer', 'Bare Core':'Bare Core' ,'Wood Pellet':'Wood Pellet' ,'Particle Board':'Particle Board','Kayu Olahan Lainnya':'Kayu Olahan Lainnya','Moulding':'Moulding','Finger Joint Board':'Finger Joint Board' })

# Membuat dataframe ketiga
# df3 = df.groupby(['Jenis Kayu Olahan', 'Produk Ekspor'])['Volume(m3)'].count().reset_index()
# df3.columns = ['source', 'target', 'value']
# df3['target'] = df3['target'].map({'Bangunan Prefarikasi': 'Bangunan Prefarikasi', 'Chipwood' : 'Chipwood', 'Furnitur Kayu' : 'Furnitur Kayu', 'Kerajinan':'Kerajinan', 'Panel':'Panel', 'Pulp':'Pulp', 'Paper':'Paper', 'Veneer': 'Veneer', 'Woodworking':'WoodWorking'})

# 2 dataframe untuk supply demand kayu olah
# Menggabungkan kedua dataframe
links = pd.concat([df1, df2], axis=0)

# Mendapatkan daftar unique source dan target dari dataframe links
unique_source_target = list(pd.unique(links[['source', 'target']].values.ravel('K')))

# Membuat dictionary untuk memetakan nilai source dan target menjadi nilai numerik
mapping_dict = {k: v for v, k in enumerate(unique_source_target)}

links['source'] = links['source'].map(mapping_dict)
links['target'] = links['target'].map(mapping_dict)

# Mengubah dataframe links menjadi dictionary dengan orientasi 'list'
links_dict = links.to_dict(orient='list')
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.8),
      label = unique_source_target,
      color = "blue"
    ),
    link = dict(
      source = links_dict["source"],
      target = links_dict["target"],
      value = links_dict["value"]
  ))])

fig.update_layout(font_size=15,margin=dict(l=0,r=0,b=0,t=30))