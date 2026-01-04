import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("📊 Sport Analytics Dashboard")

sport = st.selectbox(
    "Scegli lo sport",
    ["Calcio ⚽", "Tennis 🎾", "Formula 1 🏎️"]
)

df = pd.DataFrame({
    "Sport": ["Calcio", "Tennis", "F1"],
    "Valore": [85, 70, 90]
})

if sport == "Calcio ⚽":
    st.subheader("Analisi Calcio")
    fig = px.bar(df, x="Sport", y="Valore", title="Calcio - Test")
    st.plotly_chart(fig, use_container_width=True)

elif sport == "Tennis 🎾":
    st.subheader("Analisi Tennis")
    fig = px.line(df, x="Sport", y="Valore", title="Tennis - Test")
    st.plotly_chart(fig, use_container_width=True)

elif sport == "Formula 1 🏎️":
    st.subheader("Analisi Formula 1")
    fig = px.scatter(df, x="Sport", y="Valore", title="F1 - Test")
    st.plotly_chart(fig, use_container_width=True)
