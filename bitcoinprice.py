from blockchain import exchangerates

def getBitcoinPrice():
    btcAmount = exchangerates.get_ticker()
    return(btcAmount['USD'].last)

getBitcoinPrice()