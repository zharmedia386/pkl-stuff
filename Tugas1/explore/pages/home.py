# import dash_html_components as html
from dash import html

# import dash_core_components as dcc
from dash import dcc
from dash.dependencies import Input, Output
from apps import navigation
import dash
import dash_bootstrap_components as dbc
from pages.details import home_detail, sankey
import plotly.express as px

dash.register_page(
    __name__,
    path="/",
    title="Home",
    description="Dashboard Pengelolaan Hutan Lestari (PHL)",
    image="logo2.png",
)

layout = html.Div(
    [
        navigation.navbar,
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Nilai Ekspor ($)"),
                                    html.H1("$ 123,456,789"),
                                    html.P("Per Bulan Januari 2023"),
                                ]
                            ),
                            style={"width": "360px", "margin-right": "50px"},
                            color="secondary",
                            inverse=True,
                        ),
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Volume Kayu Olahan (m3)"),
                                    html.H1("123,456,789 m3"),
                                    html.P("Per Bulan Januari 2023"),
                                ]
                            ),
                            style={"width": "360px", "margin-right": "50px"},
                            color="info",
                            inverse=True,
                        ),
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Volume Kayu Bulat (m3)"),
                                    html.H1("123,456,789 m3"),
                                    html.P("Per Bulan Januari 2023"),
                                ]
                            ),
                            style={"width": "360px", "margin-right": "50px"},
                            color="warning",
                            inverse=True,
                        ),
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H5("Volume Bahan Baku (m3)"),
                                    html.H1("123,456,789 m3"),
                                    html.P("Per Bulan Januari 2023"),
                                ]
                            ),
                            style={"width": "360px", "margin-right": "50px"},
                            color="danger",
                            inverse=True,
                        ),
                    ],
                    className="d-flex justify-content-center",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Col(
                                    [
                                        html.H4(
                                            "Alur Proses Pemetaan Supply and Demand",
                                            style={"margin-top": "60px"},
                                        ),
                                        dcc.Graph(id="bar-chart", figure=sankey.fig),
                                    ],
                                    md=12,
                                ),
                            ]
                        )
                    ],
                    className="d-flex justify-content-center",
                    style={"margin-left": "30px", "margin-right": "30px"},
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H4(
                                    "Nilai Produksi Kayu Bulat dan Ekspor berdasarkan Provinsi",
                                    style={"margin-top": "60px"},
                                ),
                                dcc.Graph(
                                    figure=px.bar(
                                        home_detail.merged_data_sorted,
                                        x="Provinsi",
                                        y="Volume(m3)",
                                        color="Nilai Ekspor(USD)",
                                    ).update_layout(margin=dict(l=0, r=0, b=0, t=30))
                                ),
                            ],
                            md=6,
                        ),
                        dbc.Col(
                            [
                                html.H4(
                                    "Nilai Produksi dan Jenis Kayu Bulat berdasarkan Provinsi",
                                    style={"margin-top": "60px"},
                                ),
                                dcc.Graph(
                                    figure=px.bar(
                                        home_detail.kbulat_grouped_by_provinsi_sorted,
                                        x="provinsi",
                                        y="volume",
                                        color="kelompok",
                                    ).update_layout(margin=dict(l=0, r=0, b=0, t=30)),
                                ),
                            ],
                            md=6,
                        ),
                    ],
                    className="d-flex justify-content-center",
                    style={"margin-left": "30px", "margin-right": "30px"},
                ),
            ],
            className="frame_home",
        ),
    ],
)
