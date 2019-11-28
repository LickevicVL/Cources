import psycopg2

connector = psycopg2.connect(
    host='localhost',
    port=5432,
    user='user',
    password='password',
    database='books'
)

cur = connector.cursor()

# execute
cur.execute('''INSERT INTO AUTHOR (name) VALUES ('Nichol')''')
cur.execute(
    '''INSERT INTO BOOKS (name, author_id) VALUES (%s, %s)''',
    ('NewBook', 1)
)
connector.commit()

# select
cur.execute(
    '''SELECT * from BOOKS WHERE author_id = %s AND created_time >= %s''',
    (1, '12:00:00',)
)
rows = cur.fetchall()
for row in rows:
    print(row)
