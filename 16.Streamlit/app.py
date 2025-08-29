import streamlit as st
import pandas as pd
import numpy as np


## Title of application
st.title("Hi Streamlit")

## Display a text
st.write("This is a text")

## Create a simple dataframe
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30]
})

## Display the dataframe
st.write("Here is the dataframe")
st.write(df)

## Create a line chart
chart_data=pd.DataFrame(
    np.random.randn(10, 2),columns= ['A', 'B']
)
st.line_chart(chart_data)