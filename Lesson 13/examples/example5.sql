CREATE TABLE IF NOT EXISTS AUTHOR (
  author_id SERIAL PRIMARY KEY,
  name VARCHAR(32)
);


CREATE TABLE BOOKS (
  book_id SERIAL PRIMARY KEY,
  name VARCHAR(32),
  created_time TIME DEFAULT CURRENT_TIME,
  author_id INT,
  FOREIGN KEY (author_id) REFERENCES AUTHOR (author_id)
);


INSERT INTO AUTHOR (name) VALUES ('Bob'), ('Kate'), ('Nick');

SELECT * FROM AUTHOR;

INSERT INTO BOOKS (name, author_id) VALUES
  ('Book1', 3),
  ('Book2', 1),
  ('Book3', 2);

SELECT * FROM BOOKS;

SELECT BOOKS.name, BOOKS.created_time, AUTHOR.name FROM BOOKS JOIN AUTHOR on BOOKS.author_id = AUTHOR.author_id;

INSERT INTO BOOKS (name, author_id) VALUES ('Book4', NULL);
INSERT INTO AUTHOR (name) VALUES ('Alex');

SELECT BOOKS.name, BOOKS.created_time, AUTHOR.name FROM BOOKS LEFT JOIN AUTHOR on BOOKS.author_id = AUTHOR.author_id;
SELECT BOOKS.name, BOOKS.created_time, AUTHOR.name FROM BOOKS RIGHT JOIN AUTHOR on BOOKS.author_id = AUTHOR.author_id;
