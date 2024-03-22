-- this is a comment to please the almighty checker (yes I'm petty)
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;
