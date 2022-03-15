from datetime import datetime

import pandas as pd
import yaml

from dash_entrypoints.elements.table_layout_wrapper import wrap_part_layout_for_callback
from dash_entrypoints.elements.table_with_dropdown import (
    add_table_with_dropdown_columns,
)
from dash_entrypoints.elements.table_with_dropdown import make_dates_list
from dash_entrypoints.elements.table_with_dropdown import make_times_list_24h


def example_callback_fun(state_data_dict, **kwargs):
    print("\n\n in example_callback_fun")

    yaml_items = [{key[0]: data} for key, data in state_data_dict.items()]
    yaml_str = yaml.dump(yaml_items)
    print("\n", yaml_str, "\n")

    with open(kwargs.get("save_path", "/tmp/example_table_content.yaml"), "w") as f:
        f.write(yaml.dump(yaml_str))
        print(f"\n{f.name}\n")

    print("\n END \n")


def layout():
    table_1 = "Procedures"
    subject_ids = ["A-A", "A-B", "A-C", "XX", "XY", "XZ"]
    times = make_times_list_24h()
    dates = make_dates_list()
    dt = datetime.now()
    df_for_table_1 = pd.DataFrame(
        {
            "subject_id": subject_ids,
            "procedure_date": dt.date().strftime("%Y-%m-%d"),
            "procedure_time_start": pd.to_datetime(dt).round("5min").strftime("%H:%M"),
        }
    )
    dropdown_options_procedures_1 = {
        "subject_id": subject_ids,
        "procedure_date": dates,
        "procedure_time_start": times,
        "procedure_time_end": times,
    }

    table_2 = "AdditionalFactor"
    subject_ids = ["A-A", "A-B", "A-C", "XX", "XY", "XZ"]
    times = make_times_list_24h()
    dates = make_dates_list()
    dt = datetime.now()
    df_for_table_2 = pd.DataFrame(
        {
            "subject_id": subject_ids,
            "procedure_date": dt.date().strftime("%Y-%m-%d"),
            "procedure_time_start": pd.to_datetime(dt).round("5min").strftime("%H:%M"),
        }
    )
    dropdown_options_procedures_2 = {
        "subject_id": subject_ids,
        "procedure_date": dates,
        "procedure_time_start": times,
        "procedure_time_end": times,
    }

    part_layout = [
        add_table_with_dropdown_columns(
            table_name=table_1,
            df=df_for_table_1,
            dropdown_options=dropdown_options_procedures_1,
            table_expandable=False,
            show_title=True,
        ),
        add_table_with_dropdown_columns(
            table_name=table_2,
            df=df_for_table_2,
            dropdown_options=dropdown_options_procedures_2,
            show_title=True,
        ),
    ]

    # for each table, add (table_name, "data")
    callback_state_tuples = [
        (table_1, "data"),
        (table_2, "data"),
    ]
    complete_layout = wrap_part_layout_for_callback(
        part_layout_pre=part_layout,
        page_title="TEST-wrap-dropdown",
        callback_state_tuples=callback_state_tuples,
        callback_fun=example_callback_fun,
        callback_kwargs={"save_path": "/tmp/example_callback_wrapper_basepath"},
    )

    return complete_layout
