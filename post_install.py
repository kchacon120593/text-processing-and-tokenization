
import spacy
import importlib.util
from spacy.cli import download
from spacy.util import is_package


def ensure_spacy_model(model_name="en_core_web_sm"):
    print(f"Checking for spaCy model: {model_name}")

    try:
        # Try to load the model directly
        spacy.load(model_name)
        print(f"✅ Model '{model_name}' is already installed.")
    except OSError:
        print(f"⬇️ Model '{model_name}' not found. Attempting to download...")
        try:
            download(model_name)
            print(f"✅ Successfully downloaded '{model_name}'.")
        except Exception as e:
            print(f"❌ Failed to download '{model_name}': {e}")

def restart_kernel():
    from IPython.display import display, Javascript
    display(Javascript("Jupyter.notebook.kernel.restart()"))
