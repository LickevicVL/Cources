CREATE TABLE IF NOT EXISTS BOOKS (
  name VARCHAR(32),
  author VARCHAR(32),
  created_date DATE NULL DEFAULT CURRENT_DATE
);

INSERT INTO BOOKS (name, author, created_date) VALUES (
  'Book1',
  'Bob',
  '2019-01-01'
);

INSERT INTO BOOKS (name, author) VALUES (
  'Book2',
  'Kate'
);

SELECT * FROM BOOKS;
