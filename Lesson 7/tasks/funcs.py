import json


def decor(func):
	from time import time
	def wrapper(*args):
		start = time()
		func(*args)
		end = time()
		print("Delay: ", end - start)
	return wrapper
	

def read_data(filename):
	with open(filename, 'r') as f:
		data = f.read().replace('"', '').split(',')
	
	return data


def find_simple(list_data):
	result = dict()
	for name in list_data:
		l = list()
		for oname in list_data:
			if name in oname and name != oname:
				 l.append(oname)
		if l:
			result[name] = l
	return result
	

def wjson(dict_data):
	with open('result.json', 'w') as f:
		json.dump(dict_data, f, indent=2)

def rjson():
	data = ''
	with open('result.json', 'r') as f:
		data = json.loads(f.read())
		
	return data
