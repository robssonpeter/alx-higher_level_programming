-- Average temp
-- Based on cities
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
