from math import sqrt
import time


def time_sqr(n):
    time_start = time.time()
    for i in range(1000000):
        x = i ** (1 / n)
    print(f'My function sqr takes {(time.time() - time_start)} seconds')


def time_sqrt():
    time_start = time.time()
    for i in range(1000000):
        x = sqrt(i)
    print(f'Function sqrt from Math takes {(time.time() - time_start)} seconds')


time_sqr(2)
time_sqrt()
