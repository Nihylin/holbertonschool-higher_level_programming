-- create devcontainer.json & docker-compose.yml files
-- setup said files
-- open in container
-- cat ./SQL_introduction/14-average.sql | mysql -hlocalhost -uroot -p
-- tada
SELECT AVG(score) AS average FROM second_table;
