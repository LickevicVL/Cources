from pony import orm


db = orm.Database()
db.bind(provider='sqlite', filename='books.sqlite', create_db=True)


class Books(db.Entity):
    book_id = orm.PrimaryKey(int, auto=True)
    title = orm.Required(str)
    pages = orm.Optional(int)


db.generate_mapping(create_tables=True)


@orm.db_session
def main():
    for i in range(1, 10):
        Books(title=f'Book{i}', pages=i**2)

    db.commit()

    book1 = Books[1]
    print(book1.book_id)

    book3 = Books.get(title='Book3')
    print(book3.title)

    books = orm.select(book for book in Books if book.pages >= 20)
    for book in books:
        print(book)


if __name__ == '__main__':
    main()
