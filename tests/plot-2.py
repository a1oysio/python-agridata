
import pandas as pd
import matplotlib.pyplot as plt
from agridata.service import AgriDataService

# ————— Parametri utente —————
MEMBER_STATE = "IT"
CROP_NAME    = "Durum wheat"   # deve corrispondere sia a productName che a crop

# ————— 1. Fetch dei dati —————
service  = AgriDataService()

# Prezzi
resp_p   = service.cereals.get_prices(memberStateCodes=MEMBER_STATE)
price_list = getattr(resp_p, 'prices',
                getattr(resp_p, 'items',
                  getattr(resp_p, 'data', [])))

# Produzione
resp_prod   = service.cereals.get_production(memberStateCodes=MEMBER_STATE)
prod_list   = getattr(resp_prod, 'production', 
                getattr(resp_prod, 'items',
                  getattr(resp_prod, 'data', [])))

# ————— 2. Costruisci il DataFrame prezzi —————
price_data = []
for item in price_list:
    if item.productName != CROP_NAME:
        continue
    dt    = pd.to_datetime(item.beginDate, dayfirst=True)
    price = float(item.price.replace('€','').replace(',',''))
    price_data.append({'Date': dt, 'Price': price})

df_price = (
    pd.DataFrame(price_data)
      .set_index('Date')
      .sort_index()
)

# ————— 3. Aggrega il prezzo su base annua (media) —————
df_price_ann = (
    df_price['Price']
      .resample('A')             # fine anno
      .mean()
      .to_frame(name='AvgPrice')
)
# Porta l'indice da 31/12/YYYY a YYYY
df_price_ann.index = df_price_ann.index.year

# ————— 4. Costruisci il DataFrame produzione —————
prod_data = []
for item in prod_list:
    if item.crop != CROP_NAME:
        continue
    prod_data.append({
        'Year': item.year,
        'Production': item.grossProduction
    })

df_prod = (
    pd.DataFrame(prod_data)
      .drop_duplicates(subset='Year')
      .set_index('Year')
      .sort_index()
)

# ————— 5. Unisci e disegna il grafico —————
df = df_prod.join(df_price_ann, how='inner')

years = df.index.astype(int)
prod  = df['Production']
price = df['AvgPrice']

fig, ax1 = plt.subplots(figsize=(10,5))

# Barre per la produzione
ax1.bar(years, prod, alpha=0.6, label='Produzione (tonnellate)')
ax1.set_xlabel('Anno')
ax1.set_ylabel('Produzione lorda (tonnellate)')
ax1.tick_params(axis='y')

# Linea per il prezzo medio annuale
ax2 = ax1.twinx()
ax2.plot(years, price, marker='o', label='Prezzo medio (€)', linestyle='-')
ax2.set_ylabel('Prezzo medio (€ per TONNES)')
ax2.tick_params(axis='y')

# Titolo e legende
fig.suptitle(f"{CROP_NAME}: Produzione vs Prezzo Medio Annuale ({MEMBER_STATE})")
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout(rect=[0,0,1,0.95])
plt.show()
