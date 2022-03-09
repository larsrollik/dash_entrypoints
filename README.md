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
- [ ] add elements like `DataTable` wrapper
- [ ] add options to change base layout from `NavbarSimple`



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
from dash_entrypoints.elements.datatable import add_table

table = add_table(app=app_object, ...)
```

##### `box for buttons`

```python

```


## Author & License
 **[Copyright 2022. Lars Rollik. All rights reserved. - See license](LICENSE)**
