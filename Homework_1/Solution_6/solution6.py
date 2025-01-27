# Find the largest tip for pickups in "East Harlem North"
largest_tip = (
    pickup_analysis[pickup_analysis['Zone'] == 'East Harlem North']
    .merge(zone_lookup_data, left_on='DOLocationID', right_on='LocationID', how='left')
    .loc[:, ['Zone_y', 'tip_amount']]
    .sort_values(by='tip_amount', ascending=False)
    .iloc[0]
)

# Output the result
largest_tip