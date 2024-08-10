import streamlit as st

ms = st.session_state
if "themes" not in ms: 
    ms.themes = {
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
}}

def ChangeTheme():
    previous_theme = ms.themes["current_theme"]
    tdict = ms.themes["light"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]
    for vkey, vval in tdict.items(): 
        if vkey.startswith("theme"): 
            st._config.set_option(vkey, vval)

    ms.themes["refreshed"] = False
    if previous_theme == "dark": 
        ms.themes["current_theme"] = "light"
    elif previous_theme == "light": 
        ms.themes["current_theme"] = "dark"

def theme_selector():
    btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
    st.sidebar.button(btn_face, on_click=ChangeTheme)

    if ms.themes["refreshed"] == False:
        ms.themes["refreshed"] = True
        st.rerun()

if __name__ == "__main__":
    theme_selector()