
import spacy
import pandas as pd

def tokenize_dataframe_column(df, column='text'):
    """
    Tokenizes each row in the specified column of a DataFrame using spaCy, filtering out stop words and non-alphabetic tokens.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame containing the text data.
    column (str): The name of the column to tokenize. Default is 'text'.
    
    Returns:
    list: A list of filtered tokens.
    """
        
    nlp = spacy.load("en_core_web_sm")  # Load the small English model
    
    tokens = [] # Initialize an empty list to store tokens
    
    for doc in nlp.pipe(df[column], batch_size=1000):
        tokens.extend([token.text for token in doc if not token.is_stop and token.is_alpha]) # Filter out stop words and non-alphabetic tokens
    return tokens

def tokenize_text(corpus):
    """
    Tokenizes the input text using spaCy, filtering out stop words and non-alphabetic tokens.
    
    Parameters:
    corpus (str): The input text to be tokenized.
    
    Returns:
    list: A list of filtered tokens.
    """
    # Load the spaCy model
    nlp = spacy.load("en_core_web_sm")  # Load the small English model
    
    # Tokenize the text
    doc = nlp(corpus)

    filtered_tokens = [token.corpus for token in doc if not token.is_stop and token.is_alpha] #filtering out stop words and non-alphabetic tokens
    
    return filtered_tokens


def tokenize_corpus(corpus):
    """
    Tokenizes the input corpus, which can be a DataFrame or a string.
    
    Parameters:
    corpus (pd.DataFrame or str): The input corpus to be tokenized.

    Returns:
    list: A flat list of filtered tokens.
    """
    if not isinstance(corpus, (pd.DataFrame, str)):
        raise TypeError("Input must be a pandas DataFrame or a string.")

    if isinstance(corpus, pd.DataFrame):
        if 'text' not in corpus.columns:
            raise ValueError("DataFrame must contain a 'text' column for tokenization.")
        return tokenize_dataframe_column(corpus)
    
    elif isinstance(corpus, str):
        return tokenize_text(corpus)
