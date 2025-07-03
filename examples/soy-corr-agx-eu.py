#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script per Soybean - Modello 1 con stima di variabilità:
Prevede il Prezzo medio annuo (€) a partire dalla Produzione media annua (t)
utilizzando dati di produzione UE (AgriDataService) e prezzi italiani (API agx.sh).
Inoltre calcola l'intervallo di previsione (prediction interval) al 95%.
"""
import requests
from agridata.service import AgriDataService
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# Configurazione API agx.sh
BASE_URL = "https://api.agx.sh/v1/ohlc"
SYMBOL = "SSN"
BUCKET = "1Y"
STATE = "IT"


def fetch_agx_yearly_prices(symbol=SYMBOL, bucket=BUCKET, state=STATE):
    params = {'symbol': symbol, 'bucket': bucket, 'stateCode': state}
    resp = requests.get(BASE_URL, params=params)
    resp.raise_for_status()
    df = pd.DataFrame(resp.json().get('ohlc', []))
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['year'] = df['timestamp'].dt.year
    return (
        df.groupby('year', as_index=False)
          .agg(price_mean=('close', 'mean'))
          .sort_values('year')
    )


def fetch_annual_production():
    service = AgriDataService()
    raw = service.oilseeds.get_production(crops="Soybean")
    df = pd.json_normalize(raw)
    df = df[df['crop'] == 'Soybean'].astype({'year': int, 'grossProduction': float})
    df = df[df['grossProduction'] > 0]
    return (
        df.groupby('year', as_index=False)
          .agg(production_mean=('grossProduction', 'mean'))
          .sort_values('year')
    )


def train_model():
    df_prod = fetch_annual_production()
    df_price = fetch_agx_yearly_prices()
    df = pd.merge(df_prod, df_price, on='year', how='inner')
    X = sm.add_constant(df['production_mean'])
    y = df['price_mean']
    model = sm.OLS(y, X).fit()
    df['pred'] = model.predict(X)
    # prediction interval
    pred = model.get_prediction(X)
    df_pi = pred.summary_frame(alpha=0.05)
    df['pi_lower'] = df_pi['obs_ci_lower']
    df['pi_upper'] = df_pi['obs_ci_upper']
    return model, df


def predict_price_with_interval(model, production_value):
    """
    Prevede il prezzo medio annuo (€) dato un valore di produzione media (t),
    restituendo anche l'intervallo di previsione al 95%.
    """
    # Allinea l'exog al modello originale
    exog_names = model.model.exog_names  # es. ['const','production_mean']
    # Crea nuova riga con costante e produzione
    X_new = pd.DataFrame([{exog_names[0]: 1.0, exog_names[1]: production_value}])
    # Ottieni predizione con intervallo di previsione
    pred = model.get_prediction(X_new)
    summary = pred.summary_frame(alpha=0.05)
    mean      = summary['mean'].iloc[0]
    lower_obs = summary['obs_ci_lower'].iloc[0]
    upper_obs = summary['obs_ci_upper'].iloc[0]
    return mean, lower_obs, upper_obs


def main():
    model, df = train_model()

    # Statistiche e formula
    print(model.summary())
    intercept, slope = model.params['const'], model.params['production_mean']
    print(f"Formula retta: prezzo = {intercept:.2f} + {slope:.2f} * produzione")

    # Plot con prediction interval a due livelli
    df_sorted = df.sort_values('production_mean')
    plt.figure(figsize=(8,6))
    plt.scatter(df['production_mean'], df['price_mean'], label='Dati osservati')
    plt.plot(df_sorted['production_mean'], df_sorted['pred'], 'r--', label=f'Fit (R²={model.rsquared:.2f})')

    # Intervallo di confidenza 95%
    pred_95 = model.get_prediction(sm.add_constant(df_sorted['production_mean']))
    ci95 = pred_95.summary_frame(alpha=0.05)[['mean_ci_lower','mean_ci_upper']]
    plt.fill_between(
        df_sorted['production_mean'],
        ci95['mean_ci_lower'],
        ci95['mean_ci_upper'],
        color='r', alpha=0.2,
        label='95% CI'
    )
    # Intervallo di confidenza 60%
    pred_60 = model.get_prediction(sm.add_constant(df_sorted['production_mean']))
    ci60 = pred_60.summary_frame(alpha=0.40)[['mean_ci_lower','mean_ci_upper']]
    plt.fill_between(
        df_sorted['production_mean'],
        ci60['mean_ci_lower'],
        ci60['mean_ci_upper'],
        color='r', alpha=0.4,
        label='60% CI'
    )

    plt.xlabel('Produzione media annua (t)')
    plt.ylabel('Prezzo medio annuo (€)')
    plt.title('Modello lineare: Prezzo ~ Produzione con variabilità')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Esempio previsione con intervallo
    example_prod = df['production_mean'].mean()
    mean, lower, upper = predict_price_with_interval(model, example_prod)
    print(f"Per produzione={example_prod:.1f} t, prezzo previsto = {mean:.2f} €")
    print(f"95% Prediction Interval: [{lower:.2f}, {upper:.2f}] €")

if __name__ == '__main__':
    main()
