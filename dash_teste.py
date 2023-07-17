import pandas as pd
import numpy as np
import streamlit as st
import plotly
import plotly.express as px

df = pd.read_csv("C:\\Users\\f41088049885\\Downloads\\Estudos\\base_cafe_brasil.txt")

st.set_page_config("Dashboard Teste", layout="wide")

st.sidebar.title("Filtros")

st.header("Dashboard de Avaliação de Café")
regiao = st.sidebar.multiselect("Região",df['Região do Brasil'].unique(), df['Região do Brasil'].unique())
marca = st.sidebar.multiselect('Marca',df['Marca'].unique(), df["Marca"].unique())
ttorra = st.sidebar.multiselect('Tipo de Torra',df['Tipo de Torra'].unique(), df['Tipo de Torra'].unique())
tpreparo = st.sidebar.multiselect('Tipo de Preparo', df['Tipo de Preparo'].unique(), df['Tipo de Preparo'].unique())
agrupar_por = st.sidebar.selectbox('Agrupar por:', df.columns)

df_filtrado = df[(df['Marca'].isin(marca)) & (df['Região do Brasil'].isin(regiao)) & (df['Tipo de Torra'].isin(ttorra)) & (df['Tipo de Torra'].isin(ttorra))]
df_agrupado = df_filtrado.groupby(agrupar_por)['Avaliação do Consumidor'].mean().reset_index()
df_agrupado['Avaliação do Consumidor'] = round(df_agrupado['Avaliação do Consumidor'], 2)

col1, col2 = st.columns(2)
col1.dataframe(df_filtrado)
col2.dataframe(df_filtrado.groupby(agrupar_por)['Avaliação do Consumidor'].mean())


st.plotly_chart(px.bar(df_agrupado, x = df_agrupado[agrupar_por], y = df_agrupado['Avaliação do Consumidor'], 
                       color = df_agrupado[agrupar_por].unique(), text_auto= True)
                ,use_container_width=True)

