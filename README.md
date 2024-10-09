Painel Interativo de Reclamações de Clientes com Streamlit e Plotly
Este repositório contém um painel interativo desenvolvido com Streamlit e Plotly para a visualização e análise de dados de reclamações de clientes de uma empresa. O painel permite explorar os dados de forma dinâmica, aplicando filtros e visualizando informações por meio de gráficos intuitivos e interativos.

Funcionalidades
Série Temporal de Reclamações: Exibe o número de reclamações ao longo do tempo, permitindo visualizar tendências sazonais e picos de atendimento.
Distribuição das Reclamações por Estado: Mostra a frequência de reclamações em cada estado, ajudando a identificar regiões com maior número de ocorrências.
Análise por Status de Reclamação: Apresenta a distribuição dos tipos de status das reclamações, como Resolvido, Pendente e Não Resolvido.
Distribuição do Tamanho do Texto: Analisa o comprimento das descrições das reclamações, facilitando o entendimento da complexidade dos casos.
Filtros Dinâmicos: Possibilidade de aplicar filtros por estado, status e tamanho das descrições para refinar a visualização e análise dos dados.
Como Utilizar
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu_usuario/nome_do_repositorio.git
Instale as dependências necessárias:

bash
Copiar código
pip install -r requirements.txt
Execute o painel utilizando o Streamlit:

bash
Copiar código
streamlit run app.py
Navegue até http://localhost:8501/ no seu navegador para acessar o painel.

Estrutura do Repositório
app.py: Arquivo principal do painel interativo.
pasta_dados/: Contém os arquivos hapvida.csv e hapvida_por_estado.csv com os dados utilizados no projeto.
requirements.txt: Arquivo de dependências necessárias para executar o projeto.
README.md: Instruções e documentação do projeto.
Tecnologias Utilizadas
Python: Linguagem de programação utilizada para a manipulação de dados e desenvolvimento do painel.
Pandas: Biblioteca para manipulação e análise dos dados.
Streamlit: Framework utilizado para a construção do painel interativo.
Plotly: Biblioteca para criação de gráficos interativos.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias, correções de bugs ou novas funcionalidades.

Licença
Este projeto é licenciado sob a MIT License.
