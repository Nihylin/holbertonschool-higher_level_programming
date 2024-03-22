-- create devcontainer.json & docker-compose.yml files
-- setup said files
-- open in container
-- cat ./SQL_introduction/16-no_link.sql | mysql -hlocalhost -uroot -p
-- tada
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
