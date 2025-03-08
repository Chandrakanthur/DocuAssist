import re
import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Load NLP model
nlp = spacy.load("en_core_web_sm")

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

# Read the document
with open("large_document.txt", "r", encoding="utf-8") as file:
    document_text = file.read()

# Clean and summarize
cleaned_text = clean_text(document_text)
summary = summarize_text(cleaned_text)

print("Summarized Text:\n", summary)
