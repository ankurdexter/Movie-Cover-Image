import streamlit as st
import pandas as pd

df = pd.read_csv("./data/spotify_dataset.csv")
movieList = df["Album"].unique()
st.table(movieList)