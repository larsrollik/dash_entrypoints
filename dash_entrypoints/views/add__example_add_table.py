from datetime import datetime
from pathlib import Path

import dash_html_components as html
import pandas as pd
import yaml
from dash import callback
from dash.dependencies import Input
from dash.dependencies import Output
from dash.dependencies import State
from dash.exceptions import PreventUpdate

from dash_entrypoints.elements.datatable import add_table
from dash_entrypoints.elements.datatable import make_dates_list
from dash_entrypoints.elements.datatable import make_times_list_24h
from dash_entrypoints.misc import add_random_id


def layout():
    """Example layout for `add_table` wrapper of dropdown columns."""

    # Table variables
    table_1 = "Procedures"
    subject_ids = ["A-A", "A-B", "A-C", "XX", "XY", "XZ"]
    times = make_times_list_24h()
    dates = make_dates_list()
    dt = datetime.now()
    df_for_table = pd.DataFrame(
        {
            "subject_id": subject_ids,
            "procedure_date": dt.date().strftime("%Y-%m-%d"),
            "procedure_time_start": pd.to_datetime(dt).round("5min").strftime("%H:%M"),
        }
    )
    dropdown_options_surgery = {
        "subject_id": subject_ids,
        "procedure_date": dates,
        "procedure_time_start": times,
        "procedure_time_end": times,
    }

    # LAYOUT
    submit_btn = add_random_id("submit_btn")
    dummy_div = add_random_id("hidden_div")

    layout = html.Div(
        [
            add_table(
                table_name=table_1,
                df=df_for_table,
                dropdown_options=dropdown_options_surgery,
                table_expandable=False,
            ),
            # NOTE: add other tables here
            html.Hr(),
            html.Button("Submit!", id=submit_btn),
            html.Div(id=dummy_div, hidden=True),
            html.Br(),
        ]
    )

    table_names = [
        table_1,
    ]
    state_inputs = [Input(submit_btn, "n_clicks")] + [
        State(t, "data") for t in table_names
    ]

    @callback(
        [Output(dummy_div, "hidden")],
        state_inputs,
    )
    def save_entry(n_clicks, *args):
        if n_clicks is None:
            raise PreventUpdate

        input_data = dict(zip(table_names, args))
        print("\n", yaml.dump(input_data), "\n")

        save_path = Path("/tmp/tmp__table_output.yaml")
        save_path.parent.mkdir(parents=True, exist_ok=True)
        if save_path.exists():
            print("Exists:", save_path.as_posix())

        with open(save_path, "w") as f:
            f.write(yaml.dump(input_data))
            print(f"\nWritten to: {save_path}\n")

        return [True]

    return layout
