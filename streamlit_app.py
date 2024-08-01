import streamlit as st
import pandas as pd

st.title("DiRA: Disaster Response Assistance")
st.write("A Decision Support System for better Disaster Response Management.")
st.write("Upload a CSV file for analysis.")

uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

df = pd.read_csv(uploaded_file)

st.write("Here's the data from your CSV file:")
st.write(df)
