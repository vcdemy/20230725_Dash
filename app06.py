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
    dash_table.DataTable(data=None, page_size=10, id="historical-prices"),
    dcc.Graph(figure={}, id='controls-and-graph')
])

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Output(component_id="historical-prices", component_property="data"),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.line(prices[col_chosen].tail(100), x=prices[col_chosen].tail(100).index, y='Close')
    data = prices[col_chosen].reset_index().tail(100).to_dict('records')
    return fig, data

if __name__ == '__main__':
    app.run(debug=True)
