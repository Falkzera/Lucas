import streamlit as st
import os

def update_config(theme):
    """Atualiza o arquivo config.toml com o tema selecionado."""
    config_path = os.path.join(os.path.expanduser("~"), ".streamlit", "config.toml")
    
    # Conteúdo do config.toml com o tema selecionado
    config_content = f"""
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#{ '0E1117' if theme == 'dark' else 'FFF' }"
secondaryBackgroundColor = "#{ '262730' if theme == 'dark' else 'F5F5F5' }"
textColor = "#{ 'FFF' if theme == 'dark' else '000' }"
font = "sans serif"
"""
    # Cria a pasta .streamlit se não existir
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    
    # Escreve o conteúdo no arquivo config.toml
    with open(config_path, "w") as config_file:
        config_file.write(config_content)

def theme_selector():
    """Cria um seletor de tema e aplica o tema selecionado."""
    # Gerenciar o estado do tema
    if  'theme' not in st.session_state:
        st.session_state.theme = 'light'

    st.sidebar.markdown("# Tema")
    theme = st.sidebar.selectbox('Escolha o tema', ['light', 'dark'], index=['light', 'dark'].index(st.session_state.theme))
    st.sidebar.button('Aplicar')
 
    # Atualizar o estado do tema
    st.session_state.theme = theme

    # Atualizar o arquivo config.toml
    update_config(theme)

if __name__ == "__main__":
    theme_selector()