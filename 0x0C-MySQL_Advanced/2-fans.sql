-- SQL script that ranks country origins of bands, ordered by the name
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ASC ORDER BY nb_fans DESC;