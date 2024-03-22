-- create devcontainer.json & docker-compose.yml files
-- setup said files
-- open in container
-- cat ./SQL_introduction/11-best_score.sql | mysql -hlocalhost -uroot -p
-- tada
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
