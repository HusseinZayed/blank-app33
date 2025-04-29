import streamlit as st
import pandas as pd

file = st.file_uploader("Upload file", type=["csv"])

if file is not None:
  df = pd.read_csv(file)
  n_rows = st.slider('Choose number of rows to display', min_value=5, max_value=len(df), step=1)
  columns_to_show = st.multiselect("Select columns to show", df.columns.to_list(), default=df.columns.to_list())  
  st.write(df.loc[:n_rows,columns_to_show])
          
