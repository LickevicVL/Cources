from threading import Thread
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

    thread1 = Thread(target=factorial, args=(100000,))
    thread2 = Thread(target=factorial, args=(100000,))

    t3 = time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    t4 = time()

    print('2 threads factorial: ', t4 - t3)
