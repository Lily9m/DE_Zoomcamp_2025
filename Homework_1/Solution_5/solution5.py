# Merge with the taxi zone lookup table
zone_lookup_path = '/mnt/data/taxi_zone_lookup.csv'
zone_lookup_data = pd.read_csv(zone_lookup_path)

pickup_analysis = october_data.merge(zone_lookup_data, left_on='PULocationID', right_on='LocationID', how='left')

# Group by the pickup zone and calculate total amount for 2019-10-18
pickup_zones_2019_10_18 = (
    pickup_analysis[pickup_analysis['lpep_pickup_datetime'].dt.date == pd.Timestamp("2019-10-18").date()]
    .groupby('Zone')
    .agg(total_amount=('total_amount', 'sum'))
    .reset_index()
)

# Filter for zones with total_amount > 13,000 and sort in descending order
top_pickup_zones = pickup_zones_2019_10_18[pickup_zones_2019_10_18['total_amount'] > 13000].sort_values(by='total_amount', ascending=False)

# Output the result
top_pickup_zones