import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output


def info():
    return "App1"


try:
    from app import app
except:
    app = dash.Dash()


def app_layout():
    return html.Div([
        html.H3('App 1'),
        dcc.Dropdown(
            id='app-1-dropdown',
            options=[
                {'label': 'App 1 - {}'.format(i), 'value': i} for i in ['A', 'B', 'C']
            ]
        ),
        html.Div(id='app-1-display-value'),
        html.Div([dcc.Link('Go to App 2', href='/app2')]),
        html.Div([dcc.Link('Go to App 3', href='/app3')]),
    ])


@app.callback(
    Output('app-1-display-value', 'children'),
    [Input('app-1-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)


if __name__ == "__main__":
    app.layout = app_layout
    app.run_server(
        debug=True,
    )

