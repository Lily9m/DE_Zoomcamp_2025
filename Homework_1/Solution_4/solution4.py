import pandas as pd

# Load the dataset for October 2019
green_taxi_data_path = '/mnt/data/green_tripdata_2019-10.csv'
green_taxi_data = pd.read_csv(green_taxi_data_path)

# Convert pickup datetime to datetime format
green_taxi_data['lpep_pickup_datetime'] = pd.to_datetime(green_taxi_data['lpep_pickup_datetime'])

# Filter data for October 2019
october_data = green_taxi_data[
    (green_taxi_data['lpep_pickup_datetime'] >= '2019-10-01') &
    (green_taxi_data['lpep_pickup_datetime'] < '2019-11-01')
]

# Group by the pickup day and find the longest trip distance for each day
longest_trip_per_day = october_data.groupby(october_data['lpep_pickup_datetime'].dt.date)['trip_distance'].max()

# Find the day with the longest trip distance overall
longest_trip_day = longest_trip_per_day.idxmax()
longest_trip_distance = longest_trip_per_day.max()

# Output the results
longest_trip_day, longest_trip_distance