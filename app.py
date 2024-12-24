import streamlit as st

option = st.selectbox(
    "How would you like to be contacted?",
    ("Hétfőn reggeli imádság", "Hétfőn estvéli imádság", 
     "Kedden reggeli imádság", "Kedden estvéli imádság",
     "Szerdán reggeli imádság", "Szerdán estvéli imádság",
     "Csütörtökön reggeli imádság", "Csütörtökön estvéli imádság",
     "Pénteken reggeli imádság", "Pénteken estvéli imádság",
     "Szombaton reggeli imádság", "Szombaton estvéli imádság"
    )
)

if option == 'Email':
    st.write('1')
else:
    st.write('Else')
