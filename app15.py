from dash import Dash, html

app = Dash(__name__)

app.layout = html.H1('Hello World!', 
                     style={"backgroundColor":"yellow",
                            "textAlign":"center"})

if __name__=="__main__":
    app.run(debug=True)
