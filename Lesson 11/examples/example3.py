from dataclasses import dataclass, field
from random import randint


@dataclass
class Book:
    title: str
    author: str
    count: int = field(default=100)


def gen_desc():
    return [randint(0, 100) for i in range(100)]


@dataclass
class Desc:
    cards: list = field(default_factory=gen_desc)


if __name__ == '__main__':
    book1 = Book('Book1', 'Author1', 10)
    book2 = Book('Book2', ['Author2', 'Могу быть и не строкой'])
    print(book1, book2)

    desk = Desc()
    print(desk)
