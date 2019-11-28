import sqlite3

connector = sqlite3.connect('books.sqlite')
cur = connector.cursor()

# execute
cur.execute('''INSERT INTO AUTHOR (name) VALUES ('Nichol')''')
cur.execute(
    '''INSERT INTO BOOKS (name, author_id) VALUES (?, ?)''',
    ('NewBook', 1)
)
connector.commit()

# select
cur.execute(
    '''SELECT * from BOOKS WHERE author_id = ? AND created_time >= ?''',
    (1, '12:00:00',)
)
rows = cur.fetchall()
for row in rows:
    print(row)
