# Importações
import streamlit as st
from streamlit_option_menu import option_menu
import Home.Credito as Credito
import Portifolios.exportacoes.exportacoes as exportacoes
import Portifolios.Edificacao.Mapas_Interativos as Mapas_Interativos
from Portifolios.CompracaoGestao.ComparacaoGestao import comparacao_gestao

# Configuração de Página
st.set_page_config(
    page_title="Projetos",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded")


# CSS para ajustar a largura da página
# page_style = """
#     <style>
#     /* Ajusta a largura máxima da página */
#     .main {
#         max-width: 1200px;
#         margin: 0 auto;
#     }
#     </style>
#     """

# Injetando o CSS na aplicação Streamlit
# st.markdown(page_style, unsafe_allow_html=True)



# Titulo da Página
st.title('PROJETOS  🚀')
st.header('Bem-vindo ao meu portfólio de projetos! :wave:')
st.subheader('Acesse o menu abaixo para visualizar os projetos realizados')
st.write('---')

# Menu de Navegação 
with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['Exportações-AL', 'Mapas Interativos', 'Transporte Público'],
        icons = ['code-slash', 'book', 'chat-left-text-fill'],
        orientation='horizontal',
    )
st.write("---")
# Seleção de Projetos

###########################################################################################
if selected == "Exportações-AL":
    exportacoes.display_export_analysis()

elif selected == "Mapas Interativos":
    Mapas_Interativos.display_interactive_map()

elif selected == "Transporte Público":
    comparacao_gestao()
###########################################################################################
# Cŕeditos
with st.sidebar:
    Credito.display_credits()
   