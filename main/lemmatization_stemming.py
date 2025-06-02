import spacy
from spacy.tokens import Doc

# Load spaCy model once (better performance if reused)


def lemmatize_text(tokens):
    """
    Lemmatize a list of tokens using spaCy.
    
    Parameters:
    tokens (list): List of word tokens.
    
    Returns:
    tuple: (lemmas, pos_tags, ner) from the processed Doc.
    """
    
    nlp = spacy.load("en_core_web_sm", disable=["tok2vec"])  # disable vectorization to save memory
    
    if not isinstance(tokens, list):
        raise ValueError("Input must be a list of tokens.")
    if not tokens:
        return [], [], []

    # Create spaCy Doc from tokens
    doc = Doc(nlp.vocab, words=tokens)

    # Run remaining pipeline (e.g., tagger, parser, ner)
    for name, proc in nlp.pipeline:
        try:
            doc = proc(doc)
        except MemoryError:
            print(f"MemoryError on pipeline stage: {name}")
            return [], [], []

    # Extract outputs
    lemmas = [token.lemma_ for token in doc]
    pos_tags = [token.pos_ for token in doc]
    ner = [(ent.text, ent.label_) for ent in doc.ents]

    return lemmas, pos_tags, ner