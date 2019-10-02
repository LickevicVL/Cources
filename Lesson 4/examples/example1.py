num = input('Please, input number: ')

odd = 0
even = 0

for n in num:
    digit = int(n)
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1


print('Odd: ', odd)
print('Even: ', even)
