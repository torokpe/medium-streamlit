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

url_mapping = {
    "Hétfőn reggeli imádság": "https://raw.githubusercontent.com/torokpe/medium-streamlit/refs/heads/main/hetfo_1.txt",
    # Add mappings for other options if needed
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
