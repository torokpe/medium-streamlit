import streamlit as st

a = st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder="Choose an option", disabled=False, label_visibility="visible")
st.write(f"Hi {a}")
