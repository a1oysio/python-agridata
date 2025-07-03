import pandas as pd
from agridata.service import AgriDataService
import matplotlib.pyplot as plt

# 1. Recupera i dati
service = AgriDataService()
response = service.cereals.get_prices(memberStateCodes="IT")
price_list = getattr(response, 'prices', getattr(response, 'items', getattr(response, 'data', [])))

# 2. Costruisci il DataFrame
data = []
for item in price_list:
    date = pd.to_datetime(item.beginDate, dayfirst=True)
    price = float(item.price.replace('€', '').replace(',', ''))
    data.append({'Date': date, 'Price': price})

df = pd.DataFrame(data).set_index('Date').sort_index()

# 3. Aggrega in OHLC mensile (label inizio mese)
ohlc = df['Price'].resample('W', label='left', closed='left').agg({
    'open':  'first',
    'high':  'max',
    'low':   'min',
    'close': 'last'
})
ohlc.columns = ['Open', 'High', 'Low', 'Close']

# 4. Calcola la media dei prezzi di chiusura
avg_close = ohlc['Close'].mean()

# 5. Disegna il grafico a linea con chiusura e media
plt.figure()
plt.plot(ohlc.index, ohlc['Close'], label='Close')
plt.axhline(y=avg_close, linestyle='--', label='Average Close')
plt.title('Prezzi di Chiusura e Media Mensile')
plt.xlabel('Data')
plt.ylabel('Prezzo (€ per TONNES)')
plt.legend()
plt.tight_layout()
plt.show()
