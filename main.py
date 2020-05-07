from account import Account

ap = 50

Acc1 = Account(1500)

print(Acc1.value())

Acc1.assetBuy(499, ap)

print(Acc1.value())

Acc1.assetSell(5, ap)

print(Acc1.value())