# Import necessary libraries for data analysis
import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Function to load dataset using Pandas
    """
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return df
    except FileNotFoundError:
        print(f"File not found at {file_path}")
        return None

if __name__ == "__main__":
    print("Python Data Analysis environment is ready.")
