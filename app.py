import streamlit as st
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv")
st.title("Bienvenue sur le site de Valentin")

option = st.selectbox(
    "Indiquez votre arrondissement de récupération",
    df["pickup_borough"].unique(),
)

st.write("You selected:", option)
st.image(f"{option}.png")