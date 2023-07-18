import pandas as pd
import numpy as np
import streamlit as st
import plotly
import plotly.express as px

# Carregando os dados
df = pd.read_csv("base_cafe_brasil.txt")

#Configuração da página
st.set_page_config("Dashboard Café Brasileiro", layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html= True)

# Nome da sidebar
st.sidebar.title("Filtros")

# Nome do Dashboard
st.markdown("# Dashboard de Avaliação de Café")

# Métricas
df_melhor_marca = df.groupby('Marca')['Avaliação do Consumidor'].mean()
melhor_marca = df_melhor_marca.idxmax()
vmelhor_marca = round(df_melhor_marca.max(),2)

df_melhor_preparo = df.groupby('Tipo de Preparo')['Avaliação do Consumidor'].mean()
melhor_preparo = df_melhor_preparo.idxmax()
vmelhor_preparo = round(df_melhor_preparo.max(),2)

m1, m2 = st.columns(2)
m1.metric("Melhor Marca", vmelhor_marca)
m2.metric("Melhor Preparo", vmelhor_preparo)

# Filtros multiseleção da sidebar
regiao = st.sidebar.multiselect("Região",df['Região do Brasil'].unique(), df['Região do Brasil'].unique())
marca = st.sidebar.multiselect('Marca',df['Marca'].unique(), df["Marca"].unique())
ttorra = st.sidebar.multiselect('Tipo de Torra',df['Tipo de Torra'].unique(), df['Tipo de Torra'].unique())
tpreparo = st.sidebar.multiselect('Tipo de Preparo', df['Tipo de Preparo'].unique(), df['Tipo de Preparo'].unique())
agrupar_por = st.sidebar.selectbox('Agrupar por:', df.columns)

# Tabelas filtradas e agrupadas
df_filtrado = df[(df['Marca'].isin(marca)) & (df['Região do Brasil'].isin(regiao)) & (df['Tipo de Torra'].isin(ttorra)) & (df['Tipo de Torra'].isin(ttorra))]
df_agrupado = df_filtrado.groupby(agrupar_por)['Avaliação do Consumidor'].mean().reset_index()
df_agrupado['Avaliação do Consumidor'] = round(df_agrupado['Avaliação do Consumidor'], 2)

# Visualização das tabelas
col1, col2 = st.columns(2)
col1.markdown('### Tabela de dados')
col1.dataframe(df_filtrado)
col2.markdown('### Tabela de dados agrupada')
col2.dataframe(df_filtrado.groupby(agrupar_por)['Avaliação do Consumidor'].mean())

# Gráfico de barras
st.markdown('## Comparativo de Avaliações')
st.plotly_chart(px.bar(df_agrupado, x = df_agrupado[agrupar_por], y = df_agrupado['Avaliação do Consumidor'], 
                       color = df_agrupado[agrupar_por].unique(), text_auto= True)
                ,use_container_width=True)

