from dash import callback
from dash import html
from dash import Input
from dash import Output

from dash_entrypoints.misc import add_random_id


def layout():
    """Front page"""
    submit_btn = add_random_id("test_button_frontpage")
    text_h5 = add_random_id("out_text")
    layout = html.Div(
        [
            html.H3(
                "Empty front page. Choose one of the linked pages in the navbar above."
            ),
            html.H5("", id=text_h5),
            html.Button("!", id=submit_btn),
        ]
    )

    @callback([Output(text_h5, "label")], Input(submit_btn, "n_clicks"))
    def f(n_clicks):
        print(n_clicks)
        return f"Clicks: {n_clicks}"

    return layout
