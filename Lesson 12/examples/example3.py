from threading import Lock, Thread
from time import sleep


class Bank:
    money = 0
    lock = Lock()

    def replenish(self, s=10):
        self.lock.acquire()
        print(Bank.money, 'money')
        sleep(10)
        Bank.money += s
        print('Replenish cash')
        self.lock.release()

    def withdraw(self, s=10):
        self.lock.acquire()
        print(Bank.money, 'money')
        sleep(1)
        if self.money >= s:
            Bank.money -= s
            print('Withdraw cash')
        else:
            print('not enough money')
        self.lock.release()


class User(Thread):
    def __init__(self, name, func):
        super().__init__(name=name)
        self.name = name
        self.func = func

    def run(self):
        print(f'{self.name} try to {self.func}')
        bank = Bank()
        func = getattr(bank, self.func)
        func()
        print(f'{self.name} made {self.func} operation')


if __name__ == '__main__':
    user1 = User('Bob', 'replenish')
    user1.start()
    sleep(1)
    user2 = User('Kate', 'withdraw')
    user2.start()

    user1.join()
    user2.join()
