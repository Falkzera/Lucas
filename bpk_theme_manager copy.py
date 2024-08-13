import streamlit as st

# Inicializar o tema no session_state se não estiver presente
if "themes" not in st.session_state: 
    st.session_state.themes = {
        "current_theme": "light",
        "refreshed": True,
        "light": {
            "theme.base": "light",
            "theme.backgroundColor": "#FFFFFF",  # Cor de fundo padrão para o tema claro
            "theme.primaryColor": "#F63366",     # Cor primária padrão para o tema claro
            "theme.secondaryBackgroundColor": "#F0F2F6",  # Cor de fundo secundária padrão para o tema claro
            "theme.textColor": "#000000",        # Cor do texto padrão para o tema claro
            "button_face": "🌞"
        },
        "dark": {
            "theme.base": "dark",
            "theme.backgroundColor": "#0E1117",  # Cor de fundo padrão para o tema escuro
            "theme.primaryColor": "#1E90FF",     # Cor primária padrão para o tema escuro
            "theme.secondaryBackgroundColor": "#262730",  # Cor de fundo secundária padrão para o tema escuro
            "theme.textColor": "#FFFFFF",        # Cor do texto padrão para o tema escuro
            "button_face": "🌜"
        },
    }

def ChangeTheme():
    previous_theme = st.session_state.themes["current_theme"]
    tdict = st.session_state.themes["light"] if st.session_state.themes["current_theme"] == "light" else st.session_state.themes["dark"]
    for vkey, vval in tdict.items(): 
        if vkey.startswith("theme"): 
            st._config.set_option(vkey, vval)

    st.session_state.themes["refreshed"] = False
    if previous_theme == "dark": 
        st.session_state.themes["current_theme"] = "light"
    elif previous_theme == "light": 
        st.session_state.themes["current_theme"] = "dark"

def theme_selector():
    btn_face = st.session_state.themes["light"]["button_face"] if st.session_state.themes["current_theme"] == "light" else st.session_state.themes["dark"]["button_face"]
    st.sidebar.button(btn_face, on_click=ChangeTheme)

    if st.session_state.themes["refreshed"] == False:
        st.session_state.themes["refreshed"] = True
        try:
            st.experimental_rerun()
        except: # Aparentemente é um erro de atributo. Que não impede a funcionalidade.
            pass

if __name__ == "__main__":
    theme_selector()