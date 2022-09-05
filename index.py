import os
import glob
from importlib import import_module
import json

import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from application import app

import apps # modules


## Apps ##
app_list = [ os.path.basename(os.path.dirname(x)) for x in glob.glob("apps/**/App.py")]
print("{:#^60}".format(f" Apps "))
print(app_list, len(app_list))


print("{:#^60}".format(f" App Modules "))
for a in app_list:
    m = f"apps.{a}.App"
    print(m)
    import_module(m)


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
            return eval(f"apps.landing_page.App.app_layout()")
        else:
            print(eval(f"apps.{a}.App.app_layout()"))
            return eval(f"apps.{a}.App.app_layout()")
    except:
        return "404" 


if __name__ == '__main__':
    app.run_server(debug=True)

