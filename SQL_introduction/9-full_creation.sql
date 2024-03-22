-- create devcontainer.json & docker-compose.yml files
-- setup said files
-- open in container
-- cat ./SQL_introduction/9-full_creation.sql | mysql -hlocalhost -uroot -p
-- tada
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

INSERT INTO second_table (id, name, score)
    VALUES (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);
