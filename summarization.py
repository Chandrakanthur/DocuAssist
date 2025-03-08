import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text) # remove punctuation
    text = re.sub(r'\d+', '', text) # remove numbers
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords]
    return tokens

def summarize_text(text, num_sentences=3):
    sentences = sent_tokenize(text)
    if not sentences:
        return "No sentences to summarize."

    word_frequencies = {}
    for sentence in sentences:
        tokens = clean_text(sentence)
        for token in tokens:
            word_frequencies[token] = word_frequencies.get(token, 0) + 1

    sentence_scores = {}
    for sentence in sentences:
        tokens = word_tokenize(sentence)
        for token in tokens:
            if token in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[token]

    scored_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    summary_sentences = [sentence for sentence, score in scored_sentences[:num_sentences]]
    summary = " ".join(summary_sentences)
    return summary
