import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name= st.text_input("Enter your name:")
if name:
    st.write(f"Salam, {name}!")


age= st.slider("Select your age:",0,100,25)
st.write( f"Your age is {age}")

options= ['Python', 'Java', 'C++', 'JavaScript']
choice= st.selectbox("Choose your favorite programming language:", options)
st.write(f"Your selected {choice}")

data= {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Country': ['USA', 'UK', 'Australia', 'Pakistan']
}

df= pd.DataFrame(data)
df.to_csv= ('Sampledata.csv')
st.write(df)

uploaded_file= st.file_uploader("Choose a CSV file ",type="CSV")

if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.write(df)