font_family = "Verdana"

DEFAULT_TABLE_STYLE_CELL = {
    "font_family": font_family,
    "textAlign": "left",
    "padding": "5px",
    "backgroundColor": None,  # "black",
    "color": "black",
    "whiteSpace": "normal",
    "height": "auto",
}
DEFAULT_TABLE_STYLE_HEADER = {
    "font_family": font_family,
    "backgroundColor": None,  # "black",
    "color": "black",
    "fontWeight": "bold",
}
DEFAULT_TABLE = {"overflowX": "scroll"}
DEFAULT_TABLE_CONDITIONAL = [
    {
        "if": {"state": "selected"},  # 'active' | 'selected'
        "backgroundColor": "white",
        "textColor": "white",
        # "border": "1px solid blue",
    },
    {
        "if": {"row_index": "odd"},
        "backgroundColor": None,
    },
    {
        "if": {"row_index": "even"},
        "backgroundColor": None,
    },
]
