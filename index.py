import os
import glob
from importlib import import_module
import json

import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from app import app

import apps # modules


## Apps ##
app_list = [ os.path.basename(os.path.dirname(x)) for x in glob.glob("apps/**/app.py")]
print("{:#^60}".format(f" Apps "))
print(app_list, len(app_list))


print("{:#^60}".format(f" App Modules "))
for a in app_list:
    m = f"apps.{a}.app"
    print(m)
    import_module(m)


import_module("apps.app1.app")
import_module("apps.app2.app")


##print("{:#^60}".format(f" globals() "))
##print(globals())


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
            return eval(f"apps.landing_page.app.app_layout()")
        else:
            return eval(f"apps.{a}.app.app_layout()")
    except:
        return "404" 


if __name__ == '__main__':
    app.run_server(debug=True)

