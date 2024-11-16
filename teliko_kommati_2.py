import pandas as pd
import matplotlib.pyplot as plt

# Load the processed data
most_popular = pd.read_csv('most_popular_items.csv')
store_sales_percentage = pd.read_csv('store_sales_percentage.csv', index_col=0, squeeze=True)

# Visualization 1: Bar chart for most popular items by zip code
plt.figure(figsize=(12, 6))
most_popular.groupby('zip_code')['bottles_sold'].sum().plot(kind='bar', color='skyblue')
plt.title('Most Popular Items by Zip Code (2016-2019)', fontsize=14)
plt.xlabel('Zip Code', fontsize=12)
plt.ylabel('Total Bottles Sold', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('most_popular_items_chart.png')
plt.show()

# Visualization 2: Pie chart for sales percentage per store
plt.figure(figsize=(10, 8))
store_sales_percentage.plot(kind='pie', autopct='%1.1f%%', cmap='tab10', legend=True)
plt.title('Percentage of Sales per Store (2016-2019)', fontsize=14)
plt.ylabel('')
plt.tight_layout()
plt.savefig('store_sales_percentage_chart.png')
plt.show()

print("Visualizations saved as 'most_popular_items_chart.png' and 'store_sales_percentage_chart.png'.")
