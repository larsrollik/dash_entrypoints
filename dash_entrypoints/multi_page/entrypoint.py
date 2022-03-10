import argparse
import importlib
import socket
from pathlib import Path

import dash
import dash_bootstrap_components as dbc
import dash_labs as dl

from dash_entrypoints.misc import get_local_ip_address

DEFAULT_APP_NAME = "InterfaceEntrypoint"
DEFAULT_VIEWS_MODULE = "dash_entrypoints.views"


def register_page_layouts(app_name=DEFAULT_APP_NAME, views_module=None):
    """Register the page layouts in the subfolders of the views_module.

    :param app_name:
    :param views_module:
    :param kwargs:
    :return:
    """
    views_imported = importlib.import_module(views_module)

    layout_paths = sorted(Path(views_imported.__path__[0]).rglob("*.py"))
    layout_files = [lay for lay in layout_paths if not lay.name.startswith("__")]

    for layout_file in layout_files:
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

    navbar = dbc.NavbarSimple(
        dbc.Nav(
            [
                dbc.NavLink(
                    f"→ {page['name'].capitalize().replace('_', ' ')}",
                    href=page["path"],
                )
                for page in dash.page_registry.values()
                if page.get("top_nav")
            ],
        ),
        brand=app_name,
        color="primary",
        dark=True,
        className="mb-2",
    )

    app.layout = dbc.Container(
        [navbar, dl.plugins.page_container],
        fluid=True,
    )
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
    app = add_base_layout(app=app, app_name=app_name, **kwargs)
    app.run_server(
        host=ip_address,
        port=port,
        debug=debug,
    )


if __name__ == "__main__":
    run_entrypoint()
