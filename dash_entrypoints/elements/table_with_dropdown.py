from datetime import datetime

import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table
import numpy as np
import pandas as pd
from dash import callback
from dash import Input
from dash import Output
from dash import State


DEFAULT_TABLE_NAME = "--".join([__name__, "table"]).replace(".", "--")


def make_times_list_24h(step_hours=1, step_minutes=5):
    """Makes list of time combinations of hours/minutes in given spacing. For dropdown table columns.

    :param step_hours:
    :param step_minutes:
    :return:
    """
    minutes = np.arange(0, 60, step_minutes)
    hours = np.arange(0, 24, step_hours)
    times_list = [f"{h}:{m:0>2}" for h in hours for m in minutes]
    return times_list


def make_dates_list(years=None, months=np.arange(1, 13, 1), days=np.arange(1, 32, 1)):
    """Makes list of date combinations of "%Y-%m-%d" in given spacing. For dropdown table columns.

    :param years: list of year str like dt.strftime("%Y") format
    :param months: list of
    :param days:
    :return:
    """
    if not years:
        years = [datetime.now().strftime("%Y")]

    dates_list = [f"{Y}-{M:0>2}-{D:0>2}" for Y in years for M in months for D in days]
    return dates_list


def add_table_with_dropdown_columns(
    table_name: str = DEFAULT_TABLE_NAME,
    df: pd.DataFrame = None,
    dropdown_options: dict = None,
    dropdown_columns: list = None,
    table_expandable: bool = True,
    table_width: int = 100,
    show_title=False,
    **kwargs,
):
    """Dash DataTable wrapper to provide dropdown columns along with free field columns. Tables are row extendable.

    https://dash.plotly.com/datatable/dropdowns
    https://community.plotly.com/t/dash-datatable-dropdown-doesnt-work/19164/2
    https://github.com/plotly/dash/issues/1140
    """
    assert isinstance(df, pd.DataFrame)
    dropdown_columns = dropdown_columns or []

    if df.empty:
        df = df.append(pd.Series(), ignore_index=True)  # add one empty row

    table_button_name = (
        "--".join([table_name, "button"]).replace(".", "--").replace(" ", "-")
    )
    table_title_heading = (
        html.H3(str(table_name).replace("_", " ").capitalize())
        if show_title
        else html.Div(hidden=True)
    )

    # Full list of options as input ?
    if dropdown_options is not None:
        dropdown_options = {
            k: {"options": [{"label": str(i), "value": i} for i in v]}
            for k, v in dropdown_options.items()
        }
        dropdown_columns = dropdown_options.keys()
    else:
        dropdown_options = {
            c: {"options": [{"label": str(i), "value": i} for i in pd.unique(df[c])]}
            for c in df.columns
            if c in dropdown_columns
        }

    # Columns
    table_columns = [
        {"id": c, "name": c, "presentation": "dropdown"}
        for c in df.columns
        if c in dropdown_columns
    ] + [
        {
            "id": c,
            "name": c,
            # "editable": True,
        }
        for c in df.columns
        if c not in dropdown_columns
    ]

    layout = html.Div(
        [
            table_title_heading,
            dash_table.DataTable(
                id=table_name,
                data=df.to_dict("records"),
                columns=table_columns,
                editable=True,
                row_deletable=table_expandable,
                dropdown=dropdown_options,
            ),
            html.Div(id=f"{table_name}-container"),
            dbc.Button("Add Row", id=table_button_name, n_clicks=0)
            if table_expandable
            else html.Div(hidden=True),
        ],
        style={
            "padding": "0px",
            "width": "90%" if table_width is None else f"{table_width}%",
        },
    )

    if table_expandable:

        @callback(
            Output(table_name, "data"),
            [
                Input(table_button_name, "n_clicks"),
                State(table_name, "data"),
                State(table_name, "columns"),
            ],
        )
        def add_row(n_clicks, rows, columns):
            if n_clicks > 0:
                rows.append({c["id"]: "" for c in columns})
            return rows

    return layout
