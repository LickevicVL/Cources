units = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen'
}

dozens = {
    '1': 'ten',
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}


for i in range(1000):
    num = str(i)
    if len(num) == 3:
        if num[-1] == '0' and num[-2] == '0':
            st = units[num[0]] + ' hundred'
            print(st)
        elif num[-1] == '0':
            st = f'{units[num[0]]} hundred and {dozens[num[1]]}'
            print(st)
        elif num[-2] == '1':
            st = f'{units[num[0]]} hundred and {units[num[1] + num[-1]]}'
            print(st)
        elif num[-2] == '0':
            st = f'{units[num[0]]} hundred and {units[num[-1]]}'
            print(st)
        else:
            st = f'{units[num[0]]} hundred and {dozens[num[1]]} ' \
                 f'{units[num[-1]]}'
            print(st)
    elif len(num) == 2:
        if num[-1] == '0':
            st = dozens[num[0]]
            print(st)
        elif num[0] == '1':
            st = units[num[0] + num[-1]]
            print(st)
        else:
            st = f'{dozens[num[0]]} {units[num[-1]]}'
            print(st)
    elif len(num) == 1:
        st = units[num]
        print(st)
