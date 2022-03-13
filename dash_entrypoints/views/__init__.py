from dash import callback
from dash import html
from dash import Input
from dash import Output


def layout():
    """Front page"""
    submit_btn = "--".join([__name__, "submit-btn"]).replace(".", "")
    text_h5 = "--".join([__name__, "out-text"]).replace(".", "")
    layout = html.Div(
        [
            html.H3(
                "Empty front page. Choose one of the linked pages in the navbar above."
            ),
            html.H5("", id=text_h5),
            html.Button("!", id=submit_btn),
        ]
    )

    @callback([Output(text_h5, "title")], Input(submit_btn, "n_clicks"))
    def f(n_clicks):
        print(n_clicks)
        return f"Clicks: {n_clicks}"

    return layout
