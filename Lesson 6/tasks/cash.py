global_dict = dict()
global_time = dict()

def multi(val1, val2):
	'''первое что пришло в голову'''
	return val1 * val2


def get_time():
	'''Получение текущего времени и даты'''
	from time import time, strftime, gmtime
	
	time_list = strftime('%y %m %d %H %M %S', gmtime(time()))
	time_list = int(time_list.replace(' ', ''))
	
	return time_list
	
	
def find_oldest_date():
	'''Поиск 'старейшей' даты'''
	min_time = 0
	arg = None
	for args, time in global_time.items():
		if min_time == 0:
			min_time = time
			arg = args
		elif time < min_time:
			min_time = time
			arg = args
			
	print(f'These data will be removed : ({arg}: {min_time})') #для проверки
	return arg
	
	
def decor(func, max_cache):
	
	def wrapper(val1, val2):
		flag = list(filter(lambda args: args == (val1, val2), global_dict))
		
		if len(global_dict) < max_cache and not flag: #если нет в кэше и кэш не переполнен
			print('Updating cache...')
			result = func(val1, val2)
			global_dict[val1, val2] = result
			global_time[val1, val2] = get_time()
		elif flag: #если есть в кэше
			print('Getting from cache...')
			result = global_dict[flag[-1]]
		elif len(global_dict) >= max_cache: #кэш переполнен
			print('Clearing cache...')
			oldest_args= find_oldest_date()
			del global_dict[oldest_args]
			del global_time[oldest_args]
			
			result = func(val1, val2)
			global_dict[val1, val2] = result
			global_time[val1, val2] = get_time()
			
			
		return result
	return wrapper



multi = decor(multi, 3)



if __name__ == '__main__':
	multi(1, 3)
	multi(3, 3)
	multi(4, 3)
	multi(1, 3)
	multi(2, 3)
	multi(2, 3)
	
	print(f'\nCurrent global_dict:\n{global_dict}')
	print(f'Current global_time:\n{global_time}')












