import pandas as pd
import time
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

df = pd.read_csv("/home/ubuntu/Projet/Project/Generated_data/data.csv", delimiter=";")
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children=[
        html.H1(children='Bienvenue dans cette API'),
        html.P(children='Suivez en direct l\'évolution du prix du S&P500 et du NASDAQ.'),
        html.P(children='Nous mettons à jour les données toutes les minutes.'),
    ]),

    dcc.Graph(
        id='Cours Index S&P 500',
        figure={
            'data': [
                {'x': pd.to_datetime(df['date'], format='%Y-%m-%d-%H-%M'), 'y': df['SP500'],'type': 'area', 'name': 'SP500'},
               ],
            'layout': {
                'title': 'Evolution de Idx S&P500'
            }
        }
    ),
    dcc.Graph(
        id='Cours Index NASDAQ',
        figure={
            'data': [
                {'x': pd.to_datetime(df['date'], format='%Y-%m-%d-%H-%M'), 'y': df['NASDAQ'],'type': 'area', 'name': 'NASDAQ'},
               ],
            'layout': {
                'title': 'Evolution de Idx  NASDAQ'
            }
        }
    ),
    dcc.Interval(
        id='interval-component',
        interval=60*1000,
        n_intervals=0
    )
])
@app.callback(
    [Output('Cours Index S&P 500', 'figure'),
     Output('Cours Index NASDAQ', 'figure')],
    Input('interval-component', 'n_intervals')
)
def update_all_graphs(n):
    # Charger les nouvelles données depuis votre fichier CSV
    df = pd.read_csv("/home/ubuntu/Projet/Project/Generated_data/data.csv", delimiter=";")
    # Mettre à jour la figure du graphique SP500 avec les nouvelles données
    sp500_figure = {
        'data': [
            {'x': pd.to_datetime(df['date'], format='%Y-%m-%d-%H-%M'), 'y': df['SP500'],'type': 'area', 'name': 'SP500'},
        ],
        'layout': {
            'title': 'Evolution de Idx S&P500'
        }
    }
    # Mettre à jour la figure du graphique NASDAQ avec les nouvelles données
    nasdaq_figure = {
        'data': [
            {'x': pd.to_datetime(df['date'], format='%Y-%m-%d-%H-%M'), 'y': df['NASDAQ'],'type': 'area', 'name': 'NASDAQ'},
        ],
        'layout': {
            'title': 'Evolution de Idx NASDAQ'
        }
    }
    return [sp500_figure, nasdaq_figure]


if __name__ == "__main__":
	app.run_server(host = "0.0.0.0", port = 8050, debug = True)
	time.sleep(60)
