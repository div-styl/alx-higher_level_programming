-- order the data with name accordingly with score
SELECT score, name
FROM second_table
WHERE name !=""
ORDER BY score DESC;
