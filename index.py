import os
import glob
from importlib import import_module
import json
import subprocess
import datetime
import re

import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from application import app 

import apps # modules


def find_apps(path, name, maxdepth=1):
    """Find filename (e.g. 'App.py') in folder using 'find'."""
    paths = subprocess.check_output(f"find '{path}' -maxdepth {maxdepth} -name '{name}'", shell=True).decode().split()
    apps_list = []
    for p in paths:
        p = re.sub(f"^{path}", "", p)
        p = re.sub(f"/{name}$", "", p)
        apps_list.append(p)
    return apps_list


## Apps ##
apps_list = [a.replace("/", ".") for a in find_apps("apps/", "App.py", 3)]
print("{:#^60}".format(f" Apps "))
print(apps_list, len(apps_list))


print("{:#^60}".format(f" App Modules "))
for a in apps_list:
    m = f"apps.{a}.App"
    print(m)
    import_module(m)


print("{:#^60}".format(f" globals() "))
print(globals())


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
    ##print("a:", a)

    ## module "path"
    m = pathname.replace("/", ".")
    m = re.sub("^\.", "", m)
    ##print("m:", m)

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{now}\tApp: '{a}' ")
    try:
        if m=="":
            m = "landing_page"

        layout = f"apps.{m}.App.app_layout()"
        ##print("layout:", layout)
        return eval(layout)
    except:
        return "404" 


if __name__ == '__main__':
    app.run_server(debug=True)

