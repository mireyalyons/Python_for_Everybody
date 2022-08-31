CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Cassie', 31);
INSERT INTO Ages (name, age) VALUES ('Samar', 25);
INSERT INTO Ages (name, age) VALUES ('Bruin', 13);
INSERT INTO Ages (name, age) VALUES ('Azlan', 30);
INSERT INTO Ages (name, age) VALUES ('Kern', 21);
INSERT INTO Ages (name, age) VALUES ('Shannon', 23);

SELECT hex(name || age) AS X FROM Ages ORDER BY X
