import streamlit as st
import requests

option = st.selectbox(
    "Imádság kiválasztása:",
    ("Hétfőn reggeli imádság", "Hétfőn estvéli imádság", 
     "Kedden reggeli imádság", "Kedden estvéli imádság",
     "Szerdán reggeli imádság", "Szerdán estvéli imádság",
     "Csütörtökön reggeli imádság", "Csütörtökön estvéli imádság",
     "Pénteken reggeli imádság", "Pénteken estvéli imádság",
     "Szombaton reggeli imádság", "Szombaton estvéli imádság",
     "Vasárnap reggeli imádság", "Vasárnap estvéli imádság"
    )
)


url_mapping = {
    "Hétfőn reggeli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/hetfo_1.txt",
    "Hétfőn estvéli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/hefto_2.txt",
    "Kedden reggeli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/kedd_1.txt",
    "Kedden estvéli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/kedd_2.txt",
    "Szerdán reggeli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/szerda_1.txt",
    "Szerdán estvéli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/szerda_2.txt",
    "Csütörtökön reggeli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/csutortok_1.txt",
    "Csütörtökön estvéli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/csutortok_1.txt",
    "Pénteken reggeli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/pentek_1.txt",
    "Pénteken estvéli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/pentek_2.txt",
    "Szombaton reggeli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/szombat_1.txt",
    "Szombaton estvéli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/szombat_2.txt",
    "Vasárnap reggeli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/vasarnap_1.txt",
    "Vasárnap estvéli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/vasarnap_2.txt"
}

# Fetch and display the file content if the option matches
if option in url_mapping:
    file_url = url_mapping[option]
    response = requests.get(file_url)
    
    if response.status_code == 200:
        st.text(response.text)  # Display the file content as plain text
    else:
        st.write("Failed to fetch the content. Please check the URL.")
else:
    st.write("No file is associated with this option.")
