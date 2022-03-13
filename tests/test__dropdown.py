from collections import OrderedDict

import pandas as pd
from dash import Dash
from dash import dash_table
from dash import html


app = Dash(__name__)

df = pd.DataFrame(
    OrderedDict(
        [
            ("climate", ["Sunny", "Snowy", "Sunny", "Rainy"]),
            ("temperature", [13, 43, 50, 30]),
            ("city", ["NYC", "Montreal", "Miami", "NYC"]),
        ]
    )
)


def layout():
    layout = html.Div(
        [
            dash_table.DataTable(
                id="table-dropdown",
                data=df.to_dict("records"),
                columns=[
                    {"id": "climate", "name": "climate", "presentation": "dropdown"},
                    {"id": "temperature", "name": "temperature"},
                    {"id": "city", "name": "city", "presentation": "dropdown"},
                ],
                editable=True,
                dropdown={
                    "climate": {
                        "options": [
                            {"label": i, "value": i} for i in df["climate"].unique()
                        ]
                    },
                    "city": {
                        "options": [
                            {"label": i, "value": i} for i in df["city"].unique()
                        ]
                    },
                },
            ),
            html.Div(id="table-dropdown-container"),
        ]
    )

    return layout
