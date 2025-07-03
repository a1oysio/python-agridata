#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script completo per Soybean in un dato Stato membro:
A) Z-score progressivo di produzione, area e resa.
B) Prezzo medio annuo con banda Min–Max.
C) Grafico combinato (produzione, area e prezzo) sugli anni condivisi con banda Min–Max.
D) Tabella delle entrate minime, medie e massime per ettaro per anno,
   calcolate come resa (t/ha) × prezzo (€/t).
"""

from agridata.service import AgriDataService
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def main():
    # ----------------------------
    # Configurazione iniziale
    # ----------------------------
    stateCode = "IT"  # Cambia per un altro Stato (es. "FR", "DE", ...)
    service   = AgriDataService()

    # -------------------------------------------------------------------------
    # A) Z-SCORE PROGRESSIVO di Produzione, Area e Resa
    # -------------------------------------------------------------------------
    raw_prod = service.oilseeds.get_production(
        memberStateCodes=stateCode, crops="Soybean"
    )
    df_prod = pd.json_normalize(raw_prod).astype({
        'year': 'int',
        'grossProduction': 'float',
        'area': 'float',
        'yield': 'float'
    })

    annual_prod = (
        df_prod
        .groupby('year', as_index=False)
        .mean(numeric_only=True)
        .sort_values('year')
    )

    z = annual_prod.copy()
    for col in ['grossProduction','area','yield']:
        mu    = annual_prod[col].expanding(min_periods=1).mean()
        sigma = annual_prod[col].expanding(min_periods=1).std(ddof=0)
        z[col] = (annual_prod[col] - mu) / sigma
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
            label=f"{col} (z-score prog.)"
        )
    plt.xlabel('Anno')
    plt.ylabel('Z-score progressivo')
    plt.title(f"Z-score prog. di Produzione, Area e Resa di Soybean ({stateCode})")
    plt.legend(loc='upper left')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # -------------------------------------------------------------------------
    # B) PREZZO MEDIO ANNUO con banda Min–Max
    # -------------------------------------------------------------------------
    raw_price = service.oilseeds.get_prices(
        memberStateCodes=stateCode, products="Soya beans"
    )
    df_price = pd.json_normalize(raw_price)
    df_price['beginDate'] = pd.to_datetime(df_price['beginDate'], format="%d/%m/%Y")
    df_price['price'] = (
        df_price['price']
        .str.replace('[^0-9,\\.]','',regex=True)
        .str.replace(',','.')
        .astype(float)
    )
    df_price['year'] = df_price['beginDate'].dt.year

    annual_price = (
        df_price
        .groupby('year', as_index=False)
        .agg(price_mean=('price','mean'),
             price_min =('price','min'),
             price_max =('price','max'))
        .sort_values('year')
    )

    plt.figure(figsize=(10, 6))
    x  = annual_price['year']
    m  = annual_price['price_mean']
    mn = annual_price['price_min']
    mx = annual_price['price_max']

    plt.plot(x, m, color='tab:orange', marker='o', label='Prezzo medio')
    plt.fill_between(x, mn, mx,
                     color='tab:orange', alpha=0.2,
                     label='Min–Max annuale')
    plt.xlabel('Anno')
    plt.ylabel('Prezzo (€)')
    plt.title(f"Prezzo medio annuo di Soybean ({stateCode})\ncon banda Min–Max")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # -------------------------------------------------------------------------
    # C) GRAFICO COMBINATO su anni condivisi con banda Min–Max
    # -------------------------------------------------------------------------
    combined = pd.merge(
        annual_prod,
        annual_price[['year','price_mean','price_min','price_max']],
        on='year', how='inner'
    )

    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.bar(combined['year']-0.2,
            combined['grossProduction'],
            width=0.4, alpha=0.7,
            label='Produzione (t)', color='tab:blue')
    ax1.bar(combined['year']+0.2,
            combined['area'],
            width=0.4, alpha=0.5,
            label='Area (ha)', color='tab:green')
    ax1.set_xlabel('Anno')
    ax1.set_ylabel('Produzione/Area', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    ax2 = ax1.twinx()
    ax2.plot(combined['year'], combined['price_mean'],
             marker='o', linestyle='-', color='tab:orange',
             label='Prezzo medio (€)')
    ax2.fill_between(combined['year'],
                     combined['price_min'],
                     combined['price_max'],
                     color='tab:orange', alpha=0.2,
                     label='Min–Max prezzo')
    ax2.set_ylabel('Prezzo (€)', color='tab:orange')
    ax2.tick_params(axis='y', labelcolor='tab:orange')

    l1, l1l = ax1.get_legend_handles_labels()
    l2, l2l = ax2.get_legend_handles_labels()
    ax1.legend(l1+l2, l1l+l2l, loc='upper left')

    plt.title(f"Produzione, Area e Prezzo di Soybean ({stateCode})\n(anni condivisi)")
    fig.tight_layout()
    plt.show()

    # -------------------------------------------------------------------------
    # D) TABELLA ENTRATE per ettaro per anno (yield × price)
    # -------------------------------------------------------------------------
    combined['revenue_min']  = combined['yield'] * combined['price_min']
    combined['revenue_mean'] = combined['yield'] * combined['price_mean']
    combined['revenue_max']  = combined['yield'] * combined['price_max']

    revenue_table = combined[[
        'year',
        'price_min','price_mean','price_max', 'yield',
        'revenue_min','revenue_mean','revenue_max'
    ]].reset_index(drop=True)

    print("\nEntrate per ettaro per anno (€/ha):")
    print(revenue_table.to_string(index=False, float_format="{:.2f}".format))


if __name__ == "__main__":
    main()
