import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import datetime


try:
    from app import app
except:
    app = dash.Dash()


def app_layout():
    return html.Div(serve_layout())


def serve_layout():
    return html.H1('Now: ' + str(datetime.datetime.now()))


if __name__ == "__main__":
    app.layout = app_layout()
    app.run_server(
        debug=True,
    )

