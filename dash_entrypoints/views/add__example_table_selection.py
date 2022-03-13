import pandas as pd
from dash import callback
from dash import html
from dash import Input
from dash import Output
from dash import State
from dash.exceptions import PreventUpdate

from dash_entrypoints.elements.table_for_selection import add_table_for_selection


def make_test_subject_ids():
    import string

    az_list = [a for a in string.ascii_uppercase]
    return az_list


def test_selection_callback(df=None, **kwargs):
    print("-- in test callback -- ", kwargs)
    print(df)


def layout():
    az_list = make_test_subject_ids()
    df = pd.DataFrame(az_list, columns=["subject_id"])

    hidden_div_name = "--".join([__name__, "hidden-div"]).replace(".", "")
    button_name = "--".join([__name__, "button-submit"]).replace(".", "")
    table_name = "--".join([__name__, "table-name"]).replace(".", "")

    main_layout = html.Div(
        [
            html.H3(__name__),
            add_table_for_selection(
                df=df,
                table_name=table_name,
                page_size=20,
            ),
            html.Button("Submit!", id=button_name, className="me-1"),
            html.Div(id=hidden_div_name, hidden=True),
        ]
    )

    @callback(
        [Output(hidden_div_name, "children")],
        [
            Input(button_name, "n_clicks"),
            State(table_name, "selected_rows"),
            State(table_name, "data"),
        ],
    )
    def f(n_clicks, selected_rows, data):
        print(n_clicks)
        if selected_rows is None or n_clicks is None:
            raise PreventUpdate

        table_data = pd.DataFrame(data).loc[selected_rows, :]

        print("Selected rows:")
        print(table_data)

        selection_callback_fun = test_selection_callback  # FIXME: move callback wrapper into table function ??
        selection_callback_kwargs = {"test-arg": 0}

        if selection_callback_fun is not None:
            print("Entering callback", selection_callback_fun)
            selection_callback_fun(table_data, **selection_callback_kwargs)

        return [None]

    return main_layout
