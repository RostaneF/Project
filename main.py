import pandas as pd
import time
import statistics as stats
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

df = pd.read_csv("/home/ubuntu/Projet/Project/Generated_data/data.csv", delimiter=";")
app = Dash(__name__)

app.layout = html.Div(children=[
    html.Div(
        [
            html.H1("Bienvenue dans cette API", className="main-title"),
            html.P("Suivez en direct l'évolution du prix du S&P500 et du NASDAQ.", className="subtitle"),
            html.P("Nous mettons à jour les données toutes les minutes.", className="subtitle"),
        ],
        className="header"
    ),

    html.Div(
        [
            html.H2("Informations sur les indices", className="info-title"),

            html.Div(
                [
                    html.H3("SP500", className="info-subtitle"),
                    html.Div([
                        html.P(id='sp500-min'),
                        html.P(id='sp500-max'),
                        html.P(id='sp500-std'),
                        html.P(id='sp500-last'),
                        html.P(id='sp500-first')
                    ], className="info-text")
                ],
                className="info-box"
            ),

            html.Div(
                [
                    html.H3("NASDAQ", className="info-subtitle"),
                    html.Div([
                        html.P(id='nasdaq-min'),
                        html.P(id='nasdaq-max'),
                        html.P(id='nasdaq-std'),
                        html.P(id='nasdaq-last'),
                        html.P(id='nasdaq-first')
                    ], className="info-text")
                ],
                className="info-box"
            )
        ],
        className="info-container"
    ),

    dcc.Graph(
        id='Cours Index S&P 500',
        figure={
            'data': [
                {'x': pd.to_datetime(df['date'], format='%Y-%m-%d-%H-%M'), 'y': df['SP500'],'type': 'scatter', 'name': 'SP500'},
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
                {'x': pd.to_datetime(df['date'], format='%Y-%m-%d-%H-%M'), 'y': df['NASDAQ'],'type': 'scatter', 'name': 'NASDAQ'},
                ],
            'layout': {
                'title': 'Evolution de Idx NASDAQ'
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
     Output('Cours Index NASDAQ', 'figure'),
     Output('sp500-min', 'children'),
     Output('sp500-max', 'children'),
     Output('sp500-std', 'children'),
     Output('sp500-last', 'children'),
     Output('sp500-first', 'children'),
     Output('nasdaq-min', 'children'),
     Output('nasdaq-max', 'children'),
     Output('nasdaq-std', 'children'),
     Output('nasdaq-last', 'children'),
     Output('nasdaq-first', 'children')],
    Input('interval-component', 'n_intervals')
)
def update_all_graphs(n):
    # Charger les nouvelles données depuis votre fichier CSV
    df = pd.read_csv("/home/ubuntu/Projet/Project/Generated_data/data.csv", delimiter=";")
    # Remplacer les valeurs manquantes par la valeur 0 dans la colonne SP500
    df['SP500'].dropna(inplace=True)

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

    # Calculer les statistiques pour le SP500
    sp500_min = round(min(df['SP500']), 2)
    sp500_max = round(max(df['SP500']), 2)
    sp500_std = round(stats.stdev(df['SP500']), 2)
    sp500_last = round(df['SP500'].iloc[-1], 2)
    sp500_first = round(df['SP500'].iloc[0], 2)

    # Calculer les statistiques pour le NASDAQ
    nasdaq_min = round(min(df['NASDAQ']), 2)
    nasdaq_max = round(max(df['NASDAQ']), 2)
    nasdaq_std = round(stats.stdev(df['NASDAQ']), 2)
    nasdaq_last = round(df['NASDAQ'].iloc[-1], 2)
    nasdaq_first = round(df['NASDAQ'].iloc[0], 2)

    # Retourner toutes les valeurs mises à jour
    return [sp500_figure, nasdaq_figure, sp500_min, sp500_max, sp500_std, sp500_last, sp500_first, nasdaq_min, nasdaq_max, nasdaq_std, nasdaq_last, nasdaq_first]


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
    time.sleep(60)
