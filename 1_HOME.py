import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import Home.Cursos as Cursos
import Home.Sobre_mim as Sobre_mim
import Home.Email as Email
import Home.Credito as Credito
import Portifolios.exportacoes.exportacoes as exportacoes
import Portifolios.Edificacao.Mapas_Interativos as Mapas_Interativos
from Portifolios.CompracaoGestao.ComparacaoGestao import comparacao_gestao

# # Configuração de Página como wide
st.set_page_config(layout="wide")

# CSS para ajustar a largura da página
page_style = """
    <style>
    /* Ajusta a largura máxima da página */
    .main {
        max-width: 1500px;
        margin: 0 auto;
    }
    </style>
    """

# Injetando o CSS na aplicação Streamlit
st.markdown(page_style, unsafe_allow_html=True)

# Menu de Navegação 
with st.container():
    selected = option_menu(
        menu_title = None,
        options = ["Sobre mim", "Cursos", "Contato"],
        icons = ['person', 'book', 'chat-left-text-fill'],
        orientation='horizontal',
    )
st.write("---")

# Opções de Navegações

if selected == "Sobre mim":
    Sobre_mim.display_profile()

    ###########################################################################################
    if selected == "Exportações-AL":
        exportacoes.display_export_analysis()

    elif selected == "Mapas Interativos":
        Mapas_Interativos.display_interactive_map()

    elif selected == "Transporte Público":
        comparacao_gestao()
    ###########################################################################################

if selected == 'Cursos':
    Cursos.display_certificates()

if selected == "Contato":
    Email.display_email_form()

# Cŕeditos
with st.sidebar:
    Credito.display_credits()







