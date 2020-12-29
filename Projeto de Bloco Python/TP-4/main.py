import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Input(
        id='input',
        value='Enter com o número',
        type='text'),
    html.Div(id='output'),
    html.H1("DashBoard"),
    dcc.Graph(
        id="example",
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5],
                 'y': [5, 4, 7, 4, 8],
                 'type': 'line',
                 'name': 'Trucks'},
                {'x': [1, 2, 3, 4, 5],
                 'y': [5, 4, 7, 4, 8],
                 'type': 'bar',
                 'name': 'Ships'}
            ],
            'layout': {
                'title': 'Basic Dashboard'
            }
        },
    )
])


@app.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    try:
        return str(float(input_data) ** 2)
    except:
        return "Error, the input is not a number"


if __name__ == '__main__':
    app.run_server()
