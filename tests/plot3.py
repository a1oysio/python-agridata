#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Estrae e visualizza per 'Soybean' in Italia:
- Produzione lorda, area e resa (metriche annuali).
- Grafico a doppio asse con barre e linea tratteggiata.
"""

from agridata.service import AgriDataService  # Wrapper per le API Agridata
import pandas as pd                          # Manipolazione dati
import matplotlib.pyplot as plt              # Plotting

def main():
    # 1) Inizializza il servizio
    service = AgriDataService()

    # 2) Estrai i dati di produzione per 'Soybean' in Italia
    prod_raw = service.oilseeds.get_production(
        memberStateCodes="IT",
        crops="Soybean"
    )  # Restituisce campi memberStateCode, year, grossProduction, area, yield :contentReference[oaicite:7]{index=7}

    # 3) Normalizza il JSON in DataFrame
    df = pd.json_normalize(prod_raw)         # Appiattisce lista di dict in tabella :contentReference[oaicite:8]{index=8}

    # 4) Converte i tipi delle colonne
    df['year']            = df['year']           .astype(int)
    df['grossProduction'] = df['grossProduction'].astype(float)
    df['area']            = df['area']           .astype(float)
    df['yield']           = df['yield']          .astype(float)

    # 5a) SOLUZIONE 1: Media solo colonne numeriche
    annual_numeric = (
        df
        .groupby('year', as_index=False)
        .mean(numeric_only=True)            # numeric_only=True esclude colonne object :contentReference[oaicite:9]{index=9}
        .sort_values('year')
    )

    # 5b) SOLUZIONE 2: Media colonne specificate
    annual_agg = (
        df
        .groupby('year', as_index=False)
        .agg({
            'grossProduction': 'mean',
            'area':            'mean',
            'yield':           'mean'
        })                                # agg su chiavi specifiche :contentReference[oaicite:10]{index=10}
        .sort_values('year')
    )

    # Scegliere una delle due serie per il grafico (qui usiamo annual_agg)
    annual = annual_agg

    # 6) Costruisci il grafico a doppio asse
    years = annual['year']
    width = 0.4

    fig, ax1 = plt.subplots(figsize=(10, 6))

    # 6.1 Barre affiancate: produzione e area
    ax1.bar(
        years - width/2,
        annual['grossProduction'],
        width=width,
        label='Produzione lorda (t)',
        alpha=0.8
    )
    ax1.bar(
        years + width/2,
        annual['area'],
        width=width,
        label='Area raccolta (ha)',
        alpha=0.6
    )
    ax1.set_xlabel('Anno')
    ax1.set_ylabel('Produzione/Area', color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # 6.2 Linea tratteggiata per la resa (asse destro)
    ax2 = ax1.twinx()
    ax2.plot(
        years,
        annual['yield'],
        linestyle='--',
        marker='o',
        label='Resa (t/ha)',
        color='tab:red'
    )
    ax2.set_ylabel('Resa (t/ha)', color='tab:red')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    # 6.3 Legenda combinata e titolo
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

    plt.title('Produzione lorda, Area e Resa annuali di Soybean in Italia')
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
