from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import yfinance as yf

stocks = ['TSLA', 'MSFT', 'AMZN']
prices = {}
for stock in stocks:
    prices[stock] = yf.download(stock)


app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='股票收盤價線圖'),
    html.Hr(),
    dcc.RadioItems(options=stocks, value='TSLA', id='controls-and-radio-item'),
    # dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Graph(figure={}, id='controls-and-graph')
])

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.line(prices[col_chosen], x=prices[col_chosen].index, y='Close')
    return fig

if __name__ == '__main__':
    app.run(debug=True)
