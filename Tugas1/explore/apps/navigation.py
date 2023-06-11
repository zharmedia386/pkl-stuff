import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State
import dash

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Img(
                                src=dash.get_asset_url("logo_phl.png"), height="40px"
                            ),
                            dbc.NavbarBrand(
                                "Dashboard Pengelolaan Hutan Lestari (PHL)",
                                className="ms-2",
                            ),
                        ],
                        width={"size": "auto"},
                    )
                ],
                align="center",
                className="g-0",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Nav(
                                [
                                    dbc.NavItem(dbc.NavLink("Home", href="/")),
                                    dbc.NavItem(
                                        dbc.DropdownMenu(
                                            children=[
                                                dbc.DropdownMenuItem(
                                                    "Sub-Case1", href="/sub-case-1"
                                                ),
                                                dbc.DropdownMenuItem(
                                                    "Sub-Case2", href="/sub-case-2"
                                                ),
                                                dbc.DropdownMenuItem(
                                                    "Sub-Case3", href="/sub-case-3"
                                                ),
                                            ],
                                            nav=True,
                                            in_navbar=True,
                                            label="Pages",
                                        )
                                    ),
                                    dbc.NavItem(dbc.NavLink("About", href="/about")),
                                    dbc.NavItem(
                                        dbc.NavLink("Settings", href="/settings")
                                    ),
                                ],
                                navbar=True,
                            )
                        ],
                        width={"size": "auto"},
                    )
                ],
                align="center",
            ),
            dbc.Col(dbc.NavbarToggler(id="navbar-toggler", n_clicks=0)),
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Collapse(
                            dbc.Nav(
                                [
                                    dbc.NavItem(
                                        dbc.NavLink(
                                            html.I(className="bi bi-github"),
                                            href="https://github.com/siddharthajuprod07/algorithms/tree/master/plotly_deep_learning_app",
                                            external_link=True,
                                        )
                                    ),
                                    dbc.NavItem(
                                        dbc.NavLink(
                                            html.I(className="bi bi bi-twitter"),
                                            href="https://twitter.com/splunk_ml",
                                            external_link=True,
                                        )
                                    ),
                                    dbc.NavItem(
                                        dbc.NavLink(
                                            html.I(className="bi bi-youtube"),
                                            href="https://www.youtube.com/channel/UC7J8myLv3tPabjeocxKQQKw",
                                            external_link=True,
                                        )
                                    ),
                                    dbc.Input(type="search", placeholder="Search"),
                                    dbc.Button(
                                        "Search",
                                        color="primary",
                                        className="ms-2",
                                        n_clicks=0,
                                    ),
                                    dbc.NavItem(dbc.NavLink("Logout", href="/logout")),
                                ]
                            ),
                            id="navbar-collapse",
                            is_open=False,
                            navbar=True,
                        )
                    )
                ],
                align="center",
            ),
        ],
        fluid=True,
    ),
    color="primary",
    dark=True,
)


@dash.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
