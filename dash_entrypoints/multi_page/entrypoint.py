import argparse
import importlib
import socket
from pathlib import Path

import dash
import dash_bootstrap_components as dbc
import dash_labs as dl
from dash import callback
from dash import html
from dash import Input
from dash import Output
from dash import State

from dash_entrypoints.misc import get_local_ip_address

DEFAULT_APP_NAME = "InterfaceEntrypoint"
DEFAULT_VIEWS_MODULE = "dash_entrypoints.views"


def _do_register_module_as_page(app_name=None, layout_file=None, views_imported=None):
    layout_name = layout_file.name.replace(".py", "")
    layout_path = layout_name.replace("__", "/")
    page = importlib.import_module(f"{views_imported.__package__}.{layout_name}")
    if hasattr(page, "layout"):
        dash.register_page(
            module=layout_name,
            title=f"{app_name}: " + layout_path,
            name=layout_name,
            layout=page.layout,
            path="/" + layout_path,
            top_nav=True,
        )


def register_page_layouts(
    app_name=DEFAULT_APP_NAME, views_module=None, register_blank_frontpage=False
):
    """Register the page layouts in the subfolders of the views_module.

    :param app_name:
    :param views_module:
    :param register_blank_frontpage:
    :param kwargs:
    :return:
    """
    views_imported = importlib.import_module(views_module)

    layout_paths = sorted(Path(views_imported.__path__[0]).rglob("*.py"))
    layout_files = [lay for lay in layout_paths if not lay.name.startswith("__")]

    if register_blank_frontpage:
        dash.register_page(
            module="",
            title=app_name,
            name="",
            layout=lambda layout: html.Div(),
            path="/",
            top_nav=True,
        )
    else:
        # Try to find front page in modules __init__
        frontpage_file = [lay for lay in layout_paths if lay.name.startswith("__")][0]
        _do_register_module_as_page(
            app_name=app_name, layout_file=frontpage_file, views_imported=views_imported
        )

    # Register other views
    for layout_file in layout_files:
        _do_register_module_as_page(app_name, layout_file, views_imported)


def get_app(
    app_name=DEFAULT_APP_NAME,
    views_module=None,
):
    """

    :param app_name:
    :param views_module:
    :param kwargs:
    :return:
    """
    app = dash.Dash(
        name=app_name,
        plugins=[dl.plugins.pages],
        external_stylesheets=[dbc.themes.BOOTSTRAP],
    )
    register_page_layouts(
        app_name=app_name,
        views_module=views_module,
    )
    return app


def add_base_layout(app=None, app_name=None, **kwargs):
    """

    :param app:
    :param app_name:
    :param kwargs:
    :return:
    """
    assert hasattr(dash, "page_registry")

    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            # dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                            dbc.Col(dbc.NavbarBrand(app_name, className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href=f"http://{kwargs.get('ip_address')}:{kwargs.get('port')}",
                    style={"textDecoration": "none"},
                ),
                # dbc.DropdownMenu(
                #     [
                #         dbc.DropdownMenuItem(page["name"], href=page["path"])
                #         for page in dash.page_registry.values()
                #         if page["module"] != "pages.not_found_404"
                #     ],
                #     nav=True,
                #     label="main dropdown",
                # ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavLink(
                                str(page["name"]).capitalize().replace("__", "/"),
                                href=page["path"],
                            )
                            for page in dash.page_registry.values()
                            if page["module"] != "pages.not_found_404"
                        ],
                    ),
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ]
        ),
        color="dark",
        dark=True,
    )

    app.layout = dbc.Container(
        [navbar, dl.plugins.page_container],
        fluid=True,
    )

    @callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")],
    )
    def toggle_navbar_collapse(n, is_open):
        if n:
            return not is_open
        return is_open

    return app


def run_entrypoint(
    app_name=DEFAULT_APP_NAME,
    ip_address=get_local_ip_address(),
    views_module=DEFAULT_VIEWS_MODULE,
    port=9050,
    debug=False,
    **kwargs,
):
    """Entrypoint for dash multi-page app wrapper.

    :param app_name:
    :param ip_address:
    :param views_module:
    :param port:
    :param debug:
    :param kwargs:
    :return:
    """
    app = get_app(app_name=app_name, views_module=views_module)
    app = add_base_layout(
        app=app, app_name=app_name, ip_address=ip_address, port=port, **kwargs
    )
    app.run_server(
        host=ip_address,
        port=port,
        debug=debug,
    )


if __name__ == "__main__":
    run_entrypoint()
