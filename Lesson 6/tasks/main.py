from ipfuncs import *



def decor(func):
	def wrapper(ipad_2, subwm_pref):                                    #list_of_str,  int
		'''Последовательность как в задании'''	
		ip, pref = checkvalid(ipad_2, subwm_pref)                       #проверяем на 'годность'
		if ip and pref:
			subwm = convert(get_mask_from_pref(subwm_pref), 10)	        #получаем маску в 2ом и сразу перевоиди в 10ую
			ipad_10 = convert(ipad_2, 10)                               #переводим ip в 10ую
			web_ip = func(ipad_10, subwm)
			
			return web_ip			
		else:
			return 0
	
	return wrapper
			
@decor			
def get_web_ip(ip_address, subweb_mask):
	'''
	Вычисляет ip сети
	'''
	web_ip = []
	for i in range(4):
		if subweb_mask[i] == 0:                                         #0
			web_ip.append(0)
		elif subweb_mask[i] != 0 and subweb_mask != 255:                #!= 0 || 255
			var_1 = 255 - subweb_mask[i] + 1
			var_2 = ip_address[i]//var_1
			web_ip.append(var_2 * var_1) 
		else:                                                           #255
			web_ip.append(ip_address[i])
			
	return web_ip


def main():
	'''
	Можно добавить пользовательский ввод преф. и ip, но уже лень, тк
	проверку на ввод надо делать
	'''
	ip_10 = [192, 145, 96, 8]
	ip_2 = convert(ip_10, 2)
	pref = 12
	web_ip = get_web_ip(ip_2, pref)

	a = f'ip_2: {ip_10}\nip_10: {ip_2}\nsub. web. prefix: {pref}\nweb_ip: {web_ip}'
	print(a)



main()
