<!--
-*- coding: utf-8 -*-

 Author: Lars B. Rollik <L.B.Rollik@protonmail.com>
 License: BSD 3-Clause
-->
<!-- Banners -->

[![DOI](https://zenodo.org/badge/467883785.svg)](https://zenodo.org/badge/latestdoi/467883785)
[![Website](https://img.shields.io/website?up_message=online&url=https%3A%2F%2Fgithub.com/larsrollik/dash_entrypoints)](https://github.com/larsrollik/dash_entrypoints)
[![PyPI](https://img.shields.io/pypi/v/dash_entrypoints.svg)](https://pypi.org/project/dash_entrypoints)
[![Wheel](https://img.shields.io/pypi/wheel/dash_entrypoints.svg)](https://pypi.org/project/dash_entrypoints)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](https://github.com/larsrollik/dash_entrypoints/pulls)

# Dash entrypoints
CLI & wrapper for multi-page apps, layout callbacks, and more.
---

See features & entrypoints listed below.



### Entrypoint for multi-page apps

##### Python

```python
from dash_entrypoints import run_entrypoint

kwargs = {}
run_entrypoint(**kwargs)
```


###### Load `app_data` from file for use with `run_entrypoint` (expects `dict`, not a filepath)

```python
from dash_entrypoints.misc import load_app_data
from dash_entrypoints import run_entrypoint

app_data_file = "/some/file/path"
app_data = load_app_data(file=app_data_file)
run_entrypoint(app_data=app_data)
```


##### CLI

Show arguments
```shell
ifentry --help
```

Example call
```shell
ifentry --app-name TEST-NAME \
        --ip-address 192.168.100.10 \
        --views-module 'mypackage.page_subpackage' \
        --assets-folder '/path/to/assets/folder' \
        --port 9050 \
        --debug
```



### Element wrappers

See for elements in `from interfaces_entrypoint import elements`

##### Standard layouts for `dash.DataTable`

###### With column dropdowns

```python
from dash_entrypoints.elements.table_with_dropdown import add_table_with_dropdown_columns

kwargs = {}
table = add_table_with_dropdown_columns(**kwargs)
```

###### With selection handles

```python

from dash_entrypoints.elements.table_for_selection import add_table_for_selection

kwargs = {}
table = add_table_for_selection(**kwargs)
```

###### With editable columns (& typecasting for entered edited values for homogenous data in callbacks)

```python

from dash_entrypoints.elements.table_for_editing import add_table_with_editable_columns

kwargs = {}
table = add_table_with_editable_columns(**kwargs)
```

###### Popup (dbc.Modal) for information, e.g. as callback confirmation
```python

from dash_entrypoints.elements.popup_for_information import add_popup_for_information

popup_list = [
        {
            "name": "success",
            "title": "Successfully inserted new entry.",
            "text": None,
            "close_button": False,
            "is_open": False,
        },
        {"name": "error", "title": "Error during insert", "close_button": True},
    ]
popup_layout, popup_list = add_popup_for_information(popup_list=popup_list)

# Add to main layout...
# Note: `popup_layout` is a list of popup layout objects
```

##### Box for buttons

```python
# TODO, see Issue #3
```

#### Callback wrapper for inner layout

This tool helps to minimise boilerplate code while dynamically combining inner layout elements
with a button in the outer layout that triggers a callback function that can be connected
to the inner elements via (state, variable) tuples.

This function takes a part layout as list of dash layout elements, e.g. one or multiple tables,
and a callback function plus the adequate states that feed data into the callback.
The callback trigger is a button that gets added to the outer layout.

The outer callback wrapper only hands down the input data to the given callback function for processing.
(See examples `add__example_callback_wrapper_dropdown` and `add__example_callback_wrapper_selection`)

```python
from dash_entrypoints.elements.table_layout_wrapper import wrap_part_layout_for_callback


```

#### Plugins for dash

To write a plugin, create a module .py file and add at least a method `plug` to it.
Data can be assigned (& virtually treated like a global attribute of the `dash` module if assigned as attribute to it in the `plug` method).

Writing plugins for Dash does not seem to be documented yet, but logic of plugins can be observed in some repos on `github.com/plotly` or at `dash_labs.plugins.pages`.
See also `dash_entrypoints.plugins` for examples.

###### Example of mnimal plugin

```python
import dash

def plug(app):
    # Assign data to `dash` module
    dash.some_plugin_data_container = {}

    # Plugin logic (Manipulate data here)
    # ...
```

###### Example use of any plugin

```python
import dash
from dash_entrypoints.plugins import minimalplugin

app = dash.Dash(
    plugins=[minimalplugin],
)

# Test here that `dash` already has the attribute from `minimalplugin`
print(dash.minimal_plugin_attribute)
# >> {'test1': 1}

```



## Contributing

Contributions are welcome! Please open
[issues](https://github.com/larsrollik/dash_entrypoints/issues) or
[pull requests](https://github.com/larsrollik/dash_entrypoints/pulls) or
[get in touch](https://github.com/larsrollik).



## Citation

> Rollik, Lars B. (2022). Dash entrypoints: . doi: [10.5281/zenodo.6412527](https://doi.org/10.5281/zenodo.6412527).

**BibTeX**
```BibTeX
@misc{rollik2021rpi,
    author       = {Lars B. Rollik},
    title        = {{Dash entrypoints: }},
    year         = {2022},
    month        = apr,
    publisher    = {Zenodo},
    url          = {https://doi.org/10.5281/zenodo.6412527},
    doi          = {10.5281/zenodo.6412527},
  }
```


## License
This software is released under the **[BSD 3-Clause License](https://github.com/larsrollik/dash_entrypoints/blob/master/LICENSE)**

---
Version: "0.2.3"
