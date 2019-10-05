from variables import *
from funcs import show, search_func, add_dbm, create_id


db = {create_id(dm_1): dm_1, create_id(dm_2): dm_2} #начальная база данных


def main_loop():		
	while True:
		answr = input(start_msg).lower()
		
		if answr == answrs[0]: #COMPLETE
			for key, dm in db.items():
				show(dm, key)		
		elif answr == answrs[1]: #COMPLETE
			search_func(db, search_by, search_msg) #если правильно понимаю, то передается не копия db, а типа по ссылке			
		elif answr == answrs[2]: ##COMPLETE      Если уже есть такой человек?
			add(db) #если правильно понимаю, то передается не копия db, а типа по ссылке
		elif answr == 'q' or answr == 'e':
			break		
		else:
			print('-unknown command-')

		print('')




#Вроде бы все работает правильно
#Что есть:
#-Вывод текущей БД
#-Поиск по: имени, фамилии, возрасту, полному имени
#-Добавление нового элемента в БД (с созданием id)
main_loop()
