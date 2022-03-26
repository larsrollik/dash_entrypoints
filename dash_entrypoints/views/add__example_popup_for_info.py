import dash_bootstrap_components as dbc
import pandas as pd
from dash import callback
from dash import html
from dash import Input
from dash import Output
from dash import State
from dash.exceptions import PreventUpdate

from dash_entrypoints.assets import get_standard_component_id
from dash_entrypoints.elements.popup_for_information import add_popup_for_information


def layout():
    popup_list = [
        {
            "name": "success",
            "title": "Successfully inserted new entry.",
            "text": None,
            "close_button": False,
            "is_open": False,
        },
        {"name": "error", "title": "Error during insert", "close_button": True},
    ]
    popup_layout, popup_list = add_popup_for_information(popup_list=popup_list)
    button_id = get_standard_component_id(__name__, "button")
    div_style = {
        "padding": "10px",
        "width": "90%",
    }
    main_layout = html.Div(
        [*popup_layout, dbc.Button("Trigger!", id=button_id)], style=div_style
    )

    @callback(
        Output(popup_list[0]["id"], "is_open"),
        [State(popup_list[0]["id"], "is_open"), Input(button_id, "n_clicks")],
    )
    def trigger(is_open, n_clicks):
        if n_clicks is None:
            raise PreventUpdate

        return not is_open

    return main_layout
