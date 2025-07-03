#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script per correlazione Prezzo ~ Produzione di tutte le colture Cereals:
- Recupera le colture disponibili con service.cereal.get_production_crops()
- Recupera i prodotti con service.cereal.get_products()
- Trova l'intersezione tra colture e prodotti disponibili
- Per ogni coltura comune, preleva le medie annuali di produzione (UE) e prezzo (EU)
- Concatena tutti i dati in un unico DataFrame
- Allena un modello di regressione lineare semplice: Prezzo ~ Produzione
- Mostra summary, formula, AIC/BIC e grafico a dispersione con retta di fit
"""
from agridata.service import AgriDataService
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def main():
    service = AgriDataService()

    # 1) Ottieni lista colture e prodotti
    crops = service.cereal.get_production_crops()
    products = [p['productName'] for p in service.cereal.get_products()]
    common = set(crops).intersection(products)
    print("Colture disponibili:", crops)
    print("Prodotti disponibili:", products)
    print("Colture comuni:", list(common))

    # 2) Preleva dati per ogni coltura comune
    frames = []
    for crop in common:
        try:
            # Produzione media annua
            raw_prod = service.cereal.get_production(crops=crop)
            dfp = pd.json_normalize(raw_prod)
            dfp = dfp[dfp['crop']==crop].astype({'year': int, 'grossProduction': float})
            dfp = dfp[dfp['grossProduction']>0]
            prod = dfp.groupby('year', as_index=False).agg(production_mean=('grossProduction','mean'))

            # Prezzo medio annuo
            raw_price = service.cereal.get_prices(memberStateCodes=None, products=crop)
            dfpr = pd.json_normalize(raw_price)
            dfpr['beginDate'] = pd.to_datetime(dfpr['beginDate'], format='%d/%m/%Y')
            dfpr['year'] = dfpr['beginDate'].dt.year
            dfpr['price'] = (
                dfpr['price']
                  .str.replace('[^0-9,\.]','',regex=True)
                  .str.replace(',','.',regex=False)
                  .astype(float)
            )
            dfpr = dfpr[dfpr['price']>0]
            price = dfpr.groupby('year', as_index=False).agg(price_mean=('price','mean'))

            # Unione annuale
            dfm = pd.merge(prod, price, on='year', how='inner')
            dfm['crop'] = crop
            frames.append(dfm)
        except Exception as e:
            print(f"Warning: salto {crop} per errore: {e}")

    # 3) Concatenazione dati
    if not frames:
        print("Nessun dato valido trovato per le colture comuni.")
        return
    df = pd.concat(frames, ignore_index=True)
    print(f"Dataset unito: {len(df)} righe.")

    # 4) Modello lineare Prezzo ~ Produzione
    X = sm.add_constant(df['production_mean'])  # aggiunge intercept
    y = df['price_mean']
    model = sm.OLS(y, X).fit()

    # 5) Output statistico
    print(model.summary())
    intercept, slope = model.params['const'], model.params['production_mean']
    print(f"Formula: prezzo = {intercept:.2f} + {slope:.2f} * produzione")
    print(f"AIC: {model.aic:.2f}, BIC: {model.bic:.2f}")

    # 6) Plot
    plt.figure(figsize=(8,6))
    for crop in common:
        d = df[df['crop']==crop]
        plt.scatter(d['production_mean'], d['price_mean'], label=crop, alpha=0.7)
    x_vals = np.linspace(df['production_mean'].min(), df['production_mean'].max(), 100)
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, 'k--', label='Fit complessivo')
    plt.xlabel('Produzione media annua (t)')
    plt.ylabel('Prezzo medio annuo (€)')
    plt.title('Prezzo ~ Produzione per colture comuni Cereals')
    plt.legend(bbox_to_anchor=(1.05,1), loc='upper left')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
