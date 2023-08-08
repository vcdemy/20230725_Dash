from dash import Dash, html, dcc, Output, Input, callback

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id="input", value=10),
    html.H1(id='output')
])

@app.callback(
    Output('output','children'),
    Output('output','style'),
    Input('input','value')
)
def update_h1(value):
    try:
        value=int(value)
    except Exception as e:
        return value, {'backgroundColor':'red'}
    if value > 100:
        style={'backgroundColor':'red'}
    else:
        style={'backgroundColor':'green'}
    return value, style

if __name__=="__main__":
    app.run(debug=True)