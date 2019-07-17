-- find all cities from california
SELECT id,
name FROM cities
WHERE state_id = 1 GROUP BY id ASC;
