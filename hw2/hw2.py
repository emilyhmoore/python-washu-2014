from random import uniform

class Portfolio:
	def __init__(self, starting_balance):
		self.funds=starting_balance
		self.stocks={}
		self.mutualfunds={}
		self.history=[]
	
	def addCash(self, amount):
		self.funds+=amount
		self.history.append("add $%.2f in cash" %amount)
		return self.history[-1]
	
	def buyStock(self, number, stock_object):
		if stock_object.name in self.stocks.keys():
			number+=self.stocks[stock_object.name]
		self.stocks.update({stock_object.name:number})
		self.funds-=stock_object.price*number
		self.history.append("buy %f in %r stocks, Balance: %f" %(number, stock_object.name, self.funds))
	
	def sellStock(self, number, stock_object):
		name=stock_object.name
		if self.stocks[name]==number:
			del self.stocks[name]
		else:
			new_value=self.stocks[name]-number
			self.stocks.update({name:new_value})
		self.funds+=number * uniform(.5 * stock_object.price, 1.5 * stock_object.price)
		self.history.append("sell %f in %r stocks, Available Balance: %f" %(number, stock_object.name, self.funds))
	
	def buyMutualFund(self, number, mf_object):
		if mf_object.name in self.mutualfunds.keys():
			number+=self.mutualfunds[name]
		self.mutualfunds.update({mf_object.name:number})
		self.funds-=number
		self.history.append("buy %f in %r mf, Available Balance: %f" %(number, mf_object.name, self.funds))
	
	def sellMutualFund(self, number, mf_object):
		name=mf_object.name
		if self.mutualfunds[name]==number:
			del self.mutualfunds[name]
		else:
			new_value=self.mutualfunds[name]-number
			self.mutualfunds.update({name:new_value})
		self.funds+=number
		self.history.append("sell %f in %r mf, Available Balance: %f" %(number, mf_object.name, self.funds))
	
	def withdrawCash(self, amount):
		self.funds-=amount
		self.history.append("withdraw $%.2f in cash" %amount)
		return self.history[-1]
	
class Stock:
	def __init__(self, price, name):
		self.name=str(name)
		self.price=price
		
class MutualFund:
	def __init__(self, name):
		self.name=str(name)
	
	
	
	
	
	
	
