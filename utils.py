import spacy
import subprocess
import sys
import streamlit as st

@st.cache_resource
def load_spacy_model():
    """
    Loads the spaCy English model. If not found, downloads it automatically.
    """
    model_name = "en_core_web_sm"
    try:
        nlp = spacy.load(model_name)
    except OSError:
        print(f"Downloading spaCy model {model_name}...")
        subprocess.check_call([sys.executable, "-m", "spacy", "download", model_name])
        nlp = spacy.load(model_name)
    return nlp
