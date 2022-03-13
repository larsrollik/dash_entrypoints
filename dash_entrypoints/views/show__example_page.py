from pathlib import Path

import numpy as np
from dash import callback
from dash import html
from dash import Input
from dash import Output
from dash import State
from dash.exceptions import PreventUpdate

from dash_entrypoints.misc import get_callback_context


def layout():
    """Example page layout. Shows a random number as proof of reload on every browser page refresh."""

    id_hidden_div = (
        "--".join([__name__, "hidden-div"]).replace(".", "-").replace("_", "-")
    )
    id_button = "--".join([__name__, "submit-button"]).replace(".", "")
    layout = html.Div(
        [
            html.H1(f"{__name__}, {np.random.randint(100)}"),
            html.Button("X!", id=id_button),
            html.Div(id=id_hidden_div, hidden=True),
        ]
    )

    @callback(Output(id_hidden_div, "hidden"), Input(id_button, "n_clicks"))
    def x(n_clicks, *args):
        if n_clicks is None:
            raise PreventUpdate

        print("CALLBACK:", {"n_clicks": n_clicks}, get_callback_context())
        return [True]

    return layout
