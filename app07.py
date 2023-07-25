from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import yfinance as yf

stocks = ['TSLA', 'MSFT', 'AMZN', 'GOOG', 'AMD', 'NVDA']
prices = {}
for stock in stocks:
    prices[stock] = yf.download(stock)


app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='股票收盤價線圖'),
    html.Hr(),
    dcc.RadioItems(options=stocks, value='TSLA', id='controls-and-radio-item', inline=True),
    dcc.Slider(10, 100, 10, value=50, id="my-slider"),
    html.Hr(),
    dash_table.DataTable(data=None, page_size=10, id="historical-prices"),
    dcc.Graph(figure={}, id='controls-and-graph')
])

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Output(component_id="historical-prices", component_property="data"),
    Input(component_id='controls-and-radio-item', component_property='value'),
    Input(component_id='my-slider', component_property='value')
)
def update_graph(stock, value):
    fig = px.line(prices[stock].tail(value), x=prices[stock].tail(value).index, y='Close')
    data = prices[stock].reset_index().tail(value).to_dict('records')
    return fig, data

if __name__ == '__main__':
    app.run(debug=True)
