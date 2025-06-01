import pandas as pd
import kagglehub


def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    try:
        columns = ['target','ids','date','flag','user','text']
        data = pd.read_csv(file_path, encoding="latin-1", header=None, names=columns)
        return data
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame() # Return an empty DataFrame on error

