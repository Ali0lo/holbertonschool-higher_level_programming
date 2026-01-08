-- List all cities with their corresponding state names
SELECT cities.id, cities.name, 
       (SELECT name FROM states WHERE id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
