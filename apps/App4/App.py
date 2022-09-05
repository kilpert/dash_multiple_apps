import dash
from dash import Dash, html, dcc


try:
    from application import app
except:
    app = dash.Dash()



def app_layout(): 
    return html.Div([

        html.H1("Hello Dash!"),
        html.Div("Dash: Web Dashboards with Python"),

        dcc.Graph(
            id="example_id",
            figure={
                "data":[
                    {
                        "x":[1, 2, 3],
                        "y":[4, 1, 2],
                        "type":"bar",
                        "name":"SF",
                    },
                    {
                        "x":[1, 2, 3],
                        "y":[2, 4, 5],
                        "type":"bar",
                        "name":"NYC",
                    }
                ],
                "layout":{
                    "title":"Bar plots",
                },
            }
        )
    ]
)


if __name__ == "__main__":
    app.layout = app_layout
    app.run_server(
        debug=True,
    )

