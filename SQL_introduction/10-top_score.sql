-- create devcontainer.json & docker-compose.yml files
-- setup said files
-- open in container
-- cat ./SQL_introduction/10-top_score.sql | mysql -hlocalhost -uroot -p
-- tada
SELECT score, name FROM second_table ORDER BY score DESC;
