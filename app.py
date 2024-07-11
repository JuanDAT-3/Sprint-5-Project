import streamlit as st 
import pandas as pd
import plotly_express as px 

vhc= pd.read_csv(r'C:\Users\Usuario\Desktop\Trabajo_aprendizaje\TripleTen\Sprint-5-Project\vehicles_us.csv')

#Despliegue de app

st.header('Analisis Exploratorio de datos')

st.write(f'Datos presentes. {vhc.head(10)}')

hist_button= st.button('Histograma')

if hist_button:

    fig= px.histogram(vhc)

st.plotly_chart(fig, use_container_width=True)