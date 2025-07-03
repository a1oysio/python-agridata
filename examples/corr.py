#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script per Soybean:
- Grafico di correlazione tra Produzione media annua per paese e Prezzo medio annuo
- Test di significatività (p-value) della correlazione

Con `stateCode = None` prende dati di tutti i paesi e calcola la media anziché la somma.
"""

from agridata.service import AgriDataService
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, linregress
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def main():
    # ----------------------------
    # Configurazione iniziale
    # ----------------------------
    # None per tutti i paesi
    stateCode = None
    service = AgriDataService()

    # -------------------------------------------------------------------------
    # 1) PRODUZIONE MEDIA ANNUA PER PAESE
    # -------------------------------------------------------------------------
    prod_kwargs = {}
    if stateCode is not None:
        prod_kwargs['memberStateCodes'] = stateCode

    raw_prod = service.oilseeds.get_production(crops="Soybean", **prod_kwargs)
    df_prod = pd.json_normalize(raw_prod).astype({
        'year': 'int',
        'grossProduction': 'float'
    })
    # Filtra righe con produzione valida
    df_prod = df_prod[df_prod['grossProduction'] > 0]

    # Calcola produzione media per paese per anno
    annual_prod = (
        df_prod
        .groupby('year', as_index=False)
        .agg(production_mean=('grossProduction', 'mean'))
        .sort_values('year')
    )

    # -------------------------------------------------------------------------
    # 2) PREZZO MEDIO ANNUO
    # -------------------------------------------------------------------------
    price_kwargs = {}
    if stateCode is not None:
        price_kwargs['memberStateCodes'] = stateCode

    raw_price = service.oilseeds.get_prices(products="Soya beans", **price_kwargs)
    df_price = pd.json_normalize(raw_price)
    df_price['beginDate'] = pd.to_datetime(df_price['beginDate'], format="%d/%m/%Y")
    df_price['price'] = (
        df_price['price']
        .str.replace('[^0-9,\\.]','', regex=True)
        .str.replace(',','.')
        .astype(float)
    )
    df_price['year'] = df_price['beginDate'].dt.year

    annual_price = (
        df_price
        .groupby('year', as_index=False)
        .agg(price_mean=('price', 'mean'))
        .sort_values('year')
    )

    # -------------------------------------------------------------------------
    # 3) UNIONE E CALCOLO CORRELAZIONE + P-VALUE
    # -------------------------------------------------------------------------
    df = pd.merge(annual_prod, annual_price, on='year', how='inner')
    x = df['production_mean']
    y = df['price_mean']

    r, p_value = pearsonr(x, y)
    lr = linregress(x, y)
    slope, intercept = lr.slope, lr.intercept

    # -------------------------------------------------------------------------
    # 4) PLOT
    # -------------------------------------------------------------------------
    plt.figure(figsize=(8,6))
    plt.scatter(x, y, s=50, alpha=0.7)
    x_vals = np.array([x.min(), x.max()])
    plt.plot(x_vals, intercept + slope * x_vals,
             linestyle='--', linewidth=1)

    plt.xlabel('Produzione media annua per paese (t)')
    plt.ylabel('Prezzo medio annuo (€)')
    plt.title(
        f"Correlazione Prod. media – Prezzo (r = {r:.2f}, p = {p_value:.3f})\n"
        f"Soybean (Tutti gli stati)"
    )
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # -------------------------------------------------------------------------
    # 5) Output test statistico
    # -------------------------------------------------------------------------
    print(f"Coefficiente di correlazione Pearson: r = {r:.4f}")
    print(f"P-value associato: p = {p_value:.4f}")
    if p_value < 0.05:
        print("La correlazione è statisticamente significativa (p < 0.05).")
    else:
        print("La correlazione NON è statisticamente significativa (p ≥ 0.05).")

if __name__ == "__main__":
    main()
