import pandas as pd

# Create a simple dataset
data = {
    'Category': ['Electronics', 'Clothing', 'Books', 'Electronics', 'Clothing'],
    'Sales': [1200, 450, 200, 1500, 600],
    'Quantity': [4, 10, 5, 5, 12]
}

df = pd.DataFrame(data)

# Display basic stats
print("--- Dataset Overview ---")
print(df.head())

print("\n--- Total Sales by Category ---")
category_sales = df.groupby('Category')['Sales'].sum()
print(category_sales)
