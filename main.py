import pandas as pd
import numpy as np

def analyze_sales_data(file_path):
    """
    Load customer sales data and print summary statistics
    """
    try:
        df = pd.read_csv(file_path)
        print("--- Dataset Info ---")
        print(df.head(), "\n")
        
        total_sales = df['Amount'].sum()
        avg_rating = df['Rating'].mean()
        
        print(f"Total Sales Amount: ${total_sales:.2f}")
        print(f"Average Customer Rating: {avg_rating:.2f} / 5.0")
        
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")

if __name__ == "__main__":
    print("Running Customer Sales Analysis...\n")
    analyze_sales_data("data/customer_sales.csv")
