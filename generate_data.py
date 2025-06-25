import pandas as pd
import numpy as np

num_rows = 23373

np.random.seed(42)

regions = ['West', 'East', 'South', 'Central']
segments = ['Consumer', 'Corporate', 'Home Office']
categories = ['Phones', 'Chairs', 'Binders', 'Storage', 'Accessories']
states = ['California', 'New York', 'Texas', 'Washington', 'Florida']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']

data = {
    'Order ID': [f'ORD{100000 + i}' for i in range(num_rows)],
    'Region': np.random.choice(regions, num_rows),
    'Segment': np.random.choice(segments, num_rows),
    'Category': np.random.choice(categories, num_rows),
    'State': np.random.choice(states, num_rows),
    'Month': np.random.choice(months, num_rows),
    'Sales': np.round(np.random.uniform(20.0, 2000.0, num_rows), 2),
    'Profit': np.round(np.random.uniform(-200.0, 500.0, num_rows), 2),
    'Order Quantity': np.random.randint(1, 11, num_rows),
    'Returns': np.random.choice([0, 1], num_rows, p=[0.95, 0.05])
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv('Retail_Supply_Chain_Data.csv', index=False)

print("CSV file 'Retail_Supply_Chain_Data.csv' generated successfully.")
