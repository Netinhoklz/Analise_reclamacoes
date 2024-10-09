import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

# Crie três abas no Streamlit
tab1, tab2, tab3 = st.tabs(["Hapvida", "Nagem", "Ibyte"])
data = pd.read_csv(f'pasta_dados//hapvida.csv')
estado_selecionado = st.sidebar.selectbox(
    'Selecione o estado:',
    data['Estado'].unique()
)
array_status = np.insert(data['STATUS'].unique(), 0, 'Todos os status')
status_selecionado = st.sidebar.selectbox(
    'Selecione o Status:',
    array_status
)
min_texto = st.sidebar.slider("Tamanho mínimo do texto (caracteres)", min_value=0, max_value=5000, value=0)
max_texto = st.sidebar.slider("Tamanho máximo do texto (caracteres)", min_value=0, max_value=5000, value=5000)
# Conteúdo da Aba 1
with tab1:
    data = pd.read_csv(f'pasta_dados//hapvida.csv')

    # Convertendo a coluna 'TEMPO' para datetime, se aplicável
    #data['TEMPO'] = pd.to_datetime(data['TEMPO'])


    st.title("Painel de Reclamações - Análise de Dados")


    if status_selecionado == 'Todos os status':
        reclamacao_por_estado = data.loc[(data['Estado'] == estado_selecionado)].copy()
        reclamacao_por_estado['um'] = 1
        reclamacao_por_estado['Total_casos'] = reclamacao_por_estado['um'].cumsum()
        frequencia_tipo_status = reclamacao_por_estado.loc[reclamacao_por_estado.STATUS == status_selecionado]
    else:
        reclamacao_por_estado = data.loc[(data['Estado'] == estado_selecionado) &(data['STATUS'] == status_selecionado)].copy()
        reclamacao_por_estado['um'] = 1
        reclamacao_por_estado['Total_casos'] = reclamacao_por_estado['um'].cumsum()
        frequencia_tipo_status = reclamacao_por_estado.loc[reclamacao_por_estado.STATUS == status_selecionado]
    tamanho_texto = reclamacao_por_estado.loc[(reclamacao_por_estado.DESCRICAO_tamanho >= min_texto) & (reclamacao_por_estado.DESCRICAO_tamanho <= max_texto)]
    # Série temporal
    fig_serie_temporal = px.line(reclamacao_por_estado,width= 500, height= 400, x = 'TEMPO', y = 'Total_casos', title = 'Série temporal do número de reclamaçãos diárias', labels = {'TEMPO':'Dias', 'CASOS':'Reclamações diárias'})
    st.plotly_chart(fig_serie_temporal)

    # Gráfico de barras
    fig_status = px.bar(reclamacao_por_estado,width= 500, height= 600, x='STATUS', title = 'Ocorrência do Status', labels = {'STATUS':'Status', 'count' : 'Frequência'})
    st.plotly_chart(fig_status)

    # histograma
    fig_histogram = px.histogram(tamanho_texto, width= 500, height= 400, x='DESCRICAO_tamanho', title = 'Distribuição do tamanho dos textos', color = 'STATUS', labels = {'DESCRICAO_tamanho':'Tamanho do texto', 'count':'Frequência'})
    fig_histogram.update_layout(
        xaxis_title='Tamanho do Texto',  # Rótulo do eixo x
        yaxis_title='Frequência'  # Rótulo do eixo y
    )
    st.plotly_chart(fig_histogram)

# Conteúdo da Aba 2
with tab2:
    data = pd.read_csv(f'pasta_dados//nagem.csv')

    # Convertendo a coluna 'TEMPO' para datetime, se aplicável
    # data['TEMPO'] = pd.to_datetime(data['TEMPO'])

    st.title("Painel de Reclamações - Análise de Dados")


    if status_selecionado == 'Todos os status':
        reclamacao_por_estado = data.loc[(data['Estado'] == estado_selecionado)].copy()
        reclamacao_por_estado['um'] = 1
        reclamacao_por_estado['Total_casos'] = reclamacao_por_estado['um'].cumsum()
        frequencia_tipo_status = reclamacao_por_estado.loc[reclamacao_por_estado.STATUS == status_selecionado]
    else:
        reclamacao_por_estado = data.loc[
            (data['Estado'] == estado_selecionado) & (data['STATUS'] == status_selecionado)].copy()
        reclamacao_por_estado['um'] = 1
        reclamacao_por_estado['Total_casos'] = reclamacao_por_estado['um'].cumsum()
        frequencia_tipo_status = reclamacao_por_estado.loc[reclamacao_por_estado.STATUS == status_selecionado]
    tamanho_texto = reclamacao_por_estado.loc[(reclamacao_por_estado.DESCRICAO_tamanho >= min_texto) & (
                reclamacao_por_estado.DESCRICAO_tamanho <= max_texto)]
    # Série temporal
    fig_serie_temporal = px.line(reclamacao_por_estado, width=500, height=400, x='TEMPO', y='Total_casos',
                                 title='Série temporal do número de reclamaçãos diárias',
                                 labels={'TEMPO': 'Dias', 'CASOS': 'Reclamações diárias'})
    st.plotly_chart(fig_serie_temporal)

    # Gráfico de barras
    fig_status = px.bar(reclamacao_por_estado, width=500, height=600, x='STATUS', title='Ocorrência do Status',
                        labels={'STATUS': 'Status', 'count': 'Frequência'})
    st.plotly_chart(fig_status)

    # histograma
    fig_histogram = px.histogram(tamanho_texto, width=500, height=400, x='DESCRICAO_tamanho',
                                 title='Distribuição do tamanho dos textos', color='STATUS',
                                 labels={'DESCRICAO_tamanho': 'Tamanho do texto', 'count': 'Frequência'})
    fig_histogram.update_layout(
        xaxis_title='Tamanho do Texto',  # Rótulo do eixo x
        yaxis_title='Frequência'  # Rótulo do eixo y
    )
    st.plotly_chart(fig_histogram)

# Conteúdo da Aba 3
with tab3:
    data = pd.read_csv(f'pasta_dados//ibyte.csv')

    # Convertendo a coluna 'TEMPO' para datetime, se aplicável
    # data['TEMPO'] = pd.to_datetime(data['TEMPO'])

    st.title("Painel de Reclamações - Análise de Dados")


    if status_selecionado == 'Todos os status':
        reclamacao_por_estado = data.loc[(data['Estado'] == estado_selecionado)].copy()
        reclamacao_por_estado['um'] = 1
        reclamacao_por_estado['Total_casos'] = reclamacao_por_estado['um'].cumsum()
        frequencia_tipo_status = reclamacao_por_estado.loc[reclamacao_por_estado.STATUS == status_selecionado]
    else:
        reclamacao_por_estado = data.loc[
            (data['Estado'] == estado_selecionado) & (data['STATUS'] == status_selecionado)].copy()
        reclamacao_por_estado['um'] = 1
        reclamacao_por_estado['Total_casos'] = reclamacao_por_estado['um'].cumsum()
        frequencia_tipo_status = reclamacao_por_estado.loc[reclamacao_por_estado.STATUS == status_selecionado]
    tamanho_texto = reclamacao_por_estado.loc[(reclamacao_por_estado.DESCRICAO_tamanho >= min_texto) & (
                reclamacao_por_estado.DESCRICAO_tamanho <= max_texto)]
    # Série temporal
    fig_serie_temporal = px.line(reclamacao_por_estado, width=500, height=400, x='TEMPO', y='Total_casos',
                                 title='Série temporal do número de reclamaçãos diárias',
                                 labels={'TEMPO': 'Dias', 'CASOS': 'Reclamações diárias'})
    st.plotly_chart(fig_serie_temporal)

    # Gráfico de barras
    fig_status = px.bar(reclamacao_por_estado, width=500, height=600, x='STATUS', title='Ocorrência do Status',
                        labels={'STATUS': 'Status', 'count': 'Frequência'})
    st.plotly_chart(fig_status)

    # histograma
    fig_histogram = px.histogram(tamanho_texto, width=500, height=400, x='DESCRICAO_tamanho',
                                 title='Distribuição do tamanho dos textos', color='STATUS',
                                 labels={'DESCRICAO_tamanho': 'Tamanho do texto', 'count': 'Frequência'})
    fig_histogram.update_layout(
        xaxis_title='Tamanho do Texto',  # Rótulo do eixo x
        yaxis_title='Frequência'  # Rótulo do eixo y
    )
    st.plotly_chart(fig_histogram)



