-- lists cities
-- and state names
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states ON states.id = cities.state_id
ORDER BY cities.id ASC;
