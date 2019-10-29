from math import sqrt
import time


def sqr(a, n):
    a = a ** (1 / n)
    return a


time_start1 = time.time()
sqr(1000000, 2)
time_finish1 = time.time()

time_start2 = time.time()
sqrt(1000000)
time_finish2 = time.time()

result1 = time_finish1 - time_start1
result2 = time_finish2 - time_start2

if result1 < result2:
    print('Function sqr is faster')
else:
    print('Function sqrt from math is faster')

print(f'sqr takes {result1}, sqrt takes {result2}')
