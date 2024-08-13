import streamlit as st
import toml

CONFIG_PATH = ".streamlit/config.toml"

# Função para ler o arquivo de configuração
def read_config():
    with open(CONFIG_PATH, "r") as f:
        return toml.load(f)

# Função para escrever no arquivo de configuração
def write_config(config):
    with open(CONFIG_PATH, "w") as f:
        toml.dump(config, f)

# Inicializar o tema no session_state se não estiver presente
if "themes" not in st.session_state:
    st.session_state.themes = {
        "current_theme": "light",
        "refreshed": True,
        "light": {
            "base": "light",
            "backgroundColor": "#FFFFFF",
            "primaryColor": "#F63366",
            "secondaryBackgroundColor": "#F0F2F6",
            "textColor": "#000000",
            "button_face": "🌞"
        },
        "dark": {
            "base": "dark",
            "backgroundColor": "#0E1117",
            "primaryColor": "#1E90FF",
            "secondaryBackgroundColor": "#262730",
            "textColor": "#FFFFFF",
            "button_face": "🌜"
        },
    }

def ChangeTheme():
    previous_theme = st.session_state.themes["current_theme"]
    new_theme = "light" if previous_theme == "dark" else "dark"
    tdict = st.session_state.themes[new_theme]

    # Ler o arquivo de configuração
    config = read_config()

    # Atualizar os valores do tema no arquivo de configuração
    config["theme"] = tdict

    # Escrever as mudanças no arquivo de configuração
    write_config(config)

    st.session_state.themes["current_theme"] = new_theme
    st.session_state.themes["refreshed"] = False

def theme_selector():
    btn_face = st.session_state.themes["light"]["button_face"] if st.session_state.themes["current_theme"] == "light" else st.session_state.themes["dark"]["button_face"]
    st.sidebar.button(f'Clique para alterar o tema ' + btn_face, on_click=ChangeTheme)

    if st.session_state.themes["refreshed"] == False:
        st.session_state.themes["refreshed"] = True
        try:
            st.experimental_rerun()
        except: AttributeError
