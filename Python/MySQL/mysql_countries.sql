USE world;
-- Query 1
SELECT countries.name, languages.language AS language, languages.percentage AS percentage 
FROM countries
JOIN languages ON languages.country_id = countries.id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;
-- Query 2
SELECT countries.name, count(cities.id) as total_cities
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY total_cities DESC
;
-- Query 3
SELECT cities.name, cities.population
FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE countries.name = 'Mexico'
ORDER BY cities.population DESC;
-- Query 4
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON languages.country_id = countries.id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;
-- Query 5
SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE surface_area < 501 and population > 100000;
-- Query 6
SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy' and capital > 200 and life_expectancy > 75;
-- Query 7
SELECT countries.name, cities.name, cities.district, cities.population
FROM cities
JOIN countries ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population > 500000;
-- Query 8
SELECT region, count(name) as num_countries
FROM countries
GROUP BY region
ORDER BY num_countries DESC;
