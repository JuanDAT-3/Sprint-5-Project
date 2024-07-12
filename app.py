import streamlit as st 
import pandas as pd
import plotly_express as px 

vhc= pd.read_csv(r'vehicles_us_cleaned.csv')

#Despliegue de app

st.header('Analisis Exploratorio de datos')

st.write('Visualización de datos de vehiculos en estados unidos basados en su kilometraje.')

hist_button= st.checkbox('Histograma')

dis_button= st.checkbox('Diagrama de Dispersión')

if hist_button:

    fig= px.histogram(vhc, x='odometer',range_x=[0,500000], nbins=150)

    st.plotly_chart(fig, use_container_width=True)

if dis_button:
    fig = px.scatter(vhc, x="odometer", y="price",range_x=[0,600000]) # crear un gráfico de dispersión

    st.plotly_chart(fig, use_container_width=True)
