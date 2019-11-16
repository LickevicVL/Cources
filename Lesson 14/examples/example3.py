from random import sample
from datetime import datetime

from pony import orm


db = orm.Database()
db.bind(provider='sqlite', filename='books.sqlite', create_db=True)


class Author(db.Entity):
    name = orm.Required(str)
    books = orm.Set(lambda: Books)


class Books(db.Entity):
    book_id = orm.PrimaryKey(int, auto=True)
    title = orm.Required(str)
    pages = orm.Optional(int)
    authors = orm.Set(Author)
    created_date = orm.Required(datetime, default=datetime.now)


db.generate_mapping(create_tables=True)


@orm.db_session
def main():
    names = ['Bob', 'Kate', 'Nick']
    authors = list()

    for name in names:
        authors.append(Author(name=name))

    for i in range(1, 10):
        Books(title=f'Book{i}', pages=i**2, authors=sample(authors, 2))

    db.commit()

    books = orm.select(
        (orm.count(book.title), author.name)
        for book in Books
        for author in Author
        if author.name in ['Bob', 'Kate'] and author in book.authors
        and book.created_date >= datetime(year=2019, month=11, day=15)
    )
    print(books.show())


if __name__ == '__main__':
    main()
