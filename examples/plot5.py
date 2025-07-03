#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script completo per Soybean in un dato Stato membro:
A) Z-score progressivo di produzione, area e resa.
B) Prezzo medio annuo con banda ±1 deviazione standard progressiva.
C) Grafico combinato (produzione, area e prezzo) sugli anni condivisi.
"""

from agridata.service import AgriDataService
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import zscore
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def main():
    # Variabile per Stato membro
    stateCode = "IT"  # Cambia qui per un altro Stato (es. "FR", "DE", ecc.)

    service = AgriDataService()

    # -------------------------------------------------------------------------
    # A) Z-SCORE PROGRESSIVO di produzione, area e resa
    # -------------------------------------------------------------------------
    raw_prod = service.oilseeds.get_production(
        memberStateCodes=stateCode,
        crops="Soybean"
    )
    df_prod = pd.json_normalize(raw_prod).astype({
        'year': 'int',
        'grossProduction': 'float',
        'area': 'float',
        'yield': 'float'
    })
    annual = (
        df_prod
        .groupby('year', as_index=False)
        .agg({
            'grossProduction': 'mean',
            'area':            'mean',
            'yield':           'mean'
        })
        .sort_values('year')
    )

    z = annual.copy()
    for col in ['grossProduction', 'area', 'yield']:
        mu    = annual[col].expanding(min_periods=1).mean()
        sigma = annual[col].expanding(min_periods=1).std(ddof=0)
        z[col] = (annual[col] - mu) / sigma
        # assegna zero al primo anno senza warning
        z.loc[0, col] = 0

    plt.figure(figsize=(10, 6))
    styles = {
        'grossProduction': ('o', '-', 'tab:blue'),
        'area':            ('s', '--','tab:green'),
        'yield':           ('^','-.','tab:red')
    }
    for col, (mk, ls, clr) in styles.items():
        plt.plot(
            z['year'], z[col],
            marker=mk, linestyle=ls, color=clr,
            label=f"{col} (z-score prog.)"
        )
    plt.xlabel('Anno')
    plt.ylabel('Z-score progressivo')
    plt.title(f"Z-score progressivo di Produzione, Area e Resa di Soybean ({stateCode})")
    plt.legend(loc='upper left')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # -------------------------------------------------------------------------
    # B) PREZZO MEDIO ANNUO con banda ±1 std progressiva
    # -------------------------------------------------------------------------
    prices_raw = service.oilseeds.get_prices(
        memberStateCodes=stateCode,
        products="Soya beans"
    )
    df_prices = pd.json_normalize(prices_raw)
    df_prices['beginDate'] = pd.to_datetime(df_prices['beginDate'], format="%d/%m/%Y")
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
        .mean(numeric_only=True)
        .sort_values('year')
    )
    annual_price['mean_prog'] = annual_price['price'].expanding(min_periods=1).mean()
    annual_price['std_prog']  = annual_price['price'].expanding(min_periods=1).std(ddof=0)

    plt.figure(figsize=(10, 6))
    x = annual_price['year']
    m = annual_price['mean_prog']
    s = annual_price['std_prog']

    plt.plot(x, m, color='tab:orange', marker='o', label='Mean prog.')
    plt.fill_between(x, m - s, m + s,
                     color='tab:orange', alpha=0.2,
                     label='±1 std prog.')

    plt.xlabel('Anno')
    plt.ylabel('Prezzo medio (€)')
    plt.title(f"Prezzo medio annuo di Soybean ({stateCode})\ncon banda ±1 deviazione std progressiva")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

    # -------------------------------------------------------------------------
    # C) GRAFICO COMBINATO: Produzione, Area e Prezzo (anni condivisi)
    # -------------------------------------------------------------------------
    combined = pd.merge(
        annual,
        annual_price[['year', 'price']],
        on='year',
        how='inner'
    )

    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Barre affiancate per produzione e area
    ax1.bar(
        combined['year'] - 0.2,
        combined['grossProduction'],
        width=0.4,
        alpha=0.7,
        label='Produzione lorda (t)',
        color='tab:blue'
    )
    ax1.bar(
        combined['year'] + 0.2,
        combined['area'],
        width=0.4,
        alpha=0.5,
        label='Area raccolta (ha)',
        color='tab:green'
    )
    ax1.set_xlabel('Anno')
    ax1.set_ylabel('Produzione / Area', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # Linea del prezzo sul secondo asse
    ax2 = ax1.twinx()
    ax2.plot(
        combined['year'],
        combined['price'],
        marker='o', linestyle='-',
        color='tab:orange',
        label='Prezzo medio annuo (€ per T)'
    )
    ax2.set_ylabel('Prezzo medio (€)', color='tab:orange')
    ax2.tick_params(axis='y', labelcolor='tab:orange')

    # Legenda combinata
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

    plt.title(f"Produzione, Area e Prezzo medio annuo di Soybean ({stateCode})\n(anni condivisi)")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
