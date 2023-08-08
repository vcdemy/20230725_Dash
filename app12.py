from dash import Dash, html, dcc, Output, Input, callback

app = Dash(__name__)

app.layout = html.Div([
                html.H1(id="output"),
                dcc.Interval(id='interval',
                             interval=1*1000, # in milliseconds
                             n_intervals=0)
])

@app.callback(
    Output('output','children'),
    Input('interval','n_intervals')
)
def update_h1(value):
    return value

if __name__=="__main__":
    app.run(debug=True)