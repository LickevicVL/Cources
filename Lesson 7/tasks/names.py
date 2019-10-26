from funcs import *

@decor
def main(filename):
	data = read_data(filename) #list

	result = find_simple(data) #dict
	

	#wjson(result)
	

if __name__ == '__main__':
	filename = 'names.txt'
	main(filename)

