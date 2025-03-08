import re
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()
    tokens = re.findall(r'\w+', text) # Simple regex word tokenization
    tokens = [word for word in tokens if word not in stopwords]
    return tokens

def split_sentences(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    return [sentence.strip() for sentence in sentences if sentence.strip()]

def summarize_text(text, num_sentences=3):
    sentences = split_sentences(text)
    if not sentences:
        return "No sentences to summarize."

    word_frequencies = {}
    for sentence in sentences:
        tokens = clean_text(sentence)
        for token in tokens:
            word_frequencies[token] = word_frequencies.get(token, 0) + 1

    sentence_scores = {}
    for sentence in sentences:
        tokens = clean_text(sentence) #use clean_text that is using regex
        for token in tokens:
            if token in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[token]

    scored_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    summary_sentences = [sentence for sentence, score in scored_sentences[:num_sentences]]
    summary = " ".join(summary_sentences)
    return summary
