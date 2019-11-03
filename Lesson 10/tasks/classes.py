from random import randint
from math import sqrt
import re
from abc import ABC
import uuid


class Address:
		def __init__(self, address):
			regex = re.compile(r'c\. ([\w]+), st\. ([\w]+), \№ ([0-9]+)')
			string = regex.findall(address)
			
			self.city = string[0][0]
			self.street = string[0][1]
			self.building = string[0][2]
			
			self.x = randint(0, 250)
			self.y = randint(0, 250)
			
			
		def __lt__(self, other):
			if isinstance(other, Address):
				return self.distance() < other.distance()
			
		def distance(self):
			return sqrt(self.x**2 + self.y**2)
			
		def show(self):
			print(self.city)
			print(self.street)
			print(self.building)


class Money:
	def __init__(self):
		self.total_money = 0
		self.shops_money = dict()
		
	def increase(self, shop, value):
		self.total_money += value
		if shop in self.shops_money.keys():
			self.shops_money[shop] += value
		else:
			self.shops_money[shop] = 0
			self.shops_money[shop] += value
			

class Shop(Address):
	_shops = []
	_money = Money()
	
	
	def __init__(self, address, name):
		super().__init__(address)
		
		self.name = name.lower()
		self.goods = dict()
		
		self.__class__._shops.append(self)
	
	def add_product(self, product, amount):
		product + amount
		self.goods[product.name] = [product, amount]
	
	def sale_product(self, name, amount):
		name = name.lower()
		if name in self.goods.keys() and self.goods[name][1] != 0:
			if amount > self.goods[name][1]:
				self._calculate(self.goods[name][1], name)
			else:
				self._calculate(amount, name)	
		else:
			return self._search_nearest(name)
			
	def _search_nearest(self, name):
		shops_with = [shop for shop in self.__class__._shops 
				if name in shop.goods.keys() and shop.goods[name][1] != 0]
		if shops_with:
			print(f"Nearest shop with {name.title()} is {min(shops_with).name.title()}")
		else:
			print(f'There are no shops with {name.title()}')
			
	def _calculate(self, value, name):
		self.goods[name][0] - value
		self.__class__._money.increase(self,
				value * self.goods[name][0].get_price())
		self.goods[name][1] -= value
	
	@staticmethod
	def print_earnings(arg):
		'''0 - by shops, 1 - total'''
		if arg == 0 and __class__._money.shops_money:
			[print(f'{shop.name.title()}: {money} points')
					for shop, money in __class__._money.shops_money.items()]
		elif arg == 1:
			print(f'Total: {__class__._money.total_money} points')
		elif type(arg) == Shop and arg in __class__._money.shops_money:
			name = arg.name
			print(f'{name.title()}: {__class__._money.shops_money[arg]} points')
		else:
			print('The shop you are interested in has no sales history.')
		
		
class Goods(ABC):
	_price = 0
	_count = 0
	
	
	def get_price(self):
		return self._price
	
	def set_price(self, value):
		setattr(self, '_price', value)
		
	def get_count(self):
		return self._count
	
	def __add__(self, value):
		self._count += value
		
	def __sub__(self, value):
		self._count -= value
	
	
class Tea(Goods):
	def __init__(self, name):
		self.name = name.lower()
		
		self.barcode = uuid.uuid1()
