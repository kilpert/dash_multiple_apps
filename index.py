import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from app import app
from apps import app1
from apps import app2
from apps import app3


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)

    if pathname == '/apps/app1':
        return app1.app_layout()
    elif pathname == '/apps/app2':
        return app2.app_layout()
    elif pathname == '/apps/app3':
        return app3.app_layout()
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)

