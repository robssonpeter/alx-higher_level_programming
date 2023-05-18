-- Average temp
-- Based on cities
SELECT city, AVG(value) AS avg_temp
GROUP BY city;
