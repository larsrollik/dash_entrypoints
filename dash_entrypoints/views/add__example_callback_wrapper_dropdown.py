import pandas as pd

from dash_entrypoints.elements.table_for_selection import add_table_for_selection
from dash_entrypoints.elements.table_layout_wrapper import wrap_part_layout_for_callback
from dash_entrypoints.elements.table_with_dropdown import (
    add_table_with_dropdown_columns,
)


def make_test_subject_ids():
    import string

    az_list = [a for a in string.ascii_uppercase]
    return az_list


def example_callback_fun(state_data_tuples, **kwargs):
    print("\n\n in example_callback_fun")
    print("--> state_data_tuples", state_data_tuples)
    print("--> kwargs", kwargs)
    # print(
    #     "--> data:",
    #     pd.DataFrame(state_data_tuples[1][-1]).iloc[state_data_tuples[0][-1]],
    # )
    # print("\n", yaml.dump(input_data), "\n")  # TODO: dump all table data into yaml format
    # TODO: write to file as in add__example_table_dropdown.py
    # TODO: add file path to input kwargs
    print("\n END \n")


def layout():
    az_list = make_test_subject_ids()
    df = pd.DataFrame(az_list, columns=["subject_id"])
    table_name = "--".join([__name__, "table-name"]).replace(".", "")

    # TODO: add multiple dropdown tables
    part_layout = (
        add_table_for_selection(
            df=df,
            table_name=table_name,
            page_size=20,
        ),
    )

    complete_layout = wrap_part_layout_for_callback(
        part_layout=part_layout,
        page_title="TEST-wrap-dropdown",
        callback_state_tuples=[
            (table_name, "selected_rows"),
            (table_name, "data"),
        ],  # TODO: for each table, add (table_name, "data")
        callback_fun=example_callback_fun,
        callback_kwargs={"save_path": "/tmp/example_callback_wrapper_basepath"},
    )

    return complete_layout
