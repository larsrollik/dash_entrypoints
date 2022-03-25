from typing import Callable

import dash_bootstrap_components as dbc
import numpy as np
from dash import callback
from dash import html
from dash import Input
from dash import Output
from dash import State
from dash.exceptions import PreventUpdate


def is_list_or_tuple(obj=None):
    return isinstance(obj, tuple) or isinstance(obj, list)


def wrap_part_layout_for_callback(
    part_layout_pre: list = None,
    part_layout_post: list = None,
    page_title: str = None,
    callback_state_tuples: list = None,
    callback_output_tuples: list = None,
    callback_fun: Callable = None,
    callback_kwargs: dict = None,
    button_label: str = "Submit",
):
    """Wrap a part layout for callback

    :param part_layout_pre:
    :param part_layout_post:
    :param page_title:
    :param callback_state_tuples:
    :param callback_output_tuples:
    :param callback_fun:
    :param callback_kwargs:
    :param button_label:
    :return:
    """
    button_name = "--".join(
        [
            __name__,
            page_title,
            "button-submit",
        ]
    ).replace(".", "")
    hidden_div_name = "--".join(
        [
            __name__,
            page_title,
            "hidden-div",
        ]
    ).replace(".", "")

    # Layout
    layout_list = []
    if page_title is not None:
        layout_list.append(html.H3(page_title))

    if not isinstance(part_layout_pre, list):
        part_layout_pre = [part_layout_pre]
    if not isinstance(part_layout_post, list):
        part_layout_post = [part_layout_post]

    layout_list += part_layout_pre
    layout_list += [
        dbc.Button(button_label, id=button_name, className="me-1"),
        html.Div(id=hidden_div_name, hidden=True),
    ]
    layout_list += part_layout_post

    complete_layout = html.Div(layout_list)

    # Callback: state input
    input_states = [State(state, var) for (state, var) in callback_state_tuples]
    state_source = [state[0] for state in callback_state_tuples]
    state_names = [state[1] for state in callback_state_tuples]

    # Callback: output
    if is_list_or_tuple(callback_output_tuples) and isinstance(
        callback_output_tuples[0], str
    ):
        callback_output_tuples = [callback_output_tuples]

    callback_output = (
        [Output(hidden_div_name, "children")]
        if callback_output_tuples is None
        else [Output(*ctuple) for ctuple in callback_output_tuples]
    )

    @callback(
        [callback_output],
        [Input(button_name, "n_clicks")] + input_states,
    )
    def callback_wrapper_fun(n_clicks, *state_args):
        if n_clicks is None:
            raise PreventUpdate

        key_tuples = [(source, name) for source, name in zip(state_source, state_names)]
        state_data_tuples = dict(zip(key_tuples, state_args))
        callback_return_value = callback_fun(state_data_tuples, **callback_kwargs)

        # Ensure correct nesting of output for dash.schema
        # - is list
        if not isinstance(callback_return_value, list) and not isinstance(
            callback_return_value, tuple
        ):
            callback_return_value = [callback_return_value]

        # - is nested list [[return-value]]
        if not isinstance(callback_return_value[0], list) and not isinstance(
            callback_return_value[0], tuple
        ):
            callback_return_value = [callback_return_value]

        return callback_return_value

    return complete_layout
