-- Import the metal_bands table dump before executing this script

-- Lists all bands with Glam rock as their main style,
-- ranked by their longevity
-- Column names must be: band_name and lifespan (in years until 2022)

SELECT band_name, IFNULL(split, 2022) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
