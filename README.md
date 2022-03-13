<!--
-*- coding: utf-8 -*-

 Author: Lars B. Rollik <L.B.Rollik@protonmail.com>
 License:
-->
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

# Interfaces entrypoint

---


### TODO

- [x] document entrypoint for CLI and python
- [x] add elements like `DataTable` wrapper
- [x] add options to change base layout from `NavbarSimple`. -> Added `Navbar`
- [ ] update `readme` with info on dropdown vs selection table wrappers
- [ ] callback function wrapper into own page layout nesting? call wrapper to get final layout. within wrapper, use table function to generate inner table. wrapper provides submit button + wrapped callback. See outline in `dash_entrypoints/views/add__example_table_selection.py`


### Entrypoint for multi-page apps

##### Python

```python
from dash_entrypoints import run_entrypoint

run_entrypoint()
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
        --port 9050 \
        --debug
```



### Element wrappers

See for elements in `from interfaces_entrypoint import elements`

##### `dash.DataTable`

```python
from dash_entrypoints.elements.datatable import add_table_with_dropdown_columns

table = add_table_with_dropdown_columns(app=app_object, ...)
```

##### `box for buttons`

```python

```


## Author & License
 **[Copyright 2022. Lars Rollik. All rights reserved. - See license](LICENSE)**
