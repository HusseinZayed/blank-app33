import streamlit as st

ls=[]
# Text input
user_input = st.text_input('Enter some text')

# Buttons
if st.button('Append'):
  ls.append(user_input)
  
if st.button('Clear'):
  ls = []

# Display the list
st.write('Text list:', ls) 
  


  
          
