import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import os

# Definir caminhos dos arquivos
hapvida_path = 'pasta_dados/hapvida.csv'
ibyte_path = 'pasta_dados/ibyte.csv'
nagem_path = 'pasta_dados/nagem.csv'

# Carregar os dados
try:
    hapvida_data = pd.read_csv(hapvida_path) if os.path.exists(hapvida_path) else None
    ibyte_data = pd.read_csv(ibyte_path) if os.path.exists(ibyte_path) else None
    nagem_data = pd.read_csv(nagem_path) if os.path.exists(nagem_path) else None
except Exception as e:
    st.error(f"Erro ao carregar os arquivos CSV: {e}")

# Verificar se todos os dados foram carregados com sucesso
if hapvida_data is not None and ibyte_data is not None and nagem_data is not None:
    
    # Definir filtros na barra lateral
    st.sidebar.header("Filtros para Análise")

    # Seleção de Estado
    estados_disponiveis = sorted(list(set(hapvida_data['Estado']).union(set(ibyte_data['Estado'])).union(set(nagem_data['Estado']))))
    estado_selecionado = st.sidebar.selectbox('Selecione o estado:', estados_disponiveis, key='estado')

    # Seleção de Status
    status_disponiveis = sorted(list(set(hapvida_data['STATUS']).union(set(ibyte_data['STATUS'])).union(set(nagem_data['STATUS']))))
    array_status = np.insert(status_disponiveis, 0, 'Todos os status')
    status_selecionado = st.sidebar.selectbox('Selecione o Status:', array_status, key='status')

    # Filtros de Tamanho de Texto
    min_texto = st.sidebar.slider("Tamanho mínimo do texto (caracteres)", min_value=0, max_value=5000, value=0, key='min_texto')
    max_texto = st.sidebar.slider("Tamanho máximo do texto (caracteres)", min_value=0, max_value=5000, value=5000, key='max_texto')

    # Criação das abas
    tab1, tab2, tab3 = st.tabs(["Hapvida", "Nagem", "Ibyte"])

    # Função para aplicar filtros nos dados de cada aba
    def aplicar_filtros(data, estado, status, min_len, max_len):
        if status == 'Todos os status':
            filtrado = data[data['Estado'] == estado].copy()
        else:
            filtrado = data[(data['Estado'] == estado) & (data['STATUS'] == status)].copy()
        
        # Aplicar filtro de tamanho de texto
        filtrado = filtrado[(filtrado['DESCRICAO_tamanho'] >= min_len) & (filtrado['DESCRICAO_tamanho'] <= max_len)]
        return filtrado

    # Conteúdo da Aba 1 - Hapvida
    with tab1:
        st.title("Painel de Reclamações - Análise de Dados (Hapvida)")
        
        # Aplicar filtros no dataframe de Hapvida
        reclamacao_por_estado = aplicar_filtros(hapvida_data, estado_selecionado, status_selecionado, min_texto, max_texto)

        # Verificar se o dataframe não está vazio após os filtros
        if not reclamacao_por_estado.empty:
            # Gráficos com Plotly
            fig_serie_temporal = px.line(reclamacao_por_estado, x='TEMPO', y='CASOS', title='Série Temporal do Número de Reclamações Diárias')
            st.plotly_chart(fig_serie_temporal)

            fig_status = px.bar(reclamacao_por_estado, x='STATUS', y='CASOS', title='Ocorrência do Status')
            st.plotly_chart(fig_status)

            fig_histogram = px.histogram(reclamacao_por_estado, x='DESCRICAO_tamanho', color='STATUS', title='Distribuição do Tamanho dos Textos')
            fig_histogram.update_layout(xaxis_title='Tamanho do Texto', yaxis_title='Frequência')
            st.plotly_chart(fig_histogram)
        else:
            st.warning("Não há dados disponíveis para os filtros selecionados.")

    # Conteúdo da Aba 2 - Nagem
    with tab2:
        st.title("Painel de Reclamações - Análise de Dados (Nagem)")
        
        # Aplicar filtros no dataframe de Nagem
        reclamacao_por_estado = aplicar_filtros(nagem_data, estado_selecionado, status_selecionado, min_texto, max_texto)

        # Verificar se o dataframe não está vazio após os filtros
        if not reclamacao_por_estado.empty:
            # Gráficos com Plotly
            fig_serie_temporal = px.line(reclamacao_por_estado, x='TEMPO', y='CASOS', title='Série Temporal do Número de Reclamações Diárias')
            st.plotly_chart(fig_serie_temporal)

            fig_status = px.bar(reclamacao_por_estado, x='STATUS', y='CASOS', title='Ocorrência do Status')
            st.plotly_chart(fig_status)

            fig_histogram = px.histogram(reclamacao_por_estado, x='DESCRICAO_tamanho', color='STATUS', title='Distribuição do Tamanho dos Textos')
            fig_histogram.update_layout(xaxis_title='Tamanho do Texto', yaxis_title='Frequência')
            st.plotly_chart(fig_histogram)
        else:
            st.warning("Não há dados disponíveis para os filtros selecionados.")

    # Conteúdo da Aba 3 - Ibyte
    with tab3:
        st.title("Painel de Reclamações - Análise de Dados (Ibyte)")
        
        # Aplicar filtros no dataframe de Ibyte
        reclamacao_por_estado = aplicar_filtros(ibyte_data, estado_selecionado, status_selecionado, min_texto, max_texto)

        # Verificar se o dataframe não está vazio após os filtros
        if not reclamacao_por_estado.empty:
            # Gráficos com Plotly
            fig_serie_temporal = px.line(reclamacao_por_estado, x='TEMPO', y='CASOS', title='Série Temporal do Número de Reclamações Diárias')
            st.plotly_chart(fig_serie_temporal)

            fig_status = px.bar(reclamacao_por_estado, x='STATUS', y='CASOS', title='Ocorrência do Status')
            st.plotly_chart(fig_status)

            fig_histogram = px.histogram(reclamacao_por_estado, x='DESCRICAO_tamanho', color='STATUS', title='Distribuição do Tamanho dos Textos')
            fig_histogram.update_layout(xaxis_title='Tamanho do Texto', yaxis_title='Frequência')
            st.plotly_chart(fig_histogram)
        else:
            st.warning("Não há dados disponíveis para os filtros selecionados.")
else:
    st.error("Erro: Não foi possível carregar os dados necessários para o painel.")
