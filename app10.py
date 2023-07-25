from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd

df = pd.read_csv("https://mopsfin.twse.com.tw/opendata/t187ap03_L.csv")

app = Dash(__name__)

app.layout = html.Div(
    [
        html.I("請輸入股票代號"),
        html.Br(),
        dcc.Input(id="input1", type="text", placeholder="股票代號"),
        html.Div(id="output"),
    ]
)


@callback(
    Output("output", "children"),
    Input("input1", "value")
)
def update_output(input1):
    return df[df['公司代號'==input1]]


if __name__ == "__main__":
    app.run(debug=True)
