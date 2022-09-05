import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import datetime
import glob
import os


try:
    from application import app
except:
    app = dash.Dash()


def app_layout():
    return html.H1("Index"), html.Div(links())


def links():
    apps_dict = {}
    for p in glob.glob("apps/**/App.py"):
        apps_dict[os.path.basename(os.path.dirname(p))] = os.path.dirname(p)
    print(apps_dict)
    
    return [
        html.Div([
            dcc.Link(a, href=p)
        ]) for a,p in apps_dict.items()
    ]


if __name__ == "__main__":
    app.layout = app_layout
    app.run_server(
        debug=True,
    )

