-- Average temp
-- Based on cities
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city;
