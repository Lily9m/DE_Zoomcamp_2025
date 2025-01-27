SELECT
    DATE(lpep_pickup_datetime) AS pickup_date,
    MAX(trip_distance) AS longest_trip_distance
FROM green_taxi_data
WHERE lpep_pickup_datetime >= '2019-10-01'
  AND lpep_pickup_datetime < '2019-11-01'
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY longest_trip_distance DESC
LIMIT 1;