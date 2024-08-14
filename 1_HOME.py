# Importações
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import json
import requests
import re
import streamlit as st
# from Tema.theme_manager import theme_selector

# Configuração de Página como wide
st.set_page_config(layout="wide")

# Aplicação de tema
# Chamar o seletor de tema

# Chame a função para mostrar o botão de alternância de tema
# try:
#     theme_selector()
# except: AttributeError

# Função para carregar o arquivo JSON
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Função para validar email
def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

# FUnção para rolar a página
def scroll_to_projects():
    st.write("""
        <script>
            document.getElementById('projetos-section').scrollIntoView({behavior: 'smooth'});
        </script>
    """, unsafe_allow_html=True)

# Organização de Imagens e Lotties
def load_assets():
    assets = {}
    assets['falkzera'] = Image.open("image/falkzera.png")
    assets['python_snake'] = "image/python_snake.gif"
    assets['mapa_al'] = "image/mapa_al.png"
    assets['lottie_contato'] = load_lottiefile("image/Contact.json")
    assets['foguete'] = load_lottiefile("image/foguete.json")
    return assets

# Carregar os ativos
assets = load_assets()

## Função para criar botões de redes sociais com ícones
# Função para criar botões de redes sociais
def social_media_button(platform, url):
    if st.button(platform):
        st.write(f"[Abrir {platform}]({url})")

#####################################################################################################
# Container Principal
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write("##")
        st.subheader("Seja bem-vindo ao meu perfil! :wave: ")
        st.title("Profile: Lucas Falcão 🦅")
        st.caption("23 anos, Maceió-AL")
        texto = """
        Olá, sou Lucas Falcão, graduando de Ciências Econômicas pela Universidade Federal de Alagoas - UFAL, amante de Python, Data Science e Econometria.
        Aqui você encontrará um pouco sobre mim, meus projetos e como entrar em contato. 🚀

        Comecei a estudar programação, em especial: python 🐍, no meu quinto período da faculdade, e desde então venho me aprimorando e estudando cada vez mais.
        Então, tudo que você verá aqui é fruto de muito estudo e dedicação ❤️

        Siga os menus abaixo, e visualize as informações que deseja. Caso queira entrar em contato, utilize o formulário no menu "Contato":email: logo abaixo.
        Ou se preferir, entre em contato pelas redes sociais.
        """
        # HTML para justificar o texto
        html_text = f"""
        <div style="text-align: justify;">
            {texto}
        </div>
        """
        # Exibir o texto justificado no Streamlit
        st.markdown(html_text, unsafe_allow_html=True)
        #     st.write("## Redes Sociais")

    with col2:
        st.image(assets['falkzera'], width=400, use_column_width=True)
        

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
# Sobre

if selected == "Sobre mim":
    scroll_to_projects()
    pass

if selected == 'Cursos':
    
    col1, col2 = st.columns(2)
    with col1: # FORMAÇÃO ACADÊMICA
        with st.expander("**FORMAÇÃO E ESPECIALIZAÇÃO**", expanded=False):
            st.write("## Graduação")
            st.write("Ciências Econômicas - Universidade Federal de Alagoas - UFAL")
            st.caption("Em andamento")
            st.write("---")

    
    with col2: # CURSOS E CERTIFICADOS
        with st.expander("**CURSOS COM CERTIFICADOS**", expanded=False):
            st.write("## Cursos")
            st.write("#### **Escola Nacional de Administração Pública (ENAP)**")
            st.write("Introdução à Ciência de Dados - Conjuntos Frequentes - 2024")
            st.write("Aprendendo com Python - 2024")
            st.write("Estatística - 2024")
            st.write("---")


# Contato
# Formulário de Contato
if selected == "Contato":
    scroll_to_projects()
    col1, col2 = st.columns(2)
    with col1:
        st.header("Envie-me um Email :email:")
        st.caption("E-mail via FormSubmit. O aplicativo está em desenvolvimento, então pode não funcionar corretamente. Caso não funcione, entre em contato pelas redes na sidebar.")


# Validação para e-mail
    with st.form(key='contact_form'):
        name = st.text_input("Seu Nome", max_chars=50)
        email = st.text_input("Seu Email", max_chars=50, type='default')
        if email:
            if not is_valid_email(email):
                st.error("Por favor, insira um email válido.")
        message = st.text_area("Sua Mensagem", height=150)
        submit_button = st.form_submit_button(label='Enviar')

    if submit_button:
        if name and email and message:
            # Lógica para enviar o email usando FormSubmit
            form_data = {
                'name': name,
                'email': email,
                'message': message
            }
            response = requests.post(
                'https://formsubmit.co/falcovisk@gmail.com',
                data=form_data
            )
            if response.status_code == 200:
                st.warning("Algo de estranho ocorreu!")
            else:
                st.error("Falha ao enviar a mensagem. Tente novamente mais tarde.")
        else:
            st.error("Por favor, preencha todos os campos.")


#####################################################################################################
# Cŕeditos
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







