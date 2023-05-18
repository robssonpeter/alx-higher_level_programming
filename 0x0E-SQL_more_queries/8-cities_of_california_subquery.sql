-- List items
-- List items of the states table
SELECT * FROM TABLE cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
