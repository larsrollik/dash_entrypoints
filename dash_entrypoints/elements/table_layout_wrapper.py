import numpy as np
from dash import callback
from dash import html
from dash import Input
from dash import Output
from dash import State
from dash.exceptions import PreventUpdate


def wrap_part_layout_for_callback(
    part_layout=None,
    page_title=None,
    callback_state_tuples=None,
    callback_fun=None,
    callback_kwargs=None,
):
    """"""
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

    layout_list += part_layout
    layout_list += [
        html.Button("Submit!", id=button_name, className="me-1"),
        html.Div(id=hidden_div_name, hidden=True),
    ]

    complete_layout = html.Div(layout_list)

    # Callback
    input_states = [State(state, var) for (state, var) in callback_state_tuples]
    state_source = [state[0] for state in callback_state_tuples]
    state_names = [state[1] for state in callback_state_tuples]

    @callback(
        [Output(hidden_div_name, "children")],
        [Input(button_name, "n_clicks")] + input_states,
    )
    def callback_wrapper_fun(n_clicks, *state_args):
        if n_clicks is None:
            raise PreventUpdate

        state_data_tuples = list(zip(state_source, state_names, state_args))
        callback_fun(state_data_tuples, **callback_kwargs)

        # print("\n\n", "n_clicks", n_clicks)
        # print("state_args", state_args)

        return [None]

    return complete_layout
