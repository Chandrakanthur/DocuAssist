import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, num_sentences=3):
    """Summarizes the given text using extractive summarization."""
    sentences = sent_tokenize(text)
    if not sentences:
        return "No sentences to summarize."

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)

    sentence_scores = tfidf_matrix.sum(axis=1).A1
    sentence_score_pairs = list(zip(sentences, sentence_scores))
    sentence_score_pairs.sort(key=lambda x: x[1], reverse=True)

    summary_sentences = [pair[0] for pair in sentence_score_pairs[:num_sentences]]
    summary = " ".join(summary_sentences)
    return summary
