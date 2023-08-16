-- top 3 cities temp
SELECT city, AVG(value) AS avg_temp
FROM temperatures
-- filter by date 
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
-- set the limit to 3 as top 3
LIMIT 3;