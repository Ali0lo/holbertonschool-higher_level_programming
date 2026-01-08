-- List all cities with their corresponding state names in a single SELECT statement
SELECT cities.id, cities.name, 
       (SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
