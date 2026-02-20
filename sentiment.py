positive_words = [
    "love", "excellent", "good", "happy", "helpful", "clear", "best"
]


negative_words = [
    "bad", "poor", "worst", "waste", "hate", "slow"
]


def predict_sentiment(text):
    pos_score = 0
    neg_score = 0


    for word in text.split():
        if word in positive_words:
            pos_score += 1
        elif word in negative_words:
            neg_score += 1


    if pos_score > neg_score:
        return "Positive"
    elif neg_score > pos_score:
        return "Negative"
    else:
        return "Neutral"
