from dash import Dash, html, dash_table
import pandas as pd
import yfinance as yf

# TODO
# 讀取股票歷史資料
df = yf.download()

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='某某股票歷史股價'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10)
])

if __name__ == '__main__':
    app.run(debug=True)