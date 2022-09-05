import os
import glob
from importlib import import_module
import json

import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from app import app


## Apps ##
apps = [ os.path.basename(os.path.dirname(x)) for x in glob.glob("apps/**/app.py")]
print("{:#^60}".format(f" Apps "))
print(apps, len(apps))


## Layouts ##
app_layouts = {}
print("{:#^60}".format(f" Layouts "))
for a in apps:
    try:
        m = import_module(f"apps.{a}.app")
        app_layouts[a] = m.app_layout()
        print(a)
    except:
        pass


## Layout ##
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


print("{:#^60}".format(f" Requests "))
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    a = os.path.basename(pathname)
    print("App:", f"'{a}'")

    try:
        if a=="":
            return app_layouts["landing_page"]
        else:
            return app_layouts[a]
    except:
        return "404" 


if __name__ == '__main__':
    app.run_server(debug=True)

