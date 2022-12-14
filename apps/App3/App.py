import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output


try:
    from application import app
except:
    app = dash.Dash()


def app_layout():
    return html.Div([
        html.H3('App 3'),
        dcc.Dropdown(
            id='app-3-dropdown',
            options=[
                {'label': 'App 3 - {}'.format(i), 'value': i} for i in [
                    'alpha', 'beta', 'gamma', 'delta', 'epsison'
                    ]
            ]
        ),
        html.Div(id='app-3-display-value'),
        html.Div([dcc.Link('Go to App 2', href='/App2')]),
        html.Div([dcc.Link('Go to App 3', href='/App3')]),
    ])


@app.callback(
    Output('app-3-display-value', 'children'),
    [Input('app-3-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)


if __name__ == "__main__":
    app.layout = app_layout
    app.run_server(
        debug=True,
    )

