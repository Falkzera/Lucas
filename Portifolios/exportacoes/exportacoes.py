import streamlit as st
from Portifolios.exportacoes.map_visualization import create_map

def display_export_analysis():
    st.title("Análise das exportações no estado de Alagoas 🌍")
    st.subheader("O projeto dispõe de uma interface gráfica interativa para visualização dos dados de exportações do estado de Alagoas, para visualizar na integra, acesse o dashboard abaixo")
    st.write('Visualize o Dashboard: [Clique Aqui](https://exportacoesal.streamlit.app/)')

    with st.expander('# Sobre o Projeto', expanded=True):
        st.subheader("Sobre o Projeto 🎯")
        st.markdown("""
            <div style="text-align: justify; font-size: 24px;">
                <p>Este projeto é um estudo de caso sobre as exportações do estado de Alagoas, baseado em dados fornecidos pelo Governo Federal. O objetivo principal é analisar o comportamento das exportações ao longo dos anos, identificando os seguintes aspectos:</p>
                <ul>
                    <li>Principais parceiros comerciais</li>
                    <li>Produtos exportados</li>
                    <li>Municípios exportadores</li>
                </ul>
                <p>O projeto foi dividido em duas etapas:</p>
                <ol>
                    <li><strong>Extração e filtragem da base de dados:</strong> 
                        <p>Na primeira etapa, foi realizada a extração da base de dados do Governo Federal, contendo informações sobre as exportações do Brasil. Inicialmente, a base possuía <strong>20.139.345</strong> linhas. Utilizando a linguagem de programação Python e a biblioteca Pandas, a base foi filtrada para incluir apenas os dados referentes ao estado de Alagoas.</p>
                        <p>Como a base de dados original não incluía o nome dos municípios, foi necessário cruzar os dados com uma outra base para identificar a origem das exportações e os parceiros comerciais.</p>
                    </li>
                    <li><strong>Criação da interface gráfica:</strong>
                        <p>Na segunda etapa, foi desenvolvida uma interface gráfica interativa com a biblioteca Streamlit. Esta interface permite ao usuário:</p>
                        <ul>
                            <li>Selecionar o município, ano e mês desejados</li>
                            <li>Visualizar gráficos com as principais informações sobre exportações</li>
                        </ul>
                        <p>Com a interface gráfica, é possível observar os principais parceiros comerciais, produtos exportados e municípios exportadores, bem como outras informações relevantes. Esta funcionalidade é crucial para a identificação de soluções de negócios e para descobrir possíveis gargalos e oportunidades de melhoria.</p>
                    </li>
                </ol>
                <p>O projeto foi desenvolvido por <strong>Lucas Falcão</strong>, estudante de Ciências Econômicas da Universidade Federal de Alagoas. Para mais informações, visite o <a href="https://github.com/Falkzera" target="_blank">perfil do desenvolvedor no GitHub</a>.</p>
            </div>
        """, unsafe_allow_html=True)

    st.write('Visualize o projeto completo: [Clique Aqui](https://exportacoesal.streamlit.app/)')

    with st.expander('Visuzalização Gráfica 🗺️', expanded=True):
        st.subheader("Visualização Gráfica do projeto 🗺️")
        st.subheader("Para facilitar a visualização, foi desenvolvido uma visualização gráfica do mapa do estado de Alagoas.")
        st.subheader("O mapa é interativo, podendo ser filtrado por ano e valor de exportação US$.")
        st.subheader("Permitindo visualizar de maneira dinâmica os municípios que mais exportaram no estado.")
        st.caption("Para a visualização completa, acesse o dashboard do projeto [Clicando Aqui](https://exportacoesal.streamlit.app/)")
        create_map()

    st.caption("Fonte: Governo Federal")

if __name__ == "__main__":
    display_export_analysis()