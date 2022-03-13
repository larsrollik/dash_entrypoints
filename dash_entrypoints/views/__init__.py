from dash import callback
from dash import html
from dash import Input
from dash import Output
from dash.exceptions import PreventUpdate


def layout():
    """Front page"""
    submit_btn = "--".join([__name__, "submit-btn"]).replace(".", "")
    text_h5 = "--".join([__name__, "out-text"]).replace(".", "")
    layout = html.Div(
        [
            html.H3(
                "Empty front page. Choose one of the linked pages in the navbar above."
            ),
            html.Button("!", id=submit_btn),
            html.Label("Clicked.", id=text_h5, hidden=True),
        ]
    )

    @callback([Output(text_h5, "hidden")], Input(submit_btn, "n_clicks"))
    def f(n_clicks):
        if n_clicks is None:
            raise PreventUpdate

        print(n_clicks)
        return [False]

    return layout
