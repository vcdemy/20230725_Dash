from dash import Dash, html

app = Dash(__name__)

app.layout = html.H1("Hello Victor")

if __name__ == '__main__':
    app.run(debug=True)