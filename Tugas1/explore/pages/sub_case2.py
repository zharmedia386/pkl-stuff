import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html, callback, Output, Input, dash_table
from flask import Flask
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from apps import navigation

dash.register_page(
    __name__,
    path="/sub-case-2",
    name="Sub Case 2",
    title="Produksi Kayu Bulat x Nilai Ekspor",
    description="Produksi Kayu Bulat x Nilai Ekspor",
)

PAGE_SIZE = 10

# Read the dataset
data_kayu_bulat = pd.read_csv("../produksi_kayu_bulat.csv")
data_ekspor = pd.read_csv("../ekspor.csv")

############################################################
# Produksi Kayu Bulat Paling Banyak berdasarkan provinsi
############################################################

# Group by provinsi and calculate the sum of the kayu bulat
kayu_bulat_grouped_by_provinsi = (
    data_kayu_bulat.groupby("provinsi")["volume"].sum().reset_index()
)

# Set the desired formatting for the values
pd.options.display.float_format = "{:,.2f}".format

# Sort the values in descending order
kayu_bulat_grouped_by_provinsi_sorted = kayu_bulat_grouped_by_provinsi.sort_values(
    by="volume", ascending=False
)

# Rename the columns
kayu_bulat_grouped_by_provinsi_sorted = kayu_bulat_grouped_by_provinsi_sorted.rename(
    columns={"provinsi": "Provinsi", "volume": "Nilai Produksi"}
)

kbulat_grouped_by_provinsi_sorted = (
    data_kayu_bulat.groupby(["provinsi", "kelompok"])["volume"].sum().reset_index()
)

############################################################
# Produksi Kayu Bulat berdasarkan jenis
############################################################

# Group by jenis and calculate the sum of the area
kayu_bulat_grouped_by_jenis = (
    data_kayu_bulat.groupby("kelompok")["volume"].sum().reset_index()
)

# Set the desired formatting for the values
pd.options.display.float_format = "{:,.2f}".format

# Sort the values in descending order
kayu_bulat_grouped_by_jenis_sorted = kayu_bulat_grouped_by_jenis.sort_values(
    by="volume", ascending=False
)

# Rename the columns
kayu_bulat_grouped_by_jenis_sorted = kayu_bulat_grouped_by_jenis_sorted.rename(
    columns={"kelompok": "Jenis Kayu", "volume": "Nilai Produksi"}
)

############################################################
# Nilai Ekspor berdasarkan provinsi
############################################################

# Group by provinsi and calculate the sum of the ekspor
ekspor_grouped_by_provinsi = (
    data_ekspor.groupby("provinsi")["value usd"].sum().reset_index()
)

# Set the desired formatting for the values
pd.options.display.float_format = "{:,.2f}".format

# Sort the values in descending order
ekspor_grouped_by_provinsi_sorted = ekspor_grouped_by_provinsi.sort_values(
    by="value usd", ascending=False
)

# Rename the columns
ekspor_grouped_by_provinsi_sorted = ekspor_grouped_by_provinsi_sorted.rename(
    columns={"provinsi": "Provinsi", "value usd": "Nilai Ekspor"}
)

############################################################
# Nilai Ekspor berdasarkan jenis produk
############################################################

# Group by jenis produk and calculate the sum of the nilai ekspor
ekspor_grouped_by_jenis = data_ekspor.groupby("produk")["value usd"].sum().reset_index()

# Set the desired formatting for the values
pd.options.display.float_format = "{:,.2f}".format

# Sort the values in descending order
ekspor_grouped_by_jenis_sorted = ekspor_grouped_by_jenis.sort_values(
    by="value usd", ascending=False
)

# Rename the columns
ekspor_grouped_by_jenis_sorted = ekspor_grouped_by_jenis_sorted.rename(
    columns={"produk": "Jenis Produk", "value usd": "Nilai Ekspor"}
)

############################################################
# Perbandingan Provinsi berdasrkan Produksi Kayu Bulat dan Ekspor
############################################################

# Merge the data based on the 'provinsi' column
merged_data = pd.merge(
    kayu_bulat_grouped_by_provinsi,
    ekspor_grouped_by_provinsi,
    on="provinsi",
    how="outer",
)

# Replace NaN values with 0
merged_data["volume"] = merged_data["volume"].fillna(0)
merged_data["value usd"] = merged_data["value usd"].fillna(0)

# Sort the merged dataframe by land area and bahan baku in descending order
merged_data_sorted = merged_data.sort_values(
    by=["volume", "value usd"], ascending=False
)

# Rename the columns
merged_data_sorted = merged_data_sorted.rename(
    columns={
        "provinsi": "Provinsi",
        "volume": "Volume(m3)",
        "value usd": "Nilai Ekspor(USD)",
    }
)

############################################################
# Graph Merge Data: Perbandingan Provinsi berdasrkan Produksi Kayu Bulat dan Ekspor
############################################################

fig = go.Figure()

# Tambahkan trace bar untuk Luas Tanah (Ha)
fig.add_trace(
    go.Bar(
        x=merged_data_sorted["Provinsi"],
        y=merged_data_sorted["Volume(m3)"],
        name="Volume(m3)",
        yaxis="y",
        offset=0,
        width=0.4,
        marker_color="blue",
    )
)

# Tambahkan trace bar untuk Bahan Baku
fig.add_trace(
    go.Bar(
        x=merged_data_sorted["Provinsi"],
        y=merged_data_sorted["Nilai Ekspor(USD)"],
        name="Nilai Ekspor(USD)",
        yaxis="y2",
        offset=0.4,
        width=0.4,
        marker_color="red",
    )
)

# Atur layout
fig.update_layout(
    title="Volume produksi kayu bulat dan nilai ekspor berdasarkan Provinsi",
    xaxis=dict(title="Provinsi"),
    yaxis=dict(title="Volume(m3)", side="left", showgrid=False, tickformat=",.2f"),
    yaxis2=dict(
        title="Nilai Ekspor(USD)",
        side="right",
        overlaying="y",
        showgrid=False,
        tickformat=",.2f",
    ),
    barmode="group",
    legend=dict(x=0.8, y=1),
)

############################################################
# Table Provinsi, Jenis Produk, dan Volume Produksi Kayu Bulat
############################################################

data_tabel = kbulat_grouped_by_provinsi_sorted[["provinsi", "kelompok", "volume"]]

# Dropdown component for selecting rows per page
dropdown_rows = dcc.Dropdown(
    id="dropdown-rows",
    options=[
        {"label": "10", "value": 10},
        {"label": "20", "value": 20},
        {"label": "50", "value": 50},
    ],
    value=10,
    clearable=False,
    style={"width": "100px"},
)

layout = html.Div(
    [
        navigation.navbar,
        html.Div(
            [
                html.H1("Produksi Kayu Bulat x Nilai Ekspor", className="ls-title"),
                ################################################################
                # Produksi Kayu Bulat Berdasarkan Provinsi
                ################################################################
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H5("1. Produksi Kayu Bulat Berdasarkan Provinsi"),
                                html.P(
                                    f"Total Produksi Kayu Bulat: {data_kayu_bulat['volume'].sum()}"
                                ),
                                html.Div(
                                    [html.Label("Rows per Page: "), dropdown_rows]
                                ),
                                html.Div(
                                    id="table-container4",
                                    style={
                                        "display": "none"
                                    },  # Hide the container initially
                                    children=[
                                        dash_table.DataTable(
                                            id="table-pagination4",
                                            columns=[
                                                {"name": i, "id": i}
                                                for i in kayu_bulat_grouped_by_provinsi_sorted.columns
                                            ],
                                            data=kayu_bulat_grouped_by_provinsi_sorted.to_dict(
                                                "records"
                                            ),
                                            page_current=0,
                                            page_size=PAGE_SIZE,
                                            page_action="custom",
                                            style_data={
                                                "whiteSpace": "normal",
                                                "height": "auto",
                                            },
                                            style_cell={"textAlign": "center"},
                                            style_table={"overflowX": "auto"},
                                        )
                                    ],
                                ),
                                html.Div(id="table-pagination-container4"),
                            ],
                            md=6,
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(
                                    figure=px.bar(
                                        kayu_bulat_grouped_by_provinsi_sorted,
                                        x="Provinsi",
                                        y="Nilai Produksi",
                                    )
                                )
                            ],
                            md=6,
                        ),
                    ]
                ),
                ################################################################
                # Produksi Kayu Bulat Berdasarkan Jenis Ka
                ################################################################
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H5(
                                    "2. Produksi Kayu Bulat Berdasarkan Jenis Kayu"
                                ),
                                dbc.Table.from_dataframe(
                                    kayu_bulat_grouped_by_jenis_sorted,
                                    striped=True,
                                    bordered=True,
                                    hover=True,
                                ),
                            ],
                            md=6,
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(
                                    figure=px.bar(
                                        kayu_bulat_grouped_by_jenis_sorted,
                                        x="Jenis Kayu",
                                        y="Nilai Produksi",
                                    )
                                ),
                            ],
                            md=6,
                        ),
                    ]
                ),
                ################################################################
                # Nilai Ekspor Berdasarkan Provinsi
                ################################################################
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H5("3. Nilai Ekspor Berdasarkan Provinsi"),
                                html.P(
                                    f"Total Nilai Ekspor: {data_ekspor['value usd'].sum()}"
                                ),
                                html.Div(
                                    [html.Label("Rows per Page: "), dropdown_rows]
                                ),
                                html.Div(
                                    id="table-container5",
                                    style={
                                        "display": "none"
                                    },  # Hide the container initially
                                    children=[
                                        dash_table.DataTable(
                                            id="table-pagination5",
                                            columns=[
                                                {"name": i, "id": i}
                                                for i in ekspor_grouped_by_provinsi_sorted.columns
                                            ],
                                            data=ekspor_grouped_by_provinsi_sorted.to_dict(
                                                "records"
                                            ),
                                            page_current=0,
                                            page_size=PAGE_SIZE,
                                            page_action="custom",
                                            style_data={
                                                "whiteSpace": "normal",
                                                "height": "auto",
                                            },
                                            style_cell={"textAlign": "center"},
                                            style_table={"overflowX": "auto"},
                                        )
                                    ],
                                ),
                                html.Div(id="table-pagination-container5"),
                            ],
                            md=6,
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(
                                    figure=px.bar(
                                        ekspor_grouped_by_provinsi_sorted,
                                        x="Provinsi",
                                        y="Nilai Ekspor",
                                    )
                                )
                            ],
                            md=6,
                        ),
                    ]
                ),
                ################################################################
                # Nilai Ekspor Berdasarkan Jenis Produk
                ################################################################
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H5("4. Nilai Ekspor Berdasarkan Jenis Produk"),
                                dbc.Table.from_dataframe(
                                    ekspor_grouped_by_jenis_sorted,
                                    striped=True,
                                    bordered=True,
                                    hover=True,
                                ),
                            ],
                            md=6,
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(
                                    figure=px.bar(
                                        ekspor_grouped_by_jenis_sorted,
                                        x="Jenis Produk",
                                        y="Nilai Ekspor",
                                    )
                                ),
                            ],
                            md=6,
                        ),
                    ]
                ),
                ################################################################
                # Perbandingan Provinsi berdasarkan Nilai Produksi Kayu Bulat dan Ekspor
                ################################################################
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H5(
                                    "5. Perbandingan Provinsi berdasarkan Nilai Produksi Kayu Bulat dan Ekspor"
                                ),
                                html.Div(
                                    [html.Label("Rows per Page: "), dropdown_rows]
                                ),
                                html.Div(
                                    id="table-container6",
                                    style={
                                        "display": "none"
                                    },  # Hide the container initially
                                    children=[
                                        dash_table.DataTable(
                                            id="table-pagination6",
                                            columns=[
                                                {"name": i, "id": i}
                                                for i in merged_data_sorted.columns
                                            ],
                                            data=merged_data_sorted.to_dict("records"),
                                            page_current=0,
                                            page_size=PAGE_SIZE,
                                            page_action="custom",
                                            style_data={
                                                "whiteSpace": "normal",
                                                "height": "auto",
                                            },
                                            style_cell={"textAlign": "center"},
                                            style_table={"overflowX": "auto"},
                                        )
                                    ],
                                ),
                                html.Div(id="table-pagination-container6"),
                            ],
                            md=6,
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(
                                    figure=px.bar(
                                        merged_data_sorted,
                                        x="Provinsi",
                                        y="Volume(m3)",
                                        color="Nilai Ekspor(USD)",
                                    )
                                ),
                            ],
                            md=6,
                        ),
                    ]
                ),
                ################################################################
                # Nilai Produksi dan Jenis Kayu Bulat berdasarkan Provinsi
                ################################################################
                dbc.Row(
                    [
                        dbc.Col(
                            [dcc.Graph(id="bar-chart", figure=fig)],
                            md=6,
                        ),
                        dbc.Col(
                            [
                                dcc.Graph(
                                    figure=px.bar(
                                        kbulat_grouped_by_provinsi_sorted,
                                        x="provinsi",
                                        y="volume",
                                        color="kelompok",
                                        title="Nilai Produksi dan Jenis Kayu Bulat berdasarkan Provinsi",
                                    )
                                ),
                            ],
                            md=6,
                        ),
                    ]
                ),
                ################################################################
                # Pemetaan Jenis Produksi dan Nilai Produksi Kayu Bulat Berdasarkan Provinsi
                ################################################################
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H5(
                                    "6. Pemetaan Jenis Produksi dan Nilai Produksi Kayu Bulat Berdasarkan Provinsi",
                                    style={"margin-top": "30px"},
                                ),
                                dcc.Graph(
                                    figure=go.Figure(
                                        data=[
                                            go.Table(
                                                header=dict(
                                                    values=[
                                                        f"<b>{col}</b>"
                                                        for col in data_tabel.columns
                                                    ],
                                                    fill_color="grey",
                                                    align="center",
                                                    font=dict(color="white", size=12),
                                                ),
                                                cells=dict(
                                                    values=[
                                                        data_tabel.provinsi,
                                                        data_tabel.kelompok,
                                                        data_tabel.volume,
                                                    ],
                                                    fill_color="lavender",
                                                    align="left",
                                                    font=dict(color="black", size=12),
                                                ),
                                            )
                                        ]
                                    )
                                ),
                            ],
                            md=12,
                            style={"padding": "0px"},
                        )
                    ]
                ),
                ################################################################
                # Conclusion
                ################################################################
                # dbc.Row(
                #     [
                #         dbc.Col(
                #             dbc.Card(
                #                 dbc.CardBody(
                #                     [
                #                         html.H4(
                #                             "Kesimpulan", className="card-subtitle"
                #                         ),
                #                         html.P(
                #                             "Some quick example text to build on the card title and make Some quick example text to build on the card title and make Some quick example text to build on the card title and make Some quick example text to build on the card title and make Some quick example text to build on the card title and make Some quick example text to build on the card title and make Some quick example text to build on the card title and make Some quick example text to build on the card title and make Some quick example text to build on the card title and make ",
                #                             className="card-text",
                #                         ),
                #                     ],
                #                     className="mb-12",
                #                 ),
                #             ),
                #         ),
                #     ],
                #     style={"margin-top": "40px"},
                # ),
            ],
            className="frame",
        ),
    ]
)


@callback(
    Output("table-pagination-container4", "children"),
    Input("table-pagination4", "page_current"),
    Input("table-pagination4", "page_size"),
)
def update_table_pagination(page_current, page_size):
    start_index = page_current * page_size
    end_index = (page_current + 1) * page_size

    table_data = kayu_bulat_grouped_by_provinsi_sorted.iloc[
        start_index:end_index
    ].to_dict("records")

    return dash_table.DataTable(
        id="table-pagination4",
        columns=[
            {"name": i, "id": i} for i in kayu_bulat_grouped_by_provinsi_sorted.columns
        ],
        data=table_data,
        page_current=page_current,
        page_size=page_size,
        page_action="custom",
        style_data={"whiteSpace": "normal", "height": "auto"},
        style_cell={"textAlign": "center"},
        style_table={"overflowX": "auto"},
    )


@callback(
    Output("table-pagination-container5", "children"),
    Input("table-pagination5", "page_current"),
    Input("table-pagination5", "page_size"),
)
def update_table_pagination(page_current, page_size):
    start_index = page_current * page_size
    end_index = (page_current + 1) * page_size

    table_data = ekspor_grouped_by_provinsi_sorted.iloc[start_index:end_index].to_dict(
        "records"
    )

    return dash_table.DataTable(
        id="table-pagination5",
        columns=[
            {"name": i, "id": i} for i in ekspor_grouped_by_provinsi_sorted.columns
        ],
        data=table_data,
        page_current=page_current,
        page_size=page_size,
        page_action="custom",
        style_data={"whiteSpace": "normal", "height": "auto"},
        style_cell={"textAlign": "center"},
        style_table={"overflowX": "auto"},
    )


@callback(
    Output("table-pagination-container6", "children"),
    Input("table-pagination6", "page_current"),
    Input("table-pagination6", "page_size"),
)
def update_table_pagination(page_current, page_size):
    start_index = page_current * page_size
    end_index = (page_current + 1) * page_size

    table_data = merged_data_sorted.iloc[start_index:end_index].to_dict("records")

    return dash_table.DataTable(
        id="table-pagination6",
        columns=[{"name": i, "id": i} for i in merged_data_sorted.columns],
        data=table_data,
        page_current=page_current,
        page_size=page_size,
        page_action="custom",
        style_data={"whiteSpace": "normal", "height": "auto"},
        style_cell={"textAlign": "center"},
        style_table={"overflowX": "auto"},
    )
