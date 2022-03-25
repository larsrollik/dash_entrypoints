import pandas as pd
from dash import html

from dash_entrypoints.elements.table_for_editing import add_table_with_editable_columns
from dash_entrypoints.elements.table_layout_wrapper import wrap_part_layout_for_callback


def make_test_subject_ids():
    import string

    az_list = [a for a in string.ascii_uppercase]
    return az_list


def example_callback_fun(state_data_dict: dict = None, **kwargs):
    print("\n\n in example_callback_fun")
    print("--> state_data_dict", state_data_dict)
    print("--> kwargs", kwargs)

    data_df = pd.DataFrame()
    for key, data in state_data_dict.items():
        if "data" == key[-1]:
            data_df = pd.DataFrame(data)

    print("data", data_df)
    print("\n END \n")


def layout():
    az_list = make_test_subject_ids()
    column_names = ["subject_fixed", "subject_editable"]
    df = pd.DataFrame({col: az_list for col in column_names})

    table_name = "--".join([__name__, "table-name"]).replace(".", "")
    part_layout = html.Div(
        [
            html.H3(__name__),
            add_table_with_editable_columns(
                df=df,
                table_name=table_name,
                columns_editable=[column_names[-1]],
                column_types={column_names[-1]: "text"},
            ),
        ]
    )

    complete_layout = wrap_part_layout_for_callback(
        part_layout_pre=part_layout,
        page_title="TEST-wrap-edit",
        callback_state_tuples=[(table_name, "data")],
        callback_fun=example_callback_fun,
        callback_kwargs={"example_kwarg": 345},
    )

    return complete_layout
