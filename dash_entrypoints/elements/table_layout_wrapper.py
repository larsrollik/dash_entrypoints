from typing import Callable

import numpy as np
from dash import callback
from dash import html
from dash import Input
from dash import Output
from dash import State
from dash.exceptions import PreventUpdate


def wrap_part_layout_for_callback(
    part_layout_pre: list = None,
    part_layout_post: list = None,
    page_title: str = None,
    callback_state_tuples: list = None,
    callback_output_tuple: list = None,
    callback_fun: Callable = None,
    callback_kwargs: dict = None,
    button_label: str = "Submit",
):
    """

    :param part_layout_pre:
    :param part_layout_post:
    :param page_title:
    :param callback_state_tuples:
    :param callback_output_tuple:
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
        html.Button(button_label, id=button_name, className="me-1"),
        html.Div(id=hidden_div_name, hidden=True),
    ]
    layout_list += part_layout_post

    complete_layout = html.Div(layout_list)

    # Callback: state input
    input_states = [State(state, var) for (state, var) in callback_state_tuples]
    state_source = [state[0] for state in callback_state_tuples]
    state_names = [state[1] for state in callback_state_tuples]

    # Callback: output
    callback_output = Output(hidden_div_name, "children") if callback_output_tuple is None else Output(*callback_output_tuple)

    @callback(
        [callback_output],
        [Input(button_name, "n_clicks")] + input_states,
    )
    def callback_wrapper_fun(n_clicks, *state_args):
        if n_clicks is None:
            raise PreventUpdate

        state_data_tuples = list(zip(state_source, state_names, state_args))
        callback_return_value = callback_fun(state_data_tuples, **callback_kwargs)
        # print("\n\n", "n_clicks", n_clicks)
        # print("state_args", state_args)
        if callback_output_tuple is None:
            return [None]
        else:
            print("Returning output value from layout wrapper...")
            return callback_return_value

    return complete_layout
