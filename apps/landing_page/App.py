import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import datetime
import glob
import os
import subprocess
import re


try:
    from application import app
except:
    app = dash.Dash()


def app_layout():
    return html.Div([
        html.H1("Index"),
        html.Div(links())
    ])


def find_apps(path, name, maxdepth=1):
    paths = subprocess.check_output(f"find '{path}' -maxdepth {maxdepth} -name '{name}'", shell=True).decode().split()
    apps_list = []
    for p in paths:
        p = re.sub(f"^{path}", "", p)
        p = re.sub(f"/{name}$", "", p)
        apps_list.append(p)
    return apps_list


def links():
    apps_list = find_apps("apps/", "App.py", 3)
    return [
        html.Div([
            dcc.Link(a, href=a)
        ]) for a in apps_list
    ]


if __name__ == "__main__":
    app.layout = app_layout
    app.run_server(
        debug=True,
    )

