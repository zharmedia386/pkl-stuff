# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

dash.register_page(
    __name__,
    path="/sub-case-3",
    name="Sub Case 3",
    title="Nilai Ekspor, Volume Produksi Kayu Bulat & Olahan, Bahan Baku Per Provinsi",
    description="Nilai Ekspor, Volume Produksi Kayu Bulat & Olahan, Bahan Baku Per Provinsi",
)
#sdas
# Incorporate data
df = pd.read_csv("../ekspor.csv")

# App layout
layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            "Dashboard Ekspor Indonesia",
                            style={"font-size": "30px", "font-weight": "bold"},
                        ),
                        dbc.CardBody(
                            [
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dcc.Dropdown(
                                                options=df["tahun"].unique(),
                                                id="pick-year",
                                                style={"margin-bottom": "10px"},
                                                placeholder="Pilih tahun",
                                            ),
                                        ),
                                        dbc.Col(
                                            dcc.Dropdown(
                                                options={},
                                                id="pick-month",
                                                style={"margin-bottom": "10px"},
                                                placeholder="Pilih bulan",
                                            ),
                                        ),
                                        dbc.Col(
                                            dcc.Dropdown(
                                                options={},
                                                id="pick-province",
                                                style={"margin-bottom": "10px"},
                                                placeholder="Pilih provinsi",
                                            ),
                                        ),
                                    ],
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dcc.Graph(figure={}, id="graphic"), md=8
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
                                                                id="title-for-total-value",
                                                                style={
                                                                    "font-weight": "bold",
                                                                },
                                                            ),
                                                            html.Div(
                                                                children="...",
                                                                id="current-total-value",
                                                                style={
                                                                    "font-size": "60px",
                                                                    "margin-bottom": "20px",
                                                                },
                                                            ),
                                                            html.Div(
                                                                children="Peringkat Provinsi",
                                                                id="title-for-current-position",
                                                                style={
                                                                    "font-weight": "bold",
                                                                },
                                                            ),
                                                            html.Div(
                                                                children="...",
                                                                id="current-position",
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
        ),
    ],
    style={"margin": "20px 75px 0px"},
)


# Callback untuk dropdown bulan
@callback(
    Output(component_id="pick-month", component_property="options"),
    Input(component_id="pick-year", component_property="value"),
)
def update_dropdown_month(drop_year):
    temp_df = df.query(f"tahun == @drop_year")
    temp_df = temp_df.query("`value usd` > 0")

    return temp_df["bulan"].unique()


# Callback untuk dropdown provinsi
@callback(
    Output(component_id="pick-province", component_property="options"),
    Input(component_id="pick-year", component_property="value"),
    Input(component_id="pick-month", component_property="value"),
)
def update_dropdown_province(drop_year, drop_month):
    temp_df = df.query(f"tahun == @drop_year and bulan == @drop_month")
    temp_df = temp_df.query("`value usd` > 0")

    return temp_df["provinsi"].unique()


# Callback untuk grafik
@callback(
    Output(component_id="graphic", component_property="figure"),
    Input(component_id="pick-year", component_property="value"),
    Input(component_id="pick-month", component_property="value"),
    Input(component_id="pick-province", component_property="value"),
)
def update_graph(drop_year, drop_month, drop_province):
    temp_df = df.query(
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


@callback(
    Output(component_id="current-total-value", component_property="children"),
    Output(component_id="current-position", component_property="children"),
    Input(component_id="pick-year", component_property="value"),
    Input(component_id="pick-month", component_property="value"),
    Input(component_id="pick-province", component_property="value"),
)
def update_divs(drop_year, drop_month, drop_province):
    temp_df = df.copy()
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


# # Run the app
# if __name__ == "__main__":
#     app.run_server(debug=True)
