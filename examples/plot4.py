#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1) Estrae produzione, area e resa per 'Soybean' in Italia e
   calcola lo z-score progressivo (expanding).
2) Mostra un grafico separato con il prezzo medio annuo di 'Soybean'.
"""

from agridata.service import AgriDataService             # API Agri-food Data Portal :contentReference[oaicite:3]{index=3}
import pandas as pd                                      # Data processing e expanding :contentReference[oaicite:4]{index=4}
import matplotlib.pyplot as plt                          # Plotting :contentReference[oaicite:5]{index=5}
from scipy.stats import zscore                           # z-score standard :contentReference[oaicite:6]{index=6}

def main():
    service = AgriDataService()

    # --- PARTE A: Z-SCORE PROGRESSIVO ---
    raw_prod = service.oilseeds.get_production(
        memberStateCodes="IT", crops="Soybean"
    )  # /api/oilseeds/production :contentReference[oaicite:7]{index=7}

    df = pd.json_normalize(raw_prod)
    df = df.astype({
        'year': 'int',
        'grossProduction': 'float',
        'area': 'float',
        'yield': 'float'
    })

    annual = (df.groupby('year', as_index=False)
                .agg({
                    'grossProduction':'mean',
                    'area':'mean',
                    'yield':'mean'
                })
                .sort_values('year'))

    # Expanding mean e std (population)  
    z = annual.copy()
    for col in ['grossProduction','area','yield']:
        mu    = annual[col].expanding(min_periods=1).mean()
        sigma = annual[col].expanding(min_periods=1).std(ddof=0)
        z[col] = (annual[col] - mu) / sigma
        # correzione con .loc per evitare warnings
        z.loc[0, col] = 0

    plt.figure(figsize=(10, 6))
    styles = {
        'grossProduction':('o','-','tab:blue'),
        'area':           ('s','--','tab:green'),
        'yield':          ('^','-.','tab:red')
    }
    for col,(mk,ls,clr) in styles.items():
        plt.plot(
            z['year'], z[col],
            marker=mk, linestyle=ls, color=clr,
            label=f"{col} (z-score progressivo)"
        )
    plt.xlabel('Anno')
    plt.ylabel('Z-score progressivo')
    plt.title('Z-score progressivo di Produzione, Area e Resa di Soybean in Italia')
    plt.legend(loc='upper left')  # legenda combinata :contentReference[oaicite:8]{index=8}
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # --- PARTE B: GRAFICO PREZZI STORICI ---
    prices_raw = service.oilseeds.get_prices(
        memberStateCodes="IT",
        products="Soya beans"
    )  # /api/oilseeds/prices :contentReference[oaicite:9]{index=9}

    df_prices = pd.json_normalize(prices_raw)
    df_prices['beginDate'] = pd.to_datetime(df_prices['beginDate'], format="%d/%m/%Y")
    # pulizia e conversione dei prezzi
    df_prices['price'] = (
        df_prices['price']
        .str.replace('[^0-9,\\.]', '', regex=True)
        .str.replace(',', '.')
        .astype(float)
    )
    df_prices['year'] = df_prices['beginDate'].dt.year

    annual_price = (
        df_prices
        .groupby('year', as_index=False)['price']
        .mean(numeric_only=True)  # esclude colonne non numeriche :contentReference[oaicite:10]{index=10}
        .sort_values('year')
    )

    plt.figure(figsize=(10, 5))
    plt.plot(
        annual_price['year'],
        annual_price['price'],
        marker='o', linestyle='-',
        color='tab:orange',
        label='Prezzo medio annuo (€ per T)'
    )
    plt.xlabel('Anno')
    plt.ylabel('Prezzo medio (€)')
    plt.title('Prezzo medio annuo di Soya beans in Italia')
    plt.legend()  # posiziona legenda automaticamente :contentReference[oaicite:11]{index=11}
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
