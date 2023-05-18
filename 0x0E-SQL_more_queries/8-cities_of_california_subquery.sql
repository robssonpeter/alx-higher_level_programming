-- List items
-- List items of the states table
SELECT * FROM TABLE cities
WHERE state_id = (SELECT id FROM states)
ORDER BY id ASC;
