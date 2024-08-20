import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
import Home.Cursos as Cursos
import Home.Sobre_mim as Sobre_mim
import Home.Email as Email
import Home.Credito as Credito


# Configuração de Página como wide
st.set_page_config(layout="wide")

# Menu de Navegação 
with st.container():
    selected = option_menu(
        menu_title = None,
        options = ["Sobre mim","Cursos", "Contato"],
        icons = ['person', 'book', 'chat-left-text-fill'],
        orientation='horizontal',
    )
st.write("---")

# Opções de Navegações

if selected == "Sobre mim":
    Sobre_mim.display_profile()

if selected == 'Cursos':
    Cursos.display_courses()

if selected == "Contato":
    Email.display_email_form()

# Cŕeditos
with st.sidebar:
    Credito.display_credits()







