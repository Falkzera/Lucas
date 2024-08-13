# Importações
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from Portifolios.exportacoes.map_visualization import create_map
from Tema.theme_manager import theme_selector 
from Portifolios.Edificacao.Edificacao import plot_map


# Configuração de Página
st.set_page_config(
    page_title="Projetos",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# tema


# Titulo da Página
st.title('PROJETOS  🚀')
st.header('Bem-vindo ao meu portfólio de projetos! :wave:')
st.subheader('Acesse o menu abaixo para visualizar os projetos realizados')
st.write('---')

# Menu de Navegação 
with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['Exportações-AL', 'Mapas Interativos'],
        icons = ['code-slash', 'book', 'chat-left-text-fill'],
        orientation='horizontal',
    )
st.write("---")

# Opções de Navegações

###########################################################################################
if selected == "Exportações-AL":

    st.title("Análise das exportações no estado de Alagoas 🌍")
    st.subheader("O projeto dispõe de uma interface gráfica interativa para visualização dos dados de exportações do estado de Alagoas, para visualizar na integra, acesse o dashboard abaixo")
    st.write('Visualize o Dashboard: [Clique Aqui](https://exportacoes.streamlit.app/)')
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
        

    st.write('Visualize o projeto completo: [Clique Aqui](https://exportacoes.streamlit.app/)')
    with st.expander('Visuzalização Gráfica 🗺️', expanded=True):
        st.subheader("Visualização Gráfica do projeto 🗺️")
        st.subheader("Para facilitar a visualização, foi desenvolvido uma visualização gráfica do mapa do estado de Alagoas.")
        st.subheader("O mapa é interativo, podendo ser filtrado por ano e valor de exportação US$.")
        st.subheader("Permitindo visualizar de maneira dinâmica os municípios que mais exportaram no estado.")
        st.caption("Para a visualização completa, acesse o dashboard do projeto [Clicando Aqui](https://exportacoes.streamlit.app/)")
        create_map()
    st.caption("Fonte: Governo Federal")



###########################################################################################


elif selected == "Mapas Interativos":
    import streamlit as st


    def main():
        # Cabeçalho
        st.title('Mapa Interativo das Edificações de Alagoas 🧭')
        st.subheader('Este projeto apresenta um mapa interativo com informações sobre as edificações do estado de Alagoas e a Taxa de Alfabetização das regiões. Utilizando a biblioteca Geopandas, é possível visualizar as edificações de acordo com a variável selecionada.')
        st.subheader('Selecione a variável desejada no menu abaixo para visualizar o mapa interativo. As opções mostram as quantidades das edificações de escolas, igrejas, áreas agrícolas e índice de analfabetismo.')
        st.caption('**Fonte**: IBGE 2022')
        # Variáveis de entrada
        escolhas = ['AGRO', 'ENSINO', 'RELIGIOSO']
        temas = [
            'Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens', 'Oranges', 'OrRd', 'PuBu',
            ]
        
        col1, col2 = st.columns(2)
        with col1:
            variavel = st.selectbox('Escolha a variável a ser plotada', escolhas)
        with col2:
            tema = st.selectbox('Escolha o tema do mapa', temas)


        if variavel == 'AGRO':
            st.subheader('Edificações Agropecuárias 🌾')
            st.write('O IBGE classifica Edificações Agropecuárias como áreas destinadas a atividades agrícolas e pecuárias. Estas áreas são utilizadas para a produção de alimentos e criação de animais.')
            st.write('O mapa abaixo mostra a quantidade de edificação por município.')
            st.caption('*Fonte*: Dados IBGE - 2022')
        elif variavel == 'ENSINO':
            st.subheader('Edificações de Ensino 🏫')
            st.write('O IBGE classifica Edificações de Ensino como áreas destinadas a atividades educacionais. Estas áreas são utilizadas para a realização de aulas, cursos e treinamentos.')
            st.write('As edificações de ensino são de diversos tipos, como escolas, creches, universidades e centros de treinamento, públicos ou privados.')
            st.write('O mapa abaixo mostra a quantidade de edificação de ensino por município.')
            st.caption('*Fonte*: Dados IBGE - 2022')
        elif variavel == 'RELIGIOSO':
            st.subheader('Edificações Religiosas ⛪')
            st.write('O IBGE classifica Edificações Religiosas como áreas destinadas a atividades religiosas. Estas áreas são utilizadas para a realização de cultos, missas, cerimônias e eventos religiosos.')
            st.write('As edificações religiosas são de diversos tipos, como igrejas, templos, sinagogas, mesquitas, centros de meditação, etc..')
            st.write('O mapa abaixo mostra a quantidade de edificação religiosa por município.')
            st.caption('*Fonte*: Dados IBGE - 2022')

        mapa = plot_map(variavel, tema)
        st.components.v1.html(mapa._repr_html_(), height=600)

    if __name__ == "__main__":
        main()

                    
###########################################################################################
# Créditos lateral
# Configurações da Barra Lateral
with st.sidebar:
    social_media_html = """
    <div style="text-align: center;">
        <h2>Redes Sociais</h2>
        <a href="https://www.instagram.com/falkzera/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" style="width:40px;height:40px;margin:10px;">
        </a>
        <a href="https://github.com/falkzera" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" style="width:40px;height:40px;margin:10px;">
        </a>
        <p style="text-align: center;">Developer by: <a href="https://GitHub.com/Falkzera" target="_blank">Lucas Falcão</a></p>
    </div>
    """
    st.markdown(social_media_html, unsafe_allow_html=True)
    theme_selector()