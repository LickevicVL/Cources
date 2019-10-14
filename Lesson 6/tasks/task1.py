
def ip_net_calc(ip_, mask):

    ip_list = ip_.split('.')
    mask_list = mask.split('.')

    print(f'IP адрес: {ip_}')
    print(f'Маска подсети: {mask}')

    ip_net = []
    for i, j in zip(ip_list, mask_list):
        if j == '255':
            ip_net.append(i)
        elif j == '0':
            ip_net.append('0')
        else:
            i = int(i)
            j = int(j)
            a = i & j
            ip_net.append(str(a))
    ip_net_user = '.'.join(ip_net)
    print(f'IP адрес сети: {ip_net_user}')


ip_net_calc('192.135.120.54', '255.255.192.0')
