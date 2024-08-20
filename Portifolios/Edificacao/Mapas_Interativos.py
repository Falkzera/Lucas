import streamlit as st
from Portifolios.Edificacao.Edificacao import plot_map

def display_interactive_map():
    # Cabeçalho
    st.title('Mapa Interativo das Edificações de Alagoas 🧭')
    st.subheader('Este projeto apresenta um mapa interativo com informações sobre as edificações do estado de Alagoas e a Taxa de Alfabetização das regiões. Utilizando a biblioteca Geopandas, é possível visualizar as edificações de acordo com a variável selecionada.')
    st.subheader('Selecione a variável desejada no menu abaixo para visualizar o mapa interativo. As opções mostram as quantidades das edificações de escolas, igrejas, áreas agrícolas e índice de analfabetismo.')
    st.caption('**Fonte**: IBGE 2022')
    
    # Variáveis de entrada
    escolhas = ['AGRO', 'ENSINO', 'RELIGIOSO']
    temas = ['Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens', 'Oranges', 'OrRd', 'PuBu']
    
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
    display_interactive_map()