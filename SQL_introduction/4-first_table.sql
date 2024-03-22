-- create devcontainer.json & docker-compose.yml files
-- setup said files
-- open in container
-- cat ./SQL_introduction/4-first_table.sql | mysql -hlocalhost -uroot -p
-- tada
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
