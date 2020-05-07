from account import Account
from bitcoinprice import getBitcoinPrice
import time

def gain5lose2(Acc1):
    ap = getBitcoinPrice()
    Acc1.assetBuy(Acc1.capital, ap)
    print('Starting Bitcoin price:', ap, 'USD')
    buyPrice = ap
    for i in range(500):
        ap = getBitcoinPrice()
        print('Bitcoin Value:', ap, 'USD')
        if ap > (buyPrice*1.0005):
            Acc1.assetSell(Acc1.assets, ap)
            break
        elif ap < (buyPrice*.9998):
            Acc1.assetSell(Acc1.assets, ap)
            break
        time.sleep(30)
    print('End of Test')
    print('Account value:', Acc1.value())
    

Acc = Account(1500)

gain5lose2(Acc)