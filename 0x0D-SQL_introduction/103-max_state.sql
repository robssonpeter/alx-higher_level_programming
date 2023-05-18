-- Average temp
-- Based on cities
SELECT state, MAX(value) AS max_temp temperatures
GROUP BY state;
