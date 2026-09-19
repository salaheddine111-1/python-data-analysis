import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_and_visualize(file_path):
    """
    Load customer sales data, print statistics, and save a visualization chart
    """
    try:
        # Load dataset
        df = pd.read_csv(file_path)
        print("--- Dataset Info ---")
        print(df.head(), "\n")
        
        # Calculations
        total_sales = df['Amount'].sum()
        avg_rating = df['Rating'].mean()
        
        print(f"Total Sales Amount: ${total_sales:.2f}")
        print(f"Average Customer Rating: {avg_rating:.2f} / 5.0\n")
        
        # Group sales by category for visualization
        category_sales = df.groupby('Category')['Amount'].sum()
        
        # Create a bar chart
        plt.figure(figsize=(8, 5))
        category_sales.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.title('Total Sales by Category')
        plt.xlabel('Category')
        plt.ylabel('Sales Amount ($)')
        plt.xticks(rotation=0)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Save the figure to the outputs directory
        output_path = 'outputs/sales_by_category.png'
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
        
        print(f"Visualization successfully saved to '{output_path}'!")
        
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")

if __name__ == "__main__":
    print("Running Customer Sales Analysis & Visualization...\n")
    analyze_and_visualize("data/customer_sales.csv")
