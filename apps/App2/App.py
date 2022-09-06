import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output


try:
    from application import app
except:
    app = dash.Dash()


def app_layout():
    return html.Div([
        html.H3('App 2'),
        dcc.Dropdown(
            id='app-2-dropdown',
            options=[
                {'label': 'App 2 - {}'.format(i), 'value': i} for i in ['1', '2', '3', '4']
            ]
        ),
        html.Div(id='app-2-display-value'),
        html.Div([dcc.Link('Go to App 1', href='/App1')]),
        html.Div([dcc.Link('Go to App 3', href='/App3')]),
    ])


@app.callback(
    Output('app-2-display-value', 'children'),
    [Input('app-2-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)


if __name__ == "__main__":
    app.layout = app_layout
    app.run_server(
        debug=True,
    )

