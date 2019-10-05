#Нормальные комменты сделать
def create_id(dm): #Create id
	i_d = f"id_{dm['name'][:4]}{dm['surname'][:2]}{dm['age']}{dm['sex']}"
	return i_d


def show(dm, key): #Вывод dm
	print(f"Full Name: {dm['name'].title()} {dm['surname'].title()},  Age: {dm['age']},  Sex: {dm['sex']},  id: {key}")


def search_by_func(db, search_p, param, trigger): #если нет совпадений, как вывести? счетчик не знаю куда вставить(если он конечно тут нужен)
	if trigger == 0:
		[show(dm, key) for key, dm in db.items() if dm[search_p] == param]
	elif trigger == 1:
		fn_l = param.split()
		[show(dm, key) for key, dm in db.items() if dm[search_p[0]] == fn_l[0] and dm[search_p[1]] == fn_l[1]]
		
		
def check_fullname(): #для правильного ввода полного имени (бывают со штуками междму именем и фамилией)
	while True:
		fn = (input("Enter Full Name (N_S): ")).lower()
		if len(fn.split()) != 2:
			print("Wrong Name! Template: Name Surname. Try again.")
		else:
			break
	return fn


def new_dm_func(): #Проверка на число !"№;%:"?*!;%!:*";!%?*
	name = (input("Name: ")).lower()
	surname = input("Surname: ").lower()
	
	while True:
		age = input("Age: ")
		if age.isdigit():
			break
	
	while True:
		sex = input("Sex(m/f): ").lower()
		if sex == 'f' or sex == 'm':
			break
	
	dm = {'name': name, 'surname': surname, 'age': age, 'sex': sex}
	return dm


def search_func(db, search_by, search_msg):	
	while True:
		search_p = input(search_msg) #name, surname, age, fn
		if search_p == search_by[0]:
			search_by_func(db, search_p, (input("Enter Name: ")).lower(), 0) 
			break
		elif search_p == search_by[1]:
			search_by_func(db, search_p, (input("Enter Surname: ")).lower(), 0)
			break
		elif search_p == search_by[2]:
			search_by_func(db, search_p, (input("Enter Age: ")).lower(), 0)
			break
		elif search_p == search_by[3]:
			search_p = [search_by[0], search_by[1]]
			search_by_func(db, search_p, check_fullname(), 1)
			break
		elif search_p == 'e' or search_p == 'q':
			break
		else:
			print("-unknown command-")


def add_dbm(db):
	new_dm = new_dm_func()
	new_id = create_id(new_dm)
	db[new_id] = new_dm
