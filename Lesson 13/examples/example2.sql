CREATE TABLE IF NOT EXISTS BOOKS (
  name VARCHAR(32),
  created_date DATE NULL DEFAULT CURRENT_DATE,
  pages INTEGER
);

INSERT INTO BOOKS VALUE ('Book1', '2018-01-01', 253);

INSERT INTO BOOKS (name, created_date, pages) VALUES
  ('Book2', '2018-01-01', 1000),
  ('Book3', '2018-01-02', 1),
  ('Book4', '2010-11-01', 100),
  ('Book100', '1901-02-01', 15),
  ('Some Book', '2017-05-07', 1234),
  ('Who I am?', '1800-07-23', 153),
  ('1Q89', '1992-05-07', 854);


SELECT AVG(pages) as pages FROM BOOKS WHERE created_date >= '2018-01-01';
