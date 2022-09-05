import os
import glob
from importlib import import_module
import json

import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from app import app


app_layouts = {}

apps = [ os.path.basename(os.path.dirname(x)) for x in glob.glob("apps/**/app.py")]
print("Apps:", apps, len(apps) )

for a in apps:
    ##print("{:#^60}".format(f" Module: {a} "))
    m = import_module(f"apps.{a}.app")
    app_layouts[a] = m.app_layout()


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    try:
        return app_layouts[os.path.basename(pathname)]
    except:
        return "404"


if __name__ == '__main__':
    app.run_server(debug=True)

