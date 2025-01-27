import pandas as pd

# Load the dataset for October 2019
correct_green_taxi_data_path = '/mnt/data/green_tripdata_2019-10.csv'
green_taxi_data = pd.read_csv(correct_green_taxi_data_path)

# Convert pickup datetime to datetime format
green_taxi_data['lpep_pickup_datetime'] = pd.to_datetime(green_taxi_data['lpep_pickup_datetime'])

# Filter data for October 2019
october_data = green_taxi_data[
    (green_taxi_data['lpep_pickup_datetime'] >= '2019-10-01') &
    (green_taxi_data['lpep_pickup_datetime'] < '2019-11-01')
]

# Calculate trip segmentation counts
october_trip_segmentation = {
    "up_to_1_mile": (october_data['trip_distance'] <= 1).sum(),
    "between_1_and_3_miles": ((october_data['trip_distance'] > 1) & (october_data['trip_distance'] <= 3)).sum(),
    "between_3_and_7_miles": ((october_data['trip_distance'] > 3) & (october_data['trip_distance'] <= 7)).sum(),
    "between_7_and_10_miles": ((october_data['trip_distance'] > 7) & (october_data['trip_distance'] <= 10)).sum(),
    "over_10_miles": (october_data['trip_distance'] > 10).sum(),
}

# Output the results
october_trip_segmentation