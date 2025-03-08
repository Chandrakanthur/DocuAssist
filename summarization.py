import re
import spacy
import subprocess
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Ensure spaCy model is installed
def load_spacy_model(model_name="en_core_web_sm"):
    try:
        return spacy.load(model_name)
    except OSError:
        print(f"Downloading {model_name} model...")
        subprocess.run(["python", "-m", "spacy", "download", model_name], check=True)
        return spacy.load(model_name)

# Load NLP model
nlp = load_spacy_model()

def clean_text(text):
    """Cleans the text by removing special characters, extra spaces, and stopwords."""
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    doc = nlp(text)
    cleaned_text = " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])
    return cleaned_text

def summarize_text(text, sentence_count=5):
    """Summarizes the text using LSA (Latent Semantic Analysis)."""
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)


