import re
import json
from collections import Counter

def decor(func):
	'''Чисто посмотреть на время выполнения функции'''
	from time import time
	def wrapper(*args):
		start = time()
		value = func(*args)
		end = time()
		print(f"Delay: {end-start}.")
		return value
	return wrapper
	

def get_file(filename):
	'''Читаем файл'''
	with open(filename, 'r') as tfile:
		text = tfile.read()
		
	return text
	

def count_words(text, expression):
	'''Возвращает списов всех слов в тексте'''
	all_words = expression.findall(text)
	
	return all_words


def words_freq(all_words):
	'''Получаем словарь с частотами слов'''
	counter = Counter()
	
	for word in all_words:
		counter[word] += 1
	#print(sum(counter.values()))
	
	return counter

			
			

if __name__ == '__main__' :
	expression = re.compile(r"[\w]+(?<!'\w)")
	text = get_file('text.txt')
	
	all_words = count_words(text.lower(), expression)
	#Удаляем s, тк оно часть притяжательного
	#all_words = list(filter(lambda el: el != 's', all_words))
	print(f'Total words: {len(all_words)}')
	
	unique_words = set(all_words)
	print('There are ', len(unique_words), ' unique words.')
	
	word_freq_dict = words_freq(all_words)
	
	n = 15
	print(f'Top {n}:') 
	top_n = Counter(word_freq_dict).most_common(n)
	for i in top_n:
		print(i)
			


