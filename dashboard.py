import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(
    children = [
        html.H1('My Dashboard'),
        dcc.Graph(
            id='My-Graph',
            figure={
                'data':[
                    {'x':[1,2,3], 'y':[4,1,2], 'type': 'bar', 'name': 'Bar Chart'},
                    {'x':[1,2,3], 'y':[2,4,5], 'type': 'line', 'name': 'Line Chart'},

                ],
                'layout':{
                    'title': 'Graph title',
                    'xaxis': {'title':'x-axis'},
                    'yaxis': {'title':'y-axis'}
                }
            }
        )
    ]
)


if __name__ == '__main__':
    app.run(debug=True)