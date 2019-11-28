from random import choice

from pony import orm


db = orm.Database()
db.bind(provider='sqlite', filename='books.sqlite', create_db=True)


class Author(db.Entity):
    name = orm.Required(str)
    book = orm.Set(lambda: Books)


class Books(db.Entity):
    book_id = orm.PrimaryKey(int, auto=True)
    title = orm.Required(str)
    pages = orm.Optional(int)
    author = orm.Required(Author)


db.generate_mapping(create_tables=True)


@orm.db_session
def main():
    names = ['Bob', 'Kate', 'Nick']
    authors = list()

    for name in names:
        authors.append(Author(name=name))

    for i in range(1, 20):
        Books(title=f'Book{i}', pages=i**2, author=choice(authors))

    db.commit()

    books = orm.select(book for book in Books if book.author.name == 'Bob')
    print(books.show())


if __name__ == '__main__':
    main()
