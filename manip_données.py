import streamlit as st
import seaborn as sns

st.title("Manipulation de données et création de graphiques")

liste_datasets = sns.get_dataset_names()

option = st.selectbox("Quel dataset voulez-vous choisir ?", liste_datasets,)

st.write("You selected:", option)

df = sns.load_dataset(option)

st.dataframe(df)

col_x = st.selectbox("Choisissez la colonne X", df.columns,)
col_y = st.selectbox("Choisissez la colonne Y", df.columns,)

liste_graph = ["bar_chart", "line_chart", "scatter_chart"]

graph = st.selectbox("Quel graphique voulez-vous choisir ?", liste_graph,)

if graph == "bar_chart":
    st.bar_chart(df, x=col_x, y=col_y)
if graph == "line_chart":
    st.line_chart(df, x=col_x, y=col_y)
if graph == "scatter_chart":
    st.scatter_chart(df, x=col_x, y=col_y)

corr = df.corr(numeric_only=True)
on = st.toggle("Afficher la matrice de corrélation")
if on:
    plot = sns.heatmap(corr, cmap="coolwarm")
    st.pyplot(plot.get_figure())
