from threading import Thread
from time import sleep

WORK = True


def handler(name, sleep_time):
    while WORK:
        print(f'{name} start to sleep {sleep_time} sec')
        sleep(sleep_time)


if __name__ == '__main__':
    thread1 = Thread(target=handler, args=('first', 2))
    thread2 = Thread(target=handler, args=('second', 3))

    thread1.start()
    thread2.start()

    print('Main start to sleep')
    sleep(60)

    WORK = not WORK

    thread1.join()
    thread2.join()
