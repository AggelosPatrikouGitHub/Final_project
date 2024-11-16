import pandas as pd

# Load the dataset
data = pd.read_csv('liquor_sales_2016_2019.csv')

# Find the most popular item per zip code
popular_items = data.groupby(['zip_code', 'item_description'])['bottles_sold'].sum().reset_index()
most_popular = popular_items.loc[popular_items.groupby('zip_code')['bottles_sold'].idxmax()]

# Save most popular items to CSV
most_popular.to_csv('most_popular_items.csv', index=False)

# Calculate the percentage of sales per store
store_sales = data.groupby('store_number')['sale_dollars'].sum()
store_sales_percentage = (store_sales / store_sales.sum()) * 100

# Save sales percentages to CSV
store_sales_percentage.to_csv('store_sales_percentage.csv', header=True)

print("Data processing complete. Results saved to 'most_popular_items.csv' and 'store_sales_percentage.csv'.")
