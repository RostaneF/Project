import pandas as pd
import time
import statistics as stats
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

df = pd.read_csv("/home/ubuntu/Projet/Project/Generated_data/data.csv", delimiter=";")
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



app.layout = dbc.Container(fluid=True, children=[
    dbc.Row(
    dbc.Col(
        html.Div(
            [
                html.H1("Bienvenue dans ce Dashboard", className="main-title"),
                html.P("Suivez en direct l'évolution du prix du S&P500 et du NASDAQ.", className="subtitle"),
                html.P("Nous mettons à jour les données toutes les minutes.", className="subtitle"),
            ],
            className="header text-center py-5",
            style={
                'background': 'linear-gradient(135deg, #2E4053 0%, #4a69bd 100%)',
                'color': 'white',
                'border-radius': '10px',
                'padding': '30px',
                'margin': '20px auto',
                'box-shadow': '0 12px 15px rgba(0, 0, 0, 0.15)',
                'position': 'relative',
                'z-index': '1',
                'overflow': 'hidden'
            }
        ),
    )
),


    dbc.Row(
    [
        dbc.Col(
            [
                html.H2("Informations sur les indices", className="info-title text-center mt-5 mb-4", style={'font-size': '2.5em', 'font-weight': 'bold', 'margin-bottom': '0'}),

                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.I(className="fas fa-chart-line", style={'font-size': '3em'}),
                                        html.H3("SP500", className="info-subtitle text-center", style={'font-size': '1.5em', 'font-weight': 'bold', 'margin-bottom': '0'}),
                                    ],
                                    className="info-header text-center",
                                    style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center', 'margin-bottom': '10px'}
                                ),
                                html.Div(
                                    [
                                        html.P(id='sp500-min', className="info-text", style={'font-size': '1.1em', 'margin-bottom': '5px', 'font-weight': 'bold'}),
                                        html.P(id='sp500-max', className="info-text", style={'font-size': '1.1em', 'margin-bottom': '5px', 'font-weight': 'bold'}),
                                        html.P(id='sp500-std', className="info-text", style={'font-size': '1.1em', 'margin-bottom': '5px', 'font-weight': 'bold'}),
                                        html.P(id='sp500-last', className="info-text", style={'font-size': '1.1em', 'margin-bottom': '5px', 'font-weight': 'bold'}),
                                        html.P(id='sp500-first', className="info-text", style={'font-size': '1.1em', 'margin-bottom': '5px', 'font-weight': 'bold'}),
                                    ],
                                    className="info-box text-center",
                                    style={'background-color': '#F2F3F4', 'border-radius': '10px', 'box-shadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'padding': '20px'}
                                ),
                            ],
                            className="mb-4", md=6
                        ),

                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.I(className="fas fa-chart-bar", style={'font-size': '3em'}),
                                        html.H3("NASDAQ", className="info-subtitle text-center", style={'font-size': '1.5em', 'font-weight': 'bold', 'margin-bottom': '0'}),
                                    ],
                                    className="info-header text-center",
                                    style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center', 'margin-bottom': '10px'}
                                ),
                                html.Div(
                                    [
                                        html.P(id='nasdaq-min', className="info-text", style={'font-size': '1.1em', 'margin-bottom': '5px', 'font-weight': 'bold'}),
                                        html.P(id='nasdaq-max', className="info-text", style={'font-size': '1.1em', 'margin-bottom': '5px', 'font-weight': 'bold'}),
                                        html.P(id='nasdaq-std', className="info-text", style={'font-size': '1.1em', 'margin-bottom': '5px', 'font-weight': 'bold'}),
                                        html.P(id='nasdaq-last', className="info-text", style={'font-size': '1.1em', 'margin-bottom': '5px', 'font-weight': 'bold'}),
                                        html.P(id='nasdaq-first', className="info-text", style={'font-size': '1.1em', 'margin-bottom': '5px', 'font-weight': 'bold'}),
                                    ],
                                    className="info-box text-center",
                                    style={'background-color': '#F2F3F4', 'border-radius': '10px', 'box-shadow': '0 4px 6px rgba(0, 0, 0, 0.1)', 'padding': '20px'}
                                ),
                            ],
                            className="mb-4", md=6
                        )
                    ],
                    className="info-container",
                    style={'width': '100%', 'display': 'flex', 'justify-content': 'space-evenly'}
                ),
            ],
        ),
    ],
),


    dbc.Row(
        [
            dbc.Col(
                dcc.Graph(
                    id='Cours Index S&P 500',
                    config={'displayModeBar': False},
                ),
                md=6,
            ),

            dbc.Col(
                dcc.Graph(
                    id='Cours Index NASDAQ',
                    config={'displayModeBar': False},
                ),
                md=6,
            ),
        ],
    ),

    dcc.Interval(
        id='interval-component',
        interval=60 * 1000,
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
Input('interval-component', 'n_intervals'))

def update_all_graphs(n):
	# Charger les nouvelles données depuis votre fichier CSV
	df = pd.read_csv("/home/ubuntu/Projet/Project/Generated_data/data.csv", delimiter=";")

	# Remplacer les valeurs manquantes par la valeur 0 dans la colonne SP500
	df['SP500'].dropna(inplace=True)

	# Calculer les statistiques pour le SP500
	sp500_min = round(min(df['SP500']), 2)
	sp500_max = round(max(df['SP500']), 2)
	sp500_mean = round(df['SP500'].mean(), 2)
	sp500_std = round(stats.stdev(df['SP500']), 2)
	sp500_last = round(df['SP500'].iloc[-1], 2)
	sp500_first = round(df['SP500'].iloc[0], 2)

        # Calculer les statistiques pour le NASDAQ
	nasdaq_min = round(min(df['NASDAQ']), 2)
	nasdaq_max = round(max(df['NASDAQ']), 2)
	nasdaq_mean = round(df['NASDAQ'].mean(), 2)
	nasdaq_std = round(stats.stdev(df['NASDAQ']), 2)
	nasdaq_last = round(df['NASDAQ'].iloc[-1], 2)
	nasdaq_first = round(df['NASDAQ'].iloc[0], 2)

	# Mettre à jour la figure du graphique SP500 avec les nouvelles données
	sp500_figure = {
        'data': [
        {'x': pd.to_datetime(df['date'], format='%Y-%m-%d-%H-%M'), 'y': df['SP500'], 'type': 'scatter', 'name': 'SP500', 'mode': 'lines+markers', 'line': {'shape': 'spline', 'smoothing': 1}},
        {'x': pd.to_datetime(df['date'], format='%Y-%m-%d-%H-%M'), 'y': df['SP500'], 'type': 'scatter', 'name': 'SP500 Aire', 'fill': 'tozeroy', 'mode': 'none', 'fillcolor': 'rgba(30, 136, 229, 0.3)'}
    	],
    	'layout': {
        'title': 'Evolution de l\'Idx S&P500',
        'xaxis': {'title': 'Date', 'range': [pd.Timestamp.now() - pd.Timedelta(hours=2), pd.Timestamp.now()]},
        'yaxis': {'title': 'Valeur', 'range': [sp500_mean - 3 * sp500_std, sp500_mean + 3 * sp500_std]},
        'autosize': True,
        'margin': {'l': 50, 'r': 50, 't': 50, 'b': 50},
        'plot_bgcolor': '#F3F3F3',
        'paper_bgcolor': '#F3F3F3',
    	'updatemenus': [
            go.layout.Updatemenu(
                buttons=list([
                    dict(
                        args=['xaxis.range', [pd.Timestamp.now() - pd.Timedelta(hours=24), pd.Timestamp.now()]],
                        label='Dernières 24h',
                        method='relayout'
                    ),
                    dict(
                        args=['xaxis.range', [pd.Timestamp.now() - pd.Timedelta(hours=72), pd.Timestamp.now()]],
                        label='Dernières 72h',
                        method='relayout'
                    ),
                    dict(
                        args=['xaxis.range', [pd.Timestamp.now() - pd.Timedelta(weeks=1), pd.Timestamp.now()]],
                        label='Dernière semaine',
                        method='relayout'
                    )
                ]),
                direction='down',
                showactive=True,
                type='buttons',
                x=0.1,
                xanchor='left',
                y=1.1,
                yanchor='top'
            )
        ]
	}
	}

	# Mettre à jour la figure du graphique NASDAQ avec les nouvelles données
	nasdaq_figure = {
        'data': [
        {'x': pd.to_datetime(df['date'], format='%Y-%m-%d-%H-%M'), 'y': df['NASDAQ'], 'type': 'scatter', 'name': 'NASDAQ', 'mode': 'lines+markers', 'line': {'shape': 'spline', 'smoothing': 1}},
        {'x': pd.to_datetime(df['date'], format='%Y-%m-%d-%H-%M'), 'y': df['NASDAQ'], 'type': 'scatter', 'name': 'NASDAQ Aire', 'fill': 'tozeroy', 'mode': 'none', 'fillcolor': 'rgba(30, 136, 229, 0.3)'}
    	],
    	'layout': {
        'title': 'Evolution de l\'Idx NASDAQ',
        'xaxis': {'title': 'Date', 'range': [pd.Timestamp.now() - pd.Timedelta(hours=2), pd.Timestamp.now()]},
        'yaxis': {'title': 'Valeur', 'range': [nasdaq_mean - 3 * nasdaq_std, nasdaq_mean + 3 * nasdaq_std]},
        'autosize': True,
        'margin': {'l': 50, 'r': 50, 't': 50, 'b': 50},
        'plot_bgcolor': '#F3F3F3',
        'paper_bgcolor': '#F3F3F3',
    	'updatemenus': [
            go.layout.Updatemenu(
                buttons=list([
                    dict(
                        args=['xaxis.range', [pd.Timestamp.now() - pd.Timedelta(hours=24), pd.Timestamp.now()]],
                        label='Dernières 24h',
                        method='relayout'
                    ),
                    dict(
                        args=['xaxis.range', [pd.Timestamp.now() - pd.Timedelta(hours=72), pd.Timestamp.now()]],
                        label='Dernières 72h',
                        method='relayout'
                    ),
                    dict(
                        args=['xaxis.range', [pd.Timestamp.now() - pd.Timedelta(weeks=1), pd.Timestamp.now()]],
                        label='Dernière semaine',
                        method='relayout'
                    )
                ]),
                direction='down',
                showactive=True,
                type='buttons',
                x=0.1,
                xanchor='left',
                y=1.1,
                yanchor='top'
            )
        ]
	}
	}

	# Retourner toutes les valeurs mises à jour
	return [sp500_figure, nasdaq_figure, f"Min: {sp500_min}", f"Max: {sp500_max}", f"Std: {sp500_std}", f"Dernière: {sp500_last}", f"Première: {sp500_first}", f"Min: {nasdaq_min}", f"Max: {nasdaq_max}", f"Std: {nasdaq_std}", f"Dernière: {nasdaq_last}", f"Première: {nasdaq_first}"]

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
    time.sleep(60)
