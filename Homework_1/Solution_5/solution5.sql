SELECT
    zpu.Zone AS pickup_zone,
    SUM(f.total_amount) AS total_amount
FROM green_taxi_data f
JOIN taxi_zone_lookup zpu ON f.PULocationID = zpu.LocationID
WHERE DATE(lpep_pickup_datetime) = '2019-10-18'
GROUP BY zpu.Zone
HAVING SUM(f.total_amount) > 13000
ORDER BY total_amount DESC;