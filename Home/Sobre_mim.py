import streamlit as st
from PIL import Image

def load_assets():
    assets = {}
    assets['falkzera'] = Image.open("image/falkzera.png")
    return assets

def display_profile():
    # Carregar os ativos
    assets = load_assets()

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

if __name__ == "__main__":
    display_profile()