def checkvalid(ip_list_str, pref_int):
	'''
	Проверяет на правильность ip и префикс маски
	'''
	flag_ip = True
	flag_pref = True
	
	val = len(ip_list_str)
	leng = sum([int(len(i)) for i in ip_list_str])
	if leng != 32 and val == 4:
		flag_ip = False
	if pref_int <0 or pref_int > 32:
		flag_pref = False
	
	return flag_ip, flag_pref	
		
				
def convert(val_list, in_system):
	'''
	Конвертит список из 4 элементов str/int в аналогичный int/str
	в str двоичная
	в int десятичная
	'''
	new_list = []
	if in_system == 10:                                                  #в 10ую
		new_list = [int(i, 2) for i in val_list]
	if in_system == 2:                                                   #в 2ую
		new_list = [str(bin(i)).replace('0b', '').zfill(8) for i in val_list]
		
	return new_list


def get_mask_from_pref(pref):
	'''
	Конвертит префикс в маску двоичную
	'''
	if pref != 0:
		mask = ('1' * pref).zfill(32)[::-1]
		mask = [mask[i*8:(i+1)*8] for i in range(4)]
	else:
		mask = ''.zfill(32)
		mask = [mask[i*8:(i+1)*8] for i in range(4)]
	
	return mask
