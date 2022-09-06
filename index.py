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


def import_apps_as_modules():
    ## find Apps
    apps_list = [a.replace("/", ".") for a in find_apps("apps/", "App.py", 3)]
    print("{:#^60}".format(f" Apps "))
    print(apps_list, len(apps_list))

    ## imort apps as modules
    print("{:#^60}".format(f" App Modules "))
    for a in apps_list:
        m = f"apps.{a}.App"
        print(m)
        import_module(m)


## Layout ##
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


print("{:#^60}".format(f" Requests "))
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    import_apps_as_modules() # import modules on page reload

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pathname = re.sub("^/", "", pathname)
    ##print(f"\n{now}\tApp: '{pathname}' ")
    print("{:#^60}".format(f" {now} App: '{pathname}' "))

    app_name = os.path.basename(pathname)
    print("app_name:", app_name)

    ## module "path"
    app_module = pathname.replace("/", ".")
    print("app_module:", app_module)
 
    try:
        if app_module=="":
            app_module = "landing_page"

        layout = f"apps.{app_module}.App.app_layout()"
        ##print("layout:", layout)
        return eval(layout)
    except:
        return "404" 


print("{:#^60}".format(f" globals() "))
print(globals())


if __name__ == '__main__':
    app.run_server(debug=True)

