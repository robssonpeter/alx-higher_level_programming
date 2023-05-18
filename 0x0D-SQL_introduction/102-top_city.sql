-- Average temp
-- Based on cities
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month >=
7 AND month <= 8 GROUP BY city ORDER BY AVG(value) DESC LIMIT 3;
