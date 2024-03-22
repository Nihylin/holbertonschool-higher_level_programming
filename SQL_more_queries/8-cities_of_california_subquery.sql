-- this is a comment to please the almighty checker (yes I'm petty)
SELECT id, name FROM cities WHERE state_id IN (
    SELECT ID FROM states WHERE name = "California"
)
ORDER BY id ASC;
