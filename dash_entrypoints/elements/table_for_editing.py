import dash_html_components as html
import dash_table
import pandas as pd

from dash_entrypoints.assets import DEFAULT_TABLE
from dash_entrypoints.assets import DEFAULT_TABLE_CONDITIONAL
from dash_entrypoints.assets import DEFAULT_TABLE_STYLE_CELL
from dash_entrypoints.assets import DEFAULT_TABLE_STYLE_HEADER

DEFAULT_TABLE_NAME = "--".join([__name__, "table"]).replace(".", "--")


def add_table_with_editable_columns(
    df: pd.DataFrame = None,
    table_name: str = None,
    columns_editable: list = None,
    column_types: dict = None,
    row_selectable=False,
    page_size: int = 20,
    style_as_list_view: bool = True,
    style_cell=DEFAULT_TABLE_STYLE_CELL,
    style_header=DEFAULT_TABLE_STYLE_HEADER,
    style_table=DEFAULT_TABLE,
    style_data_conditional=DEFAULT_TABLE_CONDITIONAL,
):
    """
    Add a table for callbacks based on editable columns

    :param df: pandas dataframe
    :param table_name: str
    :param columns_editable: list, ["col1"]
    :param column_types:  dict, e.g. {"col1": "text", "col2": "numeric"}
    :param row_selectable: True/False, "single", "multi"
    :param page_size: int
    :param style_as_list_view: bool
    :param style_cell:
    :param style_header:
    :param style_table:
    :param style_data_conditional:
    :return:
    """
    assert isinstance(columns_editable, list) or columns_editable is None
    assert isinstance(column_types, dict) or column_types is None

    if columns_editable is None:
        columns_editable = []
    if column_types is None:
        column_types = {}

    columns = [
        {
            "name": col,
            "id": col,
            "editable": True if col in columns_editable else False,
            "type": column_types.get(col, "text"),
        }
        for idx, col in enumerate(df.columns)
    ]

    output_layout = html.Div(
        [
            dash_table.DataTable(
                id=table_name,
                columns=columns,
                data=df.to_dict("records"),
                row_selectable=row_selectable,
                row_deletable=False,
                selected_columns=[],
                selected_rows=[],
                sort_action="native",
                sort_mode="multi",
                sort_by=[],
                page_current=0,
                page_size=page_size,
                style_as_list_view=style_as_list_view,
                style_cell=style_cell,
                style_header=DEFAULT_TABLE_STYLE_HEADER,
                style_table=DEFAULT_TABLE,
                style_data_conditional=DEFAULT_TABLE_CONDITIONAL,
            ),
        ]
    )
    return output_layout
