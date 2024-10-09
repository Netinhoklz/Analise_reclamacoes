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

# Definindo os caminhos dos arquivos CSV
hapvida_path = 'pasta_dados/hapvida.csv'
ibyte_path = 'pasta_dados/ibyte.csv'

# Carregar os dados das três abas
try:
    # Verificar se os arquivos existem antes de carregar
    hapvida_data = pd.read_csv(hapvida_path) if os.path.exists(hapvida_path) else None
    ibyte_data = pd.read_csv(ibyte_path) if os.path.exists(ibyte_path) else None
except Exception as e:
    st.error(f"Erro ao carregar os arquivos CSV: {e}")

# Se os dados forem carregados com sucesso, continue com o painel
if hapvida_data is not None and ibyte_data is not None:
    # Definir os filtros na barra lateral uma única vez
    st.sidebar.header("Filtros para Análise")
    
    # Seleção de Estado
    estado_selecionado = st.sidebar.selectbox('Selecione o estado:', hapvida_data['Estado'].unique(), key='estado')
    
    # Seleção de Status
    array_status = np.insert(hapvida_data['STATUS'].unique(), 0, 'Todos os status')
    status_selecionado = st.sidebar.selectbox('Selecione o Status:', array_status, key='status')
    
    # Filtros de Tamanho de Texto
    min_texto = st.sidebar.slider("Tamanho mínimo do texto (caracteres)", min_value=0, max_value=5000, value=0, key='min_texto')
    max_texto = st.sidebar.slider("Tamanho máximo do texto (caracteres)", min_value=0, max_value=5000, value=5000, key='max_texto')

    # Criação das três abas no Streamlit
    tab1, tab2, tab3 = st.tabs(["Hapvida", "Nagem", "Ibyte"])

    # Conteúdo da Aba 1 - Hapvida
    with tab1:
        st.title("Painel de Reclamações - Análise de Dados (Hapvida)")

        # Aplicar Filtros
        if status_selecionado == 'Todos os status':
            reclamacao_por_estado = hapvida_data[hapvida_data['Estado'] == estado_selecionado].copy()
        else:
            reclamacao_por_estado = hapvida_data[(hapvida_data['Estado'] == estado_selecionado) & (hapvida_data['STATUS'] == status_selecionado)].copy()

        tamanho_texto = reclamacao_por_estado[(reclamacao_por_estado['DESCRICAO_tamanho'] >= min_texto) & 
                                              (reclamacao_por_estado['DESCRICAO_tamanho'] <= max_texto)]

        # Gráficos com Plotly
        fig_serie_temporal = px.line(reclamacao_por_estado, x='TEMPO', y='CASOS', title='Série Temporal do Número de Reclamações Diárias')
        st.plotly_chart(fig_serie_temporal)

        fig_status = px.bar(reclamacao_por_estado, x='STATUS', y='CASOS', title='Ocorrência do Status')
        st.plotly_chart(fig_status)

        fig_histogram = px.histogram(tamanho_texto, x='DESCRICAO_tamanho', color='STATUS', title='Distribuição do Tamanho dos Textos')
        fig_histogram.update_layout(xaxis_title='Tamanho do Texto', yaxis_title='Frequência')
        st.plotly_chart(fig_histogram)

    # Conteúdo da Aba 2 - Nagem
    with tab2:
        st.title("Painel de Reclamações - Análise de Dados (Nagem)")
        
        # Reaplicando os filtros
        if status_selecionado == 'Todos os status':
            reclamacao_por_estado = hapvida_data[hapvida_data['Estado'] == estado_selecionado].copy()
        else:
            reclamacao_por_estado = hapvida_data[(hapvida_data['Estado'] == estado_selecionado) & (hapvida_data['STATUS'] == status_selecionado)].copy()

        tamanho_texto = reclamacao_por_estado[(reclamacao_por_estado['DESCRICAO_tamanho'] >= min_texto) & 
                                              (reclamacao_por_estado['DESCRICAO_tamanho'] <= max_texto)]

        # Gráficos com Plotly
        fig_serie_temporal = px.line(reclamacao_por_estado, x='TEMPO', y='CASOS', title='Série Temporal do Número de Reclamações Diárias')
        st.plotly_chart(fig_serie_temporal)

        fig_status = px.bar(reclamacao_por_estado, x='STATUS', y='CASOS', title='Ocorrência do Status')
        st.plotly_chart(fig_status)

        fig_histogram = px.histogram(tamanho_texto, x='DESCRICAO_tamanho', color='STATUS', title='Distribuição do Tamanho dos Textos')
        fig_histogram.update_layout(xaxis_title='Tamanho do Texto', yaxis_title='Frequência')
        st.plotly_chart(fig_histogram)

    # Conteúdo da Aba 3 - Ibyte
    with tab3:
        st.title("Painel de Reclamações - Análise de Dados (Ibyte)")

        # Aplicar Filtros usando os mesmos valores da barra lateral
        if status_selecionado == 'Todos os status':
            reclamacao_por_estado = ibyte_data[ibyte_data['Estado'] == estado_selecionado].copy()
        else:
            reclamacao_por_estado = ibyte_data[(ibyte_data['Estado'] == estado_selecionado) & (ibyte_data['STATUS'] == status_selecionado)].copy()

        tamanho_texto = reclamacao_por_estado[(reclamacao_por_estado['DESCRICAO_tamanho'] >= min_texto) & 
                                              (reclamacao_por_estado['DESCRICAO_tamanho'] <= max_texto)]

        # Gráficos com Plotly
        fig_serie_temporal = px.line(reclamacao_por_estado, x='TEMPO', y='CASOS', title='Série Temporal do Número de Reclamações Diárias')
        st.plotly_chart(fig_serie_temporal)

        fig_status = px.bar(reclamacao_por_estado, x='STATUS', y='CASOS', title='Ocorrência do Status')
        st.plotly_chart(fig_status)

        fig_histogram = px.histogram(tamanho_texto, x='DESCRICAO_tamanho', color='STATUS', title='Distribuição do Tamanho dos Textos')
        fig_histogram.update_layout(xaxis_title='Tamanho do Texto', yaxis_title='Frequência')
        st.plotly_chart(fig_histogram)
else:
    st.error("Erro: Não foi possível carregar os dados necessários para o painel.")
