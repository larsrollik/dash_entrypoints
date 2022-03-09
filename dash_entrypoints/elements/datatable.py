import dash_html_components as html
import dash_table
import pandas as pd
from dash import Input
from dash import Output
from dash import State


def add_table(
    app=None,
    table_name=None,
    df=None,
    dropdown_options=None,
    dropdown_columns=[],
    table_expandable=True,
    table_width=90,
):
    """Dash DataTable wrapper to provide dropdown columns along with free field columns. Tables are row extendable.

    https://dash.plotly.com/datatable/dropdowns
    https://community.plotly.com/t/dash-datatable-dropdown-doesnt-work/19164/2
    https://github.com/plotly/dash/issues/1140
    """
    assert isinstance(df, pd.DataFrame)
    if df.empty:
        df = df.append(pd.Series(), ignore_index=True)  # add one empty row

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

    table_title = str(table_name).replace("_", " ").capitalize()

    layout = html.Div(
        [
            html.H3(
                table_title,
            ),
            dash_table.DataTable(
                id=table_name,
                data=df.to_dict("records"),
                columns=table_columns,
                editable=True,
                row_deletable=table_expandable,
                dropdown=dropdown_options,
            ),
            html.Div(id=f"{table_name}-container"),
            html.Button("Add Row", id=f"{table_name}-button", n_clicks=0)
            if table_expandable
            else html.Div(),
            html.Br(),
        ],
        style={
            "padding": "10px",
            "width": "90%" if table_width is None else f"{table_width}%",
        },
    )

    @app.callback(
        Output(table_name, "data"),
        Input(f"{table_name}-button", "n_clicks"),
        State(table_name, "data"),
        State(table_name, "columns"),
    )
    def add_row(n_clicks, rows, columns):
        if n_clicks > 0:
            rows.append({c["id"]: "" for c in columns})
        return rows

    return layout
