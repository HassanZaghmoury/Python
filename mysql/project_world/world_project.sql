-- select * from countries.name, languages.language, languages.percentage
-- left join languages ON countries.id = languages.country_id
-- WHERE country.id = 1;
-- 1
select name, languages.language, languages.percentage
from countries
join languages on countries.id = languages.country_id
where language = "Slovene"
order by percentage desc;
-- 2
select countries.name, count(cities.id) as city_count
from countries
join citites on countries.id = cities.country_id
group by counties.name
order by city_count desc;

-- 3
select cities.name, cities.population
from cities
where country_code = 'MEX' AND cities.population > 500000
order by cities.population desc;

-- 4
select languages.language, languages.percentage
from languages
where languages.percentage > 89
order by languages.percentage desc;

-- 5
select countries.surface_area, countries.population
from countries
where countries.surface_area < 501 and countries.population > 100000
order by countries.population desc;

-- 6
select countries.name, countries.government_form, countries.capital, countries.life_expectancy
from countries
where countries.government_form = 'Constitutional Monarchy' and countries.capital > 200 and countries.life_expectancy > 75
order by countries.name desc;

-- 7
select countries.name, cities.name, cities.district, cities.population
from countries
join cities on countries.id = 'argentina' and cities.district = 'Buenos Aires' and cities.population > 500000
order by cities.population asc;

-- 8
select region, count(name) as country_count
from countries
group by region
order by country_count desc;



