-- create devcontainer.json & docker-compose.yml files
-- setup said files
-- open in container
-- cat ./SQL_introduction/8-count_89.sql | mysql -hlocalhost -uroot -p
-- tada
SELECT COUNT(*) FROM first_table WHERE id = 89;
