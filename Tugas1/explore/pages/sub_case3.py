# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from apps import navigation

dash.register_page(
    __name__,
    path="/sub-case-3",
    name="Sub Case 3",
    title="Nilai Ekspor, Volume Produksi Kayu Bulat & Olahan, Bahan Baku Per Provinsi",
    description="Nilai Ekspor, Volume Produksi Kayu Bulat & Olahan, Bahan Baku Per Provinsi",
)

# Read data
ekspor_df = pd.read_csv("../ekspor.csv")
produksi_kayu_olahan_df = pd.read_csv("../produksi_kayu_olahan.csv")
produksi_kayu_bulat_df = pd.read_csv("../produksi_kayu_bulat.csv")
pemenuhan_bahan_baku_df = pd.read_csv("../pemenuhan_bahan_baku.csv")

# App layout
layout = html.Div(
    [
        navigation.navbar,
        html.Div(
            [
                # Dataset: Ekspor
                dbc.Row(
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Produk Ekspor per Provinsi",
                                    style={"font-size": "30px", "font-weight": "bold"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        options=ekspor_df[
                                                            "tahun"
                                                        ].unique(),
                                                        id="pick-year-ekspor",
                                                        style={"margin-bottom": "10px"},
                                                        placeholder="Pilih tahun",
                                                    ),
                                                ),
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        options={},
                                                        id="pick-month-ekspor",
                                                        style={"margin-bottom": "10px"},
                                                        placeholder="Pilih bulan",
                                                    ),
                                                ),
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        options={},
                                                        id="pick-province-ekspor",
                                                        style={"margin-bottom": "10px"},
                                                        placeholder="Pilih provinsi",
                                                    ),
                                                ),
                                            ],
                                        ),
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dcc.Graph(
                                                        figure={}, id="graphic-ekspor"
                                                    ),
                                                    md=8,
                                                ),
                                                dbc.Col(
                                                    dbc.Card(
                                                        [
                                                            dbc.CardHeader(
                                                                "Informasi Tambahan"
                                                            ),
                                                            dbc.CardBody(
                                                                [
                                                                    html.Div(
                                                                        children="Total Nilai Ekspor",
                                                                        id="title-for-total-value-ekspor",
                                                                        style={
                                                                            "font-weight": "bold",
                                                                        },
                                                                    ),
                                                                    html.Div(
                                                                        children="...",
                                                                        id="current-total-value-ekspor",
                                                                        style={
                                                                            "font-size": "60px",
                                                                            "margin-bottom": "20px",
                                                                        },
                                                                    ),
                                                                    html.Div(
                                                                        children="Peringkat Provinsi",
                                                                        id="title-for-current-position-ekspor",
                                                                        style={
                                                                            "font-weight": "bold",
                                                                        },
                                                                    ),
                                                                    html.Div(
                                                                        children="...",
                                                                        id="current-position-ekspor",
                                                                        style={
                                                                            "font-size": "60px",
                                                                            "margin-bottom": "20px",
                                                                        },
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    style={"margin-bottom": "15px"},
                ),
                # Dataset: Produksi Kayu Olahan
                dbc.Row(
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Jenis Produk Kayu Olahan per Provinsi",
                                    style={"font-size": "30px", "font-weight": "bold"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        options=produksi_kayu_olahan_df[
                                                            "tahun"
                                                        ].unique(),
                                                        id="pick-year-kayu-olahan",
                                                        style={"margin-bottom": "10px"},
                                                        placeholder="Pilih tahun",
                                                    ),
                                                ),
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        options={},
                                                        id="pick-month-kayu-olahan",
                                                        style={"margin-bottom": "10px"},
                                                        placeholder="Pilih bulan",
                                                    ),
                                                ),
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        options={},
                                                        id="pick-province-kayu-olahan",
                                                        style={"margin-bottom": "10px"},
                                                        placeholder="Pilih provinsi",
                                                    ),
                                                ),
                                            ],
                                        ),
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dcc.Graph(
                                                        figure={},
                                                        id="graphic-kayu-olahan",
                                                    ),
                                                    md=8,
                                                ),
                                                dbc.Col(
                                                    dbc.Card(
                                                        [
                                                            dbc.CardHeader(
                                                                "Informasi Tambahan"
                                                            ),
                                                            dbc.CardBody(
                                                                [
                                                                    html.Div(
                                                                        children="Total Volume Produk",
                                                                        id="title-for-total-value-kayu-olahan",
                                                                        style={
                                                                            "font-weight": "bold",
                                                                        },
                                                                    ),
                                                                    html.Div(
                                                                        children="...",
                                                                        id="current-total-value-kayu-olahan",
                                                                        style={
                                                                            "font-size": "60px",
                                                                            "margin-bottom": "20px",
                                                                        },
                                                                    ),
                                                                    html.Div(
                                                                        children="Peringkat Provinsi",
                                                                        id="title-for-current-position-kayu-olahan",
                                                                        style={
                                                                            "font-weight": "bold",
                                                                        },
                                                                    ),
                                                                    html.Div(
                                                                        children="...",
                                                                        id="current-position-kayu-olahan",
                                                                        style={
                                                                            "font-size": "60px",
                                                                            "margin-bottom": "20px",
                                                                        },
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    style={"margin-bottom": "15px"},
                ),
                # Dataset: Produksi Kayu Bulat
                dbc.Row(
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Jenis Produk Kayu Bulat per Provinsi",
                                    style={"font-size": "30px", "font-weight": "bold"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        options=produksi_kayu_bulat_df[
                                                            "tahun"
                                                        ].unique(),
                                                        id="pick-year-kayu-bulat",
                                                        style={"margin-bottom": "10px"},
                                                        placeholder="Pilih tahun",
                                                    ),
                                                ),
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        options={},
                                                        id="pick-month-kayu-bulat",
                                                        style={"margin-bottom": "10px"},
                                                        placeholder="Pilih bulan",
                                                    ),
                                                ),
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        options={},
                                                        id="pick-province-kayu-bulat",
                                                        style={"margin-bottom": "10px"},
                                                        placeholder="Pilih provinsi",
                                                    ),
                                                ),
                                            ],
                                        ),
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dcc.Graph(
                                                        figure={},
                                                        id="graphic-kayu-bulat",
                                                    ),
                                                    md=8,
                                                ),
                                                dbc.Col(
                                                    dbc.Card(
                                                        [
                                                            dbc.CardHeader(
                                                                "Informasi Tambahan"
                                                            ),
                                                            dbc.CardBody(
                                                                [
                                                                    html.Div(
                                                                        children="Total Volume Produk",
                                                                        id="title-for-total-value-kayu-bulat",
                                                                        style={
                                                                            "font-weight": "bold",
                                                                        },
                                                                    ),
                                                                    html.Div(
                                                                        children="...",
                                                                        id="current-total-value-kayu-bulat",
                                                                        style={
                                                                            "font-size": "60px",
                                                                            "margin-bottom": "20px",
                                                                        },
                                                                    ),
                                                                    html.Div(
                                                                        children="Peringkat Provinsi",
                                                                        id="title-for-current-position-kayu-bulat",
                                                                        style={
                                                                            "font-weight": "bold",
                                                                        },
                                                                    ),
                                                                    html.Div(
                                                                        children="...",
                                                                        id="current-position-kayu-bulat",
                                                                        style={
                                                                            "font-size": "60px",
                                                                            "margin-bottom": "20px",
                                                                        },
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    style={"margin-bottom": "15px"},
                ),
                # Dataset: Pemenuhan Bahan Baku
                dbc.Row(
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    "Jenis Bahan Baku per Provinsi",
                                    style={"font-size": "30px", "font-weight": "bold"},
                                ),
                                dbc.CardBody(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        options=pemenuhan_bahan_baku_df[
                                                            "tahun"
                                                        ].unique(),
                                                        id="pick-year-bahan-baku",
                                                        style={"margin-bottom": "10px"},
                                                        placeholder="Pilih tahun",
                                                    ),
                                                ),
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        options={},
                                                        id="pick-month-bahan-baku",
                                                        style={"margin-bottom": "10px"},
                                                        placeholder="Pilih bulan",
                                                    ),
                                                ),
                                                dbc.Col(
                                                    dcc.Dropdown(
                                                        options={},
                                                        id="pick-province-bahan-baku",
                                                        style={"margin-bottom": "10px"},
                                                        placeholder="Pilih provinsi",
                                                    ),
                                                ),
                                            ],
                                        ),
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    dcc.Graph(
                                                        figure={},
                                                        id="graphic-bahan-baku",
                                                    ),
                                                    md=8,
                                                ),
                                                dbc.Col(
                                                    dbc.Card(
                                                        [
                                                            dbc.CardHeader(
                                                                "Informasi Tambahan"
                                                            ),
                                                            dbc.CardBody(
                                                                [
                                                                    html.Div(
                                                                        children="Total Bahan Baku",
                                                                        id="title-for-total-value-bahan-baku",
                                                                        style={
                                                                            "font-weight": "bold",
                                                                        },
                                                                    ),
                                                                    html.Div(
                                                                        children="...",
                                                                        id="current-total-value-bahan-baku",
                                                                        style={
                                                                            "font-size": "60px",
                                                                            "margin-bottom": "20px",
                                                                        },
                                                                    ),
                                                                    html.Div(
                                                                        children="Peringkat Provinsi",
                                                                        id="title-for-current-position-bahan-baku",
                                                                        style={
                                                                            "font-weight": "bold",
                                                                        },
                                                                    ),
                                                                    html.Div(
                                                                        children="...",
                                                                        id="current-position-bahan-baku",
                                                                        style={
                                                                            "font-size": "60px",
                                                                            "margin-bottom": "20px",
                                                                        },
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    style={"margin-bottom": "15px"},
                ),
            ],
            style={"margin": "25px"},
        ),
    ],
)


######################################################
### EKSPOR ###########################################
######################################################
# Callback untuk dropdown bulan
@callback(
    Output(component_id="pick-month-ekspor", component_property="options"),
    Input(component_id="pick-year-ekspor", component_property="value"),
)
def update_dropdown_month_ekspor(drop_year):
    temp_df = ekspor_df.query(f"tahun == @drop_year")
    temp_df = temp_df.query("`value usd` > 0")

    return temp_df["bulan"].unique()


# Callback untuk dropdown provinsi
@callback(
    Output(component_id="pick-province-ekspor", component_property="options"),
    Input(component_id="pick-year-ekspor", component_property="value"),
    Input(component_id="pick-month-ekspor", component_property="value"),
)
def update_dropdown_province_ekspor(drop_year, drop_month):
    temp_df = ekspor_df.query(f"tahun == @drop_year and bulan == @drop_month")
    temp_df = temp_df.query("`value usd` > 0")

    return temp_df["provinsi"].unique()


# Callback untuk grafik
@callback(
    Output(component_id="graphic-ekspor", component_property="figure"),
    Input(component_id="pick-year-ekspor", component_property="value"),
    Input(component_id="pick-month-ekspor", component_property="value"),
    Input(component_id="pick-province-ekspor", component_property="value"),
)
def update_graph_ekspor(drop_year, drop_month, drop_province):
    temp_df = ekspor_df.query(
        f"tahun == @drop_year and bulan == @drop_month and provinsi == @drop_province"
    )
    temp_df = temp_df.filter(["provinsi", "produk", "value usd"])
    temp_df = temp_df.groupby(["provinsi", "produk"]).sum().reset_index()
    temp_df = temp_df.query("`value usd` > 0")
    temp_df["value usd"] = temp_df["value usd"].astype(int)
    temp_df = temp_df.sort_values(by="value usd", ascending=False)

    # Show the figure using Plotly Express bar chart, also show every product's value usd above the bar
    fig = px.bar(
        temp_df,
        x="produk",
        y="value usd",
        color="provinsi",
        text="value usd",
    )

    # Hide the legend
    fig = fig.update_layout(showlegend=False)

    # Rename the axis
    fig = fig.update_layout(xaxis_title="Produk", yaxis_title="Nilai Ekspor (USD)")

    # Make the plot responsive
    fig = fig.update_layout(autosize=True)

    # Make the plot more neat
    fig = fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))

    # Show percentage of each product's value usd on the bar
    fig = fig.update_traces(texttemplate="%{text:.2s}", textposition="outside")

    return fig


# Callback untuk informasi tambahan
@callback(
    Output(component_id="current-total-value-ekspor", component_property="children"),
    Output(component_id="current-position-ekspor", component_property="children"),
    Input(component_id="pick-year-ekspor", component_property="value"),
    Input(component_id="pick-month-ekspor", component_property="value"),
    Input(component_id="pick-province-ekspor", component_property="value"),
)
def update_divs_ekspor(drop_year, drop_month, drop_province):
    temp_df = ekspor_df.copy()
    temp_df = temp_df.query("`value usd` > 0")
    temp_df = temp_df.query(f"tahun == @drop_year and bulan == @drop_month")
    temp_df = temp_df.filter(["provinsi", "value usd"])
    temp_df = temp_df.groupby(["provinsi"]).sum().reset_index()
    temp_df = temp_df.sort_values(by="value usd", ascending=False)
    temp_df = temp_df.reset_index(drop=True)
    temp_df.index += 1
    temp_df["value usd"] = temp_df["value usd"].astype(int)

    # Find the current total value and current rank
    current_total_value = temp_df.query("provinsi == @drop_province")
    if current_total_value.empty:
        current_total_value = "..."
        current_rank = "..."
    else:
        current_rank = current_total_value.index.values[0]
        current_total_value = current_total_value["value usd"].values[0]
        current_total_value = f"${current_total_value:,}"

    return current_total_value, current_rank


######################################################
### PRODUKSI KAYU OLAHAN #############################
######################################################
# Callback untuk dropdown bulan
@callback(
    Output(component_id="pick-month-kayu-olahan", component_property="options"),
    Input(component_id="pick-year-kayu-olahan", component_property="value"),
)
def update_dropdown_month_kayu_olahan(drop_year):
    temp_df = produksi_kayu_olahan_df.query(f"tahun == @drop_year")
    temp_df = temp_df.query("`volume` > 0")

    return temp_df["bulan"].unique()


# Callback untuk dropdown provinsi
@callback(
    Output(component_id="pick-province-kayu-olahan", component_property="options"),
    Input(component_id="pick-year-kayu-olahan", component_property="value"),
    Input(component_id="pick-month-kayu-olahan", component_property="value"),
)
def update_dropdown_province_kayu_olahan(drop_year, drop_month):
    temp_df = produksi_kayu_olahan_df.query(
        f"tahun == @drop_year and bulan == @drop_month"
    )
    temp_df = temp_df.query("`volume` > 0")

    return temp_df["provinsi"].unique()


# Callback untuk grafik
@callback(
    Output(component_id="graphic-kayu-olahan", component_property="figure"),
    Input(component_id="pick-year-kayu-olahan", component_property="value"),
    Input(component_id="pick-month-kayu-olahan", component_property="value"),
    Input(component_id="pick-province-kayu-olahan", component_property="value"),
)
def update_graph_kayu_olahan(drop_year, drop_month, drop_province):
    temp_df = produksi_kayu_olahan_df.query(
        f"tahun == @drop_year and bulan == @drop_month and provinsi == @drop_province"
    )
    temp_df = temp_df.filter(["provinsi", "jenis", "volume"])
    temp_df = temp_df.groupby(["provinsi", "jenis"]).sum().reset_index()
    temp_df = temp_df.query("`volume` > 0")
    temp_df["volume"] = temp_df["volume"].astype(int)
    temp_df = temp_df.sort_values(by="volume", ascending=False)

    # Show the figure using Plotly Express bar chart, also show every product's value usd above the bar
    fig = px.bar(
        temp_df,
        x="jenis",
        y="volume",
        color="provinsi",
        text="volume",
    )

    # Hide the legend
    fig = fig.update_layout(showlegend=False)

    # Rename the axis
    fig = fig.update_layout(xaxis_title="Jenis", yaxis_title="Volume")

    # Make the plot responsive
    fig = fig.update_layout(autosize=True)

    # Make the plot more neat
    fig = fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))

    # Show percentage of each product's value usd on the bar
    fig = fig.update_traces(texttemplate="%{text:.2s}", textposition="outside")

    return fig


# Callback untuk informasi tambahan
@callback(
    Output(
        component_id="current-total-value-kayu-olahan", component_property="children"
    ),
    Output(component_id="current-position-kayu-olahan", component_property="children"),
    Input(component_id="pick-year-kayu-olahan", component_property="value"),
    Input(component_id="pick-month-kayu-olahan", component_property="value"),
    Input(component_id="pick-province-kayu-olahan", component_property="value"),
)
def update_divs_kayu_olahan(drop_year, drop_month, drop_province):
    temp_df = produksi_kayu_olahan_df.copy()
    temp_df = temp_df.query("`volume` > 0")
    temp_df = temp_df.query(f"tahun == @drop_year and bulan == @drop_month")
    temp_df = temp_df.filter(["provinsi", "volume"])
    temp_df = temp_df.groupby(["provinsi"]).sum().reset_index()
    temp_df = temp_df.sort_values(by="volume", ascending=False)
    temp_df = temp_df.reset_index(drop=True)
    temp_df.index += 1
    temp_df["volume"] = temp_df["volume"].astype(int)

    # Find the current total value and current rank
    current_total_value = temp_df.query("provinsi == @drop_province")
    if current_total_value.empty:
        current_total_value = "..."
        current_rank = "..."
    else:
        current_rank = current_total_value.index.values[0]
        current_total_value = current_total_value["volume"].values[0]
        current_total_value = f"{current_total_value:,}"

    return current_total_value, current_rank


######################################################
### PRODUKSI KAYU BULAT ##############################
######################################################
# Callback untuk dropdown bulan
@callback(
    Output(component_id="pick-month-kayu-bulat", component_property="options"),
    Input(component_id="pick-year-kayu-bulat", component_property="value"),
)
def update_dropdown_month_kayu_bulat(drop_year):
    temp_df = produksi_kayu_bulat_df.query(f"tahun == @drop_year")
    temp_df = temp_df.query("`volume` > 0")

    return temp_df["bulan"].unique()


# Callback untuk dropdown provinsi
@callback(
    Output(component_id="pick-province-kayu-bulat", component_property="options"),
    Input(component_id="pick-year-kayu-bulat", component_property="value"),
    Input(component_id="pick-month-kayu-bulat", component_property="value"),
)
def update_dropdown_province_kayu_bulat(drop_year, drop_month):
    temp_df = produksi_kayu_bulat_df.query(
        f"tahun == @drop_year and bulan == @drop_month"
    )
    temp_df = temp_df.query("`volume` > 0")

    return temp_df["provinsi"].unique()


# Callback untuk grafik
@callback(
    Output(component_id="graphic-kayu-bulat", component_property="figure"),
    Input(component_id="pick-year-kayu-bulat", component_property="value"),
    Input(component_id="pick-month-kayu-bulat", component_property="value"),
    Input(component_id="pick-province-kayu-bulat", component_property="value"),
)
def update_graph_kayu_bulat(drop_year, drop_month, drop_province):
    temp_df = produksi_kayu_bulat_df.query(
        f"tahun == @drop_year and bulan == @drop_month and provinsi == @drop_province"
    )
    temp_df = temp_df.filter(["provinsi", "kelompok", "volume"])
    temp_df = temp_df.groupby(["provinsi", "kelompok"]).sum().reset_index()
    temp_df = temp_df.query("`volume` > 0")
    temp_df["volume"] = temp_df["volume"].astype(int)
    temp_df = temp_df.sort_values(by="volume", ascending=False)

    # Show the figure using Plotly Express bar chart, also show every product's value usd above the bar
    fig = px.bar(
        temp_df,
        x="kelompok",
        y="volume",
        color="provinsi",
        text="volume",
    )

    # Hide the legend
    fig = fig.update_layout(showlegend=False)

    # Rename the axis
    fig = fig.update_layout(xaxis_title="Kelompok", yaxis_title="Volume")

    # Make the plot responsive
    fig = fig.update_layout(autosize=True)

    # Make the plot more neat
    fig = fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))

    # Show percentage of each product's value usd on the bar
    fig = fig.update_traces(texttemplate="%{text:.2s}", textposition="outside")

    return fig


# Callback untuk informasi tambahan
@callback(
    Output(
        component_id="current-total-value-kayu-bulat", component_property="children"
    ),
    Output(component_id="current-position-kayu-bulat", component_property="children"),
    Input(component_id="pick-year-kayu-bulat", component_property="value"),
    Input(component_id="pick-month-kayu-bulat", component_property="value"),
    Input(component_id="pick-province-kayu-bulat", component_property="value"),
)
def update_divs_kayu_bulat(drop_year, drop_month, drop_province):
    temp_df = produksi_kayu_bulat_df.copy()
    temp_df = temp_df.query("`volume` > 0")
    temp_df = temp_df.query(f"tahun == @drop_year and bulan == @drop_month")
    temp_df = temp_df.filter(["provinsi", "volume"])
    temp_df = temp_df.groupby(["provinsi"]).sum().reset_index()
    temp_df = temp_df.sort_values(by="volume", ascending=False)
    temp_df = temp_df.reset_index(drop=True)
    temp_df.index += 1
    temp_df["volume"] = temp_df["volume"].astype(int)

    # Find the current total value and current rank
    current_total_value = temp_df.query("provinsi == @drop_province")
    if current_total_value.empty:
        current_total_value = "..."
        current_rank = "..."
    else:
        current_rank = current_total_value.index.values[0]
        current_total_value = current_total_value["volume"].values[0]
        current_total_value = f"{current_total_value:,}"

    return current_total_value, current_rank


######################################################
### PEMENUHAN BAHAN BAKU #############################
######################################################
# Callback untuk dropdown bulan
@callback(
    Output(component_id="pick-month-bahan-baku", component_property="options"),
    Input(component_id="pick-year-bahan-baku", component_property="value"),
)
def update_dropdown_month_bahan_baku(drop_year):
    temp_df = pemenuhan_bahan_baku_df.query(f"tahun == @drop_year")
    temp_df = temp_df.query("`value` > 0")

    return temp_df["bulan"].unique()


# Callback untuk dropdown provinsi
@callback(
    Output(component_id="pick-province-bahan-baku", component_property="options"),
    Input(component_id="pick-year-bahan-baku", component_property="value"),
    Input(component_id="pick-month-bahan-baku", component_property="value"),
)
def update_dropdown_province_bahan_baku(drop_year, drop_month):
    temp_df = pemenuhan_bahan_baku_df.query(
        f"tahun == @drop_year and bulan == @drop_month"
    )
    temp_df = temp_df.query("`value` > 0")

    return temp_df["provinsi"].unique()


# Callback untuk grafik
@callback(
    Output(component_id="graphic-bahan-baku", component_property="figure"),
    Input(component_id="pick-year-bahan-baku", component_property="value"),
    Input(component_id="pick-month-bahan-baku", component_property="value"),
    Input(component_id="pick-province-bahan-baku", component_property="value"),
)
def update_graph_bahan_baku(drop_year, drop_month, drop_province):
    temp_df = pemenuhan_bahan_baku_df.query(
        f"tahun == @drop_year and bulan == @drop_month and provinsi == @drop_province"
    )
    temp_df = temp_df.filter(["provinsi", "jenis", "value"])
    temp_df = temp_df.groupby(["provinsi", "jenis"]).sum().reset_index()
    temp_df = temp_df.query("`value` > 0")
    temp_df["value"] = temp_df["value"].astype(int)
    temp_df = temp_df.sort_values(by="value", ascending=False)

    # Show the figure using Plotly Express bar chart, also show every product's value usd above the bar
    fig = px.bar(
        temp_df,
        x="jenis",
        y="value",
        color="provinsi",
        text="value",
    )

    # Hide the legend
    fig = fig.update_layout(showlegend=False)

    # Rename the axis
    fig = fig.update_layout(xaxis_title="Jenis", yaxis_title="Value")

    # Make the plot responsive
    fig = fig.update_layout(autosize=True)

    # Make the plot more neat
    fig = fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))

    # Show percentage of each product's value usd on the bar
    fig = fig.update_traces(texttemplate="%{text:.2s}", textposition="outside")

    return fig


# Callback untuk informasi tambahan
@callback(
    Output(
        component_id="current-total-value-bahan-baku", component_property="children"
    ),
    Output(component_id="current-position-bahan-baku", component_property="children"),
    Input(component_id="pick-year-bahan-baku", component_property="value"),
    Input(component_id="pick-month-bahan-baku", component_property="value"),
    Input(component_id="pick-province-bahan-baku", component_property="value"),
)
def update_divs_bahan_baku(drop_year, drop_month, drop_province):
    temp_df = pemenuhan_bahan_baku_df.copy()
    temp_df = temp_df.query("`value` > 0")
    temp_df = temp_df.query(f"tahun == @drop_year and bulan == @drop_month")
    temp_df = temp_df.filter(["provinsi", "value"])
    temp_df = temp_df.groupby(["provinsi"]).sum().reset_index()
    temp_df = temp_df.sort_values(by="value", ascending=False)
    temp_df = temp_df.reset_index(drop=True)
    temp_df.index += 1
    temp_df["value"] = temp_df["value"].astype(int)

    # Find the current total value and current rank
    current_total_value = temp_df.query("provinsi == @drop_province")
    if current_total_value.empty:
        current_total_value = "..."
        current_rank = "..."
    else:
        current_rank = current_total_value.index.values[0]
        current_total_value = current_total_value["value"].values[0]
        current_total_value = f"{current_total_value:,}"

    return current_total_value, current_rank
