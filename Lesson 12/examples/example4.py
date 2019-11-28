from multiprocessing import Pool
from time import time


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i

    return res


if __name__ == '__main__':
    t1 = time()
    factorial(100000)
    t2 = time()

    print('Single factorial: ', t2 - t1)

    pool = Pool(2)
    t3 = time()
    pool.map(factorial, [100000] * 2)
    pool.close()
    pool.join()
    t4 = time()

    print('Pool factorial: ', t4 - t3)
