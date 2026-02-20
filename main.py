from preprocessing import preprocess_text
from sentiment import predict_sentiment


with open("data.txt", "r", encoding="utf-8") as file:
    texts = file.readlines()


print("NLP SENTIMENT ANALYSIS RESULTS\n")


for text in texts:
    clean_text = preprocess_text(text)
    sentiment = predict_sentiment(clean_text)


    print("Original :", text.strip())
    print("Processed:", clean_text)
    print("Sentiment:", sentiment)
    print("-" * 40)