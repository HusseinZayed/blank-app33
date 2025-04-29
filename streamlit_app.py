import streamlit as st

st.title("🎈 My new app")
if shape=='Circle':
    r = st.number_input('Reduis: ',1.0,step=.1,max_value=10.0)
    area = 3.14*2*r
else:
    w = st.number_input('width: ',1.0,step=.1,max_value=10.0)
    h = st.number_input('Height: ',1.0,step=.1,max_value=10.0)
    area = w*h

show_btn = st.button('show area')
if show_btn:
    st.write(area)
