from classes import *
	
	
if __name__ == '__main__':
	#addr_3 = Address('c. Minsk, st. Gromova, № 144')
	#addr_4 = Address('c. Hell, st. Circle_7, № 666')
	
	
	shop_1 = Shop('c. Hell, st. Circle_8, № 666', 'Vasilek')
	shop_2 = Shop('c. Hell, st. Hell_Entrance, № 665', 'Brick')
	shop_3 = Shop('c. Hell, st. Circle_4, № 1337', 'Cave_of_Happines')
	
	#lipton = Tea('Lipton')
	#lipton.set_price(2.88)
	#lipton + 20
	#print(lipton.name, lipton.barcode, lipton.get_price(), lipton.get_count())
	
	chacha = Tea('Chacha')
	chacha.set_price(3.50)
	shop_1.add_product(chacha, 15)
	shop_3.add_product(chacha, 13)
	
	print(chacha.name, chacha.barcode, chacha.get_price(), chacha.get_count())
	print('Shop 1: ', shop_1.goods)
	print('Shop 2: ', shop_2.goods)
	print('Shop 3: ', shop_3.goods)
	
	#print('\nBuying 16 Chacha in Shop 1:')
	#shop_1.sale_product('chacha', 16)
	
	print(chacha.name, chacha.get_count())
	print('Shop 1: ', shop_1.goods)

	print('\nTrying to buy Chacha in Shop 2:')
	shop_2.sale_product('chacha', 13)
	print(shop_1 < shop_3)
	
	print('\nTrying to buy 12 Lipton in Shop 1:')
	shop_1.sale_product('lipton', 12)
	print(shop_1.goods)
	
	print('\nTrying to buy 12 Chacha in Shop 1:')
	shop_1.sale_product('Chacha', 12)
	print(shop_1.goods)
	
	print('\nBuying 10 Chacha in Shop 3:')
	shop_3.sale_product('chacha', 10)
	print(shop_3.goods)
	print(chacha.name, chacha.get_count())
	
	
	print('\nEarnings:')
	Shop.print_earnings(0)
	Shop.print_earnings(1)
	shop_3.print_earnings(shop_2)





