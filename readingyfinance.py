import yfinance as yf

tsla = yf.Ticker("tsla")

tslai = tsla.info


print(tslai['ask'])
print(tslai['bid'])
print(tslai['regularMarketPrice'])

hist = tsla.history(period="max")

print(hist)