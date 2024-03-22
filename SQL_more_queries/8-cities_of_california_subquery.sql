SELECT id, name FROM cities WHERE state_id IN (
    SELECT ID FROM states WHERE name = "California"
)
ORDER BY id ASC;
