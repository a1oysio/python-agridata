#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script per Soybean:
- Costruisce e confronta modelli di regressione lineare per prevedere il Prezzo medio annuo (UE)
  1) Modello 1: Prezzo ~ Produzione media annua
  2) Modello 2: Prezzo ~ Produzione media annua + Superficie media annua
  3) Modello 3: Prezzo ~ Produzione media annua + Superficie media annua + Resa media annua
- Visualizza i fit dei tre modelli in un'unica figura e riporta statistiche (R²)

Se `stateCode` è None prende dati di tutti i paesi, altrimenti filtra per Stato specificato.
"""

from agridata.service import AgriDataService
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def main():
    # Configurazione
    stateCode = None  # 'IT' per Italia, None per tutti i paesi
    service = AgriDataService()

    # 1) Carica e prepara dati
    prod_kwargs = {'crops': 'Soybean'}
    if stateCode:
        prod_kwargs['memberStateCodes'] = stateCode
    raw_prod = service.oilseeds.get_production(**prod_kwargs)
    df_prod = pd.json_normalize(raw_prod)
    df_prod = df_prod[df_prod['crop'] == 'Soybean']
    df_prod = df_prod.astype({'year': int, 'grossProduction': float, 'area': float, 'yield': float})
    df_prod = df_prod[(df_prod['grossProduction'] > 0) & (df_prod['area'] > 0)]

    # Calcola medie annuali
    annual = df_prod.groupby('year', as_index=False).agg(
        production_mean=('grossProduction', 'mean'),
        area_mean=('area', 'mean'),
        yield_mean=('yield', 'mean')
    ).sort_values('year')

    price_kwargs = {'products': 'Soya beans'}
    if stateCode:
        price_kwargs['memberStateCodes'] = stateCode
    raw_price = service.oilseeds.get_prices(**price_kwargs)
    df_price = pd.json_normalize(raw_price)
    df_price = df_price[df_price['product'] == 'Soya beans']
    df_price['beginDate'] = pd.to_datetime(df_price['beginDate'], format="%d/%m/%Y")
    df_price['year'] = df_price['beginDate'].dt.year
    df_price['price'] = df_price['price']\
        .str.replace('[^0-9,\.]', '', regex=True)\
        .str.replace(',', '.', regex=False)\
        .astype(float)
    df_price = df_price[df_price['price'] > 0]

    annual_price = df_price.groupby('year', as_index=False).agg(
        price_mean=('price', 'mean')
    ).sort_values('year')

    # Unione dati
    df = pd.merge(annual, annual_price, on='year', how='inner')

    # Variabili esplicative e dipendente
    X1 = df[['production_mean']]
    X2 = df[['production_mean', 'area_mean']]
    X3 = df[['production_mean', 'area_mean', 'yield_mean']]
    y = df['price_mean']

    # Aggiungi intercept
    X1_sm = sm.add_constant(X1)
    X2_sm = sm.add_constant(X2)
    X3_sm = sm.add_constant(X3)

    # Stima modelli
    model1 = sm.OLS(y, X1_sm).fit()
    model2 = sm.OLS(y, X2_sm).fit()
    model3 = sm.OLS(y, X3_sm).fit()

    # Previsioni
    df['pred1'] = model1.predict(X1_sm)
    df['pred2'] = model2.predict(X2_sm)
    df['pred3'] = model3.predict(X3_sm)

    # Plots
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    years = df['year']

    # Modello 1
    axes[0].plot(years, y, 'o-', label='Osservato')
    axes[0].plot(years, df['pred1'], '--', label=f'Predetto (R²={model1.rsquared:.2f})')
    axes[0].set_title('Modello 1: Prezzo ~ Produzione')
    axes[0].set_xlabel('Anno')
    axes[0].set_ylabel('Prezzo medio (€)')
    axes[0].legend()

    # Modello 2
    axes[1].plot(years, y, 'o-', label='Osservato')
    axes[1].plot(years, df['pred2'], '--', label=f'Predetto (R²={model2.rsquared:.2f})')
    axes[1].set_title('Modello 2: Prezzo ~ Produzione + Area')
    axes[1].set_xlabel('Anno')
    axes[1].legend()

    # Modello 3
    axes[2].plot(years, y, 'o-', label='Osservato')
    axes[2].plot(years, df['pred3'], '--', label=f'Predetto (R²={model3.rsquared:.2f})')
    axes[2].set_title('Modello 3: Prezzo ~ Prod + Area + Resa')
    axes[2].set_xlabel('Anno')
    axes[2].legend()

    fig.suptitle('Confronto tra modelli di regressione')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

    # Statistiche
    print("--- Sommario Modelli ---")
    print("Modello 1:\n", model1.summary())
    print("Modello 2:\n", model2.summary())
    print("Modello 3:\n", model3.summary())

if __name__ == '__main__':
    main()
