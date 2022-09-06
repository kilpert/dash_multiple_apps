import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output


try:
    from application import app
except:
    app = dash.Dash()


def app_layout():
    return html.Div([
        html.H3('Test 2'),
        dcc.Dropdown(
            id='test-2-dropdown',
            options=[
                {'label': 'Test 1 - {}'.format(i), 'value': i} for i in ['1', '10', '100']
            ]
        ),
        html.Div(id='test-2-display-value'),
        html.Div([dcc.Link('Go to App 2', href='/App2')]),
        html.Div([dcc.Link('Go to App 3', href='/App3')]),
    ])


@app.callback(
    Output('test-2-display-value', 'children'),
    [Input('test-2-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)


if __name__ == "__main__":
    app.layout = app_layout
    app.run_server(
        debug=True,
    )

