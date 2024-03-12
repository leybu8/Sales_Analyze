import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
data = pd.read_csv('sales_data.csv')

# Display the first few rows of the DataFrame
print("First few rows of the data:")
print(data.head())

# Basic statistics of the revenue column
print("\nSummary statistics of the revenue column:")
print(data['Revenue'].describe())

# Total revenue
total_revenue = data['Revenue'].sum()
print(f"\nTotal revenue: ${total_revenue}")

# Visualization: Revenue trends over time
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Revenue'], marker='o', linestyle='-')
plt.title('Revenue Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
