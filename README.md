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
- [ ] update `readme` with examples for `kwargs` and `button box`
- [x] callback function wrapper into own page layout nesting? call wrapper to get final layout. within wrapper, use table function to generate inner table. wrapper provides submit button + wrapped callback. See outline in `dash_entrypoints/views/add__example_table_selection.py`
- [ ] document `table_layout_wrapper for callback`

### Entrypoint for multi-page apps

##### Python

```python
from dash_entrypoints import run_entrypoint

kwargs = {}
run_entrypoint(**kwargs)
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

##### `box for buttons`

```python
# TODO
```


## Author & License
 **[Copyright 2022. Lars Rollik. All rights reserved. - See license](LICENSE)**
