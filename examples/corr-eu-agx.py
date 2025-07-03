#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script per Soybean:
- Utilizza produzione media annua UE da AgriDataService
- Recupera prezzi annuali di soia dall'API agx.sh (Italia) per simbolo SSN e bucket 1Y
- Costruisce e confronta modelli di regressione lineare per prevedere il Prezzo medio annuo
  1) Modello 1: Prezzo ~ Produzione media annua
  2) Modello 2: Prezzo ~ Produzione media annua + Superficie media annua
  3) Modello 3: Prezzo ~ Produzione media annua + Superficie media annua + Resa media annua
- Visualizza i fit dei tre modelli e mostra le statistiche di R²
"""

import requests
from agridata.service import AgriDataService
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# AGX.sh API configuration
BASE_URL = "https://api.agx.sh/v1/ohlc"
SYMBOL = "SSN"
BUCKET = "1Y"
STATE = "IT"


def fetch_agx_yearly_prices(symbol=SYMBOL, bucket=BUCKET, state=STATE):
    """
    Chiama l'API agx.sh e restituisce un DataFrame con prezzo medio annuo (close) per ogni anno.
    """
    params = { 'symbol': symbol, 'bucket': bucket }
    resp = requests.get(BASE_URL, params=params)
    resp.raise_for_status()
    data = resp.json()
    df = pd.DataFrame(data.get('ohlc', []))
    if df.empty:
        raise ValueError("Nessun dato OHLC restituito dall'API agx.sh")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['year'] = df['timestamp'].dt.year
    # Calcola prezzo medio annuo sul campo 'close'
    annual_price = (
        df.groupby('year', as_index=False)
          .agg(price_mean=('close', 'mean'))
          .sort_values('year')
    )
    return annual_price


def main():
    # 1) Recupera dati di produzione da AgriDataService (UE aggregata)
    service = AgriDataService()
    raw = service.oilseeds.get_production(crops="Soybean", memberStateCodes="IT")
    df_prod = pd.json_normalize(raw)
    df_prod = df_prod[df_prod['crop']=='Soybean'].astype({
        'year': int,
        'grossProduction': float,
        'area': float,
        'yield': float
    })
    df_prod = df_prod[(df_prod['grossProduction']>0) & (df_prod['area']>0)]
    annual_prod = (
        df_prod.groupby('year', as_index=False)
               .agg(
                   production_mean=('grossProduction','mean'),
                   area_mean=('area','mean'),
                   yield_mean=('yield','mean')
               )
               .sort_values('year')
    )

    # 2) Recupera prezzi annuali da agx.sh (Italia)
    annual_price = fetch_agx_yearly_prices()

    # 3) Unisci produzione e prezzi per anno
    df = pd.merge(annual_prod, annual_price, on='year', how='inner')

    # 4) Prepara variabili per modelli
    y = df['price_mean']
    X1 = sm.add_constant(df[['production_mean']])
    X2 = sm.add_constant(df[['production_mean','area_mean']])
    X3 = sm.add_constant(df[['production_mean','area_mean','yield_mean']])

    # 5) Stima modelli OLS
    m1 = sm.OLS(y, X1).fit()
    m2 = sm.OLS(y, X2).fit()
    m3 = sm.OLS(y, X3).fit()

    # 6) Previsioni
    df['pred1'] = m1.predict(X1)
    df['pred2'] = m2.predict(X2)
    df['pred3'] = m3.predict(X3)

    # 7) Plot dei tre modelli
    years = df['year']
    fig, ax = plt.subplots(1,1, figsize=(8,6))
    ax.plot(years, y, 'o-', label='Osservato')
    ax.plot(years, df['pred1'], '--', label=f'Mod1 R²={m1.rsquared:.2f}')
    ax.plot(years, df['pred2'], '-.', label=f'Mod2 R²={m2.rsquared:.2f}')
    ax.plot(years, df['pred3'], ':', label=f'Mod3 R²={m3.rsquared:.2f}')
    ax.set_title('Confronto modelli regressione')
    ax.set_xlabel('Anno')
    ax.set_ylabel('Prezzo medio annuo (€)')
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # 8) Stampa sommario
    print("--- Sommario Modelli OLS ---")
    print("Modello 1: Prezzo ~ Produzione")
    print(m1.summary())
    print("\nModello 2: Prezzo ~ Produzione + Area")
    print(m2.summary())
    print("\nModello 3: Prezzo ~ Produzione + Area + Resa")
    print(m3.summary())

if __name__ == '__main__':
    main()
