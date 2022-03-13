import dash_html_components as html
import dash_table

DEFAULT_TABLE_NAME = "--".join([__name__, "table"]).replace(".", "--")


def add_table_for_selection(
    df=None,
    table_name=DEFAULT_TABLE_NAME,
    single_select=False,
    page_size=20,
):
    output_layout = html.Div(
        [
            dash_table.DataTable(
                id=table_name,
                columns=[
                    {"name": i, "id": i, "deletable": False, "selectable": True}
                    for i in df.columns
                ],
                data=df.to_dict("records"),
                editable=False,
                filter_action="native",
                sort_action="native",
                sort_mode="multi",
                row_selectable="single" if single_select else "multi",
                row_deletable=False,
                selected_columns=[],
                selected_rows=[],
                page_action="native",
                page_current=0,
                page_size=page_size,
            ),
        ]
    )
    return output_layout
