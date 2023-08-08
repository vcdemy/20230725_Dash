from dash import Dash, html, dcc, Output, Input, callback
import pandas as pd
import plotly.express as px
import json

app = Dash(__name__)

url = "https://github.com/mwaskom/seaborn-data/raw/master/flights.csv"
df = pd.read_csv(url)
wide = df.pivot(index="year", columns="month", values="passengers")
wide = wide[['January','February','March','April','May','June',
             'July','August','September','October','November','December']]
fig = px.imshow(wide, text_auto=True)

app.layout = html.Div([
    html.H1('1949-1960個月分旅客數量'),
    dcc.Graph(id="passengers", figure=fig),
    html.Pre(id="pre")
])

@app.callback(
    Output('pre', 'children'),
    Input('passengers','hoverData')
)
def get_data(value):
    return json.dumps(value, indent=2)

if __name__=="__main__":
    app.run(debug=True)