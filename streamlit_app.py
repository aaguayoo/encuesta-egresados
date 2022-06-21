import streamlit as st
import numpy as np

st.title("Encuesta egresados")
st.header("Esto es un encabezado")

with st.form("Años empleo"):
    years = list(np.linspace(2000,2022,1))
    col1, col2 = st.columns(2)
    start = col1.selectbox("",years)
    end = col2.selectbox("",years)
