SELECT
    zdo.Zone AS dropoff_zone,
    MAX(f.tip_amount) AS largest_tip
FROM green_taxi_data f
JOIN taxi_zone_lookup zpu ON f.PULocationID = zpu.LocationID
JOIN taxi_zone_lookup zdo ON f.DOLocationID = zdo.LocationID
WHERE zpu.Zone = 'East Harlem North'
  AND lpep_pickup_datetime >= '2019-10-01'
  AND lpep_pickup_datetime < '2019-11-01'
GROUP BY zdo.Zone
ORDER BY largest_tip DESC
LIMIT 1;