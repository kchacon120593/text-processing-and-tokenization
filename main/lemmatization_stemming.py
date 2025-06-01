import spacy
import nlkt


def lemmatize_text(text):
    """
    Lemmatize the input text using spaCy.

    Parameters:
    text (str): The text to be lemmatized.

    Returns:
    list: A list of lemmas.
    """
    # Load the spaCy model
    nlp = spacy.load("en_core_web_sm") #Core English model
    
    # Ensure the text is a string
    if not isinstance(text, str):
        raise ValueError("Input text must be a string.")
    
    # Process the text with spaCy
    if not text:
        return []  # Return an empty list if the text is empty
    
    # Lemmatize the text
    doc = nlp(text)
    return [token.lemma_ for token in doc]
