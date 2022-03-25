import pandas as pd
from dash import callback
from dash import html
from dash import Input
from dash import Output
from dash import State
from dash.exceptions import PreventUpdate

from dash_entrypoints.elements.table_for_editing import add_table_with_editable_columns


def make_test_subject_ids():
    import string

    az_list = [a for a in string.ascii_uppercase]
    return az_list


def test_selection_callback(df=None, **kwargs):
    print("-- in test callback -- ", kwargs)
    print(df)


def layout():
    az_list = make_test_subject_ids()
    column_names = ["subject_fixed", "subject_editable"]
    df = pd.DataFrame({col: az_list for col in column_names})

    hidden_div_name = "--".join([__name__, "hidden-div"]).replace(".", "")
    button_name = "--".join([__name__, "button-submit"]).replace(".", "")
    table_name = "--".join([__name__, "table-name"]).replace(".", "")

    main_layout = html.Div(
        [
            html.H3(__name__),
            add_table_with_editable_columns(
                df=df,
                table_name=table_name,
                columns_editable=[column_names[-1]],
                column_types={column_names[-1]: "text"},
            ),
            html.Button("Submit!", id=button_name, className="me-1"),
            html.Div(id=hidden_div_name, hidden=True),
        ]
    )

    @callback(
        [Output(hidden_div_name, "children")],
        [
            Input(button_name, "n_clicks"),
            State(table_name, "data"),
        ],
    )
    def f(n_clicks, data):
        print(n_clicks)
        if n_clicks is None:
            raise PreventUpdate

        table_data = pd.DataFrame(data)
        print("Table data:")
        print(table_data)
        return [None]

    return main_layout
