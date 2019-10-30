from abc import ABC, abstractmethod
from random import randint

from example1 import Man, Person


class Worker(
    ABC,
    # Person  # Раскомментировать, чтобы увидеть чудо!
):
    @abstractmethod
    def do(self):
        pass

    def measure(self):
        return self.__class__.__name__

    def weigh(self):
        return self.__class__.__name__


class Programmer(Man, Worker):
    def do(self):
        if self.get_force() > randint(1, 10):
            return 'Done!'

        return 'Not done!'


if __name__ == '__main__':
    programmer = Programmer('Bob', 34, 56, 200)
    print(programmer.measure())
    print(programmer.do())

    del Person.measure
    print(programmer.measure())

    print(programmer.weigh())
