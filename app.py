import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

if option == 'Email':
    st.write('1')
else:
    st.write('Else')
