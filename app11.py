from datetime import date
from dash import Dash, dcc, html, Input, Output, callback
import yfinance as yf
import plotly.express as px

df = yf.download('TSLA')

app = Dash(__name__)
app.layout = html.Div([
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2017, 9, 19),
        start_date=date(2015, 10, 10),
        end_date=date(2017, 8, 25)
    ),
    dcc.Graph(figure={}, id="myplot")
])


@callback(
    Output('myplot', 'figure'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'))
def update_output(start_date, end_date):
    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_date_string = start_date_object.strftime('%Y-%m-%d')
    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_date_string = end_date_object.strftime('%Y-%m-%d')
    fig = px.line(df[start_date_string:end_date_string], x=df[start_date_string:end_date_string].index, y='Close')
    return fig


if __name__ == '__main__':
    app.run(debug=True)
