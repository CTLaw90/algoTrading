class Account:
	def __init__(self, initCapital):
		self.capital = initCapital
		self.assets = 0
		
		
	def assetBuy(self, amount, assetprice):
		self.capital = self.capital - amount
		self.assets += (amount/assetprice)
		print('Bought', amount, 'of asset')
		return(1)
		
	def assetSell(self, amount, assetprice):
		self.assets = self.assets - amount
		self.capital += (amount*assetprice)
		print('Sold', amount, 'of asset')
		return(1)
		
	def value(self):
		return(self.capital, self.assets)
