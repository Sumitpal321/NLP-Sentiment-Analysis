import streamlit as st
from preprocessing import preprocess_text
from sentiment import predict_sentiment

st.set_page_config(page_title="NLP Sentiment Analyzer")

st.title("🧠 NLP Sentiment Analysis")

# Option 1: Manual text input
st.subheader("Enter Text Manually")
user_input = st.text_area("Type your sentence here")

if st.button("Analyze Text"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        clean_text = preprocess_text(user_input)
        sentiment = predict_sentiment(clean_text)

        st.write("Original:", user_input)
        st.write("Processed:", clean_text)
        st.write("Sentiment:", sentiment)

        if sentiment.lower() == "positive":
            st.success("😊 Positive")
        elif sentiment.lower() == "negative":
            st.error("😡 Negative")


# Option 2: Analyze data.txt file
st.subheader("Analyze data.txt File")

if st.button("Analyze data.txt"):
    with open("data.txt", "r", encoding="utf-8") as file:
        texts = file.readlines()

    for text in texts:
        clean_text = preprocess_text(text)
        sentiment = predict_sentiment(clean_text)

        st.write("---")
        st.write("Original:", text.strip())
        st.write("Processed:", clean_text)
        st.write("Sentiment:", sentiment)