import argparse
import importlib
import socket
from pathlib import Path

import dash
import dash_labs as dl
import numpy as np
from dash import callback
from dash import Dash
from dash import dcc
from dash import html
from dash import Input
from dash import Output
from dash import State


def layout():
    """Example page layout. Shows a random number as proof of reload on every browser page refresh."""
    layout = html.Div([html.H1(f"{__name__}, {np.random.randint(100)}")])
    return layout
