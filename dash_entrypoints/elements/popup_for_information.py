import dash_bootstrap_components as dbc
from dash import callback
from dash import html
from dash import Input
from dash import Output

from dash_entrypoints.assets import get_standard_component_id


def add_popup_for_information(
    popup_list: list = None, placeholder: str = "PLACEHOLDER"
):
    """

    :param popup_list: example below
    :param placeholder:
    :return:

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

    """
    assert isinstance(popup_list, list) or isinstance(popup_list, tuple)
    return_layout = []
    for popup in popup_list:
        popup_id = get_standard_component_id(__name__, popup.get("name", placeholder))
        close_button_id = get_standard_component_id(
            __name__, "--".join([popup.get("name"), "close"])
        )
        popup.update({"id": popup_id})
        popup_layout = dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle(popup.get("title", placeholder))),
                dbc.ModalBody(popup.get("text"))
                if popup.get("text", None) is not None
                else html.Div(hidden=True),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id=close_button_id, className="ms-auto", n_clicks=0
                    )
                )
                if popup.get("close_button")
                else html.Div(hidden=True),
            ],
            id=popup_id,
            is_open=popup.get("is_open", False),
        )
        return_layout.append(popup_layout)
        if popup.get("close_button", False):

            @callback(
                Output(close_button_id, "is_open"),
                Input(close_button_id, "is_open"),
            )
            def close(is_open):
                return not is_open

    return return_layout, popup_list
