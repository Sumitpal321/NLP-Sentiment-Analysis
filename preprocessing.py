import nltk
import spacy
import re


nltk.download("punkt")
nltk.download("stopwords")


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))


def preprocess_text(text):
    # lowercase
    text = text.lower()


    # remove numbers
    text = re.sub(r"\d+", "", text)


    # remove punctuation
    text = re.sub(r"[^\w\s]", "", text)


    # tokenization
    tokens = word_tokenize(text)


    # stop words removal
    tokens = [word for word in tokens if word not in stop_words]


    # lemmatization using spaCy
    doc = nlp(" ".join(tokens))
    lemmas = [token.lemma_ for token in doc]


    return " ".join(lemmas)