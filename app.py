import streamlit as st
import requests

# Define a function to fetch and justify text content
def fetch_and_display_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Wrap the text in a <div> with justified alignment
        justified_text = f"""
        <div style="text-align: justify;">
            {response.text.replace('\n', '<br>')}  <!-- Replace line breaks for HTML formatting -->
        </div>
        """
        st.markdown(justified_text, unsafe_allow_html=True)  # Display text as justified
    else:
        st.write("Failed to fetch the content. Please check the URL.")

# Options and URL mapping
options = [
    "Hétfőn reggeli imádság", "Hétfőn estvéli imádság",
    "Kedden reggeli imádság", "Kedden estvéli imádság",
    "Szerdán reggeli imádság", "Szerdán estvéli imádság",
    "Csütörtökön reggeli imádság", "Csütörtökön estvéli imádság",
    "Pénteken reggeli imádság", "Pénteken estvéli imádság",
    "Szombaton reggeli imádság", "Szombaton estvéli imádság",
    "Vasárnap reggeli imádság", "Vasárnap estvéli imádság"
]

url_mapping = {
    "Hétfőn reggeli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/hetfo_1.txt",
    # Add the rest of the URL mappings...
}

# Dropdown for selection
option = st.selectbox("Imádság kiválasztása:", options)

# Fetch and display the content in justified alignment
if option in url_mapping:
    fetch_and_display_text(url_mapping[option])
else:
    st.write("No file is associated with this option.")
