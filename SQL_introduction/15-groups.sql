-- create devcontainer.json & docker-compose.yml files
-- setup said files
-- open in container
-- cat ./SQL_introduction/15-groups.sql | mysql -hlocalhost -uroot -p
-- tada
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
