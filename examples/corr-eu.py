#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script per Soybean:
- Grafici di correlazione tra Produzione media annua (UE), Superficie media annua (UE), Resa media annua (UE) e Prezzo medio annuo (UE)
- Test di significatività (p-value) della correlazione per tutte le variabili

Se `stateCode` è None prende dati di tutti i paesi, altrimenti filtra per Stato specificato.
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
    stateCode = None  # 'IT' per Italia, None per tutti i paesi
    service = AgriDataService()

    # -------------------------------------------------------------------------
    # 1) CARICA E FILTRA DATI PRODUZIONE
    # -------------------------------------------------------------------------
    prod_kwargs = {'crops': 'Soybean'}
    if stateCode:
        prod_kwargs['memberStateCodes'] = stateCode
    raw_prod = service.oilseeds.get_production(**prod_kwargs)
    df_prod = pd.json_normalize(raw_prod)
    df_prod = df_prod[df_prod['crop'] == 'Soybean']
    df_prod = df_prod.astype({
        'year': 'int',
        'grossProduction': 'float',
        'area': 'float',
        'yield': 'float'
    })
    df_prod = df_prod[(df_prod['grossProduction'] > 0) & (df_prod['area'] > 0)]

    # Calcola media annua di produzione (t), superficie (ha) e resa (t/ha)
    annual = (
        df_prod
        .groupby('year', as_index=False)
        .agg(
            production_mean=('grossProduction', 'mean'),
            area_mean=('area', 'mean'),
            yield_mean=('yield', 'mean')
        )
        .sort_values('year')
    )

    # -------------------------------------------------------------------------
    # 2) CARICA E FILTRA DATI PREZZO
    # -------------------------------------------------------------------------
    price_kwargs = {'products': 'Soya beans'}
    if stateCode:
        price_kwargs['memberStateCodes'] = stateCode
    raw_price = service.oilseeds.get_prices(**price_kwargs)
    df_price = pd.json_normalize(raw_price)
    df_price = df_price[df_price['product'] == 'Soya beans']
    df_price['beginDate'] = pd.to_datetime(df_price['beginDate'], format="%d/%m/%Y")
    df_price['year'] = df_price['beginDate'].dt.year
    df_price['price'] = (
        df_price['price']
        .str.replace('[^0-9,\.]', '', regex=True)
        .str.replace(',', '.', regex=False)
        .astype(float)
    )
    df_price = df_price[df_price['price'] > 0]

    annual_price = (
        df_price
        .groupby('year', as_index=False)
        .agg(price_mean=('price', 'mean'))
        .sort_values('year')
    )

    # -------------------------------------------------------------------------
    # 3) UNISCI DATI
    # -------------------------------------------------------------------------
    df = pd.merge(annual, annual_price, on='year', how='inner')

    # Variabili per correlazioni
    x_prod = df['production_mean']
    x_area = df['area_mean']
    x_yield = df['yield_mean']
    y_price = df['price_mean']

    # Calcoli statistici
    r_prod, p_prod = pearsonr(x_prod, y_price)
    lr_prod = linregress(x_prod, y_price)
    r_area, p_area = pearsonr(x_area, y_price)
    lr_area = linregress(x_area, y_price)
    r_yield, p_yield = pearsonr(x_yield, y_price)
    lr_yield = linregress(x_yield, y_price)

    # -------------------------------------------------------------------------
    # 4) PLOT TRIPLO IN UN'UNICA FINESTRA
    # -------------------------------------------------------------------------
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18,6))

    # Scatter produzione vs prezzo
    axes[0].scatter(x_prod, y_price, s=60, alpha=0.7)
    x_vals = np.array([x_prod.min(), x_prod.max()])
    axes[0].plot(x_vals, lr_prod.intercept + lr_prod.slope * x_vals,
                 linestyle='--', linewidth=1)
    axes[0].set_xlabel('Produzione media annua (t)')
    axes[0].set_ylabel('Prezzo medio annuo (€)')
    axes[0].set_title(f"Prod–Prezzo: r={r_prod:.2f}, p={p_prod:.3f}")
    axes[0].grid(alpha=0.3)

    # Scatter superficie vs prezzo
    axes[1].scatter(x_area, y_price, s=60, alpha=0.7)
    x_vals2 = np.array([x_area.min(), x_area.max()])
    axes[1].plot(x_vals2, lr_area.intercept + lr_area.slope * x_vals2,
                 linestyle='--', linewidth=1)
    axes[1].set_xlabel('Superficie media annua (ha)')
    axes[1].set_ylabel('Prezzo medio annuo (€)')
    axes[1].set_title(f"Area–Prezzo: r={r_area:.2f}, p={p_area:.3f}")
    axes[1].grid(alpha=0.3)

    # Scatter resa vs prezzo
    axes[2].scatter(x_yield, y_price, s=60, alpha=0.7)
    x_vals3 = np.array([x_yield.min(), x_yield.max()])
    axes[2].plot(x_vals3, lr_yield.intercept + lr_yield.slope * x_vals3,
                 linestyle='--', linewidth=1)
    axes[2].set_xlabel('Resa media annua (t/ha)')
    axes[2].set_ylabel('Prezzo medio annuo (€)')
    axes[2].set_title(f"Resa–Prezzo: r={r_yield:.2f}, p={p_yield:.3f}")
    axes[2].grid(alpha=0.3)

    fig.suptitle('Correlazioni con il Prezzo (€)')
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    plt.show()

    # -------------------------------------------------------------------------
    # 5) OUTPUT STATISTICHE
    # -------------------------------------------------------------------------
    print(f"Anni considerati: {len(df)}")
    print(f"Produzione–Prezzo: r = {r_prod:.4f}, p = {p_prod:.4f}")
    print(f"Area–Prezzo:       r = {r_area:.4f}, p = {p_area:.4f}")
    print(f"Resa–Prezzo:       r = {r_yield:.4f}, p = {p_yield:.4f}")
    print("--- Interpretazione ---")
    print("Produzione significativa" if p_prod<0.05 else "Produzione non significativa")
    print("Area significativa" if p_area<0.05 else "Area non significativa")
    print("Resa significativa" if p_yield<0.05 else "Resa non significativa")

if __name__ == "__main__":
    main()
