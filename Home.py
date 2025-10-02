import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Home",  # Title for the browser tab
    page_icon="🎬",               # Optional: icon for the tab
    layout="wide"                 # "centered" or "wide"
)

df = pd.read_csv("./data/spotify_dataset.csv")

st.title("Album Cover Image")

input_album = st.text_input("Enter the Album name (Case Insensitive)").lower()
album_url = df.loc[df["Album"].str.lower() == input_album]["Cover Image"].head(1).squeeze()
suggestion = df.loc[df["Album"].str.lower().str.contains(input_album)]["Album"].unique()

#output = st.selectbox("test", ["yes", "no"])
#st.caption(output)

if len(input_album) != 0:
    if len(album_url) != 0:
        st.image(album_url)
    else:
        st.warning(f"{input_album} not found in my database. Do you mean {suggestion}")
        #st.warning(suggestion)
else:
    st.info("Write the Album Name and press ENTER")
##st.page_link("http://www.google.com", label="Google", icon="🌎")
#st.page_link("pages/page1.py", label="newpage", icon="✅")
#st.session_state