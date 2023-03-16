import pandas as pd
import time
from dash import Dash, dcc, html

df = pd.read_csv("/home/ubuntu/Projet/Project/Generated_data/data.csv", delimiter=";")
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children=[
        html.H1(children='Bienvenue dans cette API'),
        html.P(children='Suivez en direct l\'évolution du prix du S&P500 et du NASDAQ.'),
        html.P(children='Nous mettons à jour les données toutes les minutes.'),
    ]),

    dcc.Graph(
        id='Cours des Index S&P 500',
        figure={
            'data': [
                {'x': df['date'], 'y': df['SP500'],'type': 'line', 'name': 'SP500'},
                {'x': df['date'], 'y': df['NASDAQ'], 'type': 'line', 'name': 'NASDAQ'},
            ],
            'layout': {
                'title': 'Evolution S&P500 et NASDAQ'
            }
        }
    )
])

if __name__ == "__main__":
	app.run_server(host = "0.0.0.0", port = 8050, debug = True)
	time.sleep(300)
