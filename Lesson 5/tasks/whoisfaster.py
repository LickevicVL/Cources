from math import sqrt


def decor(func):
	from time import time
	def wrapper(*args):
		start = time()
		value = func(*args)
		end = time()
		delay = end - start
		print(delay)
		return value, delay
	return wrapper
	
@decor
def sqr(val, n):
	return (val)**(1/n)
	

sqrt = decor(sqrt)


if __name__ == '__main__':
	print('sqr function delay:')
	val1, delay1 = sqr(0.00002, 2)
	
	print('\nsqrt function delay:')
	val2, delay2 = sqrt(25)
	
	if delay1 < delay2:
		print('\nSqr function is faster.')
		
	else:
		print('\nSqrt function is faster')
		
	
