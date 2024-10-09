import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import os

# Inicializar variáveis padrão para os filtros
estado_selecionado = None
status_selecionado = 'Todos os status'
min_texto = 0
max_texto = 5000

# Crie três abas no Streamlit
tab1, tab2, tab3 = st.tabs(["Hapvida", "Nagem", "Ibyte"])

# Conteúdo da Aba 1 - Hapvida
with tab1:
    data_path = 'pasta_dados/hapvida.csv'
    if not os.path.exists(data_path):
        st.error(f"Arquivo {data_path} não encontrado.")
    else:
        data = pd.read_csv(data_path)
        st.title("Painel de Reclamações - Análise de Dados (Hapvida)")

        # Filtros com identificadores únicos
        estado_selecionado = st.sidebar.selectbox('Selecione o estado:', data['Estado'].unique(), key='estado1')
        array_status = np.insert(data['STATUS'].unique(), 0, 'Todos os status')
        status_selecionado = st.sidebar.selectbox('Selecione o Status:', array_status, key='status1')
        min_texto = st.sidebar.slider("Tamanho mínimo do texto (caracteres)", min_value=0, max_value=5000, value=0, key='min_texto1')
        max_texto = st.sidebar.slider("Tamanho máximo do texto (caracteres)", min_value=0, max_value=5000, value=5000, key='max_texto1')

        # Aplicar Filtros
        if status_selecionado == 'Todos os status':
            reclamacao_por_estado = data[data['Estado'] == estado_selecionado].copy()
        else:
            reclamacao_por_estado = data[(data['Estado'] == estado_selecionado) & (data['STATUS'] == status_selecionado)].copy()

        tamanho_texto = reclamacao_por_estado[(reclamacao_por_estado['DESCRICAO_tamanho'] >= min_texto) & 
                                              (reclamacao_por_estado['DESCRICAO_tamanho'] <= max_texto)]

        # Gráficos com identificadores únicos
        fig_serie_temporal = px.line(reclamacao_por_estado, x='TEMPO', y='CASOS', title='Série Temporal do Número de Reclamações Diárias')
        st.plotly_chart(fig_serie_temporal, key='fig_serie_temporal1')

        fig_status = px.bar(reclamacao_por_estado, x='STATUS', y='CASOS', title='Ocorrência do Status')
        st.plotly_chart(fig_status, key='fig_status1')

        fig_histogram = px.histogram(tamanho_texto, x='DESCRICAO_tamanho', color='STATUS', title='Distribuição do Tamanho dos Textos')
        fig_histogram.update_layout(xaxis_title='Tamanho do Texto', yaxis_title='Frequência')
        st.plotly_chart(fig_histogram, key='fig_histogram1')

# Conteúdo da Aba 2 - Nagem
with tab2:
    data_path = 'pasta_dados/hapvida.csv'
    if not os.path.exists(data_path):
        st.error(f"Arquivo {data_path} não encontrado.")
    else:
        data = pd.read_csv(data_path)
        st.title("Painel de Reclamações - Análise de Dados (Nagem)")

        # Filtros com identificadores únicos para a segunda aba
        estado_selecionado = st.sidebar.selectbox('Selecione o estado:', data['Estado'].unique(), key='estado2')
        array_status = np.insert(data['STATUS'].unique(), 0, 'Todos os status')
        status_selecionado = st.sidebar.selectbox('Selecione o Status:', array_status, key='status2')
        min_texto = st.sidebar.slider("Tamanho mínimo do texto (caracteres)", min_value=0, max_value=5000, value=0, key='min_texto2')
        max_texto = st.sidebar.slider("Tamanho máximo do texto (caracteres)", min_value=0, max_value=5000, value=5000, key='max_texto2')

        # Aplicar Filtros
        if status_selecionado == 'Todos os status':
            reclamacao_por_estado = data[data['Estado'] == estado_selecionado].copy()
        else:
            reclamacao_por_estado = data[(data['Estado'] == estado_selecionado) & (data['STATUS'] == status_selecionado)].copy()

        tamanho_texto = reclamacao_por_estado[(reclamacao_por_estado['DESCRICAO_tamanho'] >= min_texto) & 
                                              (reclamacao_por_estado['DESCRICAO_tamanho'] <= max_texto)]

        # Gráficos com identificadores únicos para a segunda aba
        fig_serie_temporal = px.line(reclamacao_por_estado, x='TEMPO', y='CASOS', title='Série Temporal do Número de Reclamações Diárias')
        st.plotly_chart(fig_serie_temporal, key='fig_serie_temporal2')

        fig_status = px.bar(reclamacao_por_estado, x='STATUS', y='CASOS', title='Ocorrência do Status')
        st.plotly_chart(fig_status, key='fig_status2')

        fig_histogram = px.histogram(tamanho_texto, x='DESCRICAO_tamanho', color='STATUS', title='Distribuição do Tamanho dos Textos')
        fig_histogram.update_layout(xaxis_title='Tamanho do Texto', yaxis_title='Frequência')
        st.plotly_chart(fig_histogram, key='fig_histogram2')

# Conteúdo da Aba 3 - Ibyte
with tab3:
    data_path = 'pasta_dados/ibyte.csv'
    if not os.path.exists(data_path):
        st.error(f"Arquivo {data_path} não encontrado.")
    else:
        data = pd.read_csv(data_path)
        st.title("Painel de Reclamações - Análise de Dados (Ibyte)")

        # Filtros com identificadores únicos para a terceira aba
        estado_selecionado = st.sidebar.selectbox('Selecione o estado:', data['Estado'].unique(), key='estado3')
        array_status = np.insert(data['STATUS'].unique(), 0, 'Todos os status')
        status_selecionado = st.sidebar.selectbox('Selecione o Status:', array_status, key='status3')
        min_texto = st.sidebar.slider("Tamanho mínimo do texto (caracteres)", min_value=0, max_value=5000, value=0, key='min_texto3')
        max_texto = st.sidebar.slider("Tamanho máximo do texto (caracteres)", min_value=0, max_value=5000, value=5000, key='max_texto3')

        # Aplicar Filtros
        if status_selecionado == 'Todos os status':
            reclamacao_por_estado = data[data['Estado'] == estado_selecionado].copy()
        else:
            reclamacao_por_estado = data[(data['Estado'] == estado_selecionado) & (data['STATUS'] == status_selecionado)].copy()

        tamanho_texto = reclamacao_por_estado[(reclamacao_por_estado['DESCRICAO_tamanho'] >= min_texto) & 
                                              (reclamacao_por_estado['DESCRICAO_tamanho'] <= max_texto)]

        # Gráficos com identificadores únicos para a terceira aba
        fig_serie_temporal = px.line(reclamacao_por_estado, x='TEMPO', y='CASOS', title='Série Temporal do Número de Reclamações Diárias')
        st.plotly_chart(fig_serie_temporal, key='fig_serie_temporal3')

        fig_status = px.bar(reclamacao_por_estado, x='STATUS', y='CASOS', title='Ocorrência do Status')
        st.plotly_chart(fig_status, key='fig_status3')

        fig_histogram = px.histogram(tamanho_texto, x='DESCRICAO_tamanho', color='STATUS', title='Distribuição do Tamanho dos Textos')
        fig_histogram.update_layout(xaxis_title='Tamanho do Texto', yaxis_title='Frequência')
        st.plotly_chart(fig_histogram, key='fig_histogram3')
