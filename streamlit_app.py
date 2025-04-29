import streamlit as st
import pandas as pd

file = st.file_uploader("Upload file", type=["csv"])

if file is not None:
  df = pd.read_csv(file)
  st.write(df)
