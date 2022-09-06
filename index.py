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


## Find Apps and load as modules ##

def find_apps(path, name, maxdepth=1):
    """Find filename (e.g. 'App.py') in folder using 'find'."""
    paths = subprocess.check_output(f"find '{path}' -maxdepth {maxdepth} -name '{name}'", shell=True).decode().split()
    apps_list = []
    for p in paths:
        p = re.sub(f"^{path}", "", p)
        p = re.sub(f"/{name}$", "", p)
        apps_list.append(p)
    return apps_list


def import_app_as_module(pathname):
    ##print("{:#^60}".format(f" import_app_as_module: '{pathname}' "))
    pathname = re.sub("^/", "", pathname)
    a = pathname.replace("/", ".")
    m = f"apps.{a}.App"
    try:
        import_module(m)
    except:
        pass
    return m


def import_apps_as_modules():
    apps_list = find_apps("apps/", "App.py", 3)
    print("apps_list:", apps_list)

    for pathname in apps_list:
        import_app_as_module(pathname)


import_apps_as_modules() # initial loading of apps modules


## Layout ##
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


## Callback ##
print("{:#^60}".format(f" Requests "))
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    ##print(f"pathname: '{pathname}'")

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pathname = re.sub("^/", "", pathname)
    ##print("{:#^60}".format(f" {now} App: '{pathname}' "))
    print(f"{now}\tApp: '{pathname}' ")

    app_name = os.path.basename(pathname)
    ##print(f"app_name: '{app_name}'")

    ## module "path"
    app_module = pathname.replace("/", ".")
 
    try:
        if app_module=="":
            app_module = "landing_page"
        
        ## import module if new
        ##print(f"app_module: '{app_module}'")
        m = f"apps.{app_module}.App"
        ##print("m:", m)
        import_module(m)

        layout = f"apps.{app_module}.App.app_layout()"
        ##print("layout:", layout)
        return eval(layout)
    except:
        return "404" 
    

## print("{:#^60}".format(f" globals() "))
## print(globals())


if __name__ == '__main__':
    app.run_server(debug=True)

