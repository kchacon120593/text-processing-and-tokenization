import pandas as pd

def basic_cleaning(df: pd.DataFrame, col: str = 'text'):
    
    """_summary_

    Returns:
        _type_: _description_
    """
       
    df_cleaned = df[[col]].copy()
    
    # Casting all columns to string type to avoid type errors
    df_cleaned[col] = df_cleaned[col].astype('str')
            
    # Lowercase all text data in the specified columns
    for col in df_cleaned.columns:
        df_cleaned[col] = df_cleaned[col].str.lower()

    # Remove URLs from all text data
    df_cleaned[col] = df_cleaned[col].str.replace(r'http\S+|www\S+|https\S+', '', regex=True)
    
    # Remove mentions (e.g., @username) from all text data
    df_cleaned[col] = df_cleaned[col].str.replace(r'@\w+', '', regex=True)
    
    # Remove hashtags (e.g., #hashtag) from all text data
    df_cleaned[col] = df_cleaned[col].str.replace(r'#\w+', '', regex=True)
        
    # Remove special characters and punctuation from all text data
    df_cleaned[col] = df_cleaned[col].str.replace(r'[^\w\s]', '', regex=True)
    
    # Remove numbers from all text data
    df_cleaned[col] = df_cleaned[col].str.replace(r'\d+', '', regex=True)
    
    # Remove extra whitespace from all text data
    df_cleaned[col] = df_cleaned[col].str.replace(r'\s+', ' ', regex=True).str.strip()
    
    # Remove rows with any NaN values
    df_cleaned = df_cleaned.dropna()
    
    # Remove duplicate rows
    df_cleaned = df_cleaned.drop_duplicates()
    
    # Reset index after cleaning
    df_cleaned = df_cleaned.reset_index(drop=True)

    return df_cleaned
    
    
    
    
    