import streamlit as st
import numpy as np

st.title("Encuesta egresados")
st.header("Esto es un encabezado")

years = list(np.linspace(2000,2022,1))
st.checkbox("",years)
