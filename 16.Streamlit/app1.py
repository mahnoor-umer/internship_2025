import streamlit as st
from collections import Counter


## Title
st.title("Text Analyzer Web App")

## Text Input area
user_text= st.text_area("Enter your text here:")

## Button to analyze text
if st.button("Analyze"):
    if user_text.strip() != "":

        ## Remove leading spaces 
        text = user_text.strip()

        ## Number of characters with spaces
        num_chars_with_spaces = len(text)

        ## Number of characters without spaces
        num_chars_without_spaces = len(text.replace(" ", ""))

        ## Split text into words
        words = text.split()

        ## Number of words
        num_words = len(words)

        ## Most common word
        word_counts = Counter(words)
        most_common_word = word_counts.most_common(1)[0]

        ## Display results
        st.subheader("Analysis Results")
        st.write(f"Number of characters with spaces: {num_chars_with_spaces}")
        st.write(f"Number of characters without spaces: {num_chars_without_spaces}")
        st.write(f"Number of words: {num_words}")
        st.write(f"Most common word: {most_common_word[0]} with a frequency of {most_common_word[1]}")
    else:
        st.warning("Please enter some text to analyze.")